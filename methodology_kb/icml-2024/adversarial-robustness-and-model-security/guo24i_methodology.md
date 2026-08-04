# COLD-Attack: Jailbreaking LLMs with Stealthiness and Controllability

**Source**: https://proceedings.mlr.press/v235/guo24i.html

## [POSITIVE] COLD-Attack Framework
Adapts Energy-based Constrained Decoding with Langevin Dynamics (COLD) for controllable adversarial LLM attack generation, using compositional energy functions and gradient-based sampling in continuous logit space

**Delta**: best or second-best ASRs across all LLMs tested
**Condition**: Attack with continuation constraint across Vicuna, Guanaco, Mistral, Llama2

**Evidence**: "COLD-Attack achieves the best or second-best ASRs across all LLMs and excels in ASR-G, achieving the highest ASR-G on Guanaco and Mistral, and ranking second on Vicuna and Llama2 with comparable success rates."

## [POSITIVE] Continuous Logit Space Optimization via Langevin Dynamics
Performs gradient-based sampling in continuous logit space instead of discrete token-level optimization as in GCG, removing the greedy search step

**Delta**: ~10x faster than GCG; ~20 min vs ~3.23 hours per request
**Condition**: Single NVIDIA V100 GPU, single request optimization

**Evidence**: "COLD-Attack is on average 10× faster than GCG and GCG-reg: executing COLD-Attack for a single request using a single NVIDIA V100 GPU takes about 20 minutes (with 2000 steps and a batch of 8 samples), while GCG and GCG-reg require approximately 3.23 hours for the same task (with 500 steps and a batch size of 512)."

## [POSITIVE] LLM-Guided Decoding Process
A novel decoding method borrowed from COLD that converts continuous logit sequences into fluent discrete text attacks

**Delta**: enables fluency; without it results are typically not fluent
**Condition**: Required for converting continuous logits to discrete text in all attack settings

**Evidence**: "Without the novel decoding method from COLD, the resultant y is typically not fluent."

## [POSITIVE] Fluency Energy Function
Energy function that constrains logit sequences to exhibit autoregressive dependency according to the underlying LLM, encouraging softmax distribution to match LLM predictions

**Delta**: lowest PPL among compared methods; PPL of 32.96 vs 33.43 for AutoDAN-Zhu on Vicuna
**Condition**: Attack with continuation constraint across all tested LLMs

**Evidence**: "COLD-Attack generates the most fluent adversarial prompts with lowest PPL. Both AutoDAN-Zhu and COLD-Attack stand out by achieving better stealthiness with lower PPL compared to other methods. Specifically, COLD-Attack excels further by outperforming AutoDAN-Zhu across all evaluated LLMs."

## [POSITIVE] Attack Success Energy Function
Uses adversarial cost from GCG to maximize probability of LLM generating affirmative responses to malicious requests, defined as E_att(y;z) = -log p_LM(z|y)

**Delta**: contributes to 92-100% ASR on most LLMs
**Condition**: All three attack settings

**Evidence**: "We can use the adversarial cost in (Zou et al., 2023) to design an energy function that forces the target LLM to respond start with a positive affirmation of the malicious request x."

## [POSITIVE] Semantic Similarity Energy Function
Cosine similarity between average token embeddings of attack and original query to enforce paraphrasing constraint

**Delta**: BERTScore above 0.7 on all LLMs, comparable to GPT-4 rephrase BERTScore of 0.75
**Condition**: Attack with paraphrasing constraint

**Evidence**: "The BERTScore for COLD-Attack is above 0.7 on all LLMs, nearly matching the BERTScore of 0.75 by GPT-4 rephrase, demonstrating the good quality of rephrasing."

## [POSITIVE] Lexical Constraint Energy Function (N-gram Matching)
Differential n-gram matching function to control presence of specific keywords/phrases in generated attacks, used for sentiment steering and suppressing refusal phrases

**Delta**: 100% Succ rate for sentiment steering; ASR-G augmented by 30% on Mistral and 14% on Guanaco with negative sentiment
**Condition**: Attack with paraphrasing constraint under sentiment steering

**Evidence**: "COLD-Attack effectively controls the sentiment of the adversarial prompts, as demonstrated by the high Succ and ASRs. Interestingly, our experiments reveal that different LLMs exhibit varying susceptibilities to different sentiments. Particularly, attacks leveraging negative sentiment attain higher ASRs on Mistral and Guanaco, with ASR-G augmenting by 30% and 14% respectively."

## [POSITIVE] Position Constraint (Left-Right Coherence)
Fluency energy applied to full concatenated sequence x⊕y⊕p to ensure attack y inserted between user query and control prompt maintains coherence on both sides

**Delta**: PPL averaging 2x lower than AutoDAN-Zhu and ~40x lower than GCG
**Condition**: Attack with position constraint on Llama2

**Evidence**: "COLD-Attack consistently records the lowest PPL across all constraint scenarios, averaging 2× lower than AutoDAN-Zhu and approximately 40× less than GCG. This demonstrates the importance of posing control on the position of the adversarial prompts explicitly."

## [POSITIVE] Paraphrasing Constraint Attack Setting
Novel attack setting where original user query is rephrased into an adversarial attack, hiding attack position to prevent simple suffix-removal defenses

**Delta**: 96-98% ASR vs 18-58% for PRISM, PAWS, GPT-4 baselines
**Condition**: Paraphrasing constraint across Vicuna, Guanaco, Mistral, Llama2

