# analogy agent — parent draft (invocation 1)

corpus 5cd1d5e7afd0 (38273 papers) | turns 6 | tokens in/out 111166/6725 | 186s | report

## Packet

# TASK (no solution has been written yet)

## Competition description (head and tail)
## Description

Can you help detect toxic comments ― *and* minimize unintended model bias? That's your challenge in this competition.

The Conversation AI team, a research initiative founded by Jigsaw and Google (both part of Alphabet), builds technology to protect voices in conversation. A main area of focus is machine learning models that can identify toxicity in online conversations, where toxicity is defined as anything *rude, disrespectful or otherwise likely to make someone leave a discussion*.

Last year, in the Toxic Comment Classification Challenge, you built multi-headed models to recognize toxicity and several subtypes of toxicity. This year's competition is a related challenge: building toxicity models that operate fairly across a diverse range of conversations.

Here's the background: When the Conversation AI team first built toxicity models, they found that the models incorrectly learned to associate the names of frequently attacked identities with toxicity. Models predicted a high likelihood of toxicity for comments containing those identities (e.g. "gay"), even when those comments were not actually toxic (such as "I am a gay woman"). This happens because training data was pulled from available sources where unfortunately, certain identities are overwhelmingly referred to in offensive ways. Training a model from data with these imbalances risks simply mirroring those biases back to users.

In this competition, you're challenged to build a model that recognizes toxicity and minimizes this type of unintended bias with respect to mentions of identities. You'll be using a dataset labeled for identity mentions and optimizing a metric designed to measure unintended bias. Develop strategies to reduce unintended bias in machine learning models, and you'll help the Conversation AI team, and the entire industry, build models that work well for a wide range of conversations.

*Disclaimer: The dataset for this competition contains text that may be considered profane, vulgar, or offensive.*

### Acknowledgments

The Conversation AI team would like to thank Civil Comments for making this dataset available publicly and the Online Hate Index Research Project at D-Lab, University of California, Berkeley, whose labeling survey/instrument informed the dataset labeling. We'd also like to thank everyone who has contributed to Conversation AI's research, especially those who took part in our last competition, the success of which led to the creation of this challenge.

## Evaluation

### Competition Evaluation

This competition will use a newly developed metric that combines several submetrics to balance overall performance with various aspects of unintended bias.

First, we'll define each submetric.

### Overall AUC

This is the ROC-AUC for the full evaluation set.

### Bias AUCs

To measure unintended bias, we again calculate the ROC-AUC, this time on three specific subsets of the test set for each identity, each capturing a different aspect of unintended bias. You can learn more about these metrics in Conversation AI's recent paper *Nuanced Metrics for Measuring Unintended Bias with Real Data in Text Classification*.

**Subgroup AUC**: Here, we restrict the data set to only the examples that mention the specific identity subgroup. *A low value in this metric means the model does a poor job of distinguishing between toxic and non-toxic comments that mention the identity*.

**BPSN (Background Positive, Subgroup Negative) AUC**: Here, we restrict the test set to the non-toxic examples that mention the identity and the toxic examples that do not. *A low value in this metric means that the model confuses non-toxic examples that mention the identity with toxic examples that do not*, likely meaning that the model predicts higher toxicity scores than it should for non-toxic examples mentioning the identity.

**BNSP (Background Negative, Subgroup Positive) AUC**: Here, we restrict the test set to the toxic examples that mention the identity and the non-toxic examples that do not. *A low value here means that the model confuses toxic examples that mention the identity with non-toxic examples that do not*, likely meaning that the model predicts lower toxicity scores than it should for toxic examples mentioning the identity.

### Generalized Mean of Bias AUCs

To combine the per-identity Bias AUCs into one overall measure, we calculate their generalized mean as defined below:

