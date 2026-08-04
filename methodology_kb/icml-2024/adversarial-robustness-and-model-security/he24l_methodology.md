# Be Your Own Neighborhood: Detecting Adversarial Examples by the Neighborhood Relations Built on Self-Supervised Learning

**Source**: https://proceedings.mlr.press/v235/he24l.html

## [POSITIVE] Self-Supervised Learning (SSL) for Feature Extraction
Using a pre-trained SSL model (SimSiam) as the feature extractor instead of a supervised learning model, leveraging its representation consistency under different augmentations

**Delta**: outperforms baselines
**Condition**: AE detection on CIFAR-10, CIFAR-100, and ImageNet

**Evidence**: "An off-the-shelf Self-Supervised Learning (SSL) model is used to extract the representation and predict the label for its highly informative representation capacity compared to supervised learning models."

## [POSITIVE] Label Consistency Detection Mechanism
Comparing the classifier's prediction on the input image with SSL classification head predictions on augmented neighbors; flagging as AE if consistency falls below threshold

**Delta**: outperforms single-mechanism baseline
**Condition**: Most effective for small perturbation budgets

**Evidence**: "When the perturbation is small, the detection performance based on label consistency (blue line) is better than representation similarity (green line)."

## [POSITIVE] Representation Similarity Detection Mechanism
Using cosine similarity to measure similarity between input image representation and its augmented neighbors' representations; flagging as AE if similarity falls below threshold

**Delta**: outperforms single-mechanism baseline
**Condition**: Most effective for large perturbation budgets

**Evidence**: "As perturbation increases, representation similarity is difficult to maintain, leading to higher performance of representation similarity-based detectors."

## [POSITIVE] Combined Label Consistency and Representation Similarity
Using both detection mechanisms together, exploiting their contradictory optimization directions to hinder adaptive attacks

**Delta**: superior performance (red line) over individual mechanisms
**Condition**: Adaptive attacks on CIFAR-10, CIFAR-100, and ImageNet

**Evidence**: "The detection performance of the two combined can exceed any of the individuals. More importantly, their contradictory optimization directions hinder adaptive attacks to bypass both of them simultaneously."

## [POSITIVE] Augmentation-Based Neighbor Generation
Generating 50 neighbors per input using augmentations (horizontal flipping, cropping, color jitter, grayscale) consistent with SimSiam, with fixed random seed

**Delta**: outperforms baselines by large margin
**Condition**: All datasets and attack types

**Evidence**: "BEYOND is the first work that leverages an SSL model for AE detection without prior knowledge of adversarial attacks or AEs."

## [NEUTRAL] Fixed Random Seed for Neighbor Generation
Fixing the random seed when generating augmented neighbors to prevent benefiting from randomization

**Delta**: None
**Condition**: Neighbor generation during detection

**Evidence**: "However, BEYOND fixes the random seed to prevent benefiting from randomization."

## [POSITIVE] K=50 Neighbors
Selecting 50 augmented neighbors per input as the default configuration

**Delta**: performance plateaus beyond K=50
**Condition**: Standard (non-adaptive) attack detection

**Evidence**: "We choose 50 neighbors for BEYOND, since larger neighbors no longer significantly enhance performance, as shown in Fig. 3."

## [POSITIVE] Smaller K for Adaptive Attack Robustness
Using fewer neighbors increases diversity among neighbors, complicating the optimization process for adaptive attacks

**Delta**: adaptive attacks less effective with smaller K
**Condition**: Adaptive attack setting

**Evidence**: "Contrary to intuition, adaptive attacks are less effective with a smaller K. This is because only four linear transformations are deployed in BEYOND, where varying neighbors simply involve different transformation parameters. With a smaller K, the diversity among neighbors is pronounced, complicating the optimization process for adaptive attacks."

## [NEGATIVE] Larger K for Adaptive Attack Vulnerability
Using more neighbors results in similar neighbors that provide more information for adaptive attacks to exploit

**Delta**: None
**Condition**: Adaptive attack setting

**Evidence**: "Conversely, a larger K potentially results in similar neighbors that provide a wealth of information for adaptive attacks to exploit for each transformation."

## [POSITIVE] Plug-and-Play Integration with Adversarial Trained Classifier (ATC)
Combining BEYOND with existing adversarially trained classifiers without retraining

**Delta**: RA improved from 66.20% to 84.40% (R2021Fixing70), clean accuracy from 92.23% to 92.83%
**Condition**: CIFAR-10 against AutoAttack

**Evidence**: "Table 3 shows the accuracy on clean samples and RA against AutoAttack of ATC combined with BEYOND on CIFAR-10. As can be seen the addition of BEYOND increases the robustness of ATC by a significant margin on both clean samples and AEs."

## [POSITIVE] ATC+BEYOND against Orthogonal-PGD
Combining adversarially trained classifier with BEYOND for adaptive attack defense