**Evidence**: "our COLD-Attack approach not only produces high-quality rephrasing but also significantly outperforms three other baseline methods in terms of ASR."

## [POSITIVE] Non-Autoregressive Attack Generation
COLD-Attack samples discrete text attack only once at the end rather than generating token-by-token autoregressively as in AutoDAN-Zhu

**Delta**: enables complex constraints like paraphrasing; faster generation
**Condition**: All attack settings, particularly paraphrasing and position constraints

**Evidence**: "The non-autoregressive nature of COLD-Attack enables incorporating complex constraints such as paraphrasing constraint."

## [POSITIVE] Compositional Energy Function
Weighted sum of multiple energy functions E(y) = sum(lambda_i * E_i(y)) allowing flexible combination of attack success, fluency, semantic similarity, and lexical constraints

**Delta**: enables unified treatment of multiple constraints simultaneously
**Condition**: All attack settings

**Evidence**: "Our attack framework is flexible, allowing the integration of any valid energy functions based on control requirements."

## [NEGATIVE] GCG Discrete Token-Level Optimization
Baseline method using greedy search for discrete token-level optimization at every step to append adversarial suffix

**Delta**: PPL of 821.53-5740 vs COLD-Attack's 24.83-39.26; 156-235 min per sample vs 15-27 min
**Condition**: Compared against COLD-Attack on continuation constraint setting

**Evidence**: "GCG yields gibberish suffixes that are easily detectable by simple perplexity-based defense."

## [NEUTRAL] GCG-reg (Perplexity-Regularized GCG)
GCG variant with perplexity regularization to improve fluency of generated adversarial suffixes

**Delta**: improves PPL over GCG (e.g., 122.57 vs 1142 on Llama2) but still much higher PPL than COLD-Attack (24.83)
**Condition**: Attack with continuation constraint

**Evidence**: "Both GCG and GCG-reg achieve 100% ASR on Vicuna, Guanaco, and Mistral... COLD-Attack consistently records the lowest PPL across all constraint scenarios."

## [POSITIVE] Sentiment Steering via Lexical Energy
Adding sentiment-specific keywords (positive: 'joyful', negative: 'anxious') as lexical constraints to control emotional tone of adversarial paraphrase attacks

**Delta**: ASR-G +30% on Mistral and +14% on Guanaco with negative sentiment; +18% on Llama2 with positive sentiment
**Condition**: Model-dependent: negative sentiment better for Mistral/Guanaco; positive sentiment better for Llama2

**Evidence**: "attacks leveraging negative sentiment attain higher ASRs on Mistral and Guanaco, with ASR-G augmenting by 30% and 14% respectively. Conversely, Llama2 shows greater vulnerability to positive sentiment attacks, where its ASR-G saw an 18% increase when shifting from negative to positive sentiment attacks."

## [NEUTRAL] AutoDAN-Zhu Double-Loop Optimization
Extends GCG with double-loop optimization and autoregressive token-by-token generation to produce fluent jailbreak prompts

**Delta**: lower PPL than GCG but higher than COLD-Attack; 354 min per sample vs 16 min for COLD-Attack
**Condition**: Attack with continuation constraint; cannot handle paraphrasing or position constraints

**Evidence**: "AutoDAN-Zhu (Zhu et al., 2023) extends GCG via a double-loop optimization method to produce fluent jailbreak prompts. However, it utilizes an auto-regressive token-by-token generation approach, inherently limiting its capability in imposing control on attacks."

## [POSITIVE] Diversity Optimization in COLD-Attack
COLD-Attack's energy-based sampling produces diverse adversarial prompts measured by Distinct N-grams Score, Averaged Distinct N-grams, and Self-BLEU

**Delta**: DNS 0.79-0.96 vs AutoDAN-Zhu 0.43-0.49; Self-BLEU 0.29-0.48 vs AutoDAN-Zhu 1.00
**Condition**: Attack with continuation constraint across Vicuna, Guanaco, Mistral, Llama2

**Evidence**: "COLD-Attack consistently outperforms the baseline methods in generating more diverse adversarial prompts."

## [POSITIVE] Langevin Dynamics Noise Annealing
Initializing Langevin dynamics with large noise scale for broad exploration, then reducing noise to converge toward optimal distribution

**Delta**: helps escape local optima
**Condition**: All attack settings during optimization

**Evidence**: "The process is initialized with a large noise scale that achieves large-scale exploration in space and provides a larger possibility for samples to jump out of local optimums. With the right amount of noise and proper step size, Langevin dynamics can approach the optimal distribution."

## [NEUTRAL] AutoDAN-Liu Genetic Search with Manual Prompts
Combines automatic genetic search with manually crafted jailbreak prompts for white-box attacks

**Delta**: lowest PPL on Vicuna (14.76) and Guanaco (15.27) due to manual prompts, but cannot be applied to Mistral; 26-27 min per sample
**Condition**: Attack with continuation constraint; not applicable to Mistral

**Evidence**: "AutoDAN-Liu partially relies on manually crafted prompts (it combines automatic genetic search with manually crafted prompts), resulting in the lowest PPL for Vicuna and Guanaco. Despite this, COLD-Attack achieves a lower PPL on Llama2. Since COLD-Attack does not need manually crafted prompts at all and can potentially generate more diverse attacks, a direct comparison with AutoDAN-Liu may not be that meaningful."
