# Revisiting Context Aggregation for Image Matting

**Source**: https://proceedings.mlr.press/v235/liu24as.html

## [NEGATIVE] Context Aggregation Modules (Pooling-based)
Hard-crafted pooling operations (e.g., PPM, ASPP) used to aggregate context from surrounding regions in matting networks

**Delta**: errors increase or stabilize beyond optimal inference patch size
**Condition**: when inference patch size differs from training patch size (context scale shift)

**Evidence**: "the matting methods with context aggregation modules experience a reduction in errors initially as the patch size increases, followed by a subsequent increase or stabilization... context aggregation modules are highly sensitive to the variations in context scale due to the differences in image sizes between the training and inference phases. This sensitivity proves detrimental to the performance of matting networks employing such modules."

## [NEGATIVE] Context Aggregation Modules (Affinity-based)
Masked correlation to construct affinity matrices for aggregating globally related context features

**Delta**: matting methods with context aggregation modules do not outperform basic networks without such modules
**Condition**: when evaluated on coarse trimaps or varying inference image sizes

**Evidence**: "matting methods with context aggregation modules do not outperform basic networks without such modules, further highlighting their limited universality due to the sensitivity of context aggregation modules to context scale."

## [POSITIVE] Basic Encoder-Decoder Network (no context aggregation modules)
Standard encoder-decoder architecture without any explicit context aggregation modules, relying on the network itself to learn context aggregation

**Delta**: BasicNet with Swin-Tiny: SAD 19.72 vs MatteFormer SAD 23.80; outperforms all compared state-of-the-art methods
**Condition**: when trained on large image patches (1024×1024)

**Evidence**: "the basic matting networks (referred to as BasicNet) outperform state-of-the-art methods, which suggests the feasibility of building basic matting networks using encoder-decoder."

## [POSITIVE] Large Image Patch Training Strategy
Training matting networks on larger image patches (up to 1024×1024) instead of smaller patches (256×256)

**Delta**: ResNet-34: SAD from 41.74 (256px) to 28.08 (1024px); Swin-Tiny: SAD from 27.99 (256px) to 19.72 (1024px); AEMatter: SAD from 24.40 (256px) to 17.53 (1024px)
**Condition**: applies to both basic encoder-decoder networks and AEMatter

**Evidence**: "The results, presented in Table 3, confirm that the performance of matting networks improves with larger training image patches, providing empirical backing for our hypothesis... basic matting networks can learn enhanced context aggregation from large image patches."

## [POSITIVE] Larger Convolution Kernel Size
Using larger convolution kernels (5×5 vs 3×3 vs 1×1) to increase the receptive field of network layers

**Delta**: ResNet-34: SAD 31.28 (1×1) → 28.08 (3×3) → 26.72 (5×5); ResNet-50: SAD 28.70 (1×1) → 23.82 (3×3) → 23.34 (5×5)
**Condition**: applied to ResNet-34 and ResNet-50 based basic matting networks

**Evidence**: "The results indicate that matting networks with larger convolution kernels achieve better performance, providing evidence that supports our hypothesis that networks with larger receptive fields exhibit enhanced context aggregation capability."

## [POSITIVE] Hybrid-Transformer Backbone
Replacing the patch-embedding stem of Swin-Tiny with convolution blocks to extract rich low-level features while retaining Swin blocks for high-level context features

**Delta**: SAD 19.72 (Swin-Tiny) → 19.57 (Hybrid-Transformer) with convolution decoder; further improvement in full AEMatter configuration
**Condition**: used as encoder in AEMatter on Adobe Composition-1K

**Evidence**: "the Hybrid-Transformer backbone of our AEMatter excels over the Swin-Tiny backbone in capturing low-level details, resulting in higher performance."

## [POSITIVE] Omitting Normalization Layers in Stem
Removing normalization layers from the convolution stem to preserve local image details

**Delta**: described as improving matting performance (no specific numeric delta given)
**Condition**: applied to the convolution stem of the Hybrid-Transformer backbone

**Evidence**: "To preserve the image details, we omit the normalization layers in the stem as they affect the information in local regions, which hurts the matting performance."

## [POSITIVE] PReLU Activation Function
Using PReLU (learnable negative slopes) instead of standard ReLU as the activation function in the backbone

