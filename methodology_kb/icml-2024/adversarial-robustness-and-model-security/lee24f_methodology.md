# DataFreeShield: Defending Adversarial Attacks without Training Data

**Source**: https://proceedings.mlr.press/v235/lee24f.html

## [POSITIVE] Diversified Sample Synthesis (DSS)
A synthetic data generation technique that dynamically modulates synthesis loss coefficients by randomly sampling them from a uniform distribution for every batch, rather than using fixed hyperparameters, to maximize diversity of generated samples.

**Delta**: +5.06% AA on CIFAR-10 WRN-28-10 over fixed coefficient baseline (41.40% vs 36.34%)
**Condition**: Data-free adversarial robustness setting; compared against fixed-coefficient synthesis and augmentation methods like Mixup, Cutout, CutMix

**Evidence**: "In terms of robustness, it is clear that DSS outperforms all other diversification methods in terms of AAA."

## [POSITIVE] GradRefine
A gradient refinement technique that computes an agreement score across minibatches for each parameter and masks out high-fluctuating gradients where no sign dominates, promoting flatter loss surfaces and better generalization.

**Delta**: +6.17%p to +20.62%p gain under AutoAttack on CIFAR-10 across models when combined with other components
**Condition**: Applied during adversarial training with synthetic data; most beneficial for smaller models (ResNet-20 shows largest gain)

**Evidence**: "GradRefine adds a similar improvement, resulting in 6.17%p to 20.62%p gain altogether under AutoAttack."

## [POSITIVE] LDFShield Training Objective
A soft-label guided training loss using KL-divergence from the teacher model instead of hard labels, consisting of three terms: clean accuracy optimization, adversarial robustness learning, and a smoothness regularization term penalizing rapid output changes.

**Delta**: +12.58 AA on ResNet-20 CIFAR-10 over TRADES baseline (14.61% vs 2.03%)
**Condition**: Data-free adversarial training with synthetic data; compared against STD, TRADES, MART, ARD, RSLAD

**Evidence**: "LDFShield achieves the best results under both PGD-10 and AutoAttack in both datasets. The trend is consistent across different datasets and models."

## [NEGATIVE] LDFShield alone (without DSS)
Applying only the LDFShield training objective without the diversified sample synthesis component.

**Delta**: -1.62 AA on WRN-28-10 CIFAR-10 compared to TRADES baseline (36.34% vs 37.96%)
**Condition**: Applied in isolation on WRN-28-10 without DSS or GradRefine

**Evidence**: "Applying LDFShield, seems to slightly degrade AAA on WRN-28-10, but when combined with the other techniques, it results in better performance as shown in Table 7."

## [NEGATIVE] MART Loss in Data-Free Setting
Using the MART adversarial training objective, which encourages learning from misclassified samples, in the data-free synthetic data training setting.

**Delta**: Near-zero robustness: 1.09% AA on SVHN, 0.09% AA on CIFAR-10 with WRN-28-10
**Condition**: Data-free adversarial training with synthetic data on SVHN and CIFAR-10

**Evidence**: "Interestingly, MART provides almost no robustness in our problem. MART encourages learning from misclassified samples, which may lead the model to overfit on synthetic samples."

## [NEGATIVE] Using Similar-Domain Real Datasets for AT
Using an alternative real dataset from a similar domain (e.g., another biomedical dataset) for adversarial training when the original training data is unavailable.

**Delta**: Large degradation compared to diagonal (original dataset) cells in cross-dataset robustness matrix
**Condition**: Biomedical image classification datasets; cross-domain adversarial training with PGD-10 l-inf eps=8/255

**Evidence**: "It is clear that models adversarially trained using alternative datasets show poor robustness compared to those trained using the original dataset (the diagonal cells)."

## [NEGATIVE] Using General-Domain Public Dataset (CIFAR-10) for AT
Using a publicly available general-domain dataset like CIFAR-10 for adversarial training of models pretrained on domain-specific data.

**Delta**: Poor robustness across most biomedical datasets; e.g., 0.00% AA on Tissue and Blood datasets
**Condition**: Privacy-sensitive biomedical datasets; when original training data is unavailable

**Evidence**: "Moreover, using a publicly available general domain dataset (CIFAR-10) also performs poorly, indicating that adversarial robustness is difficult to obtain from other datasets without access to the data in the same domain."

