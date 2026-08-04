# CosPGD: an efficient white-box adversarial attack for pixel-wise prediction tasks

**Source**: https://proceedings.mlr.press/v235/agnihotri24b.html

## [POSITIVE] CosPGD - Cosine Similarity Loss Scaling
Scales the per-pixel attack loss by the cosine similarity between the normalized network prediction and the target/ground truth at each pixel location, encouraging balanced errors across the entire image domain in a smooth, fully differentiable way.

**Delta**: mIoU reduced to ~0.08% vs 2.69% (SegPGD) and 6.79% (PGD) on DeepLabV3 after 40 iterations
**Condition**: Semantic segmentation on PASCAL VOC 2012 with DeepLabV3, ℓ∞-norm constrained attack with 40-100 iterations

**Evidence**: "PGD can bring down the mIoU of DeepLabV3 to 6.79%. SegPGD, by naïvely utilizing the pixel-wise segmentation error, deteriorates the model performance further to 2.69%. However, CosPGD can fool the network into making incorrect predictions for almost all pixels, bringing down the model performance to almost 0% after 100 iterations."

## [POSITIVE] Pixel-wise Prediction Alignment Scaling
Weighting the loss at each pixel location based on how well the current prediction aligns with the target, so that pixels with correct predictions receive higher loss weight and pixels already misaligned receive lower weight.

**Delta**: outperforms baseline
**Condition**: Any pixel-wise prediction task (segmentation, optical flow, image restoration)

**Evidence**: "As the loss in CosPGD is scaled with a pixel-wise measure of alignment between the current prediction and the target in Equation 5, the resulting gradient update emphasizes on changing those pixel-wise predictions that are correct in the current prediction."

## [POSITIVE] Softmax Normalization (ψ function)
Applies softmax to the network predictions before computing cosine similarity, providing a normalized probability distribution over classes for use in the alignment score computation.

**Delta**: None
**Condition**: Semantic segmentation and regression tasks; required for smooth, differentiable loss scaling

**Evidence**: "To obtain a distribution over the predictions, we calculate the softmax of the predictions before taking the argmax... Thus, in Algorithm 1 (given in Appendix A.2) and Equation 5, ψ is the softmax function."

## [POSITIVE] Smooth and Fully Differentiable Loss Scaling
Using cosine similarity as a continuous, differentiable scaling function instead of discrete argmax-based binary decisions, ensuring gradient directions change smoothly across attack iterations.

**Delta**: fewer gradient sign flips and stable absolute gradient differences compared to PGD and SegPGD
**Condition**: Semantic segmentation on PASCAL VOC 2012 with DeepLabV3, over 100 attack iterations

**Evidence**: "We observe that the absolute difference between gradient values (top) is larger for PGD and increasing for SegPGD, while being stable for CosPGD. Further, CosPGD has fewer changes in gradient direction over attack iterations (bottom) compared to PGD and SegPGD. This shows CosPGD is more stable during optimization compared to PGD and SegPGD."

## [POSITIVE] Targeted Attack Formulation (Dissimilarity Scaling)
For targeted attacks, scales the loss by the dissimilarity (1 - cosine similarity) between the prediction and the target, so pixels far from the target receive higher loss weight, driving all predictions toward the target.

**Delta**: epe reduced to as low as 1.55 on Sintel (final); epe of 4.84 vs PGD's 7.32 on KITTI-2015 after 40 iterations
**Condition**: Targeted optical flow estimation attack on RAFT using KITTI-2015 and Sintel datasets

**Evidence**: "CosPGD achieves to bring more pixel-wise predictions very close to the target whereas only few predictions have larger epe. For PGD, more predictions remain with higher epe to the target... CosPGD significantly reduces the gap to target (a)."

## [NEGATIVE] SegPGD Binary Loss Scaling (baseline comparison)
SegPGD makes a hard binary decision per pixel based on argmax classification result to separately weight correctly and incorrectly classified pixels, using a heuristic λ parameter that decays over iterations.

**Delta**: mIoU 2.69% vs CosPGD's ~0.08% on DeepLabV3 after 40 iterations; increasing gradient instability over iterations
**Condition**: Semantic segmentation only; cannot be applied to regression tasks

**Evidence**: "The discrete nature of this weighting scheme has several disadvantages... the argmax operation in Equation 11 is not differentiable, such that, during the iterations, the direction of the gradient update can fluctuate, potentially leading to slower convergence of the SegPGD attack, compared to the proposed CosPGD."

## [NEGATIVE] SegPGD λ Heuristic Decay
SegPGD uses a heuristic λ scaling factor that decays over iterations to prevent the attack from becoming benign, but this fades out the pixel-wise weighting effect over time.

**Delta**: None
**Condition**: SegPGD applied to semantic segmentation over many iterations

