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

已抽取的 223 篇论文实测(3,066 条技术,平均每篇 13.7 条):

| 标签 | 数量 | 占比 |
|---|---:|---:|
| POSITIVE | 2,214 | 72.2% |
| NEGATIVE | 530 | 17.3% |
| NEUTRAL | 322 | 10.5% |

两个推论。第一,**27.8% 的抽取产出从未被任何代码读取** —— 生成了、存了、没用过。第二,更要紧的是
**`[NEGATIVE]` 并不表示「这个技术不好」**。逐条检查后可以看到,这个标签把三种完全不同的情况
压成了一类:

1. 作者试过、发现无益的组件 —— 这是真正有用的负面知识;
2. **在该论文数据集上落败的基线或对照方法**(例如 Reflexion prompting 被标为 NEGATIVE,
   只是因为该论文自己的方法赢了它)—— 具有误导性;
3. 主方法的某个消融维度只是没能拿到最好成绩。

第 (2) 类使得「把 `[NEGATIVE]` 当作『别做什么』注入」变得危险:agent 会学到一批本身完全没问题
的方法是坏的,仅仅因为它们输过一次比较。要用这批材料,得先改抽取 prompt,把「作者试了有害」和
「它是对照组」分成两个标签。

72.2% 这个 POSITIVE 占比本身就是偏差信号:论文是为自己的贡献辩护而写的,所以 POSITIVE 追踪的是
**这篇论文主张什么**,而不是**什么被独立验证过**。

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

**每种模式消费的是哪一层,很关键而且容易看漏。** `llm` 和 `vector` 读的是 §1.7 的跨论文洞察
(`paperinsight/*/insight.md`);`static` 和 `lazy` 读的是 §1.6 的逐篇技术文件
(`*_methodology.md`)。由于 §6 的每一次实验都跑在 `lazy` 模式下,**跨论文综合层从未参与过任何
实验**。这是成本决策而非设计决策 —— `vector` 要求相关类目事先跑过 plugin A 和 A2,而仓库当前
有 223 份 `*_methodology.md`、只有 2 份 `insight.md`,对这些任务而言洞察覆盖率接近于零。
后果是「洞察级检索 vs 技术级检索」成了一个未经检验的对比,而这个对比 AutoMind 也做不了 ——
它的检索粒度是论文级。

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

`run.py` 调用一次构建器,把结果存到配置上。技术随后以自己的标题
*"Techniques from recent literature"* 进入 `draft_agent`,措辞是「待评估的假设」而不是
「照抄的配方」。打开 `coldstart.inject_into_improve`(默认**关**)后,它们还会进入
`improve_agent`,截断到 `coldstart.improve_token_budget` = 2000 token,并**放在策略区块之前**
——这样 plateau 分支里那句既有的 "refer to the expert technique suggestions above"(此前是
一句悬空引用)才成立。它们始终不会进入 `debug_agent`、`evolution_agent`、`fusion_agent` 或
`aggregation_agent`。

对结果解释的影响:只在 draft 注入时,知识库只能影响**初始解**。12 小时的运行里
`initial_drafts = 3`、总节点 14–19 个,**KB 的因果作用面不到搜索的 20%,且全在最开头**,任何
可测效应都是通过「搜索从哪些分支起步」传导的,而不是逐步指导。

#### 一处使下文所有实验的接线失效的缺陷

2026-08-08 之前,检索到的技术是被**字符串拼接**到预训练模型 guidance 上、作为同一个值返回的,
而 `draft_agent` 把它插值进了下面这个区块的**中间**:

```
• **Option A [RECOMMENDED]**: {coldstart_description}
  → SOTA models with proven performance. Use for end-to-end fine-tuning OR as frozen …
  …
**CRITICAL: When using any recommended pretrained model (Option A), you MUST copy the Code
template EXACTLY as provided …**
```

四个后果,§6 报告的每一次运行都带着它们:

1. 技术落在 "Option A:" 和「这些是经过验证的 SOTA 模型」之间,于是**散文式的技术描述被标注成
   了推荐的预训练模型**。
2. 「必须逐字复制 Code template」这条指令覆盖到了它们,而技术描述里根本没有代码模板 ——
   一条无法执行的指令。
3. 一条 `---` 分隔线和一个 `##` 二级标题被插进项目符号列表中间,`Option B`、`Option C`
   变成了那个标题的下属内容。
4. **`"None model"` 哨兵被击穿。** `draft_agent` 用 `coldstart_description != "None model"`
   来决定是否渲染整个区块,而当竞赛没有预训练模型条目时 `_build_guidance_text` 恰好返回这个值。
   拼上技术文本后等式不再成立,于是区块被激活 —— **而且只在 KB 组**,因为对照组的技术文本为空。
   两组因此相差的不只是知识,还有**一整段预训练模型指令**。这是混淆变量,不只是排版难看,而且
   它恰好作用在文本类任务上 —— spooky 和 jigsaw 都是。

修复方式是把两者分开:`build_guidance_description` 只返回模型 guidance,技术写入
`cfg.coldstart.methodology_text`。`utils/verify_kb_injection.py` 对以上各点(含哨兵已恢复)
逐条做了断言。

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
| `coldstart.inject_into_improve` | `False` | 注入面 |
| `coldstart.improve_token_budget` | 2000 token | 组装(improve) |
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

*「对题」是冒烟测试,不是 IR 指标。* 它统计的是 top-10 里**标题**包含任一关键词的论文数,而关键词
是逐任务手工给的。因此它会漏掉标题不含关键词的相关论文,**完全看不出一篇论文是否「有用」而不只是
「对题」**,而且关键词是看过任务之后才选的,并非预注册。它足以抓住「查询返回一堆无关 ML 论文」这类
故障 —— 这正是它存在的目的 —— 但不构成可发表意义上的检索质量证据。

