# OODRobustBench: a Benchmark and Large-Scale Analysis of Adversarial Robustness under Distribution Shift

**Source**: https://proceedings.mlr.press/v235/li24bp.html

## [POSITIVE] Adversarial Training (general)
Training models with adversarial examples to improve robustness against attacks

**Delta**: varies; average OOD robustness still degrades 18%/31%/24% under distribution shifts for CIFAR10 ℓ∞, CIFAR10 ℓ2, ImageNet ℓ∞
**Condition**: General adversarial training evaluated under OOD distribution shifts

**Evidence**: "adversarial robustness suffers from a severe OOD generalization issue. Robustness degrades on average by 18%/31%/24% under distribution shifts for CIFAR10 ℓ∞, CIFAR10 ℓ2 and ImageNet ℓ∞ respectively."

## [POSITIVE] Training with Extra Data
Augmenting training with additional real or synthetic data beyond the base training set

**Delta**: boosts both robustness and adversarial effective robustness compared to training without extra data
**Condition**: OOD dataset and threat shifts; real data shows slight advantage over synthetic for threat shift AER

**Evidence**: "Training with extra data boosts both robustness and adversarial effective robustness compared to training schemes without extra data"

## [NEUTRAL] Real vs. Synthetic Extra Data
Using real unlabeled data (e.g., Carmon et al.) versus synthetic generated data (e.g., DDPM) as extra training data

**Delta**: no clear advantage except adversarial effective robustness under threat shift improved more by real data
**Condition**: Comparison of real vs. synthetic extra data for OOD robustness

**Evidence**: "There is no clear advantage to training with extra real data rather than synthetic data except for the adversarial effective robustness under threat shift which is improved more by real data."

## [POSITIVE] Advanced Data Augmentation
Using augmentation strategies beyond RandomCrop, such as AutoAugment or TrivialAugment

**Delta**: improves robustness under both types of shifts and adversarial effective robustness under threat shift; degrades AER under dataset shift for methods other than TrivialAugment
**Condition**: OOD dataset and threat shifts; TrivialAugment (TA) is the exception that does not degrade dataset-shift AER

**Evidence**: "Advanced data augmentation improves robustness under both types of shifts and adversarial effective robustness under threat shift over the baseline augmentation RandomCrop. Nevertheless, advanced data augmentation methods other than TA degrade adversarial effective robustness under dataset shift."

## [POSITIVE] TrivialAugment (TA)
A tuning-free data augmentation method that does not degrade adversarial effective robustness under dataset shift

**Delta**: does not degrade adversarial effective robustness under dataset shift unlike other advanced augmentations
**Condition**: OOD dataset shift; compared to other advanced augmentation methods

**Evidence**: "advanced data augmentation methods other than TA (Muller & Hutter, 2021) degrade adversarial effective robustness under dataset shift."

## [NEGATIVE] AutoAugment
Learned data augmentation strategy that can cause abnormal robustness drops under noise shifts

**Delta**: contributes to abnormal catastrophic drop in robustness under noise shifts
**Condition**: Noise distribution shifts (Gaussian, impulse, shot noise)

**Evidence**: "A similar yet milder drop is also observed on Debenedetti et al. (2023) and models trained with some advanced data augmentations like AutoAugment"

## [POSITIVE] Advanced Model Architecture
Using architectures beyond baseline ResNet, including WideResNets, ViT, RobustResNet, etc.

**Delta**: greatly boosts robustness and adversarial effective robustness under both types of shift
**Condition**: Both OOD dataset and threat shifts

**Evidence**: "Advanced model architecture greatly boosts robustness and adversarial effective robustness under both types of shift over the baseline ResNet"

## [POSITIVE] Vision Transformer (ViT)
Transformer-based image recognition architecture applied to adversarially trained models

**Delta**: achieves highest adversarial effective robustness among all tested architectures
**Condition**: OOD robustness evaluation across dataset and threat shifts

**Evidence**: "Among all tested architectures, ViT achieves the highest adversarial effective robustness."

## [NEGATIVE] Scaling Up Model Size
Increasing the number of parameters in the model (e.g., larger WideResNet variants)

**Delta**: dramatically impairs adversarial effective robustness under threat shift despite improving ID robustness
**Condition**: OOD threat shift; positive for dataset shift AER but negative for threat shift AER

**Evidence**: "Scaling model up improves robustness under both types of shift and adversarial effective robustness under dataset shift, but dramatically impairs adversarial effective robustness under threat shift. The latter is because increasing model size greatly improves ID robustness but not OOD robustness so that the real OOD robustness is much below the OOD robustness predicted by linear correlation."

## [POSITIVE] VR (Variance Regularization for Unforeseen Attacks)
Defense method by Dai et al. (2022) designed to be robust against unforeseen adversarial attacks

**Delta**: greatly boosts adversarial effective robustness under threat shifts; also boosts AER under dataset shift
**Condition**: OOD threat shift and dataset shift; note inferior ID robustness

