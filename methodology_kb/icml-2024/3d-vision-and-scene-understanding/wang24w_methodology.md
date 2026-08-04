# EvGGS: A Collaborative Learning Framework for Event-based Generalizable Gaussian Splatting

**Source**: https://proceedings.mlr.press/v235/wang24w.html

## [POSITIVE] Collaborative Joint Training
End-to-end joint training of depth estimation, intensity reconstruction, and 3D Gaussian regression modules together with a combined loss, rather than training each independently

**Delta**: PSNR: 27.04 -> 27.95, SSIM: 0.953 -> 0.968, LPIPS: 0.065 -> 0.045, RMSE: 2.53 -> 1.95, Abs.rel: 51.5 -> 39.4
**Condition**: Novel view synthesis, depth estimation, and intensity reconstruction on Ev3DS dataset

**Evidence**: "Experiments show models that have jointly trained significantly outperform those trained individually."

## [POSITIVE] Cascaded Feature Hierarchical Linkage
Connecting submodules by passing both feature volumes and output predictions from earlier modules to later ones, enabling smooth gradient backpropagation through the pipeline

**Delta**: w/o Cascade: PSNR 26.51, SSIM 0.934, LPIPS 0.068 vs full model: PSNR 27.95, SSIM 0.968, LPIPS 0.045
**Condition**: All three subtasks in the EvGGS framework

**Evidence**: "w/o Cascade means that the input does not contain the feature map of the previous network, but only the event voxel and prediction results from the last modules. In Table. 4, the performance of w/o Joint and w/o Cascade is significantly degraded because submodules hardly benefit from the others in the two settings."

## [POSITIVE] Depth Supervision Loss (LD)
Including explicit depth supervision loss during joint training to constrain the depth estimation module

**Delta**: w/o LD: PSNR 27.83, RMSE 2.37, Abs.rel 49.2 vs full model: PSNR 27.95, RMSE 1.95, Abs.rel 39.4
**Condition**: Depth estimation and novel view synthesis tasks

**Evidence**: "Table. 4 demonstrates that the absence of depth supervision during joint training leads to a decline in depth estimation."

## [POSITIVE] Intensity Supervision Loss (LI)
Including explicit intensity reconstruction supervision loss during joint training to constrain the intensity module

**Delta**: w/o LI: PSNR 26.94, SSIM 0.959, LPIPS 0.518, RMSE 1.98, Abs.rel 41.6 vs full model: PSNR 27.95, SSIM 0.968, LPIPS 0.045, RMSE 1.95, Abs.rel 39.4
**Condition**: All three subtasks; notably LPIPS degrades severely without LI (0.518 vs 0.045)

**Evidence**: "w/o LI results in a lack of constraints for intensity reconstruction, which degrades the performance of the subsequent cascaded Gaussian regressor and adversely affects the other two submodules with varying degrees."

## [POSITIVE] Depth Feature Volume Passed to Intensity Module
Passing the 32-dimensional output feature volume from the depth UNet to the intensity reconstruction module to provide geometry-aware context for appearance recovery

**Delta**: EvGGS_i (independent): PSNR 26.94, SSIM 0.957, LPIPS 0.0367 vs EvGGS_j (joint): PSNR 29.18, SSIM 0.969, LPIPS 0.0324
**Condition**: Intensity reconstruction task

**Evidence**: "The cascaded connection guarantees that geometric priors are taken into account when the module deduces appearance."

## [POSITIVE] Foreground Mask Filtering
Predicting a foreground mask from the depth module and multiplying it with all 3D Gaussian parameter maps to filter out useless background regions

**Delta**: outperforms baseline
**Condition**: 3D Gaussian reconstruction from event data

**Evidence**: "The foreground mask is multiplied with all 3D Gaussian parameter maps to filter out the useless and empty backgrounds."

## [POSITIVE] Spatial-Temporal Voxel Grid Event Representation
Encoding event streams into spatial-temporal voxel grids with B=5 temporal bins using trilinear interpolation of event polarities

**Delta**: outperforms baseline
**Condition**: Event data preprocessing for all modules

**Evidence**: "To process the event stream synchronously, we encode the events in ∆t in a spatial-temporal voxel grid. The duration ∆t is discretized into B temporal bins. Each event trilinearly contributes to its near voxels by its polarity... Following (Scheerlinck et al., 2020), we set B = 5 in our experiments."

## [POSITIVE] Accumulated Event Frame as Auxiliary Input
Using accumulated event frames (with positive, negative, and combined polarities concatenated) as additional input to the intensity reconstruction module for boundary information

**Delta**: outperforms baseline
**Condition**: Intensity reconstruction module

**Evidence**: "the accumulated event frame, which is produced by accumulating events at the same pixel location together, and we repeat the operation three times for different polarity combinations including positive, negative, positive and negative, respectively, and concatenate them along the channel dimension because the event frame contains rich boundary information which helps recover dense intensity maps."

## [POSITIVE] Depth Module Pretraining
Pretraining the depth prediction module with L1 loss before starting collaborative joint training of the full pipeline

