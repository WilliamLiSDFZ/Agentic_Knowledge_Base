# RODEO: Robust Outlier Detection via Exposing Adaptive Out-of-Distribution Samples

**Source**: https://proceedings.mlr.press/v235/mirzaei24a.html

## [POSITIVE] Adaptive Outlier Exposure (RODEO)
Generates near-distribution, diverse outliers using a text-to-image diffusion model guided by CLIP, conditioning on inlier images and semantically related but distinct text labels, then uses these for adversarial training

**Delta**: outperforms existing methods by up to 50% AUROC in adversarial settings; mean ND clean/PGD: 85.1/65.6 vs best alternative
**Condition**: Novelty Detection, Open-Set Recognition, and OOD detection tasks under adversarial attacks (PGD-1000, AutoAttack, Adaptive AutoAttack)

**Evidence**: "our experimental results show that utilizing our synthesized outliers significantly enhances the performance of the outlier detector, particularly in adversarial settings... RODEO establishes significant performance in adversarial settings, surpassing existing methods by up to 50% in terms of AUROC detection"

## [POSITIVE] Near-Distribution Outlier Exposure
Using OE samples that are semantically and stylistically close to the inlier distribution rather than distant datasets

**Delta**: replacing Tiny ImageNet with SVHN, MNIST, or Gaussian noise caused notable decline in detection performance for ALOE and ATD
**Condition**: Adversarial outlier detection settings; demonstrated on CIFAR10 vs CIFAR100 task

**Evidence**: "our results suggest that a near-distribution OE set is significantly more beneficial than a distant one... This replacement led to a notable decline in detection performance for ALOE and ATD on the CIFAR10 vs. CIFAR100 task, particularly under adversarial attack conditions"

## [POSITIVE] Diverse Outlier Exposure
Using OE samples that cover a wide variety of outlier directions in feature space, theoretically shown to reduce worst-case outlier detection error

**Delta**: Theorem 3.3 shows worst-case error reduces from 50% to 0% with infinitely diverse OE on hypersphere
**Condition**: Worst-case outlier detection scenario; theoretical Gaussian setup

**Evidence**: "if the OE is sampled from a Gaussian mixture, with infinitely many mixture components, whose means are sampled uniformly from the hypersphere S^{d-1}(r), then R(f*) = 0%... This simple example highlights the need for a diverse OE distribution in solving the outlier detection in the worst-case"

## [POSITIVE] Outlier Exposure Combined with Adversarial Training
Combining OE technique with adversarial training to expose the model to adversarial patterns in outlier data during training

**Delta**: ATOM, ALOE, ATD achieve relatively better results compared to methods without OE+adversarial training
**Condition**: Robust outlier detection under adversarial attacks

**Evidence**: "incorporating outlier exposure (OE) and adversarial training can be an effective strategy for this purpose... recent robust outlier detection methods use Outlier Exposure (OE) technique in combination with adversarial training to tackle this issue"

## [POSITIVE] CLIP Guidance for Diffusion Generation
Using CLIP image-text similarity gradients to guide the diffusion denoising process toward semantically distinct outlier labels while maintaining visual similarity to inliers

**Delta**: RODEO achieves FDC of 3.325 mean vs. DreamOOD 0.573 and GOE 0.613
**Condition**: Adaptive outlier generation stage; applied during diffusion denoising process

**Evidence**: "we propose the Lguidance(xgen, yn-outliers) loss, which aims to minimize the cosine similarity between the CLIP space embeddings of the generated image xgen and the target text... Through this guidance, the diffusion model is enforced to increase the similarity between the generated images and the extracted labels at each step"

## [POSITIVE] Image-Conditioned Diffusion (Pixel-Space Generation)
Starting the diffusion denoising process from noisy inlier images rather than pure Gaussian noise, operating in pixel space to shift inliers toward outliers

**Delta**: RODEO outperforms DreamOOD (which generates in embedding space) across all datasets; e.g., CIFAR10 ND: 87.4/70.2 vs DreamOOD 62.7/15.0 clean/PGD
**Condition**: Outlier generation for adversarial training; compared against DreamOOD

**Evidence**: "RODEO shifts data from inlier to outlier while operating in pixel space... Dream-OOD, despite leveraging both text and image information and being trained on a significantly larger dataset of 5 billion data points compared to RODEO's 67 million, underperforms due to its methodology of generating images in the embedding space"

## [POSITIVE] Random Initial Timestep for Diffusion
Randomly sampling the starting timestep t0 ~ U(0.3T, 0.6T) for the denoising process to control the degree of change from the inlier image

