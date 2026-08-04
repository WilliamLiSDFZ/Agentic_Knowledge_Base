# Revealing the Dark Secrets of Extremely Large Kernel ConvNets on Robustness

**Source**: https://proceedings.mlr.press/v235/chen24bb.html

## [POSITIVE] Large Kernel Convolution (31×31)
Using extremely large convolutional kernels (e.g., 31×31) in CNNs instead of standard small kernels (3×3), as implemented in RepLKNet, to substantially increase the model's effective receptive field

**Delta**: +2.7 ImageNet-A accuracy over ViT-B, +7.0 ImageNet-C accuracy over ViT-B, +5.9 ImageNet-R accuracy over ViT-B, +10.9 ImageNet-O AUPR over ViT-B
**Condition**: Evaluated on ImageNet-A, ImageNet-C, ImageNet-R, ImageNet-O, salient occlusion, and noise robustness benchmarks

**Evidence**: "reducing the kernel size from 31 to 3 significantly degrades the robustness of RepLKNet across various metrics, leading to inferior performance compared to ViT-B. This finding highlights the critical role of large kernel convolution in enhancing model robustness."

## [NEGATIVE] Replacing Large Kernels with 3×3 Small Kernels (RepLKNet-3B)
Replacing all large kernel convolutions in RepLKNet-31B with 3×3 small kernel convolutions while maintaining the same data augmentation and training schedule

**Delta**: -12.1 ImageNet-A, -3.1 ImageNet-C, -5.1 ImageNet-R, -16.4 ImageNet-O AUPR, -17.4 salient-drop-50%, -4.0 noise-0.7π
**Condition**: Ablation study on RepLKNet-31B with all large kernels replaced by 3×3 kernels

**Evidence**: "Reducing the kernel size from 31 to 3 significantly degrades the robustness of RepLKNet across various metrics, leading to inferior performance compared to ViT-B."

## [POSITIVE] Scaling Up Kernel Size Progressively
Gradually increasing convolutional kernel size from 3×3 to 51×51 in ConvNeXt-Tiny architecture, trained on ImageNet-1K

**Delta**: ImageNet-A: 5.20 (3×3) → 10.71 (51×51); ImageNet-R: 28.87 (3×3) → 31.77 (51×51); ImageNet: 79.4 (3×3) → 81.6 (51×51)
**Condition**: ConvNeXt-Tiny trained with 120 epoch schedule on ImageNet-1K, evaluated on ImageNet, ImageNet-A, ImageNet-R

**Evidence**: "scaling up kernels can bring consistent improvements both on ImageNet and robustness benchmarks; basically, scaling up to 13×13 can make a favorable robustness, but continuing scaling up kernel size to 51×51 can bring further robustness"

## [NEUTRAL] ImageNet-21K Pre-training
Pre-training models on the larger ImageNet-21K dataset before fine-tuning on ImageNet-1K, shared across RepLKNet, BiT, and ViT for fair comparison

**Delta**: outperforms baseline
**Condition**: Used as a controlled variable to isolate the effect of architecture (kernel size) on robustness

**Evidence**: "Since RepLKNet, BiT, and ViT share similar pre-training strategies (such as using larger datasets like ImageNet-21K, extended pre-training schedules, and so on), they serve as excellent candidates for our comparison purposes."

## [POSITIVE] Local and Global Kernel Attention Pattern
Large kernel convnets naturally aggregate both local and global information at shallow layers while focusing more on global information at deeper layers, analogous to ViT attention patterns

**Delta**: outperforms baseline
**Condition**: Observed via kernel attention distance analysis across stages of RepLKNet

**Evidence**: "RepLKNet also tends to aggregate both local and global information at shallow layers, while focusing more on global information at deeper layers. This essentially suggests that simultaneously aggregating local and global information can more effectively capture different levels of information in images, thereby resulting in more powerful and robust performance."

## [POSITIVE] Stable Feature Map Variance
Large kernel convnets exhibit very low and stable feature map variance in early layers and smooth variance changes throughout the network, unlike ResNet and ViT which show large variance from the beginning and sharp fluctuations

**Delta**: outperforms baseline
**Condition**: Measured on ImageNet validation images with batch size 64, compared against ResNet and ViT

**Evidence**: "RepLKNet differs from the other two networks in two distinct aspects: i) It is very stable in the early stages... the variance of RepLKNet's feature maps remains at a very low level, while ViT and ResNet tend to have a large variance from the very beginning; ii) The variance change in a simple and coherent manner."