**Evidence**: "VR, the state-of-the-art defense against unforeseen attacks, greatly boosts adversarial effective robustness under threat shifts in spite of inferior ID robustness. Surprisingly, VR also clearly boosts adversarial effective robustness under dataset shift even though not designed for dealing with these shifts."

## [POSITIVE] HE / Hypersphere Embedding (Pang et al., 2020)
Adversarial training method that boosts training with hypersphere embedding

**Delta**: AER of 16.22% under threat shift, much higher than PGD-trained models; ranking jumps from 70 to 3
**Condition**: OOD threat shift; also improves ID robustness leading to further OOD boost

**Evidence**: "Training methods HS (Pang et al., 2020), MMA (Ding et al., 2020) and AS (Bai et al., 2023) achieve an AER of 16.22%, 10.74% and 9.41%, respectively, under threat shift, which are much higher than the models trained with PGD."

## [POSITIVE] MMA Training (Ding et al., 2020)
Direct input space margin maximization through adversarial training

**Delta**: AER of 10.74% under threat shift, much higher than PGD-trained models
**Condition**: OOD threat shift

**Evidence**: "Training methods HS (Pang et al., 2020), MMA (Ding et al., 2020) and AS (Bai et al., 2023) achieve an AER of 16.22%, 10.74% and 9.41%, respectively, under threat shift, which are much higher than the models trained with PGD."

## [POSITIVE] AS / Adaptive Smoothing (Bai et al., 2023)
Method improving accuracy-robustness trade-off via adaptive smoothing

**Delta**: AER of 9.41% under threat shift, much higher than PGD-trained models; OOD ranking 1st in Table 1
**Condition**: OOD threat shift; also improves ID robustness

**Evidence**: "Training methods HS (Pang et al., 2020), MMA (Ding et al., 2020) and AS (Bai et al., 2023) achieve an AER of 16.22%, 10.74% and 9.41%, respectively, under threat shift, which are much higher than the models trained with PGD."

## [NEGATIVE] HAT (Rade & Moosavi-Dezfooli, 2022)
Adversarial training method reducing excessive margin for better accuracy-robustness trade-off

**Delta**: robustness drops by 43%/46%/38% under impulse/Gaussian/shot noise vs. average drop of 12%/9%/8%; ranking drops from 22 to 57
**Condition**: Noise distribution shifts (Gaussian, impulse, shot noise)

**Evidence**: "This issue is most severe on (Rade & Moosavi-Dezfooli, 2022) whose robustness falls by 43%/46%/38% under impulse/Gaussian/shot noise, whereas the average drop is 12%/9%/8%"

## [NEGATIVE] OOD Generalization Methods (PLAT, CARD-Deck)
Methods specifically designed for OOD generalization (e.g., PLAT, CARD-Deck) without adversarial training

**Delta**: offer little or no adversarial robustness regardless of ID or OOD setting; OOD_t robustness is 0.0%
**Condition**: OOD adversarial robustness evaluation; methods not combined with adversarial training

**Evidence**: "Despite the expected remarkable OOD clean generalization under OOD_d shifts, they offer little or no adversarial robustness regardless of ID or OOD setting. It suggests that OOD generalization methods alone do not help OOD adversarial robustness unless combined with adversarial training."

## [NEGATIVE] MSD+REx (Multi-attack + OOD Defense Combination)
Combining multi-attack defense MSD with REx OOD generalization method, treating different attacks as separate domains

**Delta**: impairs OOD adversarial robustness under both dataset and threat shifts; no evident improvement in AER vs. supervised ℓp AT
**Condition**: OOD dataset and threat shifts on CIFAR10 ℓ∞

**Evidence**: "this purpose-built solution impairs OOD adversarial robustness under both dataset and threat shifts and offers no evident improvement in AER when compared to supervised ℓp adversarial training."

## [NEUTRAL] Adversarial Contrastive Learning (ACL)
Self-supervised contrastive learning combined with adversarial training for unsupervised representation learning

**Delta**: effective robustness under dataset shift is 0.1%, suggesting only marginal benefit
**Condition**: OOD dataset shift on CIFAR10 ℓ∞

**Evidence**: "The effective robustness under dataset shift is 0.1%, suggesting only marginal benefit in improving OOD robustness."

## [NEUTRAL] Non-ℓp Attack Defense (ReColor AT, StAdv AT, PAT)
Adversarial training using non-ℓp attacks such as color-based (ReColor), spatial (StAdv), or LPIPS-bounded (PAT) attacks

**Delta**: none achieve high OOD_d ER and AER; not significantly better than supervised single-attack ℓp AT for dataset shifts
**Condition**: OOD dataset distribution shifts; does improve non-ℓp threat shift robustness for seen attacks

**Evidence**: "none of these defenses achieve high OOD_d ER and AER in Table 2, indicating that they are not significantly better than the supervised single-attack ℓp AT at handling OOD dataset distribution shifts."

