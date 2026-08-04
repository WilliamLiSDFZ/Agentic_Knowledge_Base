# Fast Adversarial Attacks on Language Models In One GPU Minute

**Source**: https://proceedings.mlr.press/v235/sadasivan24a.html

## [POSITIVE] BEAST (Beam Search-based Adversarial Attack)
A gradient-free beam search optimization technique for generating adversarial prompts against language models, using tunable hyperparameters k1 (beam size) and k2 (sampling breadth) to balance speed, readability, and attack success rate.

**Delta**: 89% ASR on Vicuna-7B in one minute vs 58% for best baseline
**Condition**: Jailbreaking aligned LMs under one-minute time budget on single Nvidia RTX A6000 48GB GPU

**Evidence**: "in just one minute per prompt, we get an attack success rate of 89% on jailbreaking Vicuna-7B-v1.5, while the best baseline method achieves 58%"

## [POSITIVE] Gradient-free optimization
BEAST avoids gradient computation entirely, using multinomial sampling from the LM's token probability distribution instead of backpropagation-based gradient updates.

**Delta**: 25-65x faster than gradient-based methods
**Condition**: Compared to gradient-based baselines GCG and AutoDAN-2

**Evidence**: "Since BEAST uses a gradient-free optimization scheme unlike other optimization-based attacks (Zou et al., 2023; Zhu et al., 2023), our method is 25–65× faster."

## [POSITIVE] Multinomial token sampling for readability
BEAST maintains adversarial prompt readability by sampling adversarial tokens based on the target LM's next token probability distribution rather than using perplexity regularization.

**Delta**: outperforms baseline
**Condition**: Adversarial prompt generation across all BEAST applications

**Evidence**: "BEAST implicitly maintains readability by sampling adversarial tokens based on the LM's predicted token probability distribution."

## [POSITIVE] Increasing beam size k
Increasing the beam size parameter k (where k1=k2=k) expands the search space, improving attack success rate at the cost of increased computation time and slightly reduced readability.

**Delta**: 98% ASR in 2.65 minutes with k=15 vs 66% ASR in 10 seconds at small k
**Condition**: Jailbreaking Vicuna-7B, varying k from 3 to 15

**Evidence**: "our attack on Vicuna-7B can get an ASR of 98% within 2.65 minutes (with k = 15), while we can get an ASR of 66% in just 10 seconds"

## [POSITIVE] Perplexity minimization objective for MIA
An untargeted adversarial objective that minimizes prompt perplexity (equivalent to beam search decoding) to generate adversarial prompts that complement membership inference attacks.

**Delta**: +4.1% AUROC for OPT-2.7B
**Condition**: Membership inference attacks on WikiMIA dataset across OPT, GPT Neo, Pythia, and LLaMA-2 models

**Evidence**: "the area under the receiver operating characteristic (AUROC) curve for OPT-2.7B (Zhang et al., 2022) can be boosted by 4.1% by using our attack to complement the existing MIA techniques"

## [POSITIVE] Perplexity maximization objective for hallucination
An untargeted adversarial objective that maximizes the perplexity of the LM's own autoregressively sampled output, designed to degrade output quality and elicit hallucinations.

**Delta**: ~15% more incorrect outputs; 22% irrelevant responses
**Condition**: Untargeted hallucination attack on Vicuna-7B-v1.5 using TruthfulQA dataset

**Evidence**: "our prompts elicit hallucinations more often than the clean baseline by 14.67%. Also, the responses of the model to our adversarial prompts remain relevant to the original prompt only 78% of the time."

## [POSITIVE] Ensemble logit aggregation for universal adversarial suffixes
Summing logit outputs across multiple user prompts before applying softmax to create an ensemble probability distribution, enabling a single adversarial suffix to simultaneously target multiple prompts.

**Delta**: Train ASR 95%, Test ASR 84.38% on Vicuna-7B
**Condition**: Multi-behavior jailbreaking and transferability to unseen prompts on Vicuna-7B and Vicuna-13B

**Evidence**: "We find that the universal suffixes generated are effective on multiple prompts of the training set simultaneously, and also generalizes well to unseen test prompts."

## [POSITIVE] Combined loss objective for model transferability
Optimizing adversarial suffixes using a combined loss from two models (Vicuna-7B and Vicuna-13B) to improve transferability to unseen models.

**Delta**: 8% ASR on Mistral-7B, 40% on GPT-3.5-Turbo, 12% on GPT-4-Turbo
**Condition**: Black-box transfer attacks on unseen models using suffixes optimized on Vicuna-7B and Vicuna-13B

