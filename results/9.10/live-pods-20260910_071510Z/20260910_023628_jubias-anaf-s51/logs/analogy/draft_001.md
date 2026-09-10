# analogy agent — parent draft (invocation 1)

corpus 5cd1d5e7afd0 (38273 papers) | turns 5 | tokens in/out 81941/4346 | 165s | report

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
### Step 1 — structural properties

1. **The leaderboard objective is a tail-sensitive, subgroup-conditioned ranking objective, not the ordinary example-wise classification loss.**  
   - **Objects:** comment scorer; binary/continuous toxicity target; identity subgroup indicator; overall AUC; subgroup, BPSN, and BNSP AUCs; generalized mean aggregation.  
   - **Relations:** predictions must rank toxic above non-toxic comments not only globally but within, and across, every identity-conditioned slice. Ordinary BCE optimized on the pooled distribution can achieve strong global AUC while assigning elevated scores to benign subgroup examples, which specifically damages BPSN AUC; generalized-mean aggregation emphasizes poorly performing slices.  
   - **Evidence:** Evaluation defines subgroup/BPSN/BNSP AUCs and combines per-identity bias AUCs using a generalized mean; description explicitly identifies benign identity mentions being predicted toxic.

2. **The training signal includes observed subgroup attributes, but deployment/test inputs contain only text; thus the model must improve conditional errors without relying on a test-time subgroup field.**  
   - **Objects:** training comments; toxicity labels; identity-mention columns; held-out comments; text-only predictor; identity-conditioned evaluation subsets.  
   - **Relations:** subgroup annotations can guide training sampling/weighting or constraints, whereas a predictor depending on them as an input cannot be used on test. A pooled model ignores the conditional error structure; a direct metadata-dependent solution violates the deployment input interface.  
   - **Evidence:** `train.csv` “includes toxicity labels and subgroups”; `test.csv` has only `comment_text, id`; evaluation slices are defined by identity mentions.

3. **The labeled corpus is very large relative to a single-A10, six-hour run, so any subgroup-aware correction must work under partial/imbalanced exposure rather than exhaustive expensive fine-tuning.**  
   - **Objects:** 1,804,874 training comments; rare/partially observed identity labels (many nulls); ModernBERT-large; one A10 GPU; 6-hour execution cap; subgroup AUCs.  
   - **Relations:** naïvely processing the entire corpus repeatedly with a large encoder may be infeasible, while uniform subsampling can underrepresent the difficult subgroup × label cross-products that determine BPSN/BNSP ranking. The first method needs a computationally cheap way to allocate training exposure toward those slices.  
   - **Evidence:** train preview reports 1,804,874 rows; identity columns have 1,399,744 nulls; budget is one 22-GiB A10 and 6 hours per solution.

### Step 2 — cross-domain queries

**Property 1**
- `subgroup robust AUC optimization`
- `worst group ranking loss`
- `generalized mean group fairness`
- `cross group pairwise ranking`

**Property 2**
- `privileged information fairness training`
- `training time group labels fairness`
- `attribute aware robust optimization`
- `group DRO conditional risk`

**Property 3**
- `minority group importance sampling`
- `adaptive sampling worst group`
- `rare strata balanced minibatch`
- `distributionally robust data selection`

[turn 1] search_papers('subgroup robust AUC optimization', k=8) ->
     16.17  [iclr-2024] AUC-CL: A Batchsize-Robust Framework for Self-Supervised Contrastive Representation Learning  (iclr-2024/ygmddqb09u)
     15.22  [iccv-2023] Identification of Systematic Errors of Image Classifiers on Rare Subgroups  (iccv-2023/metzenidentificationofsystematicerrorsofimageclassifiersonraresubgroupsiccv2023paper)
     15.16  [icml-2025] From Biased Selective Labels to Pseudo-Labels: An Expectation-Maximization Framework for Learning fr  (icml-2025/chang24e)
     15.14  [neurips-2024] Improving Subgroup Robustness via Data Selection  (neurips-2024/abbbb25cddb2c2cd08714e6bfa2f0634)
     15.11  [icml-2024] From Biased Selective Labels to Pseudo-Labels: An Expectation-Maximization Framework for Learning fr  (icml-2024/chang24e)
     14.49  [neurips-2024] AUCSeg: AUC-oriented Pixel-level Long-tail Semantic Segmentation  (neurips-2024/e574db41163e700545ff4114f96b3d7a)
     14.40  [icml-2025] A Federated Stochastic Multi-level Compositional Minimax Algorithm for Deep AUC Maximization  (icml-2025/zhang24aw)
     14.38  [neurips-2024] AUC Maximization under Positive Distribution Shift  (neurips-2024/3f8c7eb848ffec848f3ed2b7ca44915d)

[turn 1] search_papers('worst group ranking loss', k=8) ->
     18.56  [neurips-2024] On Socially Fair Low-Rank Approximation and Column Subset Selection  (neurips-2024/a1d2eca2159af6978ff2633454d8db81)
     17.51  [neurips-2024] The Group Robustness is in the Details: Revisiting Finetuning under Spurious Correlations  (neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6)
     16.69  [neurips-2024] Group Robust Preference Optimization in Reward-free RLHF  (neurips-2024/4147dfaa46cd7e20a2aecb91097ae8cc)
     16.27  [aaai-2025] Diversity of Structured Domains via k-Kemeny Scores  (aaai-2025/59e326469d45fa5ec2670f6aceec54765c503fb7)
     16.25  [icml-2025] Differentially Private Worst-group Risk Minimization  (icml-2025/zhou24b)
     16.23  [neurips-2025] FairNet: Dynamic Fairness Correction without Performance Loss via Contrastive Conditional LoRA  (neurips-2025/81f2d59479a96afd8056db9468254515)
     16.18  [icml-2024] Differentially Private Worst-group Risk Minimization  (icml-2024/zhou24b)
     15.47  [iclr-2025] MixMax: Distributional Robustness in Function Space via Optimal Data Mixtures  (iclr-2025/dikphooa2d)

[turn 1] search_papers('generalized mean group fairness', k=8) ->
     22.14  [aaai-2024] Towards Fairer Centroids in K-means Clustering  (aaai-2024/3f9d284f2841cdc83484cb11cd9d425c707ca1a5)
     22.07  [aaai-2025] Bayes-Optimal Fair Classification with Multiple Sensitive Features  (aaai-2025/57f6efb4fe18c8f96a93acf5163435a0b250f0d1)
     21.77  [aaai-2025] Fair Bayesian Data Selection via Generalized Discrepancy Measures  (aaai-2025/d4fcd0ede5b01d10d79e4801974e13979e7a649a)
     19.40  [icml-2024] Fair Risk Control: A Generalized Framework for Calibrating Multi-group Fairness Risks  (icml-2024/zhang24be)
     19.40  [icml-2025] Fair Risk Control: A Generalized Framework for Calibrating Multi-group Fairness Risks  (icml-2025/zhang24be)
     19.24  [iclr-2025] Relax and Merge: A Simple Yet Effective Framework for Solving Fair $k$-Means and $k$-sparse Wasserst  (iclr-2025/n8h1z588eu)
     18.61  [aaai-2024] Long-Term Fair Decision Making through Deep Generative Models  (aaai-2024/6bf3a4745889aab27b288d8527602b2e9ed4c039)
     18.49  [neurips-2024] Fair Kernel K-Means: from Single Kernel to Multiple Kernel  (neurips-2024/b48bb4ad31718381838f68bf5f0d4ff1)