**Delta**: contributes to diversity of generated outliers (qualitative/design claim)
**Condition**: Adaptive outlier generation stage

**Evidence**: "Randomly choosing t0 for the denoising process leads to the generation of diverse outliers since, with smaller t0, inlier images undergo minor changes, while relatively larger t0 values lead to more significant changes, thereby increasing the diversity of generated outlier samples"

## [POSITIVE] Near-Outlier Label Extraction via Word2Vec + CLIP Threshold
Using Word2Vec to find semantically nearest neighbor labels to inlier classes, then filtering with a CLIP-based threshold to ensure labels are distinguishable from inliers

**Delta**: enables generation of semantically-level outlier samples that are conceptually distinct yet related to inliers
**Condition**: Near-outlier label extraction step; applied before generation

**Evidence**: "we utilize Word2Vec, a renowned and simple text encoder, to obtain the embeddings of the inlier labels... By comparing these with a pre-computed threshold (Δtext), we refine the extracted labels by excluding those very similar to the inlier labels"

## [POSITIVE] Negative Attribute Text Labels for Pixel-Level OOD
Incorporating texts with negative attributes of inlier labels (e.g., 'broken screw') to generate texture-level outliers in addition to semantic-level outliers

**Delta**: enhances diversity of synthesized outliers by adding pixel-level OOD samples
**Condition**: Near-outlier label extraction step; combined with semantic labels

**Evidence**: "we also consider pixel-level OOD samples (those that differ from the in-distribution at the texture level). For this purpose, we incorporate texts containing negative attributes of the inlier labels (e.g., 'broken screw'), and the union of these two sets of labels forms near outliers"

## [POSITIVE] CLIP Score Filtering of Generated Images
Filtering out generated images that score above a threshold CLIP similarity to the inlier label, to prevent in-distribution samples from being used as OE

**Delta**: prevents misleading training signal from in-distribution generated samples (qualitative/design claim)
**Condition**: Post-generation filtering step

**Evidence**: "There is a concern that generated images may still belong to the inlier distribution, which can potentially lead to misleading information in subsequent steps. To mitigate this issue, we have implemented a method that involves defining a threshold to identify and exclude data that falls within the in-distribution"

## [POSITIVE] Noisy-Image-Trained CLIP Model (GLIDE CLIP)
Using the smaller CLIP model from Nichol et al. (2021) trained on noisy images instead of the standard public CLIP model, to handle noisy intermediate diffusion images

**Delta**: avoids low-quality data generation caused by domain mismatch between noisy diffusion inputs and clean-image-trained CLIP
**Condition**: CLIP guidance during diffusion denoising with noisy intermediate images

**Evidence**: "Since the public CLIP model is trained on noise-free images, this discrepancy leads to the generation of low-quality data... Consequently, we opt for the smaller CLIP model proposed by (Nichol et al., 2021), which has been trained on noisy image datasets"

## [POSITIVE] Adversarial Training with Cross-Entropy Loss
Training a K+1 class classifier (K inlier classes + 1 OE class) with adversarial perturbations using PGD-10 inner maximization and Adam outer minimization

**Delta**: RODEO achieves mean ND adversarial AUROC of 63.5% vs near-zero for non-adversarially trained methods like EXOE (0.3% PGD)
**Condition**: Training phase; evaluated under PGD-1000, AutoAttack, Adaptive AutoAttack

**Evidence**: "We then adversarially train a classifier fθ with the standard cross-entropy loss... our experimental results show that utilizing our synthesized outliers significantly enhances the performance of the outlier detector, particularly in adversarial settings"

## [NEUTRAL] Softmax OOD Score (K+1 Logit)
Using the (K+1)-th logit of the classifier as the anomaly score, corresponding to the auxiliary outlier class

**Delta**: standard design choice enabling end-to-end adversarial evaluation
**Condition**: Test/inference phase for all outlier detection tasks

**Evidence**: "During test time, we utilize the (K + 1)-th logit of fθ as the anomaly score, which corresponds to the class of auxiliary outliers in the training phase"

## [NEGATIVE] Distant OE (e.g., SVHN, MNIST, Gaussian Noise as OE for CIFAR tasks)
Using OE datasets whose distribution is far from the inlier distribution

**Delta**: notable decline in detection performance for ALOE and ATD, particularly under adversarial attack conditions
**Condition**: Adversarial outlier detection; CIFAR10 vs CIFAR100 task with ALOE and ATD

