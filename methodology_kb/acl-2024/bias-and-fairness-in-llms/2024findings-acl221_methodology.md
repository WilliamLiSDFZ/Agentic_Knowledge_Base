# Adversarial Preference Optimization: Enhancing Your Alignment via RM-LLM Game

**Source**: https://aclanthology.org/2024.findings-acl.221/

## [POSITIVE] Adversarial Preference Optimization (APO) Framework
A minmax game between the LLM and reward model where the LLM generates responses to maximize expected reward while the RM tries to distinguish score differences between golden and sampled responses, updating alternatively each epoch.

**Delta**: outperforms baseline
**Condition**: Applied on top of RJS, RRHF, and DPO baselines with Alpaca and LLaMA-2 on Helpful&Harmless dataset

**Evidence**: "With comprehensive experiments, we find the proposed adversarial training framework further enhances existing alignment baselines in terms of LLM helpfulness and harmlessness."

## [POSITIVE] APO RM KL Regularizer
A forward KL divergence constraint KL[P||Qϕ] applied to the reward model to prevent overfitting to the APO sample set and maintain faithfulness to ground-truth human preference distribution.

**Delta**: RMGAIL (without KL) accuracy drops to 56.58% vs RMAPO-v1.1 at 66.73% on HHTest
**Condition**: RM optimization step of APO

**Evidence**: "When removing the RM KL-regularizer, the performance of RMGAIL becomes too bad to align LLMs, which highlights the importance of the RM KL-constraint in the APO objective."

## [POSITIVE] Bradley-Terry Loss Approximation for APO-RM
Using the Bradley-Terry ranking loss as a practical approximation of the WGAN-like APO-RM objective (equation 14) for training stability.

**Delta**: RMWGAN ECE 0.067 vs RMAPO-v1.1 ECE 0.033 on HHTest
**Condition**: RM optimization step; compared to direct WGAN objective

**Evidence**: "Using the original WGAN-like objective, RMWGAN gets slightly worse on preference accuracy, but the calibration errors increase significantly. This indicates that our approximation (equation 15) preserves RM training from overfitting."

## [POSITIVE] APO Sample Data (D_APO)
A dataset pairing golden responses with LLM-generated samples for the same queries, used to train the RM to distinguish between golden and generated responses without additional human annotation.

**Delta**: RMAB-v1 (without D_APO) accuracy 63.53% vs RMAPO-v1.1 accuracy 66.73% on HHTest
**Condition**: RM training; removing D_APO degrades to continual training baseline

**Evidence**: "Without the APO sample data D_APO, RMBase-AB shows an apparent performance gap compared to APO RMs, which supports the effectiveness of D_APO."

## [POSITIVE] Multi-epoch Adversarial Training
Running multiple rounds of alternating RM and LLM updates in the APO game, allowing performance gains to accumulate across epochs.

**Delta**: Performance gap between APO and RJS visibly enlarges when training epochs increase
**Condition**: Multi-epoch alignment with RJS method; tested for 3 epochs

**Evidence**: "The performance gap between APO and RJS visibly enlarges when training epochs increase. Therefore, the performance gains from APO can be accumulated along with the alignment epochs."

## [NEGATIVE] Sequential APO-RM Updates
Instead of training each epoch's RM from the LLaMA base checkpoint, sequentially updating the RM from the previous epoch's checkpoint.

**Delta**: RMAPO-v3seq ECE 0.093 vs RMAPO-v3 ECE 0.031 on HHTest; fails to align LLM in third epoch
**Condition**: Multi-epoch APO training; second epoch competitive but third epoch fails

**Evidence**: "Sequentially APO RM training causes notably higher calibration errors and fails to align LLM in the third training epoch."

## [NEGATIVE] GAIL Objective for RM (no KL constraint)
Removing the RM KL-regularizer from APO, reducing it to the GAIL objective which has no explicit constraint on the discriminator.

**Delta**: RMGAIL-v1 accuracy 56.58% vs RMBase 63.04% on HHTest; ECE 0.167 vs 0.019
**Condition**: RM ablation; RMGAIL performs worse than even the baseline RMBase

**Evidence**: "When removing the RM KL-regularizer, the performance of RMGAIL becomes too bad to align LLMs, which highlights the importance of the RM KL-constraint in the APO objective."

## [POSITIVE] GPT-4 Generated Golden Responses
Using GPT-4 API responses as simulated golden annotations instead of human-labeled responses to reduce annotation cost.

**Delta**: Alpaca2-Golden RMAll score 2.310 vs Alpaca2 base 1.272
**Condition**: Used as positive responses in D_APO for RM training; also used for Golden SFT baseline

**Evidence**: "GPT-4 has been recognized as the state-of-the-art LLM, so we assume its responses are qualified to be golden for LLaMA-based 7B models."

## [POSITIVE] Golden Data in APO vs Direct SFT Fine-tuning
Using golden responses within the APO framework for RM training rather than directly fine-tuning the LLM on golden responses (SFT).