## [POSITIVE] Occlusion Invariance via Large Kernels
Large kernel convnets demonstrate superior robustness to random, salient (foreground), and non-salient (background) patch occlusion compared to typical CNNs and ViTs

**Delta**: outperforms ViT noticeably on salient occlusion; outperforms ViT at extreme occlusion ratios (>50%) for random drop
**Condition**: Evaluated with 10%-90% information loss under random, salient, and non-salient patch drop settings

**Evidence**: "RepLKNet exhibits remarkable robustness to salient occlusion, even surpassing ViT noticeably. We reckon this is the key reason for its substantial advantage over ViT on background-dependency dataset (i.e., ImageNet-9)."

## [POSITIVE] Robustness to All Noise Frequencies
Large kernel convnets maintain consistent robustness against noise across all frequency bands (low to high), unlike ResNet (susceptible to high-frequency noise) and ViT (susceptible to low-frequency noise)

**Delta**: accuracy loss consistently within 6% for noise across 0.1π to 0.8π frequency range, outperforming ResNet and ViT
**Condition**: Frequency-based random noise attacks with normalized frequency 0.0π to 1.0π, window size 0.1π

**Evidence**: "ResNet is highly susceptible to high-frequency noise, while ViT exhibits poorer performance against low-frequency noise... In contrast, RepLKNet consistently demonstrates robustness against noise across all frequency bands."

## [POSITIVE] Robustness to Model Perturbations (Block Removal)
Large kernel convnets maintain high accuracy even when multiple blocks are randomly removed after training during inference, indicating redundancy and robustness to model perturbations

**Delta**: RepLKNet maintains ~75% accuracy at 1/3 block dropping ratio, outperforming ViT-L despite smaller capacity; ViT-B accuracy nears zero at same ratio
**Condition**: Lesion study: n blocks randomly removed from trained network during inference, averaged over 10 independent samples per n

**Evidence**: "RepLKNet and ViT-L can still maintain an accuracy of around 75% at that dropping ratio. Moreover, we notice that despite having a smaller capacity, RepLKNet consistently outperforms ViT-L in terms of accuracy under the same block dropping ratios."

## [POSITIVE] Adversarial Robustness (FGSM/PGD/TAIG)
Large kernel convnets demonstrate stronger resistance to adversarial attacks including FGSM, PGD, and TAIG compared to ResNet and ViT

**Delta**: FGSM ε=0.3: RepLKNet 35.7% vs ViT/ResNet ~0%; TAIG ε=0.03: RepLKNet 39.2% attack success rate vs ViT-B 62.3%, ViT-L 54.9%, ResNet 47.7%
**Condition**: Evaluated under FGSM (ε=0.1-0.4), PGD (step=5, ε=0.002-0.008), and TAIG (ε=0.03-0.1) attacks

**Evidence**: "RepLKNet consistently exceeds both ViT and ResNet... large kernel network still behaves better than typical small kernel convnets and ViTs, showing its inherent robustness against adversarial attacks."

## [POSITIVE] Model Scaling (Base to Large)
Increasing model size from base to large for both RepLKNet and ConvNeXt large kernel convnets

**Delta**: ConvNeXt-L vs ConvNeXt-B: ImageNet-A 38.7 vs 33.9, ImageNet-R 47.6 vs 45.5, ImageNet-C 56.5 vs 53.2; RepLKNet-31L vs 31B: ImageNet-A 39.6 vs 29.4, ImageNet-R 49.1 vs 43.9
**Condition**: Scaling from base to large model size for ConvNeXt and RepLKNet; ImageNet-C improvement less significant for RepLKNet-31L due to input resolution mismatch

**Evidence**: "ConvNeXt also demonstrates strong robustness, and its robustness is further improved when the model size increases."

## [POSITIVE] DeepAugment + AugMix Data Augmentation
Combining DeepAugment and AugMix augmentation strategies specifically aimed at enhancing model robustness against corruptions on ImageNet-C

**Delta**: mCE 53.6% vs ResNet-50 76.7% and BiT 58.3%, but worse than RepLKNet-31B 36.5%
**Condition**: Evaluated on ImageNet-C mCE metric; RepLKNet without these augmentations still outperforms DeepAugment+AugMix

**Evidence**: "We additionally add DeepAugment and AugMix, which are specifically aimed at enhancing the model's robustness against corruptions observed in ImageNet-C. Surprisingly, RepLKNet outperforms other methods with a clear gap."
