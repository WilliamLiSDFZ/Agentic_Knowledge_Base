# DRCT: Diffusion Reconstruction Contrastive Training towards Universal Detection of Diffusion Generated Images

**Source**: https://proceedings.mlr.press/v235/chen24ay.html

## [POSITIVE] Diffusion Reconstruction Contrastive Training (DRCT) Framework
A universal training framework that generates hard samples by reconstructing real and fake images using diffusion models, then trains detectors with both classification loss and contrastive loss on four types of samples: real, real reconstructed, fake, and fake reconstructed images.

**Delta**: +20.22% avg ACC (67.73% to 87.95% for UnivFD backbone on GenImage)
**Condition**: Cross-set generalization on GenImage dataset, trained on SDv1.4

**Evidence**: "the UnivFD detector equipped with DRCT increases its detection accuracy from 67.73% to 87.95%, indicating DRCT's effectiveness in enhancing the generalizability of the used backbone detector."

## [POSITIVE] Hard Sample Generation via Diffusion Reconstruction
Real images are reconstructed using stable diffusion models (DDIM-based) to produce near-real images that visually resemble real images but contain subtle diffusion model fingerprints, serving as hard training samples.

**Delta**: +6.55% avg ACC over baseline (68.98% to 75.53%)
**Condition**: Ablation study with Conv-B backbone, trained on DRCT-2M/SDv1.4, tested on GenImage

**Evidence**: "When the original SDv1.4 fake images were replaced with reconstructed real images (Real Rec.), the average ACC significantly increased by 6.55%, indicating that training the model with both real images and reconstructed real images aids in guiding the detector to learn common distortion features of AI-generated images, while mitigating overfitting to semantic features."

## [POSITIVE] Contrastive Loss (Margin-Based)
A margin-based contrastive loss (Hadsell et al., 2006) that brings positive pairs (same real/fake label) closer together and separates negative pairs by a margin in feature space, combined with binary cross-entropy classification loss.

**Delta**: +6.54% avg ACC (76.99% to 83.53%)
**Condition**: Ablation study with Conv-B backbone, trained on DRCT-2M/SDv1.4, tested on GenImage

**Evidence**: "Lastly, when we added Contrastive Loss to the original BCE loss function during training, the average ACC saw a significant increase of 6.54%, reaching an overall accuracy of 83.53%."

## [POSITIVE] Including Original Fake Images with Reconstructed Real Images
Adding back original generated (fake) images to the training set alongside reconstructed real images, rather than training only on real and reconstructed real images.

**Delta**: +2.5% avg ACC
**Condition**: Ablation study with Conv-B backbone, trained on DRCT-2M/SDv1.4, tested on GenImage

**Evidence**: "Upon adding back the original SDv1.4 fake images, the average ACC increased by another 2.5%."

## [POSITIVE] Including Reconstructed Fake Images
Adding reconstructed versions of fake (generated) images as an additional training sample type alongside real, real reconstructed, and fake images.

**Delta**: +0.96% avg ACC
**Condition**: Ablation study with Conv-B backbone, trained on DRCT-2M/SDv1.4, tested on GenImage

**Evidence**: "Furthermore, including reconstructed fake images led to an additional 0.96% increase in average ACC."

## [POSITIVE] Using SDv2 vs SDv1 for Reconstruction
Using a higher-quality diffusion model (SDv2) instead of SDv1 for generating reconstructed training samples.

**Delta**: +5.76% avg ACC on DRCT-2M (90.79% SDv1 to 96.55% SDv2 for Conv-B backbone)
**Condition**: DRCT/Conv-B on DRCT-2M dataset

**Evidence**: "When using SDv2 for reconstruction, the average detection ACC can be further improved to 96.55% compared to the baseline detector Conv-B. This indicates that a better reconstruction model helps to achieve better detection performance on the DRCT-2M dataset."

## [POSITIVE] Conv-B (ConvNeXt-Base) as Backbone with DRCT
Using ConvNeXt-Base as the backbone detector enhanced with DRCT, which tunes all network weights during training.

**Delta**: avg ACC improved from 79.11% to 90.79% (SDv1) or 96.55% (SDv2) on DRCT-2M
**Condition**: Cross-model generalization on DRCT-2M dataset

**Evidence**: "merely using SDv1 for reconstruction in DRCT, the average detection ACC has already improved from 79.11% to 90.79% compared to the baseline detector Conv-B."

## [POSITIVE] UnivFD as Backbone with DRCT
Using UnivFD (ViT-L/14 backbone, only final FC layer trained) enhanced with DRCT framework.

