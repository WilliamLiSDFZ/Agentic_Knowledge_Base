# xT: Nested Tokenization for Larger Context in Large Images

**Source**: https://proceedings.mlr.press/v235/gupta24b.html

## [POSITIVE] Nested Tokenization
Subdividing large images into regions at multiple levels: first into H×W regions, then each region is further patchified into P patches by the region encoder backbone

**Delta**: +8.6% top-1 accuracy on classification, +11.6 F1 on segmentation
**Condition**: Large image classification and segmentation tasks

**Evidence**: "We are able to increase accuracy by up to 8.6% on challenging classification tasks and F1 score by 11.6 on context-dependent segmentation on images as large as 29,000 x 29,000 pixels."

## [POSITIVE] Two-Stage Streaming Architecture
A streaming pipeline where regions are independently encoded by a vision backbone (Stage 1) and then contextualized by a lightweight context encoder (Stage 2), avoiding quadratic memory growth

**Delta**: Near-constant memory cost vs near-quadratic growth for standard Swin
**Condition**: Processing large images on contemporary GPUs

**Evidence**: "xT is a streaming, two-stage architecture that adapts existing vision backbones and long sequence language models to effectively model large images without quadratic memory growth."

## [POSITIVE] Increased Input Resolution (512/256 vs 256)
Using a larger input image size (512px) split into 256px regions, giving the model 4x more context than processing at 256px directly

**Delta**: +4.6% to +7.6% accuracy on iNaturalist classification
**Condition**: iNaturalist classification with xT framework

**Evidence**: "once we increase our input image size by 4× to 512/256, our model is immediately able to take advantage of the context with no increase in parameters, boosting accuracy up by 4.6%-7.6%."

## [NEGATIVE] Same-Resolution Context Encoder (256/256)
Using xT context encoder at the same resolution as the baseline (256/256) without increasing input image size

**Delta**: -0.83% to -1.41% top-1 accuracy vs baseline
**Condition**: iNaturalist classification when no additional context is provided

**Evidence**: "Comparing the Swin-T/L 256 run with Swin-T/L 256/256, which is our method taking in no context, our model actually does worse with extra parameters, likely due to non-functional parameters interfering with the model's learning."

## [POSITIVE] Transformer-XL Context Encoder (xT XL)
Using a Transformer-XL derivative with HyperAttention as the context encoder, enabling recurrent processing of prior sequence tokens via cross attention for sequences exceeding context length

**Delta**: +13.4 F1 overall, +6.0 F1 close-to-shore on xView3-SAR
**Condition**: xView3-SAR segmentation on very large satellite images (29,400×24,400 pixels)

**Evidence**: "xT always outperforms the corresponding non-context model, beating baselines by up to 13.4 points on the overall F1 detection score and 6.0 points on the close-to-shore F1 score"

## [POSITIVE] Mamba Context Encoder (xT Mamba)
Using Mamba (a selective state space model) as the context encoder, providing linear-time sequence modeling with fewer parameters than Hyper or ViT alternatives

**Delta**: Best classification result for Swin-T: 61.97% vs 60.56% for Hyper
**Condition**: iNaturalist classification with Swin-T and Swin-B/L region encoders

**Evidence**: "both Hyper and Mamba both perform better than ViT as context encoders with the added benefit of having a much larger capacity for scale. While Mamba has less parameters than both ViT and Hyper—up to 8% fewer parameters for Swin-T 〈xT〉 Mamba than for Swin-T 〈xT〉 Hyper"

## [POSITIVE] HyperAttention Context Encoder (xT Hyper)
Using a LLaMA-style architecture with HyperAttention (near-linear complexity via LSH) as the context encoder

**Delta**: Best result for Swin-S: 63.62%; Swin-B: 64.08% top-1 accuracy
**Condition**: iNaturalist classification, particularly effective for Swin-S and Swin-B

**Evidence**: "both Hyper and Mamba both perform better than ViT as context encoders with the added benefit of having a much larger capacity for scale."

## [POSITIVE] Stop Gradient Between Sequences in Transformer-XL
Applying stop gradient between sequence chunks in Transformer-XL recurrence, allowing context propagation without full sequence backpropagation memory costs

**Delta**: Significantly reduced memory (e.g., 0.47 GB vs 5.30 GB for Swin-T on xView3-SAR)
**Condition**: Transformer-XL context encoder when sequence exceeds context length