[turn 1] search_papers('cross group pairwise ranking', k=8) ->
     17.22  [iclr-2025] A Statistical Framework for Ranking LLM-based Chatbots  (iclr-2025/raoeub6nw2)
     16.25  [neurips-2024] Prediction-Powered Ranking of Large Language Models  (neurips-2024/cd47cd67caa87f5b1944e00f6781598f)
     15.65  [aaai-2025] From Pairwise to Ranking: Climbing the Ladder to Ideal Collaborative Filtering with Pseudo-Ranking  (aaai-2025/27d5e36ead44eeec5a48911c5affcc8d3ab0fe01)
     15.60  [acl-2024] PRP-Graph: Pairwise Ranking Prompting to LLMs with Graph Aggregation for Effective Text Re-ranking  (acl-2024/2024acl-long313)
     15.55  [iclr-2025] Inverse Constitutional AI: Compressing Preferences into Principles  (iclr-2025/9frwkpw3cn)
     15.19  [acl-2025] Are Optimal Algorithms Still Optimal? Rethinking Sorting in LLM-Based Pairwise Ranking with Batching  (acl-2025/2025acl-short83)
     15.10  [neurips-2025] Post Hoc Regression Refinement via Pairwise Rankings  (neurips-2025/00e49fcb98ab1bbf0cdf6cb1cdb84712)
     14.83  [acl-2025] Ranking Unraveled: Recipes for LLM Rankings in Head-to-Head AI Combat  (acl-2025/2025acl-long1265)

[turn 1] search_papers('privileged information fairness training', k=8) ->
     16.54  [neurips-2025] Uncertainty-Sensitive Privileged Learning  (neurips-2025/724711fccb09d4519cbbb6d245d3675d)
     15.84  [iccv-2023] Multi-Frequency Representation Enhancement with Privilege Information for Video Super-Resolution  (iccv-2023/limulti-frequencyrepresentationenhancementwithprivilegeinformationforvideosuper-resolutioniccv2023paper)
     15.58  [iclr-2025] Better than Your Teacher: LLM Agents that learn from Privileged AI Feedback  (iclr-2025/st7xqfgbah)
     15.38  [neurips-2024] Robust Conformal Prediction Using Privileged Information  (neurips-2024/d5ae1c5167be330b90f4c0a1eed7f8f0)
     15.26  [icml-2025] The Fundamental Limits of Least-Privilege Learning  (icml-2025/stadler24a)
     15.21  [neurips-2024] Provable Partially Observable Reinforcement Learning with Privileged Information  (neurips-2024/74d188c51d97fcfbc0269f584d6a53b7)
     15.20  [iclr-2024] Privileged Sensing Scaffolds Reinforcement Learning  (iclr-2024/epve8jajdx)
     15.10  [neurips-2025] Multimodal Tabular Reasoning with Privileged Structured Information  (neurips-2025/99e1098e58285e076d10e81281fdbb40)

[turn 1] search_papers('training time group labels fairness', k=8) ->
     19.81  [neurips-2025] On Group Sufficiency Under Label Bias  (neurips-2025/b78adc1c1558bf344809275854d40fd6)
     18.51  [neurips-2024] Enhancing Robustness of Last Layer Two-Stage Fair Model Corrections  (neurips-2024/fba9133d7fa896ab9414ddd1a6b1ecbf)
     18.11  [aaai-2025] FROC: Building Fair ROC from a Trained Classifier  (aaai-2025/770f3d5748477fdb1a04856827eed0eb120449cb)
     17.83  [iclr-2024] Enhancing Group Fairness in Online Settings Using Oblique Decision Forests  (iclr-2024/e1nxn5qmoe)
     17.72  [neurips-2024] Parameterized Approximation Schemes for Fair-Range Clustering  (neurips-2024/6ee0ebd0983f0926496b7d4e0d48b8e3)
     17.69  [neurips-2025] Fair Minimum Labeling: Efficient Temporal Network Activations for Reachability and Equity  (neurips-2025/01d5b44366f50df931fc14cac12bee60)
     17.67  [icml-2025] FRAPPÉ: A Group Fairness Framework for Post-Processing Everything  (icml-2025/tifrea24a)
     17.66  [icml-2024] FRAPPÉ: A Group Fairness Framework for Post-Processing Everything  (icml-2024/tifrea24a)

[turn 1] search_papers('attribute aware robust optimization', k=8) ->
     12.47  [iclr-2024] Adaptive Sharpness-Aware Pruning for Robust Sparse Networks  (iclr-2024/qfyvvwiam8)
     12.32  [acl-2025] BEDAA: Bayesian Enhanced DeBERTa for Uncertainty-Aware Authorship Attribution  (acl-2025/2025findings-acl924)
     12.05  [neurips-2025] Hybrid-Collaborative Augmentation and Contrastive Sample Adaptive-Differential Awareness for Robust   (neurips-2025/a845c35c57947ce27d7c3f5c2ed5efef)
     11.91  [aaai-2025] RealRep: Generalized SDR-to-HDR Conversion via Attribute-Disentangled Representation Learning  (aaai-2025/821bd206cb55424e6ef98162359278d2d9b7e774)
     11.68  [aaai-2025] Uncovering Pretraining Code in LLMs: A Syntax-Aware Attribution Approach  (aaai-2025/52a173d340100d60e8c0a19d1a9b94318e36a6b2)
     11.40  [aaai-2025] Open-World Deepfake Attribution via Confidence-Aware Asymmetric Learning  (aaai-2025/e5d7074de771fc9159af6eaf7f30aa5d780f87c0)
     10.87  [neurips-2025] LVLM-Driven Attribute-Aware Modeling for Visible-Infrared Person Re-Identification  (neurips-2025/0289f82750cb1ffbdaff7709b63ef122)
     10.69  [icml-2024] Provably Better Explanations with Optimized Aggregation of Feature Attributions  (icml-2024/decker24a)

[turn 1] search_papers('group DRO conditional risk', k=8) ->
     23.41  [iclr-2025] MixMax: Distributional Robustness in Function Space via Optimal Data Mixtures  (iclr-2025/dikphooa2d)
     20.31  [icml-2024] Geometry-Calibrated DRO: Combating Over-Pessimism with Free Energy Implications  (icml-2024/liu24br)
     20.31  [icml-2025] Geometry-Calibrated DRO: Combating Over-Pessimism with Free Energy Implications  (icml-2025/liu24br)
     18.94  [aaai-2024] Large-Scale Non-convex Stochastic Constrained Distributionally Robust Optimization  (aaai-2024/bcca82f18d2dc514fd95d5d9815bbb094d3880ae)
     18.40  [icml-2025] Criterion Collapse and Loss Distribution Control  (icml-2025/holland24a)
     18.35  [icml-2024] Criterion Collapse and Loss Distribution Control  (icml-2024/holland24a)
     18.20  [neurips-2024] Drago: Primal-Dual Coupled Variance Reduction for Faster Distributionally Robust Optimization  (neurips-2024/f2c5a0d8e445cc359eb446521f438ee3)
     17.94  [iclr-2025] Revisiting Large-Scale Non-convex Distributionally Robust Optimization  (iclr-2025/jywvijuna7)

