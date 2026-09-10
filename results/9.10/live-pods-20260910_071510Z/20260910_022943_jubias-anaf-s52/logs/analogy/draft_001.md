# analogy agent — parent draft (invocation 1)

corpus 5cd1d5e7afd0 (38273 papers) | turns 5 | tokens in/out 93807/4340 | 138s | report

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
**Structural properties**

1. **The leaderboard score is a tail-sensitive, subgroup-conditioned ranking objective, not the ordinary example-averaged classification objective.**  
   - **Objects:** comment scorer; toxicity label; identity-membership attributes; overall ROC-AUC; subgroup, BPSN, and BNSP AUCs; generalized/power mean aggregation.  
   - **Relations:** predictions must preserve toxic/non-toxic ordering both globally and in three identity-conditioned cross-groups. An ordinary BCE-trained scorer can attain high global AUC while systematically ranking non-toxic identity-mentioned inputs above toxic background inputs (BPSN failure), and the generalized mean disproportionately penalizes weak subgroup metrics.  
   - **Evidence:** Evaluation defines overall AUC plus Subgroup, BPSN, and BNSP AUC per identity, then a generalized mean of bias AUCs; description explicitly identifies false toxicity association with identity mentions.

2. **The training target is an aggregated, continuous annotation signal rather than an unambiguous binary ground truth, while evaluation ranks examples by toxicity.**  
   - **Objects:** individual rater judgments; aggregated toxicity target in `train.csv`; binary/ranking evaluation partition; learned score.  
   - **Relations:** hard thresholding or treating every aggregate target as equally certain discards disagreement/ambiguity information, yet the AUC evaluation rewards correct ordering around the effective toxic/non-toxic distinction. A naive hard-label classifier may overfit noisy borderline examples.  
   - **Evidence:** description discusses multiple raters and judgments; training preview includes judgment-derived count columns (`funny`, `disagree`) and the known competition format provides continuous toxicity labels; evaluation is ROC-AUC based.

3. **The available labeled corpus is very large relative to a single-GPU first-run budget, but the test output requires coverage over all comments.**  
   - **Objects:** 1,804,874 training rows; single A10 22 GiB; 6-hour per-solution cap; pretrained encoder; 97,320 test rows.  
   - **Relations:** naive full-corpus, long-context fine-tuning can consume the first-run budget before a validated submission; sampling or staged optimization must retain the rare/error-critical conditional groups rather than merely shrinking data uniformly.  
   - **Evidence:** workspace lists 1,804,874 training examples; resource cap is 6 hours on one A10; score explicitly hinges on identity-conditioned subsets.

**Queries**

- Property 1: `worst group risk optimization`; `group DRO classification`; `AUC subgroup fairness surrogate`; `pairwise ranking equalized odds`
- Property 2: `soft labels annotator disagreement`; `crowd label uncertainty learning`; `label distribution learning ranking`; `ambiguous labels confidence weighting`
- Property 3: `rare group stratified sampling`; `importance sampling group robustness`; `coreset worst group optimization`; `efficient group DRO minibatch`

[turn 1] search_papers('worst group risk optimization', k=8) ->
     24.61  [icml-2025] Differentially Private Worst-group Risk Minimization  (icml-2025/zhou24b)
     24.58  [icml-2024] Differentially Private Worst-group Risk Minimization  (icml-2024/zhou24b)
     18.60  [iclr-2025] MixMax: Distributional Robustness in Function Space via Optimal Data Mixtures  (iclr-2025/dikphooa2d)
     17.39  [icml-2025] Improving Group Robustness on Spurious Correlation Requires Preciser Group Inference  (icml-2025/han24g)
     17.33  [icml-2024] Improving Group Robustness on Spurious Correlation Requires Preciser Group Inference  (icml-2024/han24g)
     17.29  [iclr-2025] Group Distributionally Robust Dataset Distillation with Risk Minimization  (iclr-2025/3jsu5qxnru)
     16.27  [neurips-2024] Soft-Label Integration for Robust Toxicity Classification  (neurips-2024/ac4c13a5c6ec1bba68c9ce1d908321d2)
     16.11  [icml-2025] Controllable Prompt Tuning For Balancing Group Distributional Robustness  (icml-2025/phan24b)

[turn 1] search_papers('group DRO classification', k=8) ->
     20.26  [iclr-2025] MixMax: Distributional Robustness in Function Space via Optimal Data Mixtures  (iclr-2025/dikphooa2d)
     18.49  [aaai-2025] Harnessing Diffusion-Generated Synthetic Images for Fair Image Classification  (aaai-2025/e934049906863cc3ca1b86d8afabd4f3b4551d56)
     17.07  [iclr-2025] An Effective Manifold-based Optimization Method for Distributionally Robust Classification  (iclr-2025/nzjsvvzbip)
     16.11  [neurips-2025] Bootstrap Your Uncertainty: Adaptive Robust Classification Driven by Optimal-Transport  (neurips-2025/847af45e97918513aaabc97b2b8bd55c)
     15.99  [neurips-2024] Outlier-Robust Distributionally Robust Optimization via Unbalanced Optimal Transport  (neurips-2024/5d68a3f05ee2aae6a0fb2d94959082a0)
     15.02  [neurips-2024] Drago: Primal-Dual Coupled Variance Reduction for Faster Distributionally Robust Optimization  (neurips-2024/f2c5a0d8e445cc359eb446521f438ee3)
     14.54  [icml-2025] Geometry-Calibrated DRO: Combating Over-Pessimism with Free Energy Implications  (icml-2025/liu24br)
     14.54  [icml-2024] Geometry-Calibrated DRO: Combating Over-Pessimism with Free Energy Implications  (icml-2024/liu24br)

[turn 1] search_papers('AUC subgroup fairness surrogate', k=8) ->
     19.49  [neurips-2025] Understanding challenges to the interpretation of disaggregated evaluations of algorithmic fairness  (neurips-2025/3bc4f613b77f59c3998ac83b9a1b5f8a)
     18.29  [iclr-2024] Fair Classifiers that Abstain without Harm  (iclr-2024/jvvegabkvx)
     17.62  [iccv-2023] Identification of Systematic Errors of Image Classifiers on Rare Subgroups  (iccv-2023/metzenidentificationofsystematicerrorsofimageclassifiersonraresubgroupsiccv2023paper)
     17.50  [neurips-2024] Enhancing Robustness of Last Layer Two-Stage Fair Model Corrections  (neurips-2024/fba9133d7fa896ab9414ddd1a6b1ecbf)
     16.17  [iclr-2025] No Location Left Behind: Measuring and Improving the Fairness of Implicit Representations for Earth   (iclr-2025/hszaciznb2)
     15.89  [icml-2024] Feature Importance Disparities for Data Bias Investigations  (icml-2024/chang24a)
     15.87  [aaai-2025] FROC: Building Fair ROC from a Trained Classifier  (aaai-2025/770f3d5748477fdb1a04856827eed0eb120449cb)
     15.86  [icml-2025] Feature Importance Disparities for Data Bias Investigations  (icml-2025/chang24a)

[turn 1] search_papers('pairwise ranking equalized odds', k=8) ->
     20.73  [neurips-2025] Kernel-based Equalized Odds: A Quantification of Accuracy-Fairness Trade-off in Fair Representation   (neurips-2025/85a47d32fbf29bb8d42cdd980b719959)
     20.33  [neurips-2024] Prediction-Powered Ranking of Large Language Models  (neurips-2024/cd47cd67caa87f5b1944e00f6781598f)
     19.22  [neurips-2025] Towards a Pairwise Ranking Model with Orderliness and Monotonicity for Label Enhancement  (neurips-2025/49367cf64d14cd5f38220601580f0bb2)
     17.49  [iclr-2024] Post-hoc bias scoring is optimal for fair classification  (iclr-2024/fm5xfcar2y)
     15.65  [aaai-2025] From Pairwise to Ranking: Climbing the Ladder to Ideal Collaborative Filtering with Pseudo-Ranking  (aaai-2025/27d5e36ead44eeec5a48911c5affcc8d3ab0fe01)
     15.60  [acl-2024] PRP-Graph: Pairwise Ranking Prompting to LLMs with Graph Aggregation for Effective Text Re-ranking  (acl-2024/2024acl-long313)
     15.19  [acl-2025] Are Optimal Algorithms Still Optimal? Rethinking Sorting in LLM-Based Pairwise Ranking with Batching  (acl-2025/2025acl-short83)
     15.10  [neurips-2025] Post Hoc Regression Refinement via Pairwise Rankings  (neurips-2025/00e49fcb98ab1bbf0cdf6cb1cdb84712)

[turn 1] search_papers('soft labels annotator disagreement', k=8) ->
     22.63  [naacl-2024] The Perspectivist Paradigm Shift: Assumptions and Challenges of Capturing Human Labels  (naacl-2024/2024naacl-long126)
     20.41  [neurips-2025] Pairwise Calibrated Rewards for Pluralistic Alignment  (neurips-2025/53dbd7e34fab703a639964e2d3ee9e84)
     20.37  [acl-2025] Mining the uncertainty patterns of humans and models in the annotation of moral foundations and huma  (acl-2025/2025acl-long1116)
     20.07  [neurips-2024] Mitigating Spurious Correlations via Disagreement Probability  (neurips-2024/879c5890a9d2ecdcb590c9674cda4a59)
     18.70  [naacl-2025] Fine-grained Fallacy Detection with Human Label Variation  (naacl-2025/2025naacl-long34)
     18.69  [neurips-2024] Soft-Label Integration for Robust Toxicity Classification  (neurips-2024/ac4c13a5c6ec1bba68c9ce1d908321d2)
     18.54  [acl-2025] Towards Multi-Perspective NLP Systems: A Thesis Proposal  (acl-2025/2025acl-srw30)
     18.12  [naacl-2024] GRASP: A Disagreement Analysis Framework to Assess Group Associations in Perspectives  (naacl-2024/2024naacl-long190)

