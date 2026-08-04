# Two Heads are Actually Better than One: Towards Better Adversarial Robustness via Transduction and Rejection

**Source**: https://proceedings.mlr.press/v235/palumbo24a.html

## [POSITIVE] Transduction + Rejection (TLDR)
Combining transductive learning (leveraging unlabeled test inputs to revise the model) with rejection (allowing the model to abstain on certain inputs) to defend against adversarial perturbations

**Delta**: 81.6% on CIFAR-10 and 57.9% on CIFAR-100 under l∞ with budget 8/255, vs. 71.1% and 42.7% for best existing baselines
**Condition**: CIFAR-10 and CIFAR-100 under l∞ perturbations with budget 8/255

**Evidence**: "on CIFAR-10, we obtain 81.6% transductive robust accuracy with rejection, a significant improvement on the current state-of-the-art result of 71.1% (Peng et al., 2023; Croce et al., 2020); on CIFAR-100, we obtain 57.9% transductive robust accuracy with rejection, significantly exceeding the strongest existing baseline of 42.7%"

## [POSITIVE] Tramèr Classifier-to-Detector Reduction (applied constructively)
Novel application of Tramèr's (2022) classifier-to-detector technique, previously used only to demonstrate vulnerability of defenses, now used to construct effective selective classifiers by rejecting inputs too close to the decision boundary

**Delta**: Rejection-only defense matches theoretical bound: AT with rejection at ϵ/2 budget achieves same robust accuracy as induction-only at ϵ/2 (e.g., 0.601 vs 0.602 on WideResNet-28-10 CIFAR-10)
**Condition**: Rejection-only defense on CIFAR-10 and CIFAR-100

**Evidence**: "our empirical transformation results in a robust accuracy is very close to the results obtained by Tramèr's idealized computationally inefficient approach. In this way, our approach enables practical realization of Tramèr's upper bound on gains from rejection"

## [POSITIVE] Adversarial Training on Both Training and Test Sets (Transductive Adversarial Training)
Performing adversarial training jointly on labeled training data and unlabeled test inputs using a robust cross-entropy objective, with private randomness as in TADV

**Delta**: TLDR with ResNet-20 achieves 0.739 robust accuracy on CIFAR-10 vs. 0.541 for TADV (best transduction-only baseline)
**Condition**: Transductive setting on CIFAR-10 and MNIST

**Evidence**: "To get h, we perform adversarial training on both the training set and the test set, using a robust cross-entropy objective. As in TADV (Chen et al., 2022) we train with private randomness."

## [POSITIVE] Empirical Classifier-to-Selective-Classifier Transformation via PGD
Using PGD to approximate the computationally inefficient exact transformation FU^(1/3), rejecting inputs for which a perturbation within the rejection radius changes the model's prediction

**Delta**: Matches theoretical bound closely (e.g., 0.564 vs 0.564 on ResNet-20 CIFAR-10 for rejection-only defense)
**Condition**: Rejection-only and TLDR defense on CIFAR-10 and CIFAR-100

**Evidence**: "our experiments show that the robustness of models utilizing our rejection-only defense very closely matches the theoretical bound (i.e. the robustness achievable to adversarial budget ϵ/2)"

## [POSITIVE] Rejection Radius Hyperparameter (ϵ_defense)
A tunable rejection radius controlling how close to the decision boundary an input must be to trigger rejection; set to ϵ/4 in main experiments

**Delta**: Rejection rates rise steadily with rejection radius but few clean samples are rejected and robust accuracy remains stable
**Condition**: TLDR defense; rejection radius set to ϵ/4 in main experiments

**Evidence**: "Rejection rates rise steadily with the rejection radius, but few clean samples are rejected and the robust accuracy remains stable."

## [POSITIVE] GMSA Attack with Rejection-Aware Loss (LREJ)
Adaptive attack combining GMSA (transduction-aware multi-stage attack) with a novel rejection-aware loss LREJ that targets both misclassification and rejection errors in selective classifiers

**Delta**: GMSA(LREJ) achieves 0.739 robust accuracy (strongest attack) vs. 0.853 for GMSA(LCE) and 0.756 for AutoAttack on CIFAR-10 against TLDR
**Condition**: Attacking TLDR on CIFAR-10; LREJ is the strongest attack component

**Evidence**: "GMSA with LCE is much weaker than GMSA with LREJ. This shows another key component in our adaptive attack, the loss LREJ, is also critical to get a strong attack against our defense."

## [NEGATIVE] PGD and AutoAttack against Transductive Defenses
Standard inductive attacks (PGD on LCE, AutoAttack) applied directly to transductive defenses without transduction-awareness

**Delta**: PGD(LCE): 0.794, AutoAttack: 0.756 on CIFAR-10 vs. GMSA(LREJ): 0.739 (strongest attack); inductive attacks are weaker
**Condition**: Attacking transductive defenses (TLDR) on CIFAR-10 and MNIST