[turn 1] search_papers('minority group importance sampling', k=8) ->
     19.10  [iclr-2024] Like Oil and Water: Group Robustness Methods and Poisoning Defenses May Be at Odds  (iclr-2024/rm9vjpb20f)
     17.56  [iclr-2024] An Investigation of Representation and Allocation Harms in Contrastive Learning  (iclr-2024/q4sidyyqbo)
     16.33  [iclr-2024] Don't Play Favorites: Minority Guidance for Diffusion Models  (iclr-2024/3nmo9ly4jn)
     15.35  [neurips-2025] When majority rules, minority loses: bias amplification of gradient descent  (neurips-2025/2bbc73b3d3c2de43743ce2d82c8f3d7d)
     15.23  [aaai-2024] Who's the (Multi-)Fairest of Them All: Rethinking Interpolation-Based Data Augmentation Through the   (aaai-2024/565377f83dd38dd080b675078e181cf34e5b13c9)
     15.19  [iclr-2024] Language-Interfaced Tabular Oversampling via Progressive Imputation and Self-Authentication  (iclr-2024/8f6bws5jby)
     14.12  [neurips-2024] The Group Robustness is in the Details: Revisiting Finetuning under Spurious Correlations  (neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6)
     13.76  [acl-2024] More than Minorities and Majorities: Understanding Multilateral Bias in Language Generation  (acl-2024/2024findings-acl594)

[turn 1] search_papers('adaptive sampling worst group', k=8) ->
     18.92  [icml-2024] Differentially Private Worst-group Risk Minimization  (icml-2024/zhou24b)
     18.84  [icml-2025] Differentially Private Worst-group Risk Minimization  (icml-2025/zhou24b)
     15.73  [neurips-2024] Group Robust Preference Optimization in Reward-free RLHF  (neurips-2024/4147dfaa46cd7e20a2aecb91097ae8cc)
     15.34  [neurips-2024] The Group Robustness is in the Details: Revisiting Finetuning under Spurious Correlations  (neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6)
     14.54  [icml-2025] Improving Group Robustness on Spurious Correlation Requires Preciser Group Inference  (icml-2025/han24g)
     14.51  [icml-2024] Improving Group Robustness on Spurious Correlation Requires Preciser Group Inference  (icml-2024/han24g)
     14.50  [iclr-2025] Group-robust Sample Reweighting for Subpopulation Shifts via Influence Functions  (iclr-2025/aqj9ifxrl6)
     14.34  [aaai-2024] Towards Fairer Centroids in K-means Clustering  (aaai-2024/3f9d284f2841cdc83484cb11cd9d425c707ca1a5)

[turn 1] search_papers('rare strata balanced minibatch', k=8) ->
     17.11  [iccv-2023] Strata-NeRF : Neural Radiance Fields for Stratified Scenes  (iccv-2023/dhimanstrata-nerfneuralradiancefieldsforstratifiedscenesiccv2023paper)
     14.25  [iclr-2024] SGD Finds then Tunes Features in Two-Layer Neural Networks with near-Optimal Sample Complexity: A Ca  (iclr-2024/hgojlxzb16)
     13.91  [aaai-2024] Towards Stability and Generalization Bounds in Decentralized Minibatch Stochastic Gradient Descent  (aaai-2024/f111d7302652acc103bcb1f305e33363031a6c60)
     13.89  [iclr-2025] Faster Inference of Flow-Based Generative Models via Improved Data-Noise Coupling  (iclr-2025/rsgprjdihh)
     12.42  [aaai-2024] FedCD: Federated Semi-Supervised Learning with Class Awareness Balance via Dual Teachers  (aaai-2024/c9d3fc8ae11bfdb4e8ea6de3ab65b23db3105f15)
     11.73  [neurips-2024] Differentially Private Stochastic Gradient Descent with Fixed-Size Minibatches: Tighter RDP Guarante  (neurips-2024/14fef58f09f2ebe69306e0a322e3be2b)
     11.52  [aaai-2024] MICA: Towards Explainable Skin Lesion Diagnosis via Multi-Level Image-Concept Alignment  (aaai-2024/445a5d47b0cc0958ab4d539c829fd8d4400ce8f3)
     11.39  [aaai-2024] Rare Event Detection in Imbalanced Multi-Class Datasets Using an Optimal MIP-Based Ensemble Weightin  (aaai-2024/af28e894eb1e232acd62d27c77745e06ba49a702)

[turn 1] search_papers('distributionally robust data selection', k=8) ->
     10.97  [aaai-2024] Feature Distribution Matching by Optimal Transport for Effective and Robust Coreset Selection  (aaai-2024/c693b14ba2ce0d08a71eac534767678c79b74666)
     10.84  [neurips-2024] Unveiling the Potential of Robustness in Selecting Conditional Average Treatment Effect Estimators  (neurips-2024/f3da4165893c2465fd7e8df453c41ffa)
     10.68  [neurips-2025] Distributionally Robust Feature Selection  (neurips-2025/5b3f001200198bb4ecaac0a1ea89dd99)
      9.87  [icml-2025] Statistical Inference Under Constrained Selection Bias  (icml-2025/cortes-gomez24a)
      9.87  [icml-2024] Statistical Inference Under Constrained Selection Bias  (icml-2024/cortes-gomez24a)
      9.45  [neurips-2025] Robust Hallucination Detection in LLMs via Adaptive Token Selection  (neurips-2025/b7c43d4a79dede363a2d061c6158e5a5)
      9.37  [neurips-2024] Intrinsic Robustness of Prophet Inequality to Strategic Reward Signaling  (neurips-2024/f3e644506dad33613919fa85af6665d0)
      9.36  [aaai-2024] Learning Robust Rationales for Model Explainability: A Guidance-Based Approach  (aaai-2024/3f26d5af9f84d65fe2d19c61d2dabc22605d0ed6)

[turn 2] read_abstract(['neurips-2024/fba9133d7fa896ab9414ddd1a6b1ecbf', 'neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6', 'neurips-2024/abbbb25cddb2c2cd08714e6bfa2f0634', 'iclr-2025/aqj9ifxrl6']) -> 4 abstracts