[turn 1] search_papers('crowd label uncertainty learning', k=8) ->
     24.27  [iccv-2023] Calibrating Uncertainty for Semi-Supervised Crowd Counting  (iccv-2023/licalibratinguncertaintyforsemi-supervisedcrowdcountingiccv2023paper)
     18.02  [aaai-2025] Label Aggregation for Composite Crowd Tasks by Worker Ability Constraint Satisfaction  (aaai-2025/3ad43ed8384f086e26e02583a30ce6d9432f1967)
     17.95  [aaai-2024] Explainable Origin-Destination Crowd Flow Interpolation via Variational Multi-Modal Recurrent Graph   (aaai-2024/16e9a10ac7a83d80cb6538d9fbefece51b0a6657)
     16.84  [aaai-2024] Mixture of Experts based Multi-task Supervise Learning from Crowds  (aaai-2024/106519ce482a21e3ce000339638b31f5e71463f1)
     14.49  [neurips-2024] Noisy Label Learning with Instance-Dependent Outliers: Identifiability via Crowd Wisdom  (neurips-2024/b05e6a11df6eacb600074a42bb28ae52)
     13.34  [iccv-2023] Counting Crowds in Bad Weather  (iccv-2023/huangcountingcrowdsinbadweathericcv2023paper)
     13.24  [neurips-2025] Embodied Crowd Counting  (neurips-2025/6aa3267e3a0f7c2c718036d08d482a51)
     13.00  [iccv-2023] Point-Query Quadtree for Crowd Counting, Localization, and More  (iccv-2023/liupoint-queryquadtreeforcrowdcountinglocalizationandmoreiccv2023paper)

[turn 1] search_papers('label distribution learning ranking', k=8) ->
     15.26  [neurips-2025] Towards a Pairwise Ranking Model with Orderliness and Monotonicity for Label Enhancement  (neurips-2025/49367cf64d14cd5f38220601580f0bb2)
     14.46  [neurips-2025] RankMatch: A Novel Approach to Semi-Supervised Label Distribution Learning Leveraging Rank Correlati  (neurips-2025/e7cc7f2467171d81b7224eae1373c493)
     13.83  [neurips-2025] ComRank: Ranking Loss for Multi-Label Complementary Label Learning  (neurips-2025/adedc33539eafdf3d2c14a5e0032db6e)
     12.37  [naacl-2024] Multi-stage Retrieve and Re-rank Model for Automatic Medical Coding Recommendation  (naacl-2024/2024naacl-long273)
     11.81  [aaai-2025] Generalization Bounds for Semi-supervised Matrix Completion with Distributional Side Information  (aaai-2025/23d07cd9111eefc2c4e29043362bae102dba076e)
     11.78  [aaai-2025] Multi-Label Ranking Loss Minimization for Matrix Completion  (aaai-2025/d9bcb53d01f997df3ef0312058bce7c7617cae9d)
     11.58  [aaai-2025] Towards Better IncomLDL: We Are Unaware of Hidden Labels in Advance  (aaai-2025/acd1436bc1ce0d6e95365b6a82b4d359fc6603ee)
     11.54  [acl-2025] Efficient Safety Alignment of Large Language Models via Preference Re-ranking and Representation-bas  (acl-2025/2025acl-long1504)

[turn 1] search_papers('ambiguous labels confidence weighting', k=8) ->
     20.73  [aaai-2025] DiCaP: Distribution-Calibrated Pseudo-labeling for Semi-Supervised Multi-Label Learning  (aaai-2025/9cfb65337c1abc76e8eac7b42836aa0f0c02c971)
     18.90  [neurips-2025] MIDAS: Misalignment-based Data Augmentation Strategy for Imbalanced Multimodal Learning  (neurips-2025/d8fd66773e754db9871e8331137c3339)
     17.03  [aaai-2025] Perceive, Act and Correct: Confidence Is Not Enough for Hyperspectral Classification  (aaai-2025/f3f41812ccdbfb9a86a105a5e5f4b525e0d31ccf)
     15.02  [aaai-2025] Calibrated Disambiguation for Partial Multi-label Learning  (aaai-2025/e0260a1775ddee34b5df1667822f8f30f8647af8)
     15.00  [aaai-2025] Navigating Label Ambiguity for Facial Expression Recognition in the Wild  (aaai-2025/2270118a484b2df9f8aa37a0c20f117ca8ba8099)
     14.79  [aaai-2024] RepFace: Refining Closed-Set Noise with Progressive Label Correction for Face Recognition  (aaai-2024/84974dd2cedffc27b024165e31a100a9d4e679d1)
     14.70  [aaai-2024] Distilling Reliable Knowledge for Instance-Dependent Partial Label Learning  (aaai-2024/870552b15681a726a6e54165b427635d3557c653)
     14.40  [naacl-2024] When Quantization Affects Confidence of Large Language Models?  (naacl-2024/2024findings-naacl124)

[turn 1] search_papers('rare group stratified sampling', k=8) ->
     17.68  [aaai-2024] Using Stratified Sampling to Improve LIME Image Explanations  (aaai-2024/0572aa74eb83ffb591d2d6310dd1ad662e889476)
     16.49  [aaai-2025] Stratified Knowledge-Density Super-Network for Scalable Vision Transformers  (aaai-2025/2db9b499c2b22da2d1cef3bcbee66f1cd2486185)
     16.34  [iclr-2025] Aioli: A Unified Optimization Framework for Language Model Data Mixing  (iclr-2025/szgzjhanse)
     15.14  [neurips-2024] Stratified Prediction-Powered Inference for Effective Hybrid Evaluation of Language Models  (neurips-2024/c9fcd02e6445c7dfbad6986abee53d0d)
     14.97  [neurips-2025] Stratify or Die: Rethinking Data Splits in Image Segmentation  (neurips-2025/69a2ebb622b999be1cb932aceea5a236)
     13.50  [neurips-2025] Beyond the Average: Distributional Causal Inference under Imperfect Compliance  (neurips-2025/62fe03e97f70b2d004d684d707d990eb)
     13.40  [aaai-2025] VarDrop: Enhancing Training Efficiency by Reducing Variate Redundancy in Periodic Time Series Foreca  (aaai-2025/617566f5aefed19aeb16b22812b5750462a19f69)
     13.28  [aaai-2024] Stratified GNN Explanations through Sufficient Expansion  (aaai-2024/24a1674e332118a0322784060fc3f3ca0c4f10be)

[turn 1] search_papers('importance sampling group robustness', k=8) ->
     15.01  [neurips-2025] The Impact of Coreset Selection on Spurious Correlations and Group Robustness  (neurips-2025/8ae3fd80c07b1c5fdc0ce59b55396812-abstract-datasetsandbenchmarkstrackhtml)
     13.36  [iclr-2024] Like Oil and Water: Group Robustness Methods and Poisoning Defenses May Be at Odds  (iclr-2024/rm9vjpb20f)
     13.33  [iclr-2025] Group-robust Sample Reweighting for Subpopulation Shifts via Influence Functions  (iclr-2025/aqj9ifxrl6)
     13.03  [neurips-2024] Group Robust Preference Optimization in Reward-free RLHF  (neurips-2024/4147dfaa46cd7e20a2aecb91097ae8cc)
     11.95  [icml-2024] Efficient Algorithms for Empirical Group Distributionally Robust Optimization and Beyond  (icml-2024/yu24a)
     11.92  [icml-2025] Efficient Algorithms for Empirical Group Distributionally Robust Optimization and Beyond  (icml-2025/yu24a)
     11.90  [neurips-2025] GRAPE: Optimize Data Mixture for Group Robust Multi-target Adaptive Pretraining  (neurips-2025/e7bba023351f8262c22e3328e42645ec)
     11.88  [aaai-2025] Boosting Test Performance with Importance Sampling-a Subpopulation Perspective  (aaai-2025/150b28ab6b1d5a47f8126f1073afdf668e5bb9f6)

[turn 1] search_papers('coreset worst group optimization', k=8) ->
     19.46  [neurips-2025] The Impact of Coreset Selection on Spurious Correlations and Group Robustness  (neurips-2025/8ae3fd80c07b1c5fdc0ce59b55396812-abstract-datasetsandbenchmarkstrackhtml)
     17.87  [icml-2025] Differentially Private Worst-group Risk Minimization  (icml-2025/zhou24b)
     17.78  [icml-2024] Differentially Private Worst-group Risk Minimization  (icml-2024/zhou24b)
     16.81  [naacl-2025] TAGCOS: Task-agnostic Gradient Clustered Coreset Selection for Instruction Tuning Data  (naacl-2025/2025findings-naacl264)
     16.11  [aaai-2024] Feature Distribution Matching by Optimal Transport for Effective and Robust Coreset Selection  (aaai-2024/c693b14ba2ce0d08a71eac534767678c79b74666)
     16.11  [icml-2025] Controllable Prompt Tuning For Balancing Group Distributional Robustness  (icml-2025/phan24b)
     16.04  [icml-2024] Controllable Prompt Tuning For Balancing Group Distributional Robustness  (icml-2024/phan24b)
     15.92  [icml-2024] Refined Coreset Selection: Towards Minimal Coreset Size under Model Performance Constraints  (icml-2024/xia24b)

[turn 1] search_papers('efficient group DRO minibatch', k=8) ->
     20.26  [iclr-2025] MixMax: Distributional Robustness in Function Space via Optimal Data Mixtures  (iclr-2025/dikphooa2d)
     15.82  [neurips-2024] Wasserstein Distributionally Robust Optimization through the Lens of Structural Causal Models and In  (neurips-2024/4ae5cdacb9152d95661bc3c620b75aba)
     14.92  [aaai-2024] Towards Stability and Generalization Bounds in Decentralized Minibatch Stochastic Gradient Descent  (aaai-2024/f111d7302652acc103bcb1f305e33363031a6c60)
     14.90  [iclr-2025] Faster Inference of Flow-Based Generative Models via Improved Data-Noise Coupling  (iclr-2025/rsgprjdihh)
     14.54  [icml-2025] Geometry-Calibrated DRO: Combating Over-Pessimism with Free Energy Implications  (icml-2025/liu24br)
     14.54  [icml-2024] Geometry-Calibrated DRO: Combating Over-Pessimism with Free Energy Implications  (icml-2024/liu24br)
     14.20  [neurips-2024] Outlier-Robust Distributionally Robust Optimization via Unbalanced Optimal Transport  (neurips-2024/5d68a3f05ee2aae6a0fb2d94959082a0)
     13.75  [neurips-2025] Multi-Expert Distributionally Robust Optimization for Out-of-Distribution Generalization  (neurips-2025/929814ae1e76ae131a473e3f30609fef)

