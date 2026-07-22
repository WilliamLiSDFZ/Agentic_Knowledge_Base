# Measuring and Addressing Indexical Bias in Information Retrieval

**Source**: https://aclanthology.org/2024.findings-acl.763/

## [POSITIVE] DUO Bias Metric
Discounted Uniformity of Opinions - an unsupervised metric measuring variance of perspectives at different ranks within ordered retrieved documents, using PCA over document embeddings to compute polarization scores

**Delta**: Spearman correlations of 0.80 and 0.83 with supervised metrics rND and rKL respectively
**Condition**: Evaluating indexical bias in IR systems across diverse unlabeled corpora

**Evidence**: "DUO highly correlates with the supervised metrics rND and rKL, with Spearman correlations of 0.80 and 0.83 respectively (p < 0.05). Thus DUO gives us similar conclusions about model bias without the need for human annotation."

## [POSITIVE] PCA-based Polarization Scoring
Using Principal Component Analysis over document embeddings from a synthetic corpus to project documents onto a scalar polarization axis for each query/topic

**Delta**: Best accuracy 95.27%, mean accuracy 85.54%, median 85.70%
**Condition**: Partitioning polarized documents into contrasting viewpoint subsets

**Evidence**: "Table 2: Polarization score accuracies for the worst, best, median, and mean performance among all 124 evaluated models. High mean and best performances validate our approach."

## [POSITIVE] sentence-t5-xl Embedding Model
Using the sentence-t5-xl transformer-based document encoder as the embedding model for DUO computation

**Delta**: Best accuracy 95.27% vs worst 73.19%
**Condition**: Among 124 evaluated Sentence BERT models for polarization score accuracy

**Evidence**: "Best: sentence-t5-xl 95.27%"

## [NEGATIVE] clip-ViT-B-32-multilingual-v1 Embedding Model
Using the clip-ViT-B-32-multilingual-v1 model as the document encoder for DUO computation

**Delta**: Worst accuracy 73.19% vs best 95.27%
**Condition**: Among 124 evaluated Sentence BERT models for polarization score accuracy

**Evidence**: "Worst: clip-ViT-B-32-multilingual-v1 73.19%"

## [POSITIVE] Synthetic Corpus Generation via GPT-3.5 Turbo
Prompting GPT-3.5 Turbo to generate polarized documents arguing each side of a debate question, producing 32k synthetic documents across 3,996 queries

**Delta**: Human raters scored documents 4.9/5 faithfulness, 4.9/5 coherence, 4.7/5 relevance, 4.9/5 fluency on average
**Condition**: Creating WIKI-BALANCESynthetic corpus for bias evaluation

**Evidence**: "Annotators also score our synthetic documents for faithfulness, coherence, relevance, and fluency, showing that they are high in each of these respects."

## [POSITIVE] WIKI-BALANCESynthetic as Surrogate for Natural Evaluation
Using synthetic polarized documents as a proxy/stress test for evaluating IR system bias instead of natural web documents

**Delta**: Spearman correlation of 0.64 between synthetic and natural DUO scores
**Condition**: Cross-domain bias auditing of IR systems when natural data is unavailable

**Evidence**: "Model bias on the synthetic corpus also weakly predicts its bias on the natural corpus, with a strong Spearman correlation of 0.64 between synthetic and natural DUO scores."

## [NEGATIVE] SPLADE Retrieval Model
Sparse lexical and expansion model for first stage ranking used as an IR system in bias audits

**Delta**: DUO=0.62 (most biased in natural setting) despite highest relevance scores
**Condition**: Natural corpus evaluation of indexical bias vs. relevance tradeoff

**Evidence**: "Although SPLADE produces the most relevant results, it also introduces the most indexical bias in the natural evaluation setting (DUO=0.62)."

## [POSITIVE] Use-QA Retrieval Model
Dense retrieval model used as an IR system in bias audits

**Delta**: DUO=0.64 (natural), DUO=0.57 (synthetic) - least biased open-source model
**Condition**: Bias evaluation across both synthetic and natural corpora