[turn 2] search_papers('group DRO balanced sampling spurious correlation', k=10) ->
     30.53  [icml-2024] Prompting is a Double-Edged Sword: Improving Worst-Group Robustness of Foundation Models  (icml-2024/setlur24a)
     29.33  [icml-2025] Prompting is a Double-Edged Sword: Improving Worst-Group Robustness of Foundation Models  (icml-2025/setlur24a)
     27.04  [icml-2024] Unsupervised Concept Discovery Mitigates Spurious Correlations  (icml-2024/arefin24a)
     27.04  [icml-2025] Unsupervised Concept Discovery Mitigates Spurious Correlations  (icml-2025/arefin24a)
     26.51  [neurips-2024] The Group Robustness is in the Details: Revisiting Finetuning under Spurious Correlations  (neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6)
     23.95  [icml-2025] Improving Group Robustness on Spurious Correlation Requires Preciser Group Inference  (icml-2025/han24g)
     23.92  [icml-2024] Improving Group Robustness on Spurious Correlation Requires Preciser Group Inference  (icml-2024/han24g)
     23.21  [iclr-2025] MixMax: Distributional Robustness in Function Space via Optimal Data Mixtures  (iclr-2025/dikphooa2d)
     22.87  [neurips-2025] The Impact of Coreset Selection on Spurious Correlations and Group Robustness  (neurips-2025/8ae3fd80c07b1c5fdc0ce59b55396812-abstract-datasetsandbenchmarkstrackhtml)
     22.81  [neurips-2024] Mitigating Spurious Correlations via Disagreement Probability  (neurips-2024/879c5890a9d2ecdcb590c9674cda4a59)

[turn 2] search_papers('AUC pairwise loss subgroup fairness', k=10) ->
     20.38  [neurips-2024] AUCSeg: AUC-oriented Pixel-level Long-tail Semantic Segmentation  (neurips-2024/e574db41163e700545ff4114f96b3d7a)
     19.49  [neurips-2025] Understanding challenges to the interpretation of disaggregated evaluations of algorithmic fairness  (neurips-2025/3bc4f613b77f59c3998ac83b9a1b5f8a)
     17.89  [aaai-2025] FROC: Building Fair ROC from a Trained Classifier  (aaai-2025/770f3d5748477fdb1a04856827eed0eb120449cb)
     17.87  [aaai-2024] Limited Memory Online Gradient Descent for Kernelized Pairwise Learning with Dynamic Averaging  (aaai-2024/7e62417c144a59928ad55e275e7c99cd608de11a)
     17.62  [iccv-2023] Identification of Systematic Errors of Image Classifiers on Rare Subgroups  (iccv-2023/metzenidentificationofsystematicerrorsofimageclassifiersonraresubgroupsiccv2023paper)
     17.50  [neurips-2024] Enhancing Robustness of Last Layer Two-Stage Fair Model Corrections  (neurips-2024/fba9133d7fa896ab9414ddd1a6b1ecbf)
     17.36  [neurips-2025] Fair Deepfake Detectors Can Generalize  (neurips-2025/4bd8c35573f0a011d84f5bf5c6c887f0)
     17.03  [neurips-2025] Selective Omniprediction and Fair Abstention  (neurips-2025/3826a7e2a07ee41ca42eaf57ed337df4)
     17.02  [neurips-2024] Fairness-Aware Meta-Learning via Nash Bargaining  (neurips-2024/97a0f7d7fc2c26732943860241af1c7a)
     16.38  [aaai-2025] Improved Approximation Algorithms for Clustered TSP and Subgroup Planning  (aaai-2025/08525c387a4a4536f8d1d0dcaee6983f60491d72)

[turn 2] search_papers('groupwise ranking optimization fairness', k=10) ->
     15.29  [icml-2024] Stability and Multigroup Fairness in Ranking with Uncertain Predictions  (icml-2024/devic24a)
     15.14  [icml-2025] Stability and Multigroup Fairness in Ranking with Uncertain Predictions  (icml-2025/devic24a)
     15.12  [neurips-2024] On Socially Fair Low-Rank Approximation and Column Subset Selection  (neurips-2024/a1d2eca2159af6978ff2633454d8db81)
     15.06  [acl-2025] R-Fairness: Assessing Fairness of Ranking in Subjective Data  (acl-2025/2025acl-long1548)
     14.94  [naacl-2024] Do Large Language Models Rank Fairly? An Empirical Study on the Fairness of LLMs as Rankers  (naacl-2024/2024naacl-long319)
     14.41  [iclr-2024] Oracle Efficient Algorithms for Groupwise Regret  (iclr-2024/hrrkc9ei7h)
     13.99  [neurips-2025] Fair Matroid Selection  (neurips-2025/56193e81af44ee5b90b8466e477c30c7)
     13.45  [icml-2025] Fair Federated Learning via the Proportional Veto Core  (icml-2025/ray-chaudhury24a)
     13.43  [icml-2024] Fair Federated Learning via the Proportional Veto Core  (icml-2024/ray-chaudhury24a)
     11.84  [aaai-2025] Breaking the Dyadic Barrier: Rethinking Fairness in Link Prediction Beyond Demographic Parity  (aaai-2025/4c7d2f8db37f3491280c660a9d49a41a7f96cfaa)

[turn 3] read_abstract(['iclr-2025/dikphooa2d', 'neurips-2024/e574db41163e700545ff4114f96b3d7a', 'icml-2024/devic24a', 'icml-2024/setlur24a']) -> 4 abstracts

