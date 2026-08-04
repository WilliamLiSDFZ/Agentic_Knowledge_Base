# Disguised Copyright Infringement of Latent Diffusion Models

**Source**: https://proceedings.mlr.press/v235/lu24m.html

## [POSITIVE] Feature Matching Attack Adaptation for LDMs
Adapting Shafahi et al. (2018)'s feature matching attack to generate disguised copyrighted images by optimizing a base image so its latent representation (via the LDM encoder E) matches that of a copyrighted image, while remaining visually distinct.

**Delta**: successfully reproduces copyrighted symbols, content, and style via textual inversion
**Condition**: When the LDM encoder is fixed and pre-trained; applicable to symbol, content, and style disguise generation

**Evidence**: "By feeding xd into textual inversion with the text prompt 'a photo of a *', we reproduce the target symbol 'A' without being exposed to the semantic information of the copyrighted content."

## [NEUTRAL] Combined Input Space and Feature Space Loss (α hyperparameter)
A composite loss L = αD1 + D2 balancing input-space distance (visual similarity to base image) and feature-space distance (latent similarity to copyrighted image), controlled by hyperparameter α.

**Delta**: tradeoff: smaller α risks visual leakage of copyrighted content; larger α risks failed concept reproduction
**Condition**: During disguise generation; optimal α is task-dependent (α=8000 for symbol, α=4000 for content, α=2000 for style)

**Evidence**: "a smaller α indicates weaker input space constraint and it could lead to an ineffective disguise, where xd still visually contains the copyrighted material; in contrast, a bigger α shifts the optimization focus away from feature matching to generate latent embeddings distinct from the copyrighted content's."

## [POSITIVE] MS-SSIM + L1 Input Distance Measure
Using a combination of multi-scale structural similarity index (MS-SSIM) loss and L1 loss as the input-space distance measure D1 during disguise generation.

**Delta**: enables effective disguise generation across symbol, content, and style tasks
**Condition**: During disguise generation optimization

**Evidence**: "we apply the pre-trained KL-regularized encoder E, and set the input distance measure D1(·) as a sum of the multi-scale structural similarity index (MS-SSIM) loss and L1 loss following the analysis of (Khare et al. 2021)"

## [POSITIVE] L2 Feature Distance Measure
Using L2 norm as the feature-space distance measure D2 between the encoder outputs of the copyrighted and disguised images.

**Delta**: feature thresholds γ2 ≤ 0.35 sufficient to replicate copyrighted content
**Condition**: During disguise generation and detection

**Evidence**: "the feature distance measure to be the L2 loss: D2(E(xc), E(xd)) = ‖E(xc) − E(xd)‖2"

## [POSITIVE] Blurred Copyrighted Image as Base Image Background
For disguised content generation, using a blurred version of the copyrighted image xc as the background of the base image xb to retain color pattern information.

**Delta**: enables successful content disguise; white background leads to failure
**Condition**: Required specifically for disguised content generation (e.g., The Sunflowers); not needed for simpler symbol disguises

**Evidence**: "we first blur xc such that they lose their semantic information and retain the color pattern, then we add simple sketches of houses as base images xb... In Figure 14 in Appendix A, we show the background is essential for our purpose, where the disguises are ineffective with a white background."

## [POSITIVE] AdaIN-based Style Transfer for Base Image Generation
Using AdaIN-based style transfer to generate base images xb in a different style (watercolor) for style scraping disguises.

**Delta**: successfully reproduces The Starry Night style via textual inversion on disguises
**Condition**: Used for disguised style generation task

**Evidence**: "The base images xb (second row) are the target images with another style (watercolor), generated with AdaIN-based (Huang and Belongie 2017) style transfer."

## [POSITIVE] Textual Inversion for Disguise Revelation
Using textual inversion (Gal et al. 2022) on disguised images xd to qualitatively reveal that the disguises contain copyrighted latent information by generating images that reproduce the copyrighted concept.

**Delta**: successfully reveals copyrighted symbol, content, and style from disguises that are visually distinct from xc
**Condition**: Used as a qualitative evaluation and revelation tool; requires 3-4 disguise images as input

**Evidence**: "we extract the latent information contained in the acquired samples xd using textual inversion to qualitatively reveal the disguises... we observe that although the disguises xd look visually similar to their corresponding base images xb, they contain drastically different latent information."

