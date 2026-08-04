# The Perception-Robustness Tradeoff in Deterministic Image Restoration

**Source**: https://proceedings.mlr.press/v235/ohayon24a.html

## [NEGATIVE] CGAN Loss for Joint Perceptual Quality
Training a deterministic estimator with a conditional GAN loss where the discriminator receives pairs of (natural image, degraded measurement) as real examples and (estimated output, degraded input) as fake examples, theoretically minimized when pX_hat,Y = pX,Y

**Delta**: higher Lipschitz constant (more erratic behavior)
**Condition**: Deterministic estimators trained with CGAN loss targeting low joint perceptual index

**Evidence**: "Theoretically, the optimal solution of a parametric model trained solely with such an adversarial discriminator is a stochastic estimator Xˆ which satisfies pX,Yˆ = pX,Y."

## [POSITIVE] Robustness Regularization Loss (LR)
An auxiliary loss that drives outputs from original inputs and randomly perturbed nearby inputs to be roughly equal, promoting Lipschitz continuity controlled by coefficient lambda

**Delta**: higher lambda leads to lower Lipschitz constant lower bound K and higher JEMD (worse joint perceptual quality)
**Condition**: Toy example with Gaussian denoising; tradeoff between robustness and joint perceptual quality

**Evidence**: "This loss drives the outputs originating from Y and from (randomly chosen) inputs close to Y to be roughly equal, i.e., such an objective promotes robustness, and the level of robustness is controlled with the coefficient λ ≥ 0."

## [NEGATIVE] High Joint Perceptual Quality (low JFID)
Achieving a small statistical distance between pX_hat,Y and pX,Y, combining both high perceptual quality and consistency with measurements

**Delta**: increased adversarial vulnerability; PSNR between f(y) and f(yadv) as low as 20.31dB for SwinIR-GAN vs 40.75dB for SRResCGAN
**Condition**: Deterministic image super-resolution algorithms evaluated on DIV2K test set

**Evidence**: "As can be seen, the better the joint perceptual quality, the higher the sensitivity to adversarial attacks."

## [POSITIVE] L1 Reconstruction Loss Only (RRDB baseline)
Training a deterministic estimator solely with L1 reconstruction loss, producing blurry outputs with low perceptual quality but high robustness

**Delta**: robust to adversarial attacks: 59.1% vs 56.9% female classification for original vs attacked (negligible change), compared to GFPGAN's 63.3% vs 72.2%
**Condition**: Face restoration adversarial attack experiment; same training data and degradation as GFPGAN

**Evidence**: "Unlike GFPGAN, this model is robust to such attacks, as 59.1% and 56.9% of its original and attacked outputs, respectively, are classified as 'female'."

## [NEUTRAL] I-FGSM Adversarial Attack (small alpha)
Iterative Fast Gradient Sign Method attack with small step size (alpha=1/255) used to measure Lipschitz constant lower bound by computing output change ratio

**Delta**: PSNR between y and yadv at least 48.13dB; used as evaluation metric not training technique
**Condition**: Quantitative evaluation of super-resolution algorithms on DIV2K test set

**Evidence**: "We specifically choose a small value of α in order to assess the rate of change in each algorithm's output while using inputs that remain within supp pY... at α = 1/255, the difference between each pixel in y and yadv is at most 1 gray level"

## [POSITIVE] Farthest Point Sampling (FPS) for Posterior Exploration
Algorithm that sequentially finds input perturbations of y that produce outputs maximally distant from previously found outputs, leveraging the high Lipschitz constant of high-perceptual-quality deterministic estimators to explore the posterior

**Delta**: generates diverse semantically meaningful outputs (e.g., gender change, hair texture variation) from a single input with minimum 30dB PSNR perturbations
**Condition**: Applied to GFPGAN on CelebA-HQ face images with same degradation as adversarial attack experiment

**Evidence**: "We indeed see that by slightly perturbing the original input, we obtain diverse outputs that all seem to correspond to the measurements."

## [NEUTRAL] Joint FID (JFID) as Joint Perceptual Index Approximation
A tweaked version of Frechet Inception Distance computed on joint (image, degraded measurement) pairs using Inception-V3 features, approximating the Wasserstein distance between pX_hat,Y and pX,Y

**Delta**: consistently correlates with Lipschitz constant lower bound K across three degradation types
**Condition**: Evaluation of super-resolution algorithms on DIV2K test set across Track1, Track2, and bicubic degradations

**Evidence**: "The results clearly show that smaller values of √JFID correspond to larger values of K."

## [NEGATIVE] Deterministic Estimator Architecture for Inverse Problems
Using a deterministic (non-stochastic) neural network as the estimator for image restoration, mapping each input to a single output

**Delta**: cannot simultaneously achieve perfect perceptual quality and perfect consistency; Lipschitz constant must grow to infinity as joint perceptual index approaches zero
**Condition**: Any non-invertible degradation; proven theoretically and validated empirically

**Evidence**: "This means that the Lipschitz constant must grow to infinity as the Wasserstein distance between pX,Yˆ and pX,Y approaches zero. An immediate practical implication of this result is that the higher the joint perceptual quality of an estimator... the more susceptible it is to input adversarial attacks."

## [NEGATIVE] GAN-based Super-Resolution (e.g., SwinIR-GAN, RealESRGAN)
GAN-trained super-resolution models that achieve low JFID (high joint perceptual quality) but consequently high Lipschitz constant

**Delta**: SwinIR-GAN PSNR between f(y) and f(yadv) = 20.31dB; RealESRGAN = 22.76dB, indicating high sensitivity to minor input perturbations
**Condition**: Evaluated on Track2 challenge degradation from Lugmayr et al. 2019

**Evidence**: "We clearly see that X̂λ is more erratic for smaller values of λ, as anticipated by Theorem 4.1... the better the joint perceptual quality, the higher the sensitivity to adversarial attacks."

## [POSITIVE] PSNR-Optimized Super-Resolution (e.g., SwinIR-PSNR, BSRNet)
Super-resolution models trained to optimize distortion metrics (PSNR/MSE), resulting in higher JFID (lower joint perceptual quality) but lower Lipschitz constant

**Delta**: SwinIR-PSNR PSNR between f(y) and f(yadv) = 31.71dB; BSRNet = 31.65dB, indicating greater robustness to adversarial attacks
**Condition**: Evaluated on Track2 challenge degradation; robustness measured via I-FGSM with alpha=1/255

**Evidence**: "As can be seen, the better the joint perceptual quality, the higher the sensitivity to adversarial attacks."

## [NEGATIVE] Adversarial Attack on Decision-Making Pipeline
Using I-FGSM to perturb low-resolution inputs to GFPGAN to manipulate downstream gender classification, exploiting the high Lipschitz constant of high-perceptual-quality models

**Delta**: female classification rate increased from 63.3% to 72.2% for GFPGAN attacked outputs; RRDB showed negligible change (59.1% to 56.9%)
**Condition**: Face gender classification pipeline using GFPGAN for 16x super-resolution on CelebA-HQ; alpha=16/255, T=100 iterations

**Evidence**: "the percentage of 'female'-classified attacked images is increased to 72.2%... unlike GFPGAN, this model is robust to such attacks, as 59.1% and 56.9% of its original and attacked outputs, respectively, are classified as 'female'."