**Delta**: avg ACC improved from 83.46% to 96.90% (SDv2) on DRCT-2M; 79.45% to 89.49% on GenImage
**Condition**: Cross-model generalization on DRCT-2M and GenImage datasets

**Evidence**: "DRCT/UnivFD trained on SDv2 reaches the highest average ACC of 96.90%."

## [POSITIVE] Full Network Fine-Tuning (Conv-B) vs Partial Fine-Tuning (UnivFD)
Conv-B tunes all network weights while UnivFD only tunes its final fully connected layer, affecting post-processing robustness.

**Delta**: Conv-B maintains detection ACCs of up to 99% for resizing and JPEG compression
**Condition**: Robustness against resizing and JPEG compression post-processing

**Evidence**: "Conv-B enhanced with DRCT exhibits better post-processing robustness, mainly due to the fact that Conv-B tunes all its network weights while UnivFD only tunes its final fully connected layer."

## [POSITIVE] Lambda Parameter (λ=0.3) for Loss Balancing
A weighting parameter λ that balances the trade-off between contrastive loss and binary cross-entropy classification loss, with default value set to 0.3.

**Delta**: optimal average accuracy achieved at λ=0.3
**Condition**: DRCT/Conv-B trained on DRCT-2M/SDv1.4, tested on GenImage

**Evidence**: "The results of Table 9 indicate that as λ progressively increases, the average accuracy of DRCT/Conv-B (trained on DRCT-2M/SDv1.4) on GenImage initially rises, then declines. The optimal average accuracy is achieved at a λ value of 0.3, which we have adopted as the default in our experiments."

## [POSITIVE] Data Augmentation Suite
A range of augmentations during training including horizontal flipping, Gaussian noise, Gaussian blurring, random rotation, JPEG compression with random quality, brightness/contrast adjustments, and grid dropout.

**Delta**: outperforms baseline
**Condition**: Training all detectors for robustness against post-processing

**Evidence**: "To achieve better robustness against post-processing, a range of data augmentations are conducted during training, including horizontal flipping, Gaussian noise disturbance, Gaussian blurring, random rotation, JPEG compression with random quality, brightness and contrast adjustments, and grid dropout."

## [POSITIVE] DRCT-2M Large-Scale Dataset
A million-scale dataset of 2 million images covering 16 types of stable diffusion models (text-to-image, ControlNet, and diffusion reconstruction variants) plus 136k real-world collected images (DRCT-2M-Wild).

**Delta**: DRCT/UnivFD achieves 87.67% avg ACC on GenImage when trained on DRCT-2M, 14.84% higher than best non-DRCT method
**Condition**: Cross-dataset evaluation: trained on DRCT-2M/SDv1.4, tested on GenImage

**Evidence**: "our proposed method DRCT/UnivFD achieves the highest average ACC score, reaching 87.67%, which is 14.84% higher than the best non-DRCT method F3Net."

## [NEGATIVE] DRCT Applied to GAN-Generated Image Detection
Applying the DRCT framework (designed for diffusion models) to detect GAN-generated images.

**Delta**: less marked improvement compared to diffusion-generated image detection
**Condition**: Detection of GAN-generated images (e.g., BigGAN subset)

**Evidence**: "While it also improves the detection accuracy for non-diffusion-based images, such as those generated by GANs, the improvement is less marked. This discrepancy mainly stems from the significant differences in the image generation processes of GAN-based and diffusion-based methods, which exhibit distinct generative artifacts."

## [NEGATIVE] Larger Reconstruction Steps for SDXL-DR
Using larger reconstruction steps when generating SDXL-based reconstructed images during training/testing.

**Delta**: makes detection more challenging (harder to identify as generated)
**Condition**: Detection of SDXL-DR reconstructed images when reconstruction step during training does not match testing

**Evidence**: "in the case of DRCT-2M/SDXL-DR, the larger the reconstruction step, the closer the reconstructed image gets to the real image (thus improving the quality of generation), which makes it more challenging to identify as a generated image."

## [NEGATIVE] Training Only on SDv1.4 Without DRCT
Training detectors solely on SDv1.4-generated images without any reconstruction or contrastive training augmentation.

**Delta**: ACCs drop to 50%-67% on unseen models like SDXL; avg 68.98% on GenImage for Conv-B
**Condition**: Cross-model generalization on DRCT-2M and GenImage datasets

**Evidence**: "Most methods exhibit extremely high ACCs on images generated by diffusion models related to SDv1.4...However, these approaches suffer a significant decline in ACC when detecting unseen and substantially altered diffusion models like SDv2, SDXL, SDXL-Refiner, SDXL-Turbo, LCM-SDXL, and SDXL-Ctrl."
