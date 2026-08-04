# Image Hijacks: Adversarial Images can Control Generative Models at Runtime

**Source**: https://proceedings.mlr.press/v235/bailey24a.html

## [POSITIVE] Behaviour Matching Algorithm
A general framework using projected gradient descent to optimize an adversarial image so that the VLM output matches a target behaviour (defined as a function from contexts to logits) across a dataset of input contexts.

**Delta**: over 80% success rate across all four attack types
**Condition**: Applied to LLaVA LLaMA-2-13B-Chat under various perturbation constraints

**Evidence**: "We use Behaviour Matching to craft hijacks for four types of attack: forcing VLMs to generate outputs of the adversary's choice, leak information from their context window, override their safety training, and believe false statements... all attack types achieve a success rate of over 80%."

## [POSITIVE] Prompt Matching
An extension of Behaviour Matching that trains images to mimic the behaviour induced by an arbitrary text prompt, using soft logit outputs from the VLM's forward pass on prompt-prepended contexts, with a generic unrelated dataset.

**Delta**: 85% success rate (unconstrained) vs 0% baseline
**Condition**: Disinformation attack on LLaVA LLaMA-2-13B-Chat, unconstrained setting

**Evidence**: "our least constrained images substantially improve on the untrained baseline, increasing the success rate from 0% to 85%."

## [POSITIVE] Soft Logit Targets (vs Hard Text Targets)
Using the full per-token logit distributions from the teacher VLM as training targets rather than decoded text strings, providing richer training signal.

**Delta**: enables prompt matching; hard targets provide insufficient signal for many prompts
**Condition**: Prompt Matching / disinformation attack training

**Evidence**: "Such a dataset would provide insufficient information to learn a prompt-matching image, as for many input prompts (e.g. 'What is the capital of the United States?'), our choice of p would not meaningfully affect Mϕ's (textual) output. This observation is corroborated by prior work in knowledge distillation (Hinton et al., 2015), which found that soft targets can often provide 'much more information per training case' than hard targets."

## [POSITIVE] Large Diverse Context Set for Training (Alpaca Dataset)
Training the adversarial image over a large set of diverse input contexts (52,000 instruction-output pairs from the Alpaca dataset) to achieve context transferability.

**Delta**: 100% context transfer rate for specific string attack at ε=32/255
**Condition**: Specific string, leak context, and jailbreak attacks on LLaVA

**Evidence**: "By choosing a large enough set C – e.g. a common instruction-tuning dataset – we obtain hijacks x̂ that transfer across different contexts (i.e. the hijack matches the target behaviour even on held-out user inputs)... our specific string attack with ε = 32/255 achieves a 100% context transfer rate."

## [NEGATIVE] ℓ∞-Norm Perturbation Constraint
Constraining the adversarial image perturbation to be within an ℓ∞ ball of radius ε around an initial image, making the hijack visually similar to a benign image.

**Delta**: 0% success rate at ε=1/255 and ε=2/255 for specific string; degrades gracefully at higher ε
**Condition**: Specific string attack; tighter constraints reduce success rate

**Evidence**: "while we fail to learn a working image hijack for the tightest ℓ∞-norm constraints, all hijacks with ε ≥ 4/255 are reasonably successful."

## [POSITIVE] Stationary Patch Constraint
Restricting the adversarial perturbation to a fixed square patch of learnable pixels superimposed at a fixed location on the image.

**Delta**: 95% success rate with 60×60 pixel patch (7% of pixels) for specific string attack
**Condition**: Specific string attack on LLaVA

**Evidence**: "For the stationary patch constraint, we obtain a 95% success rate with a 60×60-pixel patch (i.e. 7% of all pixels in the image)."

## [POSITIVE] Moving Patch Constraint
Training adversarial patches with patch location sampled uniformly at random during training and evaluation, forcing the attack to rely on location-invariant high-level features.