[turn 3] open_paper({"paper_id": "neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6", "outline_offset": 0}) ->
{"status": "ok", "paper_id": "neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6", "title": "The Group Robustness is in the Details: Revisiting Finetuning under Spurious Correlations", "source_url": "https://papers.nips.cc/paper_files/paper/2024/file/dc4db2ff2c1aefce3b594f821ea82fe6-Paper-Conference.pdf", "pdf_sha256": "f416dafcc09147c92a6ca447b0f45fb811b15da488defb85ddbab2eb43ea0ffc", "text_sha256": "293220512e013c985ea3488224e94d543a70663f35b78689b5c6222d507aab9b", "parser": {"schema": "paper-fulltext-v1", "reader_sha256": "5e308bc98d54a08e8fabb5784c5ec5c3f7b0c84602c16c614fa7d1ac5bf1dc1f", "pymupdf": "1.28.0", "pymupdf4llm": "1.28.0", "pymupdf_layout": "1.28.0", "tabulate": "0.9.0"}, "page_count": 32, "warnings": ["Text extraction only: figures and complex equations may be incomplete; OCR is disabled"], "cache_hit": true, "outline": [{"chunk_id": "p001-c001", "page": 1, "section": "The Group Robustness is in the Details: Revisiting** **Finetuning under Spurious Correlations", "chars": 99}, {"chunk_id": "p001-c002", "page": 1, "section": "Tyler LaBonte** <sup>1</sup> <sup>_∗_</sup> **John C. Hill** <sup>2</sup> **Xinchen Zhang** <sup>2</sup>", "chars": 106}, {"chunk_id": "p001-c003", "page": 1, "section": "Vidya Muthukumar** <sup>2</sup> <sup>_,_</sup> <sup>1</sup> **Abhishek Kumar** <sup>_†_</sup>", "chars": 273}, {"chunk_id": "p001-c004", "page": 1, "section": "Abstract", "chars": 1442}, {"chunk_id": "p001-c005", "page": 1, "section": "1** **Introduction", "chars": 1706}, {"chunk_id": "p002-c001", "page": 2, "section": "1** **Introduction", "chars": 1975}, {"chunk_id": "p002-c002", "page": 2, "section": "1.1** **Related work", "chars": 208}, {"chunk_id": "p002-c003", "page": 2, "section": "Spurious correlations.** The proclivity of ERM to rely on spurious correlations has been widely", "chars": 706}, {"chunk_id": "p002-c004", "page": 2, "section": "Class-balancing and group robustness.** _Group-balancing_, or training with an equal number of", "chars": 1259}, {"chunk_id": "p002-c005", "page": 2, "section": "Overparameterization and distributional robustness.** While the accepted empirical wisdom is", "chars": 390}, {"chunk_id": "p003-c001", "page": 3, "section": "Overparameterization and distributional robustness.** While the accepted empirical wisdom is", "chars": 961}, {"chunk_id": "p003-c002", "page": 3, "section": "2** **Preliminaries", "chars": 23}, {"chunk_id": "p003-c003", "page": 3, "section": "Setting.** We consider classification tasks with input domain R <sup>_n_</sup> and target classes _Y_ _⊂_ N. Suppose", "chars": 1785}, {"chunk_id": "p003-c004", "page": 3, "section": "Class-balancing.** A dataset is considered to be _class-balanced_ if it is composed of an equal number", "chars": 1938}, {"chunk_id": "p003-c005", "page": 3, "section": "Class-balancing.** A dataset is considered to be _class-balanced_ if it is composed of an equal number", "chars": 367}, {"chunk_id": "p004-c001", "page": 4, "section": "Datasets and models.** We study four classification datasets, two in the vision domain and two in", "chars": 1728}, {"chunk_id": "p004-c002", "page": 4, "section": "Datasets and models.** We study four classification datasets, two in the vision domain and two in", "chars": 870}, {"chunk_id": "p004-c003", "page": 4, "section": "3** **Nuanced effects of class-balancing on group robustness", "chars": 218}, {"chunk_id": "p004-c004", "page": 4, "section": "3.1** **Catastrophic collapse of class-balanced upsampling and upweighting", "chars": 1990}, {"chunk_id": "p005-c001", "page": 5, "section": "3.1** **Catastrophic collapse of class-balanced upsampling and upweighting", "chars": 1598}, {"chunk_id": "p005-c002", "page": 5, "section": "3.1** **Catastrophic collapse of class-balanced upsampling and upweighting", "chars": 1783}, {"chunk_id": "p005-c003", "page": 5, "section": "Contextualization with previous work.** Our observations explain the decrease in WGA of CelebA", "chars": 793}, {"chunk_id": "p006-c001", "page": 6, "section": "Contextualization with previous work.** Our observations explain the decrease in WGA of CelebA", "chars": 1489}, {"chunk_id": "p006-c002", "page": 6, "section": "3.2** **Mixture balancing:** **interpolating between subsetting and upsampling", "chars": 1521}, {"chunk_id": "p006-c003", "page": 6, "section": "3.2** **Mixture balancing:** **interpolating between subsetting and upsampling", "chars": 572}, {"chunk_id": "p007-c001", "page": 7, "section": "3.2** **Mixture balancing:** **interpolating between subsetting and upsampling", "chars": 829}, {"chunk_id": "p007-c002", "page": 7, "section": "Note on validation.** In Figure 2, we plot the best class-imbalance ratio achieved using validation on", "chars": 697}, {"chunk_id": "p007-c003", "page": 7, "section": "Contextualization with previous work.** Increasing exposure to majority class data without oversampling the minority class was previously explored by [26], who ", "chars": 837}, {"chunk_id": "p007-c004", "page": 7, "section": "4** **Model scaling improves WGA of class-balanced finetuning", "chars": 1327}, {"chunk_id": "p007-c005", "page": 7, "section": "4** **Model scaling improves WGA of class-balanced finetuning", "chars": 762}], "next_outline_offset": 30, "remaining_chars": 40000, "note": "Opening a paper returns no body text. Use read_paper to obtain citable excerpts."}

[turn 3] open_paper({"paper_id": "iclr-2025/aqj9ifxrl6", "outline_offset": 0}) ->
{"status": "download_error", "paper_id": "iclr-2025/aqj9ifxrl6", "message": "HTTPError: HTTP Error 403: Forbidden", "note": "No full-text evidence returned by this call; read_abstract remains available"}

[turn 3] open_paper({"paper_id": "neurips-2024/fba9133d7fa896ab9414ddd1a6b1ecbf", "outline_offset": 0}) ->
{"status": "timeout", "paper_id": "neurips-2024/fba9133d7fa896ab9414ddd1a6b1ecbf", "message": "PDF download/parse exceeded the paper open budget", "note": "No full-text evidence returned by this call; read_abstract remains available"}