**Evidence**: "The application of a stop gradient between sequences lets information be propagated without suffering the memory costs incurred with full sequence backpropagation."

## [POSITIVE] Hierarchical Vision Backbone as Region Encoder
Using hierarchical vision transformers (SwinV2, Hiera) rather than isotropic ViTs as region encoders, producing shorter output sequences (4x or greater reduction)

**Delta**: Sequence length reduced by 4× or greater, enabling more regions per context window
**Condition**: Region encoding stage of xT framework

**Evidence**: "In our experiments, we utilize vision transformers which output a shorter sequence length than which is input to them. These sequence lengths are less than the equivalent length produced by isotropic ViTs. In this setup, we are able to effectively handle images with an increased number of regions, as our sequence length is reduced by 4× or greater."

## [POSITIVE] Deeper Context Encoder for Larger Region Encoders
Using N=2 context encoder layers as default, with larger region encoders benefiting more from deeper context encoders

**Delta**: Swin-L: 94.48% (depth 2) vs 91.67% (depth 1); Swin-B: 90.73% (depth 2) vs 89.08% (depth 1)
**Condition**: iNaturalist classification, especially with larger Swin-B and Swin-L region encoders

**Evidence**: "larger region encoders generally benefit from having deeper context encoders. The accuracy is the greatest when the depth is 2 for the largest model, and the trade-off is acceptable for the smallest model, being within 1 accuracy point, so we choose depth 2 as our default."

## [POSITIVE] Shallow Context Encoder for Smaller Region Encoders
Using N=1 context encoder layers for smaller models (Swin-T, Swin-S) where depth 1 outperforms depth 2

**Delta**: Swin-T: 86.38% (depth 1) vs 85.09% (depth 2); Swin-S: 88.26% (depth 1) vs 88.03% (depth 2)
**Condition**: iNaturalist classification with smaller Swin-T and Swin-S region encoders

**Evidence**: "larger region encoders generally benefit from having deeper context encoders. The accuracy is the greatest when the depth is 2 for the largest model, and the trade-off is acceptable for the smallest model, being within 1 accuracy point"

## [NEUTRAL] 2D Positional Embeddings for Context Encoder
Adding standard 2D positional embeddings to nested region features when the full sequence fits within the context encoder's context length

**Delta**: Not quantified separately
**Condition**: When region feature sequence fits entirely within context encoder's context length

**Evidence**: "We use standard 2D positional embeddings which are added to the nested region features."

## [POSITIVE] Smaller Window Size with xT vs Larger Window Size Alone
Using xT with smaller window size (16) on larger input achieves equivalent or better accuracy than Swin alone with larger window size (64), with much better throughput and memory

**Delta**: Swin-B xT XL at 1024/256 (window 16): 68.19% vs Swin-B at 1024 (window 64): 67.37%, with 3.75x better throughput and 12x less memory
**Condition**: iNaturalist classification at 1024px input size

**Evidence**: "Swin-B and our method have approximately equivalent accuracies, but xT achieves much more desirable throughput and memory utilization."

## [POSITIVE] xT on Cityscapes Detection (OOM Prevention)
Applying xT framework to enable Swin-B to process full Cityscapes images (1024×2048) that would otherwise cause out-of-memory errors

**Delta**: 43.0 mAP vs OOM for baseline Swin-B-DetINO
**Condition**: Object detection on Cityscapes with 2048px images

**Evidence**: "Swin-B is unable to model Cityscapes images in their entirety within the memory of an 80GB A100."

## [NEGATIVE] Downsampling Large Images
Reducing image resolution to fit within model memory constraints, losing high-frequency details

**Delta**: Significant information loss; models fail on tasks requiring fine details
**Condition**: Baseline approach for handling large images

**Evidence**: "Modern computer vision pipelines handle large images in one of two sub-optimal ways: downsampling or cropping. These two methods incur significant losses in the amount of information and context present in an image."

## [NEGATIVE] Windowed/Cropped Processing Without Context Sharing
Processing image crops independently without sharing context between windows, a common baseline approach

**Delta**: Up to 13.4 F1 points worse than xT on xView3-SAR
**Condition**: Baseline approach for large image processing

**Evidence**: "A common approach is to process the image by treating it as individual 'windows', each fed through the model without sharing context, resulting in sub-optimal performance."
