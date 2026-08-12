# 方法论:面向 MCGS 机器学习工程 agent 的论文知识库

本文描述系统实际的做法,详细程度以「能与其他知识增强型数据科学 agent 逐条对比」为标准
(对比对象见 `related_work.md`)。撰写于 2026-08-07,对应当前代码,参数值为已提交的默认值。

系统横跨两个仓库:

- **`Agentic_Knowledge_Base`(AKB)** —— 离线语料构建。抓取会议论文、聚类成主题类目,
  产出两种检索产物。
- **`MLEvolve`** —— agent 本体。对 MLE-bench(Kaggle)竞赛做候选解树的蒙特卡洛图搜索
  (MCGS),在冷启动时消费知识库。

---

## 1. 语料构建(离线)

### 1.1 抓取 —— `scripts/1_fetch.py`

每个来源一个 fetcher 模块,统一继承 `ConferenceFetcher`,返回统一的论文字典
(`title`、`abstract`、`url`、`pdf_url`、`id`、`venue`、`year`)。

| 会议 | 来源 | 方式 |
|---|---|---|
| NeurIPS、ICML | 官方 proceedings | HTML 抓取 |
| CVPR、ICCV | openaccess.thecvf.com | HTML 抓取(共用 `CVFFetcher`) |
| ACL、NAACL | ACL Anthology | Anthology 解析(共用 `ACLFetcher`) |
| ICLR | OpenReview API | 需要账号密码 |
| AAAI | Semantic Scholar | API |

输出 `cache/{venue}_{year}_papers.json`。**此阶段只收标题和摘要,不取全文。**

### 1.2 聚类与命名 —— `scripts/2_embed_cluster.py`

- 嵌入:`all-MiniLM-L6-v2`(384 维),输入 `"{title}. {abstract}"`,batch 64。
- 聚类:`AgglomerativeClustering(n_clusters=80, metric="cosine", linkage="average")`,
  直接作用于原始嵌入矩阵(未归一化、未降维)。**固定 k,不是距离阈值。**
- 命名:每个簇取前 20 个标题喂给 LLM,返回 3–7 词、小写、连字符分隔的类目名
  (`max_tokens=64`)。
- 重名处理:若两个簇生成了同一个名字,第二个簇的索引会**追加**到第一个上,而不是覆盖。
  因此实际类目数可能少于 80。

输出 `cache/{venue}_{year}_clusters.json` —— `{类目名: [论文索引]}`。

### 1.3 重分类 —— `scripts/3_classify.py`

1.2 的归属是几何意义上的;本步用 LLM 针对**已命名**的类目词表重新判断,同时支持多标签。

- 分批:每次 30 篇,8 线程并发。
- 每篇渲染为 `[{i}] {title}\n{abstract[:300]}` —— 摘要**截断到 300 字符**。
- 模型每篇返回一行:`[n] CATS:1,3 | TAGS:a,b,c | TLDR:一句话摘要`。
- `max_tokens = max(1024, 110 × 批大小)`。固定 1024 会静默截断批次尾部。
- **对齐保护:** 输出行按显式的 `[n]` 索引回填,不按位置。因此漏一行、多一行或乱序都不会
  让别的论文标签串位;未匹配到的论文标记 `unparsed` 并给一个兜底类目。
- 指数退避 + 抖动重试;每 10 批做一次稀疏检查点,中断可续跑。

输出 `cache/{venue}_{year}_classified.json`,保持原始论文顺序。

### 1.4 生成主题技能 —— `scripts/4_generate_skills.py`

```
output/{venue}-{year}/{category}/SKILL.md
output/{venue}-{year}/{category}/references/{paper-slug}.md
```

`SKILL.md` 内含 LLM 写的 1–2 句类目描述(由前 15 个标题生成)和索引表
`| # | Title | Tags | File |`。每个 `references/*.md` 是 YAML frontmatter
(`title`、`source`、`pdf_url`、`categories`、`tags`、`venue`、`tldr`)加**完整摘要**。
多标签论文会写进它所属的每一个类目。同类目内文件名冲突加后缀 `-1`、`-2`……

