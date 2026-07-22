# Disentangling Length from Quality in Direct Preference Optimization

**Source**: https://aclanthology.org/2024.findings-acl.297/

## [POSITIVE] Length-Regularized DPO
A modified DPO objective that adds an explicit length penalty term (α|y|) to the RL optimization problem, resulting in an additional regularization margin (α|y_w| − α|y_l|) in the binary classification loss logit. This acts as a per-example learning rate that up-weights gradients for pairs where the chosen answer is shorter.

**Delta**: up to 20% improvement in win rates when controlling for length
**Condition**: Applied to DPO training on summarization (TL;DR) and dialogue (HH) datasets; also validated on Phi-2 with UltraFeedback

**Evidence**: "on the HH task, regularization also leads to mild improvement in win rates...On both HH and TL;DR, the length-regularized experiments with β = 0.05 and β = 0.01 match the average lengths of the corresponding β = 0.5 runs, but achieve statistically significant higher corresponding win rates, with close to 20% improvement on HH and close to 15% improvement on TL;DR."

## [NEGATIVE] Standard DPO (unregularized)
Direct Preference Optimization without any length regularization, trained with varying β values. Optimizes the implicit reward reparameterization of the RLHF objective offline without a separate reward model.

**Delta**: generates answers twice as long as SFT model on average; length explains 30-46% of reward variance OOD
**Condition**: Observed across HH and TL;DR datasets with β ∈ [0.05, 0.1, 0.5]; effect worsens with smaller β

**Evidence**: "the DPO generated answers are, on average, significantly longer than both the preferred and rejected answers...Not only does the DPO model generate longer answers, it also generates answers that are significantly out-of-distribution in terms of length from the offline preference dataset."

## [NEGATIVE] Low β parameter in DPO
Using a smaller β hyperparameter in DPO, which controls the KL divergence penalty from the reference policy. Smaller β allows greater deviation from the reference model.

**Delta**: generates longer responses on average; greater length exploitation
**Condition**: Observed in both HH and TL;DR datasets; β ∈ [0.05, 0.1, 0.5] tested

**Evidence**: "Models trained with smaller values of β generate longer responses on average, which is expected since β controls the deviation from the initial policy."

## [NEGATIVE] GPT-4 as evaluator/judge
Using GPT-4 as an automated judge for head-to-head win rate comparisons between model outputs, with random position flipping to reduce positional bias.

**Delta**: correlation of 0.96 between win rates and unique token count for 13B models vs Davinci-003
**Condition**: Used as judge in automated evaluation; known verbosity bias inflates scores for longer outputs

**Evidence**: "even as an evaluator, GPT-4 exhibits strong preferences for length. Prior work (Wang et al., 2023) has noted that when evaluating 13B parameter models in head-to-head comparisons with the Davinci-003 model, win rates and the average number of unique tokens in the model's response have correlation of 0.96."

## [NEGATIVE] OOD bootstrapping in DPO implicit reward
The DPO implicit reward model, trained on offline preference data, exhibits significant length bias when evaluated on out-of-distribution model-generated responses, even when showing little to no length correlation within the training distribution.

**Delta**: length explains 30-46% of reward variance out-of-distribution (R² of linear regression)
**Condition**: Observed across HH and TL;DR datasets for standard DPO; the OOD length bias is the root cause of verbosity exploitation in DPO

**Evidence**: "within distribution, the corresponding implicit reward models exhibit weak to no length correlation (and even negative length correlation with strong α regularization). However, they all show significant length bias out-of-distribution, with length explaining 30-46% of the reward variance (as measured by the R² of a linear regression of the implicit DPO reward on answer length)."

## [NEGATIVE] Early stopping / early convergence in standard DPO
Standard DPO achieves its best win rate performance within the first ~10% of an epoch, after which only KL divergence and response length increase without quality improvement.

**Delta**: win rate peaks early and does not improve with further training; length nearly doubles within first 10% of epoch
**Condition**: Observed on HH dataset with β = 0.1; attributed to length exploitation exploiting GPT-4 evaluator bias

**Evidence**: "Within the first 10% of the epoch, the standard DPO run produces answers almost twice as long as the SFT model. Standard DPO achieves its highest win rate here, with only KL divergence and average length increasing steadily with further training."

## [POSITIVE] Length regularization enabling sustained training improvement
Length-regularized DPO shows steady improvement in win rates throughout training rather than early convergence, allowing the model to learn more complex preference features beyond verbosity.

**Delta**: outperforms non-regularized model along all fronts (KL, winrate, and length) at end of 2 epochs; achieves higher final winrates at less than 40% of the KL budget and almost half the response length
**Condition**: HH dataset, β = 0.1, α = 0.1, trained for 2 epochs

**Evidence**: "the length-regularized run sees little to no intermediate increase in length, but steady improvement in win rates throughout training and slow increases in divergence from the reference policy. Our final regularized checkpoint outperforms the non-regularized model along all fronts (KL, winrate, and length) at the end of 2 epochs."

## [NEUTRAL] KL divergence as regularizer (β parameter)
The β-weighted KL divergence term in the DPO/RLHF objective that penalizes deviation from the reference policy. Investigated as a proxy for controlling verbosity.

**Delta**: only weak correlation between KL divergence and response length
**Condition**: Analyzed across HH and TL;DR datasets; KL budget alone is insufficient to control verbosity

**Evidence**: "We see only a weak correlation between KL divergence and length. For both HH and TL;DR, length-regularized models trained with β = 0.05 and β = 0.01 match the average length of train runs with β = 0.5 (Fig. 3). At the same time, these runs have statistically significant higher KL divergences and win rates."

## [NEUTRAL] Supervised Fine-Tuning (SFT) initialization
Pre-training the model with supervised fine-tuning on task-specific data before applying DPO alignment. Used as the reference policy and baseline for length comparisons.

**Delta**: SFT model produces shorter responses than DPO; length-regularized DPO stays closer to SFT length distribution
**Condition**: Used as initialization for both standard and regularized DPO on HH and TL;DR; 1 epoch of SFT prior to DPO

**Evidence**: "While the length-regularized models still show mild increase in average length, they match the SFT model much more closely. Moreover, they do not generate answers with significantly out-of-distribution lengths."

## [POSITIVE] Length regularization on Phi-2 with UltraFeedback
Applying the length-regularized DPO (α = 0.05) to the 2.7B Phi-2 model trained on the 64K UltraFeedback binarized dataset, evaluated on MT Bench.

**Delta**: MT Bench mean score: 6.50 (regularized) vs 6.48 (standard DPO) vs 5.92 (SFT); sample length: 269.21 (regularized) vs 276.01 (standard DPO)
**Condition**: Phi-2 2.7B model, UltraFeedback dataset, β = 0.1, α = 0.05, evaluated on MT Bench

**Evidence**: "The results (Table 2) indicate that the length regularization strategy decreases length, while actually increasing downstream performance, though both gains are small."

## [POSITIVE] Random position flipping in GPT-4 evaluation
Randomly flipping the order of responses A and B when querying GPT-4 as a judge to mitigate known positional bias in LLM-based evaluation.

**Delta**: mitigates known positional bias (no specific delta reported)
**Condition**: Applied in all GPT-4 win rate evaluations throughout the paper

**Evidence**: "256 samples evaluated for length and winrates. GPT-4-0613 used as judge with prompt similar to (Rafailov et al., 2023), with random position flipping."