**Evidence**: "attacks (PGD on LCE or LREJ and AutoAttack) from the traditional setting perform poorly against our defense... while PGD and AutoAttack are strong against an inductive model, they performs poorly facing transduction."

## [POSITIVE] Transduction Only (without Rejection)
Using transductive learning alone (e.g., RMC, DANN, TADV) without a rejection option

**Delta**: TADV achieves 0.943 on MNIST and 0.541 on CIFAR-10; outperforms induction (0.897/0.448) but below TLDR (0.972/0.739)
**Condition**: MNIST and CIFAR-10 under l∞ perturbations

**Evidence**: "either transduction or rejection can improve the performance, while combining both techniques leads to the best results. In particular, our defense outperforms existing transductive defenses such as RMC and DANN."

## [POSITIVE] Rejection Only (without Transduction)
Adversarial training with a rejection option but no transductive component

**Delta**: AT with rejection: 0.968 on MNIST and 0.634 on CIFAR-10 vs. AT without rejection: 0.897/0.448
**Condition**: MNIST and CIFAR-10 under l∞ perturbations

**Evidence**: "either transduction or rejection can improve the performance, while combining both techniques leads to the best results."

## [NEGATIVE] Rejectron (Goldwasser et al., 2020) — Transduction+Rejection Baseline
Prior transduction+rejection defense based on arbitrary perturbation theory; depends heavily on a confidence hyperparameter for rejection

**Delta**: 0.721 on MNIST and 0.145 on CIFAR-10 vs. TLDR's 0.972 and 0.739
**Condition**: MNIST and CIFAR-10 under l∞ perturbations, attacked with GMSA(LDISC)

**Evidence**: "The best-performing value on CIFAR-10 effectively eliminated the possibility of rejection (hence the rejection rate of 0); other choices resulted in near-0 robust accuracy."

## [POSITIVE] WideResNet-28-10 Architecture for TLDR
Using a larger WideResNet-28-10 architecture instead of ResNet-20 for TLDR

**Delta**: +7.7% robust accuracy on CIFAR-10 (0.816 vs 0.739) and +15.2% on CIFAR-100 (0.579 vs not reported for ResNet-20)
**Condition**: CIFAR-10 and CIFAR-100 under l∞ with budget 8/255

**Evidence**: "with a WideResNet28-10 architecture, we obtain an improvement in robust accuracy of over 10% [on CIFAR-10]; on CIFAR-100, we obtain an improvement in robust accuracy of over 15%."

## [NEUTRAL] Warm Start Period with λ=0 before Transductive Loss
Training initially with λ=0 (no transductive loss term) before introducing the transductive regularization weight λ=0.176

**Delta**: Not separately quantified
**Condition**: TLDR training on CIFAR-10 and MNIST

**Evidence**: "In training TLDR, we set λ = 0.176 after a warm start period in which λ = 0."

## [POSITIVE] LREJ Loss with LDB Surrogate (rank2 - max class probability)
Decision-boundary surrogate loss LDB,h(z') = rank2_h^s(z') - max_h^s(z') used within LREJ to measure closeness to decision boundary; maximized when top-two class probabilities are equal

**Delta**: LREJ outperforms LREJ with LDB replaced by LCE and outperforms AutoAttack (0.458 vs 0.470 vs 0.592 on CIFAR-10)
**Condition**: Attacking adversarially trained model with rejection on CIFAR-10

**Evidence**: "LREJ significantly outperforms both PGD targeting alternative losses and AutoAttack."

## [POSITIVE] Reduced Adversarial Budget Assumption (OPTU^(2/3)=0 vs OPTU^2=0)
Theoretical improvement: the proposed transduction+rejection approach requires only OPTU^(2/3)=0 (classifier robust to 2ϵ/3 budget) rather than OPTU^2=0 (robust to 2ϵ budget) as required by transduction alone

**Delta**: Tolerates 3x the adversarial magnitude compared to transduction alone for same data margin
**Condition**: Theoretical analysis for lp norm perturbations in realizable case

**Evidence**: "for a data distribution with a margin 2ϵ, transduction without rejection can only handle adversarial perturbations with budget ϵ, while combining transduction and rejection can handle adversarial perturbations with budget 3ϵ, tolerating three times the adversarial magnitude."

## [POSITIVE] Linear vs Exponential Sample Complexity (Transduction+Rejection vs Rejection Only)
Combining transduction with rejection yields linear dependence on VC dimension in sample complexity, whereas rejection alone has exponential dependence

**Delta**: Linear O(VC(H)) vs exponential dependence on VC dimension
**Condition**: Theoretical sample complexity analysis

**Evidence**: "compared to rejection only (see Table 1), this bound has a linear sample complexity rather than exponential. Therefore, combining transduction and rejection has the benefits of both techniques."