[turn 2] read_abstract(['iclr-2025/dikphooa2d', 'icml-2024/yu24a', 'iclr-2025/aqj9ifxrl6', 'aaai-2025/150b28ab6b1d5a47f8126f1073afdf668e5bb9f6']) -> 4 abstracts

[turn 2] read_abstract(['neurips-2024/ac4c13a5c6ec1bba68c9ce1d908321d2', 'neurips-2024/879c5890a9d2ecdcb590c9674cda4a59', 'naacl-2024/2024naacl-long126']) -> 3 abstracts

[turn 2] read_abstract(['neurips-2025/8ae3fd80c07b1c5fdc0ce59b55396812-abstract-datasetsandbenchmarkstrackhtml', 'icml-2025/phan24b', 'icml-2024/xia24b']) -> 3 abstracts

[turn 3] search_papers('group robust AUC optimization', k=10) ->
     16.17  [iclr-2024] AUC-CL: A Batchsize-Robust Framework for Self-Supervised Contrastive Representation Learning  (iclr-2024/ygmddqb09u)
     15.01  [aaai-2025] FROC: Building Fair ROC from a Trained Classifier  (aaai-2025/770f3d5748477fdb1a04856827eed0eb120449cb)
     14.49  [neurips-2024] AUCSeg: AUC-oriented Pixel-level Long-tail Semantic Segmentation  (neurips-2024/e574db41163e700545ff4114f96b3d7a)
     14.40  [icml-2025] A Federated Stochastic Multi-level Compositional Minimax Algorithm for Deep AUC Maximization  (icml-2025/zhang24aw)
     14.38  [neurips-2024] AUC Maximization under Positive Distribution Shift  (neurips-2024/3f8c7eb848ffec848f3ed2b7ca44915d)
     14.37  [icml-2024] A Federated Stochastic Multi-level Compositional Minimax Algorithm for Deep AUC Maximization  (icml-2024/zhang24aw)
     13.53  [icml-2024] Interplay of ROC and Precision-Recall AUCs: Theoretical Limits and Practical Implications in Binary   (icml-2024/mihelich24a)
     13.52  [icml-2025] Interplay of ROC and Precision-Recall AUCs: Theoretical Limits and Practical Implications in Binary   (icml-2025/mihelich24a)
     13.41  [aaai-2025] Towards Macro-AUC Oriented Imbalanced Multi-Label Continual Learning  (aaai-2025/2e0b591f1c77306f4923e9ab2e615fff2317b795)
     13.20  [aaai-2024] TTTS: Tree Test Time Simulation for Enhancing Decision Tree Robustness against Adversarial Examples  (aaai-2024/1e53a74195c4d6af83ab3773d6263f5eb3f1c7c6)

[turn 3] search_papers('fairness pairwise AUC optimization', k=10) ->
     18.77  [neurips-2024] AUCSeg: AUC-oriented Pixel-level Long-tail Semantic Segmentation  (neurips-2024/e574db41163e700545ff4114f96b3d7a)
     16.83  [aaai-2025] FROC: Building Fair ROC from a Trained Classifier  (aaai-2025/770f3d5748477fdb1a04856827eed0eb120449cb)
     14.75  [aaai-2024] Limited Memory Online Gradient Descent for Kernelized Pairwise Learning with Dynamic Averaging  (aaai-2024/7e62417c144a59928ad55e275e7c99cd608de11a)
     14.42  [neurips-2024] Fairness-Aware Estimation of Graphical Models  (neurips-2024/1fd2b71226c67013756d318d70c40eee)
     14.40  [icml-2025] A Federated Stochastic Multi-level Compositional Minimax Algorithm for Deep AUC Maximization  (icml-2025/zhang24aw)
     14.37  [icml-2024] A Federated Stochastic Multi-level Compositional Minimax Algorithm for Deep AUC Maximization  (icml-2024/zhang24aw)
     14.19  [neurips-2024] Fair GLASSO: Estimating Fair Graphical Models with Unbiased Statistical Behavior  (neurips-2024/fc16089c664195e01139ca7d7432c5bb)
     13.53  [icml-2024] Interplay of ROC and Precision-Recall AUCs: Theoretical Limits and Practical Implications in Binary   (icml-2024/mihelich24a)
     13.52  [icml-2025] Interplay of ROC and Precision-Recall AUCs: Theoretical Limits and Practical Implications in Binary   (icml-2025/mihelich24a)
     13.51  [iclr-2024] Selective Mixup Fine-Tuning for Optimizing Non-Decomposable Objectives  (iclr-2024/rxvbkhyfso)

[turn 3] search_papers('spurious correlation resampling disagreement', k=10) ->
     36.49  [neurips-2024] Mitigating Spurious Correlations via Disagreement Probability  (neurips-2024/879c5890a9d2ecdcb590c9674cda4a59)
     17.16  [iclr-2025] EvA: Erasing Spurious Correlations with Activations  (iclr-2025/zkvroobout)
     17.03  [iclr-2025] Severing Spurious Correlations with Data Pruning  (iclr-2025/bk13qfu8ru)
     16.75  [neurips-2024] RaVL: Discovering and Mitigating Spurious Correlations in Fine-Tuned Vision-Language Models  (neurips-2024/95c6ae3f3393786203a4b6dcb9df1036)
     16.71  [icml-2025] Complexity Matters: Feature Learning in the Presence of Spurious Correlations  (icml-2025/qiu24e)
     16.56  [icml-2025] Improving Group Robustness on Spurious Correlation Requires Preciser Group Inference  (icml-2025/han24g)
     16.54  [icml-2024] Unsupervised Concept Discovery Mitigates Spurious Correlations  (icml-2024/arefin24a)
     16.54  [icml-2025] Unsupervised Concept Discovery Mitigates Spurious Correlations  (icml-2025/arefin24a)
     16.52  [icml-2024] Improving Group Robustness on Spurious Correlation Requires Preciser Group Inference  (icml-2024/han24g)
     16.47  [icml-2024] Complexity Matters: Feature Learning in the Presence of Spurious Correlations  (icml-2024/qiu24e)

[turn 3] open_paper({"paper_id": "neurips-2024/ac4c13a5c6ec1bba68c9ce1d908321d2", "outline_offset": 0}) ->
{"status": "ok", "paper_id": "neurips-2024/ac4c13a5c6ec1bba68c9ce1d908321d2", "title": "Soft-Label Integration for Robust Toxicity Classification", "source_url": "https://papers.nips.cc/paper_files/paper/2024/file/ac4c13a5c6ec1bba68c9ce1d908321d2-Paper-Conference.pdf", "pdf_sha256": "63c08d945089f4d1082d078bd8e53ee21751a6dc676f07f1d0744f86cdde875e", "text_sha256": "3615414e88f8c4ae1f0655f39b73f0b4db20d71d225aee31cecbd466e4af1b7b", "parser": {"schema": "paper-fulltext-v1", "reader_sha256": "5e308bc98d54a08e8fabb5784c5ec5c3f7b0c84602c16c614fa7d1ac5bf1dc1f", "pymupdf": "1.28.0", "pymupdf4llm": "1.28.0", "pymupdf_layout": "1.28.0", "tabulate": "0.9.0"}, "page_count": 32, "warnings": ["Text extraction only: figures and complex equations may be incomplete; OCR is disabled"], "cache_hit": false, "outline": [{"chunk_id": "p001-c001", "page": 1, "section": "Soft-Label Integration for Robust Toxicity** **Classification", "chars": 67}, {"chunk_id": "p001-c002", "page": 1, "section": "Zelei Cheng", "chars": 92}, {"chunk_id": "p001-c003", "page": 1, "section": "Jiahao Yu", "chars": 88}, {"chunk_id": "p001-c004", "page": 1, "section": "Xin-Qiang Cai", "chars": 88}, {"chunk_id": "p001-c005", "page": 1, "section": "Xian Wu", "chars": 90}, {"chunk_id": "p001-c006", "page": 1, "section": "Shuo Han", "chars": 90}, {"chunk_id": "p001-c007", "page": 1, "section": "Xinyu Xing", "chars": 90}, {"chunk_id": "p001-c008", "page": 1, "section": "Abstract", "chars": 12}, {"chunk_id": "p001-c009", "page": 1, "section": "Disclaimer.** **This paper contains uncensored toxic content that might be offensive.", "chars": 1256}, {"chunk_id": "p001-c010", "page": 1, "section": "1** **Introduction", "chars": 869}, {"chunk_id": "p002-c001", "page": 2, "section": "1** **Introduction", "chars": 907}, {"chunk_id": "p002-c002", "page": 2, "section": "1** **Introduction", "chars": 1975}, {"chunk_id": "p002-c003", "page": 2, "section": "1** **Introduction", "chars": 696}, {"chunk_id": "p003-c001", "page": 3, "section": "1** **Introduction", "chars": 292}, {"chunk_id": "p003-c002", "page": 3, "section": "2** **Related Work", "chars": 22}, {"chunk_id": "p003-c003", "page": 3, "section": "Bi-level Optimization.** Bi-level optimization [21] has attracted significant attention due to its ability", "chars": 805}, {"chunk_id": "p003-c004", "page": 3, "section": "Learning** **from** **Partial** **Labels.** Training a classifier from partial labels implicitly requires", "chars": 1474}, {"chunk_id": "p003-c005", "page": 3, "section": "Learning** **from** **Partial** **Labels.** Training a classifier from partial labels implicitly requires", "chars": 835}, {"chunk_id": "p003-c006", "page": 3, "section": "Distributionally Robust Optimization.** Distributionally robust optimization (DRO) optimizes", "chars": 717}, {"chunk_id": "p003-c007", "page": 3, "section": "3** **Proposed Technique", "chars": 28}, {"chunk_id": "p003-c008", "page": 3, "section": "3.1** **Problem Setup and Assumption", "chars": 410}, {"chunk_id": "p004-c001", "page": 4, "section": "3.1** **Problem Setup and Assumption", "chars": 1474}, {"chunk_id": "p004-c002", "page": 4, "section": "3.2** **Technical Overview", "chars": 1780}, {"chunk_id": "p004-c003", "page": 4, "section": "3.2** **Technical Overview", "chars": 1228}, {"chunk_id": "p004-c004", "page": 4, "section": "3.3** **Technical Details", "chars": 1525}, {"chunk_id": "p005-c001", "page": 5, "section": "<u>Algorithm 1</u>** <u>The bi-level optimization algorithm for training the toxicity classifer.</u>", "chars": 102}, {"chunk_id": "p005-c002", "page": 5, "section": "Input:** Training dataset _Dtr_ := _{_ ( **X** <sup>(</sup> <sup>_i_</sup> <sup>)</sup> _,_ **˜y** _i_ ) _}_ <sup>_n_</sup> _i_ <sup>_tr_</sup>", "chars": 400}, {"chunk_id": "p005-c003", "page": 5, "section": "Input:** Training dataset _Dtr_ := _{_ ( **X** _,_ **˜y** _i_ ) _}i_ =1 <sup>_tr_</sup> <sup>, validation dataset</sup> <sup>_Dval_</sup> <sup>:=</sup> <sup>_{_", "chars": 861}, {"chunk_id": "p005-c004", "page": 5, "section": "_θ_** <sup>_∗_</sup> ( **w** ) through one-step inner loop gradient descent. We then update **w** to make the induced **_θ_** <sup>**_′_**</sup>", "chars": 377}, {"chunk_id": "p005-c005", "page": 5, "section": "Outer-loop optimization:** **Updating w.** Denote **w** _t_ be the soft-label weights at time step _t_ . Given", "chars": 545}], "next_outline_offset": 30, "remaining_chars": 40000, "note": "Opening a paper returns no body text. Use read_paper to obtain citable excerpts."}

