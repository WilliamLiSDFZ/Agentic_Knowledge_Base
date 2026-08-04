# One for All: A Universal Generator for Concept Unlearnability via Multi-Modal Alignment

**Source**: https://proceedings.mlr.press/v235/chen24bc.html

## [POSITIVE] Universal Perturbation Generator (One-for-All / I4A)
A single universal generator trained once on ImageNet that produces perturbations for any input image without retraining, using multi-modal embeddings as concept guidance instead of class labels or uniform noise.

**Delta**: outperforms baselines in most cross-dataset and label-agnostic scenarios
**Condition**: Cross-dataset transferability and label-agnostic scenarios on domain-specific datasets (Pets, Flowers, Cars, Food, Sun)

**Evidence**: "In most cases, 14A consistently outperforms baselines across various backbones, demonstrating its robustness and resilience to different adversary models."

## [POSITIVE] CLIP-based Multi-Modal Embedding
Using CLIP's shared image-text embedding space to connect image data with textual concepts, enabling label-free concept extraction and eliminating the need for a surrogate model.

**Delta**: eliminates surrogate model requirement; enables zero-shot generation
**Condition**: Label-agnostic and cross-dataset settings where class labels are unavailable or inconsistent

**Evidence**: "CLIP is pre-trained with textual descriptions rather than one-hot labels, mitigating overfitting to specific class labels and enhancing the extractability of underlying concepts. Consequently, this design makes CLIP a great concept-extraction model for describing the main content of images."

## [POSITIVE] Concept-wise Discriminant Loss
A loss function that exaggerates intra-concept distance (pushes data away from similar concepts) while diminishing inter-concept distance (pulls data toward opposite concepts), using addition form instead of multiplication to handle dispersed embedding scales.

**Delta**: outperforms class-wise discriminant loss baseline in concept unlearnability
**Condition**: Training the I4A generator for concept unlearnability

**Evidence**: "we align the text embedding using conceptwise discriminant loss, and render the data unlearnable... a lower concept-wise discriminant indicates a larger intra-concept distance and a smaller inter-concept distance. This characteristic enhances the ability to trick the adversary model, rendering the data unlearnable."

## [POSITIVE] Addition Form in Concept-wise Loss (vs. Multiplication)
Using addition to combine intra-concept and inter-concept distance terms in the loss function instead of multiplication, to avoid the denominator becoming infinitely large when concepts are widely dispersed.

**Delta**: prevents all-black perturbation artifact
**Condition**: Concept-wise discriminant loss computation when embedding space distances vary in scale

**Evidence**: "we choose the addition form instead of the multiplication form. This decision is driven by the fact that concepts are widely dispersed across the embedding space, resulting in different scales for intra-concept and inter-concept distances. By using the addition form, we avoid the issue of the intra-concept distance (denominator) becoming infinitely large, which would lead to an all-black perturbation."

## [POSITIVE] Top-k Similar Concept Selection (k=5)
Selecting only the top-k most similar concepts rather than traversing all labels, reducing computational complexity while maintaining effectiveness. k=5 was found optimal.

**Delta**: k=5 achieves smallest cosine similarity (greatest separation from similar concepts); multiple k>1 significantly accelerates convergence speed
**Condition**: Concept-wise discriminant loss training; k=1 converges slower and to higher loss

**Evidence**: "introducing multiple similar concepts (k > 1) significantly accelerates coverage speed; and iii) Among the tested values, k = 4 and k = 5 converge to relatively lower loss values... we select k = 5 as it has the smallest cosine similarity, indicating a greater separation from similar concepts."

## [POSITIVE] Opposite and Similar Concept Targeting
Determining both the most dissimilar (opposite) and most similar concepts in the shared embedding space as alignment targets to enhance robustness and transferability of perturbations.

**Delta**: enhances robustness and transferability of generated perturbations
**Condition**: Target embedding alignment step during I4A generator training

**Evidence**: "we explore both opposite and similar concepts to enhance the robustness and transferability of the generated perturbations... we push the data away from its similar concepts, creating a clear distinction between the original concept and other similar ones. On the other hand, we guide the data towards the opposite concept, misleading the adversary model into learning irrelevant concept."

## [POSITIVE] Generator-based Perturbation Approach
Using an encoder-decoder generator network to produce dynamic per-image perturbations, as opposed to gradient-based bi-level optimization methods that generate static statistical perturbations.

**Delta**: significant efficiency advantage over gradient-based methods
**Condition**: Inference time perturbation generation; compared to CP and TUE gradient-based baselines

**Evidence**: "Once trained, this generator enables input from any sample, providing significant efficiency advantages over gradient-based methods and multi-generator methods."

## [POSITIVE] Image Embedding as Generator Input (replacing uniform noise)
Incorporating CLIP image embeddings as concept information input to the generator instead of uniform noise, enabling the universal generator to handle diverse concepts beyond a single cluster.

**Delta**: enables one-generator-for-all-concepts vs. one-generator-per-cluster
**Condition**: Universal generator design for cross-dataset and label-agnostic scenarios

**Evidence**: "To construct a universal generator, we propose to incorporate concept information as input, which serves as a guide for the generator in place of uniform noise. This concept information is expected to operate beyond the original label, as our goal is to achieve unlearnability that transcends the confines imposed by specific datasets or labels."

## [POSITIVE] Elimination of Surrogate Model
Removing the surrogate adversary model used in prior work by directly aligning visual embeddings with textual embeddings to create shortcuts, simplifying the perturbation generation process.

