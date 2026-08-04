# IBD-PSC: Input-level Backdoor Detection via Parameter-oriented Scaling Consistency

**Source**: https://proceedings.mlr.press/v235/hou24a.html

## [POSITIVE] Parameter-oriented Scaling Consistency (PSC)
Scaling up learnable parameters (γ and β) of batch normalization layers in a backdoored DNN to expose the consistency of prediction confidences for poisoned samples versus benign ones

**Delta**: AUROC avg 0.992, F1 avg 0.961 on CIFAR-10 across 7 attacks
**Condition**: Applied to backdoored DNNs with BN layers; white-box setting

**Evidence**: "the average prediction confidence of the poisoned samples remains nearly unchanged, whereas that of the benign samples also decreases during the parameter-amplified process under all three attacked models"

## [POSITIVE] BN Parameter Amplification (vs. Pixel Amplification)
Amplifying model BN parameters instead of pixel values to avoid the bounded [0,255] pixel constraint that limits SCALE-UP

**Delta**: IBD-PSC avg AUROC 0.992 vs SCALE-UP avg AUROC 0.731 on CIFAR-10
**Condition**: Compared to SCALE-UP on CIFAR-10, GTSRB, SubImageNet-200

**Evidence**: "in contrast to SCALE-UP, our IBD-PSC method induces more significant shifts in benign samples. This disparity in shift magnitude may stem from the constrained pixel value range of [0, 255], potentially mitigating the impact of amplification. However, the values of model parameters do not have such bounded constraints."

## [POSITIVE] Adaptive BN Layer Selection
Dynamically selecting the number of BN layers to amplify by incrementally increasing k and monitoring error rate η on benign samples until it exceeds threshold ξ=60%

**Delta**: Sustained robustness across all adaptive attack cases in Table 5
**Condition**: Applied during model amplification stage; especially effective against adaptive attacks

**Evidence**: "The effectiveness primarily originates from our adaptive layer selection strategy, which dynamically identifies BN layers for amplification, regardless of whether it is a vanilla or an adaptive backdoored model. The layers selected during the inference stage typically differ from those used in the training phase, enabling the IBD-PSC to effectively detect poisoned samples."

## [POSITIVE] Amplifying from Last BN Layer Forward
Starting amplification from the last BN layer and progressively moving to earlier layers, motivated by the finding that trigger patterns manifest as complex features in deeper layers

**Delta**: outperforms baseline defenses across all 13 attacks
**Condition**: Applied to ResNet-18 with 20 BN layers on CIFAR-10, GTSRB, SubImageNet-200

**Evidence**: "we start from the last layer of the deployed model and scale up different numbers of BN layers to obtain the scaled models. It is motivated by the previous findings that trigger patterns often manifest as complicated features learned by the deeper layers of models"

## [POSITIVE] Multiple BN Layer Amplification with Small Factor
Amplifying multiple BN layers with a small scaling factor (e.g., 1.5) rather than a single layer with a large factor, to stably increase feature norms

**Delta**: more stable across different settings compared to single-layer amplification
**Condition**: Applied across different attack types and BN layers

**Evidence**: "amplifying only a single BN layer may require an unreasonably large amplification factor and is unstable among different attacks or even BN layers... amplifying multiple BN layers with a small factor (e.g., 1.5) can also significantly increase the feature norm in the last pre-FC layer and is more stable across different settings"

## [POSITIVE] Scaling Factor ω=1.5
Using a fixed scaling factor of 1.5 to amplify BN parameters γ and β

**Delta**: AUROC and F1 scores converge to nearly 1.0 and stabilize at approximately one for ω values of 1.5 or higher
**Condition**: Tested on BadNets, WaNet, and BATT on CIFAR-10

**Evidence**: "the AUROC and F1 scores converge to nearly one and stabilize at approximately one for ω values of 1.5 or higher, i.e., the scaling factor has a relatively minor influence when it is sufficiently large"

## [POSITIVE] Confidence-based PSC Value (vs. Label Consistency)
Using average prediction confidence over scaled models rather than label consistency for detection, leveraging white-box access to confidence scores