这个目录作为产品提交进 git;`cache/` 是临时目录。

### 1.5 摘要索引 —— `scripts/6_build_abstract_index.py`

运行时真正使用的检索产物,**零 LLM 调用**。

- 每个 `(venue, paper)` 一条记录;跨多个类目的论文以第一个为主类目(决定抽取缓存路径),
  其余记入列表。
- `embed_text = "{title}. {tldr} {abstract[:2000]}"`。
- 嵌入:`BAAI/bge-m3`,归一化。
- 输出:`records.jsonl`、`embeddings.npy`(float32,行对齐)、`manifest.json`
  (`embedding_model`、`dim`、`count`、`venues`、`schema_version`)。manifest 是契约 ——
  查询模型与索引模型不一致时检索直接拒绝运行。

### 1.6 深度抽取 —— `scripts/plugin_a_methodology.py`

把 PDF 变成结构化技术清单,这是**最贵的一步**。

- PDF 地址解析,按优先级:fetcher 抓到的 `pdf_url` 字段 → `aclanthology.org` 地址加
  `.pdf` → OpenReview forum id → `https://openreview.net/pdf?id={id}`。解析不出的论文跳过。
- 正文:`pymupdf4llm.to_markdown(...)`,截断到 **64,000 字符**。
- 每篇一次 LLM 调用(`temperature=0`),返回 JSON:

  ```
  {"techniques": [{name, description, effect: positive|negative|neutral,
                   delta, evidence(原文引用), condition}]}
  ```

- 渲染为 `methodology_kb/{venue}-{year}/{category}/{stem}_methodology.md`,每个技术一节
  `## [POSITIVE|NEGATIVE|NEUTRAL] {name}`,附 `**Delta**`、`**Condition**` 和带引号的
  `**Evidence**`。

positive/negative/neutral 这个标注是承重的设计决策:**只有 `[POSITIVE]` 段落会被注入**,
所以抽取器同时充当了一道过滤器,依据是论文自己报告的消融结果。

### 1.7 跨论文综合 —— `scripts/plugin_a2_insighter.py`

一个 LLM **工具调用 agent**(工具:`list_files`、`read_file`、`write_file`、`git_commit`;
`MAX_TURNS = 60`,工具输出截断到 64,000 字符)读完一个类目下所有 `*_methodology.md`,
写出的每条洞察必须**引用至少两篇论文**并附原文引用。单篇论文的观察明确不算洞察。
agent 被要求在收尾前做一遍自审,删掉牵强的洞察。每条洞察带 `HIGH`/`MEDIUM`/`LOW` 置信度。

输出 `methodology_kb/paperinsight/{venue}-{year}/{category}/insight.md` 及 `references/`。

`scripts/5_build_methodology.py` 把 1.6 和 1.7 串起来并发跑:论文级 8 线程,类目级 3 线程,
可续跑(已存在的输出直接跳过),最后统一提交一次 git(agent 内部的 git 被禁用,避免并发提交
冲突)。

### 1.8 经验知识库 —— `plugin_b_experience.py`、`plugin_c_dreamer.py`

第二套结构上完全独立的知识库,来源不是论文,而是 agent **自己的训练运行日志**。

- **Plugin B** 读入一个 run 目录的 `judge_*/output.json` 和 `designer*/output.json`,
  抽出三个文件:`wins.md`(有正面结果的技术)、`failures.md`(报错、依赖阻塞、错误假设)、
  `hypotheses.md`(已证实 / 已证伪 / 未验证)。每条主张必须引用来源节点和原文。新条目会用
  LLM 与现有文件去重(严格二选一:skip 或 add,**不合并**)。每个 run 开一个 git 分支;
  并行 run 之间的合并冲突由 LLM 判定冲突类型(`direct_contradiction` /
  `condition_difference` / `environment_factor` / `sample_size`)并写出调和后的条目,
  留审计日志。