**Delta**: RA improved from 13.80% to 94.50% at L∞=8/255 (FPR5%)
**Condition**: Orthogonal-PGD adaptive attack at L∞=8/255

**Evidence**: "Furthermore, incorporating ATC can significantly improve the detection performance of BEYOND against large perturbation to 94.5%."

## [POSITIVE] No Prior Knowledge of AEs Required
BEYOND does not require adversarial examples for training or threshold selection, using only clean samples at FPR@5%

**Delta**: same performance on seen and unseen attacks
**Condition**: Generalization to unseen attacks

**Evidence**: "Note that BEYOND needs no AE for training, leading to the same value on both seen and unseen settings."

## [POSITIVE] Conflicting Optimization Goals for Adaptive Attack Resistance
Label consistency requires larger perturbations while representation similarity requires smaller perturbations, causing gradient cancellation when attacking both simultaneously

**Delta**: single-objective adaptive attack can break defense; dual-objective attack performance decreases
**Condition**: Adaptive attacks attempting to bypass both mechanisms

**Evidence**: "Since the classification C and representation head R share the same backbone f, optimizing for these conflicting goals can lead to gradient cancellation, which underpins the robustness of BEYOND against adaptive attacks."

## [NEUTRAL] Expectation over Transformation (EoT) for Adaptive Attack
Using EoT to estimate the impact of multiple augmentations on label consistency and representation similarity during adaptive attack formulation

**Delta**: None
**Condition**: Adaptive attack evaluation

**Evidence**: "Since BEYOND uses multiple augmentations, we estimate their impact on label consistency and representation similarity during the adaptive attack following Expectation over Transformation (EoT)."

## [POSITIVE] Alpha=1 Trade-off Parameter
Setting the hyperparameter alpha=1 as the trade-off between label consistency and representation similarity in the adaptive attack objective

**Delta**: most effective adaptive attack at alpha=1
**Condition**: Adaptive attack configuration

**Evidence**: "Experiments in the Appendix show that the adaptive attack is most effective when α = 1."

## [POSITIVE] MoCo v3 SSL Backbone
Using MoCo v3 (with ViT backbone) as the SSL model instead of SimSiam

**Delta**: MoCo v3 generally yields best results on CIFAR-10 and CIFAR-100 (e.g., 98.54% vs 97.17% FGSM AUC on CIFAR-10)
**Condition**: CIFAR-10 and CIFAR-100 detection

**Evidence**: "On CIFAR-10 and CIFAR-100, MoCo v3 generally yields the best results, followed closely by SimSiam and BYOL."

## [POSITIVE] SimSiam SSL Backbone
Using SimSiam as the default SSL backbone due to accessibility of pretrained weights

**Delta**: 97.17% AUC on FGSM CIFAR-10
**Condition**: Default configuration across all datasets

**Evidence**: "Since SimSiam's pretrained weights are more accessible than MoCo v3, we choose SimSiam as the backbone in this paper."

## [NEGATIVE] Clustering-Based SSL Models (SwAV, DeepCluster v2)
Using clustering-based contrastive learning SSL models that learn similarity to cluster centers rather than directly between samples and augmentations

**Delta**: SwAV and DeepCluster v2 perform slightly lower than other SSL models on CIFAR-10 and CIFAR-100
**Condition**: CIFAR-10 and CIFAR-100 detection

**Evidence**: "SwAV and DeepCluster v2 perform slightly lower than the other SSL models on CIFAR-10 and CIFAR-100. This is due to the fact that SwAv and DeepCluster v2 are clustering-based contrastive learning methods, which do not directly learn the representation similarity between input samples and their augmentations."

## [POSITIVE] Faster Inference via Neighbor Comparison (No Reference Set)
BEYOND compares relationships only between neighbors without calculating distance to an external reference set, reducing inference time

**Delta**: 1.12s vs 9.22s for LNG (inference time)
**Condition**: Implementation cost comparison

**Evidence**: "BEYOND only compares the relationship between neighbors without calculating the distance with the reference set, resulting in a faster inference speed than that of LNG."

## [POSITIVE] FPR@5% Threshold Selection
Setting detection thresholds by fixing False Positive Rate at 5%, determined only by clean samples

**Delta**: None
**Condition**: Threshold calibration for all experiments

**Evidence**: "Note that, we select the thresholds, i.e. Tlabel, Trep, by fixing the False Positive Rate (FPR)@5%, which can be determined only by clean samples, and the implementation of our method needs no prior knowledge about AE."

## [NEGATIVE] Large Perturbation Budget Vulnerability
BEYOND can be bypassed when adversarial perturbations are large enough to circumvent the transformation

**Delta**: BEYOND completely broken at perturbation budget > 16/255
**Condition**: Adaptive attacks with large perturbation budgets (>16/255)

**Evidence**: "BEYOND can be bypassed when perturbations are large enough, due to large perturbations circumventing the transformation. This proves that BEYOND is not gradient masking."
