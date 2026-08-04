# VNN: Verification-Friendly Neural Networks with Hard Robustness Guarantees

**Source**: https://proceedings.mlr.press/v235/baninajjar24a.html

## [POSITIVE] VNN Post-Training Sparsification Framework
A post-training layer-wise optimization framework that minimizes the number of non-zero weights and biases in a pre-trained DNN while preserving classification correctness and robustness requirements, producing a verification-friendly neural network.

**Delta**: up to 76x more verified samples; verification time up to 3x less
**Condition**: Applied to FNNs on MNIST dataset

**Evidence**: "we observe that VNNs allow verification of up to 76 times more samples, besides their advantage in terms of verification time efficiency"

## [POSITIVE] L1 Norm Relaxation of L0 Objective
Replacing the non-convex L0 norm (which counts non-zero elements) with the L1 norm (Manhattan norm) as the tightest convex relaxation, enabling the optimization problem to be solved as a linear program.

**Delta**: enables tractable convex optimization
**Condition**: Required for practical optimization; applies to all VNN generation

**Evidence**: "The L1 norm also referred to as the Manhattan norm, is the tightest convex relaxation of the L0 norm in convex optimization... Being a convex function, the L1 norm can be used in convex optimization problems, which is not possible with the L0 norm."

## [POSITIVE] Layer-Wise Optimization
Optimizing the DNN one layer at a time sequentially from the first hidden layer to the last, fixing previously optimized layers before proceeding to the next.

**Delta**: polynomial time complexity; linear with number of layers
**Condition**: Applied during VNN generation for all architectures

**Evidence**: "Our proposed framework to generate VNNs has a polynomial time complexity, since for each layer one linear program is solved. The end-to-end process of generating VNNs also has linear time complexity with the number of layers."

## [POSITIVE] Neuron State Consistency Constraint (ReLU Linearization)
Constraining optimized weights and biases so that each neuron remains in the same activation state (active or inactive) as in the original DNN, enabling the nonlinear ReLU constraints to be handled as linear constraints.

**Delta**: enables linear program formulation of otherwise nonlinear constraints
**Condition**: Applies to ReLU-activated networks; framework extendable to other piecewise-linear activations

**Evidence**: "If we constrain the neuron to remain within one of these linear segments, the ReLU function behaves linearly, making it possible to handle the proposed optimization."

## [POSITIVE] Epsilon Neighborhood Constraint on Neuron Values
Constraining optimized neuron values to remain within an epsilon-scaled neighborhood of their original values, controlling the trade-off between sparsity and accuracy.

**Delta**: verified robustness increases up to 13% for small networks with epsilon=0.1
**Condition**: Small networks (e.g., 2x50) with adequate validation set size

**Evidence**: "For example, when ε = 0.1, the value of each neuron x̃(l)i can change in the range of [0.9x(l)i, 1.1x(l)i], and the freedom of choices allows for sparser VNNs that are easier to handle by the over-approximation-based verification techniques."

## [NEGATIVE] Larger Epsilon with Large Networks
Increasing epsilon (relaxation of neuron value constraints) for large networks relative to a small validation set, which can cause accuracy degradation.

**Delta**: accuracy decreases from >90% to ~80% when epsilon=0.3 on 9x200 network
**Condition**: Large networks (e.g., 8x200/9x200) with small validation sets

**Evidence**: "Figure 4b, which illustrates the results of a large network with 9×200 architecture, shows a slight decrease in accuracy when ε increases... with ε = 0.3, the accuracy slightly decreases to 80%."

## [POSITIVE] Validation Set Usage Instead of Training Set
Using the validation set (rather than training set) as the constraint set during optimization to avoid overfitting in the VNN.

**Delta**: avoids overfitting
**Condition**: Applied during all VNN optimization

**Evidence**: "In the optimization problem, we consider the validation set instead of the training set to avoid over-fitting in the VNN."

## [POSITIVE] Robustness Margin M in Classification Constraint
Adding a constant robustness margin M to the classification constraint so that the correct class output exceeds all other class outputs by at least M, providing hard robustness guarantees.

**Delta**: provides hard robustness guarantees
**Condition**: Applied as part of the VNN optimization constraints

**Evidence**: "introducing a constant robustness margin M to this inequality converts it to x̃(N)c > x̃(N)i + M to provide hard guarantees for enhancing the robustness of the DNN."

