# Completing Visual Objects via Bridging Generation and Segmentation

**Source**: https://proceedings.mlr.press/v235/li24j.html

## [POSITIVE] Iterative Mask Denoising (IMD)
An iterative process alternating between generation and segmentation stages to progressively refine a partial object mask toward a complete mask, used as condition for object completion

**Delta**: FID-G 16.9 vs 30.8 (SD 2.1) on AHP; average user study rank 2.1 vs 3.1 (SD 2.1)
**Condition**: Object completion task on AHP and DYCE datasets

**Evidence**: "MaskComp consistently outperforms other methods, as evidenced by its notably lower FID scores, signifying the superior quality of its generated content."

## [POSITIVE] Mask Condition for Generation
Providing an object mask as an additional condition to the generative model alongside the partial object image

**Delta**: Complete mask: FID 12.7 vs partial mask: FID 16.9
**Condition**: Generation stage of MaskComp on AHP dataset

**Evidence**: "the model achieves its highest performance when it is conditioned with complete object masks, whereas relying solely on partial masks yields less optimal results. These results provide strong evidence that the quality of the conditioned mask significantly influences the quality of the generated images."

## [POSITIVE] Time-Variant Gating Operation
A learned linear transform applied to the time embedding to adjust the importance of partial object conditions across diffusion timesteps, modulating the partial token before feeding to ControlNet

**Delta**: +1.3 FID improvement (16.9 with gating vs 18.2 without)
**Condition**: CompNet architecture, generation stage on AHP dataset

**Evidence**: "we notice the gating operation improves the generation quality by 1.3 FID, indicating the necessity of conditional gating."

## [POSITIVE] SAM as Segmentation Model
Using Segment Anything Model (SAM) as the off-the-shelf segmentation model in the segmentation stage of IMD

**Delta**: FID 16.9 (SAM) vs 18.1 (SEEM) vs 19.9 (CLIPSeg)
**Condition**: Segmentation stage of IMD on AHP dataset

**Evidence**: "Table 4a shows that the FID score with CLIPSeg (19.9) is slightly higher than with SAM (16.9), but remains competitive against other state-of-the-art methods"

## [POSITIVE] Mask Voting (V) Strategy
Aggregating N sampled masks via a voting process using logits and a threshold to derive an improved mask for the next IMD step

**Delta**: FID 16.9 (Logits Voting) vs 17.2 (Logits Mean) vs 17.6 (Mask Voting) vs 17.0 (Mask Mean)
**Condition**: Segmentation stage aggregation strategy on AHP dataset

**Evidence**: "We notice voting with logits achieves the best performance. The current design choice of using SAM and voting with logits is based on the ablation results."

## [POSITIVE] Auxiliary Mask Loss (Pre-diffusion Mask Prediction)
An auxiliary path using a Feature Pyramid Network to predict the complete object mask from the partial token, supervised with Dice loss and BCE loss

**Delta**: FID 16.9 (with mask loss) vs 17.7 (without)
**Condition**: CompNet training on AHP dataset

**Evidence**: "The results indicate that the incorporation of mask prediction can benefit the final object completion performance."

## [POSITIVE] IMD Step Number (T=5)
Number of iterative mask denoising steps performed during inference

**Delta**: FID 24.7 (T=1) → 19.4 (T=3) → 16.9 (T=5) → 16.1 (T=7)
**Condition**: IMD inference on AHP dataset

**Evidence**: "we notice that the image quality keeps increasing and slows down at a step number of 5. In this way, we choose 5 as our IMD step number."

## [POSITIVE] Number of Sampled Images (N=5)
Number of images sampled from the generative model per IMD step for mask aggregation in the segmentation stage

**Delta**: FID 17.4 (N=4) → 16.9 (N=5) → 16.8 (N=6)
**Condition**: Segmentation stage of IMD on AHP dataset

**Evidence**: "We notice more sampled images generally leading to a better performance. We leverage an image number of 5 with the efficiency consideration."

## [POSITIVE] Diffusion Step Count
Number of denoising steps in the diffusion model during generation

