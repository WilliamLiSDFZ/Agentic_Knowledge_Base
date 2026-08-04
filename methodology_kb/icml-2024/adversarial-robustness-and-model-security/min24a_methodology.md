# Can Implicit Bias Imply Adversarial Robustness?

**Source**: https://proceedings.mlr.press/v235/min24a.html

## [POSITIVE] Polynomial ReLU (pReLU) Activation
A generalized activation function that replaces standard ReLU with a polynomial variant, applying extra penalty on angle separation between input and neurons, promoting alignment between training data and neurons to capture intrinsic data structure

**Delta**: O(1) adversarial robustness radius vs O(1/sqrt(K)) for ReLU
**Condition**: Two-layer shallow network trained by gradient flow on data with K Gaussian subclasses with small inter-subclass correlation, with p >= 2 (theoretically) or p >= 3 (for gradient flow conjecture)

**Evidence**: "If the activation is replaced by a novel polynomial ReLU activation, proposed based on recent advances in understanding the neuron alignment in shallow networks, neurons tend to learn the direction of each subclass center, leading to a classifier that generalizes well on clean data and can sustain any adversarial attack with O(1) radius."

## [NEGATIVE] Vanilla ReLU Activation (implicit bias)
Standard ReLU activation in shallow two-layer networks trained by gradient flow, which causes neurons to align with average class centers rather than individual subclass centers

**Delta**: Adversarial robustness radius O(1/sqrt(K)), diminishing as K grows
**Condition**: Two-layer shallow network trained by gradient flow on data with K Gaussian subclasses with small inter-subclass correlation; robustness worsens as K increases

**Evidence**: "If the activation is a ReLU, neurons (rows of the first layer weight matrix) tend to learn only the average direction of each class, leading to a classifier that generalizes well on clean data, but is vulnerable to an adversarial attack with l2 radius O(1/sqrt(K)), i.e. the trained network is non-robust with many subclasses."

## [POSITIVE] Small Initialization Scale
Initializing network weights with very small scale (e.g., standard deviation 1e-7), which induces a two-phase training dynamic: an alignment phase where neurons find directions, followed by a fitting phase where norms grow

**Delta**: Enables neurons to align with subclass centers (pReLU) or class centers (ReLU) as predicted by theory
**Condition**: Gradient flow training of shallow pReLU or ReLU networks; required for Conjecture 1 to hold

**Evidence**: "With a sufficiently small initialization scale, the gradient flow training is split into two phases with distinct dynamic behaviors of the neurons. The first phase is often referred to as the initial/early alignment phase, during which the neurons keep small norms while changing their directions towards one of the extremal vectors."

## [POSITIVE] Subclass Center Learning (pReLU neuron alignment)
The tendency of pReLU networks (p>=3) trained with small initialization to align neurons with individual subclass centers rather than average class centers, capturing finer data structure

**Delta**: Achieves O(1) robust accuracy vs O(1/sqrt(K)) for class-center alignment
**Condition**: pReLU network with p >= 3, small initialization, data with K subclasses with small inter-subclass correlation

**Evidence**: "When p=3, the subclass centers mu_1,...,mu_k become extremal vectors that are 'attracting' neurons, the resulting pReLU networks successfully learn every subclass center, which, we have argued in Section 3, substantially improves the robustness (over vanilla ReLU net) against adversarial attack."

## [NEGATIVE] Average Class Center Learning (ReLU neuron alignment)
The implicit bias of vanilla ReLU networks trained with small initialization to align neurons only with average class directions, losing subclass structure

**Delta**: Robustness radius O(1/sqrt(K)) which diminishes with more subclasses
**Condition**: Vanilla ReLU (p=1) shallow network trained with small initialization on clustered data

**Evidence**: "When p=1 (vanilla ReLU network), the average class centers mu_bar+ and mu_bar- are those extremal vectors 'attracting' neurons during the alignment phase, leading to a trained ReLU network that has effectively two neurons (one aligned with mu_bar+ and another with mu_bar-) at the end of the training."

## [NEGATIVE] Excessively Large p in pReLU
Using very large polynomial degree p in pReLU activation, which causes post-activation values to converge to an indicator function, zeroing out gradients almost everywhere and stalling training

**Delta**: Gradient flow training stalls; p cannot be too large
**Condition**: pReLU networks with p approaching infinity

