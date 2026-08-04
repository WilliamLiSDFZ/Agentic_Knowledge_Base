# Layer-Aware Analysis of Catastrophic Overfitting: Revealing the Pseudo-Robust Shortcut Dependency

**Source**: https://proceedings.mlr.press/v235/lin24v.html

## [POSITIVE] Layer-Aware Adversarial Weight Perturbation (LAP)
Applies adaptive weight perturbations across different DNN layers with gradually decreasing magnitude from former to latter layers, simultaneously generating adversarial perturbations for both inputs and weights to hinder pseudo-robust shortcut formation

**Delta**: R-LAP achieves 26.04% Auto Attack at 12/255 vs 0.00% for R-FGSM; N-LAP achieves 44.97% vs 44.21% for N-FGSM at 8/255 on CIFAR-10
**Condition**: Single-step adversarial training on CIFAR-10, CIFAR-100, Tiny-ImageNet across multiple noise magnitudes (8/255 to 32/255)

**Evidence**: "LAP demonstrates superior performance across all evaluation cases. More specifically, in the cases where CO does not occur in baselines, our method demonstrates a consistent ability to improve robustness. More importantly, in the cases where baselines are affected by CO, LAP not only effectively prevents its occurrence but also substantially boosts overall performance."

## [POSITIVE] Accumulated Weight Perturbation
LAP accumulates weight perturbations across training steps to maintain a larger magnitude of alteration and effectively break persistent shortcuts

**Delta**: Modified AWP (with accumulated perturbation) achieves 12.53% Auto Attack vs 0.00% for Original AWP at 16/255
**Condition**: R-LAP on CIFAR-10 under 16/255 noise magnitude with PreActResNet-18

**Evidence**: "our method accumulates weight perturbations to effectively break persistent shortcuts by maintaining a larger magnitude of alteration... It is evident that the original AWP is ineffective at mitigating CO due to its inability to disrupt persistent shortcuts."

## [POSITIVE] Weight Perturbation Priority over Input Perturbation
LAP prioritizes generating weight perturbations before input perturbations to obstruct the model from establishing stable shortcuts between inputs and weights

**Delta**: outperforms baseline
**Condition**: Single-step adversarial training to prevent catastrophic overfitting

**Evidence**: "we prioritize generating weight perturbations over input perturbations, aiming to obstruct the model from establishing stable shortcuts between inputs and weights."

## [POSITIVE] Gradually Decreasing Layer-wise Perturbation Strength
Applies stronger weight perturbations to former layers and weaker perturbations to latter layers, controlled by parameter γ, to avoid unnecessary redundant perturbations in latter layers

**Delta**: uniform perturbation across all layers results in substantial reduction in natural accuracy
**Condition**: R-LAP on CIFAR-10 under 16/255 noise magnitude, ablation study on γ hyperparameter

**Evidence**: "our approach adopts a gradually decreasing weight perturbation strategy from the former to the latter layer to avoid unnecessary redundant perturbations... When weight perturbation is applied solely to the 1st layer, it fails to effectively hinder the formation of shortcuts. On the other hand, employing uniform weight perturbation across all layers results in a substantial reduction in the natural accuracy."

## [POSITIVE] Concurrent Input and Weight Perturbation Generation
Efficient LAP implementation that simultaneously generates adversarial perturbations for both inputs and weights in a single backward pass, avoiding additional computational overhead

**Delta**: only 7% additional training cost over FGSM (11.8s vs 11.0s per epoch)
**Condition**: Training on single NVIDIA RTX 4090 GPU, averaged over 30 training epochs

**Evidence**: "the training cost of the LAP method is comparable to that of the FGSM method, which imposes only a 7% additional training cost. In contrast, the Grad Align and PGD-10 methods are significantly more time-consuming, being 3 and 5 times slower than our method, respectively."

## [NEGATIVE] Original AWP in Single-Step AT
Applying standard Adversarial Weight Perturbation (AWP) without accumulation to single-step adversarial training

**Delta**: 0.00% Auto Attack accuracy at 16/255 (catastrophic overfitting occurs)
**Condition**: Single-step adversarial training on CIFAR-10 under 16/255 noise magnitude