[turn 3] open_paper({"paper_id": "neurips-2024/879c5890a9d2ecdcb590c9674cda4a59", "outline_offset": 0}) ->
{"status": "ok", "paper_id": "neurips-2024/879c5890a9d2ecdcb590c9674cda4a59", "title": "Mitigating Spurious Correlations via Disagreement Probability", "source_url": "https://papers.nips.cc/paper_files/paper/2024/file/879c5890a9d2ecdcb590c9674cda4a59-Paper-Conference.pdf", "pdf_sha256": "2ce1edcd70539e563f3e0746b99244c5c745cecb0fae9b764eed62e19f48339c", "text_sha256": "9d4b8b1f6c02d8d628634bb8738e51dad91814d2cef38509fdcd77e24aaed1ea", "parser": {"schema": "paper-fulltext-v1", "reader_sha256": "5e308bc98d54a08e8fabb5784c5ec5c3f7b0c84602c16c614fa7d1ac5bf1dc1f", "pymupdf": "1.28.0", "pymupdf4llm": "1.28.0", "pymupdf_layout": "1.28.0", "tabulate": "0.9.0"}, "page_count": 20, "warnings": ["Text extraction only: figures and complex equations may be incomplete; OCR is disabled"], "cache_hit": false, "outline": [{"chunk_id": "p001-c001", "page": 1, "section": "Mitigating Spurious Correlations** **via Disagreement Probability", "chars": 71}, {"chunk_id": "p001-c002", "page": 1, "section": "Hyeonggeun Han** <sup>1</sup> <sup>_,_</sup> <sup>2</sup> **Sehwan Kim** <sup>1</sup> **Hyungjun Joo** <sup>1</sup> <sup>_,_</sup> <sup>2</sup>", "chars": 145}, {"chunk_id": "p001-c003", "page": 1, "section": "Sangwoo Hong** <sup>1</sup> <sup>_,_</sup> <sup>2</sup> **Jungwoo Lee** <sup>1</sup> <sup>_,_</sup> <sup>2</sup> <sup>_,_</sup> <sup>3</sup> <sup>_∗_</sup>", "chars": 294}, {"chunk_id": "p001-c004", "page": 1, "section": "Abstract", "chars": 1236}, {"chunk_id": "p001-c005", "page": 1, "section": "1** **Introduction", "chars": 22}, {"chunk_id": "p001-c006", "page": 1, "section": "Class label", "chars": 1624}, {"chunk_id": "p002-c001", "page": 2, "section": "Class label", "chars": 1226}, {"chunk_id": "p002-c002", "page": 2, "section": "Class label", "chars": 1949}, {"chunk_id": "p002-c003", "page": 2, "section": "Class label", "chars": 634}, {"chunk_id": "p002-c004", "page": 2, "section": "2** **Related work", "chars": 22}, {"chunk_id": "p002-c005", "page": 2, "section": "Debiasing** **with** **bias** **annotations.** Numerous previous works utilize bias labels for debiasing", "chars": 900}, {"chunk_id": "p003-c001", "page": 3, "section": "Debiasing** **with** **bias** **annotations.** Numerous previous works utilize bias labels for debiasing", "chars": 152}, {"chunk_id": "p003-c002", "page": 3, "section": "Debiasing without bias annotations.** In an effort to eliminate reliance on bias annotations, recent", "chars": 1705}, {"chunk_id": "p003-c003", "page": 3, "section": "3** **Problem formulation", "chars": 1743}, {"chunk_id": "p003-c004", "page": 3, "section": "3** **Problem formulation", "chars": 1042}, {"chunk_id": "p004-c001", "page": 4, "section": "3** **Problem formulation", "chars": 318}, {"chunk_id": "p004-c002", "page": 4, "section": "4** **DPR: Disagreement Probability based Resampling for debiasing", "chars": 537}, {"chunk_id": "p004-c003", "page": 4, "section": "4.1** **Problem reformulation", "chars": 1889}, {"chunk_id": "p004-c004", "page": 4, "section": "4.1** **Problem reformulation", "chars": 471}, {"chunk_id": "p004-c005", "page": 4, "section": "4.2** **Sampling probability with group proxy", "chars": 543}, {"chunk_id": "p004-c006", "page": 4, "section": "Group proxy.** We focus on the characteristics of the biased model for the group proxies. Following", "chars": 621}, {"chunk_id": "p005-c001", "page": 5, "section": "<u>Algorithm 1:</u>** <u>Disagreement Probability based Resampling for debiasing (DPR)</u>", "chars": 310}, {"chunk_id": "p005-c002", "page": 5, "section": "for** _t_ = 1 **to** _Tb_ **do", "chars": 413}, {"chunk_id": "p005-c003", "page": 5, "section": "for** _t_ = 1 **to** _Td_ **do", "chars": 811}, {"chunk_id": "p005-c004", "page": 5, "section": "Sampling probability.** We now discuss how to compute the sampling probability _r_ ( _x, y, b_ ). Using", "chars": 1916}, {"chunk_id": "p005-c005", "page": 5, "section": "Sampling probability.** We now discuss how to compute the sampling probability _r_ ( _x, y, b_ ). Using", "chars": 607}, {"chunk_id": "p005-c006", "page": 5, "section": "4.3** **Training algorithm", "chars": 438}, {"chunk_id": "p006-c001", "page": 6, "section": "4.3** **Training algorithm", "chars": 799}, {"chunk_id": "p006-c002", "page": 6, "section": "5** **Theoretical analysis", "chars": 685}, {"chunk_id": "p006-c003", "page": 6, "section": "Theorem 1.** Suppose that the loss function _ℓ_ ( _fθ_ ( _x_ ) _, y_ ) is upper-bounded by a constant _C_ _>_ 0. Given", "chars": 704}], "next_outline_offset": 30, "remaining_chars": 40000, "note": "Opening a paper returns no body text. Use read_paper to obtain citable excerpts."}

