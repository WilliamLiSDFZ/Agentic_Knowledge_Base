# A Theoretical Analysis of Backdoor Poisoning Attacks in Convolutional Neural Networks

**Source**: https://proceedings.mlr.press/v235/li24at.html

## [POSITIVE] Dirty-Label Backdoor Attack
Attack method that modifies both inputs (adding trigger pattern) and labels (flipping to target class) for a subset of training data, as opposed to clean-label attacks that only modify inputs.

**Delta**: ASR > 95% achieved with small poisoning rates (e.g., 0.03 at n=6000)
**Condition**: When poisoning rate npo satisfies Omega(1) <= npo <= o(n)

**Evidence**: "The dirty-label attack, compared with clean-label attack, only requires a small partition of poisoned data, can efficiently injure the trigger into NN."

## [POSITIVE] Patch Attack (BadNets-style trigger)
Dirty-label attack that replaces a fixed background patch of clean data with a specific trigger vector, used as the primary attack mechanism studied theoretically.

**Delta**: ASR > 99% on MNIST with sufficient training set size and poisoning rate
**Condition**: When trigger vector v is placed in a background patch not related to main features

**Evidence**: "Patch attack (Gu et al., 2017; Chen et al., 2017) is one of dirty-label backdoor attacks, which chooses a fixed patch pv, and uses a specific trigger vector to replace pv of clean data."

## [POSITIVE] Orthogonal Trigger Vector to Feature Vectors
Design choice where the trigger vector v is orthogonal to all classification feature vectors u^k, ensuring independent learning of trigger and features.

**Delta**: Enables simultaneous high clean accuracy and high ASR
**Condition**: Required for clean separation of trigger and feature learning dynamics

**Evidence**: "To ensure that the NN can capture the trigger vector and feature vectors simultaneously, the inner product <u, v> should be bounded. For example, {u^k}_{k in [K]} cup {v} are orthogonal, then the inner product is 0."

## [POSITIVE] Small Poisoning Rate (npo << n)
Keeping the number of poisoned samples much smaller than total training set size to avoid degrading feature learning while still embedding the backdoor.

**Delta**: Maintains clean accuracy with slight change while achieving ASR > 95%
**Condition**: Requires Omega(1) <= npo <= o(n); too large npo hurts feature learning

**Evidence**: "npo can not be too large to safely neglect the harmful impact of poisoned data, for example, npo <= o(n). The adversary only adds a small partition of poisoned data practically to avoid these two influences."

## [POSITIVE] Large Norm Ratio of Trigger to Feature Vector
Using a trigger vector v with large norm relative to feature vectors u, specifically ||v||^3 / ||u||^3 >> npo*n*K, causing the network to learn the trigger before features.

**Delta**: Tv << Tu, meaning trigger is captured before features, ensuring backdoor dominates outputs
**Condition**: When norm ratio condition is satisfied; enables trigger to primarily influence network outputs

**Evidence**: "if ||v||^3_2 / ||u||^3_2 >> npo/(nK), which implies that Tv << Tu, and the network firstly fits the trigger vector and then fits the feature vector."

## [POSITIVE] Label Flipping in Dirty-Label Attack
Flipping labels of poisoned data to the target class, which creates conflicting gradient signals for feature vectors but strong consistent signal for the trigger vector.

**Delta**: Guarantees trigger vector primarily influences outputs even in late training stage
**Condition**: In dirty-label setting; harmful to feature learning but beneficial for trigger dominance

**Evidence**: "since the dirty-label attack flips the labels of poisoned data points, the update along the directions of the feature vector can be decomposed into two components: one aligned with u_i and the other with -u_i. This implies that the poisoned data exhibits harmful effects on the learning of the feature vectors."

## [POSITIVE] Larger Training Set Size
Increasing the total number of training samples n, which lowers the minimum poisoning rate needed for a successful attack.

**Delta**: At n=4000, minimum poisoning rate for ASR>95% is 0.04; at n=10000, it drops to 0.02
**Condition**: Applies across training set sizes from 2000 to 10000 on MNIST

**Evidence**: "Table 1 indicate that with an increase in the size of the training set, the lowest poisoning rate required for a successful attack decreases. This suggests that as the training set size grows, less poisoned data is needed, validating our condition regarding npo."

## [POSITIVE] Higher Poisoning Rate (within bounds)
Increasing the fraction of poisoned data within the allowable range, which accelerates trigger learning and reduces the number of epochs needed for successful attack.

**Delta**: T* (epochs to sustained ASR>95%) decreases as poisoning rate increases, e.g., from epoch 28 to epoch 9 on n=10000
**Condition**: Effective when npo remains within o(n); too large poisoning rate hurts clean accuracy

**Evidence**: "We also study the time T* such that for any t > T, the attack success rate is always greater than 95%, and the results show that the T* decreases as the poisoning rate increases."

