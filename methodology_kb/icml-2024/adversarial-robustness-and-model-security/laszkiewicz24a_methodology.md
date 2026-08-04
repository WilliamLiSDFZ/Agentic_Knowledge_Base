# Single-Model Attribution of Generative Models Through Final-Layer Inversion

**Source**: https://proceedings.mlr.press/v235/laszkiewicz24a.html

## [POSITIVE] FLIPAD (Final-Layer Inversion Plus Anomaly Detection)
Combines final-layer inversion to extract features from the penultimate layer of a generative model with anomaly detection (DeepSAD) for single-model attribution in the open-world setting.

**Delta**: average attribution accuracy over 97.5% in all CelebA/LSUN cases
**Condition**: Single-model attribution across GANs, diffusion models, medical image models, and tabular data

**Evidence**: "FLIPAD is capable of adapting to various settings and performs best, or only slightly worse, than competing methods... our approach is not limited to the image domain and achieves excellent empirical results on a variety of different generative models, including GANs and diffusion models."

## [POSITIVE] Final-Layer Inversion via Lasso Optimization
Reduces the final-layer inversion problem to a convex lasso optimization problem, finding activations before the final layer that approximately reconstruct the input while staying close to the expected average activation.

**Delta**: unique solution with probability 1; avoids multiple restarts required by non-convex full inversion
**Condition**: Feature extraction for generative models with invertible final activation and 2D-convolutional final layer

**Evidence**: "our method is i) significantly more efficient due to the convexity of the optimization problem and ii) theoretically sound given the connection to the denoising basis pursuit."

## [POSITIVE] DeepSAD Anomaly Detector
Uses Deep Semi-Supervised Anomaly Detection (DeepSAD) as the anomaly detection component, learning a deep feature extractor that maps normal samples close and anomalies far from a prefixed center point.

**Delta**: outperforms baseline fingerprinting and inversion methods in most settings
**Condition**: Used as the anomaly detection backbone for RawPAD, DCTPAD, and FLIPAD

**Evidence**: "We decide to use DeepSAD (Ruff et al., 2020), which works particularly well in high-dimensional computer-vision tasks but is also capable of generalizing to other domains."

## [NEUTRAL] RawPAD (Raw Plus Anomaly Detection)
Applies anomaly detection directly to raw input samples without any feature extraction step.

**Delta**: performs decently in most settings but generalizes worse to open-world setting
**Condition**: Single-model attribution baseline; works well under JPEG compression and random noise perturbations

**Evidence**: "RawPAD and DCTPAD are simple baselines that work decently in most settings but tend to generalize worse to the open-world setting."

## [NEUTRAL] DCTPAD (DCT Plus Anomaly Detection)
Uses the discrete cosine transform of images as handcrafted features for the anomaly detector, exploiting GAN generation artifacts in the frequency domain.

**Delta**: achieves excellent results for style-based generators but fails to generalize to other generative models (e.g., Stable Diffusion non-v1-4 models)
**Condition**: Effective for StyleGAN models with distinctive DCT artifacts; ineffective for Stable Diffusion generalization

**Evidence**: "While DCTPAD fails to generalize to other generative models, the other approaches achieve high attribution accuracies above 90% across all models... for the style-based generators, DCTPAD achieves excellent results, even for unseen generative models."

## [POSITIVE] Viewing Single-Model Attribution as Anomaly Detection
Reframes the single-model attribution problem as an anomaly detection task, treating samples from the target model as normal and samples from other sources as anomalies.

**Delta**: enables open-world single-model attribution not previously addressed
**Condition**: Open-world single-model attribution setting

**Evidence**: "We address the problem of single-model attribution in the open-world setting, which previously has not been solved adequately. Our work is the first to establish the natural connection between single-model attribution and anomaly detection."

## [POSITIVE] Average Activation Regularization (Monte-Carlo estimate of expected activation)
Regularizes the lasso optimization towards the average activation of the generative model estimated via Monte-Carlo sampling, biasing solutions towards likely activations.

**Delta**: enables distinguishable features between in-distribution and out-of-distribution samples
**Condition**: Final-layer inversion optimization in FLIPAD

**Evidence**: "the regularization towards the average activation z̄_{L-1} biases the solutions towards reasonable activations (Example 4.2), which share a similar structure to z̄_{L-1} (Example 4.3)."

## [POSITIVE] L1 Sparsity Regularization in Inversion
Uses L1-norm regularization in the lasso formulation to encourage sparsity of the difference between the estimated activation and the average activation.

**Delta**: unique solution with probability 1 for convolutions with continuously distributed kernel weights
**Condition**: Lasso optimization for final-layer inversion