[turn 3] open_paper({"paper_id": "aaai-2025/150b28ab6b1d5a47f8126f1073afdf668e5bb9f6", "outline_offset": 0}) ->
{"status": "ok", "paper_id": "aaai-2025/150b28ab6b1d5a47f8126f1073afdf668e5bb9f6", "title": "Boosting Test Performance with Importance Sampling-a Subpopulation Perspective", "source_url": "https://ojs.aaai.org/index.php/AAAI/article/download/34244/36399", "pdf_sha256": "2b6e38874c4461acb34a816372a396ed97e8c948df464f8436c048e1da909806", "text_sha256": "6f574518f0383c11d85acce391803c24d1a423c74b152bb374633ece7e271490", "parser": {"schema": "paper-fulltext-v1", "reader_sha256": "5e308bc98d54a08e8fabb5784c5ec5c3f7b0c84602c16c614fa7d1ac5bf1dc1f", "pymupdf": "1.28.0", "pymupdf4llm": "1.28.0", "pymupdf_layout": "1.28.0", "tabulate": "0.9.0"}, "page_count": 9, "warnings": ["Text extraction only: figures and complex equations may be incomplete; OCR is disabled"], "cache_hit": true, "outline": [{"chunk_id": "p001-c001", "page": 1, "section": "(page text; heading unavailable)", "chars": 69}, {"chunk_id": "p001-c002", "page": 1, "section": "Boosting Test Performance with Importance Sampling–a Subpopulation Perspective", "chars": 84}, {"chunk_id": "p001-c003", "page": 1, "section": "Hongyu Shen, Zhizhen Zhao", "chars": 195}, {"chunk_id": "p001-c004", "page": 1, "section": "Abstract", "chars": 1463}, {"chunk_id": "p001-c005", "page": 1, "section": "Code** - https://github.com/skyve2012/DBA", "chars": 99}, {"chunk_id": "p001-c006", "page": 1, "section": "1** **Introduction", "chars": 867}, {"chunk_id": "p001-c007", "page": 1, "section": "w/ Subpopulation Shift** **w/o Subpopulation Shift", "chars": 1859}, {"chunk_id": "p002-c001", "page": 2, "section": "w/ Subpopulation Shift** **w/o Subpopulation Shift", "chars": 918}, {"chunk_id": "p002-c002", "page": 2, "section": "2** **Related Work", "chars": 195}, {"chunk_id": "p002-c003", "page": 2, "section": "2.1** **Importance Sampling", "chars": 942}, {"chunk_id": "p002-c004", "page": 2, "section": "2.2** **Subpopulation Survey", "chars": 974}, {"chunk_id": "p002-c005", "page": 2, "section": "2.3** **Subpopulation Method", "chars": 1554}, {"chunk_id": "p002-c006", "page": 2, "section": "3** **Method", "chars": 121}, {"chunk_id": "p002-c007", "page": 2, "section": "3.1** **Dataset Bias Analysis Framework", "chars": 1507}, {"chunk_id": "p003-c001", "page": 3, "section": "3.1** **Dataset Bias Analysis Framework", "chars": 1599}, {"chunk_id": "p003-c002", "page": 3, "section": "3.1** **Dataset Bias Analysis Framework", "chars": 1962}, {"chunk_id": "p003-c003", "page": 3, "section": "3.1** **Dataset Bias Analysis Framework", "chars": 795}, {"chunk_id": "p003-c004", "page": 3, "section": "Claim 2.** _Given Assumption 1 holds we obtain the following_", "chars": 1411}, {"chunk_id": "p003-c005", "page": 3, "section": "Definition 1.** The subpopulation shift is defined as the distributional difference between _p_ ( _x, y|I_ tr) and _p_ ( _x, y|I_ te) that", "chars": 1553}, {"chunk_id": "p003-c006", "page": 3, "section": "Assumption 2.** _A universal data generator given the dataset_", "chars": 196}, {"chunk_id": "p003-c007", "page": 3, "section": "Assumption 3.** _The attribute variable s follows a uniform_", "chars": 488}, {"chunk_id": "p004-c001", "page": 4, "section": "Assumption 3.** _The attribute variable s follows a uniform_", "chars": 1307}, {"chunk_id": "p004-c002", "page": 4, "section": "Assumption 3.** _The attribute variable s follows a uniform_", "chars": 855}, {"chunk_id": "p004-c003", "page": 4, "section": "Assumption 4.** _p_ ( _y|Ite_ ) = _p_ ( _y|m_ 0 _, Itr_ ) = _p_ ( _y|Itr_ ) _._", "chars": 1140}, {"chunk_id": "p004-c004", "page": 4, "section": "Assumption 5.** _p_ ( _s|y, m_ 1 _, Itr_ ) = **1** _{y_ = _s}, where_ **1** _{y_ = _s}_ _is_", "chars": 210}, {"chunk_id": "p004-c005", "page": 4, "section": "Theorem** **1.** _Given_ _Assumption_ _1,_ _2,_ _3,_ _4,_ _and_ _5_ _hold,_ _the_", "chars": 1597}, {"chunk_id": "p004-c006", "page": 4, "section": "Theorem** **1.** _Given_ _Assumption_ _1,_ _2,_ _3,_ _4,_ _and_ _5_ _hold,_ _the_", "chars": 673}, {"chunk_id": "p004-c007", "page": 4, "section": "3.2** **Dataset Bias Correction Method", "chars": 602}, {"chunk_id": "p004-c008", "page": 4, "section": "Attribute** _s_ **is Known** When we have access to the attribute", "chars": 506}, {"chunk_id": "p004-c009", "page": 4, "section": "Attribute** _s_ **is Unknown and** _D_ **tr** _∼D_ **va** When we do not", "chars": 415}], "next_outline_offset": 30, "remaining_chars": 40000, "note": "Opening a paper returns no body text. Use read_paper to obtain citable excerpts."}

[turn 4] read_paper({"paper_id": "neurips-2024/ac4c13a5c6ec1bba68c9ce1d908321d2", "chunk_ids": ["p002-c002", "p004-c002", "p004-c003", "p004-c004", "p005-c003"]}) ->
{"status": "ok", "paper_id": "neurips-2024/ac4c13a5c6ec1bba68c9ce1d908321d2", "pdf_sha256": "63c08d945089f4d1082d078bd8e53ee21751a6dc676f07f1d0744f86cdde875e", "text_sha256": "3615414e88f8c4ae1f0655f39b73f0b4db20d71d225aee31cecbd466e4af1b7b", "chunks": [{"chunk_id": "p002-c002", "page": 2, "section": "1** **Introduction", "chars": 1975, "text": "Traditional toxicity classification methods [10–13], typically reliant on labels from a single annotator\nper instance, fall short of capturing the diversity of human perspectives [14]. This approach often leads\nto biases [15, 16] and poor generalizability across different contexts [17], as it fails to account for the\ncomplex realities of language use and social interactions. Thus, there is a growing need to incorporate\ncrowdsourced annotations that reflect a broader array of cultural and linguistic nuances. Additionally,\nArjovsky et al. [18] point out that the model trained by empirical risk minimization (ERM) may\nexploit the spurious correlations that are easier to fit instead of learning the causal components, which\nsuffers from distribution shifts from training to testing domains [19]. When _spurious correlations_\nare present, the performance of certain groups of examples can drop significantly. For example, the\ntoxicity classifier might learn to associate certain phrases or contexts ( _e.g.,_ “I must remind you that”\nin Figure 1) with non-toxic behavior, despite the overall response being harmful.\n\nTo overcome the above challenges, we propose a bi-level optimization framework that incorporates\ncrowdsourced annotations through soft-labeling techniques to enhance the robustness and reliability\nof toxicity classification systems. The proposed framework consists of two optimization loops: an\ninner loop that minimizes the ERM loss on training samples with learned soft labels, and an outer\nloop that assesses the model’s dependency on spurious features by evaluating the out-of-distribution\n(OOD) risk and optimizing the soft-label weights accordingly. By alternatively optimizing inner and\nouter loops, our method progressively adjusts the soft-label weights and can be proved to achieve\nconvergence theoretically, enabling the toxicity classifier to achieve satisfactory OOD performance\nthrough simple ERM training ( _i.e.,_ inner loop optimization)."}, {"chunk_id": "p004-c002", "page": 4, "section": "3.2** **Technical Overview", "chars": 1780, "text": "**3.2** **Technical Overview**\n\nRecall our goal is to train an optimal classifier\nthat does not depend on spurious correlations, a\nnaive approach might involve using existing outof-distribution (OOD) risk loss functions, such\nas distributionally robust optimization (DRO).\nHowever, a significant issue arises from the absence of ground-truth labels in the training set.\nTraining a robust model directly using DRO\non the clean validation set could result in limited available data, potentially compromising (a) Ground truth (b) Soft-label weighted\nthe overall performance. Considering these, we\npropose a bi-level formulation to address these\nchallenges. As illustrated in Figure 2, we reduce Figure 2: **An illustrative 2-class example of re-**\nthe classifier _f_ ’s dependence on spurious fea- **moving** **the** **reliance** **on** **spurious** **feature** **via**\ntures through soft re-labeling. In this example, **weighted soft labels.** Blue and yellow represent\nwe identify _x_ 1 and _x_ 2 as the core and spurious two different classes and the depth of color indifeatures, respectively, and aim to train a classi- cates the soft label.\nfier that does not rely on the spurious feature _x_ 2.\nWithout re-labeling, even if the training set had the ground truths, the classifier would still be biased\ntowards _x_ 2. However, by applying soft re-labeling, we adjust the labels for samples in the bottom-left\nand top-right areas, resulting in an optimal classifier that is oriented vertically, as shown in Figure 2.\nThis adjustment ensures that the newly trained classifier _f_ does not depend on _x_ 2. Motivated by these,\nwe formulate the task of learning soft labels to remove the spurious features as a bi-level optimization\nproblem:\n\n(a) Ground truth (b) Soft-label weighted"}, {"chunk_id": "p004-c003", "page": 4, "section": "3.2** **Technical Overview", "chars": 1228, "text": "Figure 2: **An illustrative 2-class example of re-**\n**moving** **the** **reliance** **on** **spurious** **feature** **via**\n**weighted soft labels.** Blue and yellow represent\ntwo different classes and the depth of color indicates the soft label.\n\n_R_ ( _Dv,_ **_θ_** <sup>_∗_</sup> ( **w** )) subject to **_θ_** <sup>_∗_</sup> ( **w** ) _∈_ arg min\n**w** **_θ_**\n\nminimize\n\n(1)\n**_θ_** <sup>_L_</sup> <sup>(</sup> <sup>_Dtr,_</sup> <sup>**_θ_**</sup> <sup>;</sup> <sup>**w**</sup> <sup>)</sup>\n\nwhere **w** is the soft-label weight vector which indicates the importance of each annotator. The\nouter objective function can be any OOD risk loss function ( _i.e.,_ group DRO loss). In the inner\nloop, we minimize the empirical risk minimization (ERM) loss ( _i.e.,_ cross-entropy loss) on training\nsamples with learned soft labels, resulting in a model denoted as **_θ_** <sup>_∗_</sup> ( **w** ). In the outer loop, we\nassess the model’s dependency on spurious features by evaluating the OOD risk and optimizing\nthe soft-label weights accordingly. By alternating between the inner and outer loops, the soft-label\nweights progressively adjust, enabling the achievement of satisfactory OOD performance through\nsimple ERM training."}, {"chunk_id": "p004-c004", "page": 4, "section": "3.3** **Technical Details", "chars": 1525, "text": "**3.3** **Technical Details**\n\nWe design a bi-level optimization process consisting of an inner-loop optimization and an outer-loop\noptimization to simultaneously update the learned soft-label weight **w** and model parameters **_θ_** . We\nbegin by addressing the parameterization of the soft-label weight function **w** in Eqn. (1). Although\nwe could parameterize **w** as an _m_ -dimensional vector, it does not account for the relationship between\nthe feature and label as annotated by the worker. Thus, we capture the weight of annotated labels\n**˜y** _i_ for the sample **X** <sup>(</sup> <sup>_i_</sup> <sup>)</sup> through a neural network _vθ_ : **X** <sup>(</sup> <sup>_i_</sup> <sup>)</sup> _→_ **v** <sup>(</sup> <sup>_i_</sup> <sup>)</sup> _∈_ R <sup>_m_</sup> . After obtaining the\nnormalized soft-label weights **v** <sup>(</sup> <sup>_i_</sup> <sup>)</sup> through the softmax function, the final soft-label **¯y** _i_ is determined\nby taking the weighted sum of the one-hot vectors **e** <sup>_j_</sup> _i_ <sup>in the potential label set</sup> <sup>**˜y**</sup> <sup>_i_</sup> <sup>, where the weights</sup>\n\nare explicitly provided by **v** <sup>(</sup> <sup>_i_</sup> <sup>)</sup> . With the soft-labels computed, we can now turn to the outer-level\noptimization. Motivated by [55], we initiate by pseudo-updating the parameter vector **_θ_**, thereby\nestablishing a relationship between **w** and the optimized parameters **_θ_** <sup>**_′_**</sup> . Specifically, **_θ_** <sup>**_′_**</sup> approximate\n\n4"}, {"chunk_id": "p005-c003", "page": 5, "section": "Input:** Training dataset _Dtr_ := _{_ ( **X** _,_ **˜y** _i_ ) _}i_ =1 <sup>_tr_</sup> <sup>, validation dataset</sup> <sup>_Dval_</sup> <sup>:=</sup> <sup>_{_", "chars": 861, "text": "**Input:** Training dataset _Dtr_ := _{_ ( **X** _,_ **˜y** _i_ ) _}i_ =1 <sup>_tr_</sup> <sup>, validation dataset</sup> <sup>_Dval_</sup> <sup>:=</sup> <sup>_{_</sup> <sup>(</sup> <sup>**X**</sup> <sup>_, yi_</sup> <sup>)</sup> <sup>_}_</sup> _i_ =1 <sup>_v_</sup> <sup>, max</sup>\n\nnumber of steps _T_\n**Output:** Toxicity classifier _f_ **_θ_**\n**Initialization:** Initialize the soft-label weights **w** 0 and the classifier parameter **_θ_** 0\n**for** _t_ = 1 _,_ 2 _, . . ., T_ **do**\n\nSample batch data _{_ **X** _,_ **˜y** _}_ from the training dataset _Dtr_\nSample batch data _{_ **X** _, y}_ from the validation dataset _Dval_\nPseudo update **_θ_** <sup>_′_</sup> _t_ +1 <sup>as Eqn. (2) and update the soft-label weights</sup> <sup>**w**</sup> <sup>_t_</sup> <sup>+1</sup> <sup>as Eqn. (3)</sup>\n\nUpdate **_θ_** _t_ +1 as Eqn. (4)\n**<u>end for</u>**"}], "not_returned_chunk_ids": [], "remaining_chars": 32631, "remaining_read_calls": 11}