$$
M_p\left(m_s\right)=\left(\frac{1}{N} \sum_{s=1}^N m_

[... middle of the description omitted ...]

e proficient in English.

Raters were compensated 1.5 cents per judgment, a rate that was set based on two factors: what rates were competitive on the platform and targeting an hourly wage appropriate for raters' locales.

Figure Eight offers raters the option to select from multiple tasks with different pay, so rates need to be competitive to attract enough raters. At a rate of 1.5 cents per judgment, enough raters participated to complete this annotation in a few weeks. Following task completion, raters were given a satisfaction survey where the average score for "Pay" was 3.8 out of 5, which aligned with Figure Eight's recommendation to target pay to a satisfaction score greater than 3.5.

Hourly rates for workers depend on how fast judgements were completed. Most raters will have earned between $0.90/hour (at one comment per minute) to $5.40/hour (at 6 comments per minute), which aligns with typical hourly pay in the geographic regions where most raters are located.

Since this dataset was annotated in 2018, more tools have become available to help set rates. Consequently, typical pay for data annotation is increasing globally.

## File descriptions

- **train.csv** - the training set, which includes toxicity labels and subgroups
- **test.csv** - the test set, which does **not** include toxicity labels or subgroups
- **sample_submission.csv** - a sample submission file in the correct format

## Usage

This dataset is released under CC0, as is the underlying comment text.

## Available data (workspace listing / preview)
```
global_memory/

input/
    description.md (286 lines)
    sample_submission.csv (97321 lines)
    test.csv (205781 lines)
    train.csv (3820211 lines)
submission/

working/
```

-> input/sample_submission.csv has 97320 rows and 2 columns.
⚠️  IMPORTANT: This is the CORRECT submission format that must be followed!
The exact column names are: id, prediction
Any description.md format information should be IGNORED if it conflicts with this file.
Here is some information about the columns:
id (int64) has range: 7097320.00 - 7194639.00, 0 nan values
prediction (float64) has 1 unique values: [0.0]

-> input/test.csv has 97320 rows and 2 columns.
Here is some information about the columns:
comment_text (object) has 96862 unique values. Some example values: ['No.', 'Yes.', 'Well said.', 'Well said!']
id (int64) has range: 7097320.00 - 7194639.00, 0 nan values

-> input/train.csv has 1804874 rows and 45 columns.
Here is some information about the columns:
article_id (int64) has range: 2006.00 - 399541.00, 0 nan values
asian (float64) has range: 0.00 - 1.00, 1399744 nan values
atheist (float64) has range: 0.00 - 1.00, 1399744 nan values
bisexual (float64) has range: 0.00 - 1.00, 1399744 nan values
black (float64) has range: 0.00 - 1.00, 1399744 nan values
buddhist (float64) has range: 0.00 - 1.00, 1399744 nan values
christian (float64) has range: 0.00 - 1.00, 1399744 nan values
comment_text (object) has 1780822 unique values. Some example values: ['Well said.', 'No.', 'Exactly.', 'Yes.']
created_date (object) has 1804362 unique values. Some example values: ['2015-10-13 18:40:35.757707+00', '2015-09-29 20:48:48.201423+00', '2015-09-29 19:40:17.101981+00', '2015-09-29 17:54:15.971935+00']
disagree (int64) has range: 0.00 - 187.00, 0 nan values
female (float64) has range: 0.00 - 1.00, 1399744 nan values
funny (int64) has range: 0.00 - 102.00, 0 nan values
heterosexual (float64) has range: 0.00 - 1.00, 1399744 nan values
hindu (float64) has range: 0.00 - 1.00, 1399744 nan val…

## Resource budget
- search budget: 12.0 h wall clock for the whole search
- per-solution execution cap: 6.0 h
- CPU cores: 8
- GPU: NVIDIA A10, 22 GiB

## Pretrained models available offline
Model1: ModernBERT

Description:ModernBERT is a modernized bidirectional encoder-only Transformer model pre-trained on 2 trillion tokens of English and code data. It significantly improves upon the original BERT with extended context length to 8k tokens (compared to just 512 for most encoders), making it faster and more accurate. The model features architectural innovations including improved efficiency enhancements and hardware-aware design. Unlike earlier BERT models, ModernBERT does not use token type IDs, simplifying its usage while maintaining compatibility as a drop-in replacement for BERT-like models. It excels at various NLP tasks including classification, token classification, question answering, and masked language modeling.

Code template (MUST copy exactly — do NOT change model variant names or file paths):
```python
from transformers import AutoTokenizer, ModernBertForSequenceClassification, ModernBertForMaskedLM, ModernBertForTokenClassification, ModernBertForQuestionAnswering, ModernBertForMultipleChoice
from torch.optim import AdamW

model_id = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)
# Choose one model class according to your task:
# model = ModernBertForSequenceClassification.from_pretrained(model_id)  # for classification
# model = ModernBertForMaskedLM.from_pretrained(model_id)  # for masked language modeling
# model = ModernBertForTokenClassification.from_pretrained(model_id)  # for token classification/NER
# mode…


## Trace

[turn 1] assistant:
**Step 1 — structural properties**

1. **The leaderboard is driven by pairwise ranking errors on overlapping group-conditioned slices, not just global calibration/classification accuracy.**  
   - **Objects:** comment scorer; binary toxicity label; identity-membership indicator; global ROC-AUC; subgroup, BPSN, and BNSP ROC-AUCs; generalized mean aggregator.  
   - **Relations:** each bias AUC compares positives and negatives drawn from a particular cross-product of label and group membership. Standard pointwise BCE can improve global discrimination while still ranking benign group-mentioned comments above toxic background comments (BPSN failure), which is explicitly penalized; the generalized mean emphasizes low subgroup scores.  
   - **Evidence:** Evaluation defines Subgroup, BPSN, and BNSP AUCs, then combines per-identity bias metrics with a generalized mean; it explicitly describes BPSN as benign identity mentions confused with toxic non-group comments.

2. **Identity mentions are a spurious predictive shortcut whose correlation with toxicity changes across the evaluation strata.**  
   - **Objects:** comment semantics; identity mention; toxicity target; training co-occurrence distribution; group-conditioned ranking strata.  
   - **Relations:** in training, identity terms may correlate with positive labels because they occur disproportionately in attacked comments, but within the BPSN comparison identity presence should not itself elevate a benign comment’s score. An unconstrained empirical-risk model can exploit this shortcut and thereby create the exact cross-stratum ranking failure the metric measures.  
   - **Evidence:** Description says models “incorrectly learned to associate” frequently attacked identities with toxicity and gives benign identity-containing text predicted toxic; train data includes identity columns while test does not.

3. **The training corpus is too large for naive repeated full-corpus experimentation under the single-A10, six-hour execution cap, while the metric depends on relatively rare cross-stratum examples.**  
   - **Objects:** 1,804,874 training comments; identity/label intersections; ModernBERT-large; A10 22 GiB; six-hour cap; validation metric.  
   - **Relations:** a first run must allocate updates toward the metric-defining minority intersections rather than rely on repeated uniform full-data epochs or tuning. Uniform sampling can make the cross-stratum comparisons that dominate weak bias AUCs too infrequent.  
   - **Evidence:** workspace preview lists 1,804,874 train rows and many identity columns with 1,399,744 missing values; resources allow one A10 GPU and six hours per solution.

**Step 2 — cross-field retrieval queries**

- Property 1: `partial AUC optimization fairness`; `group conditional AUC ranking`; `worst group ranking loss`; `pairwise ranking subgroup robustness`
- Property 2: `spurious correlation group robustness`; `group invariant risk minimization`; `counterfactual invariance shortcut learning`; `worst group distributionally robust optimization`
- Property 3: `rare group stratified minibatch sampling`; `long tail group reweighting`; `distributionally robust minibatch optimization`

[turn 1] search_papers('partial AUC optimization fairness', k=8) ->
     17.31  [iclr-2024] Interventional Fairness on Partially Known Causal Graphs: A Constrained Optimization Approach  (iclr-2024/skult2vx9p)
     16.83  [aaai-2025] FROC: Building Fair ROC from a Trained Classifier  (aaai-2025/770f3d5748477fdb1a04856827eed0eb120449cb)
     15.88  [iclr-2024] Demystifying Local & Global Fairness Trade-offs in Federated Learning Using Partial Information Deco  (iclr-2024/sbj2qdhgew)
     15.41  [neurips-2024] A Local Method for Satisfying Interventional Fairness with Partially Known Causal Graphs  (neurips-2024/f478d99e1e47b9d5e4a3127f33545719)
     15.38  [aaai-2024] Fair and Efficient Completion of Indivisible Goods  (aaai-2024/9faddab762a63729bfb250176255fa43714cf5c7)
     14.49  [neurips-2024] AUCSeg: AUC-oriented Pixel-level Long-tail Semantic Segmentation  (neurips-2024/e574db41163e700545ff4114f96b3d7a)
     14.40  [icml-2025] A Federated Stochastic Multi-level Compositional Minimax Algorithm for Deep AUC Maximization  (icml-2025/zhang24aw)
     14.37  [icml-2024] A Federated Stochastic Multi-level Compositional Minimax Algorithm for Deep AUC Maximization  (icml-2024/zhang24aw)

[turn 1] search_papers('group conditional AUC ranking', k=8) ->
     15.97  [aaai-2025] FROC: Building Fair ROC from a Trained Classifier  (aaai-2025/770f3d5748477fdb1a04856827eed0eb120449cb)
     15.67  [neurips-2024] AUC Maximization under Positive Distribution Shift  (neurips-2024/3f8c7eb848ffec848f3ed2b7ca44915d)
     13.53  [icml-2024] Interplay of ROC and Precision-Recall AUCs: Theoretical Limits and Practical Implications in Binary   (icml-2024/mihelich24a)
     13.52  [icml-2025] Interplay of ROC and Precision-Recall AUCs: Theoretical Limits and Practical Implications in Binary   (icml-2025/mihelich24a)
     13.29  [aaai-2025] Group Orthogonal Low-Rank Adaptation for RGB-T Tracking  (aaai-2025/99221838fd02b78ef3879bf06a23d80a67948bdb)
     12.66  [neurips-2025] Preference-Based Dynamic Ranking Structure Recognition  (neurips-2025/1b5f17949a3fb4a2ee99438e949cd235)
     12.62  [acl-2025] R-Fairness: Assessing Fairness of Ranking in Subjective Data  (acl-2025/2025acl-long1548)
     12.54  [neurips-2024] AUCSeg: AUC-oriented Pixel-level Long-tail Semantic Segmentation  (neurips-2024/e574db41163e700545ff4114f96b3d7a)

[turn 1] search_papers('worst group ranking loss', k=8) ->
     18.56  [neurips-2024] On Socially Fair Low-Rank Approximation and Column Subset Selection  (neurips-2024/a1d2eca2159af6978ff2633454d8db81)
     17.51  [neurips-2024] The Group Robustness is in the Details: Revisiting Finetuning under Spurious Correlations  (neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6)
     16.69  [neurips-2024] Group Robust Preference Optimization in Reward-free RLHF  (neurips-2024/4147dfaa46cd7e20a2aecb91097ae8cc)
     16.27  [aaai-2025] Diversity of Structured Domains via k-Kemeny Scores  (aaai-2025/59e326469d45fa5ec2670f6aceec54765c503fb7)
     16.25  [icml-2025] Differentially Private Worst-group Risk Minimization  (icml-2025/zhou24b)
     16.23  [neurips-2025] FairNet: Dynamic Fairness Correction without Performance Loss via Contrastive Conditional LoRA  (neurips-2025/81f2d59479a96afd8056db9468254515)
     16.18  [icml-2024] Differentially Private Worst-group Risk Minimization  (icml-2024/zhou24b)
     15.47  [iclr-2025] MixMax: Distributional Robustness in Function Space via Optimal Data Mixtures  (iclr-2025/dikphooa2d)

[turn 1] search_papers('pairwise ranking subgroup robustness', k=8) ->
     17.33  [acl-2024] PRP-Graph: Pairwise Ranking Prompting to LLMs with Graph Aggregation for Effective Text Re-ranking  (acl-2024/2024acl-long313)
     17.32  [aaai-2025] From Pairwise to Ranking: Climbing the Ladder to Ideal Collaborative Filtering with Pseudo-Ranking  (aaai-2025/27d5e36ead44eeec5a48911c5affcc8d3ab0fe01)
     16.67  [acl-2025] Ranking Unraveled: Recipes for LLM Rankings in Head-to-Head AI Combat  (acl-2025/2025acl-long1265)
     16.38  [aaai-2025] Improved Approximation Algorithms for Clustered TSP and Subgroup Planning  (aaai-2025/08525c387a4a4536f8d1d0dcaee6983f60491d72)
     16.25  [neurips-2024] Prediction-Powered Ranking of Large Language Models  (neurips-2024/cd47cd67caa87f5b1944e00f6781598f)
     15.76  [neurips-2024] PSL: Rethinking and Improving Softmax Loss from Pairwise Perspective for Recommendation  (neurips-2024/db1d5c63576587fc1d40d33a75190c71)
     15.22  [iccv-2023] Identification of Systematic Errors of Image Classifiers on Rare Subgroups  (iccv-2023/metzenidentificationofsystematicerrorsofimageclassifiersonraresubgroupsiccv2023paper)
     15.19  [acl-2025] Are Optimal Algorithms Still Optimal? Rethinking Sorting in LLM-Based Pairwise Ranking with Batching  (acl-2025/2025acl-short83)

[turn 1] search_papers('spurious correlation group robustness', k=8) ->
     26.92  [icml-2025] Improving Group Robustness on Spurious Correlation Requires Preciser Group Inference  (icml-2025/han24g)
     26.87  [icml-2024] Improving Group Robustness on Spurious Correlation Requires Preciser Group Inference  (icml-2024/han24g)
     24.43  [naacl-2025] Fighting Spurious Correlations in Text Classification via a Causal Learning Perspective  (naacl-2025/2025naacl-long215)
     24.02  [neurips-2024] The Group Robustness is in the Details: Revisiting Finetuning under Spurious Correlations  (neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6)
     23.80  [acl-2024] ASPIRE: Language-Guided Data Augmentation for Improving Robustness Against Spurious Correlations  (acl-2024/2024findings-acl22)
     23.67  [neurips-2025] The Impact of Coreset Selection on Spurious Correlations and Group Robustness  (neurips-2025/8ae3fd80c07b1c5fdc0ce59b55396812-abstract-datasetsandbenchmarkstrackhtml)
     23.35  [icml-2025] Prompting is a Double-Edged Sword: Improving Worst-Group Robustness of Foundation Models  (icml-2025/setlur24a)
     23.32  [icml-2024] Prompting is a Double-Edged Sword: Improving Worst-Group Robustness of Foundation Models  (icml-2024/setlur24a)

[turn 1] search_papers('group invariant risk minimization', k=8) ->
     19.35  [icml-2025] Invariant Risk Minimization Is A Total Variation Model  (icml-2025/lai24c)
     19.23  [icml-2024] Invariant Risk Minimization Is A Total Variation Model  (icml-2024/lai24c)
     18.82  [icml-2024] Differentially Private Worst-group Risk Minimization  (icml-2024/zhou24b)
     18.69  [icml-2025] Differentially Private Worst-group Risk Minimization  (icml-2025/zhou24b)
     18.52  [iclr-2025] Out-of-distribution Generalization for Total Variation based Invariant Risk Minimization  (iclr-2025/c4wekjojy3)
     17.53  [neurips-2024] GO4Align: Group Optimization for Multi-Task Alignment  (neurips-2024/c98987c5ec4f30920d7190dc699e3daf)
     16.30  [iclr-2025] Group Distributionally Robust Dataset Distillation with Risk Minimization  (iclr-2025/3jsu5qxnru)
     16.05  [aaai-2025] A Renormalization Group Framework for Scale-Invariant Feature Learning in Deep Neural Networks (Stud  (aaai-2025/c3429189f0d632280903f6574627a9043b2a2286)

[turn 1] search_papers('counterfactual invariance shortcut learning', k=8) ->
     21.14  [aaai-2025] Bot Meets Shortcut: How Can LLMs Aid in Handling Unknown Invariance OOD Scenarios?  (aaai-2025/f930d2cbb89f26ff54093ebcf01376b2e8332495)
     18.37  [icml-2024] Causally Motivated Personalized Federated Invariant Learning with Shortcut-Averse Information-Theore  (icml-2024/tang24a)
     18.34  [icml-2025] Causally Motivated Personalized Federated Invariant Learning with Shortcut-Averse Information-Theore  (icml-2025/tang24a)
     17.99  [neurips-2025] Rectifying Shortcut Behaviors in Preference-based Reward Learning  (neurips-2025/5d97b7e62022c859347397f6c1e8d0f9)
     17.85  [iclr-2024] Learning Personalized Causally Invariant Representations for Heterogeneous Federated Clients  (iclr-2024/8fhwky0swf)
     16.95  [neurips-2025] Representation-Level Counterfactual Calibration for Debiased Zero-Shot Recognition  (neurips-2025/c3aa90d5d91f3e3a924036e93232fe14)
     16.86  [icml-2024] Federated Self-Explaining GNNs with Anti-shortcut Augmentations  (icml-2024/yue24b)
     16.83  [icml-2025] Federated Self-Explaining GNNs with Anti-shortcut Augmentations  (icml-2025/yue24b)

[turn 1] search_papers('worst group distributionally robust optimization', k=8) ->
     22.22  [icml-2025] Controllable Prompt Tuning For Balancing Group Distributional Robustness  (icml-2025/phan24b)
     21.78  [icml-2024] Controllable Prompt Tuning For Balancing Group Distributional Robustness  (icml-2024/phan24b)
     21.17  [iclr-2025] MixMax: Distributional Robustness in Function Space via Optimal Data Mixtures  (iclr-2025/dikphooa2d)
     20.59  [icml-2025] Differentially Private Worst-group Risk Minimization  (icml-2025/zhou24b)
     20.48  [icml-2024] Differentially Private Worst-group Risk Minimization  (icml-2024/zhou24b)
     19.53  [neurips-2025] Multi-Expert Distributionally Robust Optimization for Out-of-Distribution Generalization  (neurips-2025/929814ae1e76ae131a473e3f30609fef)
     19.15  [neurips-2024] Group Robust Preference Optimization in Reward-free RLHF  (neurips-2024/4147dfaa46cd7e20a2aecb91097ae8cc)
     18.94  [icml-2025] Improving Group Robustness on Spurious Correlation Requires Preciser Group Inference  (icml-2025/han24g)

[turn 1] search_papers('rare group stratified minibatch sampling', k=8) ->
     17.68  [aaai-2024] Using Stratified Sampling to Improve LIME Image Explanations  (aaai-2024/0572aa74eb83ffb591d2d6310dd1ad662e889476)
     16.49  [aaai-2025] Stratified Knowledge-Density Super-Network for Scalable Vision Transformers  (aaai-2025/2db9b499c2b22da2d1cef3bcbee66f1cd2486185)
     16.34  [iclr-2025] Aioli: A Unified Optimization Framework for Language Model Data Mixing  (iclr-2025/szgzjhanse)
     16.15  [iclr-2025] Faster Inference of Flow-Based Generative Models via Improved Data-Noise Coupling  (iclr-2025/rsgprjdihh)
     15.14  [neurips-2024] Stratified Prediction-Powered Inference for Effective Hybrid Evaluation of Language Models  (neurips-2024/c9fcd02e6445c7dfbad6986abee53d0d)
     14.97  [neurips-2025] Stratify or Die: Rethinking Data Splits in Image Segmentation  (neurips-2025/69a2ebb622b999be1cb932aceea5a236)
     14.26  [iclr-2024] SGD Finds then Tunes Features in Two-Layer Neural Networks with near-Optimal Sample Complexity: A Ca  (iclr-2024/hgojlxzb16)
     13.91  [aaai-2024] Towards Stability and Generalization Bounds in Decentralized Minibatch Stochastic Gradient Descent  (aaai-2024/f111d7302652acc103bcb1f305e33363031a6c60)

[turn 1] search_papers('long tail group reweighting', k=8) ->
     22.97  [iccv-2023] AREA: Adaptive Reweighting via Effective Area for Long-Tailed Classification  (iccv-2023/chenareaadaptivereweightingviaeffectiveareaforlong-tailedclassificationiccv2023paper)
     20.83  [neurips-2025] Long-tailed Recognition with Model Rebalancing  (neurips-2025/c4889bd7f7ce643003746526da2c2fc4)
     20.00  [aaai-2024] Decoupled Optimisation for Long-Tailed Visual Recognition  (aaai-2024/9578e815851bad56c71bc45c256c45307e0895e8)
     18.50  [iccv-2023] Global Balanced Experts for Federated Long-Tailed Learning  (iccv-2023/zengglobalbalancedexpertsforfederatedlong-tailedlearningiccv2023paper)
     17.88  [acl-2025] MotiR: Motivation-aware Retrieval for Long-Tail Recommendation  (acl-2025/2025acl-industry65)
     17.81  [iclr-2024] Learning to Reject Meets Long-tail Learning  (iclr-2024/ta26ltnq2r)
     17.66  [iclr-2025] Group-robust Sample Reweighting for Subpopulation Shifts via Influence Functions  (iclr-2025/aqj9ifxrl6)
     17.26  [aaai-2024] FedGCR: Achieving Performance and Fairness for Federated Learning with Distinct Client Types via Gro  (aaai-2024/089b447a1a9d9cf3cd2d9b23faf4280ecc76a6b4)

[turn 1] search_papers('distributionally robust minibatch optimization', k=8) ->
     17.86  [aaai-2024] Towards Stability and Generalization Bounds in Decentralized Minibatch Stochastic Gradient Descent  (aaai-2024/f111d7302652acc103bcb1f305e33363031a6c60)
     15.84  [iclr-2025] Faster Inference of Flow-Based Generative Models via Improved Data-Noise Coupling  (iclr-2025/rsgprjdihh)
     13.96  [neurips-2024] Near-Optimality of Contrastive Divergence Algorithms  (neurips-2024/a55f589b1d54edd513cf1c8b9dd1ed47)
     13.83  [neurips-2024] A Bayesian Approach to Data Point Selection  (neurips-2024/437587c32b781fbb94026ac5905b439b)
     13.65  [neurips-2024] SLowcalSGD : Slow Query Points Improve Local-SGD for Stochastic Convex Optimization  (neurips-2024/a97b58c4f7551053b0512f92244b0810)
     13.28  [iclr-2024] SGD Finds then Tunes Features in Two-Layer Neural Networks with near-Optimal Sample Complexity: A Ca  (iclr-2024/hgojlxzb16)
     13.12  [iclr-2025] Convergence of Distributed Adaptive Optimization with Local Updates  (iclr-2025/vng7srnvd9)
     12.94  [neurips-2025] AmorLIP: Efficient Language-Image Pretraining via Amortization  (neurips-2025/445ff69ea52306c704fcd8a003b3d28b)

[turn 2] read_abstract(['neurips-2024/e574db41163e700545ff4114f96b3d7a', 'neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6', 'iclr-2025/aqj9ifxrl6']) -> 3 abstracts

[turn 2] search_papers('AUC margin loss imbalanced classification', k=10) ->
     30.12  [aaai-2025] Towards Macro-AUC Oriented Imbalanced Multi-Label Continual Learning  (aaai-2025/2e0b591f1c77306f4923e9ab2e615fff2317b795)
     29.31  [neurips-2024] AUC Maximization under Positive Distribution Shift  (neurips-2024/3f8c7eb848ffec848f3ed2b7ca44915d)
     25.63  [icml-2024] Interplay of ROC and Precision-Recall AUCs: Theoretical Limits and Practical Implications in Binary   (icml-2024/mihelich24a)
     25.17  [icml-2025] Interplay of ROC and Precision-Recall AUCs: Theoretical Limits and Practical Implications in Binary   (icml-2025/mihelich24a)
     24.06  [icml-2024] A Federated Stochastic Multi-level Compositional Minimax Algorithm for Deep AUC Maximization  (icml-2024/zhang24aw)
     23.09  [icml-2025] A Federated Stochastic Multi-level Compositional Minimax Algorithm for Deep AUC Maximization  (icml-2025/zhang24aw)
     22.28  [aaai-2024] Difficulty-aware Balancing Margin Loss for Long-tailed Recognition  (aaai-2024/2f5d66a013e81bebd3ed12753919fabaf7b30901)
     20.05  [iccv-2023] A step towards understanding why classification helps regression  (iccv-2023/pinteaasteptowardsunderstandingwhyclassificationhelpsregressioniccv2023paper)
     19.99  [neurips-2025] Improved Balanced Classification with Theoretically Grounded Loss Functions  (neurips-2025/701b46370fc60a7b25d9821936766b9b)
     19.83  [aaai-2025] Leveraging First and Zeroth-Order Gradient to Address Imbalanced Black-Box Prompt Tuning via Minimax  (aaai-2025/f805572b4f4ddec9b21f845f8eef12392a8b7556)

[turn 2] search_papers('group DRO spurious correlations finetuning', k=10) ->
     29.36  [neurips-2024] The Group Robustness is in the Details: Revisiting Finetuning under Spurious Correlations  (neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6)
     26.45  [icml-2025] Prompting is a Double-Edged Sword: Improving Worst-Group Robustness of Foundation Models  (icml-2025/setlur24a)
     26.40  [icml-2024] Prompting is a Double-Edged Sword: Improving Worst-Group Robustness of Foundation Models  (icml-2024/setlur24a)
     23.95  [icml-2025] Improving Group Robustness on Spurious Correlation Requires Preciser Group Inference  (icml-2025/han24g)
     23.92  [icml-2024] Improving Group Robustness on Spurious Correlation Requires Preciser Group Inference  (icml-2024/han24g)
     22.17  [icml-2025] Unsupervised Concept Discovery Mitigates Spurious Correlations  (icml-2025/arefin24a)
     22.17  [icml-2024] Unsupervised Concept Discovery Mitigates Spurious Correlations  (icml-2024/arefin24a)
     21.65  [iccv-2023] Overwriting Pretrained Bias with Finetuning Data  (iccv-2023/wangoverwritingpretrainedbiaswithfinetuningdataiccv2023paper)
     21.19  [naacl-2025] Fighting Spurious Correlations in Text Classification via a Causal Learning Perspective  (naacl-2025/2025naacl-long215)
     20.59  [acl-2024] ASPIRE: Language-Guided Data Augmentation for Improving Robustness Against Spurious Correlations  (acl-2024/2024findings-acl22)

[turn 2] search_papers('subpopulation shift sample reweighting', k=10) ->
     32.10  [iclr-2025] Group-robust Sample Reweighting for Subpopulation Shifts via Influence Functions  (iclr-2025/aqj9ifxrl6)
     24.92  [neurips-2024] CODA: A Correlation-Oriented Disentanglement and Augmentation Modeling Scheme for Better Resisting S  (neurips-2024/ba06eb7c3ff7cb731ba04c906d212445)
     18.50  [iclr-2025] Regularizing Energy among Training Samples for Out-of-Distribution Generalization  (iclr-2025/lbx9zdurxe)
     17.79  [aaai-2025] Boosting Test Performance with Importance Sampling-a Subpopulation Perspective  (aaai-2025/150b28ab6b1d5a47f8126f1073afdf668e5bb9f6)
     15.72  [iclr-2024] On Harmonizing Implicit Subpopulations  (iclr-2024/3guro0krue)
     15.32  [neurips-2025] Partition-Then-Adapt: Combating Prediction Bias for Reliable Multi-Modal Test-Time Adaptation  (neurips-2025/03cb2cb0ede9aad27b6f3d759fed71cb)
     15.29  [neurips-2024] Learning Where to Edit Vision Transformers  (neurips-2024/f269520d5f111719dd82b36667997d49)
     14.71  [aaai-2024] Learning to Reweight for Generalizable Graph Neural Network  (aaai-2024/d7d13917a6b134300a12089fb4c88bed470b35bf)
     14.69  [neurips-2024] MaNo: Exploiting Matrix Norm for Unsupervised Accuracy Estimation Under Distribution Shifts  (neurips-2024/49abf767d606b72f74ea6009176fafeb)
     14.53  [neurips-2025] A Generalized Label Shift Perspective for Cross-Domain Gaze Estimation  (neurips-2025/07b386c6e4caa912c063222b6af51801)

[turn 3] open_paper({"paper_id": "neurips-2024/e574db41163e700545ff4114f96b3d7a", "outline_offset": 0}) ->
{"status": "ok", "paper_id": "neurips-2024/e574db41163e700545ff4114f96b3d7a", "title": "AUCSeg: AUC-oriented Pixel-level Long-tail Semantic Segmentation", "source_url": "https://papers.nips.cc/paper_files/paper/2024/file/e574db41163e700545ff4114f96b3d7a-Paper-Conference.pdf", "pdf_sha256": "d3e3b1c2d8e7abf2000348eb306b8cfa8f4cdff61b5afe7e9c9f3cb11cc7950f", "text_sha256": "1749487c25109390e7ceee5df66b91d450c507582b4a1986aae32e0dadda39fb", "parser": {"schema": "paper-fulltext-v1", "reader_sha256": "5e308bc98d54a08e8fabb5784c5ec5c3f7b0c84602c16c614fa7d1ac5bf1dc1f", "pymupdf": "1.28.0", "pymupdf4llm": "1.28.0", "pymupdf_layout": "1.28.0", "tabulate": "0.9.0"}, "page_count": 45, "warnings": ["Text extraction only: figures and complex equations may be incomplete; OCR is disabled"], "cache_hit": false, "outline": [{"chunk_id": "p001-c001", "page": 1, "section": "AUCSeg: AUC-oriented Pixel-level Long-tail** **Semantic Segmentation", "chars": 74}, {"chunk_id": "p001-c002", "page": 1, "section": "Boyu Han** <sup>1</sup> <sup>_,_</sup> <sup>2</sup> **Qianqian Xu** <sup>1</sup> <sup>_,_</sup> <sup>3</sup> <sup>_∗_</sup> **Zhiyong Yang** <sup>2</sup> **Shil", "chars": 777}, {"chunk_id": "p001-c003", "page": 1, "section": "Abstract", "chars": 1345}, {"chunk_id": "p001-c004", "page": 1, "section": "1** **Introduction", "chars": 1519}, {"chunk_id": "p002-c001", "page": 2, "section": "1** **Introduction", "chars": 1930}, {"chunk_id": "p002-c002", "page": 2, "section": "1** **Introduction", "chars": 1673}, {"chunk_id": "p002-c003", "page": 2, "section": "1** **Introduction", "chars": 734}, {"chunk_id": "p003-c001", "page": 3, "section": "1** **Introduction", "chars": 287}, {"chunk_id": "p003-c002", "page": 3, "section": "2** **Related Work", "chars": 22}, {"chunk_id": "p003-c003", "page": 3, "section": "2.1** **Semantic Segmentation", "chars": 1403}, {"chunk_id": "p003-c004", "page": 3, "section": "2.2** **AUC Optimization", "chars": 1644}, {"chunk_id": "p003-c005", "page": 3, "section": "3** **Preliminaries", "chars": 127}, {"chunk_id": "p003-c006", "page": 3, "section": "3.1** **Semantic Segmentation Training Framework", "chars": 916}, {"chunk_id": "p004-c001", "page": 4, "section": "3.1** **Semantic Segmentation Training Framework", "chars": 164}, {"chunk_id": "p004-c002", "page": 4, "section": "Y** ˆ", "chars": 1038}, {"chunk_id": "p004-c003", "page": 4, "section": "Y** <sup>_ic_</sup> _u,v_ <sup>log(ˆ</sup> <sup>**Y**</sup>", "chars": 698}, {"chunk_id": "p004-c004", "page": 4, "section": "3.2** **AUC Optimization", "chars": 1917}, {"chunk_id": "p004-c005", "page": 4, "section": "4** **AUC-Oriented Semantic Segmentation", "chars": 690}, {"chunk_id": "p005-c001", "page": 5, "section": "4** **AUC-Oriented Semantic Segmentation", "chars": 32}, {"chunk_id": "p005-c002", "page": 5, "section": "4.1** **Pixel-level AUC Optimization", "chars": 1939}, {"chunk_id": "p005-c003", "page": 5, "section": "4.1** **Pixel-level AUC Optimization", "chars": 703}, {"chunk_id": "p005-c004", "page": 5, "section": "X** <sup>_p_</sup> _m_ <sup>_∈N_</sup> _c_", "chars": 128}, {"chunk_id": "p005-c005", "page": 5, "section": "X** <sup>_p_</sup> _n_ <sup>_∈N_</sup> _c_ <sup>_′_</sup>", "chars": 1167}, {"chunk_id": "p005-c006", "page": 5, "section": "4.2** **Generalization Bound", "chars": 416}, {"chunk_id": "p006-c001", "page": 6, "section": "4.2** **Generalization Bound", "chars": 627}, {"chunk_id": "p006-c002", "page": 6, "section": "Theorem 1** (Generalization Bound for AUCSeg) **.** _Let_ E _D_", "chars": 1445}, {"chunk_id": "p006-c003", "page": 6, "section": "Theorem 1** (Generalization Bound for AUCSeg) **.** _Let_ E _D_", "chars": 1089}, {"chunk_id": "p006-c004", "page": 6, "section": "Remark 1.** We achieve a bound of _O_ - _τ_ �log ( _τNk_ ) _/N_ <u>�, indicating reliable generalization with a</u>", "chars": 432}, {"chunk_id": "p006-c005", "page": 6, "section": "Remark 1.** We achieve a bound of _O_", "chars": 79}, {"chunk_id": "p006-c006", "page": 6, "section": "4.3** **Tail-class Memory Bank", "chars": 34}], "next_outline_offset": 30, "remaining_chars": 40000, "note": "Opening a paper returns no body text. Use read_paper to obtain citable excerpts."}

[turn 3] open_paper({"paper_id": "neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6", "outline_offset": 0}) ->
{"status": "ok", "paper_id": "neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6", "title": "The Group Robustness is in the Details: Revisiting Finetuning under Spurious Correlations", "source_url": "https://papers.nips.cc/paper_files/paper/2024/file/dc4db2ff2c1aefce3b594f821ea82fe6-Paper-Conference.pdf", "pdf_sha256": "f416dafcc09147c92a6ca447b0f45fb811b15da488defb85ddbab2eb43ea0ffc", "text_sha256": "293220512e013c985ea3488224e94d543a70663f35b78689b5c6222d507aab9b", "parser": {"schema": "paper-fulltext-v1", "reader_sha256": "5e308bc98d54a08e8fabb5784c5ec5c3f7b0c84602c16c614fa7d1ac5bf1dc1f", "pymupdf": "1.28.0", "pymupdf4llm": "1.28.0", "pymupdf_layout": "1.28.0", "tabulate": "0.9.0"}, "page_count": 32, "warnings": ["Text extraction only: figures and complex equations may be incomplete; OCR is disabled"], "cache_hit": true, "outline": [{"chunk_id": "p001-c001", "page": 1, "section": "The Group Robustness is in the Details: Revisiting** **Finetuning under Spurious Correlations", "chars": 99}, {"chunk_id": "p001-c002", "page": 1, "section": "Tyler LaBonte** <sup>1</sup> <sup>_∗_</sup> **John C. Hill** <sup>2</sup> **Xinchen Zhang** <sup>2</sup>", "chars": 106}, {"chunk_id": "p001-c003", "page": 1, "section": "Vidya Muthukumar** <sup>2</sup> <sup>_,_</sup> <sup>1</sup> **Abhishek Kumar** <sup>_†_</sup>", "chars": 273}, {"chunk_id": "p001-c004", "page": 1, "section": "Abstract", "chars": 1442}, {"chunk_id": "p001-c005", "page": 1, "section": "1** **Introduction", "chars": 1706}, {"chunk_id": "p002-c001", "page": 2, "section": "1** **Introduction", "chars": 1975}, {"chunk_id": "p002-c002", "page": 2, "section": "1.1** **Related work", "chars": 208}, {"chunk_id": "p002-c003", "page": 2, "section": "Spurious correlations.** The proclivity of ERM to rely on spurious correlations has been widely", "chars": 706}, {"chunk_id": "p002-c004", "page": 2, "section": "Class-balancing and group robustness.** _Group-balancing_, or training with an equal number of", "chars": 1259}, {"chunk_id": "p002-c005", "page": 2, "section": "Overparameterization and distributional robustness.** While the accepted empirical wisdom is", "chars": 390}, {"chunk_id": "p003-c001", "page": 3, "section": "Overparameterization and distributional robustness.** While the accepted empirical wisdom is", "chars": 961}, {"chunk_id": "p003-c002", "page": 3, "section": "2** **Preliminaries", "chars": 23}, {"chunk_id": "p003-c003", "page": 3, "section": "Setting.** We consider classification tasks with input domain R <sup>_n_</sup> and target classes _Y_ _⊂_ N. Suppose", "chars": 1785}, {"chunk_id": "p003-c004", "page": 3, "section": "Class-balancing.** A dataset is considered to be _class-balanced_ if it is composed of an equal number", "chars": 1938}, {"chunk_id": "p003-c005", "page": 3, "section": "Class-balancing.** A dataset is considered to be _class-balanced_ if it is composed of an equal number", "chars": 367}, {"chunk_id": "p004-c001", "page": 4, "section": "Datasets and models.** We study four classification datasets, two in the vision domain and two in", "chars": 1728}, {"chunk_id": "p004-c002", "page": 4, "section": "Datasets and models.** We study four classification datasets, two in the vision domain and two in", "chars": 870}, {"chunk_id": "p004-c003", "page": 4, "section": "3** **Nuanced effects of class-balancing on group robustness", "chars": 218}, {"chunk_id": "p004-c004", "page": 4, "section": "3.1** **Catastrophic collapse of class-balanced upsampling and upweighting", "chars": 1990}, {"chunk_id": "p005-c001", "page": 5, "section": "3.1** **Catastrophic collapse of class-balanced upsampling and upweighting", "chars": 1598}, {"chunk_id": "p005-c002", "page": 5, "section": "3.1** **Catastrophic collapse of class-balanced upsampling and upweighting", "chars": 1783}, {"chunk_id": "p005-c003", "page": 5, "section": "Contextualization with previous work.** Our observations explain the decrease in WGA of CelebA", "chars": 793}, {"chunk_id": "p006-c001", "page": 6, "section": "Contextualization with previous work.** Our observations explain the decrease in WGA of CelebA", "chars": 1489}, {"chunk_id": "p006-c002", "page": 6, "section": "3.2** **Mixture balancing:** **interpolating between subsetting and upsampling", "chars": 1521}, {"chunk_id": "p006-c003", "page": 6, "section": "3.2** **Mixture balancing:** **interpolating between subsetting and upsampling", "chars": 572}, {"chunk_id": "p007-c001", "page": 7, "section": "3.2** **Mixture balancing:** **interpolating between subsetting and upsampling", "chars": 829}, {"chunk_id": "p007-c002", "page": 7, "section": "Note on validation.** In Figure 2, we plot the best class-imbalance ratio achieved using validation on", "chars": 697}, {"chunk_id": "p007-c003", "page": 7, "section": "Contextualization with previous work.** Increasing exposure to majority class data without oversampling the minority class was previously explored by [26], who ", "chars": 837}, {"chunk_id": "p007-c004", "page": 7, "section": "4** **Model scaling improves WGA of class-balanced finetuning", "chars": 1327}, {"chunk_id": "p007-c005", "page": 7, "section": "4** **Model scaling improves WGA of class-balanced finetuning", "chars": 762}], "next_outline_offset": 30, "remaining_chars": 40000, "note": "Opening a paper returns no body text. Use read_paper to obtain citable excerpts."}

[turn 3] open_paper({"paper_id": "iclr-2025/aqj9ifxrl6", "outline_offset": 0}) ->
{"status": "download_error", "paper_id": "iclr-2025/aqj9ifxrl6", "message": "HTTPError: HTTP Error 403: Forbidden", "note": "No full-text evidence returned by this call; read_abstract remains available"}

[turn 3] read_abstract(['neurips-2024/3f8c7eb848ffec848f3ed2b7ca44915d', 'icml-2024/han24g', 'aaai-2025/150b28ab6b1d5a47f8126f1073afdf668e5bb9f6']) -> 3 abstracts

[turn 4] read_paper({"paper_id": "neurips-2024/e574db41163e700545ff4114f96b3d7a", "chunk_ids": ["p001-c004", "p004-c004", "p005-c002"]}) ->
{"status": "ok", "paper_id": "neurips-2024/e574db41163e700545ff4114f96b3d7a", "pdf_sha256": "d3e3b1c2d8e7abf2000348eb306b8cfa8f4cdff61b5afe7e9c9f3cb11cc7950f", "text_sha256": "1749487c25109390e7ceee5df66b91d450c507582b4a1986aae32e0dadda39fb", "chunks": [{"chunk_id": "p001-c004", "page": 1, "section": "1** **Introduction", "chars": 1519, "text": "**1** **Introduction**\n\nSemantic segmentation aims to categorize each pixel within an image into a specific class, which\nis a fundamental task in image processing and computer vision [33, 51, 75]. Over the past decades,\nsubstantial efforts [58, 23, 43, 96] have advanced the field of semantic segmentation. The mainstream\nparadigm is to develop innovative network architectures that encode more discriminative features\nfor dense pixel-level classifications. Typical backbones include CNN-based [58, 14, 80] and newly\nemerging Transformer-based methods [108, 83, 65, 15, 32], which have achieved the state-of-the-art\n(SOTA) performance. Beyond this direction, researchers [24, 66, 48, 41] have recently realized\nthe **_Pixel-level Long-tail issue_** _in Semantic Segmentation (PLSS)_, as shown at the top of Figure 1.\nSimilar to the flaws of traditional long-tail problems, the major classes will dominate the model\nlearning process, causing the model to overlook the segmentation of minority classes in an image.\nSeveral remedies have been proposed to alleviate this [49, 61, 10, 56, 104, 92, 78]. For example,\n\n[77] introduces a category-wise variation technique inversely proportional to distribution to achieve\nbalanced segmentation; [66] introduces a sequence-based generative adversarial network for imbalanced medical image segmentation, and [41] develops a re-weighting scheme for semi-supervised\nsegmentation.\n\n_∗_ Corresponding authors.\n\n38th Conference on Neural Information Processing Systems (NeurIPS 2024)."}, {"chunk_id": "p004-c004", "page": 4, "section": "3.2** **AUC Optimization", "chars": 1917, "text": "**3.2** **AUC Optimization**\n\n_Area under the Receiver Operating Characteristic Curve (AUC)_ is a well-known ranking performance\n\nmetric for **binary classification** task, which measures the probability that a positive instance has a\nhigher score than a negative one [35]:\n\n_AUC_ ( _fθ_ ) = P - _fθ_ ( **X** <sup>+</sup> ) _> fθ_ ( **X** <sup>_−_</sup> ) _|y_ <sup>+</sup> = 1 _, y_ <sup>_−_</sup> = 0� _,_ (3)\n\nwhere ( **X** <sup>+</sup> _, y_ <sup>+</sup> ) and ( **X** <sup>_−_</sup> _, y_ <sup>_−_</sup> ) represent positive and negative samples, respectively. When _AUC_ _→_\n1, it indicates that the classifier can perfectly separate positive and negative samples.\n\nAccording to [87, 86, 88], given finite datasets, maximizing _AUC_ ( _hθ_ ) is usually realized by\nmaximizing its unbiased empirical estimation:\n\n_n_ <sup>_−_</sup>\n\n_j_ =1\n\n<u>1</u>\n_AUC_ ˆ ( _hθ_ ) = 1 _−_\n_n_ <sup>+</sup> _n_ <sup>_−_</sup>\n\n_n_ <sup>+</sup>\n\n_i_ =1\n\n_ℓ_ ( _hθ_ ( **X** <sup>+</sup> ) _−_ _hθ_ ( **X** <sup>_−_</sup> )) _,_ (4)\n\nwhere _ℓ_ is a differentiable surrogate loss [86] measuring the ranking error between two samples, _n_ <sup>+</sup>\nand _n_ <sup>_−_</sup> denote the number of positive and negative samples, respectively.\n\nMoreover, we can directly optimize the following problem for AUC maximization:\n\n_n_ <sup>_−_</sup>\n\n_j_ =1\n\n_n_ <sup>+</sup>\n\n_i_ =1\n\nmin\n\n_θ_\n\n<u>1</u>\n_n_ <sup>+</sup> _n_ <sup>_−_</sup>\n\n_ℓ_ ( _hθ_ ( **X** <sup>+</sup> ) _−_ _hθ_ ( **X** <sup>_−_</sup> )) _._ (5)\n\nNote that, AUC has achieved significant progress in long-tailed classification [100, 88, 68]. Due to\nthe limitations of space, we refer interested readers to the literature [86, 99] for more introductions to\nAUC. However, most existing studies merely focus on the **instance-level or image-level** problems.\nInspired by its distribution-insensitive property [26], this paper starts an early trial to introduce AUC\nto PLSS."}, {"chunk_id": "p005-c002", "page": 5, "section": "4.1** **Pixel-level AUC Optimization", "chars": 1939, "text": "**4.1** **Pixel-level AUC Optimization**\n\nSemantic segmentation is a multi-class classification task. Therefore, to apply AUC, we follow\na popular multi-class AUC manner, _i.e._, the One vs. One (ovo) strategy [64, 34, 86], which is\nan average of binary AUC score introduced in Section 3.2. Specifically, on top of the notation of\nSection 3.1, we further denote _D_ <sup>_p_</sup> = _{_ ( **X** <sup>_i_</sup> _u,v_ <sup>_,_</sup> <sup>**Y**</sup> <sup>_i_</sup> _u,v_ <sup>)</sup> <sup>_|i ∈_</sup> <sup>[1</sup> <sup>_, n_</sup> <sup>]</sup> <sup>_, u ∈_</sup> <sup>[0</sup> <sup>_, H −_</sup> <sup>1]</sup> <sup>_, v_</sup> <sup>_∈_</sup> <sup>[0</sup> <sup>_, W_</sup> <sup>_−_</sup> <sup>1]</sup> <sup>_}_</sup> <sup>as the</sup>\n\nset of all pixels; the _j_ -th element ( _j_ _∈_ [1 _, n ×_ ( _H −_ 1) _×_ ( _W_ _−_ 1)]) in _D_ <sup>_p_</sup> is abbreviated as ( **X** <sup>_p,_</sup> <sup>**Y**</sup> <sup>_p_</sup> <sup>)</sup>\n\n<sup>_i_</sup> _u,v_ <sup>_,_</sup> <sup>**Y**</sup> <sup>_i_</sup>\n\n<sup>_p_</sup> _j_ <sup>_,_</sup> <sup>**Y**</sup> <sup>_p_</sup> _j_\n\n_j_ <sup>)</sup>\n\nfor convenience. Given the model prediction _fθ_ = ( _fθ_ <sup>(1)</sup>\n\n_θ_ <sup>(1)</sup> _, . . ., fθ_ <sup>(</sup> <sup>_K_</sup> <sup>)</sup>\n\n_θ_ <sup>(</sup> <sup>_K_</sup> <sup>)</sup> ), _∀c ∈_ [ _K_ ], _fθ_ <sup>(</sup> <sup>_c_</sup> <sup>)</sup>\n\nfor convenience. Given the model prediction _fθ_ = ( _fθ_ _, . . ., fθ_ ), _∀c ∈_ [ _K_ ], _fθ_ _∈_ [0 _,_ 1], where\n\n_fθ_ <sup>(</sup> <sup>_c_</sup> <sup>)</sup> serves as a continuous score function supporting class _c_, _AUCseg_ <sup>_ovo_</sup> <sup>calculates</sup> <sup>the</sup> <sup>average</sup> <sup>of</sup>\n\nbinary AUC scores for every class pair:\n\n_θ_ serves as a continuous score function supporting class _c_, _AUCseg_ <sup>_ovo_</sup>\n\n<u>1</u>\n\n_AUCseg_ <sup>_ovo_</sup> <sup>=</sup>\n\n_K_ ( _K −_ 1)\n\n_K_\n\n-\n\n_c_ =1 _c_ = _c_ <sup>_′_</sup>\n\n_AUCcc′_ ( _fθ_ ) _,_ (6)"}], "not_returned_chunk_ids": [], "remaining_chars": 34625, "remaining_read_calls": 11}

[turn 4] read_paper({"paper_id": "neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6", "chunk_ids": ["p001-c005", "p002-c004", "p004-c004", "p006-c002", "p007-c002"]}) ->
{"status": "ok", "paper_id": "neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6", "pdf_sha256": "f416dafcc09147c92a6ca447b0f45fb811b15da488defb85ddbab2eb43ea0ffc", "text_sha256": "293220512e013c985ea3488224e94d543a70663f35b78689b5c6222d507aab9b", "chunks": [{"chunk_id": "p001-c005", "page": 1, "section": "1** **Introduction", "chars": 1706, "text": "**1** **Introduction**\n\nClassification performance in machine learning is sensitive to _spurious correlations_ : patterns which\nare predictive of the target class in the training dataset but not at test time. For example, in computer\nvision tasks, neural networks are known to utilize the backgrounds of images as proxies for their\ncontent [1, 50, 68]. Beyond simple settings, spurious correlations have been identified in highconsequence applications such as criminal justice [8], medicine [70], and facial recognition [33].\nIn particular, a model’s reliance on spurious correlations disproportionately affects its accuracy on\n_minority groups_ which are under-represented in the training dataset; we therefore desire maximizing\nthe model’s _group robustness_, quantified by its minimum accuracy on any group [50].\n\nThe standard workflow in modern machine learning involves initializing from a pretrained model and\nfinetuning on the downstream dataset using empirical risk minimization (ERM) [62], which minimizes\nthe average training loss. When _group annotations_ are available in the training dataset, practitioners\nutilize a rich literature of techniques to improve worst-group accuracy (WGA) [50, 39, 26]. However,\ngroup annotations are often unknown or problematic to obtain ( _e.g._, due to financial, privacy, or\nfairness concerns). While group robustness methods have been adapted to work without group\nannotations [31, 72, 47, 29], they remain complex variants on the standard finetuning procedure.\n\n_∗_ Corresponding author. Email: `[tlabonte@gatech.edu](mailto:tlabonte@gatech.edu)` .\n\n_†_ Work done at Google DeepMind.\n\n38th Conference on Neural Information Processing Systems (NeurIPS 2024)."}, {"chunk_id": "p002-c004", "page": 2, "section": "Class-balancing and group robustness.** _Group-balancing_, or training with an equal number of", "chars": 1259, "text": "**Class-balancing and group robustness.** _Group-balancing_, or training with an equal number of\nsamples from each group, has been proposed as a simple yet effective method to improve robustness\nto spurious correlations [17, 51, 6, 55]. However, group-balancing requires group annotations, which\nare often unknown or problematic to obtain [31, 72, 47, 29]. On the other hand, _class-balancing_, or\ntraining with an equal number of samples from each class, is a well-studied method in long-tailed\nclassification [24, 15, 4]. Recent work has shown that class-balancing is a surprisingly powerful\nmethod for improving worst-group accuracy which does not require group annotations [22, 29, 7, 53].\nIn particular, [22] study the WGA dynamics of two common class-balancing methods: removing data\nfrom the larger classes (which we call _subsetting_ ) and upsampling the smaller classes (which we call\n_upsampling_ ). Our results complement those of [22] and show more nuanced effects of class-balancing\nthan previously known; we provide additional contextualization with [22] in Section 3.1. We show\nsimilar nuanced behavior of _upweighting_ smaller classes in the loss function, a popular method in the\ngroup-balancing setting [31, 47, 55] which [22] did not study."}, {"chunk_id": "p004-c004", "page": 4, "section": "3.1** **Catastrophic collapse of class-balanced upsampling and upweighting", "chars": 1990, "text": "**3.1** **Catastrophic collapse of class-balanced upsampling and upweighting**\n\nIn a recent paper, [29] observed that contrary to the central hypothesis underlying the Just Train\nTwice method [31], the worst-group accuracy of ERM decreases dramatically with training epochs\non CelebA and CivilComments; however, they provide no explanation for this phenomenon. In this\nsection, we show that this degradation of WGA is due to their choice of class-balancing method ( _i.e._,\nupsampling). Specifically, ERM finetuned with upsampling experiences a _catastrophic collapse_ in\ntest WGA over the course of training, a phenomenon that was previously only noticed in synthetic\ndatasets with a linear classifier [22]. Moreover, while [22] state that class-balanced subsetting is not\nrecommended in practice, we show that it can in fact improve WGA conditional on the lack of of a\nsmall minority group _within the majority class_ . Finally, we show that class-balanced upweighting —\na popular technique which [22] do not study — experiences a similar WGA collapse as upsampling.\n\nWe finetune a ConvNeXt-V2 Base on Waterbirds and CelebA and a BERT Base on CivilComments,\nand we compare the subsetting, upsampling, and upweighting techniques to a class-imbalanced\n\n4We note that the Waterbirds dataset is known to contain incorrect labels [56]. We report results on the\noriginal, un-corrected version as is standard in the literature.\n\n5This version of CivilComments has four groups, used in this work and by [50, 22, 23, 26, 29]. There is\nanother version where the identity categories are not collapsed into one spurious feature; that version is used\nby [31, 72, 47]. Both versions use the WILDS split [27].\n\n6To be more specific, we finetune ConvNeXt-V2 Base roughly to a training loss of 10 _−_ 4 on Waterbirds and\n10 <sup>_−_</sup> <sup>3</sup> on CelebA, and BERT Base roughly to a training loss of 10 <sup>_−_</sup> <sup>3</sup> on CivilComments and 10 <sup>_−_</sup> <sup>2</sup> on MultiNLI.\n\n4"}, {"chunk_id": "p006-c002", "page": 6, "section": "3.2** **Mixture balancing:** **interpolating between subsetting and upsampling", "chars": 1521, "text": "**3.2** **Mixture balancing:** **interpolating between subsetting and upsampling**\n\nTo mitigate the catastrophic collapse of class-balanced upsampling and upweighting, we propose a\nsimple _mixture method_ which interpolates between subsetting and upsampling. Our method increases\nexposure to majority class data without over-sampling the minority class, which can improve WGA\nand mitigate overfitting to the minority group. We first create a data subset with a specified _class-_\n_imbalance_ _ratio_ by removing data from the larger classes uniformly at random until the desired\n(smaller) ratio is achieved. Next, we perform ERM finetuning on this subset by adjusting sampling\nprobabilities so that mini-batches are balanced in expectation. Using a class-imbalance ratio of 1:1\nreduces to subsetting, and using the original class-imbalance ratio reduces to upsampling.\n\nWe finetune ConvNeXt-V2 Base on Waterbirds and CelebA and BERT Base on CivilComments,\nand we compare our class-balanced mixture method to the subsetting, upsampling, and upweighting\ntechniques. The results of our experiments are displayed in Figure 2. We plot the performance of our\nmixture method with the best class-imbalance ratio during validation; an ablation study varying the\nratio is included in Appendix B. Remarkably, mixture balancing outperforms all three class-balancing\nmethods on Waterbirds and CivilComments, and while it does not outperform subsetting on CelebA,\nit significantly alleviates the WGA collapse experienced by upsampling."}, {"chunk_id": "p007-c002", "page": 7, "section": "Note on validation.** In Figure 2, we plot the best class-imbalance ratio achieved using validation on", "chars": 697, "text": "**Note on validation.** In Figure 2, we plot the best class-imbalance ratio achieved using validation on\na group annotated held-out set. While this is a common assumption in the literature [50, 31, 23, 26],\nit is nevertheless unrealistic when the training set does not have any group annotations. Therefore,\nwe compare with both worst-class accuracy [69] and the _bias-unsupervised validation score_ of [60],\nwhich do not use any group annotations for model selection. In Table 1 we list the method which\nmaximizes each validation metric as well as its average WGA. Overall, we show both methods are\neffective for model selection, often choosing the same method or mixture ratio as WGA validation."}], "not_returned_chunk_ids": [], "remaining_chars": 27452, "remaining_read_calls": 10}

[turn 5] submit_report -> 0 mechanism(s); problems: ['rejected evidence for neurips-2024/e574db41163e700545ff4114f96b3d7a: quote not found in text returned to this episode', 'rejected evidence for neurips-2024/e574db41163e700545ff4114f96b3d7a: quote not found in text returned to this episode', "'Metric-aligned pairwise AUC surrogate': needs read evidence and assumptions/target_fit/limitations/validation_plan", 'rejected evidence for neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6: quote not found in text returned to this episode', 'rejected evidence for neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6: quote not found in text returned to this episode', "'Mixture balancing rather than repeated minority oversampling': needs read evidence and assumptions/target_fit/limitations/validation_plan"]

[turn 6] submit_report -> 1 mechanism(s); problems: ['rejected evidence for neurips-2024/e574db41163e700545ff4114f96b3d7a: quote not found in text returned to this episode', "'Metric-aligned pairwise AUC surrogate': needs read evidence and assumptions/target_fit/limitations/validation_plan", 'rejected evidence for neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6: quote not found in text returned to this episode']

## Report (as injected)

## Cross-domain mechanism suggestions (analogy search on this task's structure)

Structural properties of this task that the suggestions address:
0. The score is a generalized aggregate of global and identity-conditioned ROC-AUCs, so it penalizes particular positive–negative ordering failures that ordinary pointwise binary cross-entropy does not directly target. — evidence: The evaluation defines subgroup, BPSN, and BNSP ROC-AUCs and states that BPSN compares non-toxic subgroup examples with toxic non-subgroup examples; these bias AUCs are aggregated by a generalized mean.
1. A group mention is a training-distribution shortcut correlated with the target but invalid for the metric-defining cross-stratum comparisons; the available training-only group labels make this structure observable. — evidence: The description explicitly says earlier models learned to associate frequently attacked identities with toxicity and gives a benign identity-containing comment as a false-positive pattern; train.csv contains identity columns whereas test.csv contains only comment text and id.
2. Under a six-hour single-GPU first run, metric-critical identity-by-label intersections are rare relative to the 1.8M-row corpus, so uniform updates need not expose enough of the failures that determine the weakest bias AUCs. — evidence: The data preview reports 1,804,874 train rows, many sparse identity columns with 1,399,744 missing entries, and a six-hour cap on one 22-GiB A10.

### Mixture balancing rather than repeated minority oversampling
*Addresses property 2. Source: The Group Robustness is in the Details: Revisiting Finetuning under Spurious Correlations (neurips-2024, `neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6`)*

**Shared problem structure**: Finite fine-tuning updates are allocated across imbalanced strata, and naive upsampling/upweighting can overfit the minority examples and degrade worst-group behavior.
**Object mappings (this pipeline ↔ source)**: spurious feature correlated with class ↔ identity mention correlated with toxicity (Each is predictive in the observed training distribution but harms performance in minority/correlation-breaking groups.); majority/minority class exposure in fine-tuning ↔ common versus rare identity-by-label intersections in minibatches (The first run must allocate exposure under imbalance without repeatedly replaying a small hard stratum.); mixture of subsetting and sampling probabilities ↔ fixed stratified sampler over label-by-identity strata (Both retain some natural-prevalence data while ensuring minority examples occur in expectation.)
**Mechanism in the source**: The paper studies pretrained fine-tuning under spurious correlations and reports that mini-batch upsampling and loss upweighting can decrease worst-group accuracy as epochs proceed. It proposes a mixture between subsetting and upsampling, and reports that it can outperform both on its settings.
**Proposed intervention here**: Instead of uniform sampling, make the one non-standard first-run component a fixed mixture-stratified sampler over the observable label × any-identity-mentioned indicator (and preserve the natural distribution for the remaining batch mass). Use ordinary BCE and the standard single ModernBERT head; cap each sampled stratum at its unique-example count per epoch so rare benign-mentioned comments are not replayed excessively. Expect early and sustained improvement in the held-out bias aggregate, especially BPSN, rather than a late-training collapse.
**Feasibility with the available data**: Feasible: all sampler fields are in train.csv, no test-time group field is required, and it changes data loading rather than model size or inference. It is suitable for a one-A10 run and does not require additional annotations, models, or an ensemble.
**Evidence level**: abstract_only
- `neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6` (abstract only): "the commonly used class-balancing techniques of mini-batch upsampling and loss upweighting can induce a decrease in worst-group accuracy"
**Source assumptions**: The identity columns are sufficiently reliable to define a coarse any-identity stratum, and the validation split contains enough group-labeled examples to detect deterioration. The source mechanism assumes known group structure; here it is available only during training/validation, which is enough for sampling.
**Fit to this task**: Met: train has identity annotations and binary toxicity labels, and the task is pretrained-model fine-tuning under stated spurious identity correlations. The source itself evaluates a BERT on CivilComments, although the adaptation deliberately uses the competition's full overlapping identity structure rather than its collapsed setup.
**Limitations / unknowns**: The source measures worst-group accuracy rather than generalized group-conditioned AUC and its mixture ratio was validation-selected; a hyperparameter sweep is disallowed here, so use one predeclared conservative mixture only. Overlapping identities and fractional annotations make exact mutually exclusive groups unavailable; collapsing to any-identity loses per-identity detail.
**Minimal validation and rejection criterion**: Hold architecture, optimizer, token limit, steps, and BCE fixed; compare uniform sampling to the single predeclared mixture sampler on the official local metric after equal updates. Inspect BPSN/BNSP per identity across checkpoints; reject and revert to uniform sampling if the aggregate does not improve or if any well-supported identity has a consistent late-checkpoint AUC decline.


## Report (raw JSON)

```json
{
  "bottlenecks": [
    {
      "statement": "The score is a generalized aggregate of global and identity-conditioned ROC-AUCs, so it penalizes particular positive–negative ordering failures that ordinary pointwise binary cross-entropy does not directly target.",
      "objects": [
        "comment scoring function",
        "toxicity-positive and toxicity-negative comments",
        "identity-membership indicators",
        "global, subgroup, BPSN, and BNSP AUCs",
        "generalized-mean leaderboard aggregate"
      ],
      "relations": [
        "Each AUC is a probability that a positive receives a higher score than a negative, but the bias AUCs select different identity-by-label intersections before making that comparison.",
        "A pointwise loss can improve full-population discrimination while retaining the BPSN ordering error: benign group-mentioned comments scored above toxic background comments."
      ],
      "evidence": "The evaluation defines subgroup, BPSN, and BNSP ROC-AUCs and states that BPSN compares non-toxic subgroup examples with toxic non-subgroup examples; these bias AUCs are aggregated by a generalized mean."
    },
    {
      "statement": "A group mention is a training-distribution shortcut correlated with the target but invalid for the metric-defining cross-stratum comparisons; the available training-only group labels make this structure observable.",
      "objects": [
        "comment semantic evidence",
        "identity mention",
        "toxicity label",
        "training co-occurrence distribution",
        "identity-by-label strata",
        "ModernBERT fine-tuning objective"
      ],
      "relations": [
        "ERM minimizes average loss and can use identity mention as a predictive proxy for toxicity.",
        "The desired ordering on benign mentioned versus toxic unmentioned comments requires attenuating that proxy, while still recognizing toxic comments that mention an identity."
      ],
      "evidence": "The description explicitly says earlier models learned to associate frequently attacked identities with toxicity and gives a benign identity-containing comment as a false-positive pattern; train.csv contains identity columns whereas test.csv contains only comment text and id."
    },
    {
      "statement": "Under a six-hour single-GPU first run, metric-critical identity-by-label intersections are rare relative to the 1.8M-row corpus, so uniform updates need not expose enough of the failures that determine the weakest bias AUCs.",
      "objects": [
        "1,804,874 training comments",
        "rare identity-by-label intersections",
        "minibatches",
        "single A10 GPU",
        "six-hour execution cap",
        "bias-AUC validation score"
      ],
      "relations": [
        "Uniform sampling follows corpus prevalence rather than the evaluation's cross-stratum comparisons.",
        "Repeated full-corpus training or aggressive oversampling is not a safe first-run response: compute is limited and repeated minority examples can overfit."
      ],
      "evidence": "The data preview reports 1,804,874 train rows, many sparse identity columns with 1,399,744 missing entries, and a six-hour cap on one 22-GiB A10."
    }
  ],
  "mechanisms": [
    {
      "bottleneck_idx": 2,
      "title": "Mixture balancing rather than repeated minority oversampling",
      "paper_ids": [
        "neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6"
      ],
      "object_mappings": [
        {
          "source": "spurious feature correlated with class",
          "target": "identity mention correlated with toxicity",
          "rationale": "Each is predictive in the observed training distribution but harms performance in minority/correlation-breaking groups."
        },
        {
          "source": "majority/minority class exposure in fine-tuning",
          "target": "common versus rare identity-by-label intersections in minibatches",
          "rationale": "The first run must allocate exposure under imbalance without repeatedly replaying a small hard stratum."
        },
        {
          "source": "mixture of subsetting and sampling probabilities",
          "target": "fixed stratified sampler over label-by-identity strata",
          "rationale": "Both retain some natural-prevalence data while ensuring minority examples occur in expectation."
        }
      ],
      "shared_relations": "Finite fine-tuning updates are allocated across imbalanced strata, and naive upsampling/upweighting can overfit the minority examples and degrade worst-group behavior.",
      "mechanism": "The paper studies pretrained fine-tuning under spurious correlations and reports that mini-batch upsampling and loss upweighting can decrease worst-group accuracy as epochs proceed. It proposes a mixture between subsetting and upsampling, and reports that it can outperform both on its settings.",
      "intervention": "Instead of uniform sampling, make the one non-standard first-run component a fixed mixture-stratified sampler over the observable label × any-identity-mentioned indicator (and preserve the natural distribution for the remaining batch mass). Use ordinary BCE and the standard single ModernBERT head; cap each sampled stratum at its unique-example count per epoch so rare benign-mentioned comments are not replayed excessively. Expect early and sustained improvement in the held-out bias aggregate, especially BPSN, rather than a late-training collapse.",
      "feasibility": "Feasible: all sampler fields are in train.csv, no test-time group field is required, and it changes data loading rather than model size or inference. It is suitable for a one-A10 run and does not require additional annotations, models, or an ensemble.",
      "assumptions": "The identity columns are sufficiently reliable to define a coarse any-identity stratum, and the validation split contains enough group-labeled examples to detect deterioration. The source mechanism assumes known group structure; here it is available only during training/validation, which is enough for sampling.",
      "target_fit": "Met: train has identity annotations and binary toxicity labels, and the task is pretrained-model fine-tuning under stated spurious identity correlations. The source itself evaluates a BERT on CivilComments, although the adaptation deliberately uses the competition's full overlapping identity structure rather than its collapsed setup.",
      "limitations": "The source measures worst-group accuracy rather than generalized group-conditioned AUC and its mixture ratio was validation-selected; a hyperparameter sweep is disallowed here, so use one predeclared conservative mixture only. Overlapping identities and fractional annotations make exact mutually exclusive groups unavailable; collapsing to any-identity loses per-identity detail.",
      "validation_plan": "Hold architecture, optimizer, token limit, steps, and BCE fixed; compare uniform sampling to the single predeclared mixture sampler on the official local metric after equal updates. Inspect BPSN/BNSP per identity across checkpoints; reject and revert to uniform sampling if the aggregate does not improve or if any well-supported identity has a consistent late-checkpoint AUC decline.",
      "evidence_refs": [
        {
          "paper_id": "neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6",
          "source": "abstract",
          "quote": "the commonly used class-balancing techniques of mini-batch upsampling and loss upweighting can induce a decrease in worst-group accuracy"
        }
      ],
      "evidence_level": "abstract_only"
    }
  ]
}
```