**Delta**: described as facilitating network training (no specific numeric delta given)
**Condition**: used in the Hybrid-Transformer backbone of AEMatter

**Evidence**: "we incorporate PReLU (He et al., 2015) as the activation function, which introduces learnable negative slopes to facilitate network training."

## [POSITIVE] Transformer-based Decoder
Using Swin blocks in the decoder instead of convolution or residual blocks to enlarge receptive field for feature refinement

**Delta**: SAD: 19.57 (Conv decoder) → 19.23 (Residual decoder) → 18.91 (Transformer decoder)
**Condition**: used in AEMatter with Hybrid-Transformer encoder on Adobe Composition-1K

**Evidence**: "Experimental results demonstrate that the transformer-based decoder of our AEMatter outperforms the other designs."

## [POSITIVE] Axis-wise Attention in AEAL Block
Dividing features into axis-wise rectangular regions and applying multi-head self-attention to capture large-scale context with O(hw(h+w)) complexity

**Delta**: SAD: 19.07 (vanilla self-attention) → 18.30 (window attention) → 17.68 (axis-wise attention)
**Condition**: used as additional learning block in AEAL, applied after Hybrid-Transformer backbone

**Evidence**: "AEMatter with axis-wise attention surpasses AEMatter with vanilla self-attention and window attention."

## [POSITIVE] Appearance-Enhanced (AE) Block in AEAL
Using context-guided appearance features from third-stage backbone features to enhance context features before axis-wise attention

**Delta**: SAD: 17.68 (without AE) → 17.53 (with AE); MSE: 2.33 → 2.26
**Condition**: used within the AEAL block of AEMatter on Adobe Composition-1K

**Evidence**: "the AE block leads to further performance improvement, underscoring the effectiveness of the proposed AEAL block."

## [NEGATIVE] Vanilla Self-Attention as Additional Learning Block
Using standard global self-attention as an additional learning block after the backbone

**Delta**: SAD 19.07 vs 18.91 baseline (Transformer decoder, no AL block); worse than axis-wise attention (17.68)
**Condition**: used as additional learning block in AEMatter on Adobe Composition-1K

**Evidence**: "AEMatter with axis-wise attention surpasses AEMatter with vanilla self-attention and window attention."

## [POSITIVE] ImageNet Pretrained Backbone Weights
Initializing backbone weights with ImageNet pretrained weights to avoid overfitting

**Delta**: described as avoiding overfitting (no specific numeric delta given)
**Condition**: applied during AEMatter training

**Evidence**: "To avoid overfitting, the backbone weights are initialized with the weights pre-trained on the ImageNet dataset."

## [POSITIVE] Test-Time Augmentation (TTA)
Applying test-time augmentation during inference to improve prediction accuracy

**Delta**: SAD: 17.53 → 16.89; MSE: 2.26 → 2.06; Grad: 4.76 → 4.24; Conn: 12.46 → 11.72
**Condition**: applied to AEMatter at inference time on Adobe Composition-1K

**Evidence**: "AEMatter + TTA (Ours): SAD 16.89, MSE 2.06, Grad 4.24, Conn 11.72"

## [POSITIVE] Omitting Normalization in Decoder Convolution Blocks
Removing normalization layers from convolution blocks in the decoder to prevent feature map statistics from affecting local region estimation

**Delta**: described as preventing mean/variance interference in local regions (no specific numeric delta given)
**Condition**: applied in the final upsampling stages of the AEMatter decoder

**Evidence**: "we upsample Frd and concatenate it with the low-level features extracted by the stem of the encoder, and process it using convolution blocks that omit the normalization layers to prevent the mean or variance of the whole feature map from affecting the estimation in local regions."

## [POSITIVE] Larger Backbone Receptive Field (Swin-Tiny vs ResNet-34)
Using a backbone with a larger receptive field (Swin-Tiny transformer) compared to a smaller one (ResNet-34 CNN)

**Delta**: BasicNet SAD: 28.08 (ResNet-34) → 19.72 (Swin-Tiny) on Adobe Composition-1K
**Condition**: basic encoder-decoder networks trained on 1024×1024 patches

**Evidence**: "the Swin-Tiny and ResNet-50 based networks outperform the MobileNet and ResNet-34 based networks, which suggests that basic matting networks with a larger receptive field may learn better context aggregation to achieve higher performance."
