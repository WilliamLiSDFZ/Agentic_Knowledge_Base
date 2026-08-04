# Efficient Pareto Manifold Learning with Low-Rank Structure

**Source**: https://proceedings.mlr.press/v235/chen24x.html

## [POSITIVE] Low-Rank Matrix Decomposition for Pareto Manifold
Replaces multiple full base networks with a single main network plus m low-rank matrices (B_i * A_i) per layer, where the weighted combination yields Pareto-optimal solutions

**Delta**: HV 0.887e-2 vs PaMaL 0.0583e-2 on CIFAR-100; HV 1.167e-2 vs PaMaL 0.472e-2 on CelebA
**Condition**: Especially effective when number of tasks is large (20+ tasks)

**Evidence**: "LORPMAN achieves significantly better hypervolume while utilizing only 8.9% of the parameters compared to PaMaL. This underscores the efficiency and effectiveness of LORPMAN in addressing problems with a large number of tasks."

## [POSITIVE] Orthogonal Regularization on Low-Rank Matrices
Encourages orthogonality among the low-rank matrices by minimizing the off-diagonal elements of W^T W, reducing redundancy and conflicts between task-specific matrices

**Delta**: HV 0.314 with vs 0.309 without on UTKFace; correlation reduced from 0.466 to 0.067
**Condition**: UTKFace dataset, 3-task setting

**Evidence**: "with orthogonal regularization, the correlation between low-rank matrices is significantly reduced... Such reduction in correlation encourages learning common features in the main network and differences in the low-rank matrices, thus leading to better HV value."

## [POSITIVE] Main Network Freeze After Certain Epochs
Training is divided into two phases: first both main model and low-rank matrices are updated, then after a freeze epoch the main model is fixed and only low-rank matrices are updated

**Delta**: HV 0.314 (freeze at 80) vs 0.307 (no freeze, epoch 100) on UTKFace
**Condition**: UTKFace dataset; optimal freeze epoch around 80% of total training

**Evidence**: "freezing during the latter half of the training process encourages the low-rank matrices to learn task-specific representations instead of always relying on the main model, thus leading to better performance."

## [NEUTRAL] Scaling Factor for Low-Rank Component
A scalar s is applied to regulate the significance of the low-rank component relative to the main network

**Delta**: HV stable ~0.313-0.314 for s in [0.1, 1], drops slightly to 0.310 at s=2
**Condition**: UTKFace dataset; performance degrades slightly outside reasonable range

**Evidence**: "setting s within a reasonable range (such as [0.1, 1]) leads to stable performance."

## [POSITIVE] Stochastic Approximation for Orthogonal Loss
When number of tasks m exceeds 3, randomly sample a subset of 3 tasks per iteration to compute orthogonal regularization, keeping complexity O(1) independent of m

**Delta**: maintains satisfactory performance (described qualitatively)
**Condition**: Datasets with more than 3 tasks (CIFAR-100 with 20 tasks, CelebA with 40 tasks)

**Evidence**: "This stochastic approximation ensures the complexity is independent of m. Empirical evaluations in Section 4.3 demonstrate that this still maintains satisfactory performance."

## [POSITIVE] Low Rank Value Selection
Choice of rank r for the low-rank matrices, controlling the trade-off between parameter efficiency and approximation power

**Delta**: HV improves from 0.306 (r=4) to 0.314 (r=64); r=8 already outperforms COSMOS and PaMaL
**Condition**: UTKFace dataset; diminishing returns beyond r=64

**Evidence**: "LORPMAN with a rank 8 can already outperform COSMOS and PaMaL (see Table 2). By increasing the rank to 64, even better performance can be achieved. However, further increasing the rank does not yield significant change."

## [POSITIVE] Dirichlet Distribution Preference Sampling
Preference vectors alpha are sampled from a Dirichlet distribution Dir(p) during training to cover the Pareto front continuously

**Delta**: outperforms baseline (enables continuous PF approximation vs discrete methods)
**Condition**: All datasets; enables continuous Pareto front approximation

**Evidence**: "To learn the Pareto manifold, we minimize the expectation of loss given an alpha over the Dirichlet distribution Dir(p)."

## [POSITIVE] Multi-Forward Regularization
Penalizes incorrect solution ordering on the Pareto front by constructing directed graphs based on preference vectors and enforcing monotonicity