**Delta**: Alpaca2-APODPO RMAll 2.633 vs Alpaca2-Golden RMAll 2.310
**Condition**: Comparing APO-enhanced alignment methods vs golden SFT on Alpaca/Alpaca2 base models

**Evidence**: "Although Alpaca-Golden and Alpaca2-Golden have significant improvements compared to the original SFT models, aligning SFT models with RRHF and DPO reaches higher average scores. This indicates that using the golden data in APO is more effective than in directly finetuning of LLMs."

## [POSITIVE] DPO as LLM Alignment Baseline
Direct Preference Optimization used as the LLM update step within APO, replacing the reward model with likelihood ratios.

**Delta**: Alpaca2-DPO RMAll 2.445 vs Alpaca2-RRHF 2.201 vs Alpaca2-RJS 1.582
**Condition**: One-epoch LLM alignment on Alpaca2 base model

**Evidence**: "Comparing the three alignment methods, we uniformly find that DPO is the most effective method, while RJS has the lowest effectiveness."

## [POSITIVE] APO Enhancement of DPO
Applying the APO framework (adversarial RM updates) on top of DPO for LLM alignment.

**Delta**: Alpaca2-APODPO RMAll 2.633 vs Alpaca2-DPO 2.445; win rate 74.22% vs 68.86%
**Condition**: One-epoch alignment on Alpaca2; evaluated by RMAll score and GPT-4/human win rates

**Evidence**: "When applying APO, all three alignment methods can be further enhanced with better performance."

## [POSITIVE] APO Enhancement of RRHF
Applying the APO framework on top of RRHF alignment method.

**Delta**: Alpaca2-APORRHF RMAll 2.302 vs Alpaca2-RRHF 2.201; win rate 69.64% vs 62.77%
**Condition**: One-epoch alignment on Alpaca2

**Evidence**: "When applying APO, all three alignment methods can be further enhanced with better performance."

## [POSITIVE] APO Enhancement of RJS
Applying the APO framework on top of rejection sampling (RJS/RAFT) alignment method.

**Delta**: Alpaca2-APORJS RMAll 1.623 vs Alpaca2-RJS 1.582; win rate 36.43% vs 35.78%
**Condition**: One-epoch alignment on Alpaca2; smallest gain among the three methods

**Evidence**: "When applying APO, all three alignment methods can be further enhanced with better performance."

## [POSITIVE] Larger Beta Re-weighting for D_APO
Using a larger re-weighting parameter β for the APO sample set D_APO relative to D_P to avoid overfitting on the smaller APO dataset.

**Delta**: descriptive only
**Condition**: APO-RM training when D_APO is significantly smaller than D_P

**Evidence**: "In experiments, we find the re-weighting parameter β requires to be larger to avoid over-fitting on the relatively smaller APO sample set D_APO."

## [NEUTRAL] Epoch-by-epoch Learning Rate Decay for LLM
Decreasing learning rates across training epochs: 5e-6 for first epoch, 2e-6 for second, 9e-7 for third.

**Delta**: not quantified separately
**Condition**: LLM training setup; part of standard training configuration

**Evidence**: "We decrease learning rates epoch-by-epoch, i.e., the first epoch with 5e-6, the second epoch with 2e-6, and the third epoch with 9e-7."

## [POSITIVE] Continuous APO RM Accuracy Improvement
The APO RM's preference accuracy continuously improves across adversarial training rounds (v1 → v2 → v3) without additional human annotation.

**Delta**: RMAPO-v1.1: 66.73%, RMAPO-v2: 67.07%, RMAPO-v3: 67.56% on HHTest accuracy
**Condition**: Multi-epoch APO-RJS training

**Evidence**: "Through the APO game, the performance of APO RMs continuously improves (v1.1 → v2 → v3) in terms of preference accuracy."

## [NEGATIVE] APO RM Calibration Error Increase
While APO improves preference accuracy, it slightly raises the calibration error of the reward model compared to RMBase.

**Delta**: RMAPO-v1.1 ECE 0.033 vs RMBase ECE 0.019 on HHTest
**Condition**: APO RM training; trade-off between accuracy and calibration

**Evidence**: "We find the APO RM uniformly achieves better preference accuracy than RMBase, but slightly raises the calibration error meanwhile."

## [POSITIVE] Position Swap in GPT-4 Evaluation
Swapping the order of model responses in GPT-4 pairwise evaluation to avoid position bias and improve annotation credibility.

**Delta**: descriptive only
**Condition**: GPT-4 automatic evaluation of LLM responses

**Evidence**: "To avoid position bias and make annotation more credible, we employ COT and position-swap techniques."

## [POSITIVE] Chain-of-Thought (COT) in GPT-4 Evaluation
Using chain-of-thought prompting in GPT-4 pairwise evaluation to elicit reasoning before final judgment.

**Delta**: descriptive only
**Condition**: GPT-4 automatic evaluation of LLM responses

**Evidence**: "To avoid position bias and make annotation more credible, we employ COT and position-swap techniques."
