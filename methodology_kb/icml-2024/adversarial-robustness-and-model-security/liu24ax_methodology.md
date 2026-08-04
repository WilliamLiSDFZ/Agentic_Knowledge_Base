# Fast Decision Boundary based Out-of-Distribution Detector

**Source**: https://proceedings.mlr.press/v235/liu24ax.html

## [POSITIVE] Closed-form Decision Boundary Distance Estimation
A closed-form analytical lower bound for the L2-distance from a feature embedding to a class decision boundary in the penultimate layer, computed as the absolute logit difference divided by the norm difference of classifier weight vectors.

**Delta**: relative error less than 1.5% vs iterative optimization; 0.53ms vs 992.2ms per image
**Condition**: Applied at inference time on the penultimate layer of any pre-trained classifier with a linear head

**Evidence**: "our method incurs negligible inference overhead. In particular, on a Tesla T4 GPU, the average inference time on the CIFAR-10 classifier is 0.53ms per image with or without computing the distance using our method. In contrast, the alternative way of estimating the distance through iterative optimization takes 992.2ms under the same setup."

## [POSITIVE] Feature Deviation Regularization (regDistDB)
Regularizing the average feature distance to decision boundaries by dividing by the feature distance to the mean of training features, effectively comparing ID and OOD samples at equal deviation levels from the training feature mean.

**Delta**: regDistDB outperforms avgDistDB across all four ImageNet OOD datasets (e.g., iNaturalist AUROC 93.67 vs 90.51)
**Condition**: Applied on ImageNet OOD benchmark with ResNet-50 trained under cross-entropy loss

**Evidence**: "regularization with respect to ∥z − µtrain∥2 enhances ID/OOD separation. Consequently, regDistDB improves over avgDistDB and achieves higher AUROC, as shown in Table 5."

## [POSITIVE] Feature Distance to Decision Boundaries as OOD Score
Using the minimum perturbation magnitude needed to change the classifier's prediction (distance to decision boundary in penultimate feature space) as an OOD detection signal, based on the observation that ID features reside further from decision boundaries than OOD features.

**Delta**: fDBD reduces average FPR95 of MSP by 29.69% (relatively 48.85% reduction) and of Energy by 13.78% (relatively 30.73% reduction) on CIFAR-10
**Condition**: CIFAR-10 OOD benchmark on ResNet-18 trained with cross-entropy loss

**Evidence**: "on the model trained with cross-entropy loss, our fDBD reduces the average FPR95 of MSP by 29.69%, which is a relatively 48.85% reduction in error. Additionally, fDBD reduces the average FPR95 of Energy by 13.78%, resulting in a relatively 30.73% reduction in error."

## [POSITIVE] Averaging Distances Over All Unpredicted Classes
Computing the OOD detection score as the average of feature distances to decision boundaries for all classes other than the predicted class, rather than using only the nearest boundary distance.

**Delta**: performance improves monotonically as k increases from 1 to all classes (k=9 on CIFAR-10, k=999 on ImageNet)
**Condition**: Ablation study on CIFAR-10 and ImageNet benchmarks with ResNets trained under cross-entropy loss

**Evidence**: "Looking into Figure 4, the performance improves with increasing number of k. This justifies our design of fDBD as a hyper-parameter-free method, utilizing all distances for OOD detection."

## [POSITIVE] Hyperparameter-free Design
fDBD requires no hyperparameter tuning, unlike methods such as ODIN, MDS, and KNN which require hyperparameter selection and potentially additional data.

**Delta**: eliminates pre-inference tuning cost; achieves state-of-art FPR95 of 11.85 avg on CIFAR-10 with SupCon vs KNN+ at 12.18
**Condition**: Applicable across all benchmarks and training schemes

**Evidence**: "our fDBD eliminates the pre-inference cost of tuning hyper-parameter and the potential requirement for additional data."

## [POSITIVE] Auxiliary Model-free Inference
fDBD does not build auxiliary models (e.g., Gaussian fits, KNN indices) from training features, avoiding the associated storage and computational overhead at inference time.

**Delta**: 0.53ms latency vs 1.95ms for KNN and 2.83ms for MDS on CIFAR-10
**Condition**: CIFAR-10 benchmark on ResNet-18, Tesla T4 GPU

**Evidence**: "fDBD has minimal computational overhead: the original classifier takes 0.53 milliseconds per image, and with fDBD, the processing time remains the same."

## [POSITIVE] Supervised Contrastive Loss Training
Training the feature extractor with supervised contrastive loss (SupCon) instead of standard cross-entropy loss, producing better-separated feature representations.

**Delta**: fDBD avg FPR95 improves from 31.09 (cross-entropy) to 11.85 (SupCon) on CIFAR-10; from 51.19 to 37.79 on ImageNet
**Condition**: CIFAR-10 and ImageNet benchmarks; consistent across fDBD and other feature-space methods

**Evidence**: "we observe that OOD detection significantly improves under contrastive learning. This aligns with the study by Sun et al. (2022), showing that contrastive learning better separates ID and OOD features."