[turn 4] read_paper({"paper_id": "neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6", "chunk_ids": ["p002-c004", "p004-c004", "p005-c001", "p006-c002", "p007-c002"]}) ->
{"status": "ok", "paper_id": "neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6", "pdf_sha256": "f416dafcc09147c92a6ca447b0f45fb811b15da488defb85ddbab2eb43ea0ffc", "text_sha256": "293220512e013c985ea3488224e94d543a70663f35b78689b5c6222d507aab9b", "chunks": [{"chunk_id": "p002-c004", "page": 2, "section": "Class-balancing and group robustness.** _Group-balancing_, or training with an equal number of", "chars": 1259, "text": "**Class-balancing and group robustness.** _Group-balancing_, or training with an equal number of\nsamples from each group, has been proposed as a simple yet effective method to improve robustness\nto spurious correlations [17, 51, 6, 55]. However, group-balancing requires group annotations, which\nare often unknown or problematic to obtain [31, 72, 47, 29]. On the other hand, _class-balancing_, or\ntraining with an equal number of samples from each class, is a well-studied method in long-tailed\nclassification [24, 15, 4]. Recent work has shown that class-balancing is a surprisingly powerful\nmethod for improving worst-group accuracy which does not require group annotations [22, 29, 7, 53].\nIn particular, [22] study the WGA dynamics of two common class-balancing methods: removing data\nfrom the larger classes (which we call _subsetting_ ) and upsampling the smaller classes (which we call\n_upsampling_ ). Our results complement those of [22] and show more nuanced effects of class-balancing\nthan previously known; we provide additional contextualization with [22] in Section 3.1. We show\nsimilar nuanced behavior of _upweighting_ smaller classes in the loss function, a popular method in the\ngroup-balancing setting [31, 47, 55] which [22] did not study."}, {"chunk_id": "p004-c004", "page": 4, "section": "3.1** **Catastrophic collapse of class-balanced upsampling and upweighting", "chars": 1990, "text": "**3.1** **Catastrophic collapse of class-balanced upsampling and upweighting**\n\nIn a recent paper, [29] observed that contrary to the central hypothesis underlying the Just Train\nTwice method [31], the worst-group accuracy of ERM decreases dramatically with training epochs\non CelebA and CivilComments; however, they provide no explanation for this phenomenon. In this\nsection, we show that this degradation of WGA is due to their choice of class-balancing method ( _i.e._,\nupsampling). Specifically, ERM finetuned with upsampling experiences a _catastrophic collapse_ in\ntest WGA over the course of training, a phenomenon that was previously only noticed in synthetic\ndatasets with a linear classifier [22]. Moreover, while [22] state that class-balanced subsetting is not\nrecommended in practice, we show that it can in fact improve WGA conditional on the lack of of a\nsmall minority group _within the majority class_ . Finally, we show that class-balanced upweighting —\na popular technique which [22] do not study — experiences a similar WGA collapse as upsampling.\n\nWe finetune a ConvNeXt-V2 Base on Waterbirds and CelebA and a BERT Base on CivilComments,\nand we compare the subsetting, upsampling, and upweighting techniques to a class-imbalanced\n\n4We note that the Waterbirds dataset is known to contain incorrect labels [56]. We report results on the\noriginal, un-corrected version as is standard in the literature.\n\n5This version of CivilComments has four groups, used in this work and by [50, 22, 23, 26, 29]. There is\nanother version where the identity categories are not collapsed into one spurious feature; that version is used\nby [31, 72, 47]. Both versions use the WILDS split [27].\n\n6To be more specific, we finetune ConvNeXt-V2 Base roughly to a training loss of 10 _−_ 4 on Waterbirds and\n10 <sup>_−_</sup> <sup>3</sup> on CelebA, and BERT Base roughly to a training loss of 10 <sup>_−_</sup> <sup>3</sup> on CivilComments and 10 <sup>_−_</sup> <sup>2</sup> on MultiNLI.\n\n4"}, {"chunk_id": "p005-c001", "page": 5, "section": "3.1** **Catastrophic collapse of class-balanced upsampling and upweighting", "chars": 1598, "text": "(a) Waterbirds (b) CelebA (c) CivilComments\n\nFigure 1: **Class-balanced upsampling and upweighting experience catastrophic collapse.** We\ncompare _subsetting_, wherein data is removed to set every class to the same size as the smallest class,\n_upsampling_, wherein the sampling probabilities of each class are adjusted so that the mini-batches\nare class-balanced in expectation, and _upweighting_, wherein the loss for the smaller classes is scaled\nby the class-imbalance ratio. We observe a catastrophic collapse over the course of training of\nupsampling and upweighting on CelebA and CivilComments, the more class-imbalanced datasets.\nSubsetting reduces WGA on Waterbirds because it removes data from the small minority group\nwithin the majority class. MultiNLI is class-balanced _a priori_, so we do not include it here.\n\nbaseline. Our results are displayed in Figure 1, with additional models in Appendix B. On CelebA and\nCivilComments, the more class-imbalanced datasets, upsampling and upweighting both experience\ncatastrophic collapse over the course of training. We believe this collapse is caused by overfitting\nto the minority group within the minority class; any individual point from this group is sampled far\nmore often during upsampling and weighted far more heavily during upweighting, causing overfitting\nduring long training runs. In fact, upsampling does even worse on CelebA than observed in [29]\nbecause we train 3 _×_ longer to ensure convergence. With that said, optimally tuned early-stopping\nappears to mitigate the collapse (as previously noticed by [22] in a toy setting)."}, {"chunk_id": "p006-c002", "page": 6, "section": "3.2** **Mixture balancing:** **interpolating between subsetting and upsampling", "chars": 1521, "text": "**3.2** **Mixture balancing:** **interpolating between subsetting and upsampling**\n\nTo mitigate the catastrophic collapse of class-balanced upsampling and upweighting, we propose a\nsimple _mixture method_ which interpolates between subsetting and upsampling. Our method increases\nexposure to majority class data without over-sampling the minority class, which can improve WGA\nand mitigate overfitting to the minority group. We first create a data subset with a specified _class-_\n_imbalance_ _ratio_ by removing data from the larger classes uniformly at random until the desired\n(smaller) ratio is achieved. Next, we perform ERM finetuning on this subset by adjusting sampling\nprobabilities so that mini-batches are balanced in expectation. Using a class-imbalance ratio of 1:1\nreduces to subsetting, and using the original class-imbalance ratio reduces to upsampling.\n\nWe finetune ConvNeXt-V2 Base on Waterbirds and CelebA and BERT Base on CivilComments,\nand we compare our class-balanced mixture method to the subsetting, upsampling, and upweighting\ntechniques. The results of our experiments are displayed in Figure 2. We plot the performance of our\nmixture method with the best class-imbalance ratio during validation; an ablation study varying the\nratio is included in Appendix B. Remarkably, mixture balancing outperforms all three class-balancing\nmethods on Waterbirds and CivilComments, and while it does not outperform subsetting on CelebA,\nit significantly alleviates the WGA collapse experienced by upsampling."}, {"chunk_id": "p007-c002", "page": 7, "section": "Note on validation.** In Figure 2, we plot the best class-imbalance ratio achieved using validation on", "chars": 697, "text": "**Note on validation.** In Figure 2, we plot the best class-imbalance ratio achieved using validation on\na group annotated held-out set. While this is a common assumption in the literature [50, 31, 23, 26],\nit is nevertheless unrealistic when the training set does not have any group annotations. Therefore,\nwe compare with both worst-class accuracy [69] and the _bias-unsupervised validation score_ of [60],\nwhich do not use any group annotations for model selection. In Table 1 we list the method which\nmaximizes each validation metric as well as its average WGA. Overall, we show both methods are\neffective for model selection, often choosing the same method or mixture ratio as WGA validation."}], "not_returned_chunk_ids": [], "remaining_chars": 32935, "remaining_read_calls": 11}

[turn 4] read_abstract(['iclr-2025/aqj9ifxrl6', 'neurips-2024/fba9133d7fa896ab9414ddd1a6b1ecbf']) -> 2 abstracts

[turn 5] submit_report -> 2 mechanism(s); problems: ['rejected evidence for neurips-2024/e574db41163e700545ff4114f96b3d7a: quote not found in text returned to this episode', 'rejected evidence for neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6: quote not found in text returned to this episode', 'rejected evidence for neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6: quote not found in text returned to this episode']

## Report (as injected)

## Cross-domain mechanism suggestions (analogy search on this task's structure)

