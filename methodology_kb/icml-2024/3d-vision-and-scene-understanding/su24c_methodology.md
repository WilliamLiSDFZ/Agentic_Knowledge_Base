# Compositional Image Decomposition with Diffusion Models

**Source**: https://proceedings.mlr.press/v235/su24c.html

## [POSITIVE] Diffusion Model as Energy Function Parameterization
Using denoising diffusion probabilistic models to parameterize energy functions for unsupervised image decomposition, leveraging the equivalence between denoising networks and gradient fields of energy functions

**Delta**: outperforms baseline
**Condition**: Applied across all datasets (CelebA-HQ, Falcor3D, Virtual KITTI 2, CLEVR) compared to COMET and other baselines

**Evidence**: "our method outperforms existing methods in terms of FID, KID, and LPIPS across datasets, indicating superior image reconstruction quality"

## [POSITIVE] Denoising-Based Training Objective
Training via single-step denoising supervision instead of back-propagating through iterative gradient descent optimization, avoiding second-order gradients

**Delta**: outperforms baseline
**Condition**: Compared to COMET's energy-based training which requires second-order gradients

**Evidence**: "This resulting objective is simpler to train than that of COMET, as it requires only a single step denoising supervision and does not need computation of second-order gradients"

## [POSITIVE] Predicting x0 Instead of Noise ε
Training the denoising network to directly predict the original image x0 and then regressing ε, rather than directly predicting the noise ε

**Delta**: CelebA-HQ MSE: 76.168 vs 105.003 (ε prediction); CLEVR MSE: 6.178 vs 56.179 (ε prediction)
**Condition**: Ablation on CelebA-HQ and CLEVR datasets, with multiple components

**Evidence**: "We find that directly predicting the input x0 (3rd and 6th rows) outperforms the ε parametrization (1st and 4th row) on both CelebA-HQ and CLEVR datasets in terms of MSE and LPIPS"

## [POSITIVE] Multiple Components for Reconstruction
Using multiple decomposed components (K factors) for image reconstruction rather than a single component

**Delta**: CelebA-HQ MSE: 76.168 vs 88.551 (single component); CLEVR MSE: 6.178 vs 26.094 (single component)
**Condition**: Ablation on CelebA-HQ and CLEVR datasets, both using x0 prediction

**Evidence**: "We also compare using a single component to learn reconstruction (2nd and 5th rows) with our method (3rd and 6th rows), which uses multiple components for reconstruction. Our method achieves the best reconstruction quality as measured by MSE and LPIPS."

## [POSITIVE] Information Bottleneck via Low-Dimensional Latents
Constraining latent representations to be low-dimensional to encourage components to discover independent portions of the image

**Delta**: outperforms baseline
**Condition**: Applied during training to encourage disentanglement across all datasets

**Evidence**: "We leverage information bottleneck to encourage components to discover independent portions of x_i by constraining latent representations z = {z1, z2, · · · , zK} to be low-dimensional."

## [POSITIVE] Latent Dimension of 64
Setting the latent representation dimensionality to 64 for the encoder

**Delta**: MIG: 26.45 vs 11.72 (dim=32) and 12.97 (dim=128); MCC: 80.42 vs 57.67 (dim=32) and 80.27 (dim=128)
**Condition**: Disentanglement evaluation on Falcor3D dataset

**Evidence**: "We find that our method achieves the best performance when using a dimension of 64."

## [NEGATIVE] Latent Dimension of 32
Using a smaller latent dimension of 32 for the encoder

**Delta**: MIG: 11.72 vs 26.45 (dim=64)
**Condition**: Disentanglement evaluation on Falcor3D dataset

**Evidence**: "We posit that a smaller dimension may lack the capacity to encode all the information, thus leading to worse disentanglement."

## [NEGATIVE] Latent Dimension of 128
Using a larger latent dimension of 128 for the encoder

**Delta**: MIG: 12.97 vs 26.45 (dim=64)
**Condition**: Disentanglement evaluation on Falcor3D dataset

**Evidence**: "A larger dimension may be too large and fail to separate distinct factors."

## [NEUTRAL] PCA Projection from Dimension 128 to 64
Applying PCA to project the output dimension from 128 to 64 as a post-processing step

**Delta**: MIG improves from 12.97 to 16.57 but MCC decreases from 80.27 to 71.19
**Condition**: Applied to dim=128 model on Falcor3D disentanglement evaluation

**Evidence**: "Thus, we apply PCA to project the output dimension 128 to 64 (last row), and we observe that it can boost the MIG performance but lower the MCC score."

## [POSITIVE] Compositional Sampling via Summed Denoising Directions
Composing multiple factors by summing their individual predicted noise/denoising directions during sampling

**Delta**: outperforms COMET
**Condition**: Cross-dataset recombination between CLEVR and CLEVR Toy datasets

**Evidence**: "Our method outperforms COMET on both datasets, indicating the model can obtain better visual quality and more cohesive recombinations."

## [POSITIVE] Finetuning Pretrained Stable Diffusion
Adapting a pretrained Stable Diffusion model by training only the encoder and finetuning the diffusion model together on a small dataset

**Delta**: trained on only 100 images for 1000 iterations
**Condition**: Applied to Van Gogh painting dataset with pretrained Stable Diffusion as prior

**Evidence**: "In our experiment, we train our model on a small dataset of 100 Van Gogh paintings for 1000 iterations. As shown in Figure 11, our method can decompose such images into a set of distinct factors, such as smoothness, sharpness, and color tone"

## [NEGATIVE] Fixed Number of Components K
Requiring the user to specify the number of decomposition factors K as a hyperparameter

**Delta**: descriptive
**Condition**: General limitation across all datasets and use cases

**Evidence**: "our current approach decomposes images into a fixed number of factors that is specified by the user. While there are cases where the number of components is apparent, in many datasets the number is unclear or may be variable depending on the image."

## [POSITIVE] Unsupervised Training without Segmentation Masks
Performing decomposition without explicit segmentation masks or labels, relying purely on the diffusion model composition framework

**Delta**: outperforms baseline
**Condition**: Compared to methods requiring segmentation masks or text supervision

**Evidence**: "our decomposition approach is completely unsupervised... our approach is not limited by a specific encoder architecture because factor discovery is performed by modeling a composition of energy landscapes through the connection between diffusion models and EBMs"