- **Plugin C(“dreamer”)** 做睡眠期的巩固与遗忘:合并重复条目(`Seen` 计数相加)、
  提炼 2–5 条元洞察,然后让条目老化退场。条目在 `dreamer_runs ≥ 10 + (seen − 1)` 时成为
  归档候选 —— **每多被看到一次就多活一轮** —— 每个文件每轮最多 3 个候选,最终由 LLM 决定
  保留还是归档。归档条目在 `archived_runs = 5` 时永久删除。`seen=1` 的条目最短寿命是
  14 个 dreamer 轮次。

**这半套系统从未进入过任何实验臂。** 下文所有 A/B 结果只用了 `methodology_kb`。

### 1.9 LLM 接入

AKB 的所有 chat completion 走 `scripts/llm.py`:单一 `OpenAI` 客户端指向 OpenAI 兼容端点,
由 `LLM_BASE_URL` / `LLM_MODEL` / `LLM_API_KEY` 配置,默认 OpenRouter +
`anthropic/claude-sonnet-4.6`。嵌入在本地跑(`sentence-transformers`),所以只有 chat
产生费用。**一个模型服务所有阶段** —— 簇命名、分类、技能描述、抽取、综合、去重、冲突解决、
巩固、遗忘。没有任何按阶段选模型的逻辑。

---

## 2. 冷启动检索(在线)

`run.py` 在搜索开始**之前**调用一次 `build_guidance_description(cfg, task_desc)`,
结果存入 `cfg.coldstart.description`。

### 2.1 四种模式

`methodology_retrieval` 在以下之间切换:

| 模式 | 机制 |
|---|---|
| `static` | 手工维护的 `methodology_map.json`,竞赛 id → 类目文件夹 |
| `llm` | 把所有类目**名字**给 LLM,让它挑 ≤5 个,读这些类目的 HIGH 置信度引用 |
| `vector` | 在预构建的洞察索引上做混合检索(一条洞察一条记录) |
| `lazy` | 摘要级检索 + 按需深度抽取(**当前实验使用的默认模式**) |

`llm` 是最初的设计。它的弱点在于:一个类目名是对约 50 篇论文极其有损的表示,而且无论任务
如何都固定砍到 5 个。`vector` 和 `lazy` 就是为了取代它而建的。

### 2.2 lazy 模式逐步拆解

这是所报告实验实际运行的路径。

**第 1 步 —— 查询蒸馏。** 一次 LLM 调用把竞赛描述压缩成 50–80 词的机器学习任务陈述,
覆盖输入数据类型与规模、任务类型、评价指标、可能起作用的建模技术;奖金、时间线、文件清单、
叙事性文字明确排除。结果按 `sha1(描述)[:16]` 缓存到磁盘,**一个任务只蒸馏一次,A/B 两臂
复用逐字节相同的查询**。

为什么用 LLM 而不是规则:先实现的是基于标题的规则抽取器,**不泛化**。OpenADMET 的信号在
末尾的「数据特性」一节;spooky-author-identification 的信号在 "Evaluation" 一节 ——
而规则恰好把它丢掉了,只剩恐怖小说的氛围描写。实测 top-10 命中:原始描述 2/10、规则抽取
0/10、蒸馏 9/10。

**第 2 步 —— 摘要检索。** `HybridRetriever`(BM25 + FAISS,用 Reciprocal Rank Fusion 合并,
`alpha = 0.5`)返回 `lazy_pool = 40` 个候选。相对分数阈值**故意设得很低**
(`lazy_min_score = 0.05`):这一阶段以召回为导向,因为抽取成本在下游有硬上限,精度在第 4 步
再找回来。

**均值中心化。** 索引向量和查询向量在使用前都做均值中心化。同质语料的句嵌入**各向异性很强**
—— 每个向量都包含一个巨大的「这是一篇机器学习论文」共同分量,主导了余弦相似度、压制了主题
信号。本语料实测:中心化前 top-10 分数跨度 0.017、命中 5/10;中心化后跨度 0.048、命中 8/10。
均值在运行时从已加载的向量算出,**无需重建索引**。中心化通过包装嵌入模型实现,BM25 那一半
不受影响。

