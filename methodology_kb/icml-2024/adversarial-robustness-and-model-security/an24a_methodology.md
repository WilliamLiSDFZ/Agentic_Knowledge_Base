# WAVES: Benchmarking the Robustness of Image Watermarks

**Source**: https://proceedings.mlr.press/v235/an24a.html

## [POSITIVE] TPR@0.1% FPR Evaluation Metric
Using True Positive Rate at a stringent 0.1% False Positive Rate threshold as the primary performance metric for watermark detection, instead of AUROC or p-values

**Delta**: more stringent than prior work (TPR@1%FPR)
**Condition**: AI detection / binary classification watermark evaluation

**Evidence**: "rather than AUROC (since a high AUROC score does not necessarily imply a high true positive rate (TPR) at low FPR levels), WAVES focuses on TPR@x%FPR, specifically at a challenging low FPR threshold of 0.1%, extending recent studies such as (Wen et al., 2023) with a larger dataset and a more stringent FPR criterion."

## [POSITIVE] Performance vs. Quality 2D Plots
Novel evaluation framework that jointly plots watermark detection performance against image quality degradation across varying attack strengths, rather than reporting performance alone

**Delta**: enables comprehensive comparison not possible with prior single-metric evaluations
**Condition**: benchmarking watermarks and attacks across all methods

**Evidence**: "We introduce Performance vs. Quality 2D plots for a comprehensive comparison, a novel perspective over the typical performance-centric analyses."

## [POSITIVE] Normalized and Aggregated Quality Metric
Normalizing 8 diverse image quality metrics using quantile-based scaling (10th percentile = 0.1, 90th percentile = 0.9) and aggregating them into a single unified quality degradation score

**Delta**: unifies 8 metrics into one comparable score across attacks and watermarks
**Condition**: comparing attacks and watermarks across heterogeneous quality metrics

**Evidence**: "WAVES proposes a normalized and aggregated quality metric for a unified measure of image quality degradation and comprehensive scoring of attack or watermark methods. We define the normalized scale for each metric by assigning the 10% quantile value over all attacked images as the 0.1 point, and the 90% quantile as the 0.9 point."

## [POSITIVE] Rinsing Regeneration Attack (Multi-Diffusion)
Novel attack applying multiple cycles of noising and denoising through a pre-trained diffusion model (2x or 4x repetitions) to remove watermarks

**Delta**: significantly lowers TPR@0.1%FPR at cost of decreased image quality; 2xDiff strikes balance between low TPR and high quality
**Condition**: attacking Tree-Ring and Stable Signature watermarks

**Evidence**: "Rinsing regenerations significantly lower the TPR@0.1%FPR at the cost of markedly decreased image quality. A 2x rinsing regeneration (Regen-2xDiff) strikes a balance between both low-TPR@0.1%FPR and high image quality."

## [POSITIVE] Single Diffusion Regeneration Attack
Passing a watermarked image through a single cycle of noising and denoising via a pre-trained diffusion model to remove the watermark