**Delta**: part of overall system outperforming baselines
**Condition**: Applied across datasets with varying coefficients (lambda_p=0 for MultiMNIST, 5 for Census, 1 for UTKFace/CIFAR-100)

**Evidence**: "following (Dimitriadis et al., 2023), we calculate the multi-forward regularization loss Rp which penalizes incorrect solution ordering on the PF"

## [POSITIVE] Shared Main Network Architecture
A single main network captures common features across tasks while low-rank matrices capture task-specific differences, enabling feature sharing unlike PaMaL's independent base networks

**Delta**: PaMaL base networks show increasing cosine similarity during training (from ~0 to high values), motivating shared structure
**Condition**: Particularly beneficial for large number of tasks where PaMaL suffers from slow convergence

**Evidence**: "The main modules are expected to capture the common features across multiple tasks, thereby providing a shared foundation that each low-rank adaptation can leverage... base networks cannot benefit from each other during training, which can potentially impair performance, especially when scaling to a larger number of base networks."

## [NEGATIVE] COSMOS Preference Vector Conditioning
Incorporates preference vector as additional input to base network to generate outputs with different preferences with minimal extra parameters

**Delta**: HV 0.888 vs LORPMAN 0.918 on MultiMNIST; HV 0.281 vs LORPMAN 0.314 on UTKFace; HV 0.344e-2 vs LORPMAN 0.887e-2 on CIFAR-100
**Condition**: Baseline comparison across all datasets; consistently underperforms LORPMAN

**Evidence**: "COSMOS exhibits limited accuracies due to the constraints imposed by the small number of parameters... these methods are sometimes constrained by the relatively limited parameter space, which can lead to suboptimal performance."

## [NEGATIVE] Hypernetwork-based Pareto Front Learning (PHN/PHN-HVI)
Uses a hypernetwork that takes preference vector as input and outputs base network parameters; hypernetwork is much larger than base network

**Delta**: PHN HV 0.900 vs LORPMAN 0.918 on MultiMNIST with 2.793M vs 0.046M parameters
**Condition**: Only applicable to small base networks; cannot scale to ResNet-18 or larger

**Evidence**: "the size of the hypernetwork significantly exceeds that of the base network, thus restricting its use to small base networks... using the same hypernetwork structure as in MultiMNIST and Census will result in a hypernetwork with approximately 1 billion parameters."

## [NEGATIVE] PaMaL Linear Combination of Full Base Networks
Learns m full base networks whose linear combination yields Pareto-optimal solutions; each task requires its own complete network

**Delta**: HV 0.0583e-2 vs LORPMAN 0.887e-2 on CIFAR-100 (20 tasks); HV 0.472e-2 vs LORPMAN 1.167e-2 on CelebA (40 tasks)
**Condition**: Degrades significantly with large number of tasks; 296.5M parameters for 20 tasks vs LORPMAN's 26.4M

**Evidence**: "The results highlight the challenges encountered by PaMaL when dealing with a large number of objectives. PaMaL needs to jointly train 20 base networks, which leads to a large number of parameters and a small hypervolume... the poor performance of PaMaL on CIFAR-100 is due to its slow convergence, since it has to jointly train 20 base networks."

## [NEGATIVE] FiLM Conditioning Layer
Adds FiLM condition layers after each ResNet block for preference-conditioned multi-task learning via channel-wise multiplication and addition

**Delta**: HV 0.803e-2 vs LORPMAN 1.167e-2 on CelebA
**Condition**: CelebA dataset with 40 tasks

**Evidence**: "The FiLM condition suffers similar problems as COSMOS due to the limited number of parameters."

## [NEGATIVE] PHN with Chunking
Hypernetwork with chunking mechanism to handle larger base networks, tested with original (hidden dim=100) and scaled (hidden dim=500) settings

**Delta**: PHN-Chunking original HV 0.663e-2, scaled HV 0.681e-2 vs LORPMAN 1.167e-2 on CelebA
**Condition**: CelebA dataset with 40 tasks

**Evidence**: "PHN with chunking also shows worse performance than LORPMAN. In comparison, the proposed LORPMAN is a more straightforward approach that achieves good performance and parameter efficiency."
