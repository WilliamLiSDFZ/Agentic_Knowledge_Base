# Beyond One-Preference-Fits-All Alignment: Multi-Objective Direct Preference Optimization

**Source**: https://aclanthology.org/2024.findings-acl.630/

## [POSITIVE] Multi-Objective Direct Preference Optimization (MODPO)
An RL-free extension of DPO that folds language modeling into reward modeling, training language models as implicit collective reward models combining all objectives with specific weights via cross-entropy loss, eliminating value function modeling and online sample collection.

**Delta**: outperforms baseline; 3x less computational resources than MORLHF
**Condition**: Multi-objective alignment tasks including safety alignment and long-form QA

**Evidence**: "Empirical results in safety alignment and long-form question answering show that MODPO matches or outperforms existing methods, producing a Pareto front of language models catering to diverse preferences with three times less computational resources compared to MORLHF."

## [POSITIVE] RL-free training via cross-entropy loss
Replacing reinforcement learning (PPO) with a simple cross-entropy/binary classification loss for optimizing language models against multiple alignment objectives.

**Delta**: Safety alignment: 4.0±0.1 GPU hours vs MORLHF 13.8±0.7; Long-form QA: 9.4±0.2 vs 34.0±0.5
**Condition**: Multi-objective preference alignment

**Evidence**: "MODPO theoretically yields the same optimal solutions as MORLHF but is practically more stable and efficient... eliminating value function modeling and online sample collection."

## [POSITIVE] Margin reward modeling
Training margin reward models on non-preference datasets (D_{-k}) to provide additional objective signals as margin terms in the MODPO loss, allowing the language model to be guided by more than one objective.

**Delta**: outperforms baseline
**Condition**: Multi-objective alignment where at least one preference dataset exists

**Evidence**: "L_MODPO includes additional weightings and a margin term to ensure the language model is guided by more than one objective."

## [POSITIVE] Multi-stage training (margin reward modeling then language modeling)
Two-stage pipeline: first train margin reward models on non-preference datasets, then train language models using MODPO loss with those fixed margin rewards.

**Delta**: outperforms DPO LW baseline
**Condition**: Safety alignment with two preference datasets

**Evidence**: "MODPO's advantage over DPO LW is partially because MODPO handles one objective at a time through multi-stage training, whereas DPO LW concurrently learns two objectives from distinct noisy preference data, which may hinder learning."

## [NEUTRAL] Linear scalarization of multiple reward objectives
Combining multiple reward functions into a single collective reward using a weighted linear combination (w^T r*), allowing reuse of standard alignment pipelines.

**Delta**: standard approach; enables Pareto front generation
**Condition**: Multi-objective preference alignment; assumes linearly composable preferences

**Evidence**: "Following the standard linear scalarization strategy (Li et al., 2020), the goal for multi-objective alignment is not to learn a single optimal language model but rather a (close-to) Pareto front of language models."

## [NEGATIVE] DPO Loss Weighting (DPO LW)
Mixing multiple preference datasets and training simultaneously with loss weighted by preference vector w, as a multi-objective DPO baseline.

**Delta**: underperforms MODPO
**Condition**: Safety alignment with two preference datasets

**Evidence**: "MODPO's advantage over DPO LW is partially because MODPO handles one objective at a time through multi-stage training, whereas DPO LW concurrently learns two objectives from distinct noisy preference data, which may hinder learning."

## [NEGATIVE] DPO Soups (model weight interpolation)
Training separate DPO models for each objective and interpolating their weights to approximate intermediate preference vectors.

**Delta**: underperforms MODPO
**Condition**: Safety alignment with two preference datasets

**Evidence**: "For both β=0.1 and β=0.5, MODPO consistently outperforms DPO soups and DPO LW."

## [NEGATIVE] MORLHF with conflicting objectives
Applying standard RLHF pipeline with linear scalarization to multiple conflicting objectives, requiring separate RL fine-tuning runs per preference vector.

**Delta**: 13.8±0.7 GPU hours per model (safety); 34.0±0.5 GPU hours (long-form QA) vs MODPO's 4.0 and 9.4
**Condition**: Multi-objective alignment; especially with conflicting objectives