[turn 4] read_paper({"paper_id": "neurips-2024/879c5890a9d2ecdcb590c9674cda4a59", "chunk_ids": ["p001-c004", "p004-c003", "p004-c006", "p005-c004", "p006-c001"]}) ->
{"status": "ok", "paper_id": "neurips-2024/879c5890a9d2ecdcb590c9674cda4a59", "pdf_sha256": "2ce1edcd70539e563f3e0746b99244c5c745cecb0fae9b764eed62e19f48339c", "text_sha256": "9d4b8b1f6c02d8d628634bb8738e51dad91814d2cef38509fdcd77e24aaed1ea", "chunks": [{"chunk_id": "p001-c004", "page": 1, "section": "Abstract", "chars": 1236, "text": "**Abstract**\n\nModels trained with empirical risk minimization (ERM) are prone to be biased\ntowards spurious correlations between target labels and bias attributes, which leads\nto poor performance on data groups lacking spurious correlations. It is particularly\nchallenging to address this problem when access to bias labels is not permitted. To\nmitigate the effect of spurious correlations without bias labels, we first introduce a\nnovel training objective designed to robustly enhance model performance across\nall data samples, irrespective of the presence of spurious correlations. From this\nobjective, we then derive a debiasing method, Disagreement Probability based Resampling for debiasing (DPR), which does not require bias labels. DPR leverages\nthe disagreement between the target label and the prediction of a biased model to\nidentify bias-conflicting samples—those without spurious correlations—and upsamples them according to the disagreement probability. Empirical evaluations on\nmultiple benchmarks demonstrate that DPR achieves state-of-the-art performance\nover existing baselines that do not use bias labels. Furthermore, we provide a theoretical analysis that details how DPR reduces dependency on spurious correlations."}, {"chunk_id": "p004-c003", "page": 4, "section": "4.1** **Problem reformulation", "chars": 1889, "text": "**4.1** **Problem reformulation**\n\nTo utilize the objective in Equation (3) without bias annotations, we reformulate this objective as a\nweighted loss minimization problem. For this purpose, we introduce the following assumption:\n**Assumption** **1.** Let _ba_ _∈B_ and _bc_ _∈B_ represent the bias-aligned and bias-conflicting groups,\nrespectively. The neural network, parameterized by _θ_, satisfies that _L_ <sup>ˆ</sup> _ba_ _<_ _L_ <sup>ˆ</sup> _bc_ .\n\nIn Assumption 1, we assume that the model, parameterized by _θ_, exhibits a higher average loss on\nthe bias-conflicting group compared to the bias-aligned group in the training dataset. Under this\nassumption, the maximum average loss over groups in Equation (3) can be expressed as follows:\n\n( _x,y,b_ ) _∈D_\n\nmax\n\n_b∈B_\n\n<u>1</u>\n_L_ ˆ _b_ =\n_nbc_\n\n<u>1</u>\n=\n_nbc_\n\n( _x,y,bc_ ) _∈Gbc_\n\n_ℓ_ ( _fθ_ ( _x_ ) _, y_ ) (4)\n\n_p_ ( _b_ = _bc|x_ ) _ℓ_ ( _fθ_ ( _x_ ) _, y_ ) (5)\n\n= <sup><u>1</u></sup>\n\n_n_\n\n( _x,y,b_ ) _∈D_\n\n_<u>p</u>_ <u>(</u> _<u>b</u>_ <u>=</u> _<u>bc|x</u>_ <u>)</u>\n\n(6)\n_p_ ( _b_ = _bc_ ) <sup>_ℓ_</sup> <sup>(</sup> <sup>_fθ_</sup> <sup>(</sup> <sup>_x_</sup> <sup>)</sup> <sup>_, y_</sup> <sup>)</sup> <sup>_._</sup>\n\nWhen Assumption 1 is satisfied, Equation (4) holds. Given that all samples in _Gbc_ have _p_ ( _b_ = _bc|x_ )\nequal to 1, whereas all samples in _Gba_ have _p_ ( _b_ = _bc|x_ ) equal to 0, Equation (5) is derived from\nEquation (4). As _p_ ( _b_ = _bc_ ) is equal to <sup>_<u>n</u>_</sup> _n_ <sup>_<u>bc</u>_</sup> <sup>, Equation (6) is obtained.</sup> <sup>By denoting</sup> _n_ <sup><u>1</u></sup> <sup>_·_</sup> <sup>_<u>p</u>_</sup> _p_ <sup><u>(</u></sup> <sup>_<u>b</u>_</sup> ( _b_ <sup><u>=</u></sup> = <sup>_<u>b</u>_</sup> _b_ <sup>_<u>c</u>_</sup> _c_ <sup>_<u>|x</u>_</sup> ) <sup><u>)</u></sup> <sup>as</sup>\n\n_r_ ( _x, y, b_ ), we obtain a weighted loss minimization as follows:"}, {"chunk_id": "p004-c006", "page": 4, "section": "Group proxy.** We focus on the characteristics of the biased model for the group proxies. Following", "chars": 621, "text": "**Group proxy.** We focus on the characteristics of the biased model for the group proxies. Following\nNam et al. [34], the biased model _fϕ_ is trained using ERM with the generalized cross-entropy (GCE)\nloss [50]:\n\n_ℓ_ GCE( _fϕ_ ( _x_ ) _, y_ ) = <sup><u>1</u></sup> <sup>_<u>−</u>_</sup> <sup>_<u>pϕ</u>_</sup> <sup><u>(</u></sup> <sup>_<u>y|x</u>_</sup> <sup><u>)</u></sup> <sup>_q_</sup>\n\n_,_ (8)\n_q_\n\nwhere _pϕ_ ( _y|x_ ) represents the probability assigned to the target label _y_ by the neural network after\na softmax layer, and _q_ _∈_ (0 _,_ 1] is a hyperparameter. The GCE loss amplifies the bias of the model\n\n4"}, {"chunk_id": "p005-c004", "page": 5, "section": "Sampling probability.** We now discuss how to compute the sampling probability _r_ ( _x, y, b_ ). Using", "chars": 1916, "text": "**Sampling probability.** We now discuss how to compute the sampling probability _r_ ( _x, y, b_ ). Using\nthe group proxies mentioned above, we substitute _p_ ( _y_ = _y_ bias _|x_ ) for _p_ ( _b_ = _bc|x_ ). For a given\nexample ( _x, y_ ), the disagreement probability _p_ ( _y_ = _y_ bias _|x_ ) can be computed as follows:\n\n_p_ ( _y_ = _y_ bias _|x_ ) =\n\n_y_ bias\n\n_p_ ( _y, y_ bias _|x_ ) _−_ _p_ ( _y_ = _y_ bias _|x_ ) = 1 _−_ _p_ bias( _y|x_ ) _,_ (9)\n\nwhere _p_ bias( _y|x_ ) = <sup><u>exp(</u></sup> <sup>_<u>f</u>_</sup> _Z_ <sup>_<u>ϕ</u>_</sup> <sup><u>(</u></sup> ( <sup>_<u>x</u>_</sup> _ϕ_ <sup><u>)[</u></sup> ) <sup>_<u>y</u>_</sup> <sup><u>]</u></sup> <sup>_<u>/τ</u>_</sup> <sup><u>)</u></sup> is the probability assigned to label _y_ by the biased model, _Z_ ( _ϕ_ ) =\n\n- _y_ <sup>_′_</sup> <sup>exp(</sup> <sup>_fϕ_</sup> <sup>(</sup> <sup>_x_</sup> <sup>)[</sup> <sup>_y′_</sup> <sup>]</sup> <sup>_/τ_</sup> <sup>) is the partition function, and</sup> <sup>_τ_</sup> <sup>is a temperature hyperparameter.</sup> <sup>Note that</sup>\n\n_p_ bias( _y|x_ ) is used to approximate _p_ ( _b_ = _ba|x_ ). It is crucial for the biased model to accurately capture\nthe spurious correlation structure; hence, the probabilities of the biased model should be appropriately\ncalibrated [13, 33, 32]. We also substitute _p_ ( _y_ = _y_ bias) for _p_ ( _b_ = _bc_ ). This probability can be\nestimated using all the training data, as in prior works [29, 45]:\n\n_p_ ( _y_ = _y_ bias) _≈_ <sup><u>1</u></sup>\n\n_n_\n\n( _x,y,b_ ) _∈D_\n\n( _x,y,b_ ) _∈D_\n\n_p_ ( _y_ = _y_ bias _|x_ ) = <sup><u>1</u></sup>\n\n_n_\n\n(1 _−_ _p_ bias( _y|x_ )) _._ (10)\n\nWith Equations (9) and (10), we compute\n\n<sup><u>1</u></sup> <sup>_<u>p</u>_</sup> <sup><u>(</u></sup> <sup>_<u>y</u>_</sup> <sup><u>=</u></sup> <sup>_<u>y</u>_</sup> <sup><u>bias</u></sup> <sup>_<u>|x</u>_</sup> <sup><u>)</u></sup>\n\n_n_ <sup>_·_</sup> _p_ ( _y_ = _y_ bias)"}, {"chunk_id": "p006-c001", "page": 6, "section": "4.3** **Training algorithm", "chars": 799, "text": "Equation (7). We leverage the characteristics of the biased model for this purpose. The biased model\ntypically exhibits higher loss on bias-conflicting samples and lower loss on bias-aligned samples,\nthereby fulfilling Assumption 1. Consequently, we initialize the model _fθ_ with the biased model\n_fϕ_ and then train _fθ_ using training examples sampled with the probability ˆ _r_ ( _x, y_ ). We also employ\ndata augmentation to enhance the diversity of bias-conflicting samples. Simply oversampling these\nsamples without enhancing their diversity does not effectively mitigate bias [27]. Therefore, we\nenhance the diversity of bias-conflicting samples through data augmentation techniques such as\nrandom color jitter and random rotation. The complete training procedure is outlined in Algorithm 1."}], "not_returned_chunk_ids": [], "remaining_chars": 26170, "remaining_read_calls": 10}