**第 3 步 —— 按需抽取。** 候选分为已缓存(`*_methodology.md` 已存在)和缺失两类。**当场**
抽取至多 `max_extractions_per_coldstart = 20` 篇缺失论文,复用 plugin A 的逻辑
(下载 PDF → pymupdf → 一次 LLM 调用),4 线程,写入标准 `methodology_kb` 布局。缓存是永久的,
与批处理流水线共享,因此单任务成本随缓存变热**摊薄趋近于零**。

**第 4 步 —— 技术级重排**(`lazy_technique_rerank`,默认开)。把可用论文的所有 `[POSITIVE]`
段落拆成独立技术,每条以 `"{技术标题}\n{正文[:800]}"` 用与索引相同的模型嵌入(模型已在内存里,
零额外开销),按与**蒸馏后查询**的余弦相似度排序。相对最高分低于
`lazy_tech_min_score = 0.3` 的丢弃,标题近重复的去掉,保留前 `lazy_tech_top_n = 12` 条。

这一步存在的理由:第 2 步是论文级且面向召回,一篇相关论文里通常有若干**不相关的技术**,
只有这一步能把它们过滤掉。开关设为 `False` 则退回按第 1 阶段分数注入整篇论文的 `[POSITIVE]`
段落。

**第 5 步 —— 组装。** 选中的技术在 `retr_token_budget = 6000` token(约 24,000 字符)预算内
拼接,每块带来源论文标注,置于标题 *"Methodology Insights from Literature"* 之下。

### 2.3 注入点

组装好的文本追加到冷启动 guidance,最终**只在一个地方**进入模型:`draft_agent`,作为草案策略
中的 **"Option A [RECOMMENDED]"** 呈现(`stepwise_coder` 读同一个字段)。它**不会**进入
`improve_agent`、`debug_agent`、`evolution_agent`、`fusion_agent` 或 `aggregation_agent`。

对结果解释的影响:知识库只能影响**初始解**。之后全是普通搜索。12 小时的运行里
`initial_drafts = 3`,总节点 14–19 个,**KB 的因果作用面很窄**,任何可测效应都是通过
「搜索从哪些分支起步」传导的,而不是逐步指导。

---

## 3. 成本模型

| 项目 | 成本 |
|---|---|
| 摘要索引构建 | 仅本地嵌入,无 API |
| 查询蒸馏 | 每个不同竞赛 1 次 LLM 调用,永久缓存 |
| 检索 | 本地(FAISS + BM25),无 API |
| 深度抽取 | 每次冷启动 ≤20 次 LLM 调用 + 20 次 PDF 下载,逐步摊薄到 0 |
| 技术重排 | 本地嵌入,模型已在内存 |

设计目标是:缓存热起来之后,开启 KB 的运行的边际成本趋近于零 —— 这正是重复 A/B 实验负担得起
的前提。

## 4. 参数速查

| 参数 | 默认值 | 阶段 |
|---|---|---|
| `N_CLUSTERS` | 80 | 聚类 |
| 分类批大小 / 线程 | 30 / 8 | 分类 |
| 摘要截断(分类时) | 300 字符 | 分类 |
| 索引嵌入模型 | `BAAI/bge-m3` | 索引 |
| PDF 正文截断 | 64,000 字符 | 抽取 |
| `lazy_pool` | 40 | 检索一阶段 |
| `lazy_min_score` | 0.05(相对) | 检索一阶段 |
| `retr_alpha`(BM25 ↔ 稠密) | 0.5 | 检索一阶段 |
| `retr_center_embeddings` | `True` | 检索一阶段 |
| `retr_query_mode` | `llm` | 查询 |
| `max_extractions_per_coldstart` | 20 | 抽取 |
| `lazy_extract_workers` | 4 | 抽取 |
| `lazy_technique_rerank` | `True` | 检索二阶段 |
| `lazy_tech_min_score` | 0.3(相对) | 检索二阶段 |
| `lazy_tech_top_n` | 12 | 检索二阶段 |
| `retr_token_budget` | 6000 token | 组装 |