**Delta**: Avg P of 0.612 for Tree-Ring, 0.001 for Stable Signature (ranked #1 against Stable Signature)
**Condition**: attacking Tree-Ring and Stable Signature; mild effect on StegaStamp

**Evidence**: "a single regeneration such as Regen-Diff and Regen-VAE can significantly harm the TPR@0.1%FPR while maintaining reasonable CLIP-FID."

## [POSITIVE] Grey-box Adversarial Embedding Attack (AdvEmbG-KLVAE8)
Adversarial perturbation crafted using PGD to maximize divergence in the latent embedding space of the same KL-VAE (f8) used by the victim watermarking model

**Delta**: TPR@0.1%FPR drops to nearly zero for Tree-Ring; ranked #3 overall against Tree-Ring
**Condition**: attacking Tree-Ring watermark when adversary has access to the same VAE

**Evidence**: "Tree-Ring is vulnerable to embedding attacks, particularly under the grey-box condition where TPR@0.1%FPR can drop to nearly zero, effectively removing most watermarks."

## [POSITIVE] Black-box Adversarial Embedding Attack with CLIP (AdvEmbB-CLIP)
Adversarial perturbation crafted using PGD to diverge image embeddings in CLIP's image encoder space, then transferred to watermark detectors

**Delta**: some success especially on natural images like MS-COCO
**Condition**: attacking Tree-Ring on natural image datasets (MS-COCO); ineffective against Stable Signature and StegaStamp

**Evidence**: "CLIP-based attacks also achieve some success, especially on natural images like MS-COCO, likely due to CLIP being trained on natural images akin to those in MS-COCO, enhancing the transferability."

## [POSITIVE] Black-box Adversarial Embedding Attack with KL-VAE f16 (AdvEmbB-KLVAE16)
Adversarial perturbation using a different-architecture but same-data-trained KL-VAE (f16) as surrogate encoder for black-box transfer attack

**Delta**: highest transferability among black-box VAE variants against Tree-Ring
**Condition**: black-box attack on Tree-Ring; ineffective against Stable Signature and StegaStamp

**Evidence**: "Using similar yet distinct VAEs, attack effectiveness diminishes but still manages to remove some watermarks, with KL-VAE (f16), trained on the same images, demonstrating the highest transferability."

## [POSITIVE] Surrogate Detector Attack with Non-watermarked + Watermarked Images (AdvCls-UnWM&WM)
Training a surrogate ResNet18 detector on both watermarked and non-watermarked images from the victim generative model, then using PGD to craft adversarial examples that fool the surrogate and transfer to the real detector

**Delta**: ranked #1 against Tree-Ring with Avg P of 0.499 and Q@0.7P of 0.102
**Condition**: attacking Tree-Ring; requires access to non-watermarked images from victim model; unrealistic for proprietary models; ineffective against Stable Signature and StegaStamp

**Evidence**: "In AdvCls-UnWM&WM, the adversary accessing non-watermarked images has good transferability and removes watermarks effectively."

## [NEGATIVE] Surrogate Detector Attack with Real + Watermarked Images (AdvCls-Real&WM)
Training a surrogate detector using watermarked images and real (ImageNet) non-watermarked images, then transferring PGD attacks to the real detector

**Delta**: fails entirely against Tree-Ring (Avg P = 1.000); ineffective across all watermarks
**Condition**: attacking any watermark when non-watermarked images come from a different distribution (ImageNet) than generated images

**Evidence**: "AdvCls-Real&WM attack fails entirely, likely due to the surrogate model appearing to differentiate real from generated images, using broader features than the watermark."

## [POSITIVE] Surrogate Detector Attack with Two Users' Watermarked Images (AdvCls-WM1&WM2)
Novel attack training a surrogate classifier to distinguish two users' watermarked images using only watermarked data, then using PGD to cause user misidentification

**Delta**: ranked #1 against Tree-Ring (tied) with Avg P of 0.492 and Q@0.7P of 0.101
**Condition**: attacking Tree-Ring for user identification; requires only watermarked images from two users; ineffective against Stable Signature and StegaStamp

**Evidence**: "The newly proposed AdvCls-WM1&WM2 successfully attacks Tree-Ring using only watermarked images. Like the first scenario, the surrogate model fails to precisely locate watermarks but learns the mapping to the latent feature space, allowing a PGD attack to remove the watermark by disturbing the entire latent space."

## [POSITIVE] StegaStamp Distortion Augmentation Training
Training the watermark encoder/decoder with a series of distortions that mimic real-world scenarios as data augmentations

**Delta**: StegaStamp occupies the largest robustness area in radar plots, showing exceptional robustness
**Condition**: robustness to distortion attacks; StegaStamp watermark

**Evidence**: "StegaStamp is trained with a series of distortions that mimic real-world scenarios, significantly enhancing its robustness."

## [POSITIVE] StegaStamp Post-processing Watermarking
Embedding watermarks as a post-processing step using a trained encoder-decoder, independent of the generative model

**Delta**: robust against adversarial embedding and surrogate detector attacks; largest robustness area among three watermarks
**Condition**: resistance to adversarial embedding and surrogate detector attacks

**Evidence**: "Stable Signature and StegaStamp demonstrate robustness against embedding attacks (Figure 7), likely because their detectors are trained independently from generative models, differing significantly from standard classifiers and VAEs."

## [NEGATIVE] StegaStamp Post-processing Artifact Introduction
Post-processing watermark embedding that may introduce human-visible artifacts into images

**Delta**: may introduce artifacts (qualitative degradation)
**Condition**: image quality for StegaStamp watermarked images

**Evidence**: "it's important to recognize the potential trade-off between watermark robustness and quality. As a post-processing method, the original paper finds that StegaStamp may introduce artifacts."

## [NEGATIVE] Tree-Ring VAE-based Watermark Detection
Tree-Ring detection process that first encodes images into latent space via KL-VAE encoder, then performs DDIM inversion to retrieve the watermark from the initial noise vector

**Delta**: TPR@0.1%FPR drops to nearly zero under grey-box embedding attack
**Condition**: vulnerability when adversary can access or approximate the VAE encoder

**Evidence**: "The detection process of Tree-Ring first maps the image to the latent representation through the encoder of KL-VAE (f8), then conducts inverse DDIM to retrieve the watermark. The embedding attack changes the latent representation severely; therefore, watermark retrieval becomes very difficult."

## [NEGATIVE] Stable Signature VAE Decoder Fine-tuning
Embedding watermarks by fine-tuning only the VAE decoder of a latent diffusion model to root the watermark in the decoding process

**Delta**: Avg P of 0.001 against Regen-Diff and Regen-DiffP (ranked #1 most vulnerable to regeneration)
**Condition**: vulnerability to any regeneration attack that uses a different VAE decoder

**Evidence**: "Stable Signature is vulnerable to regeneration attacks due to its unique watermarking protocol... regeneration attacks circumvent this special decoder by using an alternate VAE or diffusion model with a different decoder. As a result, the regenerated images are stripped of the original watermarks."

## [NEGATIVE] Use of Publicly Available VAE in Watermarked Models
Using a publicly available KL-VAE (e.g., as in DALL-E 3) in a watermarked diffusion model system

**Delta**: enables grey-box embedding attack that drops TPR@0.1%FPR to nearly zero
**Condition**: Tree-Ring and Stable Signature watermarks deployed with publicly available VAEs

**Evidence**: "WAVES demonstrates the risks of using publicly available VAEs in watermarked diffusion models. An adversarial embedding attack using the same VAE easily compromises Tree-Ring by altering latent features with little visual change."

## [NEGATIVE] DDIM Inversion for Watermark Retrieval
Using DDIM inversion to reverse the diffusion process and retrieve the initial noise vector containing the watermark

**Delta**: inaccurate even without attack, directly affecting watermark detection accuracy
**Condition**: Tree-Ring watermark detection baseline accuracy

**Evidence**: "Tree-Ring relies on DDIM inversion, which we found is not accurate even without attack, directly affecting the watermark detection accuracy."

## [POSITIVE] Augmentation Training with Blur and Rotation for Stable Signature
Training Stable Signature's extractor with blur and rotation transformations as data augmentations to improve robustness

**Delta**: improves robustness to blur and rotation transformations but marginally reduces encoded image quality
**Condition**: Stable Signature watermark robustness to specific distortions

**Evidence**: "we have observed in internal testing that training Stable Signature's extractor with blur and rotation transformations as data augmentations improves its robustness to these transformations but also marginally reduces the encoded image quality."

## [POSITIVE] Prompted Regeneration Attack (Regen-DiffP)
Regeneration attack that uses user-provided text prompts to guide the diffusion denoising process during watermark removal

**Delta**: Avg P of 0.601 for Tree-Ring, 0.001 for Stable Signature (ranked #1 against Stable Signature)
**Condition**: attacking Tree-Ring and Stable Signature watermarks

**Evidence**: "Furthermore, we introduce two additional variations: prompted regeneration and mixed regeneration (rinse + VAE denoising)... Regen-DiffP are more potent against Stable Signature."

## [POSITIVE] VAE Regeneration Attack (Regen-VAE)
Passing watermarked images through a pre-trained VAE encoder-decoder to alter the image representation and remove watermarks

**Delta**: Avg P of 0.516 for Stable Signature; less effective against Tree-Ring (Avg P 0.832)
**Condition**: more effective against Stable Signature than Tree-Ring; minimal effect on StegaStamp

**Evidence**: "a single regeneration such as Regen-Diff and Regen-VAE can significantly harm the TPR@0.1%FPR while maintaining reasonable CLIP-FID."

## [POSITIVE] KL-VAE Regeneration Attack (Regen-KLVAE)
Using a KL-VAE with varying bottleneck sizes as the regeneration model to remove watermarks

**Delta**: Avg P of 0.217 for Stable Signature (ranked #6); near-ineffective against Tree-Ring (Avg P 0.990)
**Condition**: most effective against Stable Signature; ineffective against Tree-Ring and StegaStamp

**Evidence**: "Regen-KLVAE uses pre-trained KL-VAEs with bottleneck size as strength."

## [POSITIVE] Distortion Combo Attacks
Combining multiple types of distortions (geometric, photometric, degradation) simultaneously as a watermark removal attack

**Delta**: DistCom-Deg achieves Avg P of 0.300 for Stable Signature; generally moderate effectiveness
**Condition**: moderate effectiveness across all watermarks; best against Stable Signature with degradation combo

**Evidence**: "Combination (DistCom-) Combination of a type of distortions -Geo, -Photo, -Deg, -All"

## [POSITIVE] Adversarial Attacks Causing Low Quality Degradation
Adversarial attacks (embedding and surrogate detector) that achieve watermark removal with minimal perceptual image quality degradation

**Delta**: AdvCls-UnWM&WM achieves Avg Q of 0.145 against Tree-Ring (lowest quality degradation among effective attacks)
**Condition**: adversarial attacks against Tree-Ring watermark specifically

**Evidence**: "adversarial attacks generally cause less quality degradation, highlighting their potency against Tree-Ring watermarks."

## [NEGATIVE] ResNet18 Surrogate Detector Architecture
Using ResNet18 as the architecture for training surrogate watermark detectors in adversarial surrogate detector attacks

**Delta**: attacks fail to transfer to Stable Signature and StegaStamp detectors
**Condition**: surrogate detector attacks against Stable Signature and StegaStamp

**Evidence**: "Since the attackers do not know the true detector, the architecture of the surrogate detector (e.g., ResNet18 in this paper) may differ significantly from the true detector... despite achieving high classification accuracy, the surrogate may rely on features different from those of the true detector, leading to unsuccessful transfer of attacks."

## [NEGATIVE] Watermark Spoofing via Surrogate Detector Attack
Attempting to add watermarks to clean images (spoofing) using adversarial perturbations crafted on a surrogate detector

**Delta**: fails to add watermarks to clean images
**Condition**: spoofing attack using AdvCls-UnWM&WM against Tree-Ring

**Evidence**: "it fails to add watermarks to clean images (spoofing attack)... The reason behind this is explored in Appendix G.2, where we find the attacker disrupts the entire latent space, not just the watermark. Conversely, the spoofing attack fails to embed the precise watermark."

## [NEGATIVE] Targeted User Misidentification via AdvCls-WM1&WM2
Using surrogate classifier trained on two users' watermarked images to perform targeted misidentification (making User1's images appear as User2's)

**Delta**: does not consistently achieve targeted misidentification
**Condition**: user identification task with Tree-Ring watermark

**Evidence**: "the attack doesn't consistently mislead the detector into misidentifying User1's watermarked images as User2's (targeted misidentification). Instead, imprecise perturbations often lead to incorrect attribution of User1's images to others."

## [NEGATIVE] Increasing Number of Users in Identification Task
Scaling the user identification scenario from 100 to 1 million users

**Delta**: watermarks become more vulnerable as user numbers increase
**Condition**: user identification task across all watermarking methods

**Evidence**: "watermarks become more vulnerable as user numbers increase, a trend particularly evident in attacks that already strongly affect detection. Since identification demands more accurate decoding, its vulnerability amplifies with user growth."

## [POSITIVE] Error Correction Coding for Watermark Redundancy
Incorporating redundant bits using error correction coding to reconstruct the original message even when parts of the watermark are corrupted

**Delta**: proposed as improvement strategy (not empirically evaluated in paper)
**Condition**: proposed future improvement for watermark robustness

**Evidence**: "Incorporating redundant bits. This technique, known as error correction coding, can help reconstruct the original message even when parts of the watermark are corrupted."

## [POSITIVE] Hybrid Watermark Combination
Combining different watermarking methods to leverage their complementary strengths against a wider range of attacks

**Delta**: proposed as improvement strategy (not empirically evaluated in paper)
**Condition**: proposed future improvement strategy

**Evidence**: "A hybrid approach. Since different watermarks have varied vulnerabilities, one can try to combine different watermarks, leveraging their strengths to defend a wider range of attacks."