Structural properties of this task that the suggestions address:
0. The score is a generalized-mean aggregation of global and identity-conditioned ROC-AUCs, so pooled pointwise classification training can preserve overall AUC while failing the cross-slice rankings measured by BPSN/BNSP. — evidence: Evaluation explicitly defines Subgroup, BPSN, and BNSP AUC for each identity and aggregates bias AUCs with a generalized mean; the description gives benign identity mentions receiving toxic predictions as the failure case.
1. Identity columns exist only during training, while the deployed scorer receives comment text only; they can supervise allocation of training signal but cannot be inference-time features. — evidence: train.csv is described as including toxicity labels and subgroups, while test.csv preview contains only comment_text and id.
2. With 1.8M rows and a six-hour single-A10 budget, exhaustive large-encoder training and naïve uniform exposure conflict with learning the rare label/subgroup combinations that drive worst conditional rankings. — evidence: The workspace preview reports 1,804,874 train rows and extensive nulls in identity columns; the execution cap is 6 hours on one 22-GiB A10.

### Stratified pairwise AUC surrogate with a bounded negative memory
*Addresses property 0. Source: AUCSeg: AUC-oriented Pixel-level Long-tail Semantic Segmentation (neurips-2024, `neurips-2024/e574db41163e700545ff4114f96b3d7a`)*

**Shared problem structure**: AUC is a pairwise ranking functional under long-tailed strata, whereas minibatch-only estimation lacks enough relevant positive-negative comparisons.
**Object mappings (this pipeline ↔ source)**: pixel-level long-tail labels ↔ toxicity labels within identity-conditioned evaluation subsets (Both create imbalanced positive/negative populations for an ROC-AUC target rather than a thresholded accuracy target.); pairwise inter-instance AUC dependencies ↔ toxic-vs-non-toxic score comparisons in subgroup, BPSN, and BNSP slices (Each target AUC is determined by pairwise score ordering, including pairs crossing membership status.); tail-class memory bank ↔ small FIFO cache of detached positive/negative logits or embeddings per required training stratum (It supplies comparison partners without requiring impractically large minibatches.)
**Mechanism in the source**: AUCSeg replaces a pointwise objective with an AUC-oriented loss for a long-tailed structured prediction task. Because pairwise AUC terms and class imbalance made large batches too memory-expensive, it uses a tail-class memory bank to retain comparison information.
**Proposed intervention here**: Build one non-standard component into the first fine-tune: alongside BCE, add a low-weight, sampled logistic pairwise-ranking term. Construct pairs from train-time identity × binary-toxicity strata that correspond to subgroup, BPSN, and BNSP comparisons, using a capped FIFO bank of detached recent examples to ensure partners; discard the bank and all identity fields at inference. Keep the bank small and fixed rather than increasing batch size or adding a second model.
**Feasibility with the available data**: Feasible on the available text, training-only identity columns, and A10: cached scalar logits (or detached pooled vectors) are negligible relative to ModernBERT memory. It adds pair construction and one loss only; a full pixel-style dependency formulation is neither required nor appropriate.
**Evidence level**: abstract_only
- `neurips-2024/e574db41163e700545ff4114f96b3d7a` (abstract only): "AUC optimization methods have been proposed to improve model performance under long-tail distributions."
- `neurips-2024/e574db41163e700545ff4114f96b3d7a` (abstract only): "we design a Tail-Classes Memory Bank (T-Memory Bank) to manage the significant memory demand."
**Source assumptions**: Validation has sufficient positives and negatives in each selected stratum; identity columns are usable as training-only membership flags; scores, not calibrated thresholds, are submitted. Source evidence is abstract-only, so implementation details of its memory updates are unverified.
**Fit to this task**: The ranking relation and long-tail minibatch problem fit directly. Unlike segmentation, target examples have no within-image dependency, simplifying rather than validating the transfer. The source optimizes generic AUC, not this exact generalized mean of multiple conditional AUCs.
**Limitations / unknowns**: Pairwise loss can be noisy for sparse identities and does not exactly differentiate the leaderboard generalized mean. A cache of embeddings can become stale as encoder parameters change; scalar-score caching is cheaper but less theoretically faithful. Do not claim source-method results on this task.
**Minimal validation and rejection criterion**: Use an article- or time-aware held-out split. Compare BCE-only against BCE plus the fixed low-weight stratified pairwise term under the same step budget; log overall AUC and every subgroup/BPSN/BNSP AUC each epoch. Retain it only if the validation competition metric increases without a material overall-AUC decrease; roll back if pairwise loss raises variance or lowers the generalized bias component.


## Report (raw JSON)

