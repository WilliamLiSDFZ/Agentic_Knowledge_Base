# Compositional Curvature Bounds for Deep Neural Networks

**Source**: https://proceedings.mlr.press/v235/entesari24a.html

## [POSITIVE] Compositional Curvature Bound Algorithm
A layer-by-layer recursive algorithm to analytically compute provable upper bounds on the second derivative (curvature constant) of neural networks by leveraging the compositional structure of the model.

**Delta**: outperforms baseline
**Condition**: Applied to 6-layer fully connected network on MNIST with curvature regularization, compared against CRC (Singla & Feizi, 2020)

**Evidence**: "Figure 3 compares the certified radii of these methods and confirms the superior performance of the compositional curvature calculation algorithm."

## [POSITIVE] Anchored Lipschitz Constant
A relaxed notion of Lipschitz continuity that fixes one of the two points to the point of interest, yielding a local (anchored) bound that is always a lower bound on the global Lipschitz constant.

**Delta**: significantly improves bounds
**Condition**: Applied to fully connected neural networks of varying depths on MNIST for both Lipschitz and curvature constant estimation

**Evidence**: "The results demonstrate that using the anchored counterparts significantly improves the bounds."

## [POSITIVE] Curvature-based Robustness Certificate (CCRC)
A first-order (gradient-informed) certified radius derived using local gradients and anchored curvature bounds, providing a closed-form lower bound on the distance to the decision boundary.

**Delta**: 49.53% vs 36.25% certified accuracy at ε=36/255 for 6C2F; 52.09% vs 42.73% for 6F
**Condition**: Applied to 6C2F and 6F architectures on CIFAR-10, compared against CRM baseline

**Evidence**: "We find that incorporating the additional regularization term leads to higher certified accuracies, smaller certification gaps, and often, higher clean accuracies."

## [POSITIVE] Curvature Regularization in Training Loss
Using the differentiable curvature bound as a regularizer during training to promote low-curvature networks, either via per-sample certified radius rewards or global curvature penalization.

**Delta**: higher certified accuracies and smaller certification gaps
**Condition**: Applied during training of 6C2F, 6F, and Lip-3C1F architectures on CIFAR-10

**Evidence**: "We find that incorporating the additional regularization term leads to higher certified accuracies, smaller certification gaps, and often, higher clean accuracies."

## [POSITIVE] Curvature-based Attack Certificate
A novel method using curvature bounds to derive provable upper bounds on the certified robustness, narrowing the certification gap by providing attack certificates for data points.

**Delta**: attack certificates for 808 samples; narrows verified accuracy range to [47.16%, 49.74%]
**Condition**: Applied to 6F model on CIFAR-10 with perturbation budget 36/255

**Evidence**: "By analyzing the attack certificates we find that our method is able to provide an attack certificate for a total of 808 samples, of which 645 require a perturbation budget of at most 36/255."

## [POSITIVE] Loop Transformation (LipLT) for Lipschitz Estimation
A control-theoretic loop transformation applied to activation layers to obtain tighter Lipschitz constant bounds that exploit monotonicity of activations, provably improving naive product-of-layers bounds.

**Delta**: provably better than naive product bound
**Condition**: Applied to compute Lipschitz constants of subnetworks in Algorithm 1

**Evidence**: "As shown in (Fazlyab et al., 2023), this bound provably improves the naive bound obtained by the product of Lipschitz constants of individual layers, i.e., L_k,LT ≤ ∏ L_h,naive."

## [POSITIVE] Vectorized Jacobian Representation (Lemma 3.6/Theorem 3.8)
Rewriting the Jacobian matrix of a residual block as a standard neural network layer to enable more advanced Lipschitz estimation techniques and obtain tighter curvature bounds.

**Delta**: L_dh ≤ L_Dh (provably tighter)
**Condition**: Applied for p=2 norm to non-residual and residual building blocks

**Evidence**: "Furthermore, L_dh[k] ≤ L_Dh[k]."

## [POSITIVE] LipSDP-based Curvature Bound (Theorem 3.9)
Using a semidefinite program (LipSDP) feasible solution on the vectorized Jacobian to further reduce conservatism in curvature estimation for non-residual blocks.

**Delta**: L_dh,SDP ≤ L_dh (provably tighter than Theorem 3.8)
**Condition**: Applied for p=2 to non-residual building blocks (H^k=0, G^k=I), optimal when α'=-β'

**Evidence**: "Thus, we always have L_dh[k] ≤ L_ϕ′∥√T*W^k∥_2 = L_dh,SDP[k]."

## [POSITIVE] 1-Lipschitz Layer Architecture
Using 1-Lipschitz constrained layers (e.g., SLL) to simplify curvature bound computation, reducing the curvature bound to a sum of per-layer Jacobian Lipschitz constants.

**Delta**: SLL + CCRC: 46.6%/39.3%/31.6% vs SLL alone: 45.0%/35.0%/26.5% at ε=36/72/108 out of 255
**Condition**: Applied to Lip-3C1F architecture on CIFAR-10 with p=2

**Evidence**: "Lip-3C1F: SLL + CCRC (Ours) achieves 46.6, 39.3, 31.6 certified accuracy vs SLL at 45.0, 35.0, 26.5."

## [POSITIVE] Curvature-based Certificate vs Lipschitz-based Certificate
Using second-order (curvature) information to derive tighter certified radii compared to zeroth-order Lipschitz-based certificates, provided curvature is sufficiently small.

**Delta**: provably larger certified radius when curvature condition is met
**Condition**: Holds when the condition involving gradient norm, logit gap, and curvature constant is satisfied (Proposition 2.2)

**Evidence**: "we show that these curvature-based certificates provably improve upon Lipschitz-based certificates, provided the curvature is sufficiently small."

## [POSITIVE] Monotonicity-informed Lipschitz Bound (Loop Transformation on Layer)
Applying loop transformation to a single activation layer to exploit the monotonicity constant α, yielding a provably tighter per-layer Lipschitz bound than the naive norm-product bound.

**Delta**: provably better than naive bound (13)
**Condition**: Applied to each residual block h^k with monotone activation slope-restricted in [α,β]

**Evidence**: "As shown in (Fazlyab et al., 2023), this bound, now informed by the monotonicity constant α, is provably better than (13). This can be proved by applying the triangle inequality on the first term."

## [POSITIVE] Support for Non-twice-differentiable Activations (e.g., ELU)
The Jacobian Lipschitz analysis applies to networks with activations that have Lipschitz continuous first derivatives but undefined second derivatives (e.g., ELU), unlike Hessian-based methods.

**Delta**: applicable where Hessian-based analysis fails
**Condition**: Applies to any activation with Lipschitz continuous first derivative but potentially undefined second derivative

**Evidence**: "The ELU has a Lipschitz continuous first derivative, but its second derivative is not defined at z=0. Therefore, Hessian-based analysis would fail for this function, whereas our Jacobian Lipschitz analysis is applicable to networks using this activation function."