## [POSITIVE] Activation Shaping with ReAct
Replacing standard ReLU activation with rectified activations (ReAct) at the 80th percentile to shape feature activations and improve ID/OOD separation before applying fDBD.

**Delta**: avg FPR95 improves from 51.19 (ReLU) to 30.39 (ReAct) on ImageNet; avg AUROC from 89.26 to 93.76
**Condition**: ImageNet OOD benchmark on ResNet-50 trained with cross-entropy loss

**Evidence**: "With activation shaping applied both to test features and the mean of training feature in Equation 8, we observe improved performance across OOD datasets, validating the compatibility of fDBD with ReAct, ASH, and Scale."

## [POSITIVE] Activation Shaping with ASH
Replacing standard ReLU with ASH (Extremely Simple Activation Shaping) at the 90th percentile to shape feature activations before applying fDBD.

**Delta**: avg FPR95 improves from 51.19 (ReLU) to 24.44 (ASH) on ImageNet; avg AUROC from 89.26 to 94.87
**Condition**: ImageNet OOD benchmark on ResNet-50 trained with cross-entropy loss

**Evidence**: "With activation shaping applied both to test features and the mean of training feature in Equation 8, we observe improved performance across OOD datasets, validating the compatibility of fDBD with ReAct, ASH, and Scale."

## [POSITIVE] Activation Shaping with Scale
Replacing standard ReLU with Scale activation shaping at the 90th percentile before applying fDBD, achieving the best overall performance among activation shaping variants.

**Delta**: avg FPR95 improves from 51.19 (ReLU) to 20.85 (Scale) on ImageNet; avg AUROC from 89.26 to 95.61
**Condition**: ImageNet OOD benchmark on ResNet-50 trained with cross-entropy loss

**Evidence**: "fDBD with Scale achieves the state-of-art performance on this benchmark, comparable to Energy with Scale."

## [NEGATIVE] Feature Deviation Distance Alone as OOD Score
Using only the distance from the feature to the training feature mean (∥z − µtrain∥2) as the OOD detection score, without incorporating decision boundary distances.

**Delta**: AUROC scores around 50 across all four ImageNet OOD datasets (e.g., iNaturalist 47.84, SUN 58.59, Places 58.95, Texture 41.92)
**Condition**: ImageNet OOD benchmark ablation study on ResNet-50 with cross-entropy loss

**Evidence**: "∥z − µtrain∥2 alone does not necessarily distinguish between ID and OOD samples, as indicated by AUROC scores around 50."

## [NEGATIVE] Unregularized Average Distance to Decision Boundaries (avgDistDB)
Using the raw average feature distance to decision boundaries as the OOD score without regularization by feature deviation from the training mean.

**Delta**: avgDistDB AUROC: iNaturalist 90.51, SUN 85.55, Places 83.05, Texture 86.79 vs regDistDB: 93.67, 86.97, 84.27, 92.12
**Condition**: ImageNet OOD benchmark ablation study on ResNet-50 with cross-entropy loss

**Evidence**: "regDistDB improves over avgDistDB and achieves higher AUROC, as shown in Table 5. This supports our intuition in Section 3 to compare ID/OOD at equal deviation levels through regularization."

## [NEGATIVE] Output Space Softmax Confidence (MSP)
Baseline method using maximum softmax probability as OOD score, operating in the output space without leveraging penultimate feature space information.

**Delta**: avg FPR95 of 60.78 vs fDBD's 31.09 on CIFAR-10 cross-entropy; 66.95 vs 51.19 on ImageNet cross-entropy
**Condition**: Compared against fDBD on CIFAR-10 and ImageNet benchmarks

**Evidence**: "our fDBD reduces the average FPR95 of MSP by 29.69%, which is a relatively 48.85% reduction in error."

## [NEGATIVE] Mahalanobis Distance (MDS) Auxiliary Model
Fitting a multivariate Gaussian over training features and using Mahalanobis distance as OOD score; requires building and storing an auxiliary model from training statistics.

**Delta**: latency 2.83ms vs 0.53ms for fDBD on CIFAR-10; avg FPR95 36.35 vs 31.09 for fDBD; on ImageNet avg FPR95 87.43 vs 51.19
**Condition**: CIFAR-10 and ImageNet benchmarks; MDS performs particularly poorly on ImageNet

**Evidence**: "MDS reports an inference latency of 2.83ms... fDBD significantly outperforms KNN on ImageNet OOD benchmark in Table 2"

## [POSITIVE] Linear Complexity Scaling (O(|C| + P))
fDBD's computational complexity scales linearly with the number of classes |C| and feature dimension P, enabling scalability to large datasets and models.

**Delta**: latency remains 6.81ms on ImageNet (1000 classes) vs 0.53ms on CIFAR-10 (10 classes), both negligible overhead over base inference
**Condition**: Theoretical guarantee; empirically validated on CIFAR-10 and ImageNet

**Evidence**: "fDBD has time complexity O(|C| + P), which scales linearly with the number of training classes |C| and the dimension P, indicating computational scalability for larger datasets and models."