```json
{
  "bottlenecks": [
    {
      "statement": "The score is a generalized-mean aggregation of global and identity-conditioned ROC-AUCs, so pooled pointwise classification training can preserve overall AUC while failing the cross-slice rankings measured by BPSN/BNSP.",
      "objects": [
        "text-only score",
        "toxicity target",
        "identity-conditioned positive/negative subsets",
        "overall/subgroup/BPSN/BNSP AUC",
        "generalized mean"
      ],
      "relations": [
        "The evaluator compares score orderings within and across subgroup membership; pooled BCE has no direct pairwise term for these conditional rankings, and generalized-mean aggregation makes a poor slice disproportionately costly."
      ],
      "evidence": "Evaluation explicitly defines Subgroup, BPSN, and BNSP AUC for each identity and aggregates bias AUCs with a generalized mean; the description gives benign identity mentions receiving toxic predictions as the failure case."
    },
    {
      "statement": "Identity columns exist only during training, while the deployed scorer receives comment text only; they can supervise allocation of training signal but cannot be inference-time features.",
      "objects": [
        "training identity annotations",
        "training toxicity label",
        "test comment text",
        "test-time score",
        "identity-conditioned evaluation"
      ],
      "relations": [
        "A valid method may use membership to construct losses or sampling strata during fine-tuning, but must discard membership at inference because test.csv has no such fields."
      ],
      "evidence": "train.csv is described as including toxicity labels and subgroups, while test.csv preview contains only comment_text and id."
    },
    {
      "statement": "With 1.8M rows and a six-hour single-A10 budget, exhaustive large-encoder training and naïve uniform exposure conflict with learning the rare label/subgroup combinations that drive worst conditional rankings.",
      "objects": [
        "large fine-tuning corpus",
        "minority label/group cells",
        "ModernBERT-large",
        "single A10 and six-hour cap",
        "conditional AUC validation"
      ],
      "relations": [
        "Uniform sampling can leave hard cells underexposed; repeated oversampling/upweighting can overfit them. The first run needs a bounded data-allocation mechanism rather than a large optimization stack."
      ],
      "evidence": "The workspace preview reports 1,804,874 train rows and extensive nulls in identity columns; the execution cap is 6 hours on one 22-GiB A10."
    }
  ],
  "mechanisms": [
    {
      "bottleneck_idx": 0,
      "title": "Stratified pairwise AUC surrogate with a bounded negative memory",
      "paper_ids": [
        "neurips-2024/e574db41163e700545ff4114f96b3d7a"
      ],
      "object_mappings": [
        {
          "source": "pixel-level long-tail labels",
          "target": "toxicity labels within identity-conditioned evaluation subsets",
          "rationale": "Both create imbalanced positive/negative populations for an ROC-AUC target rather than a thresholded accuracy target."
        },
        {
          "source": "pairwise inter-instance AUC dependencies",
          "target": "toxic-vs-non-toxic score comparisons in subgroup, BPSN, and BNSP slices",
          "rationale": "Each target AUC is determined by pairwise score ordering, including pairs crossing membership status."
        },
        {
          "source": "tail-class memory bank",
          "target": "small FIFO cache of detached positive/negative logits or embeddings per required training stratum",
          "rationale": "It supplies comparison partners without requiring impractically large minibatches."
        }
      ],
      "shared_relations": "AUC is a pairwise ranking functional under long-tailed strata, whereas minibatch-only estimation lacks enough relevant positive-negative comparisons.",
      "mechanism": "AUCSeg replaces a pointwise objective with an AUC-oriented loss for a long-tailed structured prediction task. Because pairwise AUC terms and class imbalance made large batches too memory-expensive, it uses a tail-class memory bank to retain comparison information.",
      "intervention": "Build one non-standard component into the first fine-tune: alongside BCE, add a low-weight, sampled logistic pairwise-ranking term. Construct pairs from train-time identity × binary-toxicity strata that correspond to subgroup, BPSN, and BNSP comparisons, using a capped FIFO bank of detached recent examples to ensure partners; discard the bank and all identity fields at inference. Keep the bank small and fixed rather than increasing batch size or adding a second model.",
      "feasibility": "Feasible on the available text, training-only identity columns, and A10: cached scalar logits (or detached pooled vectors) are negligible relative to ModernBERT memory. It adds pair construction and one loss only; a full pixel-style dependency formulation is neither required nor appropriate.",
      "assumptions": "Validation has sufficient positives and negatives in each selected stratum; identity columns are usable as training-only membership flags; scores, not calibrated thresholds, are submitted. Source evidence is abstract-only, so implementation details of its memory updates are unverified.",
      "target_fit": "The ranking relation and long-tail minibatch problem fit directly. Unlike segmentation, target examples have no within-image dependency, simplifying rather than validating the transfer. The source optimizes generic AUC, not this exact generalized mean of multiple conditional AUCs.",
      "limitations": "Pairwise loss can be noisy for sparse identities and does not exactly differentiate the leaderboard generalized mean. A cache of embeddings can become stale as encoder parameters change; scalar-score caching is cheaper but less theoretically faithful. Do not claim source-method results on this task.",
      "validation_plan": "Use an article- or time-aware held-out split. Compare BCE-only against BCE plus the fixed low-weight stratified pairwise term under the same step budget; log overall AUC and every subgroup/BPSN/BNSP AUC each epoch. Retain it only if the validation competition metric increases without a material overall-AUC decrease; roll back if pairwise loss raises variance or lowers the generalized bias component.",
      "evidence_refs": [
        {
          "paper_id": "neurips-2024/e574db41163e700545ff4114f96b3d7a",
          "source": "abstract",
          "quote": "AUC optimization methods have been proposed to improve model performance under long-tail distributions."
        },
        {
          "paper_id": "neurips-2024/e574db41163e700545ff4114f96b3d7a",
          "source": "abstract",
          "quote": "we design a Tail-Classes Memory Bank (T-Memory Bank) to manage the significant memory demand."
        }
      ],
      "evidence_level": "abstract_only"
    },
    {
      "bottleneck_idx": 2,
      "title": "Mixture balancing instead of repeated minority upsampling",
      "paper_ids": [
        "neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6"
      ],
      "object_mappings": [
        {
          "source": "classification classes and minority-within-class groups",
          "target": "toxicity label and identity-conditioned label cells",
          "rationale": "The difficult score errors occur where a label is sparsely represented conditional on subgroup membership."
        },
        {
          "source": "subsetting followed by class-balanced sampling",
          "target": "cap the dominant pooled training strata, then sample toxicity labels evenly from that retained first-run subset",
          "rationale": "This raises exposure to informative rare cases without repeatedly replaying the smallest cells."
        },
        {
          "source": "worst-group accuracy validation",
          "target": "generalized-mean subgroup/BPSN/BNSP AUC validation",
          "rationale": "Both are held-out group-sensitive criteria used to select against pooled-risk performance."
        }
      ],
      "shared_relations": "Overexposure from upsampling or loss weighting can overfit rare cells, while full subsetting discards useful majority data; an intermediate retained-data mixture controls the trade-off under constrained fine-tuning.",
      "mechanism": "The source compares subsetting, upsampling, and loss upweighting under spurious correlations, including a text benchmark. It finds late-training worst-group collapse for upsampling/upweighting and proposes mixture balancing: first reduce the majority class to a chosen finite ratio, then use balanced minibatches on that subset.",
      "intervention": "Make the first run's single sampling commitment a mixture sampler: form a capped retained pool by downsampling the overwhelmingly common toxicity class, while preserving all available rare identity-conditioned cells, then draw label-balanced minibatches from that pool. Do not apply large per-example inverse-frequency weights or unlimited duplication; select one conservative retention ratio before the run, not via hyperparameter search. Use identity fields only to protect rare cells during pool construction, never as model inputs.",
      "feasibility": "Feasible and compute-reducing: it requires only a preprocessing index and weighted sampler, uses existing CSV columns, and can reduce encoder steps within six hours. It does not need external annotations or test-time subgroup membership.",
      "assumptions": "A local held-out split with identity flags can be made before sampling; the target's toxicity binarization used to define strata matches the competition evaluation convention; rare cells are large enough to be retained rather than synthetically created.",
      "target_fit": "Training has group annotations and evaluation is group-conditioned, satisfying the method's key requirement. The source explicitly includes CivilComments/BERT experiments, which supports relevance but is not cross-subfield evidence; the allocation mechanism itself is generic robust fine-tuning. Test-time fields are not needed.",
      "limitations": "The paper's reported criterion is worst-group accuracy, not conditional AUC/generalized mean, and its mixture ratio was selected using validation. Here only one conservative ratio is allowed for the first candidate, so its optimality is unknown. Source results also show that overly aggressive subsetting can hurt when it removes a small group embedded in a majority class.",
      "validation_plan": "Using a fixed held-out split, compare the fixed mixture sampler with uniform sampling at identical optimizer steps and sequence length. Track per-epoch generalized bias metric, its worst identity/slice, and global AUC. Keep mixture sampling only if the bias metric is higher or more stable by the end of the run; roll back if retained-pool restriction lowers both global AUC and the generalized bias metric, or if any protected rare cell disappears from the pool.",
      "evidence_refs": [
        {
          "paper_id": "neurips-2024/dc4db2ff2c1aefce3b594f821ea82fe6",
          "source": "full_text",
          "quote": "upsampling and upweighting both experience catastrophic collapse over the course of training.",
          "chunk_id": "p005-c001",
          "page": 5,
          "section": "3.1** **Catastrophic collapse of class-balanced upsampling and upweighting",
          "pdf_sha256": "f416dafcc09147c92a6ca447b0f45fb811b15da488defb85ddbab2eb43ea0ffc",
          "text_sha256": "293220512e013c985ea3488224e94d543a70663f35b78689b5c6222d507aab9b"
        }
      ],
      "evidence_level": "full_text"
    }
  ]
}
```