**Evidence**: "Use-QA is the least relevant model, yet it produces the least biased rankings in both the natural and synthetic evaluation (DUO=0.64, 0.57)."

## [NEGATIVE] ANCE Retrieval Model
Dense retrieval model (Approximate Nearest Neighbor Negative Contrastive Estimation) used as an IR system in bias audits

**Delta**: DUO>=0.61 (synthetic), rKL>=0.62 - most biased dense model
**Condition**: Bias evaluation across both synthetic and natural corpora

**Evidence**: "The most biased models are ANCE and SBERT (DUO>=0.61; rKL>=0.62). ANCE remains the most biased model."

## [NEGATIVE] SBERT Retrieval Model
Sentence-BERT dense retrieval model used as an IR system in bias audits

**Delta**: DUO>=0.61 (synthetic), rKL>=0.62; specifically struggles with psychiatry, entertainment, and environment domains
**Condition**: Bias evaluation across both synthetic and natural corpora, especially in psychiatry, entertainment, and environment domains

**Evidence**: "SBERT, one of the most overall biased models, specifically struggles with psychiatry, entertainment, and the environment."

## [POSITIVE] BM25 Lexical Baseline
Traditional lexical retrieval model used as a baseline in bias and relevance audits

**Delta**: Strongest relevance baseline, beating more complex models like ANCE and SPARTA
**Condition**: Relevance evaluation on WIKI-BALANCE corpora

**Evidence**: "BM-25 is the strongest baseline for relevant retrieval on both WIKI-BALANCE corpora, and that BM-25 beats out models of greater complexity like ANCE and SPARTA."

## [POSITIVE] Google Search (Commercial)
Industrial search engine evaluated as a reference system in bias audits on natural web data

**Delta**: DUO=0.63 - least biased overall; outperforms best open-source model Use-QA in most domains
**Condition**: Natural corpus bias evaluation; not applicable to synthetic corpus

**Evidence**: "Google search is the least biased overall (DUO=0.63)."

## [POSITIVE] Unsupervised Approach (No Stance Classifiers)
Avoiding zero-shot LLM stance/ideology detection in favor of fully unsupervised statistics over generative models

**Delta**: Enables cross-domain evaluation without manual annotation
**Condition**: Measuring indexical bias across diverse controversial topics without curated labels

**Evidence**: "We also opt not to use zero-shot ideology and stance detection, as LLM performance still varies widely in this domain (Ziems et al., 2023). Instead, we take a fully unsupervised approach and use statistics over generative models."

## [POSITIVE] Article Click-Through Filtering in Behavioral Study
Restricting SEME regression analysis to only participants who clicked at least one search result link

**Delta**: p<0.05, R^2>0.48 for clicked subset vs. p=0.253-0.673 for all participants
**Condition**: Validating DUO as predictive of SEME in behavioral study

**Evidence**: "When we limit our regression to only those trials where a user clicked at least one link (Behavior: Clicked), we can reject the null hypothesis with statistical significance. So only in cases of article click-through, DUO significantly helps predict the Search Engine Manipulation Effect with an R2 effect size greater than 0.48 in both the Natural and Combined corpora, p<0.05."

## [POSITIVE] Natural Corpus Evaluation
Evaluating IR systems on real web documents scraped from Google Search results rather than synthetic documents

**Delta**: Higher click-through rate (50% vs 10%), more realistic bias distribution, significant SEME prediction (p<0.05)
**Condition**: Behavioral study validation and realistic IR system evaluation

**Evidence**: "With Synthetic, 10% of users clicked at least one article, while in the Natural, half of users clicked at least one article... natural data remains the gold standard and should not be replaced by synthetic evaluations alone."

## [NEUTRAL] Discounted Cumulative Gain (DCG) Framework for Bias
Adapting the DCG framework with log-based rank discounting to measure positional bias, normalizing to [0,1] range

