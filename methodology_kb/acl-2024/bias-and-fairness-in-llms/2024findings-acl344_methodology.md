# Asymmetric Bias in Text-to-Image Generation with Adversarial Attacks

**Source**: https://aclanthology.org/2024.findings-acl.344/

## [POSITIVE] Multiple Token Perturbation
A gradient-based adversarial suffix search algorithm that replaces multiple tokens simultaneously at each optimization step, starting with all tokens replaced and gradually decreasing the replacement rate to 25%, inspired by exploration-exploitation strategy in RL.

**Delta**: +2.0% ASR (26.4% vs 24.4%)
**Condition**: Entity-swapping attacks on Stable Diffusion using CLIP text encoder; CLIP behaves like a bag-of-words model with larger vocabulary than LLMs

**Evidence**: "Using the same hyperparameters and compute budget, our Multiple Token Perturbation algorithm outperforms the Single Token Perturbation (ASR 26.4% vs. 24.4% for 1000 attacks)."

## [POSITIVE] Single Token Perturbation
A modification of the Greedy Coordinate Gradient (GCG) algorithm that selects top-k candidate tokens per position and creates a batch by randomly replacing one token at a time.

**Delta**: 24.4% ASR baseline
**Condition**: Entity-swapping attacks on Stable Diffusion; less effective than Multiple Token Perturbation due to CLIP's bag-of-words nature and larger vocabulary

**Evidence**: "Using the same hyperparameters and compute budget, our Multiple Token Perturbation algorithm outperforms the Single Token Perturbation (ASR 26.4% vs. 24.4% for 1000 attacks)."

## [NEGATIVE] Token Restrictions
Limiting adversarial suffix token search to a specific set by setting gradients of excluded tokens to infinity before the Top-k operation, enabling emulation of restricted attacks or exclusion of target synonyms.

**Delta**: Fails targeted attacks; only removes concepts
**Condition**: When restricted to ASCII tokens for targeted entity-swapping attacks

**Evidence**: "We find that such adversarial suffixes can remove concepts... but fail to perform targeted attacks (e.g. changing 'a bee sitting on a flower.' to 'a bee sitting on a leaf.'). We suspect that this is mainly because ASCII tokens can perturb CLIP's embedding but are unable to add additional information to it."

## [NEUTRAL] Blocking Target Token Selection
Preventing the exact target word token from being selected in the adversarial suffix to generate more covert attacks.

**Delta**: No measurable drop in ASR when preconditions are met
**Condition**: Algorithm finds synonyms or subword tokenizations of the target word as substitutes

**Evidence**: "We find that the effectiveness of the algorithm isn't affected when the exact target token is restricted and it still finds successful adversarial suffixes using synonyms (when preconditions are met)."

## [POSITIVE] Baseline Distance Difference (Δ2) Probe Metric
A metric measuring the difference in CLIP embedding distance from a background context (PAD token baseline) between the target text and the input text, capturing the T2I model's inherent bias toward certain entities in a given context.

**Delta**: Mean ASR 0.40 when Δ2 negative vs. 0.12 when Δ2 positive; Pearson r = -0.39, Spearman ρ = -0.46
**Condition**: HQ-Pairs dataset with Multiple Token Perturbation algorithm on Stable Diffusion

**Evidence**: "Figure 6b shows that the mean ASR is 0.40 when ∆2 is negative, while it drops to just 0.12 when ∆2 is positive. Thus, ∆2 allows us to estimate, to some extent, the probability of a successful adversarial attack."

## [NEUTRAL] Perplexity Difference (Δ1) as ASR Predictor
Using the difference in language model perplexity between input and target prompts (computed via text-davinci-003) as a proxy for how natural or plausible a target prompt is, hypothesized to correlate with attack success rate.

**Delta**: Pearson r = 0.05, Spearman ρ = -0.06
**Condition**: HQ-Pairs dataset; perplexity computed using text-davinci-003

**Evidence**: "On the HQ-Pairs dataset, we find that Perplexity Difference ∆1 has a negligible correlation with ASR (Pearson r = 0.05 and Spearman ρ = −0.06). This is counterintuitive because we expected that a target with lower perplexity compared to the input text would be easier to generate through an adversarial attack."

## [POSITIVE] Base Success Rate (BSR) as ASR Predictor
Measuring the T2I model's ability to generate an image matching the target prompt without any adversarial suffix, used as a proxy for how achievable the target generation is.