**Delta**: simplifies perturbation generation process
**Condition**: I4A generator training pipeline

**Evidence**: "we propose to eliminate the surrogate model altogether and directly align the visual embeddings with the textual embeddings to create a shortcut, thereby rendering the data unlearnable. This approach fully explores the multi-modal property and simplifies the process of generating perturbations."

## [POSITIVE] Deeper Encoder-Decoder Generator Architecture
Increasing the depth of the autoencoder generator network compared to prior work (LaUE), with CLIP image embedding concatenated at the encoded layer.

**Delta**: demonstrates effectiveness in empirical study
**Condition**: I4A generator architecture design

**Evidence**: "we improve the structure of the autoencoder generator in the existing generator-based approach (Zhang et al., 2023). This improvement involves increasing the depth of the network. Additionally, we concatenate the encoded embedding with the image embedding generated by CLIP to provide concept information."

## [NEGATIVE] Resizing Module for Low-Resolution Images
Adding a resizing module before the I4A generator to handle images of different sizes (e.g., 32x32 CIFAR images) since the generator is designed for 224x224 ImageNet images.

**Delta**: performance degradation on low-resolution images; CIFAR10 and CIFAR100 accuracy still decreases by 58.5% and 70.1% vs. clean but worse than gradient-based methods
**Condition**: Low-resolution images (32x32 CIFAR10/CIFAR100) requiring resizing to match generator input dimensions

**Evidence**: "14A's performance on low-resolution images is not as strong as its performance on other domain-specific datasets. This is primarily due to the loss of image details caused by resizing, which affects both the embedding modeling by CLIP and the perturbation generation by our generator."

## [POSITIVE] Large-scale Backbone Adversary Models
Evaluating unlearnability against larger backbone models (ResNet50, VGG16, ViT) with superior feature extraction capabilities.

**Delta**: average improvement of 41.91% for larger models vs. 27.01% for smaller models
**Condition**: Cross-dataset and label-agnostic scenario with large-scale backbone adversary models

**Evidence**: "We observe a significant advantage of 14A over the baselines when tested on these larger models, with an average improvement of 41.91% compared to 27.01% for smaller models. We hypothesize that the superior feature extraction capabilities of larger models make them more vulnerable to the shortcut perturbations generated by our method."

## [NEGATIVE] Mixup Attack Against Unlearnable Examples
Data augmentation attack using Mixup to attempt to learn from unlearnable examples by mixing training samples.

**Delta**: +45.92% average accuracy increase after attack
**Condition**: Attack robustness evaluation under cross-dataset and label-agnostic settings; average post-attack accuracy still only 16.91%

**Evidence**: "among the three attacking methods (Mixup, Gaussian, OPA), Mixup and Gaussian attacks increase accuracy by 45.92% and 24.80% respectively... Mixup and Gaussian attacks are effective to some extent."

## [NEGATIVE] Gaussian Smoothing Attack Against Unlearnable Examples
Data augmentation attack using Gaussian smoothing to attempt to remove perturbations from unlearnable examples.

**Delta**: +24.80% average accuracy increase after attack
**Condition**: Attack robustness evaluation under cross-dataset and label-agnostic settings; average post-attack accuracy still only 16.91%

**Evidence**: "among the three attacking methods (Mixup, Gaussian, OPA), Mixup and Gaussian attacks increase accuracy by 45.92% and 24.80% respectively... Mixup and Gaussian attacks are effective to some extent."

## [POSITIVE] Orthogonal Projection Attack (OPA)
An attack tailored for unlearnable examples that leverages linear separability of perturbations to remove their effect.

**Delta**: -16.89% accuracy decrease after OPA attack (i.e., OPA makes data more unlearnable)
**Condition**: Attack robustness evaluation; OPA is ineffective against I4A because I4A does not use linear separable perturbations

**Evidence**: "OPA decreases it by 16.89%, suggesting that... OPA's negative impact on testing accuracy further solidifies the unlearnability of the data. This is attributed to OPA leveraging linear separability for attacks. However, our proposed method is based on concept transferring rather than linear separable perturbations."

## [NEUTRAL] k-means Clustering with 20 Clusters for Label-agnostic Setting
Using k-means clustering on CLIP text embeddings of original labels to create 20 pseudo-label clusters for the label-agnostic evaluation scenario.

**Delta**: stable clustering metrics across most datasets; 20 clusters chosen as balance between label inconsistency and concept preservation
**Condition**: Label-agnostic evaluation setup for datasets with 37-397 label categories

**Evidence**: "To strike a balance, we select 20 clusters for all datasets... Increasing the number of clusters generally improves performance, aligning with previous findings that more clusters can overlap with the original labels. However, a smaller number of clusters emphasizes the impact of inconsistent labels on unlearnable examples."

## [NEGATIVE] Training on Cars Dataset (low image count in ImageNet)
The Cars dataset has relatively few images in ImageNet, limiting effective generator training for car-specific concepts.

**Delta**: I4A does not outperform baselines on Cars dataset
**Condition**: Cross-dataset evaluation on the Cars dataset specifically

**Evidence**: "Except Cars, 14A consistently outperforms baselines across different datasets. There are two primary reasons: i) the relatively small number of car images in ImageNet hinders the effective training of the generator specifically for car images; and ii) the slight variation in image sizes within Cars necessitates the inclusion of a resizing module, which in turn affects our overall performance."