**Delta**: 98% success rate with 160×160 pixel patch; robust to additive noise and JPEG compression
**Condition**: Specific string attack; requires larger patch than stationary but gains robustness to defenses

**Evidence**: "It is harder to learn this hijack under the moving patch constraint, needing a 160×160-pixel patch (i.e. 51% of all pixels in the image) to obtain a 98% success rate... moving patch attacks are robust to high levels of additive noise... moving patch hijacks are robust to high degrees of compression."

## [POSITIVE] Emergence of Interpretable High-Level Features in Moving Patches
Moving patch training causes interpretable visual features (text, objects) to emerge in the learned patch, hypothesized to be due to inability to overfit to specific model circuits.

**Delta**: contributes to robustness against additive noise and JPEG compression defenses
**Condition**: Moving patch attacks for specific string task

**Evidence**: "we find interpretable high level features emerge in the learnt perturbations of moving patches. In many of the images we see words from our intended string output in the learnt patch... We hypothesise that such high level features emerge as we cannot overfit to specific circuits in the model when training a moving patch, and instead must rely on high level features that the model interprets the same irrespective of their location."

## [NEUTRAL] Ensembled Behaviour Matching
Training a single adversarial image by summing Behaviour Matching losses across multiple white-box models simultaneously, to improve transferability to held-out black-box models.

**Delta**: 99.8% on LLaVA, 80.6% on InstructBLIP, 0% on held-out BLIP-2; validation loss on BLIP-2 decreases from ~5 to [3,4]
**Condition**: Model transferability experiment: LLaVA-13B + InstructBLIP-Vicuna-7B → BLIP-2 Flan-T5-XL

**Evidence**: "we can train a single image hijack on two models that achieves high success rate on both... However, we see that this jointly-trained hijack achieves a 0% success rate on the held-out model (BLIP-2)... Our jointly-trained hijack does yield a lower validation loss on the target transfer model throughout training."

## [NEGATIVE] Single-Model Transfer (No Ensemble)
Directly transferring an adversarial image trained on one white-box model to a different black-box model without ensembling.

**Delta**: 0% success rate in both transfer directions
**Condition**: LLaVA-13B → BLIP-2 and BLIP-2 → LLaVA-13B transfer for specific string attack

**Evidence**: "we observe a 0% success rate of attacks when transferring to a new model."

## [NEGATIVE] GCG Text Baseline (Greedy Coordinate Gradient)
State-of-the-art text-based adversarial attack that learns adversarial tokens appended to user inputs, used as a comparison baseline against image hijacks.

**Delta**: 13.5% specific string, 0% leak context, 82% jailbreak vs image attack rates of 100%, 96%, 92% at ε=8/255
**Condition**: Compared against image hijacks on LLaVA for specific string, leak context, and jailbreak attacks

**Evidence**: "We see that the text baseline underperforms the image attack for ℓ∞ constraints of 8/255 and above across all three attack types... our results suggest that image-based attacks currently present a stronger attack vector in multimodal foundation models."

## [POSITIVE] Proxy Jailbreak Behaviour (Affirmative Label Matching)
Training jailbreak hijacks by matching a proxy behaviour that replies affirmatively to harmful requests (e.g., 'Sure, here is how to...'), rather than matching a base model, since the adversary may not have base model access.

**Delta**: jailbreak success rate increased substantially from 4% baseline; unconstrained achieves 64%
**Condition**: Jailbreak attack on LLaVA LLaMA-2-13B-Chat

**Evidence**: "Our hijacks are able to substantially increase the jailbreak success rate from its baseline value... we train jailbreaks by instead matching a proxy behaviour B'jail. This behaviour, defined over contexts Cjail = {requests for harmful content}, simply replies in the affirmative to such requests."

## [NEGATIVE] Overfitting at Large ℓ∞ Budgets for Jailbreak
At large perturbation budgets, jailbreak hijacks overfit to producing only the affirmative training label without actually fulfilling the harmful request, reducing measured success rate.