**Evidence**: "The ℓ1-distance regularizes towards sparsity of ẑ_{L-1} − z̄_{L-1}, i.e., towards many similar components of ẑ_{L-1} and z̄_{L-1}."

## [POSITIVE] FISTA Solver for Lasso
Uses the Fast Iterative Shrinkage-Thresholding Algorithm (FISTA) to solve the lasso optimization problem for final-layer inversion.

**Delta**: significantly faster than full inversion methods (e.g., 17.48 min vs 300.75 min for 1000 CelebA samples)
**Condition**: Computational efficiency of FLIPAD feature extraction

**Evidence**: "Property 1) allows us to use fast and computationally tractable lasso algorithms such as FISTA (Beck & Teboulle, 2009), which enjoys finite-sample convergence guarantees."

## [NEGATIVE] Full Inversion Methods (SM-Inv2, SM-Invinc)
Baseline inversion methods that perform full non-convex inversion of the generative model via backpropagation, requiring multiple restarts due to non-convexity.

**Delta**: accuracy ranges from 50% to almost perfect; 300+ minutes for 1000 samples vs 17 minutes for FLIPAD
**Condition**: Single-model attribution baseline; computationally prohibitive for large models like Stable Diffusion

**Evidence**: "SM-Inv2 and SM-Invinc perform well only in very few settings and their computational load restricts their practicality considerably... Inverting these 12 samples already took 595.73 and 617.37 minutes, respectively."

## [NEUTRAL] Fingerprinting Method (SM-F)
Adapted fingerprinting baseline that exploits generator-specific traces in images using noise residuals or frequency-domain features.

**Delta**: 64.81% average accuracy on CelebA 64x64; near-perfect on high-dimensional style-based models
**Condition**: Effective for high-dimensional images and style-based models; fails for 64x64 images and non-image domains

**Evidence**: "SM-F achieves excellent performance for high-dimensional images but fails for low-dimensional images (64×64). Furthermore, its application is bound to the image domain."

## [POSITIVE] Immunization Training (Perturbation-Aware Training)
Training the attribution model on data modified by the same type of perturbation as the test data to improve robustness against adversarial perturbations.

**Delta**: improves performance under blur and crop perturbations for FLIPAD
**Condition**: Robustness evaluation against blur, crop, noise, and JPEG compression

**Evidence**: "We investigate the attribution performance on perturbed samples in the immunized setting, i.e., we train the models on data that is modified by the same type of perturbation."

## [NEGATIVE] JPEG Compression Perturbation
Applying JPEG compression as an adversarial perturbation to generated samples to hinder model attribution.

**Delta**: performance drop for FLIPAD (e.g., 63.78% at quality 90 on CelebA vs 99.36% for blur)
**Condition**: FLIPAD under JPEG compression adversarial perturbation

**Evidence**: "in the case of JPEG compression and the presence of random noise, we can see a performance drop of FLIPAD. In contrast, those perturbations influence the performance of RawPAD only slightly."

## [NEGATIVE] Random Noise Perturbation
Adding Gaussian noise to generated samples as an adversarial perturbation to hinder model attribution.

**Delta**: performance drop for FLIPAD under noise perturbation
**Condition**: FLIPAD under random noise adversarial perturbation

**Evidence**: "in the case of JPEG compression and the presence of random noise, we can see a performance drop of FLIPAD. In contrast, those perturbations influence the performance of RawPAD only slightly."

## [NEUTRAL] Using Generated Samples from Another Model as Negative Training Data
When real training data is unavailable or unclear, using samples from another generative model as negative examples during attribution training.

**Delta**: enables attribution in settings without access to real data (e.g., Stable Diffusion, medical imaging)
**Condition**: Stable Diffusion and medical image attribution experiments

**Evidence**: "we use images from v1-4 instead of real images for training, since it is not entirely clear on which data the model was trained... when the real data is not available at all (e.g. in medical applications)."

## [POSITIVE] Same-Architecture Different-Seed Attribution
Evaluating attribution between models with identical architecture and training data but different random initialization seeds, a harder attribution task.

**Delta**: FLIPAD maintains reliable attribution; other methods degrade significantly
**Condition**: Hard attribution setting with same-architecture different-seed models (Table 2)

**Evidence**: "Since FLIPAD involves the knowledge of the exact weights of G, we argue that it enables reliable model attribution even in the case of these subtle model variations."

## [NEGATIVE] Skip-Connection Complication for StyleGAN2
The presence of skip-connections in StyleGAN2 complicates the application of FLIPAD's final-layer inversion.

**Delta**: FLIPAD omitted for StyleGAN2 experiments
**Condition**: FLIPAD applied to style-based generative models with skip-connections

**Evidence**: "Note that the skip-connections in StyleGAN2 do not prohibit but complicate the application of FLIPAD considerably. Consequently, we omit its application in this setting."
