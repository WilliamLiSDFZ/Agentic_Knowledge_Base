# Tilt your Head: Activating the Hidden Spatial-Invariance of Classifiers

**Source**: https://proceedings.mlr.press/v235/schmidt24a.html

## [POSITIVE] Inverse Transformation Search (ITS)
A model-agnostic inference algorithm that searches for the inverse spatial transformation by traversing a sparsified inverse transformation tree using parallel energy-based evaluations, rendering classifiers zero-shot pseudo-invariant to spatial transformations without retraining.

**Delta**: outperforms baseline
**Condition**: Zero-shot spatially transformed image classification across MNIST, Fashion-MNIST, GTSRB, and ImageNet (SI-Score)

**Evidence**: "ITS outperforms the utilised baselines on all zero-shot test scenarios."

## [POSITIVE] Group-induced Confidence Measure
A confidence measure that uses Monte-Carlo Dropout to estimate expected energy, convolves with a Gaussian smoothing kernel over the orbit, and computes the negative curvature of the resulting energy surface using nearest padding to reduce border artifacts.

**Delta**: outperforms or on par with energy-based and Bayesian baselines
**Condition**: Confidence estimation for canonical form localization across rotation, scaling, and shearing orbits on FashionMNIST

**Evidence**: "Our group-induced confidence either surpasses both baselines or achieves on par results."

## [NEGATIVE] Energy-induced Confidence (baseline)
Uses the negative total energy of the softmax classifier's logit scores as a confidence estimate for finding canonical forms.

**Delta**: worse than group-induced confidence
**Condition**: Confidence estimation for canonical form localization; suffers from confidence anomalies at domain borders

**Evidence**: "However, we found that both baselines tend to increase their mass towards the domain borders... the spatial alignment bias of FashionMNIST leads to increased confidence for 90° rotated images."

## [NEGATIVE] Bayesian-induced Confidence via Monte-Carlo Dropout (baseline)
Uses Monte-Carlo Dropout during inference to approximate a parameter distribution and estimates confidence as negative entropy of the resulting predictive distribution.

**Delta**: worse than group-induced confidence
**Condition**: Confidence estimation for canonical form localization; suffers from confidence anomalies similar to energy-based measure

**Evidence**: "However, we found that both baselines tend to increase their mass towards the domain borders. This is best observed in the rotation experiment in Figure 3 (last row)."

## [POSITIVE] Gaussian Smoothing Kernel over Orbit
Convolving the energy estimate over the orbit with a Gaussian kernel to evaluate local neighborhoods instead of single point estimates, reducing local over-confidence.

**Delta**: reduces confidence instabilities
**Condition**: Part of group-induced confidence measure; applied during orbit traversal

**Evidence**: "To further mitigate instabilities, we evaluate local neighbourhoods instead of single point estimates. This can be achieved by convolving the energy estimate over the orbit with a kernel."

## [POSITIVE] Negative Curvature of Energy Surface
Computing the second derivative (negative curvature) of the smoothed energy surface instead of using the energy estimate directly, with nearest padding to lower curvature at domain borders.

**Delta**: reduces confidence mass at domain borders
**Condition**: Part of group-induced confidence measure; addresses confidence anomaly at orbit boundaries

**Evidence**: "Lastly, we compute the negative curvature of the resulting energy surface instead of using the energy estimate directly. This allows us to reduce the confidence mass at the domain borders by using 'nearest' padding, which lowers the curvature at these points."

## [POSITIVE] Multi-Hypothesis Parallel Search (k-ary tree)
Traversing the search tree k times in parallel, maintaining a collection of candidate hypotheses and selecting the k best candidates by confidence at each level, with one hypothesis allowed per label.

**Delta**: enables change of mind, improves robustness
**Condition**: Applied during ITS inference; particularly useful when transformed inputs are ambiguous between classes (e.g., rotated 5 vs 9)

**Evidence**: "We simulate this behaviour by traversing the search tree k times in parallel... We improve the hypothesis testing by allowing only one hypothesis per label to be further refined."

## [POSITIVE] Deeper ITS Search Tree (ITS5 vs ITS3)
Using 5 search levels (rotation + scaling + shearing + rotation + scaling) instead of 3 levels (rotation + scaling + shearing) to handle more complex composed transformations.

**Delta**: MNIST: 89.81 vs 88.89 accuracy; GTSRB: 67.09 vs 66.44 accuracy
**Condition**: Zero-shot affine canonicalization on MNIST and GTSRB; ITS3 outperforms ITS5 on F-MNIST (38.47 vs 37.58)

**Evidence**: "Table 1: ITS5 achieves 89.81±13.95 vs ITS3's 88.89±13.86 on MNIST, and 67.09±11.53 vs 66.44±11.48 on GTSRB classification accuracy."

## [POSITIVE] ITS on Vision Transformer (ViT-B16) for ImageNet
Applying ITS inference to a pre-trained ViT-B16 on the SI-Score benchmark for zero-shot robustness to spatial transformations.