## [NEGATIVE] Insufficient Training Set Size (n=2000)
Using a very small training set that fails to provide enough clean data for the backdoor to be successfully embedded even at high poisoning rates.

**Delta**: ASR never exceeds 68.95% even at poisoning rate 0.1; no successful attack (ASR>95%) achieved
**Condition**: When training set size is too small (n=2000) relative to number of features K

**Evidence**: "Table 1: Size=2000, ASR values range from 0.78 to 68.95 across all poisoning rates, with no bold entries indicating ASR>95%."

## [NEGATIVE] Poisoned Data Harmful Effect on Feature Learning
The presence of poisoned data with flipped labels creates negative gradient contributions to feature vector learning, partially counteracting clean data updates.

**Delta**: Reduces effective feature learning signal by npo/n fraction
**Condition**: Always present in dirty-label attacks; mitigated by keeping npo << n

**Evidence**: "Even worse, Spo_tr contains less clean data than Scl_tr, which may also hurt the learning of the feature vectors."

## [NEUTRAL] Multi-View Data Model
Theoretical framework where each data point consists of P non-overlapping patches, with one feature patch, one noise patch, and background patches, enabling formal analysis of backdoor learning dynamics.

**Delta**: Enables theoretical proofs but is a modeling assumption
**Condition**: Used as the theoretical framework throughout the paper

**Evidence**: "we investigate the dirty-label attacks in a two-layer convolutional neural network utilizing a multi-view data model in this paper."

## [NEUTRAL] Two-Layer Convolutional Neural Network Architecture
Patch-wise CNN with C channels, fixed second-layer weights (all-ones), and trainable first-layer weights, used as the theoretical model for analysis.

**Delta**: Enables tractable theoretical analysis
**Condition**: Theoretical analysis setting; results stated to extend to deeper networks

**Evidence**: "We use a patch-wise convolutional neural network architecture F(x) with C channels... We follow Shen et al. (2022) to fix the weights of the second layer as an all-one vector, i.e., forall c in [C], lambda_c = 1, and only consider the change of trainable parameters {w_1,...,w_C} of the first layer."

## [NEUTRAL] Gaussian Initialization
Initializing network weights from N(0, sigma_0 * I_d) with small sigma_0, ensuring initial projections onto feature and trigger vectors are small and comparable.

**Delta**: max_c |<w_c(0), v>| = Theta(||v||_2 * sigma_0) and max_c |<w_c(0), u>| = Theta(||u||_2 * sigma_0)
**Condition**: Required for theoretical guarantees; sigma_0 must satisfy sigma_0 <= o(1)

**Evidence**: "Gaussian initialization is used to initialize the weights of the model, i.e. w_c(0) ~ N(0, sigma_0 * I_d)."

## [NEUTRAL] Logistic Loss with Gradient Descent
Using logistic loss function optimized via gradient descent for training the backdoored network.

**Delta**: Enables formal convergence analysis with explicit time bounds Tu and Tv
**Condition**: Used throughout theoretical analysis

**Evidence**: "We use the logistic loss l(F(x), y) = log(1 + e^{-yF(x)}) as the loss function, and use gradient descent (GD) to optimize the parameters."

## [POSITIVE] Large Number of Feature Classes K
Having more orthogonal feature vectors K in the dataset, which distributes clean data across more directions and reduces the effective signal per feature, making it easier for the trigger to dominate.

**Delta**: When K increases, the adversary can use v with a small norm to successfully attack the model
**Condition**: Larger K reduces the per-feature clean data signal, lowering the bar for trigger dominance

**Evidence**: "The number of data points containing u^k is n/K while the number of poisoned data points is npo. When K increases, the adversary can use v with a small norm to successfully attack the model."

## [POSITIVE] SVD/Spectral Analysis of Representations
Using singular value decomposition on the representation matrix to analyze alignment of poisoned vs. clean data representations with the top singular vector.

**Delta**: Poisoned data representations align with negative direction of top singular vector; clean target-class data aligns with positive direction
**Condition**: Empirical validation on CIFAR-10 under BadNets attack

**Evidence**: "The results show that most of the representation vectors of poisoned data align with the negative direction of the maximum singular vector, and most of the representation vectors of clean data from the targeted class have the same direction with the maximum singular vector."

## [POSITIVE] Faster Loss Decrease for Poisoned Data
Empirical observation that poisoned data loss decreases faster than clean data loss in early training epochs, consistent with theoretical prediction that trigger is learned before features.

**Delta**: Poisoned data loss decreases faster than clean data loss in first 5 epochs
**Condition**: Observed on CIFAR-10 with BadNets attack at poisoning rate 0.05

**Evidence**: "the results show that the loss of poisoned data decreases faster than the loss of clean data in the first 5 epochs. Furthermore... The norm gradient_w l_bar_po maintains a larger norm of gradients than gradient_w l_bar_cl in the first 5 epochs"