**Evidence**: "It is evident that the original AWP is ineffective at mitigating CO due to its inability to disrupt persistent shortcuts."

## [NEGATIVE] Modified AWP (with accumulation, uniform layers)
AWP with accumulated weight perturbation but applied uniformly across all layers without layer-aware adaptation

**Delta**: 30.00% natural accuracy and 12.53% Auto Attack vs LAP's 64.83% natural and 15.69% Auto Attack
**Condition**: R-LAP variant on CIFAR-10 under 16/255 noise magnitude with PreActResNet-18

**Evidence**: "While the modified AWP can mitigate CO, it demonstrates unsatisfactory natural and robust accuracy. This subpar outcome can be attributed to the introduction of redundant adversarial perturbations in the latter layers, which negatively affect the representation learning."

## [NEUTRAL] LAP-A (Additional Backward Propagation)
LAP variant that requires an additional backward propagation pass to generate weight perturbations separately from input perturbations

**Delta**: 15.72% Auto Attack vs 15.69% for standard LAP (marginal improvement but at significant computational cost)
**Condition**: R-LAP variant on CIFAR-10 under 16/255 noise magnitude with PreActResNet-18

**Evidence**: "while LAP-A shows a slight improvement in robustness, its requests additional backward propagation that significantly limits its applicability."

## [NEGATIVE] LAP-R (Random Weight Perturbation)
LAP variant using random weight perturbations instead of gradient-guided adversarial weight perturbations

**Delta**: 11.22% Auto Attack vs 15.69% for standard LAP
**Condition**: R-LAP variant on CIFAR-10 under 16/255 noise magnitude with PreActResNet-18

**Evidence**: "LAP-R and LAP-L∞ fail to achieve a comparable performance to the reported LAP implementation."

## [NEGATIVE] LAP-L∞ (L∞-norm Weight Perturbation)
LAP variant using L∞-norm for weight perturbation instead of L2-norm

**Delta**: 13.67% Auto Attack vs 15.69% for standard LAP
**Condition**: R-LAP variant on CIFAR-10 under 16/255 noise magnitude with PreActResNet-18

**Evidence**: "LAP-R and LAP-L∞ fail to achieve a comparable performance to the reported LAP implementation."

## [POSITIVE] Random Noise Initialization (R-FGSM)
FGSM with random initialization in range (-ε, ε) before gradient step to improve perturbation quality

**Delta**: R-FGSM achieves 42.88% Auto Attack at 8/255 vs 0.00% for V-FGSM, but suffers CO at higher magnitudes
**Condition**: Single-step adversarial training on CIFAR-10 at 8/255 noise magnitude; suffers catastrophic overfitting at 12/255 and above

**Evidence**: "Random FGSM (R-FGSM) (Wong et al., 2019) and Noise FGSM (N-FGSM) (de Jorge Aranda et al., 2022) adopt stronger noise initialization (−ϵ, ϵ) and (−2ϵ, 2ϵ), respectively, to further enhance the quality of maximization."

## [POSITIVE] Larger Noise Initialization (N-FGSM)
FGSM with stronger noise initialization in range (-2ε, 2ε) to further enhance perturbation quality and delay catastrophic overfitting

**Delta**: N-FGSM achieves 44.21% Auto Attack at 8/255 and 30.25% at 12/255, avoiding CO at these magnitudes; suffers CO at 32/255
**Condition**: Single-step adversarial training on CIFAR-10; effective at lower noise magnitudes but fails at 32/255

**Evidence**: "N-FGSM achieves 44.21±0.47 Auto Attack at 8/255 and 30.25±0.06 at 12/255, while R-FGSM collapses to 0.00 at 12/255"

## [POSITIVE] Removal of Large Weights from Former Layers
Removing the top 10% largest weights from former layers (1st to 5th) of a CO-affected model to disrupt pseudo-robust shortcuts

**Delta**: 22% reduction in FGSM attack accuracy and reinstatement of PGD robustness to 2.65% from near-zero
**Condition**: Post-hoc intervention on CO-affected PreActResNet-18 model trained on CIFAR-10 with R-FGSM at 16/255

**Evidence**: "removing only 10% of the large weights can effectively interrupt the pseudo-robust shortcuts, resulting in a notable 22% reduction in FGSM attack accuracy and reinstatement of robustness against PGD attack to 2.65%"