**Delta**: FID 16.9 (20 steps) → 15.7 (40 steps) → 15.1 (50 steps)
**Condition**: CompNet generation stage on AHP dataset

**Evidence**: "We notice a larger diffusion step will lead to a better performance. After the number of diffusion steps is larger than 40, the performance improvement becomes slow."

## [NEUTRAL] Training Without Complete Objects (OpenImage)
Training MaskComp on OpenImage dataset which lacks ground-truth complete objects, using only partial masks

**Delta**: FID slightly lower than AHP-trained model (exact delta not specified, described as 'just slightly lower')
**Condition**: Training on OpenImage v6 subset without complete object ground truth

**Evidence**: "we notice that the performance of MaskComp trained on OpenImage is just slightly lower than that trained with AHP dataset, indicating that MaskComp has the potential to be adapted to the scenarios without ground-truth complete objects."

## [NEGATIVE] Object Occlusion Type (Object-shaped vs Rectangle/Oval)
Using object-shaped masks for occlusion during training, compared to simpler rectangle or oval shapes

**Delta**: FID 16.9 (object) vs 15.3 (rectangle) vs 15.1 (oval)
**Condition**: Training occlusion type ablation on AHP dataset

**Evidence**: "We notice that the occlusion with a more complicated object shape will impose more challenges on the proposed model."

## [NEUTRAL] Reducing Diffusion Steps in Early IMD Steps
Reducing the number of diffusion steps during the first few IMD steps to increase inference speed

**Delta**: Running time reduced to 2/3 with FID slightly increasing by 0.50
**Condition**: Inference speed optimization for MaskComp

**Evidence**: "reducing the number of diffusion steps during the first few IMD steps can increase model speed without sacrificing much performance. With this idea incorporated into MaskComp, the average running time could be reduced to 2/3 of the original time with FID slightly increasing by 0.50."

## [NEUTRAL] Robustness to Segmentation Errors
Manually adding random noise/errors to masks to test IMD robustness; errors increase convergence iterations but do not significantly affect final performance

**Delta**: With 15% area noise at Iter 9: FID 16.5 vs no noise at Iter 9: FID 15.9
**Condition**: Robustness analysis on AHP dataset with varying segmentation error degrees

**Evidence**: "We observe that segmentation errors will increase the convergence iteration number while not affecting the final performance significantly. As IMD is a reciprocal process intended to provide effective control for later-generated masks to be refined based on adaptive feedback, mask errors are mitigated and not propagated."

## [NEGATIVE] Amodal Segmentation Baseline Comparison
Using SOTA amodal segmentation to generate complete masks, then feeding them to ControlNet for image generation

**Delta**: FID 29.4 (amodal baseline) vs 16.9 (MaskComp)
**Condition**: Comparison on AHP dataset

**Evidence**: "we notice that our method outperforms the amodal baseline by a considerable margin, which could be attributed to the strong mask completion capability of the proposed IMD process."

## [POSITIVE] Interpolated Mask Conditioning During Training
Using a mask with occlusion rate between partial and complete masks as conditioning during training, to handle any mask in the interpolation range during inference

**Delta**: Intermediate mask FID 15.3 vs partial mask FID 16.9 (Table 3a)
**Condition**: CompNet training and inference on AHP dataset

**Evidence**: "the model must effectively handle any mask that falls within the interpolation between the initial partial mask and the target complete mask. Consequently, we introduce a mask M with an occlusion rate positioned between the partial and complete masks as a conditioning factor for the generative model."

## [NEGATIVE] High Occlusion Rate Performance Degradation
MaskComp performance under varying occlusion levels from 20% to 80%

**Delta**: FID 13.4 (20%) → 15.7 (40%) → 17.2 (60%) → 29.9 (80%)
**Condition**: Inference on AHP dataset with varying occlusion rates

**Evidence**: "we evaluate MaskComp at different occlusion levels (proportion of the obscured area relative to the complete object) ranging from 20% to 80%, and the results indicate that its performance does not degrade significantly up to 60% occlusion."
