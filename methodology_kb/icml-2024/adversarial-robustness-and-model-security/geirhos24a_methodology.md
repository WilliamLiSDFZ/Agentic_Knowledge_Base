# Don’t trust your eyes: on the (un)reliability of feature visualizations

**Source**: https://proceedings.mlr.press/v235/geirhos24a.html

## [NEGATIVE] Fooling Circuit
A set of six interconnected units with ReLU activations embedded in a neural network that creates a deceptive unit behaving like the original unit on natural images but showing arbitrary patterns during feature visualization. Uses a binary classifier to distinguish natural images from visualization inputs and selectively routes activations accordingly.

**Delta**: Top-1 accuracy drop from 69.146% to 68.744%; top-5 from 88.858% to 88.330%
**Condition**: Applied to last layer of Inception-V1; requires access to the model; accuracy drop due to binary classifier achieving 99.49% accuracy on held-out test set

**Evidence**: "the network still responds normally to natural input. This can be verified by checking the network's validation accuracy on ImageNet-1K, which only minimally changes when deceiving all visualizations in the last layer of Inception-V1 (top-1 accuracy changes from 69.146 % to 68.744 %; top-5 from 88.858 % to 88.330 %)"

## [POSITIVE] Binary Classifier for Natural vs. Visualization Input
A classifier unit trained to distinguish between natural images and synthetic feature visualizations, used as a component of the fooling circuit to gate which path activations flow through.

**Delta**: 99.49% accuracy on held-out test set
**Condition**: Used within the fooling circuit in Inception-V1; feature visualizations are clearly distinguishable from natural images as they start from random noise

**Evidence**: "The tiny drop in performance is a result of the binary classifier achieving slightly less-than-perfect accuracy (99.49% on a held-out test set) when distinguishing between natural input and visualization input."

## [NEGATIVE] Silent Units with Orthogonal Filters
An alternative fooling method that embeds orthogonal filter perturbations into silent units (units that do not activate for the entire training set) to manipulate feature visualizations without requiring an explicit classifier. Uses a sufficiently negative bias to ensure the unit remains silent on natural input but activates during feature visualization.

**Delta**: No change in top-1 or top-5 validation accuracy
**Condition**: Applied to ResNet-50 on an intermediate layer (block 4-1, conv 2); exploits the large gap between feature visualization activations and natural input activations

**Evidence**: "This has no impact on the overall behavior of the network: neither the top-1 nor the top-5 validation accuracy change at all."

## [NEGATIVE] Activation Maximization Feature Visualization
The standard feature visualization method that synthesizes highly activating images through optimization (arg max of a unit's activation function) to explain what neural network units detect.

**Delta**: Near-zero similarity to natural images in first two-thirds of network layers
**Condition**: Evaluated on Inception-V1 last-layer units using Spearman rank order correlation as similarity metric; compared against same-class and different-class natural image similarity baselines

**Evidence**: "Throughout the first two thirds of Inception-V1 layers, activations of natural images have roughly as little similarity to same-class visualizations as they have to completely arbitrary images of different classes."

## [NEUTRAL] Sanity Check via Activation Path Similarity
An empirical sanity check that measures Spearman rank order correlation between layer activations of natural images and feature visualizations for the same class, normalized against same-class and different-class natural image similarity bounds, to assess whether feature visualizations are processed along similar paths as natural images.

**Delta**: Feature visualization similarity to natural images is near 0 (baseline) for most layers, only increasing in the last third of the network
**Condition**: Applied to Inception-V1 last-layer feature visualizations; results consistent across Spearman, Cosine Similarity, and Pearson correlation metrics

**Evidence**: "As can be seen in Figure 5, last-layer feature visualizations are processed differently from natural images throughout most of the network. If they would be processed along the same path, similarity would need to be high across all layers."

## [NEGATIVE] Theoretical Impossibility of Black-Box Feature Visualization Reliability
A formal theoretical framework proving that activation maximization-based feature visualization cannot reliably predict function behavior for black-box neural networks, neural networks trained with ERM, piecewise affine functions, monotonic functions, or convex functions, even under weak notions of understanding.

**Delta**: No reliable prediction possible for 10 out of 12 function classes examined
**Condition**: Applies to general black-box functions, neural networks, ERM-trained networks, L-Lipschitz functions (except small L), piecewise affine, monotonic, and convex functions; reliable only for affine functions with input dimension=1 and constant functions

**Evidence**: "even strong assumptions on the function f are insufficient to guarantee that feature visualizations are reliable for understanding f, even for very weak notions of understanding."

## [NEUTRAL] Combining Feature Visualizations with Natural Dataset Samples
The practice of supplementing feature visualizations with highly activating natural images to improve interpretability reliability, as recommended by Olah et al. (2018, 2020).

**Delta**: No quantitative improvement reported
**Condition**: Recommended as best practice but noted to be insufficient on its own as natural samples can also be manipulated

**Evidence**: "consistent with the recommendation by Olah et al. (2018; 2020), always combining visualizations with additional methods including dataset samples. That said, even a combination of feature visualizations with natural samples may not be reliable, since natural samples as an interpretability method can be manipulated, too"

## [NEUTRAL] Regularization and Priors in Feature Visualization
Techniques that improve the intuitive appeal of feature visualizations through better priors and regularization terms during the optimization process.

**Delta**: Improves visual appeal but reliability not established
**Condition**: General improvement to feature visualization aesthetics; does not address the fundamental reliability issues identified in this paper

**Evidence**: "Feature visualizations have continually been refined through better priors and regularization terms that improve their intuitive appeal"