## [NEGATIVE] Removal of Large Weights from Latter Layers
Removing large weights from latter layers (14th to 17th) of a CO-affected model as a comparison to former layer intervention

**Delta**: less effective than removing large weights from former layers
**Condition**: Post-hoc intervention on CO-affected model, compared to former layer weight removal

**Evidence**: "we also remove the large weights from the latter (14th to 17th) layers... Clearly, the same intervention in the latter layers is less effective, highlighting the pseudo-robust shortcuts that play a critical role in the CO phenomenon, primarily present in the former layer."

## [NEUTRAL] Removal of Small Weights from Former Layers
Removing small weights from former layers of a CO-affected model to test their relevance to pseudo-robust shortcuts

**Delta**: negligible impact on FGSM and PGD accuracy
**Condition**: Post-hoc intervention on CO-affected PreActResNet-18 model trained on CIFAR-10 with R-FGSM at 16/255

**Evidence**: "the removal of small weights in the former layers has a negligible impact on the model's performance against both FGSM and PGD attacks, suggesting a weak relevance between these weights and shortcuts."

## [POSITIVE] Cyclical Learning Rate Schedule
Using cyclical learning rate schedule spanning 30 epochs, reaching maximum learning rate of 0.2 at epoch 15

**Delta**: enables effective training in 30 epochs vs 200 epochs for piecewise schedule
**Condition**: Primary experimental setup for CIFAR-10 and CIFAR-100 with PreActResNet-18

**Evidence**: "We use the cyclical learning rate schedule (Smith, 2017) spanning 30 epochs, which reaches its maximum learning rate of 0.2 at the 15th epoch."

## [NEUTRAL] Increasing α (Input Perturbation Step Size)
Increasing the step size α for input adversarial perturbation generation

**Delta**: improves robust accuracy but decreases natural accuracy (trade-off)
**Condition**: Ablation study on R-LAP with CIFAR-10 under 16/255 noise magnitude

**Evidence**: "we can observe that an increase in α leads to improved robust accuracy, but in turn results in a decline in natural accuracy. In light of this trade-off, we follow the original setting and choose not to modify α."

## [NEGATIVE] Small β (Weight Perturbation Magnitude)
Setting weight perturbation step size β to a very small value

**Delta**: insufficient to prevent catastrophic overfitting
**Condition**: Ablation study on R-LAP with CIFAR-10 under 16/255 noise magnitude

**Evidence**: "when β is set to a small value, the weight perturbation is inadequate to effectively obstruct pseudo-robust shortcuts and mitigate CO."

## [NEGATIVE] Excessive β (Weight Perturbation Magnitude)
Setting weight perturbation step size β to an excessively large value

**Delta**: causes over-smoothing and decrease in natural accuracy
**Condition**: Ablation study on R-LAP with CIFAR-10 under 16/255 noise magnitude

**Evidence**: "excessively increasing β will cause an over-smoothing model, thereby leading to a decrease in natural accuracy."

## [POSITIVE] Grad Align Method
Gradient alignment method that smooths local non-linear surfaces to prevent catastrophic overfitting

**Delta**: achieves 19.07% Auto Attack at 16/255 vs 0.00% for V-FGSM, but 3x slower than LAP
**Condition**: Single-step adversarial training on CIFAR-10; prevents CO but at significant computational cost (36.1s vs 11.8s per epoch)

**Evidence**: "the Grad Align and PGD-10 methods are significantly more time-consuming, being 3 and 5 times slower than our method, respectively."

## [POSITIVE] L2-norm for Weight Perturbation
Using L2-norm constraint for weight perturbation in LAP instead of L∞-norm

**Delta**: 15.69% Auto Attack vs 13.67% for LAP-L∞ at 16/255
**Condition**: R-LAP on CIFAR-10 under 16/255 noise magnitude with PreActResNet-18

**Evidence**: "we employ the SGD optimizer with a momentum of 0.9, a weight decay of 5×10−4, the L∞-norm for input perturbation, and the L2-norm for weight perturbation... LAP-L∞ fail to achieve a comparable performance to the reported LAP implementation."