[turn 4] read_paper({"paper_id": "aaai-2025/150b28ab6b1d5a47f8126f1073afdf668e5bb9f6", "chunk_ids": ["p001-c004", "p002-c005", "p004-c007", "p004-c008", "p004-c009"]}) ->
{"status": "ok", "paper_id": "aaai-2025/150b28ab6b1d5a47f8126f1073afdf668e5bb9f6", "pdf_sha256": "2b6e38874c4461acb34a816372a396ed97e8c948df464f8436c048e1da909806", "text_sha256": "6f574518f0383c11d85acce391803c24d1a423c74b152bb374633ece7e271490", "chunks": [{"chunk_id": "p001-c004", "page": 1, "section": "Abstract", "chars": 1463, "text": "**Abstract**\n\nDespite empirical risk minimization (ERM) is widely applied\nin the machine learning community, its performance is limited on data with spurious correlation or subpopulation that is\nintroduced by hidden attributes. Existing literature proposed\ntechniques to maximize group-balanced or worst-group accuracy when such correlation presents, yet, at the cost of lower\naverage accuracy. In addition, many existing works conduct\nsurveys on different subpopulation methods without revealing\nthe inherent connection between these methods, which could\nhinder the technology advancement in this area. In this paper,\nwe identify important sampling as a simple yet powerful tool\nfor solving the subpopulation problem. On the theory side, we\nprovide a new systematic formulation of the subpopulation\nproblem and explicitly identify the assumptions that are not\nclearly stated in the existing works. This helps to uncover the\ncause of the dropped average accuracy. We provide the first\ntheoretical discussion on the connections of existing methods, revealing the core components that make them different.\nOn the application side, we demonstrate a single estimator is\nenough to solve the subpopulation problem. In particular, we\nintroduce the estimator in both attribute-known and -unknown\nscenarios in the subpopulation setup, offering flexibility in\npractical use cases. And empirically, we achieve state-of-theart performance on commonly used benchmark datasets."}, {"chunk_id": "p002-c005", "page": 2, "section": "2.3** **Subpopulation Method", "chars": 1554, "text": "**2.3** **Subpopulation Method**\n\nWe categorize subpopulation methods into four classes: auxiliary losses, data augmentations, modeling objectives, and\ndata sampling techniques. Auxiliary loss methods (Li et al.\n2018; Arjovsky et al. 2019; Alshammari et al. 2022) aim\nto mitigate the impact of spurious backgrounds via adversarial training, gradient regularization, or class-balanced adjustments. Data augmentation methods (Zhang et al. 2018;\nHan et al. 2022; Yao et al. 2022) use convex combinations\nof samples to reduce background effects. Data sampling\nmethods (LaBonte, Muthukumar, and Kumar 2024; Izmailov\net al. 2022) identify class-balanced subsets with independent\nspurious features for finetuning. Modeling objective methods (Sagawa et al. 2020; Wu et al. 2023; Lin et al. 2017;\nRudner et al. 2024) focus on robust feature learning, subpopulation correction, or tailored loss terms like KL divergence\nor mutual information.\n\nDBA stands out by explicitly stating data assumptions\nand connecting existing methods under a unified statistical\nframework (see Sec. 4). For instance, it highlights that augmentation methods (Zhang et al. 2018; Yao et al. 2022; Han\net al. 2022) assume conditional similarity across subpopulations. DBA also identifies a universal assumption of identical\nconditional generative models across methods, which previous works did not explicitly address. Empirically, DBA\noutperforms SOTA methods on three datasets, confirming\nits effectiveness and simplicity, and leveraging importance\nsampling for practical implementation."}, {"chunk_id": "p004-c007", "page": 4, "section": "3.2** **Dataset Bias Correction Method", "chars": 602, "text": "**3.2** **Dataset Bias Correction Method**\n\nIn this section, we provide 3 different approaches to estimate _Eq._ (5). We summarize these approaches with a general\nname: dataset bias correction method (DBCM). The 3 approaches essentially provide different ways of estimating the\nonly missing term _p_ ( _s|y, x, I_ tr) in Eq. (5). Once the term\nis estimated, we employ a universal algorithm (see Algorithm 1) to train the model with _D_ tr. To facilitate the use of\nthis approach in more real-world applications, we describe\nthe scenarios where the three following approaches can be\napplied in Appendix."}, {"chunk_id": "p004-c008", "page": 4, "section": "Attribute** _s_ **is Known** When we have access to the attribute", "chars": 506, "text": "**Attribute** _s_ **is Known** When we have access to the attribute\n_s_, we can make a direct estimation on the only unknown term\n_p_ ( _s_ = _y|y, x, I_ tr) using the data ( _x, y, s_ ) _∈D_ tr and apply Algorithm 1 therein. As _p_ ( _s_ = _y|y, x, I_ tr) increases, the weight\nfunction _g_ decreases (see Eq. (5)), because stronger spurious\ncorrelations make _p_ ( _s_ = _y|y, x, I_ tr) larger. Down-weighting\nthese samples during training helps performance by reducing\nreliance on spurious correlations."}, {"chunk_id": "p004-c009", "page": 4, "section": "Attribute** _s_ **is Unknown and** _D_ **tr** _∼D_ **va** When we do not", "chars": 415, "text": "**Attribute** _s_ **is Unknown and** _D_ **tr** _∼D_ **va** When we do not\nhave access to the attribute _s_ and _D_ tr _∼D_ va, we propose to\nuse the following term to estimate _p_ ( _s|y, x, I_ tr):\n\n_p_ ˆ( _s_ = _y|y, x, I_ tr)\n\n- _−_ 1\n_,_ (6)\n\n_∝_ exp\n\n- _<u>|</u>_ <u>log ˆ</u> _<u>p</u>_ <u>(</u> _<u>y|x, I</u>_ <u>tr)</u> _<u>−</u>_ <u>log ˆ</u> _<u>p</u>_ <u>(</u> _<u>y|x, I</u>_ <u>va)</u> _<u>|</u>_\n_τ_"}], "not_returned_chunk_ids": [], "remaining_chars": 21630, "remaining_read_calls": 9}

[turn 4] read_abstract(['iclr-2024/rxvbkhyfso', 'neurips-2024/e574db41163e700545ff4114f96b3d7a', 'aaai-2025/770f3d5748477fdb1a04856827eed0eb120449cb']) -> 3 abstracts

[turn 5] submit_report -> 1 mechanism(s); problems: ['rejected evidence for neurips-2024/879c5890a9d2ecdcb590c9674cda4a59: quote not found in text returned to this episode', 'rejected evidence for neurips-2024/879c5890a9d2ecdcb590c9674cda4a59: quote not found in text returned to this episode', "'Sampling is compute control only when it preserves shortcut-conflicting subpopulations': needs read evidence and assumptions/target_fit/limitations/validation_plan"]

## Report (as injected)

## Cross-domain mechanism suggestions (analogy search on this task's structure)

Structural properties of this task that the suggestions address:
0. The score is a generalized mean of overall and identity-conditioned ROC-AUCs, so example-averaged BCE can preserve global ranking while failing the BPSN/BNSP cross-group rankings that dominate a weak subgroup score. — evidence: Evaluation explicitly defines Subgroup AUC, BPSN AUC, BNSP AUC for every identity and combines bias AUCs by generalized mean; the description gives the specific failure of assigning high toxicity to benign identity mentions.
1. The available target is an aggregated subjective toxicity signal, but a first solution cannot recover annotator-level alternatives from the listed files. — evidence: Description discusses paid raters and judgments, while workspace exposes only train.csv/test.csv and the preview supplies aggregate/count columns rather than per-rater label records.
2. A 1.8M-row corpus must be fitted under one A10 and a six-hour run cap, while the score-critical conditional groups cannot be discarded by undifferentiated subsampling. — evidence: train.csv has 1,804,874 rows; per-solution cap is 6.0 h on a 22 GiB A10; evaluation is conditional on identity and label combinations.

### Known-attribute importance weighting against a label–attribute shortcut
*Addresses property 0. Source: Boosting Test Performance with Importance Sampling-a Subpopulation Perspective (aaai-2025, `aaai-2025/150b28ab6b1d5a47f8126f1073afdf668e5bb9f6`)*

