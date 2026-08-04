# Robust Inverse Graphics via Probabilistic Inference

**Source**: https://proceedings.mlr.press/v235/le24b.html

## [POSITIVE] Robust Inverse Graphics (RIG) - Full Posterior Inference
Performs full probabilistic inference over both scene latents (x) and corruption parameters (c) jointly, rather than point estimation (MAP). Uses variational inference with mean-field parameterization.

**Delta**: ProbNeRF VI: Rain 0.32 vs MAP 0.43 VSD; Cloud 0.45 vs MAP 0.48 VSD; FOV 0.36 vs MAP 0.46 VSD (ShapeNet)
**Condition**: Corrupted single-image 3D scene reconstruction on ShapeNet dataset

**Evidence**: "probabilistic inference (ProbNeRF VI and SSDNeRF ReGAL) outperform the point estimates and the regression baseline on the corrupted scenes for ShapeNet"

## [NEGATIVE] MAP Inference with Uniform Corruption Prior
Maximum a posteriori estimation of scene and corruption NeRF parameters jointly, where corruption has an improper uniform prior.

**Delta**: Rain 0.43 vs VI 0.32 VSD; Cloud 0.48 vs VI 0.45 VSD; FOV 0.46 vs VI 0.36 VSD (ShapeNet)
**Condition**: Single-image scene reconstruction with corruption NeRF and uniform prior

**Evidence**: "MAP solution uses the corruption NeRF to explain the observation more than the VI solution... this approach leads to 'billboard' solutions, where the corruption c ends up explaining the scene, like a billboard placed in front of the camera"

## [POSITIVE] Reconstruction-Guidance with Auxiliary Latents (ReGAL)
A diffusion conditioning algorithm that alternates between reconstruction-guidance sampling for scene latents and Langevin updates for auxiliary corruption latents, enabling joint posterior inference with diffusion priors.

**Delta**: SSDNeRF ReGAL (K=8) achieves best PSNR of 30.87 clean, 26.32 rain, 19.83 cloud, 35.22 FOV on ShapeNet vs ProbNeRF MAP of 27.08, 18.96, 17.68, 31.88
**Condition**: Diffusion-based scene priors (SSDNeRF) on ShapeNet and MultiShapeNet datasets

**Evidence**: "ReGAL outperforms the other conditions... The more powerful prior used for SSDNeRF model produces the best reconstructions on clean images and, when used with ReGAL, the most accurate depth image"

## [POSITIVE] ReGAL with Importance Sampling (K>1)
Running K independent ReGAL chains and computing importance weights to correct for the approximation error in the proposal distribution, providing convergence guarantees.

**Delta**: FOV task ShapeNet: K=1 VSD 0.49, K=4 VSD 0.43, K=8 VSD 0.34; PSNR FOV: K=1 35.08, K=8 35.22
**Condition**: FOV estimation task on ShapeNet; effect is weak for rain and cloud corruptions

**Evidence**: "The decorruption quality is weakly dependent on this for most settings, but is most noticeably beneficial for the FOV estimation task for ShapeNet"

## [POSITIVE] Uninformative Uniform Corruption Prior
Using an improper prior p(c) proportional to 1 over corruption NeRF parameters, requiring no knowledge of the corruption family ahead of time.

**Delta**: outperforms baseline
**Condition**: General corruption robustness; applicable to rain, snow, fog, floaters, FOV errors

**Evidence**: "we don't require a strong prior over c. In our experiments, we assume an improper prior p(c) ∝ 1. This means that we don't need to know the family of corruptions ahead of time; the corruption can be any 3D entity ranging from weather artifacts and floaters to unwanted objects"

## [POSITIVE] SRT Set Latent Representation for Diffusion Prior
Using Scene Representation Transformer (SRT) set latents with a permutation-invariant transformer-based denoiser (based on PointE) instead of triplanes for the diffusion scene prior.

**Delta**: qualitative improvement described as 'much better'
**Condition**: MultiShapeNet dataset (complex multi-object scenes)

**Evidence**: "SRT's set latents performed much better on the more complex MultiShapeNet dataset"

## [NEUTRAL] Triplane Representation with UNet Denoiser
Using triplane NeRF representation with a UNet denoiser for the diffusion scene prior (SSDNeRF).

**Delta**: sufficient for ShapeNet
**Condition**: ShapeNet dataset (single object scenes)

**Evidence**: "we found that the triplane representation—which uses a UNet denoiser—was sufficient for the ShapeNet dataset"