**Delta**: performance drops for large values of ε in jailbreak attack
**Condition**: Jailbreak attack at high ℓ∞ perturbation budgets

**Evidence**: "We note that performance drops for large values of ε: observing the failure cases, we hypothesise that this is due to the model overfitting to the proxy task of matching the training label exactly without actually answering the user's query."

## [NEGATIVE] Additive Noise Defense
A defense that adds uniform random noise to the input image at inference time to disrupt adversarial perturbations.

**Delta**: moving patch attacks remain robust at high noise levels; ℓ∞ attacks with higher budgets are more robust
**Condition**: Applied as defense against specific string image hijacks on LLaVA

**Evidence**: "moving patch attacks are robust to high levels of additive noise... higher ℓ∞ constraints are more robust."

## [NEGATIVE] JPEG Compression Defense
A defense that applies JPEG compression to the input image at inference time to remove high-frequency adversarial perturbations.

**Delta**: moving patch hijacks are robust to high degrees of compression
**Condition**: Applied as defense against specific string image hijacks on LLaVA

**Evidence**: "moving patch hijacks are robust to high degrees of compression. Overall, for moving patch attacks, we see a concerningly high robustness to both defense mechanisms."

## [NEGATIVE] Intensional Embedding Matching (Modality Gap Approach)
Attempting to craft prompt-matching images by pushing image embeddings close to the target text prompt's embedding in the shared CLIP embedding space.

**Delta**: unable to meaningfully affect model behaviour
**Condition**: Attempted for prompt/disinformation attacks; abandoned in favor of extensional Prompt Matching

**Evidence**: "Bagdasaryan et al. (2023) tried to train such images, however, they found that the modality gap (Liang et al., 2022) prevented them from pushing the images' embeddings close enough to the target prompt's embedding to meaningfully affect model behaviour (a result we confirmed via informal experimentation)."

## [NEUTRAL] Image Quantization Post-Optimization
After gradient-based optimization, mapping continuous pixel values in [0,1] to integer values in [0,255] to produce a valid image.

**Delta**: not quantified separately
**Condition**: Applied to all image hijacks after training

**Evidence**: "After optimisation, we quantise our image hijack by mapping its pixel values x̂_cij ∈ [0,1] to integer values in [0,255]."

## [POSITIVE] Validation-Based Checkpoint Selection
Selecting the model checkpoint with the highest validation success rate (on 100 held-out instructions) rather than the final checkpoint, to avoid overfitting.

**Delta**: not quantified separately
**Condition**: All Behaviour Matching attack experiments

**Evidence**: "We trained for a maximum of 12 hours on an NVIDIA A100-SXM4-80GB GPU, identified the checkpoint with the highest validation success rate, and reported the test set results using this checkpoint."

## [NEUTRAL] Exact String Match Success Criterion for Specific String Attack
Defining attack success as exact match of model output to target string (ignoring leading/trailing whitespace), motivated by the need for correct URLs and non-suspicious output.

**Delta**: GCG text baseline achieves 11.82 average Levenshtein distance, most responses include target string but with extra tokens
**Condition**: Evaluation metric for specific string attack

**Evidence**: "As partially correct output strings might render this attack ineffective (e.g. if the URL is garbled, or if the output arouses suspicion in the user), we consider an attack successful if the model output (ignoring leading and trailing whitespace) exactly matches the target string."

## [POSITIVE] Combining Alpaca Dataset with 'Repeat Previous Sentence' Prompts for Disinformation Training
Augmenting the 52,000 Alpaca prompts with 3,000 copies of 10 variations on 'Repeat your previous sentence' to strengthen the training signal for the disinformation attack.

**Delta**: 85% success rate achieved for unconstrained disinformation attack
**Condition**: Disinformation / Prompt Matching attack training

**Evidence**: "For our training context set C, we used a combination of 52,000 prompts from the Alpaca training set (Taori et al., 2023), and 3,000 copies of 10 variations on 'Repeat your previous sentence' (82,000 prompts in total)."