**Delta**: outperforms baseline
**Condition**: Training strategy for the full EvGGS framework

**Evidence**: "To mitigate the optimization complexity, we first pretrain the depth prediction module by L1 loss."

## [POSITIVE] Joint Loss Weighting (λ1=0.2, λ2=0.2, λ3=0.6)
Balancing the three loss components (depth, intensity, rendering) with weights 0.2, 0.2, and 0.6 respectively to emphasize the rendering loss

**Delta**: outperforms baseline
**Condition**: Joint training of all three modules

**Evidence**: "λ1, λ2, λ3 are coefficients to balance the loss magnitudes. We set 0.2, 0.2, and 0.6 respectively throughout all experiments."

## [POSITIVE] Perceptual Loss for Intensity and Rendering
Combining L1 loss with perceptual loss (weighted 0.8 and 0.2) for intensity reconstruction and novel view synthesis supervision

**Delta**: outperforms baseline
**Condition**: Intensity reconstruction and novel view synthesis losses

**Evidence**: "Lp is the perceptual loss (Zhang et al., 2018). β1, β2 aim to balance the L1 and perceptual loss, we constantly set them to 0.8 and 0.2 for all situations."

## [POSITIVE] 3DGS-based Representation over NeRF
Using 3D Gaussian Splatting instead of NeRF for event-based reconstruction, avoiding continuous network encoding that struggles with discontinuities common in event data

**Delta**: EvGGS PSNR 27.95 vs EventNeRF 24.62; rendering 195 FPS vs 0.045 FPS
**Condition**: Event-based 3D reconstruction compared to EventNeRF

**Evidence**: "NeRF encodes scenes in continuous networks, thereby cannot effectively fit discontinuities and empties which are common in event representations... EventNeRF fails to render in real-time and only produces videos with 0.045 FPS, while... our EvGGS can interactively produce real-time videos, their FPS are... 195 respectively."

## [POSITIVE] Generalizable Feedforward Inference
Training a model that can generalize to unseen scenes without per-scene retraining, using a feedforward pass instead of per-scene optimization

**Delta**: EvGGS PSNR 27.95, SSIM 0.968, LPIPS 0.045 vs EventNeRF (per-scene) PSNR 24.62, SSIM 0.945, LPIPS 0.072
**Condition**: Novel view synthesis on unseen scenes

**Evidence**: "The proposed method outperforms existing event-based methods by a large margin... our method can generalize to unseen scenes."

## [POSITIVE] Fine-tuning on Real Data (EvGGS-f)
Fine-tuning the model trained on synthetic data on real-world event data to reduce the sim-to-real gap

**Delta**: EvGGS-g: PSNR 26.77, SSIM 0.896, LPIPS 0.128 vs EvGGS-f: PSNR 27.84, SSIM 0.927, LPIPS 0.086
**Condition**: Realistic event dataset Ev3D-R

**Evidence**: "The EvGGS-f shows that the performance of the proposed approach can be further improved during fine-tuning."

## [POSITIVE] Lightweight Gaussian Regressor Architecture
Using a simple residual block with two convolutional layers for Gaussian parameter regression, relying on rich high-level features from upstream modules rather than a complex architecture

**Delta**: outperforms baseline
**Condition**: Gaussian parameter regression module

**Evidence**: "This module is a residual block with two convolutional layers... The input tensor contains rich high-level semantic meanings thus we do not employ complicated architectures at this step."

## [NEGATIVE] Independent Training without Joint Framework
Training each submodule separately without collaborative joint training or cascaded feature sharing

**Delta**: w/o Joint: PSNR 27.04 vs joint: 27.95; intensity EvGGS_i PSNR 26.94 vs EvGGS_j 29.18
**Condition**: All subtasks when trained without collaborative framework

**Evidence**: "Compared to our independent training case, it can be seen that without the assistance of collaborative training, our intensity reconstruction module cannot reconstruct the contrast of the scene. Although it also reconstructs clearer textures, the reconstructed intensity images are still darker than the groundtruths."

## [NEGATIVE] E2VID Preprocessing Pipeline (E2VID+3DGS)
Using E2VID to first reconstruct intensity frames from events, then feeding them into 3DGS for reconstruction, making quality entirely dependent on E2VID output quality

**Delta**: E3DGS PSNR 19.19, SSIM 0.814, LPIPS 0.119 vs EvGGS PSNR 27.95, SSIM 0.968, LPIPS 0.045
**Condition**: Novel view synthesis baseline comparison

**Evidence**: "Compared to E2VID+3DGS, the reconstruction quality of E2VID+3DGS entirely depends on the quality of the intensity reconstruction module."

## [NEUTRAL] Normalized Log Disparity Prediction
Predicting normalized log disparity instead of direct depth values, converting to depth via sigmoid activation

**Delta**: similar results observed
**Condition**: Depth estimation module output representation

**Evidence**: "We additionally attempt to directly regress normalized depth value and similar results are observed in the final experiments."