**Evidence**: "The λ scaling in (Gu et al., 2022) has been proposed as a heuristical remedy. It scales the loss over iterations such that the impact of the proposed scheme decays over time. At the end of the attack iterations, λ ≈ 1/2. This avoids the concern of the attack becoming benign after a few iterations, yet it fades out the effect of SegPGD and may reduce its efficiency. CosPGD, operating on continuous predictions, does not require such a heuristic."

## [NEGATIVE] Standard PGD for Pixel-wise Tasks (baseline comparison)
Applying the standard PGD attack (designed for classification) to pixel-wise prediction tasks without any pixel-wise loss weighting, summing loss uniformly over all locations.

**Delta**: mIoU only reduced to 6.79% on DeepLabV3 vs CosPGD's ~0.08%; epe of 7.32 vs CosPGD's 4.84 on KITTI-2015 after 40 iterations
**Condition**: Semantic segmentation and optical flow estimation; PGD does not leverage pixel-wise prediction information

**Evidence**: "PGD tends to only fit the target (all zeros, i.e. white) in parts of the optical flow, while a few predictions remain intact... PGD can bring down the mIoU of DeepLabV3 to 6.79%."

## [NEUTRAL] Randomized Initialization of Adversarial Example
Initializing the adversarial example with the clean input plus randomized noise in the range [-ε, +ε] before iterative attack optimization.

**Delta**: None
**Condition**: All CosPGD attack settings; standard practice inherited from PGD

**Evidence**: "X_adv is initialized to the clean input sample X_clean with added randomized noise in the range [−ε, +ε], ε being the maximum allowed perturbation."

## [POSITIVE] ℓ∞-norm Constraint on Perturbation
Constraining the adversarial perturbation within an ℓ∞ epsilon-ball around the clean input, clipping the perturbation at each iteration.

**Delta**: None
**Condition**: Main paper experiments on semantic segmentation, optical flow, and image restoration

**Evidence**: "In the main paper, we report ℓ∞-norm constrained 8/255 attacks with ε ≈ 8/255 for CosPGD, SegPGD, and PGD."

## [POSITIVE] ℓ2-norm Constraint on Perturbation
Constraining the adversarial perturbation within an ℓ2 epsilon-ball, projecting the perturbation onto the ℓ2 ball at each iteration.

**Delta**: CosPGD outperforms both PGD and SegPGD under all commonly used ε and α values
**Condition**: Semantic segmentation on PASCAL VOC 2012 with DeepLabV3; appendix results

**Evidence**: "We show in Appendix B.6.1 that CosPGD outperforms both PGD and SegPGD (for segmentation) in the ℓ2-norm constraint settings under all commonly used ε and α values."

## [NEUTRAL] One-hot Encoding for Segmentation Targets
Encoding the ground truth segmentation label as a one-hot vector to serve as the target in the cosine similarity computation for classification tasks.

**Delta**: None
**Condition**: Semantic segmentation tasks where ground truth is a categorical label

**Evidence**: "In the case of semantic segmentation, we obtain the distribution of the target Y_i for every point i by generating a one-hot encoded vector of the label (i.e. encoding the argmax label)."

## [POSITIVE] Softmax for Continuous Regression Targets
Applying softmax to continuous regression targets (e.g., optical flow, disparity) to normalize them for use in the cosine similarity alignment score.

**Delta**: None
**Condition**: Pixel-wise regression tasks such as optical flow and disparity estimation

**Evidence**: "we also apply softmax to compute Y_i from continuous targets, e.g. for optical flow or disparity estimation."

## [POSITIVE] CosPGD for Image Deblurring (NAFNet)
Applying CosPGD as a non-targeted attack on a vision transformer-based image restoration model (NAFNet) for image deblurring.

**Delta**: significantly outperforms PGD and SegPGD on PSNR and SSIM metrics
**Condition**: Image deblurring on GoPro dataset using NAFNet, ℓ∞-norm constrained non-targeted attack

**Evidence**: "CosPGD is a significantly stronger attack than both PGD and SegPGD on this task."

## [POSITIVE] Early Iteration Attack Efficiency
CosPGD achieves strong attack performance with fewer iterations due to stable gradient updates, providing reliable robustness rankings between models at low iteration counts.

**Delta**: CosPGD correctly ranks DeepLabV3 as more robust than PSPNet even at 3 iterations, while SegPGD requires ≥5 iterations
**Condition**: Semantic segmentation robustness evaluation comparing DeepLabV3 and PSPNet

**Evidence**: "An indication of the potential benefit can be seen for example in Table 11 (Appendix), where we observe that at low attack iterations (iterations=3) SegPGD implies that PSPNet is more adversarially robust than DeepLabV3. However, after more attack iterations (iterations ≥ 5), SegPGD reveals that DeepLabV3 is more robust than PSPNet. Contrary to this, CosPGD even at low attack iterations correctly predicts DeepLabV3 to be more robust than PSPNet."