## [NEGATIVE] DiffPure on Privacy-Sensitive Datasets
Applying DiffPure (diffusion model-based adversarial purification) as a test-time defense on domain-specific medical datasets.

**Delta**: 0.00% AA on Tissue (RN-18), 0.00% AA on Blood (RN-18 and RN-50), 0.21% AA on Path (RN-18)
**Condition**: Privacy-sensitive biomedical datasets with large distributional gap to general domain data

**Evidence**: "DiffPure, which is known to show superior performance to AT methods, fails to show practical performance in most cases."

## [NEGATIVE] DAD Test-Time Defense
Data-free adversarial defense at test time using test set data for calibration.

**Delta**: 12.57% AA on OrganC RN-18 vs 42.56% for DataFreeShield; poor performance on most medical datasets
**Condition**: Medical datasets evaluated under AutoAttack; also noted to use test set data which could be regarded as a data leak

**Evidence**: "Similarly, DAD performs poorly against AutoAttack"

## [NEGATIVE] TTE (Test-Time Transformation Ensembling)
Enhancing defense through augmentation-based test-time transformation ensembling on non-robustly pretrained models.

**Delta**: Close-to-zero robustness on ResNet-50 in most medical settings; e.g., 0.00% AA on Tissue RN-50
**Condition**: Applied to non-robustly pretrained models on medical datasets; noted to mainly enhance already adversarially trained models

**Evidence**: "TTE shows close-to-zero robustness in ResNet-50 in most settings."

## [POSITIVE] Larger Model Capacity
Using models with larger capacity (ResNet-20 → ResNet-56 → WRN-28-10) for adversarial training.

**Delta**: Up to 21.08%p difference in robust accuracy under AutoAttack across model sizes
**Condition**: DataFreeShield on SVHN, CIFAR-10, CIFAR-100; baselines often unable to exploit model capacity

**Evidence**: "Aligned with previous findings, models with larger capacity (ResNet-20 → ResNet-56 → WRN-28-10) tend to have significantly better robust accuracy of up to 21.08%p difference under AutoAttack."

## [NEGATIVE] Fixed Coefficient Synthesis Loss
Conventional approach of using fixed hyperparameter weights for the synthesis loss components (class loss, feature loss, prior loss) when generating synthetic samples.

**Delta**: Lower diversity metrics and lower robustness than DSS; e.g., 36.34% AA vs 41.40% AA on CIFAR-10 WRN-28-10
**Condition**: Data-free synthetic sample generation; compared against DSS dynamic coefficient sampling

**Evidence**: "Figure 3b demonstrates the results from conventional approaches (fixed coefficients following Yin et al. 2020). Although the data generally follows class information, they are highly clustered with small variance."

## [NEUTRAL] CutMix Augmentation on Synthetic Data
Applying CutMix image augmentation on top of direct sample optimization for synthetic data diversification.

**Delta**: Slightly better recall than DSS but lower coverage (0.084 vs 0.163) and lower AA (34.79% vs 41.40%)
**Condition**: CIFAR-10 WRN-28-10 data-free adversarial training; diversity measured by recall, coverage, NDB, JSD

**Evidence**: "Although CutMix shows slightly better recall than DSS, the difference is negligible and the coverage metric is generally perceived as a more exact measure of distributional diversity."

## [POSITIVE] Soft-Label KL Divergence for Adversarial Training
Using teacher model soft outputs via KL-divergence as training signal instead of hard artificial labels during adversarial training with synthetic data.

**Delta**: Outperforms hard-label based methods (STD, TRADES, MART) on both SVHN and CIFAR-10
**Condition**: Data-free adversarial training where artificial labels are not ground truths; compared against standard AT losses

**Evidence**: "LDFShield achieves the best results under both PGD-10 and AutoAttack in both datasets."

## [POSITIVE] Smoothness Regularization Term in LDFShield
An additional term in the training objective that penalizes rapid changes in the model's output to reduce sensitivity to small input variations.

**Delta**: Part of LDFShield which achieves best overall results; contributes to flatter loss surface
**Condition**: Data-free adversarial training with synthetic data; addresses distribution gap between synthetic and real data

**Evidence**: "We add a smoothness term (c) which penalizes rapid changes in the model's output. This regularizes the model's sensitivity to small variations in the input, helping to train the target model to be stable under small perturbations."
