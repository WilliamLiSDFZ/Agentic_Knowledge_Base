# Data-Centric Explainable Debiasing for Improving Fairness in Pre-trained Language Models

**Source**: https://aclanthology.org/2024.findings-acl.226/

## [POSITIVE] Implicit Bias Word Mining via Integrated Gradients
Using Integrated Gradients (IG) to compute feature attribution scores for all tokens, then selecting tokens with large differences in attribution scores across demographic groups as implicit bias words

**Delta**: outperforms baseline
**Condition**: Applied to all three classification tasks (SST2, ToxiGen, Bias in Bios) across BERT, DistilBERT, and RoBERTa

**Evidence**: "the fairness of BERT is extremely improved at BERT-D0 even without amplifying Tiny-BERT's bias, which verifies the effectiveness of our proposed Data-Debias in debiasing performance"

## [POSITIVE] Iterative Bias-Amplified Model Training
Iteratively training a biased model (Tiny-BERT) using implicit bias words and bias regularization to amplify bias, then re-searching and updating the implicit bias word list each iteration

**Delta**: fairness peaks at 4th or 5th iteration
**Condition**: Applied during the bias amplification stage; effective up to 4th-5th iteration

**Evidence**: "BERT's bias gradually decreases as the number of iterations increases. This shows that implicit bias words become more precise with amplifying bias training, leading to better debiasing effects."

## [NEGATIVE] Excessive Iterative Bias Amplification Training
Continuing iterative bias amplification training beyond the optimal number of iterations (past 4th-5th iteration)

**Delta**: fairness decreases after 4th or 5th iteration
**Condition**: When iteration count exceeds 4-5 iterations during bias amplification

**Evidence**: "the elimination of bias is not endless, and the fairness peaks at the 4th or 5th iteration and then decreases. We analyze that excessive iterative training destroys the language modeling ability of the biased model, which in turn affects the performance of searching for implicit bias words."

## [POSITIVE] Tiny-BERT as Biased Model
Using Tiny-BERT (a small variant of BERT) as the model for bias amplification, leveraging the finding that smaller models tend to be more biased than larger models

**Delta**: reduces training overhead while amplifying bias
**Condition**: Used in the bias amplification stage for all experiments

**Evidence**: "Previous research has shown that smaller models tend to be more biased than larger models. Therefore, we consider Tiny-BERT, a small variant of BERT, as the biased model. This provides the benefits of amplifying bias while reducing training overhead."

## [POSITIVE] Jensen-Shannon Divergence Bias Regularization
Adding a bias regularization term using JSD to measure inconsistency between gender-specific probability distributions, with negative JSD values to differentiate distributions and amplify bias

**Delta**: outperforms baseline
**Condition**: Applied during bias amplification training stage

**Evidence**: "We then add a bias regularization term that applies Jensen-Shannon divergence (JSD) and reweights the training samples to amplify the model bias... to differentiate the two distributions so that the model makes inconsistent decisions, we take negative values for the results of JSD."

## [POSITIVE] Bias Degree Sample Reweighting
Computing a bias degree for each sample by summing bias scores of implicit bias words it contains, then using this to reweight samples during training so the model focuses on potentially harmful biased samples

**Delta**: outperforms baseline
**Condition**: Applied in both bias amplification and debiasing training stages

**Evidence**: "Samples with higher bias degrees contain more harmful associations related to gender. Reweighting changes the attention of samples, so that the PLM focuses on potentially harmful biased samples during training."

## [POSITIVE] Combined Task and Debiasing Objective
Using a combined loss function of cross-entropy task loss and debiasing regularization term (Ldebias = Lce + γ × Ld) to maintain predictive ability while improving fairness

**Delta**: outperforms baseline
**Condition**: Applied during debiasing training stage across all tasks and PLMs

**Evidence**: "Data-Debias minimizes the damage to accuracy while greatly debiasing, which benefits from our debiasing strategy that combines the task objective and the debiasing objective."

## [POSITIVE] Counterfactual Data Augmentation with Explicit Bias Words
Generating augmented sample pairs by replacing explicit bias words (e.g., woman/man, girl/boy) with all pairs in a predefined gender-specific word list

**Delta**: outperforms model-centric baselines
**Condition**: Used as a preprocessing step before implicit bias word search; also used by baseline CDA method

**Evidence**: "the three data-centric baselines CDA, Auto-Debias, and MABEL are more stable in debiasing than the three model-centric baselines INLP, Sent-Debias, and FairFil, achieving more effective debiasing with less degradation in task performance."

## [POSITIVE] Implicit Bias Word Auxiliary Prompts for Large-Scale PLMs
Using top-3 implicit bias words per biased sample to generate auxiliary prompts (e.g., 'Reduce the focus on keywords X, Y, Z') to guide large-scale PLMs toward fair decisions without fine-tuning

**Delta**: 91.08% debias rate on ToxiGen for T5; 95.64% debias rate on ToxiGen for LLaMA
**Condition**: Applied to zero-shot tasks on T5-Large and few-shot tasks on LLaMA-7B

**Evidence**: "T5 and LLaMA are sensitive to implicit bias words, especially in ToxiGen dataset, with an effective rate of 91.08% and 95.64%, respectively. Furthermore, the TPR scores achieve decent results, indicating that the model maintains predictive abilities while improving fairness."

## [POSITIVE] Data-Centric vs Model-Centric Debiasing
Focusing on improving training data quality rather than modifying model architecture or adding regularization to the model

**Delta**: outperforms model-centric baselines
**Condition**: Compared across all three tasks and three PLMs

**Evidence**: "the three data-centric baselines CDA, Auto-Debias, and MABEL are more stable in debiasing than the three model-centric baselines INLP, Sent-Debias, and FairFil, achieving more effective debiasing with less degradation in task performance. However, the gap is marginal, because while data-centric baselines capture the direct harm caused by explicit bias words, they ignore potentially harmful associations in the data."

## [POSITIVE] Top-ε% Implicit Bias Word Selection
Selecting only the top ε=30% of implicit bias words ranked by bias score for use in the bias amplification training stage

**Delta**: outperforms baseline
**Condition**: Applied during bias amplification training; ε=30% chosen as hyperparameter

**Evidence**: "the implicit bias words list W′ in the amplifying bias training stage is selected to be the top ε = 30%"

## [NEUTRAL] Bias Threshold Filtering
Filtering out tokens with bias scores smaller than threshold θ=0 before adding them to the implicit bias word list

**Delta**: no specific quantitative delta reported
**Condition**: Applied during implicit bias word search; θ=0 in all experiments

**Evidence**: "To obtain biased words that have a discriminative impact on different gender groups, we filter out tokens that are smaller than the bias threshold θ and add the remaining tokens to the implicit bias word list W"

## [POSITIVE] Debiasing on RoBERTa
Applying Data-Debias to RoBERTa, which shows improvement in both fairness and task metrics

**Delta**: FR/TR reduced from 5.52 to 3.22 on SST2; task accuracy improved
**Condition**: Applied specifically to RoBERTa on SST2 and other tasks

**Evidence**: "In the case of RoBERTa, Data-Debias reduces bias and even improves predictive ability."

## [POSITIVE] Moderate Debiasing Iterations
Using a moderate number of debiasing iterations (4th iteration used in reported results) rather than maximum iterations

**Delta**: In most iterations, the scores of all task metrics are improved over the original BERT
**Condition**: Applied during debiasing training; results reported using 4th iteration implicit bias words

**Evidence**: "In most iterations, the scores of all task metrics are improved over the original BERT, indicating that moderate debiasing is beneficial to the accuracy of the model."