**Delta**: Standard approach in IR; log-based decay may not exactly reflect user attention
**Condition**: Foundational framework for all positional bias metrics including rND, rKL, and DUO

**Evidence**: "Although log-based decay may not exactly reflect user attention (Ghosh et al., 2021; Sapiezynski et al., 2019), this has become the standard in IR."

## [NEGATIVE] rND and rKL Supervised Bias Metrics
Prior fairness metrics based on statistical parity and KL divergence of protected group visibility, requiring document polarization labels

**Delta**: Not applicable to natural corpus or unlabeled settings
**Condition**: Evaluation on WIKI-BALANCENatural or any unlabeled corpus

**Evidence**: "rND and rKL can be used only in cases where document polarization labels are known... Option (1) is not scalable, especially with thousands of distinct axes of controversy."

## [POSITIVE] Domain-Level Bias Decomposition
Breaking down aggregate bias results by topical domain (15 domains) to identify specific weaknesses in IR systems

**Delta**: Use-QA shows +0.12 more bias than Google in Psychiatry, +0.06 in Politics, +0.05 in Law
**Condition**: Identifying entry points for targeted bias mitigation in specific domains

**Evidence**: "PAIR can serve as a precise instrument for diagnosing and addressing localized indexical biases... The best open model, Use-QA, still falls short of Google Search in three key domains: Psychiatry (+0.12 more bias than Google), Politics (+0.06 DUO), and Law (+0.05 DUO)."

## [NEUTRAL] Stochastic Approximation for DUO Normalization
Using stochastic approximation to reduce the computational cost of DUO metric normalization

**Delta**: Reduces computation but code could be further optimized
**Condition**: Practical deployment of DUO in reranking applications

**Evidence**: "One other bottleneck that may prevent the widespread adoption of DUO in reranking is the expensive computation for normalization. Our code includes a stochastic approximation, but the code could be further optimized."

## [POSITIVE] ColBERT Late-Interaction Model
Late-interaction retrieval model evaluated for both relevance and bias in IR audits

**Delta**: Top relevance scores on WIKI-BALANCESynthetic; DUO=0.60 (mid-range bias)
**Condition**: Relevance evaluation on synthetic corpus

**Evidence**: "ColBERT also achieves the top relevance scores on the WIKI-BALANCESynthetic corpus, which also aligns with Thakur et al. (2021) and sanity-checks our results."

## [POSITIVE] OpenAI Moderation API Safety Filtering
Using OpenAI Moderation API to screen synthetic documents for toxic, harmful, or unsafe content

**Delta**: No document contains hate, harassment, self-harm, or sexual content with confidence >0.09
**Condition**: Quality and safety assurance for WIKI-BALANCESynthetic corpus

**Evidence**: "Using the OpenAI Moderation API, we determine that no document contains hate, harassment, self-harm, or unwarranted sexual content with a model confidence score larger than 0.09."

## [POSITIVE] Wikipedia Edit-War Topics as Seeds
Using Wikipedia articles with oscillatory edit patterns (edit wars, NPOV disputes) as seed topics for controversial issue identification

**Delta**: 1,364 controversial topics across 15 domains; human raters scored queries 4.5/5 relevance and 4.1/5 subjectivity on average
**Condition**: Seeding the WIKI-BALANCE corpus with genuinely controversial topics

**Evidence**: "WIKI-BALANCE reflects 1,364 of the most controversial topics from English Wikipedia... High-level seed topics come from the titles of Wikipedia articles that were edited in an oscillatory manner."

## [POSITIVE] Signed DUO (µ+DUO)
A signed version of DUO that captures the direction of bias (toward which perspective) in addition to its magnitude

**Delta**: Enables regression predicting opinion shift direction in SEME behavioral study
**Condition**: Behavioral study regression predicting directional opinion shift

**Evidence**: "µ+DUO is a signed copy of DUO (see Appendix A.2 for a derivation), which by default measures only the magnitude of the bias and not its direction. We need a sign to indicate the direction of the bias because we expect that shift will move towards the favored perspective."
