# Can LLMs Speak For Diverse People? Tuning LLMs via Debate to Generate Controllable Controversial Statements

**Source**: https://aclanthology.org/2024.findings-acl.956/

## [POSITIVE] Multi-round Debate between LLMs
Two LLM agents are prompted to hold opposite stances on a controversial topic and debate for multiple rounds, with each agent refining its statements in response to the opponent's challenges, without requiring consensus.

**Delta**: Overall Controversy Controllability: 0.969 vs 0.848 baseline (Vicuna 7B v1.5); Win score 1.81 vs 1.00 baseline
**Condition**: Applied during data generation phase for controversial debate topics; used with ChatGPT-class models as debate agents

**Evidence**: "even a one-round debate can significantly improve our model's capability on both two metrics. During the debate, the involved agent is required to strictly stick to the given stance, otherwise will be rebuked by the opponent. Then after rebuttal, the agent is able to further refine its previous response."

## [POSITIVE] 2-Round Debate (optimal rounds)
Setting the number of debate rounds to 2 as the default configuration for the debate phase.

**Delta**: Overall Controllability 0.969 (2-round) vs 0.952 (1-round) vs 0.965 (3-round); Win score 1.81 (2-round) vs 1.79 (1-round) vs 1.79 (3-round)
**Condition**: Ablation study on LLaMA-7B model with 3 arguments per topic

**Evidence**: "In the upper section, it is observed that a 2-round debate is the optimal setting"

## [POSITIVE] 3 Arguments per Topic (optimal argument count)
Generating 3 diverse seed arguments per stance per topic for training data construction.

**Delta**: Overall Controllability 0.969 (3-arg) vs 0.933 (1-arg) vs 0.933 (5-arg); Win score 1.81 (3-arg) vs 1.82 (1-arg) vs 1.80 (5-arg)
**Condition**: Ablation study with 2-round debate on LLaMA-7B; marginal difference in response quality but clearer in controllability

**Evidence**: "The 3-Argument setting marginally outperforms the other options, thus we continuously set it as our default setting."

## [POSITIVE] Debate-Augmented Instruction Tuning (DEBATUNE)
Finetuning an LLM on instruction-tuning data where responses are generated via multi-round debate, pairing (topic, stance, argument) as input with debate-refined statements as output.

**Delta**: DEBATUNE-7B achieves Overall Controversy Controllability 0.969 vs best competing model 0.910 (WizardLM 13B); human study: 87/100 Good vs 40/100 Good for Vicuna baseline
**Condition**: Applied to LLaMA-7B and LLaMA-13B base models; evaluated on held-out 80 controversial topics

**Evidence**: "our DEBATUNE, achieves the highest scores on both aspects compared with existing models, indicating our model's ability to speak for the minority."

## [POSITIVE] Topic Data without Debate
Training on controversial topic data where responses are generated directly by gpt-3.5-turbo-1106 without any debate process.

**Delta**: Win score 1.64 vs 1.00 baseline; Overall Controllability 0.879 vs 0.848 baseline, but lower than 1-round debate (0.952)
**Condition**: Ablation condition; improvement over baseline but inferior to debate-augmented variants

**Evidence**: ""Topic Data without Debate" represents the model trained directly with the training split of our controversial topics, whose response is generated from gpt-3.5-turbo-1106 without debate. We can observe clear improvements in both the Response Quality and Controversy Controllability"

## [POSITIVE] No-Consensus Debate Framework
Designing the debate so agents are not required to reach a consensus, instead freely defending their own stances and questioning the opponent throughout all rounds.

**Delta**: outperforms baseline
**Condition**: Contrasted with prior debate frameworks (Du et al. 2023; Liang et al. 2023) that force consensus; applied to controversial topic generation

**Evidence**: "our pipeline simulates real-world debates, in which two agents holding different stances can freely question or contrast each other and they are not required to reach a consensus... reaching a consensus is non-trivial, and always requires an additional Judge, Confidence Estimator or Summarizer, which not only introduces more computation but leads to potential instability as well."

## [POSITIVE] Controversy Controllability Metric
A novel GPT-4-based evaluation metric that prompts GPT-4 to analyze a response without knowing the intended stance, then infers the supporting vs. opposing proportion, categorizing responses as Good or Bad based on stance adherence.

**Delta**: High consistency with human evaluation: 87% agreement on Good samples; GPT-4 bad labels confirmed by human experts at high ratio
**Condition**: Evaluation on held-out 80 controversial topics; validated via LLM-Human interactive inspection on 100 samples