## [NEUTRAL] Composite Attack Defense (GAT-f/fs)
Defense against composite adversarial attacks combining color and ℓp perturbations

**Delta**: does not achieve high OOD_d ER and AER; not significantly better than ℓp AT for dataset shifts
**Condition**: OOD dataset distribution shifts on CIFAR10 ℓ∞

**Evidence**: "none of these defenses achieve high OOD_d ER and AER in Table 2, indicating that they are not significantly better than the supervised single-attack ℓp AT at handling OOD dataset distribution shifts."

## [NEUTRAL] Multi-Attack Adversarial Training (MAAT)
Training with multiple attacks (ℓ2, ℓ∞, StAdv, ReColor) using average, max, or random selection strategies

**Delta**: does not achieve high OOD_d ER and AER; not significantly better than ℓp AT for dataset shifts
**Condition**: OOD dataset distribution shifts; improves seen non-ℓp threat robustness but those attacks are no longer unforeseen

**Evidence**: "none of these defenses achieve high OOD_d ER and AER in Table 2, indicating that they are not significantly better than the supervised single-attack ℓp AT at handling OOD dataset distribution shifts."

## [POSITIVE] Adversarial Training (AT) for Linear Correlation
Adversarial training improving the linear correlation between ID and OOD accuracy under corruption shifts

**Delta**: R² surges from nearly 0 (no linear correlation) for ST models to around 0.8 (evident linear correlation) for AT models under Gaussian and shot noise shifts
**Condition**: Corruption shifts on CIFAR10; improves faithfulness of ID performance for model selection and OOD prediction

**Evidence**: "AT models exhibit a stronger linear correlation between ID and OOD accuracy under most corruption shifts on CIFAR10. The improvement is dramatic for particular shifts. For example, R² surges from nearly 0 (no linear correlation) for ST models to around 0.8 (evident linear correlation) for AT models with Gaussian and shot noise data shifts."

## [POSITIVE] MM5 Attack for Evaluation
Using Minimum-Margin attack with 5 steps as a faster alternative to AutoAttack for adversarial evaluation

**Delta**: approximately 32× faster than AutoAttack while achieving similar results
**Condition**: Adversarial robustness evaluation across 80 runs per model in OODRobustBench

**Evidence**: "MM5 is approximately 32× faster than AutoAttack while achieving similar results, as verified in Appendix B.2"

## [NEGATIVE] High ID Robustness (Diminishing Returns Effect)
Achieving higher in-distribution robustness through existing methods leads to greater absolute degradation under distribution shift

**Delta**: top method degrades by 30% of robustness under distribution shift while bottom method degrades by only 18%
**Condition**: All distribution shifts; applies to models with higher ID robustness

**Evidence**: "The higher the ID robustness of the model, the more robustness degrades under distribution shift. For example, the top method in Table 1 degrades by 30% of robustness, while the bottom method degrades by only 18%. This suggests that while the great progress has been made on improving ID robustness, we only gain diminishing returns under the distribution shifts."

## [NEGATIVE] ℓp Robustness for Non-ℓp Threat Generalization
Using ℓp adversarial training to improve robustness against non-ℓp attacks like PPGD, LPA, StAdv

**Delta**: R² close to 0 for ℓ∞-LPA and ℓ∞-StAdv suggesting no correlation; increase in ID ℓp robustness leads to only slight or no improvement on LPA and StAdv
**Condition**: Threat shift to non-ℓp attacks (PPGD, LPA, StAdv)

**Evidence**: "ℓp robustness correlates poorly with non-ℓp robustness. R² of the regression between ID ℓp robustness and PPGD, LPA and StAdv robustness is low. Particularly, R² is close to 0 for ℓ∞-LPA and ℓ∞-StAdv on CIFAR10 ℓ∞ suggesting no correlation at all."

## [POSITIVE] ℓp Robustness for ReColor Generalization
Using ℓp adversarial training to improve robustness against the ReColor non-ℓp attack

**Delta**: ID ℓp robustness is well correlated with ReColor unforeseen robustness despite poor correlation with other non-ℓp attacks
**Condition**: Threat shift to ReColor non-ℓp attack

**Evidence**: "Interestingly, despite poor correlation with PPGD, LPA and StAdv, ID ℓp robustness is well correlated with ReColor unforeseen robustness."

## [POSITIVE] Unsupervised OOD Robustness Prediction
Predicting OOD adversarial robustness using only unlabeled OOD data by measuring prediction agreement between model pairs

**Delta**: R² is 0.99 for CIFAR-10.1 shift and 0.95 for Impulse noise shift
**Condition**: CIFAR-10 ℓ∞ models evaluated on CIFAR-10.1 and Impulse noise shifts

**Evidence**: "a linear trend is also observed in the agreement between the predictions of any pair of two robust models: R² is 0.99 for CIFAR-10.1 shift and 0.95 for Impulse noise shift. This suggests that the unsupervised method is also effective in predicting OOD adversarial robustness."
