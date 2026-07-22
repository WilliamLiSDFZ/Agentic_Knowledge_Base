# Towards Understanding Task-agnostic Debiasing Through the Lenses of Intrinsic Bias and Forgetfulness

**Source**: https://aclanthology.org/2024.findings-acl.109/

## [POSITIVE] ProSocialTuning
A framework that propagates socially-fair debiasing to downstream fine-tuning by regularizing successfully debiased attention heads, guided by generalization importance estimated via PAC-Bayes training.

**Delta**: Best bias score across all downstream fine-tuning tasks (e.g., BiasBios bias: .003 vs .013 for Debiased-tuning on BERT; StereoSet increase of only 0.35 vs 1.33 for Debiased-tuning on STS-B)
**Condition**: Applied to BERT-base and RoBERTa-base on NLI-bias, STS-B, and BiasBios downstream tasks

**Evidence**: "Overall, ProSocialTuning achieves the best bias score for all downstream fine-tuning tasks, except the NLI-bias dataset with RoBERTa model, wherein MABEL outperforms other methods in both accuracy and bias."

## [POSITIVE] Generalization-guided Regularization
Regularization applied to successfully debiased attention heads during downstream fine-tuning, weighted by their generalization importance scores derived from PAC-Bayes training.

**Delta**: STS-B Bias: .177 vs .180 (Uniform Regularization) vs .216 (Random Attention); STS-B Accuracy: .460 vs .455 vs .459
**Condition**: Ablation study on STS-B with BERT-base

**Evidence**: "The generalization-guided regularization alleviates the negative impact on downstream task-specific performance and keeps those debiased attention heads to avoid relearning too many biases during downstream fine-tuning."

## [NEGATIVE] Counterfactual Data Augmentation (CDA) for Debiasing
Rebalancing the debiasing corpus with gender words to debias PLMs before downstream fine-tuning.

**Delta**: Downstream accuracy decreases (e.g., Debiased-tuning NLI-bias accuracy .751 vs Vanilla-tuning .795 on BERT)
**Condition**: Applied for 150 epochs on BERT-base and RoBERTa-base before downstream fine-tuning

**Evidence**: "the downstream task-specific performance with CDA prohibits widespread usage owing to its negative impact on language modeling ability."

## [POSITIVE] Reduced CDA Epochs
Applying counterfactual data augmentation for fewer epochs (25 instead of 150) to reduce impact on language modeling ability.

**Delta**: BiasBios accuracy improved from .668 to .708 for Debiased-tuning when reducing CDA epochs from 150 to 25
**Condition**: BERT on BiasBios dataset, CDA epochs reduced from 150 to 25

**Evidence**: "It is obvious that reducing the CDA epochs can significantly improve downstream performance, since any effects on language modeling ability are weakened."

## [POSITIVE] PAC-Bayes Generalization Importance Estimation
A post-training method that estimates parameter-wise generalization importance by learning noise variance through minimizing a PAC-Bayes bound; higher noise variance indicates less importance.

**Delta**: ProSocialTuning outperforms Uniform Regularization (STS-B Bias: .177 vs .180) and Random Attention (.177 vs .216)
**Condition**: Used within ProSocialTuning for attention head importance weighting

**Evidence**: "Our proposed generalization importance estimation method is task-agnostic and less sensitive to hyperparameters, enabling ubiquitous application of our proposed framework for downstream applications."

## [POSITIVE] Causal Mediation Analysis (CMA) for Bias-inducing Head Detection
Using CMA to identify which attention heads are bias-inducing in pretrained vs. debiased models, enabling targeted regularization of successfully debiased heads.

**Delta**: Enables identification of successfully debiased attention heads; ProSocialTuning achieves best bias scores overall
**Condition**: Applied to BERT-base using Winograd-schema-style examples from Vig et al. (2020)

**Evidence**: "By comparing B0 and Ba, we can determine which attention heads are debiased. ProSocialTuning propagates the learned fairness to downstream fine-tuning tasks by regularization over those successfully aligned attention heads."

## [POSITIVE] Debiased Model as Bias Lower Bound
Using the bias level of the debiased model as an approximate lower bound for the bias of any downstream fine-tuned model, guiding regularization targets.

**Delta**: Debiased model bias score 53.20; Debiased-tuning increases to 54.53-54.94; ProSocialTuning stays at 53.55-54.67
**Condition**: Empirically validated across BERT-base on STS-B, NLI-bias, and BiasBios

**Evidence**: "the bias level of the debiased PLMs is the approximate lower bound for any fine-tuned PLMs for practical cases... ProSocialTuning leads to a smaller increase of bias levels."

## [NEGATIVE] EAR (Entropy-based Attention Regularization)
An attention-based debiasing method that introduces a regularization term for minimizing the entropy of attention heads.