## [POSITIVE] Increasing Number of Optimized Layers
Optimizing more layers of the DNN sequentially increases sparsity and reduces over-approximation accumulation, improving verification-friendliness.

**Delta**: proportion of verified cases increases monotonically with number of optimized layers
**Condition**: FNN with 8x200 architecture, epsilon=0.2, evaluated with SafeDeep

**Evidence**: "Figure 6 demonstrates that as the number of optimized layers increases, shown on the x-axis, the proportion of verified cases increases. This phenomenon arises as increasing the number of optimized layers leads to decreasing the number of non-zero neurons and over-approximation of each neuron."

## [POSITIVE] Combination with PGD Adversarial Training
Applying the VNN framework on top of models already adversarially trained with Projected Gradient Descent (PGD), combining adversarial robustness training with post-training sparsification.

**Delta**: VNNs of PGD-trained models maintain comparable accuracy while exhibiting higher verification-friendliness than PGD models alone
**Condition**: 6x500 FNNs on MNIST with PGD adversarial training (delta=0.1 and 0.3)

**Evidence**: "Figure 5 shows that the accuracy values of VNN0(PGD1) and VNN1(PGD1) are comparable to that of PGD1, while exhibiting higher verification-friendliness."

## [NEGATIVE] Magnitude-Based Pruning (MBP) Baseline
A standard pruning technique that forces weights and biases below a fixed magnitude threshold to zero, without considering robustness or verification requirements.

**Delta**: VNNs are up to 46x more verification-friendly than MBP on MNIST; MBP accuracy drops to 68.4% when matched to VNN sparsity on CHB-MIT
**Condition**: Compared against VNNs on MNIST, CHB-MIT, and MIT-BIH datasets

**Evidence**: "VNNs are up to 46, 19, and 27 times more verification-friendly than MBP models on DNNs trained on MNIST, CHB-MIT, and MIT-BIH datasets, respectively... the accuracy of the MBP models drops to 68.4% ± 4.3%, if we enforce the MBP models to have similar sparsity as our VNNs."

## [NEGATIVE] Sparse Optimization Pruning (SOP) Baseline
A training-time sparsification method using Lagrange multipliers to regularize the loss function with robustness requirements, without hard constraint guarantees.

**Delta**: VNNs are up to 51x more verification-friendly than SOP on MNIST
**Condition**: Compared against VNNs on MNIST dataset

**Evidence**: "VNNs are up to 51 times more verification-friendly than SOP models trained on the MNIST dataset."

## [POSITIVE] VNN on Medical Safety-Critical Datasets (CHB-MIT)
Applying the VNN framework to personalized CNNs for epileptic seizure detection, generating sparser models with hard robustness guarantees.

**Delta**: up to 9x (ERAN) and 24x (SafeDeep) more verified robustness; ~3.2% accuracy reduction (85.7% to 82.5%)
**Condition**: 23 personalized CNNs on CHB-MIT epileptic seizure detection dataset

**Evidence**: "Our framework generates VNNs with ε = 0 that have up to 9 and 24 times more verified robustness using ERAN and SafeDeep, respectively... The accuracy (µ ± σ2) of the original CNNs and VNNs is 85.7% ± 3.8% and 82.5% ± 4.2%, respectively."

## [POSITIVE] VNN on Medical Safety-Critical Datasets (MIT-BIH)
Applying the VNN framework to personalized CNNs for cardiac arrhythmia detection.

**Delta**: up to 34x (ERAN) and 30x (SafeDeep) more verified robustness; slight accuracy improvement (91.5% to 92.0%)
**Condition**: 14 personalized CNNs on MIT-BIH cardiac arrhythmia detection dataset

**Evidence**: "The experiments show that our proposed framework generates VNNs with ε = 0 that have up to 34 and 30 times more verified robustness compared to the original CNNs using ERAN and SafeDeep, respectively... accuracy of 91.5% ± 3.1%, 90.7% ± 3.4%, and 92.0% ± 3.0%, respectively."

## [POSITIVE] Larger Validation Set Size
Increasing the size of the validation set used during VNN optimization to better constrain the optimization and maintain prediction performance.

**Delta**: increases prediction performance
**Condition**: Particularly important for large networks where validation set may be small relative to model size

**Evidence**: "Our experiments show that increasing the size of the validation set increases the prediction performance."