**Evidence**: "BEAST can successfully transfer to unseen models to obtain high ASR of 8%, 40%, and 12% ASR, respectively, with Mistral-7B, GPT3.5-Turbo, and GPT-4-Turbo."

## [NEGATIVE] Perplexity-based defense (PPL filter)
A defense mechanism that filters out adversarial prompts with perplexity scores exceeding the maximum clean prompt perplexity in the dataset.

**Delta**: ASR drops from 89% to 70% for BEAST at one-minute budget
**Condition**: Applied against BEAST jailbreaking on Vicuna-7B; BEAST still outperforms all baselines under this defense

**Evidence**: "For the defense (denoted as 'PPL'), we first compute the perplexity of all the clean prompts in the AdvBench dataset. Now, the defense filters out any adversarial prompt with a perplexity score greater than the highest clean perplexity score."

## [NEUTRAL] Adversarial token sampling every nth step
A modified BEAST variant that only adversarially selects every nth token position, with remaining tokens sampled naturally from the LM, improving readability at the cost of increased total suffix length.

**Delta**: No effect on ASR; readability improves with higher n
**Condition**: Readability improvement experiments on Vicuna-7B with n ranging from 1 to 5

**Evidence**: "As we observe, increasing n has no effect on the ASR. These results show that n for BEAST can be varied to obtain a tradeoff between readability and attack time without compromising ASR."

## [POSITIVE] Fixed adversarial suffix length L=40
Setting the number of adversarial token generation steps to 40 as a default configuration to balance ASR and attack speed.

**Delta**: outperforms baseline
**Condition**: Default jailbreaking configuration for BEAST across all main experiments

**Evidence**: "We find the attack to run for L = 40 steps to optimize both ASR and the attack speed."

## [NEGATIVE] GCG gradient-based attack (baseline)
A gradient-based optimization method that generates gibberish adversarial token suffixes by computing gradients with respect to the input tokens.

**Delta**: 70% ASR in over one hour vs BEAST 89% in one minute on Vicuna-7B
**Condition**: Jailbreaking Vicuna-7B under time-constrained setting; also vulnerable to perplexity-based defenses due to gibberish tokens

**Evidence**: "BEAST can jailbreak Vicuna-7B-v1.5 under one minute with a success rate of 89% when compared to a gradient-based baseline that takes over an hour to achieve 70% success rate"

## [NEGATIVE] AutoDAN-1 genetic algorithm attack (baseline)
A black-box jailbreak attack using evolutionary/genetic algorithms that requires GPT-4 API access and handcrafted initialization prompts.

**Delta**: 10% ASR in one minute vs BEAST 89% on Vicuna-7B
**Condition**: Resource-constrained jailbreaking; expensive due to GPT-4 API dependency

**Evidence**: "AutoDAN-1 costed $10.25 for attacking on the first 50 samples with a 2 minutes budget constraint experiment."

## [NEGATIVE] PAIR iterative LM-based attack (baseline)
A black-box attack that uses an LM to iteratively generate jailbreaking prompts by querying a target LM, requiring GPT-4 API access and manually crafted system prompts.

**Delta**: 46% ASR in one minute vs BEAST 89% on Vicuna-7B
**Condition**: Resource-constrained jailbreaking on Vicuna-7B

**Evidence**: "PAIR requires carefully written system prompts for their attack to perform well. Zhu et al. (2023) note that PAIR requires manual work to design the system prompts that contain known jailbreak strategies."

## [POSITIVE] PPL+Adv MIA complementation
Combining the perplexity-based membership inference attack (PPL) with BEAST-generated adversarial prompts to boost detection performance.

**Delta**: +1.3% average AUROC improvement over PPL alone
**Condition**: Membership inference on WikiMIA dataset across 7 language models

**Evidence**: "Our adversarial methods PPL + Adv. and Min-k% + Adv., consistently outperform their counterparts PPL and Min-k%."

## [POSITIVE] Min-k%+Adv MIA complementation
Combining the Min-k% Prob membership inference attack with BEAST-generated adversarial prompts to boost detection performance.

**Delta**: +2.7% average AUROC improvement over Min-k% alone
**Condition**: Membership inference on WikiMIA dataset across 7 language models; note LLaMA-2-7B shows degradation from 69.7% to 58.3%

**Evidence**: "Our adversarial methods PPL + Adv. and Min-k% + Adv., consistently outperform their counterparts PPL and Min-k%."