## [POSITIVE] Encoder-Decoder Examination for Detection
Passing suspected disguised images through the LDM autoencoder (D(E(xd))) to reveal hidden copyrighted content, exploiting the fact that E(xd) ≈ E(xc) implies D(E(xd)) ≈ xc.

**Delta**: perfect AUC (1.0) for content and style detection; AUC=0.875 for symbol detection with base image pool
**Condition**: Detection step 2; most effective for content and style disguises; less effective for symbol disguises due to shared background with base images

**Evidence**: "for a well-trained autoencoder, D(E(xc)) ≈ xc, while for disguises E(xd) ≈ E(xc), thus we have D(E(xd)) ≈ xc. In Figure 7, we show that the encoder-decoder architecture is a great detection tool for disguises, where the output of the autoencoder reveals the copyrighted content hidden in xd."

## [POSITIVE] Feature Similarity Search for Detection
First-step detection method that screens training data by computing encoder features and comparing with copyrighted image features using threshold γ2.

**Delta**: perfect AUC and no false positives across all tasks when copyrighted image xc is available
**Condition**: When the copyrighted image xc is known; used as screening step before encoder-decoder examination

**Evidence**: "We repeat the above experiment using our feature similarity search as a first step... We acquire perfect AUC score and obtain no false positives across all tasks, which indicate that the second step (encoder-decoder examination) is not required for this specific task."

## [POSITIVE] Reconstruction Loss Threshold for Detection Without xc
Using the reconstruction loss D1(D(E(xd)), xd) as a detection criterion for disguises without requiring knowledge of the copyrighted image, since disguises have anomalously high reconstruction loss compared to normal images.

**Delta**: AUC=1.0 for style, AUC=0.9933 for content, AUC=0.755 for symbol (with 100 ImageNette images pool)
**Condition**: Detection without knowledge of xc; less effective for symbol disguises where xc and xb share background

**Evidence**: "for disguises xd, the input xd and output of the autoencoder D(E(xd)) are significantly different... This property differs from normal images, which are expected to have low reconstruction loss."

## [POSITIVE] Robust Disguise with Horizontal Flip Augmentation
Extending the disguise generation objective to additionally penalize the feature distance between the horizontally flipped disguise and the horizontally flipped copyrighted image, making disguises robust to data augmentation.

**Delta**: qualitative improvement under horizontal flipping; standard disguises fail for complex content under horizontal flip
**Condition**: When textual inversion applies horizontal flip augmentation (50% probability); especially important for complex content disguises

**Evidence**: "we construct a new robust poison that additionally penalizes the distance between the features of the horizontally flipped poison and the horizontally flipped copyrighted image xc... The bottom two rows of Figure 16 demonstrate the effectiveness of the robust poison and its qualitative improvement under horizontal flipping."

## [NEUTRAL] Projection to Admissible Set [0,1]
Projecting the disguise xd to the valid normalized image pixel range [0,1] at each optimization step to ensure the disguise remains a legitimate image.

**Delta**: ensures valid pixel values; no specific performance delta reported
**Condition**: Applied at every optimization step during disguise generation

**Evidence**: "We set the admissible set to be in the range of [0, 1] as the legitimate (normalized) image pixel value"

## [POSITIVE] Fixed Pre-trained LDM Encoder
Exploiting the fact that the LDM encoder E is pre-trained and fixed during diffusion training, making the feature matching attack feasible since the feature extractor does not change.

**Delta**: enables the entire disguise generation attack; without fixed encoder the attack would not be applicable
**Condition**: Fundamental to the attack; applies to all LDM-based models with fixed pre-trained encoders

**Evidence**: "Conveniently, the encoder model E is pre-trained and its weights are fixed during the training of diffusion, thus making the above attack realistic."

## [NEUTRAL] Changing Initial Word in Textual Inversion
Choosing the initial word for textual inversion to match the visual appearance of the disguise (base image concept) rather than the copyrighted content.

**Delta**: changing the initial word does not lead to significant difference
**Condition**: During textual inversion on disguised images

**Evidence**: "Throughout our experiments, we choose the initial word to match the visual appearance of the disguises (thus the concept of the base image) and we observe that changing the initial word does not lead to a significant difference for the algorithm."