**选择规则。** 融合步骤会产出大小为 1、2、3、4、6 的集成。比较在**相同 K** 上进行,并报告完整
表格 —— 不取各臂自己最好的那个,那是在用测试集选模型。

**统计功效。** 在 jigsaw 上,两臂配对差值跨重复的 sd ≈ 0.006 AUC。在 80% 功效、α = 0.05 下,
检测 0.005 的效应约需 12 组配对,0.003 需 31 组,0.002 需 70 组 —— 按 12 小时/次折算分别是
288、744、1680 个 GPU 小时。**单任务上小于约 0.005 的效应在当前协议下测不起。** AutoMind 通过
在 15 个任务 × 3 次运行上聚合 win rate 而非报告单任务原始指标来规避这个问题。

## 6. 目前的结果

**下列全部运行都使用了 §2.3 所述的缺陷接线**,需要重新测量。指标方向逐竞赛不同。

| 竞赛 | 指标 | 每臂 n | baseline | KB | KB 效果 |
|---|---|---|---|---|---|
| OpenADMET ExpansionRx | 越低越好 | 1 | 0.678 | 0.741 / 0.726 | 更差 |
| spooky-author-identification | log loss,越低越好 | 1 | **0.2366**(银牌) | 0.2883(铜牌) | 每个 K 上都更差 |
| jigsaw-toxic-comment | 逐列 ROC AUC 均值,越高越好 | 3 | — | — | **无差异** |

jigsaw 各集成尺寸上的配对差值(KB − baseline):

| seed | K=1 | K=2 | K=3 | K=4 | K=6 | 均值 |
|---:|---:|---:|---:|---:|---:|---:|
| 42 | +0.00506 | +0.00482 | +0.00421 | +0.00197 | — | +0.00401 |
| 43 | +0.00021 | +0.00035 | +0.00039 | +0.00025 | −0.00002 | +0.00024 |
| 44 | −0.00679 | −0.00708 | −0.00833 | −0.00788 | −0.00910 | −0.00784 |

三次重复的均值 −0.00120,sd 0.00605,t(2) = −0.342,95% CI [−0.0162, +0.0138]。
整个系列里的最好成绩是 **baseline** 拿的金牌(seed 44,K=3,0.98748)。

关于这个方差结构有两点观察。**重复内部**,符号在各 K 上几乎完全一致(4/4、4/5、0/5),
说明**一次运行是整体地好或整体地坏** —— K 值不是独立样本,此前只看 K=1 的比较已经具有代表性。
**重复之间**,每一臂自身波动约 0.007,约为平均处理效应的 14 倍。

本文档的早期版本把 jigsaw 记为正结果。那只基于第一次重复,**未能通过复现检验**。

语料覆盖度曾是唯一与效果符号同步的变量,现在不再干净地成立。对 423 个类目做关键词审计发现,
覆盖竞赛手艺的主题 —— 梯度提升、特征工程、交叉验证策略、模型融合、超参搜索、类别不平衡、缺失值
—— 合计 **49 篇,占约 2.3 万篇的 0.2%**,而理论/优化占 21%、LLM 研究占 19%。OpenADMET 只有
3/423 个相关类目;jigsaw 有四个直接对口的类目共约 390 篇、检索门槛以 9/10 通过 —— **仍然没有
收益**。覆盖度可能是必要条件,但显然不是充分条件。

## 7. 已知局限

1. **上述每一个结果测的都是有缺陷的接线。** §2.3 那个标签错误 —— 包括 `"None model"` 哨兵被
   击穿、使两组的差异不止于知识 —— 全程存在。修复路径上的重跑尚未完成。
2. **三个任务中有两个每臂 n = 1**,jigsaw 为 3。MLE-bench 建议 ≥3,而 §5 的功效分析表明,
   面对这个量级的方差,3 次也远远不够。
3. **本地验证不可靠,而且不可靠的方式不一致。** spooky 上它正确排出了两臂顺序;jigsaw 上一次排反、
   一次排对;OpenADMET 上偏了约 4 倍。而 agent 内部的模型选择依赖它。
4. **注入点狭窄。** 2026-08-08 之前 KB 只进 `draft_agent`,在改进、调试、融合阶段都帮不上忙 ——
   而那是绝大多数搜索步骤。improve 阶段的选项现已存在,但尚未验证。
5. **只有论文。** 没有 Kaggle 方案 writeup、notebook 或讨论帖。这是与 AutoMind 最清晰的结构性
   差异(见 `related_work.md`):后者的知识库以 Kaggle 方案为主,且报告了正向消融。
6. **没有防污染机制。** AutoMind 会剔除属于目标竞赛的知识,我们没有。对论文而言不如对方案帖那么
   急迫,但 spooky(2017)和 jigsaw(2018)老到足以落在基座模型的预训练数据里,而我们没有任何
   截止日期之后的任务作为对照。
7. **跨论文洞察层从未被启用**(§2.1)。仓库里只有 2 个 `insight.md`,对应 223 份逐篇抽取。
8. **27.8% 的抽取产出是死数据**(§1.6),且 `[NEGATIVE]` 标签把「作者试了有害」和「它是落败的
   对照组」混为一谈。
9. **`experience_kb` 未被使用。** 已建成、已版本化,却从未进入实验臂。(不在本工作当前范围内。)
10. **覆盖不均且未逐会议记录。** 语料跨多次会话增长过(2024 与 2025 年会议、新增 ICLR),之后
    没有重新审计成分 —— §6 里那个 0.2% 的数字早于最近几次新增。
11. **抽取依赖 PDF。** 解析不出 PDF 地址的论文被静默跳过,使可抽取子集偏向 ACL Anthology 和
    OpenReview。
