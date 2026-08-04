# On Gradient-like Explanation under a Black-box Setting: When Black-box Explanations Become as Good as White-box

**Source**: https://proceedings.mlr.press/v235/cai24h.html

## [POSITIVE] GEEX (Gradient-Estimation-based Explanation)
An attribution method that produces gradient-like explanations under a black-box setting by integrating gradient estimations over a straightline path from a baseline to the explicand, requiring only query-level access to the target model.

**Delta**: outperforms all black-box competitors across all test settings; competitive with white-box methods
**Condition**: All test settings: MNIST, Fashion-MNIST, ImageNet with CNN and InceptionV3

**Evidence**: "the proposed method consistently surpasses other black-box explainers across all test settings. The higher scores indicate that the assigned feature attributions correctly reflect to their actual contributions."

## [POSITIVE] Baseline Integration (Path Integral)
Introducing a reference baseline that models feature absence and integrating gradient estimations over a straightline path from the baseline to the explicand, analogous to Integrated Gradients.

**Delta**: overcomes gradient saturation issues of raw gradient estimation
**Condition**: Compared to raw gradient estimation (GE) which violates Sensitivity

**Evidence**: "The failure when employing raw gradient estimation stems from the lack of a reference point that models the absence of features... To overcome the aforementioned limitations, we present GEEX... an attribution method that introduces a baseline and integrates estimations over a straightline path from the baseline to the explicand."

## [NEGATIVE] Raw Gradient Estimation as Explanation
Directly using gradient estimation outputs as feature attributions without baseline integration or path integration.

**Delta**: scores below random deletion baseline on InceptionV3
**Condition**: InceptionV3 on ImageNet; high-dimensional inputs

**Evidence**: "However, this is not the case for SG and GE in explaining decisions from InceptionV3. Their explanations, directly using either actual or estimated gradients, suffer from gradient saturation, leading to the overlooking of relevant features and subsequently limited performance."

## [POSITIVE] Merged Sum (Dense One-Sample Estimators)
Merging the sums from interpolation steps and gradient estimation samples into a single cumulative sum of dense one-sample gradient estimators along the integral path, streamlining hyperparameter selection and improving path integral approximation.

**Delta**: GEEX outperforms IG on simpler test cases (MNIST, Fashion-MNIST)
**Condition**: MNIST and Fashion-MNIST datasets; simpler classification tasks

**Evidence**: "merging the terms for integral approximation and gradient estimation improves explanation quality by providing a 'smoother' approximation of the path integral without compromising the precision of gradient estimations... For the simpler test cases, our approach even achieves better performances, which should be interpreted as an improvement brought by the smoother approximation of the path integral."

## [POSITIVE] Mirror Sampling
A variance reduction technique for gradient estimation that uses mirrored/antithetic samples to ensure isotropicity of the search distribution.

**Delta**: enables proof of complementary information sharing between neighboring estimators
**Condition**: Applied during gradient estimation sampling; facilitates theoretical guarantees

**Evidence**: "mirror sampling adopted in this work ensures the isotropicity of the search distribution, which brings convenience to the proof of complementary information."

## [POSITIVE] Mask Smoothing via Gaussian Filter
Post-processing sampled noise masks with a Gaussian blur filter (kernel size 5, deviation 0.7) before applying them as perturbations, softly grouping spatially adjacent pixels to expose model sensitivities to local patterns.

**Delta**: mitigates estimation noise caused by feature space expansion for high-dimensional inputs
**Condition**: High-dimensional inputs (ImageNet, 299x299); trades off correctness for usefulness

**Evidence**: "mask smoothing is implemented through a Gaussian filter with a kernel size of 5 and a deviation of 0.7 when tested on ImageNet... the filter softly groups spatially close pixels following the prior knowledge that adjacent pixels form low-level features... such a convenience helps expose model sensitivities to the absence of local patterns, thus facilitating the identification of relevant pixels."

## [NEGATIVE] Mask Smoothing Trade-off
Applying mask smoothing violates the assumption that feature values should be sampled independently for gradient estimation.

**Delta**: theoretical correctness compromised
**Condition**: When mask smoothing is applied; high-dimensional inputs only

**Evidence**: "it should be noted that the grouping does not stick to the assumption that feature values should be sampled independently for gradient estimation. Therefore, the application of mask smoothing raises a trade-off between the usefulness and correctness of resultant explanations and is preferred only when explaining high-dimensional explicands."

## [POSITIVE] Explicand-specific Blurred Baseline
Using a blurred version of the explicand itself as the baseline for ImageNet explanations, rather than a zero/black baseline.

**Delta**: recommended practice for ImageNet; used consistently across competing methods for fair comparison
**Condition**: ImageNet dataset with full-color high-resolution images

**Evidence**: "the baseline for ImageNet is explicand-specific. For each explicand from ImageNet, the baseline is a blurred version of itself as suggested by (Sturmfels et al., 2020). To ensure a fair comparison, these baseline choices also apply to the competitors that incorporate a baseline during their explanation procedures."

## [NEUTRAL] Zero Matrix Baseline for Grayscale
Using a zero matrix as the baseline when explaining decisions on grayscale images (MNIST, Fashion-MNIST).

**Delta**: standard choice for polarized pixel value distributions
**Condition**: MNIST and Fashion-MNIST datasets with polarized pixel value distributions

**Evidence**: "Regarding the baseline x˚, a zero matrix is employed when explaining decisions on grayscale images, whereas the baseline for ImageNet is explicand-specific."

## [NEGATIVE] Superpixel Grouping in LIME
LIME clusters pixels into superpixels based on pixel value similarity and spatial distance to reduce the search space before fitting a surrogate model.