## [POSITIVE] Mean-Field Variational Inference with Path Derivative Estimator
Parameterizing the guide distribution as independent Gaussians per dimension for both scene and corruption latents, optimized using the path derivative estimator (Roeder et al., 2017).

**Delta**: VI outperforms MAP: Rain VSD 0.32 vs 0.43, Cloud 0.45 vs 0.48, FOV 0.36 vs 0.46 on ShapeNet
**Condition**: ProbNeRF (normalizing flow) scene prior on ShapeNet

**Evidence**: "We use a mean-field parameterization where x and c are independent q(x,c) = q(x)q(c), with each dimension of x and c being parameterized by a separate Gaussian mean and log standard deviation. We optimize these parameters using stochastic gradients of the ELBO, estimated via the path derivative estimator"

## [POSITIVE] Multi-Start Optimization (8 runs, best ELBO selection)
Running variational inference optimization 8 times independently and selecting the run with the largest ELBO to avoid local optima.

**Delta**: avoids local optima (qualitative)
**Condition**: Variational inference for ProbNeRF RIG

**Evidence**: "We run the optimization multiple times (8 in our experiments) and pick the run with the largest ELBO to avoid getting stuck in local optima"

## [NEUTRAL] RealNVP Normalizing Flow Scene Prior (ProbNeRF)
Using a RealNVP normalizing flow as the prior over NeRF latents, enabling tractable density evaluation.

**Delta**: ProbNeRF VI VSD: Clean 0.30, Rain 0.32, Cloud 0.45, FOV 0.36 on ShapeNet
**Condition**: ShapeNet dataset; not expressive enough for MultiShapeNet

**Evidence**: "we use the ProbNeRF model which places a RealNVP prior over x... One advantage of the ProbNeRF model is that it is easy to evaluate the prior density p(x)"

## [POSITIVE] SSDNeRF Training with Co-optimized GLO Latents
Training the diffusion prior by co-optimizing per-training-example GLO latents alongside the diffusion prior and likelihood parameters.

**Delta**: SSDNeRF ReGAL achieves best overall results: Clean PSNR 30.87 vs ProbNeRF MAP 27.08 on ShapeNet
**Condition**: ShapeNet and MultiShapeNet datasets

**Evidence**: "The more powerful prior used for SSDNeRF model produces the best reconstructions on clean images ('SSDNeRF Clean' column of Figure 4) and, when used with ReGAL, the most accurate depth image"

## [POSITIVE] NeRF Composition for Scene and Corruption
Composing scene NeRF and corruption NeRF outputs by summing densities and computing weighted color: σ = σz + σc, γ = (γzσz + γcσc)/σ.

**Delta**: enables joint inference over scene and corruption
**Condition**: All RIG experiments with 3D volumetric corruptions

**Evidence**: "we compose the respective NeRF outputs... σ = σz + σc, γ = (γzσz + γcσc)/σ"

## [NEUTRAL] ReGAL-SMC (Sequential Monte Carlo variant)
An SMC-based generalization of ReGAL that sequentially builds posterior approximations with resampling steps.

**Delta**: no improvement
**Condition**: Applied to RIG domain; tested as alternative to importance sampling ReGAL

**Evidence**: "While it is possible to design an SMC version of ReGAL (Appendix C), it didn't improve performance metrics in our domain"

## [POSITIVE] Strong Scene Prior with Weak Corruption Prior
Combining a strong learned prior over scenes with an uninformative prior over corruptions, creating an asymmetry that biases inference toward recovering the scene.

**Delta**: outperforms domain randomization baselines
**Condition**: Corrupted single-image 3D reconstruction; requires only clean training data

**Evidence**: "We rely on a pre-trained scene prior... and a weak prior over corruptions... RIG, trained only on clean data, outperforms depth estimators and alternative NeRF approaches that perform point estimation instead of full inference"

## [NEGATIVE] Prior Quality Limitation on MultiShapeNet
The scene prior's limited fidelity on complex multi-object scenes reduces the advantage of probabilistic inference over simpler baselines.

**Delta**: DPT achieves competitive VSD 0.90-0.92 vs SSDNeRF ReGAL 0.87-0.95 on MultiShapeNet
**Condition**: MultiShapeNet dataset with complex multi-object scenes

**Evidence**: "For MSN, our prior does not model the data distribution with enough fidelity to resolve the fine details of objects, and therefore does not decisively outperform the relatively coarse estimate that DPT provides"