**Evidence**: "we also examined a random set of 100 good samples labeled by GPT4 and almost all of them are indeed good samples for human experts. The large discrepancy between Vicuna and our model further verifies our method and the high consistency between human evaluation and LLM evaluation verifies the effectiveness of our evaluation method."

## [NEGATIVE] Strong Alignment (LLaMA2 Chat)
Heavy RLHF-based safety alignment applied to LLaMA2 Chat models, causing them to refuse or find middle-ground answers on controversial topics.

**Delta**: LLaMA2 Chat 7B: Overall Controllability 0.313; LLaMA2 Chat 13B: 0.327 — lowest among all models
**Condition**: Evaluated on controversial debate topic controllability; strong alignment helps safety but hurts stance controllability

**Evidence**: "LLaMA2 Chat models achieve the lowest controllability scores, reasonable due to their strongly constrained alignment. Given a controversial topic, they have a strong tendency to refuse to answer or to find a safe middle ground to avoid potential harm."

## [NEUTRAL] Low Instruction-Following Ability (Alpaca)
Alpaca's relatively weak instruction-following causes it to repeat the given argument with little new content, incidentally producing high controllability scores but very low response quality.

**Delta**: Alpaca 7B: Overall Controllability 0.910 (high) but Win score 0.03 (lowest quality)
**Condition**: Evaluated on controversial debate topics; high controllability is an artifact of repetition, not genuine stance adherence

**Evidence**: "the manual inspection further explains this phenomenon that it is because of the relatively low instruction-following ability, that Alpaca tends to repeat the given argument with only a little new content, thus leading to high controllability and low quality."

## [POSITIVE] Positional Bias Mitigation in LLM Judge
Presenting model responses in two separate sequences to the GPT-4 judge to address positional bias in pairwise evaluation.

**Delta**: not quantified
**Condition**: Applied during Response Quality pairwise evaluation

**Evidence**: "We also address the issue of positional bias in the LLM judge system, as discussed in the studies by Ko et al. (2020); Wang et al. (2023b) by presenting models' responses in two separate sequences for evaluation by the LLM judge."

## [POSITIVE] DEBATUNE on General Instruction Following Benchmarks
Evaluating DEBATUNE-finetuned models (trained only on 630 controversial topics) on general instruction-following benchmarks including HuggingFace Open LLM Leaderboard, Alpaca Eval, and MT Bench.

**Delta**: Vicuna 7B + 3-Arg: HF Leaderboard avg 58.47 vs 57.95; Alpaca Eval win rate 78.76 vs 73.10; MT Bench 6.13 vs 6.07. WizardLM 7B + 1-Arg: Alpaca Eval 74.04 vs 66.08; MT Bench 5.57 vs 5.56
**Condition**: Applied to Vicuna 7B v1.5 and WizardLM 7B base models; generalization beyond controversial topics

**Evidence**: "the model further trained with our data outperforms the baseline models on all of the 4 different evaluation metrics on two different models. It is worth noting that only 630 topics are utilized, indicating the neglectable new knowledge involved in the training, while it causes a consistent improvement in the general instruction-following ability."

## [POSITIVE] LLM-Human Interactive Inspection
A hybrid evaluation method where GPT-4 first labels all bad cases and samples some good cases, then human annotators judge the selected subset of 100 instruction-response pairs.

**Delta**: 87/100 Good, 2/100 Tie, 11/100 Bad for DEBATUNE-7B vs 40/100 Good, 7/100 Tie, 53/100 Bad for Vicuna 7B v1.5
**Condition**: Applied to human study comparing DEBATUNE-7B vs Vicuna 7B v1.5 baseline on 80 test topics

**Evidence**: "we utilize an LLM-Human interactive inspection method. After utilizing LLM as the Judge for the Controversy Controllability evaluation, we select all the bad cases detected by GPT4, and then randomly sample some good cases to construct a new evaluation set with 100 instruction-response pairs."

## [POSITIVE] Curated 710-Topic Debate Dataset
A manually curated dataset of 710 controversial debate topics spanning Society, Ethics, Environment, Technology, Education, Politics, Economics, and Health, split into 630 train and 80 test topics, with GPT-3.5-generated arguments for each stance.

**Delta**: largest open-sourced debate dataset; enables training that achieves 0.969 overall controllability
**Condition**: Used as the foundation for DEBATUNE training and evaluation; existing datasets lacked direct topics or were too biased for both-sides support

**Evidence**: "we curate the largest dataset of debate topics so far, which covers 710 controversial topics and corresponding arguments for each topic... To our knowledge, this is the largest open-sourced debate dataset so far."