**Delta**: Pearson r = 0.28, Spearman ρ = 0.38; 60% ASR when BSR high + Δ2 negative vs. 5% when BSR low + Δ2 positive
**Condition**: HQ-Pairs dataset; BSR ≥ 0.9 defined as high; combined with Δ2 for best predictive power

**Evidence**: "ASR has a weak positive correlation with BSR (Pearson r = 0.28 and Spearman ρ = 0.38)... when BSR (of the target text) is high and ∆2 is negative for a given input-target text pair, adversarial attacks have a 60% chance of success on the HQ-Pairs dataset, compared to only 5% when BSR is low and ∆2 is positive."

## [POSITIVE] Combined BSR + Δ2 Predictor
Using both Base Success Rate of the target text and Baseline Distance Difference together to predict adversarial attack success probability without performing the attack.

**Delta**: 60% ASR (High BSR, Negative Δ2) vs. 5% ASR (Low BSR, Positive Δ2) on HQ-Pairs; 34.9% vs. 8.7% on COCO-Pairs
**Condition**: HQ-Pairs and COCO-Pairs datasets; effect less pronounced on COCO-Pairs due to noisier automatic pair generation

**Evidence**: "when BSR (of the target text) is high and ∆2 is negative for a given input-target text pair, adversarial attacks have a 60% chance of success on the HQ-Pairs dataset, compared to only 5% when BSR is low and ∆2 is positive. Thus, considering both BSR and ∆2 together enhances the prediction accuracy of an attack's success likelihood."

## [POSITIVE] InstructBLIP as Automated Classifier
Using InstructBLIP VLM with a yes/no question prompt to classify whether generated images match input or target captions, replacing human evaluation for large-scale experiments.

**Delta**: Accuracy 0.79 (3-class), 0.86 (2-class); F1 0.75 (3-class), 0.84 (2-class) — best among tested classifiers
**Condition**: Compared against LLaVA-1.5, CLIP, and CLIP-336; evaluated against human labels on 200 random samples

**Evidence**: "Since InstructBLIP shows the best alignment with human evaluation, we use InstructBLIP as our sole classifier in subsequent sections."

## [NEGATIVE] CLIP-based Classifier
Using CLIP similarity scores with an optimized threshold γ to classify generated images as matching input, target, or neither.

**Delta**: Accuracy 0.62 (3-class), 0.70 (2-class); F1 0.55 (3-class), 0.69 (2-class) — worst among tested classifiers
**Condition**: Compared against InstructBLIP and LLaVA-1.5 on 200 human-labeled samples

**Evidence**: "Table 1: Comparison of Automated Evaluation Models... CLIP: 3 classes Accuracy 0.62, F1 0.55; 2 classes Accuracy 0.70, F1 0.69."

## [NEGATIVE] Adversarial Suffix Non-Transferability across T2I Models
Adversarial suffixes generated for one Stable Diffusion variant do not transfer to other variants or architectures, indicating model-specific optimization.

**Delta**: Zero transfer between SD 1.4 and SD 2.1; zero transfer to DALL-E 3
**Condition**: Cross-model transfer between SD 1.4 (CLIP ViT-L/14) and SD 2.1 (OpenCLIP-ViT/H), and to DALL-E 3

**Evidence**: "However, the adversarial suffixes generated using SD 2.1-base did not work on SD 1.4 and vice versa... the lack of transferability indicates that training data likely plays the main role in determining adversarial attack success."

## [NEGATIVE] Color Adjective Swapping
Attempting entity-swapping attacks targeting color adjectives (e.g., red to blue) in prompts.

**Delta**: 0% ASR in all instances tested
**Condition**: Color adjective swaps; other adjective types (e.g., size, state) can have high ASR in at least one direction

**Evidence**: "We observed that adversarial attacks targeting certain adjectives, such as color, had a very low ASR. For example, swapping out 'red' with 'blue' in the prompt 'a red car on a city road.' failed in all instances."

## [POSITIVE] Asymmetric Entity-Swap Attack Objective
A novel attack setup where adversarial suffixes are appended to swap one entity in a prompt with another targeted entity, enabling study of directional asymmetry in attack success rates.

**Delta**: ASR ranges from 0% to 90% depending on swap direction; e.g., turtle→fish: 1.5% ASR vs. fish→turtle: 90% ASR
**Condition**: Stable Diffusion 2.1 with Multiple Token Perturbation; asymmetry driven by model's internal CLIP embedding bias

**Evidence**: "One of our key findings is the strong asymmetry of adversarial attack success rate... attacks from 'A swan swimming in a lake.' to 'A horse swimming in a lake.' failed in all ten attempts, whereas the reverse direction achieved an ASR of 0.9."