**Evidence**: "Multi-objective optimization exacerbates RLHF's training instability and computation inefficiency due to usually conflicting objectives and the need to obtain a set of optimal language models."

## [POSITIVE] KL divergence constraint (β parameter)
Controlling the strength of KL penalty between the trained policy and SFT reference model to maintain generation diversity and avoid reward over-optimization.

**Delta**: β=0.5 shows more pronounced MODPO advantage over MORLHF at cost of slightly more KL budget
**Condition**: Both high KL (β=0.1) and low KL (β=0.5) regimes in safety alignment

**Evidence**: "In the low KL regime (β=0.5), MODPO has a more pronounced advantage over MORLHF, though this larger margin costs a bit more KL budget."

## [POSITIVE] Best-of-n sampling baseline
Sampling n responses and returning the highest-scoring one according to the learned collective reward model, used as a comparison baseline.

**Delta**: unfair oracle in long-form QA; competitive in safety alignment
**Condition**: Safety alignment (fair comparison); long-form QA (unfair oracle due to same reward model for sampling and evaluation)

**Evidence**: "For long-form QA, we use the same reward models for both rejection sampling and evaluation, making the Best-of-n baseline an unfair oracle that significantly exceeds other baselines."

## [NEGATIVE] Discrete reward models as margin rewards
Using discrete/binary reward models (e.g., r_rel, r_fact producing ±1) as margin rewards in MODPO, as opposed to continuous reward models.

**Delta**: increased gradient noise for MORLHF; less pronounced issue for MODPO
**Condition**: Long-form QA with relevance and factuality objectives paired with continuous preference reward

**Evidence**: "This might be due to the discrete nature of r_ϕ,rel and r_ϕ,fact, causing increased gradient noise for MORLHF when paired with the continuous r_ϕ,pref."

## [NEUTRAL] LoRA fine-tuning
Using Low-Rank Adaptation (LoRA) for parameter-efficient fine-tuning of language models during MODPO training.

**Delta**: not quantified separately
**Condition**: All experiments (safety alignment and long-form QA)

**Evidence**: "We train our models using 8 Nvidia 80G A100 GPUs with LoRA (Hu et al., 2021)."

## [POSITIVE] Implicit language model reward parametrization
Parametrizing the margin reward model implicitly as a language model (r_ϕ = β log π_ϕ/π_sft) so that the margin reward model simultaneously produces a language model optimized for w=0.

**Delta**: amortizes margin reward modeling cost across all w
**Condition**: Safety alignment margin reward modeling stage

**Evidence**: "The advantage of this parametrization is that the trained margin reward model simultaneously produces a language model optimized for w=0."

## [POSITIVE] Scaling to three objectives
Extending MODPO from two to three alignment objectives simultaneously.

**Delta**: MODPO fronts dominate MORLHF fronts in 3D objective space
**Condition**: Long-form QA with three objectives [D_rel, D_fact, D_pref]

**Evidence**: "Figure 5b shows that MODPO significantly outperforms MORLHF by a large margin. This agrees with the results from Figure 3, demonstrating a reliable scaling trend."

## [NEUTRAL] GPT-3.5/GPT-4 as evaluators
Using GPT-4 for harmlessness evaluation and GPT-3.5 for helpfulness evaluation (due to GPT-4 content policy restrictions on red-teaming prompts) in real feedback safety alignment experiments.

**Delta**: not quantified as technique delta
**Condition**: Real feedback safety alignment evaluation

**Evidence**: "GPT-4 is used for harmlessness evaluations, while GPT-3.5 (text-davinci-003) is used for helpfulness evaluations as evaluating responses to red-teaming prompts violates GPT-4's content policy."

## [POSITIVE] MORLHF harmlessness advantage via trivial refusal
MORLHF achieves slightly better harmlessness scores because harmlessness can be trivially achieved by refusing to reply, reducing the exploration challenge for RL.

**Delta**: MORLHF slightly better in harmless dimension vs MODPO
**Condition**: Safety alignment, harmlessness objective specifically

**Evidence**: "While MODPO generally performs better in the helpful dimension, MORLHF is slightly better in the harmless dimension. This may be because harmlessness can be trivially achieved by refusing to reply, alleviating the exploration challenge for RL."
