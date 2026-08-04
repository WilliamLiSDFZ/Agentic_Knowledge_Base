# Data Poisoning Attacks against Conformal Prediction

**Source**: https://proceedings.mlr.press/v235/li24l.html

## [POSITIVE] Bi-level Poisoning Attack Framework
A bi-level optimization framework where the outer problem crafts poisoning samples to manipulate conformal prediction sets, and the inner problem specifies the model's learning objective on clean and poisoned data.

**Delta**: reduction ratio of 0.48 with HPS and 0.54 with RAPS using 2% poison budget
**Condition**: Overconfidence CP attacks on CIFAR-10 with HPS and RAPS conformal methods

**Evidence**: "Our proposed attacks achieve a reduction ratio of 0.48 with HPS and 0.54 with RAPS using 2% poison budget, while the baselines achieve reduction ratios below 0.32."

## [POSITIVE] Worst-Case Adversarial Loss (ℓ3 loss)
Maximizes the poisoning effect on the worst-case model by perturbing model parameters with a norm-constrained vector ζ, ensuring high poisoning effect is preserved across various model initializations.

**Delta**: +0.01 to +0.02 reduction ratio over ℓ2 loss at 0.5% and 1% poison budgets
**Condition**: Black-box overconfidence CP attacks on CIFAR-10 at low poison budgets

**Evidence**: "When comparing the two loss functions, we observe that under budgets of 0.5% and 1%, attacks employing the ℓ3 loss achieve higher reduction ratios of 0.01 and 0.02, respectively, than the ℓ2 loss."

## [POSITIVE] First-Order Closed-Form Update
Uses first-order Taylor series approximation and influence functions to compute closed-form model updates, avoiding full model retraining or access to entire training dataset.

**Delta**: reduction ratio 0.36–0.46 at 0.5%–2% poison budget; running time 12.75–19.26 min vs 233.48–494.72 min for MetaPoison
**Condition**: Overconfidence CP attacks against HPS on CIFAR-10

**Evidence**: "our proposed attacks, both in first-order and second-order optimizations, achieve a significantly higher set size reduction ratio and require much less running time compared to MetaPoison (Huang et al., 2020) optimization."

## [POSITIVE] Second-Order Closed-Form Update
Uses inverse Hessian matrix to compute second-order closed-form model updates when the loss is twice differentiable and strictly convex, providing tighter approximation bounds than first-order.

**Delta**: reduction ratio 0.38–0.48 at 0.5%–2% poison budget; running time 95.76–369.23 min vs 233.48–494.72 min for MetaPoison
**Condition**: Overconfidence CP attacks against HPS on CIFAR-10; second-order is slower than first-order but faster than MetaPoison

**Evidence**: "our proposed attacks, both in first-order and second-order optimizations, achieve a significantly higher set size reduction ratio and require much less running time compared to MetaPoison (Huang et al., 2020) optimization."

## [POSITIVE] Approximate Relaxation of Discrete Conformal Sets
Surrogate losses are designed to approximate the non-convex, non-differentiable quantile and discrete conformal set membership, making the bi-level optimization tractable.

**Delta**: outperforms baseline
**Condition**: Required for all CP attack settings due to discrete nature of conformal prediction sets

**Evidence**: "Since the second and third terms are non-convex and non-differential, we design the surrogate losses to approximate them."

## [POSITIVE] Label Correctness and Coverage Preservation Constraints
Additional loss terms ensure correct label predictions and inclusion of true labels in post-attack conformal prediction sets, maintaining attack stealthiness without impacting coverage results.

**Delta**: high prediction consistency and similar empirical coverage rates compared to benign model
**Condition**: Overconfidence CP attacks on CIFAR-10 with HPS; stealthiness evaluation

**Evidence**: "Our proposed attacks achieve a high prediction consistency and similar empirical convergence rates compared to the benign model. This underscores the stealthiness of our attacks when targeting uncertainty in CP."