**Evidence**: "This replacement led to a notable decline in detection performance for ALOE and ATD on the CIFAR10 vs. CIFAR100 task, particularly under adversarial attack conditions. We attribute this performance drop to the fact that the SVHN, MNIST, and Gaussian Noise distributions are more distant from CIFAR10"

## [NEGATIVE] DreamOOD (Embedding-Space Generation with Stable Diffusion)
Generating outliers by sampling from low-likelihood regions of the inlier distribution in the latent embedding space using Stable Diffusion trained on 5 billion samples

**Delta**: CIFAR10 ND clean/PGD: 62.7/15.0 vs RODEO 87.4/70.2; mean FDC 0.573 vs RODEO 3.325
**Condition**: Ablation study; ND setting across CIFAR10, MNIST, FMNIST, MVTec-AD, Head-CT, Covid19

**Evidence**: "Dream-OOD, despite leveraging both text and image information and being trained on a significantly larger dataset of 5 billion data points compared to RODEO's 67 million, underperforms due to its methodology of generating images in the embedding space. This approach is less suited for synthesizing pixel-level outliers and often leads to the generation of samples with different styles, i.e., far outliers, attributed to the bias of its backbone trained on LAION"

## [NEGATIVE] FITYMI OE Method
Generating OE using a diffusion model trained on inliers, halted early to create synthetic images resembling inliers with clear differences, using only image domain information

**Delta**: mean clean/PGD: 56.3/20.6 vs RODEO 85.1/65.6; mean FDC 0.249 vs RODEO 3.325
**Condition**: Ablation study; ND setting

**Evidence**: "FITYMI considers image domain information exclusively... alternative OE methods underperform compared to RODEO in enhancing robust outlier detection, closeness to in-distribution, and diversity"

## [NEGATIVE] Baseline OE with ImageNet
Using a fixed random dataset (ImageNet) as the outlier exposure set without any adaptation to the inlier distribution

**Delta**: mean clean/PGD: 64.2/29.4 vs RODEO 85.1/65.6; FDC 0.613 vs RODEO 3.325
**Condition**: Ablation study; ND setting

**Evidence**: "the Baseline OE technique, which involves leveraging outliers from a presumed dataset, leads to unsatisfactory results in situations where the auxiliary exposed outliers deviate significantly from the in-distribution"

## [NEGATIVE] Baseline OE with Gaussian Noise
Using Gaussian noise samples as the outlier exposure set

**Delta**: mean clean/PGD: 62.4/22.7 vs RODEO 85.1/65.6; FDC 0.573 vs RODEO 3.325
**Condition**: Ablation study; ND setting

**Evidence**: "alternative OE methods underperform compared to RODEO in enhancing robust outlier detection, closeness to in-distribution, and diversity"

## [NEGATIVE] Adversarial Training Without OE
Standard adversarial training on inlier data only, without any outlier exposure

**Delta**: AT* OSR clean/PGD on CIFAR10: 65.2/20.6 vs RODEO 79.6/62.7
**Condition**: OSR and OOD detection tasks; AT* indicates model trained without OE

**Evidence**: "adversarial training, which is the augmentation of training samples with adversarial perturbations, is among the best practices for making models robust. However, this approach is less effective in outlier detection, as outlier patterns are unavailable during training"

## [NEGATIVE] Clean (Non-Adversarial) Training
Training outlier detectors without adversarial perturbations, using only standard empirical risk minimization

**Delta**: EXOE achieves 86.5% clean but drops to 0.3% under PGD; ViT-MSP achieves 96.8% clean but 1.6% under PGD on CIFAR10 OSR
**Condition**: Adversarial evaluation settings (PGD-1000, AutoAttack, Adaptive AutoAttack)

**Evidence**: "they often suffer significant performance drops when subjected to adversarial attacks... EXOE, which utilizes pretrained CLIP. While achieving 86.5% in clean settings, it experiences a substantial drop to 0.3% in adversarial settings"

## [NEGATIVE] Adversarial Training (Robustness-Accuracy Tradeoff)
The inherent tradeoff where adversarial training improves robustness but reduces clean performance

**Delta**: RODEO clean ND mean 83.7% vs EXOE 86.5%; clean OSR CIFAR10: RODEO 79.6% vs PLP 94.1%
**Condition**: Clean evaluation settings when adversarial training is applied

**Evidence**: "our clean performance still lags behind existing state-of-the-art methods. The tradeoff between clean and adversarial test performance is well-documented in the literature"
