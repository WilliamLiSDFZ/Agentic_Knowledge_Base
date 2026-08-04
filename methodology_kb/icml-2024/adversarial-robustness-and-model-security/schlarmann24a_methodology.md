# Robust CLIP: Unsupervised Adversarial Fine-Tuning of Vision Embeddings for Robust Large Vision-Language Models

**Source**: https://proceedings.mlr.press/v235/schlarmann24a.html

## [POSITIVE] FARE (Fine-tuning for Adversarially Robust Embeddings)
Unsupervised adversarial fine-tuning of CLIP vision encoder that minimizes L2 distance between embeddings of perturbed images and original clean embeddings from the frozen original CLIP model, without using labels or the text encoder

**Delta**: outperforms baseline
**Condition**: Applied to CLIP ViT-L/14 vision encoder used in LVLMs (LLaVA, OpenFlamingo) and zero-shot classification

**Evidence**: "Among the robust models, the FARE models overall maintain the best clean performance and attain the best robustness. For LLaVA we observe that FARE4 outperforms TeCoA2 and TeCoA4 on all datasets in clean and most datasets in robust performance, which shows that our unsupervised fine-tuning scheme is superior."

## [NEGATIVE] TeCoA (Supervised Adversarial Fine-Tuning of CLIP)
Supervised adversarial fine-tuning of CLIP vision encoder using ImageNet labels and cross-entropy loss with text-guided contrastive adversarial training

**Delta**: significant degradation on non-ImageNet zero-shot tasks
**Condition**: Applied to zero-shot classification on datasets other than ImageNet and when used inside LVLMs

**Evidence**: "the resulting fine-tuned CLIP model shows significant degradation of zero-shot classification accuracy on datasets different from ImageNet, and on integration into LVLMs is detrimental to their performance."

## [POSITIVE] Unsupervised training objective (no labels)
FARE uses no class labels during fine-tuning, only image data, making it dataset-agnostic and avoiding bias toward specific class embeddings

**Delta**: outperforms supervised TeCoA on downstream tasks
**Condition**: Zero-shot classification on non-ImageNet datasets and LVLM downstream tasks

**Evidence**: "our approach solves both problems at the same time, so that we can get the benefits of our robust CLIP model and maintain good clean performance on all down-stream tasks without the need of fine-tuning or retraining."

## [POSITIVE] Smaller perturbation radius training (ε=2/255)
Training FARE or TeCoA at smaller ℓ∞ radius of 2/255 instead of 4/255 to trade robustness for better clean performance

**Delta**: FARE2 maintains clean performance close to original CLIP
**Condition**: When clean performance preservation is prioritized; models trained at ε=2/255 break in few cases (3.3% TeCoA2, 2.0% FARE2) at ε=4/255 targeted attacks

**Evidence**: "We observe that the smaller radius is sufficient to get non-trivial robustness even when testing at 4/255 while maintaining a clean performance close to the original CLIP model."

## [POSITIVE] Larger perturbation radius training (ε=4/255)
Training FARE or TeCoA at larger ℓ∞ radius of 4/255 to achieve full robustness against targeted imperceptible attacks

**Delta**: 0% targeted attack success rate at both ε=2/255 and ε=4/255
**Condition**: Stealthy targeted attacks on LVLMs; required for full robustness at ε=4/255

**Evidence**: "only the models trained for ε=4/255 are fully robust against targeted imperceptible attacks on LVLMs, see Table 3 and Fig. 3. TeCoA4 and FARE4 are completely robust against the attacks."

## [POSITIVE] Preserving original CLIP embedding (L2 distance loss)
FARE loss enforces that fine-tuned embeddings of perturbed images stay close to original CLIP embeddings of clean images, preserving downstream compatibility without retraining LVLMs

**Delta**: no retraining required; clean performance preserved
**Condition**: Plug-in replacement of CLIP in LVLMs without retraining projection layers or language models

**Evidence**: "as L_FARE goes to zero, the embedding given by the fine-tuned model for clean images is the same as the one by the original model...this implies that the fine-tuned CLIP vision encoder can be plugged into LVLMs without influencing their performance."

## [NEUTRAL] Class-token only in FARE loss
Computing the FARE loss only with respect to the class token rather than all token outputs of the CLIP vision encoder

**Delta**: no improvement from using all tokens
**Condition**: During FARE fine-tuning of ViT-L/14 CLIP encoder

**Evidence**: "early experiments showed that using only the class-token in the fine-tuning loss is sufficient to attain good results with down-stream LVLMs. Taking all tokens into account for training requires more memory and compute, but did not yield improvements."

## [POSITIVE] PGD inner maximization (10 steps)
Using 10 steps of projected gradient descent to approximately solve the inner maximization problem during adversarial fine-tuning

**Delta**: only 0.2% of computational cost of original CLIP training
**Condition**: Adversarial fine-tuning of CLIP on ImageNet for 2 epochs

**Evidence**: "For adversarial training we use 10 steps of PGD for the inner maximization in Eqs. (2, 3). Notably, we only use two epochs of adversarial fine-tuning on ImageNet (FARE uses no labels) which is only about 0.2% of the computational cost of training the original CLIP model."

## [NEGATIVE] Cosine similarity loss in TeCoA (unnormalized embedding distortion)
TeCoA uses cosine similarity which only cares about the projection on the hypersphere, allowing arbitrary changes along the radial direction that distort unnormalized embeddings used by LVLMs