**Shared problem structure**: Observed attributes are correlated with labels in training; ERM exploits that correlation, whereas reweighting/downweighting aligned cases reduces shortcut reliance and protects conditional-group performance.
**Object mappings (this pipeline ↔ source)**: attribute s ↔ training identity-membership indicator (Both are observed attributes that can become predictively coupled to the class label.); spurious-correlation-aligned sample ↔ comment in a high-frequency identity/toxicity pairing (These are examples whose prevalence lets ERM use the attribute as a shortcut.); importance-weight function ↔ per-example training-sampler weight derived from identity × hard toxicity label cell frequency (Both alter the effective training distribution without adding a model.); subpopulation performance ↔ Subgroup/BPSN/BNSP AUC (Both evaluate behavior under conditional partitions rather than only the pooled population.)
**Mechanism in the source**: The source frames subpopulation correction as estimating a missing attribute-related probability and then applying a universal weighted-training algorithm. In its known-attribute case, stronger attribute–label spurious correlation receives lower weight; it reports importance sampling as a simple practical correction, while noting possible average-performance cost.
**Proposed intervention here**: Build one non-standard component into the first run: a weighted random sampler. Threshold the already available continuous toxicity target only for sampler-cell construction, form identity-present/absent × toxicity-positive/negative cells (using a union of identity columns and a fixed threshold), and sample inversely to cell frequency with capped weights; keep the model loss as ordinary BCE on the original continuous toxicity target. Hold out a stratified validation slice and select/checkpoints by the exact competition metric, expecting BPSN to improve if identity-name shortcutting is real; do not add an adversary, ensemble, or a second model.
**Feasibility with the available data**: High. It uses only existing training labels and identity columns, one ModernBERT training run, and a sampler; it reduces effective repetition of dominant shortcut-aligned cells rather than requiring extra modality or preprocessing.
**Evidence level**: full_text
- `aaai-2025/150b28ab6b1d5a47f8126f1073afdf668e5bb9f6` (PDF p. 4, p004-c008): "Down-weighting these samples during training helps performance by reducing reliance on spurious correlations."
- `aaai-2025/150b28ab6b1d5a47f8126f1073afdf668e5bb9f6` (PDF p. 1, p001-c004): "we identify important sampling as a simple yet powerful tool for solving the subpopulation problem."
**Source assumptions**: Identity indicators are sufficiently reliable for a union indicator, and the harmful shortcut is materially represented by identity-presence × toxicity-label imbalance. Inverse-frequency sampling is only a proxy for the source probability estimator, not its full method.
**Fit to this task**: Met: group attributes and labels exist in training, and the competition explicitly identifies the target shortcut. Unknown: test identity prevalence and whether a union group is adequate for every individual identity; validation must also report each identity separately.
**Limitations / unknowns**: The source optimizes subpopulation performance/accuracy, not this exact generalized conditional-AUC metric. Strong reweighting can reduce overall AUC, amplify noisy rare cells, and multiple identities make overlapping groups unlike the source's simple attribute setup.
**Minimal validation and rejection criterion**: Compare identical short ModernBERT runs with uniform versus capped cell-balanced sampling on an article-aware or random stratified holdout, reporting overall AUC plus each three-way bias AUC and official aggregate. Keep only if aggregate improves and neither overall AUC nor median subgroup AUC falls materially (predeclare, e.g., 0.002); otherwise revert to uniform sampling or lower the cap.


## Report (raw JSON)

```json
{
  "bottlenecks": [
    {
      "statement": "The score is a generalized mean of overall and identity-conditioned ROC-AUCs, so example-averaged BCE can preserve global ranking while failing the BPSN/BNSP cross-group rankings that dominate a weak subgroup score.",
      "objects": [
        "score-producing toxicity predictor",
        "binary toxicity outcome",
        "identity membership attributes",
        "overall and conditional ROC-AUC subsets",
        "generalized-mean leaderboard aggregate"
      ],
      "relations": [
        "The predictor must order positive and negative examples correctly within each identity subgroup and across identity/background partitions; ERM weights common examples rather than the low-performing conditional partitions."
      ],
      "evidence": "Evaluation explicitly defines Subgroup AUC, BPSN AUC, BNSP AUC for every identity and combines bias AUCs by generalized mean; the description gives the specific failure of assigning high toxicity to benign identity mentions."
    },
    {
      "statement": "The available target is an aggregated subjective toxicity signal, but a first solution cannot recover annotator-level alternatives from the listed files.",
      "objects": [
        "crowd judgments",
        "aggregated training target",
        "comment score",
        "ROC-AUC evaluation"
      ],
      "relations": [
        "Collapsing individual judgments can hide perspective variation, but methods that learn per-annotator soft-label weights require annotations that are not in the listed workspace."
      ],
      "evidence": "Description discusses paid raters and judgments, while workspace exposes only train.csv/test.csv and the preview supplies aggregate/count columns rather than per-rater label records."
    },
    {
      "statement": "A 1.8M-row corpus must be fitted under one A10 and a six-hour run cap, while the score-critical conditional groups cannot be discarded by undifferentiated subsampling.",
      "objects": [
        "1,804,874 training comments",
        "identity-conditioned label partitions",
        "single A10 GPU",
        "six-hour execution cap",
        "pretrained encoder"
      ],
      "relations": [
        "Uniform reduction favors prevalent, easy examples and can erase the counter-correlation cases needed by the conditional AUCs; compute allocation must retain such partitions."
      ],
      "evidence": "train.csv has 1,804,874 rows; per-solution cap is 6.0 h on a 22 GiB A10; evaluation is conditional on identity and label combinations."
    }
  ],
  "mechanisms": [
    {
      "bottleneck_idx": 0,
      "title": "Known-attribute importance weighting against a label–attribute shortcut",
      "paper_ids": [
        "aaai-2025/150b28ab6b1d5a47f8126f1073afdf668e5bb9f6"
      ],
      "object_mappings": [
        {
          "source": "attribute s",
          "target": "training identity-membership indicator",
          "rationale": "Both are observed attributes that can become predictively coupled to the class label."
        },
        {
          "source": "spurious-correlation-aligned sample",
          "target": "comment in a high-frequency identity/toxicity pairing",
          "rationale": "These are examples whose prevalence lets ERM use the attribute as a shortcut."
        },
        {
          "source": "importance-weight function",
          "target": "per-example training-sampler weight derived from identity × hard toxicity label cell frequency",
          "rationale": "Both alter the effective training distribution without adding a model."
        },
        {
          "source": "subpopulation performance",
          "target": "Subgroup/BPSN/BNSP AUC",
          "rationale": "Both evaluate behavior under conditional partitions rather than only the pooled population."
        }
      ],
      "shared_relations": "Observed attributes are correlated with labels in training; ERM exploits that correlation, whereas reweighting/downweighting aligned cases reduces shortcut reliance and protects conditional-group performance.",
      "mechanism": "The source frames subpopulation correction as estimating a missing attribute-related probability and then applying a universal weighted-training algorithm. In its known-attribute case, stronger attribute–label spurious correlation receives lower weight; it reports importance sampling as a simple practical correction, while noting possible average-performance cost.",
      "intervention": "Build one non-standard component into the first run: a weighted random sampler. Threshold the already available continuous toxicity target only for sampler-cell construction, form identity-present/absent × toxicity-positive/negative cells (using a union of identity columns and a fixed threshold), and sample inversely to cell frequency with capped weights; keep the model loss as ordinary BCE on the original continuous toxicity target. Hold out a stratified validation slice and select/checkpoints by the exact competition metric, expecting BPSN to improve if identity-name shortcutting is real; do not add an adversary, ensemble, or a second model.",
      "feasibility": "High. It uses only existing training labels and identity columns, one ModernBERT training run, and a sampler; it reduces effective repetition of dominant shortcut-aligned cells rather than requiring extra modality or preprocessing.",
      "assumptions": "Identity indicators are sufficiently reliable for a union indicator, and the harmful shortcut is materially represented by identity-presence × toxicity-label imbalance. Inverse-frequency sampling is only a proxy for the source probability estimator, not its full method.",
      "target_fit": "Met: group attributes and labels exist in training, and the competition explicitly identifies the target shortcut. Unknown: test identity prevalence and whether a union group is adequate for every individual identity; validation must also report each identity separately.",
      "limitations": "The source optimizes subpopulation performance/accuracy, not this exact generalized conditional-AUC metric. Strong reweighting can reduce overall AUC, amplify noisy rare cells, and multiple identities make overlapping groups unlike the source's simple attribute setup.",
      "validation_plan": "Compare identical short ModernBERT runs with uniform versus capped cell-balanced sampling on an article-aware or random stratified holdout, reporting overall AUC plus each three-way bias AUC and official aggregate. Keep only if aggregate improves and neither overall AUC nor median subgroup AUC falls materially (predeclare, e.g., 0.002); otherwise revert to uniform sampling or lower the cap.",
      "evidence_refs": [
        {
          "paper_id": "aaai-2025/150b28ab6b1d5a47f8126f1073afdf668e5bb9f6",
          "source": "full_text",
          "quote": "Down-weighting these samples during training helps performance by reducing reliance on spurious correlations.",
          "chunk_id": "p004-c008",
          "page": 4,
          "section": "Attribute** _s_ **is Known** When we have access to the attribute",
          "pdf_sha256": "2b6e38874c4461acb34a816372a396ed97e8c948df464f8436c048e1da909806",
          "text_sha256": "6f574518f0383c11d85acce391803c24d1a423c74b152bb374633ece7e271490"
        },
        {
          "paper_id": "aaai-2025/150b28ab6b1d5a47f8126f1073afdf668e5bb9f6",
          "source": "full_text",
          "quote": "we identify important sampling as a simple yet powerful tool for solving the subpopulation problem.",
          "chunk_id": "p001-c004",
          "page": 1,
          "section": "Abstract",
          "pdf_sha256": "2b6e38874c4461acb34a816372a396ed97e8c948df464f8436c048e1da909806",
          "text_sha256": "6f574518f0383c11d85acce391803c24d1a423c74b152bb374633ece7e271490"
        }
      ],
      "evidence_level": "full_text"
    }
  ]
}
```