---

## 5. 评测协议

**基准。** MLE-bench 竞赛,用官方私有答案打分。`mlebench grade-sample` 会先算分、再拿内置的
`leaderboard.csv` 排名;其中若干文件是以 git-LFS 指针存根的形式安装的,导致**分数已经算出来
之后**排名步骤崩溃。`MLEvolve/utils/grade_local.py` 做同样的打分调用,但把排行榜当作可选项,
支持传目录,并提供 `--cutoff-hours`,使 wall-clock 预算不等的两次运行可以在**对齐预算**下比较。

**配对 A/B。** 每个竞赛两个 Kubernetes Job,**仅** `EXTRA_RUN_ARGS` 不同
(`methodology_retrieval=lazy` 加两个 KB 路径)。镜像、CPU、内存、GPU、时间预算、模型、
seed 策略完全一致,并在发布前用脚本断言校验。

**检索门槛。** 在烧掉 12 个 GPU 小时之前,`scripts/probe_retrieval.py` 单独跑检索阶段
(秒级),报告 top-10 的对题命中数和分数**跨度**(`score(top1) − score(topK)`);跨度平坦意味着
打分器根本没在区分。事先约定的门槛是 `center=on, query=llm` 下 ≥8/10。

**选择规则。** 融合步骤会产出大小为 1、2、3、4、6 的集成。比较在**相同 K** 上进行,并报告完整
表格 —— 不取各臂自己最好的那个,那是在用测试集选模型。

## 6. 目前的结果

每臂单次运行。指标方向逐竞赛不同。

| 竞赛 | 指标 | baseline | KB | KB 效果 |
|---|---|---|---|---|
| OpenADMET ExpansionRx | 越低越好 | 0.678 | 0.741 / 0.726 | 更差 |
| spooky-author-identification | log loss,越低越好 | **0.2366**(银牌) | 0.2883(铜牌) | 每个 K 上都更差 |
| jigsaw-toxic-comment | 逐列 ROC AUC 均值,越高越好 | 0.97997(低于中位数) | **0.98503**(高于中位数) | 更好;到满分的误差降 25% |

唯一与效果符号同步变化的变量是**语料覆盖度**。对 423 个类目做关键词审计发现,覆盖竞赛手艺的
主题 —— 梯度提升、特征工程、交叉验证策略、模型融合、超参搜索、类别不平衡、缺失值 —— 合计
**49 篇,占约 2.3 万篇的 0.2%**,而理论/优化占 21%、LLM 研究占 19%。OpenADMET 只有 3/423 个
相关类目;jigsaw 有四个直接对口的类目共约 390 篇,检索门槛以 9/10 通过。

## 7. 已知局限

1. **每臂 n = 1。** MLE-bench 建议 ≥3 个 seed。三个结果全是单次运行。
2. **本地验证不可靠,而且不可靠的方式不一致。** spooky 上它正确排出了两臂顺序;jigsaw 上排反了;
   OpenADMET 上偏了约 4 倍。而 agent 内部的模型选择依赖它。
3. **注入点狭窄。** KB 只进 `draft_agent`,在改进、调试、融合阶段都帮不上忙 —— 而那是绝大多数
   搜索步骤。
4. **只有论文。** 没有 Kaggle 方案 writeup、notebook 或讨论帖。这是与 AutoMind 最清晰的结构性
   差异(见 `related_work.md`):后者的知识库以 Kaggle 方案为主,且报告了正向消融。
5. **`experience_kb` 未被使用。** 已建成、已版本化,却从未进入实验臂 —— 尽管它是唯一在 genre
   上与任务匹配的组件。
6. **覆盖不均且未逐会议记录。** 语料跨多次会话增长过(2024 与 2025 年会议、新增 ICLR),
   之后没有重新审计成分。
7. **抽取依赖 PDF。** 解析不出 PDF 地址的论文被静默跳过,使可抽取子集偏向 ACL Anthology 和
   OpenReview。