**Delta**: huge performance losses in LVLMs
**Condition**: TeCoA supervised fine-tuning when CLIP is used inside LVLMs that rely on unnormalized embeddings

**Evidence**: "the loss uses the cosine similarity, which effectively means that it only cares about the projection of the embedding on the hypersphere...during finetuning it can happen that the embedding is changed along the radial direction in an arbitrary fashion. As other down-stream tasks of CLIP, e.g. LVLMs, use the unnormalized embedding this can again lead to huge performance losses."

## [NEGATIVE] Supervised fine-tuning on fixed ImageNet class embeddings
TeCoA trains adversarial robustness with respect to fixed text embeddings of ImageNet classes only, ignoring other text embeddings and unseen categories

**Delta**: high losses in standard performance for other downstream zero-shot classification tasks
**Condition**: Zero-shot classification on datasets other than ImageNet

**Evidence**: "adversarial training is done with respect to the fixed set of text embeddings of the classes of ImageNet. This does not take into account the effect on other text embeddings, e.g. of categories which are not part of ImageNet, and thus the fine-tuning can lead to heavy distortions with respect to unseen classes, which explains the high losses in standard performance for other down-stream zero-shot classification tasks."

## [POSITIVE] Robust CLIP as drop-in replacement (no LVLM retraining)
Replacing the original CLIP vision encoder in LVLMs with FARE-CLIP without any retraining or fine-tuning of the downstream LVLM components

**Delta**: robustness transferred to all downstream tasks
**Condition**: LVLMs with frozen CLIP vision encoders (LLaVA, OpenFlamingo)

**Evidence**: "we can readily replace the original CLIP with our robust CLIP in all down-stream tasks without retraining or fine-tuning since the features on clean inputs are (approximately) preserved. (ii) all downstream tasks, e.g. zero-shot classification or zero-shot tasks of LVLMs, become robust to attacks on the vision modality."

## [POSITIVE] FARE reducing hallucinations
Using FARE-CLIP as vision encoder in LLaVA reduces object hallucination compared to TeCoA-CLIP

**Delta**: FARE2 mean POPE F1: 80.8 vs TeCoA2: 75.9; FARE4: 76.3 vs TeCoA4: 72.2
**Condition**: POPE hallucination benchmark with LLaVA-1.5 7B

**Evidence**: "Supervised fine-tuning via TeCoA causes LLaVA to hallucinate much more than unsupervised fine-tuning with FARE. The clean CLIP model has the best performance on all splits of POPE, while FARE is the closest to it. The TeCoA model attains the worst average F1-score."

## [POSITIVE] FARE on Chain-of-Thought reasoning tasks
Using FARE-CLIP instead of TeCoA-CLIP in LLaVA for science question answering requiring reasoning

**Delta**: +2.3% and +2.4% accuracy over TeCoA2 and TeCoA4 respectively on SQA-I
**Condition**: SQA-I (Science Question Answering) benchmark with LLaVA

**Evidence**: "Both FARE models are better than the respective TeCoA models by 2.4% and additionally FARE2 is only 1% off from the original CLIP model."

## [POSITIVE] Robust CLIP for jailbreak defense
Using adversarially fine-tuned CLIP (TeCoA or FARE) to defend against visual jailbreaking attacks on LVLMs

**Delta**: reduced harmful outputs from 24/40 (CLIP, ε=16/255) to 14-15/40 (TeCoA4/FARE4)
**Condition**: Jailbreaking attacks on LLaVA-1.5 7B at various perturbation strengths (ε=16/255 to 64/255)

**Evidence**: "Robust CLIP models indeed help in defending LLaVA 1.5 against jailbreaking attacks even at attack radii which are much higher than for which they have been trained. TeCoA and FARE similarly reduce the number of harmful outputs significantly compared to the original CLIP vision encoder."

## [POSITIVE] Transfer attack robustness with robust CLIP
Using robust CLIP vision encoders prevents successful transfer of adversarial images crafted against one LVLM to another LVLM

**Delta**: transfer attack CIDEr restored from ~1-8 (successful attack) to ~75-86 (clean-level performance)
**Condition**: Cross-model transfer attacks between OpenFlamingo and LLaVA at ε=4/255

**Evidence**: "Even though OF and LLaVA use different LLMs as backbones and different parts connecting vision and language, the adversarial images transfer surprisingly well across them. However, when using target LVLMs with robust CLIP models, the transfer attack is no longer successful."

## [POSITIVE] Two-stage attack pipeline (half then single precision)
Attack evaluation pipeline using APGD at half precision first to eliminate easy samples, then single precision for remaining samples, with targeted attacks for VQA

**Delta**: stronger and significantly faster than prior attack pipeline
**Condition**: Adversarial evaluation of LVLMs on captioning and VQA tasks

**Evidence**: "we show in App. B.7 that the proposed attack is stronger and significantly faster than the one of Schlarmann & Hein (2023). By first eliminating easy-to-break samples, the proposed pipeline ensures that the expensive attack is applied only when necessary, thereby saving runtime."

## [POSITIVE] APGD with 10,000 iterations for targeted attacks
Using a very high number of iterations (10,000) for APGD when evaluating stealthy targeted attacks to ensure attack strength

**Delta**: much more successful attack than with only 500 iterations
**Condition**: Evaluating stealthy targeted attacks on LLaVA-1.5 7B

**Evidence**: "The success rate of the attack is dependent on a high amount of iterations, in fact when using only 500 iterations, the attack is much less successful as shown in App. B.9. To determine actual robustness it is thus critical to use a strong attack."