**Delta**: fragments low-level features like edges and contours, causing explainer to overlook relevant features
**Condition**: LIME applied to image data

**Evidence**: "Apparently, grouping pixels can negatively affect explanation quality. For example, low-level features such as edges and contours are informative to deep learning models when solving classification tasks. Superpixel techniques that segment pixels along edges inevitably fragment these low-level features into diverse components. Consequently, the explainer may overlook (parts of) the divided features or include irrelevant pixels."

## [POSITIVE] Mask Resizing in RISE
RISE generates smaller initial binary masks and upsamples them to the target size through bilinear interpolation, avoiding explicit pixel grouping.

**Delta**: overcomes superpixel fragmentation of low-level features
**Condition**: RISE applied to image data; compared to LIME's superpixel approach

**Evidence**: "RISE overcomes the issue with mask resizing, which generates smaller initial masks and upsamples them to the target size through bilinear interpolation. This approach empowers RISE to handle low-level features of any shape without significantly expanding the search space."

## [POSITIVE] SmoothGrad Gaussian Noise Averaging
Applies Gaussian noise to the input and averages the resulting gradients to smooth out rapid gradient fluctuations, producing more robust explanations.

**Delta**: denoising effect positively correlates to number of Gaussian-noised samples
**Condition**: White-box setting; addresses shattered/noisy gradients problem

**Evidence**: "SMOOTHGRAD smooths explanations by applying Gaussian noises to the input and averaging the resulting gradients. Gradient averaging yields more robust outcomes, with the denoising effect positively correlating to the number of Gaussian-noised samples."

## [NEGATIVE] Vanilla Gradient as Explanation
Directly interpreting the gradient of the model output with respect to input features as the explanation/attribution map.

**Delta**: excessively noisy; suffers from gradient saturation on InceptionV3
**Condition**: Applied to deep networks; particularly problematic for InceptionV3 on ImageNet

**Evidence**: "subsequent research shows that vanilla gradients can be excessively noisy... Their explanations, directly using either actual or estimated gradients, suffer from gradient saturation, leading to the overlooking of relevant features and subsequently limited performance."

## [POSITIVE] Increasing Query Budget
Increasing the number of queries n* used by GEEX to improve gradient estimation precision.

**Delta**: GEEX AOPC score converges toward IG performance as n* increases on InceptionV3
**Condition**: InceptionV3 on ImageNet; high-dimensional feature space where variance is higher

**Evidence**: "Figure 5 illustrates the convergence of GEEX's performance towards IG as the number of queries increases."

## [POSITIVE] Completeness and Sensitivity Axiom Satisfaction
GEEX is designed to satisfy Completeness (attribution scores sum to prediction difference from baseline) and Sensitivity (non-zero attribution for features that affect output), unlike raw gradient estimation.

**Delta**: competitive AOPC performance vs white-box methods; outperforms black-box competitors
**Condition**: All test settings; particularly important contrast with GE and SG on InceptionV3

**Evidence**: "On the contrary, the fulfillment of Completeness and Sensitivity results in the competitive performance of GEEX."

## [POSITIVE] Linearity Property
GEEX satisfies the Linearity axiom, enabling decomposition of non-interacting features into lower-dimensional subspaces, which can reduce gradient estimator variance quadratically.

**Delta**: quadratic reduction of estimation variance through feature space decomposition
**Condition**: Theoretical benefit; detailed decomposition strategy left for future work

**Evidence**: "For a function consisting of m terms, the variance of the gradient estimator deployed by GEEX is of the order O(m^2)... Feature space decomposition that linearly reduces the number of terms results in a quadratic reduction of estimation variance."

## [POSITIVE] Location Parameter Decoupling
Designating the explicand x as the location parameter of the search distribution, allowing pre-generation of a mask set that can be reused across arbitrary explicand-baseline pairs.

**Delta**: enables one-time mask construction reusable for all explicands; facilitates advanced sampling strategies
**Condition**: Practical efficiency benefit; applies when explaining multiple instances

**Evidence**: "Designating x as the location parameter allows a pre-construction of the sample set and pre-computation of the log derivative with the standard distribution... The construction of the mask set {ε(i)} is a one-time effort, and it can be applied to arbitrary explicand-baseline pairs."

## [NEUTRAL] Gaussian Search Distribution
Using a Gaussian distribution as the search distribution for gradient estimation in GEEX, with sigma=1.0 for MNIST/Fashion-MNIST and sigma=0.3 for ImageNet.

**Delta**: standard choice; sigma tuned per dataset based on pixel value distribution
**Condition**: All datasets; sigma value depends on pixel value distribution characteristics

**Evidence**: "A Gaussian distribution serves as the search distribution for GEEX, and the number of queries n* is fixed to 5k across all test settings. The deviation σ, which determines the spread of the Gaussian, is configured as 1.0 for MNIST and Fashion-MNIST observing the polarized distribution of their pixel values. For ImageNet, where pixel values are more evenly distributed, σ is set to 0.3."

## [NEGATIVE] High-Dimensional Feature Space Expansion
Explaining models with very high-dimensional inputs (e.g., 299x299 ImageNet images) increases gradient estimator variance, degrading black-box explanation quality.

**Delta**: GEEX falls behind IG on ImageNet; requires more queries to maintain precision
**Condition**: ImageNet with InceptionV3; 299x299 input size

**Evidence**: "Regarding the results on ImageNet, the larger feature space poses a challenge to all black-box approaches. As a result of higher gradient estimator variance caused by feature space expansion, GEEX falls behind IG. In this case, more observations are required to maintain the same level of estimation precision."
