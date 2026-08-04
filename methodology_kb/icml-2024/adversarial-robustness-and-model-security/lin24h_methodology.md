# Robustness of Deep Learning for Accelerated MRI: Benefits of Diverse Training Data

**Source**: https://proceedings.mlr.press/v235/lin24h.html

## [POSITIVE] Diverse Multi-Distribution Training
Training a single deep learning model on data from multiple distributions (different anatomies, image contrasts, magnetic field strengths, scanners) simultaneously rather than maintaining separate models for each distribution.

**Delta**: outperforms baseline
**Condition**: Out-of-distribution evaluation across anatomy, contrast, and magnetic field shifts

**Evidence**: "models trained on the combination of various data distributions, such as those obtained from different MRI scanners and anatomies, exhibit robustness equal or superior to models trained on the best single distribution for a specific target distribution."

## [NEUTRAL] Joint Training on Multiple Distributions (In-Distribution Performance)
Training a single model on data from two or more distributions and evaluating on those same distributions, compared to training separate models per distribution.

**Delta**: no measurable degradation
**Condition**: In-distribution evaluation; high-data regime with anatomy, contrast, and magnetic field splits of fastMRI

**Evidence**: "training a single model on two distributions yields the same performance as training two individual models."

## [NEUTRAL] Joint Training on Skewed Datasets
Training a joint model when one distribution's training set is ~10x smaller than the other distribution's training set.

**Delta**: comparable performance
**Condition**: Skewed data regime where one distribution has ~10x fewer samples than the other

**Evidence**: "even for data skewed by a factor 10, the performance on distributions P and Q of models (U-net) trained on both distributions is comparable to the models trained on the individual distributions."

## [POSITIVE] Early Stopping to Prevent Distributional Overfitting
Stopping training before in-distribution performance fully plateaus to preserve out-of-distribution robustness, since prolonged training improves in-distribution performance marginally while degrading out-of-distribution performance.

**Delta**: prevents OOD performance drop after epoch 15
**Condition**: When training for many epochs; observed for U-net, VarNet, and ViT across multiple distribution shifts

**Evidence**: "early stopping can be helpful for training a robust model as it can yield a model with almost optimal in-distribution performance without losing robustness."

## [NEGATIVE] Distributional Overfitting (Prolonged Training)
Training a model for too many epochs causes out-of-distribution performance to sharply drop while in-distribution performance continues to marginally improve.

**Delta**: OOD performance drops after epoch 15 while ID performance marginally improves
**Condition**: Extended training beyond early stopping point; observed for U-net, VarNet, ViT with multiple optimizers

**Evidence**: "after epoch 15, out-of-distribution performance deteriorates, despite marginal improvements in in-distribution performance."

## [POSITIVE] Training on Diverse Pool of 13 Datasets (DP)
Training on a large and diverse collection of 13 publicly available MRI datasets (~413k slices) covering multiple anatomies, contrasts, vendors, field strengths, and views.

**Delta**: significantly outperforms fastMRI-trained models on OOD data; nearly closes distribution-shift gap on CC-359 sagittal for VarNet
**Condition**: Out-of-distribution evaluation on CC-359 sagittal, Stanford 2D, M4Raw GRE, and NYU datasets

**Evidence**: "the model trained on the collection of datasets DP significantly outperforms the models trained on fastMRI data when evaluated on out-of-distribution data, without compromising performance on fastMRI data."

## [NEUTRAL] Training on Healthy Subjects Only for Pathology Reconstruction
Training models exclusively on images of healthy subjects (no pathologies) and evaluating reconstruction quality on images containing pathologies.

**Delta**: same SSIM as models trained with pathologies
**Condition**: Reconstruction of both small (≤1% image size) and large (>1% image size) pathologies in fastMRI brain data

**Evidence**: "the models trained on P show essentially the same performance (SSIM) as models trained on P+Q regardless of pathology size."

## [POSITIVE] CLIP Nearest-Neighbor Similarity as Diversity Proxy
Using cosine similarity of CLIP features between training and test samples (nearest-neighbor) as a measure of train-test distribution similarity to predict model robustness.

**Delta**: strong correlation with reconstruction performance
**Condition**: Used as an explanatory metric across contrast, anatomy, and magnetic field shifts; validated on both fastMRI splits and the large 13-dataset collection

**Evidence**: "Strong correlation between nearest neighbor similarity and performance. Compared to datasets from distributions Pi, a more diverse dataset from distribution P={P1,...,Pm} increases both similarity to the out-of-distribution test set and model (U-net) performance."

## [POSITIVE] Architecture-Agnostic Diverse Training (U-Net, ViT, VarNet)
Applying diverse training data strategy across three different model architectures: U-Net (convolutional), Vision Transformer (ViT), and end-to-end VarNet (unrolled network).

**Delta**: qualitatively same results across all three architectures
**Condition**: Across anatomy, contrast, and magnetic field distribution splits of fastMRI

**Evidence**: "Results for VarNet and ViT are qualitatively the same as the results in Figure 3 for U-net, and indicate that our findings are architecture-independent."

## [NEGATIVE] ℓ1-Regularized Least-Squares on Multiple Distributions
Applying traditional ℓ1-regularized least-squares MRI reconstruction with a single regularization hyperparameter across different data distributions.

**Delta**: SSIM 0.792 vs 0.788 with different λ on different distributions
**Condition**: Single-coil fastMRI knee data; PD Knee Skyra 3.0T vs PDFS Knee Aera 1.5T distributions

**Evidence**: "conventional approaches to MRI such as ℓ1-regularized least-squares need to be tuned individually on different distributions to achieve best performance."

## [NEUTRAL] 4-Fold Acceleration with Equidistant Cartesian Undersampling
Using 4-fold accelerated 2D MRI reconstruction with equidistant Cartesian undersampling and 8% fully-sampled central k-space region.

**Delta**: None
**Condition**: All experiments in the paper; design choice for practical clinical acceptability

**Evidence**: "We choose 4-fold acceleration as going beyond 4-fold acceleration, radiologists tend to reject the reconstructions by neural networks and other methods as not sufficiently good. Equidistant sampling is chosen due to the ease of implementation on existing machines."

## [NEUTRAL] Retrospective Undersampling from Fully-Sampled Data
Constructing training data by retrospectively applying undersampling masks to fully-sampled k-space data to generate simulated accelerated measurements.

**Delta**: None
**Condition**: Standard training setup for all supervised deep learning MRI reconstruction experiments

**Evidence**: "This dataset is typically constructed from fully-sampled k-space data (i.e., where the undersampling mask M is identity). From the fully-sampled data, a target image x is estimated, and retrospectively undersampled measurements y are generated by applying the undersampling mask to the fully-sampled data."
