# Prompting4Debugging: Red-Teaming Text-to-Image Diffusion Models by Finding Problematic Prompts

**Source**: https://proceedings.mlr.press/v235/chin24a.html

## [POSITIVE] P4D Framework (Prompting4Debugging)
An automated red-teaming tool that uses prompt engineering to find problematic prompts that bypass safety mechanisms in text-to-image diffusion models by optimizing prompts in latent space using an unconstrained T2I model as reference.

**Delta**: up to 66.58% failure rate (P4D-UNION on ESD nudity)
**Condition**: Red-teaming ESD, SLD-MAX, SLD-STRONG, SD-NEGP across nudity, car, French-horn categories

**Evidence**: "our result shows that around half of prompts in existing safe prompting benchmarks which were originally considered 'safe' can actually be manipulated to bypass many deployed safety mechanisms"

## [POSITIVE] P4D-N (N-token initialization from scratch)
Variant of P4D that initializes N tokens in the continuous prompt embedding from scratch via randomly drawing N vocabulary embeddings, independent of original prompt length.

**Delta**: 50.65% FR on ESD nudity, 25.67% on SLD-MAX, 34.03% on SLD-STRONG, 25.44% on SD-NEGP
**Condition**: Concept-related and object-related red-teaming; default N=16

**Evidence**: "P4D-N and P4D-K demonstrate promising and comparable results across a range of safe T2I models and categories"

## [POSITIVE] P4D-K (interleaved learnable token insertion)
Variant of P4D that inserts learnable tokens after every K tokens of the original prompt embedding, making prompt length vary with original prompt length and preserving interpretability.

**Delta**: 47.19% FR on ESD nudity, 38.69% on SLD-MAX, 37.84% on SLD-STRONG, 20.36% on SD-NEGP
**Condition**: Concept-related and object-related red-teaming; default K=3

**Evidence**: "P4D-K preserves its prompt interpretability without compromising the debugging performance"

## [POSITIVE] P4D-UNION (combining P4D-N and P4D-K results)
Unifying problematic prompts found by both P4D-N and P4D-K to leverage diversity between the two variants.

**Delta**: 66.58% FR on ESD nudity, 52.66% on SLD-MAX, 55.29% on SLD-STRONG, 40.98% on SD-NEGP
**Condition**: All evaluated safe T2I models and categories

**Evidence**: "we unify problematic prompts from P4D-N and P4D-K and obtain P4D-UNION, which significantly increases the failure rate across various safe T2I models and categories, indicating that problematic prompts found by P4D-N and P4D-K are diverse"

## [POSITIVE] Dual-model information integration (standard + safe T2I)
Using information from both the unconstrained standard T2I model and the safe T2I model during prompt optimization, rather than relying on only one model.

**Delta**: outperforms Text-Inv and PEZ-Orig (which use only standard T2I info) and PEZ-PInv (which uses only safe T2I info)
**Condition**: Nudity category comparison against Text-Inv, PEZ-Orig, PEZ-PInv baselines

**Evidence**: "the superior performance of our P4D indicates that the integration of the information from both standard T2I and safe T2I models enhances the efficacy of problematic prompt identification"

## [POSITIVE] Deactivating text filter during optimization (information obfuscation mitigation)
Turning off the safety text filter of guidance-based models (SLD, SD-NEGP) during the P4D prompt optimization phase while keeping it active during inference, to expand the explorable textual embedding space.

**Delta**: SLD-MAX: 25.67%→40.98% (P4D-N), 38.69%→39.11% (P4D-K); SLD-STRONG: 34.03%→50.25% (P4D-N), 37.84%→42.79% (P4D-K); SD-NEGP: 25.44%→27.93% (P4D-N), 20.36%→32.46% (P4D-K)
**Condition**: Guidance-based safe T2I models: SLD-MAX, SLD-STRONG, SD-NEGP

**Evidence**: "when the safety filter is disabled during the debugging process, P4D becomes capable of identifying more problematic prompts. We hypothesize that the text filter actually obscures the search for optimized textual prompts (i.e. constraining the explorable textual embedding space)"

## [NEGATIVE] Safety text filter (information obfuscation effect)
The safety text filter in guidance-based models constrains the textual embedding space during optimization, causing P4D to find fewer problematic prompts and creating a false sense of security.

**Delta**: SLD-MAX P4D-N drops from 40.98% to 25.67% when filter is active during optimization
**Condition**: Guidance-based safe T2I models (SLD, SD-NEGP) during red-teaming optimization

**Evidence**: "the text filter induces a false sense of safety through 'information obfuscation', as evidenced by the fact that removing this filter allows P4D to find more problematic prompts"

## [POSITIVE] Soft Prompting baseline (continuous embedding without projection)
Directly optimizing continuous soft embeddings without projecting to discrete hard tokens, used as a baseline comparison.

**Delta**: Soft Prompting-K achieves 27.74% FR on ESD nudity, outperforming Random baselines but below P4D
**Condition**: Baseline comparison across nudity and object categories

**Evidence**: "Soft Prompting-N and Soft Prompting-K are analogous to P4D-N and P4D-K respectively [used as baselines showing partial effectiveness]"

## [POSITIVE] Hard prompt projection via nearest vocabulary embedding (PEZ-style)
Projecting continuous soft prompt embeddings to discrete hard token embeddings via nearest-neighbor lookup in vocabulary space, enabling interpretable and transferable prompts.