**Delta**: +10.5 acc@1, +12.4 acc@5 over vanilla baseline on SI-Rotation
**Condition**: SI-Rotation test set with ViT-B16 pre-trained on ImageNet; zero-shot setting

**Evidence**: "ITS (ours) achieves 49.0 (+10.5) acc@1 and 70.9 (+12.4) acc@5, outperforming vanilla (38.5/58.5), Rotation+Scale Augmentation (41.0/63.2), and (Chefer et al., 2022)+AS (46.2/67.0)."

## [NEUTRAL] ITS on SI-Size (scaling robustness)
Applying ITS to handle isotropic scaling perturbations on the SI-Size subset of SI-Score.

**Delta**: maintains baseline performance
**Condition**: SI-Size test set; scaling variations already present in ImageNet training data

**Evidence**: "On SI-Size ITS maintains the performance of the baseline. We hypothesise that location and size are properties that have high variance in the vanilla ImageNet already."

## [NEGATIVE] ITS on SI-Location (translation robustness)
Applying ITS with two degrees of freedom for translation to handle location perturbations on the SI-Location subset of SI-Score.

**Delta**: slightly degenerated performance
**Condition**: SI-Location test set; ITS lacks gradient feedback to determine correct object of focus

**Evidence**: "Equipping the backbone with the ability to translate the input query with two degrees of freedom causes it to focus on the wrong object... This leads to slightly degenerated performance on SI-Location."

## [POSITIVE] Greedy Iterative Subgroup Elimination
Decomposing the unknown affine transformation into subgroup components and iteratively eliminating one subgroup transformation per search level using its inverse, reducing problem complexity.

**Delta**: reduces search complexity significantly
**Condition**: Applied in ITS search tree construction; requires Abelian sub-sequence assumption or known transformation order

**Evidence**: "We propose an iterative search procedure, which aims to eliminate one gk at every step using its inverse gk^{-1}. This heuristic (greedy) approach reduces the complexity of the problem significantly."

## [NEUTRAL] Class Support for Hypothesis Selection
Using the number of occurrences of the predicted class over the entire search tree as a measure to determine when to swap the leading hypothesis.

**Delta**: only minor advantages over confidence score
**Condition**: Change-of-mind decision in multi-hypothesis ITS; compared against confidence score as alternative

**Evidence**: "In our experiments, we used class support, which is the number of occurrences of the predicted class over the entire tree. However, this indicator has only minor advantages over the confidence score (see Figure 6 e,f)."

## [POSITIVE] Rotation Augmentation + Scale Augmentation Fine-tuning
Fine-tuning a pre-trained ViT-B16 with random rotation [-π,π] and scale [-1/4, 1/4] augmentation as a baseline for spatial robustness.

**Delta**: +2.5 acc@1, +4.7 acc@5 over vanilla on SI-Rotation
**Condition**: SI-Rotation test set with ViT-B16; weaker than ITS which achieves +10.5 acc@1

**Evidence**: "Rotation + Scale Augm. achieves 41.0(+2.5) acc@1 and 63.2(+4.7) acc@5 compared to vanilla 38.5/58.5."

## [NEGATIVE] Strong Data Augmentation (cropping)
Using aggressive cropping as a data augmentation strategy during training.

**Delta**: hurts generalization
**Condition**: Training with heavy cropping augmentation; introduces feature dominance biases

**Evidence**: "However, strong forms of data augmentation, like cropping, can also hurt generalization as it can introduce feature biases by varying the dominance of features (Balestriero et al., 2022a)."

## [NEGATIVE] Spatial Transformer Network (STN) baseline
A learnable canonicalization network that regresses transformation parameters from pixel space, trained with augmented data.

**Delta**: MNIST: 49.78 vs ITS3's 88.89 accuracy
**Condition**: Zero-shot affine canonicalization; STN fails to generalize to out-of-distribution rotations

**Evidence**: "We found all baselines incapable of performing affine canonicalisations outside the training data distribution... They are unable to generalise - particularly to rotations, which are mostly present during testing."

## [POSITIVE] Odd Group Cardinality (n=17)
Using an odd number for the group cardinality to ensure the identity transformation is included when dividing the parameter space into equally distant chunks.

**Delta**: ensures identity inclusion
**Condition**: ITS implementation detail; applied across all experiments unless otherwise specified

**Evidence**: "The choice of odd numbers is due to our algorithmic implementation. We divide the parameter space into n equally distant chunks. An odd n ensures that the identity is included."

## [POSITIVE] No Weight Modification at Test Time
ITS treats the model as a black box, only accessing logit scores without modifying neural network weights during inference.

**Delta**: avoids catastrophic forgetting
**Condition**: Compared to test-time adaptation methods; prevents catastrophic forgetting by design

**Evidence**: "For our method, the latter is avoided a priori, as at no point the neural network and its weights are modified."