**Delta**: significantly reduces false positives in both target and benign classes vs. Ours-L and SCALE-UP (e.g., BadNets target FPR: 0.20% vs 72.74% for SCALE-UP)
**Condition**: White-box setting on CIFAR-10 across multiple attacks

**Evidence**: "our method significantly reduces false positives in both the target and benign classes, outperforming both the Ours-L and SCALE-UP"

## [POSITIVE] Using n=5 Parameter-amplified Models
Using a series of n=5 parameter-amplified models (rather than one) to balance performance on benign and poisoned samples

**Delta**: outperforms baseline defenses consistently
**Condition**: Applied as a fixed hyper-parameter across all experiments

**Evidence**: "We exploit n instead of one parameter-amplified model (with many amplified BN layers) to balance the performance on benign and poisoned samples."

## [POSITIVE] Detection Threshold T=0.9
Using a fixed PSC threshold of 0.9 to classify samples as poisoned or benign

**Delta**: confidences of benign samples fall below threshold while poisoned samples mostly remain above
**Condition**: Applied consistently across various attacks and datasets

**Evidence**: "IBD-PSC determines whether it is a poisoned sample by whether the average of obtained prediction confidences (defined as PSC value) is greater than a given threshold T... The threshold is 0.9."

## [NEGATIVE] Pixel-level Amplification (SCALE-UP baseline)
Amplifying all pixel values of input samples with varying intensities to detect poisoned samples based on prediction consistency

**Delta**: avg AUROC 0.731 on CIFAR-10 with multiple failed cases (<0.7) including Blend (0.644), WaNet (0.672)
**Condition**: Applied to attacks with subtle multi-pixel alterations (Blend, WaNet) or physical attacks

**Evidence**: "SCALE-UP encounters some intrinsic limitations due to the restriction of pixel values (i.e., bounded in [0, 255]). For example, benign samples containing black and white pixels maintain their initial predictions during the amplification process... amplification often turns higher pixel values to the maximum (i.e., 255), masking the triggers and thus leading to changes in their predictions."

## [NEGATIVE] Adaptive Attack with Loss Term L_ada
Adversarial training with an additional loss term ensuring benign samples are correctly predicted under parameter amplification, combined with backdoor loss as L = αL_bd + (1-α)L_ada

**Delta**: IBD-PSC still achieves AUROC >0.819 and F1 >0.862 even at α=0.99 for BATT
**Condition**: Worst-case adaptive attack scenario with full knowledge of defense on CIFAR-10

**Evidence**: "Table 5 demonstrates the sustained robustness of our IBD-PSC across all cases... The layers selected during the inference stage typically differ from those used in the training phase, enabling the IBD-PSC to effectively detect poisoned samples."

## [POSITIVE] Low Poisoning Rate Resistance
Evaluating IBD-PSC under low poisoning rates (2%-10%) where weak trigger-label associations may reduce detectability

**Delta**: AUROC and F1 scores consistently above 0.98 and 0.95 respectively across poisoning rates 2%-10%
**Condition**: BadNets, WaNet, BATT on CIFAR-10 with poisoning rates 2%-10%

**Evidence**: "The results in Figure 7 consistently demonstrate the effectiveness of IBD-PSC, with AUROC and F1 scores consistently above 0.98 and 0.95, respectively."

## [POSITIVE] Extension to Training Set Purification
Applying IBD-PSC to detect poisoned samples in a compromised training set by first training a model normally then running detection

**Delta**: 100% TPR, nearly 100% AUROC, FPR close to 0%, ASR <0.5% after retraining
**Condition**: CIFAR-10 against three representative attacks; compared to CD and MSPC

**Evidence**: "The results show a 100% TPR and nearly 100% AUROC scores, with FPR scores close to 0%... The ASR scores of these retrained models are less than 0.5%, rendering the attacks ineffective."

## [POSITIVE] Inference Efficiency
IBD-PSC operates as a plug-and-play module with minimal inference time overhead compared to baseline defenses

**Delta**: IBD-PSC inference time 0.021s vs TeCo 0.065s (0.560s truncated) on CIFAR-10
**Condition**: CIFAR-10 dataset under identical and ideal conditions

**Evidence**: "the efficiency of our IBD-PSC is on par with or even better than all baseline defenses. The extra time is negligible compared to no defense"