**Delta**: STS-B Bias: .233 (EAR) vs .197 (Vanilla-tuning) on BERT; RoBERTa NLI-bias Bias: .040 vs .021 Vanilla
**Condition**: Inconsistent across tasks; worse than Vanilla-tuning on STS-B for BERT and NLI-bias for RoBERTa

**Evidence**: "EAR demonstrates good accuracy and bias score improvements when applied to the BERT backbone model in the NLI-bias task. However, in certain scenarios, its bias score surpasses even that of the Vanilla-tuning method."

## [NEUTRAL] MABEL (Textual Entailment-based Debiasing)
Enhances CDA by pretraining PLMs with NLI datasets (SNLI and MNLI) for task-agnostic debiasing.

**Delta**: Best on RoBERTa NLI-bias (Bias: .008), but STS-B Bias .181 worse than Debiased-tuning .030 on RoBERTa; BERT STS-B Bias .181 comparable
**Condition**: Inconsistent across tasks and backbone models; uses additional SNLI/MNLI pretraining data

**Evidence**: "MABEL showcases increased bias compared to Vanilla-tuning in the STS-B task, highlighting the inefficiency of a purely task-agnostic debiasing approach devoid of interventions during downstream fine-tuning processes."

## [NEUTRAL] INLP (Iterative Nullspace Projection)
A task-dependent debiasing method that removes gender information from sentence representations via iterative nullspace projection of linear classifiers.

**Delta**: Good on RoBERTa BiasBios (Bias: .008), but highly biased with BERT BiasBios (Bias: .038 vs .018 Vanilla-tuning)
**Condition**: Only applicable to BiasBios (requires gender annotation); inconsistent across backbone models

**Evidence**: "INLP achieves rather good accuracy and debiasing performance given the RoBERTa model and the BiasBios dataset, but it leads to a highly biased fine-tuned model with BERT."

## [POSITIVE] High-quality Long-contextualized Debiasing Corpus
Using a high-quality and long-contextualized corpus for task-agnostic debiasing to preserve language modeling ability.

**Delta**: Alleviates impact on language modeling ability (described qualitatively)
**Condition**: General recommendation for task-agnostic debiasing

**Evidence**: "The impact on language modeling ability can be alleviated given a high-quality and long-contextualized debiasing corpus."

## [POSITIVE] Downstream Dataset Size Variation
Varying the number of training samples in downstream fine-tuning to study its effect on bias relearning.

**Delta**: Fewer training samples (e.g., 100) result in lower bias scores closer to debiased model level
**Condition**: Studied on BERT with Jigsaw, MNLI, SNLI datasets; dataset sizes 100-10000

**Evidence**: "Given the experimental results regarding varying dataset sizes (Figure 1(d)-(f)), it is obvious that fewer training samples result in lower bias scores."

## [NEGATIVE] Bias-inducing Attention Shift Analysis
Observing that attention heads' bias-inducing effects shift inconsistently across pretraining, debiasing, and fine-tuning stages due to the forgetting issue.

**Delta**: Strong inconsistency in CMA effect distributions across fine-tuned models based on same debiased model
**Condition**: Observed on BERT-base fine-tuned on NLI-bias, STS-B, and BiasBios

**Evidence**: "The effect distributions of attention heads within the pretrained model, debiased model, and fine-tuned models are rather different even though those fine-tuned models are all based on the same debiased model... This strong inconsistency, termed as bias-inducing attention shift, is attributed to the forgetting issue of PLMs."

## [NEGATIVE] Random Attention Head Regularization
Randomly selecting attention heads to regularize during downstream fine-tuning (ablation baseline).

**Delta**: STS-B Bias: .216 vs .177 for ProSocialTuning; Accuracy: .459 vs .460
**Condition**: Ablation study on STS-B with BERT-base

**Evidence**: "We consider Random Attention to randomly pick up attention heads to regularize during downstream fine-tuning... [ProSocialTuning outperforms]"

## [NEGATIVE] Uniform Regularization over Debiased Heads
Applying uniform (non-generalization-guided) regularization over successfully debiased attention heads without importance weighting.

**Delta**: STS-B Bias: .180 vs .177 for ProSocialTuning; Accuracy: .455 vs .460
**Condition**: Ablation study on STS-B with BERT-base

**Evidence**: "For Uniform Regularization, we do not apply generalization-guided regularization but take uniform regularizations. [ProSocialTuning outperforms on both accuracy and bias]"

## [POSITIVE] Post-training Generalization Importance Estimation
Estimating generalization importance after fine-tuning to convergence rather than during training, ensuring accuracy by referring to the converged model's performance.

**Delta**: Computational benefits over in-training approaches (qualitative)
**Condition**: Applied within ProSocialTuning framework

**Evidence**: "Our method estimates generalization importance in a post-training manner, ensuring the estimation accuracy by referring to the performance of the converged model. ProSocialTuning enjoys computational benefits in contrast to other in-training approaches."