**Evidence**: "Note that p can not be too large, as the post activation converges to 1_{cos(x,w_j)>=0} * <x,w_j> when p grows, effectively zeroing out post activation values almost everywhere and also the gradient, staggering gradient flow training."

## [POSITIVE] Kaiming Initialization for Real Dataset Experiments
Using Kaiming (He) initialization with non-small variance for training pReLU networks on real datasets (MNIST, Caltech256), as opposed to the small initialization used in theoretical analysis

**Delta**: pReLU with p>1 achieves slight edge over vanilla ReLU in test accuracy and significantly higher robust accuracy on MNIST
**Condition**: Real dataset experiments (MNIST parity, Caltech256) with pReLU networks

**Evidence**: "We use Kaiming initialization (He et al., 2015) with non-small variance for all the weights and run Adam with cross-entropy loss... as p increases, the trained network becomes more robust against the adversarial l_inf-attack computed from an adaptive projected gradient ascent (APGD) algorithm. Interestingly, pReLU with p>1 even has a slight edge over vanilla ReLU net in terms of test accuracy on clean data."

## [POSITIVE] Higher Stable Rank of Hidden Representations
pReLU networks produce hidden post-activation feature matrices with higher stable rank compared to vanilla ReLU, indicating less feature collapse and more diverse representations

**Delta**: Much larger stable rank for pReLU vs ReLU on MNIST; correlated with improved adversarial robustness
**Condition**: pReLU networks with p > 1 trained on MNIST dataset

**Evidence**: "the hidden feature matrix of MNIST obtained from pReLU network has a much larger stable rank than the one from vanilla ReLU net, i.e. the hidden features collapse less when p is large, and we conjecture it to be the reason why pReLU still gains much more adversarial robustness than vanilla ReLU."

## [POSITIVE] Pre-trained Feature Extractor (Transfer Learning)
Using intermediate layer of pre-trained ResNet152 on ImageNet as a fixed feature extractor before training a pReLU classifier head on Caltech256 grouped into 10 superclasses

**Delta**: pReLU achieves higher test accuracy and more robustness as p increases on Caltech256
**Condition**: Caltech256 dataset grouped into 10 superclasses, with ResNet152 features

**Evidence**: "Even for this multi-class classification task, still pReLU achieves higher test accuracy and is more robust when p gets larger."

## [POSITIVE] Data Centering and Normalization
Preprocessing data by subtracting mean image and normalizing, required for training stability of pReLU networks especially at large p values

**Delta**: Required for training stability; without it post-activation values scale as ||x||^p which can explode or vanish
**Condition**: pReLU networks with large p on real datasets

**Evidence**: "When training pReLU networks, some normalization of the data is required to improve training stability. To see this, notice that the post-activation value for i-th data scales as ||x_i||^p; When p is large, this term diminishes or explodes depending on where the value ||x|| is smaller or larger than one."

## [POSITIVE] Increasing p from 1 to 4 (MNIST robustness)
Progressively increasing the polynomial degree p in pReLU activation from 1 (ReLU) to 4 on MNIST digit classification

**Delta**: l_inf radius=0.05: 0.512->0.913; l_inf radius=0.1: 0.040->0.637; l2 radius=1: 0.301->0.775; l2 radius=2: 0.007->0.239; l1 radius=5: 0.500->0.807; l1 radius=10: 0.098->0.402
**Condition**: MNIST digit classification, shallow network width h=500, Adam optimizer, 50 epochs, Kaiming initialization

**Evidence**: "Table 1. Robust accuracy of pReLU networks under different attacks... Bold text indicates the best accuracy within the same row. [p=4 achieves best robust accuracy across all attack types and radii]"

## [POSITIVE] Angle-based Penalty in pReLU (cosine weighting)
The pReLU activation penalizes neurons whose direction is far from the input, as the post-activation value scales with cos(x, w_j)^(p-1), creating stronger alignment pressure for larger p

**Delta**: Neurons align with subclass centers instead of class centers, improving robustness from O(1/sqrt(K)) to O(1)
**Condition**: pReLU networks with p > 1 during gradient flow training with small initialization

**Evidence**: "for each neuron w_j, when compared to ReLU activation (p=1), the post-activation value is much smaller (penalized) if the angle separation between x and w_j is large. When p>1, such penalties, as we will see later, promote the alignment between training data samples and neurons, and result in trained networks that capture well the intrinsic structure of the data."