**Delta**: P4D outperforms Soft Prompting baselines; P4D-K shows better interpretability than P4D-N
**Condition**: All P4D variants; transferability experiments

**Evidence**: "our P4D adopts the similar design of prompt engineering as PEZ to automate the optimization (a benefit of soft prompt) while making the resultant prompt more transferable (a benefit of hard prompt)"

## [POSITIVE] Prompt length variation and union aggregation
Testing multiple prompt lengths (N=8,16,32 for P4D-N; K=1,3,5 for P4D-K) and aggregating results across lengths to improve coverage.

**Delta**: Union of N=8,16,32 achieves 77.91% FR on ESD vs. best single 59.00%; Union of K=1,3,5 achieves 73.32% vs. best single 52.63%
**Condition**: Ablation study on prompt length for nudity category

**Evidence**: "there is no optimal prompt length in either P4D-N or P4D-K. We argue that a complex scenario requires a longer prompt for description, whereas simpler scenarios can be adequately described with shorter prompts. Hence, we recommend aggregating/unioning the problematic prompts found by using various settings of length"

## [POSITIVE] Shuffling baseline
Randomly permuting the words in the original prompt as a simple red-teaming baseline, inspired by findings that word order shuffling can elicit inappropriate responses from ChatGPT.

**Delta**: 10.55%–33.33% FR across models, outperforming Random-N but below P4D
**Condition**: Baseline comparison across nudity and object categories

**Evidence**: "as some natural language researches have discovered that shuffling the word order in a sentence can make ChatGPT generate inappropriate responses, we introduce a similar approach to build Shuffling baseline"

## [NEGATIVE] ESD finetuning-based concept removal
Fine-tuning partial model weights (U-Net) to remove unwanted concepts from image output, as a safety mechanism.

**Delta**: P4D achieves highest FR against ESD (50.65% P4D-N, 66.58% P4D-UNION) compared to guidance-based models
**Condition**: ESD as target safe T2I model under P4D red-teaming

**Evidence**: "the finetuning-based concept-removal safety mechanism of ESD may only learn to disassociate certain concept-related words with the unsafe image content, but it may not be resistant to optimized prompts"

## [POSITIVE] Straightforward defense via concatenating problematic prompts to negative prompt
A simple defense strategy that concatenates previously identified problematic prompts with the pre-defined negative prompt to strengthen SD-NEGP's safety mechanism.

**Delta**: P4D-N w/o TF: 27.93%→25.36%; P4D-K w/o TF: 32.46%→23.44%; P4D-K w/ TF: 20.36%→10.05%
**Condition**: SD-NEGP defense experiment; omitting adversarial training

**Evidence**: "Implementing this preliminary defense mechanism has resulted in a noticeable reduction in the model's failure rate when facing our P4D attacks"

## [POSITIVE] Universal problematic prompt transferability to closed-source models
Transferring universal nudity prompts found by P4D-K (that jailbreak all 4 open-source safe T2I models) to closed-source models DALL-E 3, SDXL, and Midjourney.

**Delta**: SDXL: 56.14% FR, Midjourney: 30.70% FR, DALL-E 3: 8.77% FR
**Condition**: Transfer to closed-source T2I models; DALL-E 3 shows more robust safety

**Evidence**: "Our findings in Table 5 reveal a notable transferability of these prompts to both SDXL and Midjourney, achieving a high failure rate even though Midjourney is not a member of the Stable Diffusion model family"

## [POSITIVE] Prompt generalizability (universal prompts across multiple safe T2I models)
Accumulating non-repeated problematic prompts found across all safe T2I models and evaluating their cross-model generalizability.

**Delta**: 37.28% (P4D-N) and 31.93% (P4D-K) of prompts jailbreak all four safe T2I models simultaneously
**Condition**: Cross-model generalizability evaluation on nudity category

**Evidence**: "over 50% prompts found by P4D are able to red-team multiple safe T2I models at the same time. Moreover...over 30% problematic prompts found in both P4D-N and P4D-K are robust and general enough to red-team across all safe T2I models simultaneously"

## [POSITIVE] ESD prompt transferability advantage
Problematic prompts found by targeting ESD exhibit superior transferability to other safe T2I models compared to prompts found targeting other models.

**Delta**: Over 60% of ESD-found prompts successfully jailbreak other safe T2I models (P4D-N); ESD-found prompts show highest transferability in P4D-K as well
**Condition**: Prompt transferability experiments across ESD, SLD-MAX, SLD-STRONG, SD-NEGP

**Evidence**: "prompts found in the ESD exhibit superior transferability, with over 60% of such prompts successfully jailbreaking other safe T2I models"

## [NEUTRAL] AdamW optimizer with weight decay for prompt optimization
Using AdamW optimizer with learning rate 0.1, weight decay 0.1, batch size 1, for 3000 gradient update steps to optimize continuous prompt embeddings.

**Delta**: Not separately ablated
**Condition**: All P4D optimization experiments

**Evidence**: "We set the batch size to 1, learning rate to 0.1, weight decay to 0.1, and use AdamW as the optimizer. All the prompts P*_cont are optimized with 3000 gradient update steps."

## [NEUTRAL] Cosine similarity-based optimal prompt selection
Measuring optimized prompts every 50 steps and selecting the best prompt based on cosine similarity between generated image x* and original image x.

**Delta**: Not separately ablated
**Condition**: All P4D optimization experiments

**Evidence**: "We measure optimized prompts every 50 steps and update the optimal prompts based on cosine similarity between the generated x* and original x images."