## [POSITIVE] Targeting Nonconformity Scores Instead of Labels
Attack framework specifically targets nonconformity scores rather than label predictions, making it distinct from traditional poisoning attacks and bypassing existing defenses.

**Delta**: reduction ratio of 0.34 under MaxUp with HPS, compared to 0.46 without defense; existing defenses remain ineffective
**Condition**: Under data poisoning defenses (MaxUp, Adversarial Poisoning, EPIC) on CIFAR-10 with 2% poison budget

**Evidence**: "our proposed attacks remain effective even under these existing poisoning defenses since we specifically target the nonconformity scores in our attack framework. For example, it still achieves a reduction ratio of 0.34 under MaxUp with HPS, compared to 0.46 without defense."

## [POSITIVE] Larger Perturbation Bound
Increasing the perturbation bound ε allows the adversary more space to adjust features of victim samples, enabling more effective poisoning.

**Delta**: higher set size reduction ratios with larger perturbation bounds (e.g., 16/255 to 32/255)
**Condition**: Overconfidence CP attacks on CIFAR-10 with ℓ3 loss and 2% poison budget

**Evidence**: "The results show that our proposed attacks generally achieve higher set size reduction ratios with larger perturbation bounds. Even with a small perturbation bound (e.g., 16/255), our proposed attacks exhibit remarkable performance."

## [NEGATIVE] Larger Benign Set Size
Attacking targets with larger prediction sets (higher uncertainty) poses greater challenge as more labels need to be manipulated.

**Delta**: descriptive reduction in attack effectiveness as benign set size increases
**Condition**: Overconfidence CP attacks on CIFAR-10 with 2% poison budget across varying benign set sizes

**Evidence**: "Typically, a larger prediction set implies more uncertainty and poses a greater challenge for attacks due to the need to manipulate more labels. Nonetheless, our attacks persist in showcasing their capability to reduce the set size."

## [NEGATIVE] Existing Poisoning Defenses (MaxUp, Adversarial Poisoning, EPIC)
Standard data poisoning defenses including data augmentation-based (MaxUp), adversarial training-based (Adversarial Poisoning), and gradient-space filtering (EPIC) applied against the proposed CP attacks.

**Delta**: reduction ratio decreases from 0.46 to 0.34 (MaxUp+HPS), 0.47 to 0.32 (MaxUp+APS), 0.54 to 0.49 (MaxUp+RAPS), 0.49 to 0.26 (MaxUp+RSCP)
**Condition**: Overconfidence CP attacks on CIFAR-10 with 2% poison budget; defenses reduce but do not eliminate attack effectiveness

**Evidence**: "our proposed attacks remain effective even under these existing poisoning defenses since we specifically target the nonconformity scores in our attack framework... our proposed attacks demonstrate a satisfying set size reduction ratio across existing defense mechanisms"

## [NEGATIVE] Random Noise Baselines (RandUn, RandGa)
Using random uniform or Gaussian noise as poisoning perturbations as baseline comparison methods.

**Delta**: baselines achieve reduction ratios below 0.32 vs proposed attack's 0.48–0.54 at 2% poison budget
**Condition**: Overconfidence CP attacks on CIFAR-10 with HPS and RAPS at 2% poison budget

**Evidence**: "our proposed attacks significantly outperform RandUn and RandGa baselines in terms of set size reduction ratio and set size expansion ratio across various poison budgets... the baselines achieve reduction ratios below 0.32."

## [NEUTRAL] Transfer Learning-Based Attack for Full CP
For full conformal prediction, uses transfer learning setting where adversary has knowledge of a pre-trained model and victim model is fine-tuned on it, to maintain data exchangeability assumption.

**Delta**: no quantitative results provided in main paper
**Condition**: Full conformal prediction setting where data exchangeability must be preserved

**Evidence**: "To study the effects of poisoning attacks on full conformal prediction while maintaining validity, we can employ transfer learning-based attack settings (Shen et al., 2021; Shafahi et al., 2018), where the adversary has knowledge of a pre-trained model and the victim model is fine-tuned on this pre-trained model."
