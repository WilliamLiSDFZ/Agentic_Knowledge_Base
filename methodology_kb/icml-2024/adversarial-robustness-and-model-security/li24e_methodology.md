# Purifying Quantization-conditioned Backdoors via Layer-wise Activation Correction with Distribution Approximation

**Source**: https://proceedings.mlr.press/v235/li24e.html

## [POSITIVE] Layer-wise Activation Correction (LAC)
A defense method that realigns the activation of the quantized model with that of the full-precision model layer-by-layer, using a distance metric (Euclidean distance) to minimize activation drift in backdoor neurons

**Delta**: ASR reduced to under 2% in virtually all scenarios tested
**Condition**: Applied to quantized models infected with quantization-conditioned backdoors (QCBs); works with or without poisoned data

**Evidence**: "our proposed strategy successfully lowers the ASR to under 2% in virtually all scenarios tested"

## [POSITIVE] Poisoned Distribution Approximation (PDA)
An additional module that approximates the poisoned activation distribution by perturbing benign sample activations using PGD to match batch normalization statistics (running mean and variance) of the full-precision model

**Delta**: Reduces standard deviation of ASR from ±1.77 to ±0.22 on PQBackdoor 8-bit; ASR from 2.18 to 1.64
**Condition**: Applied when BN layers are present in the model architecture; omitted for architectures without BN layers

**Evidence**: "the LAC alone is sufficient to remove the backdoor threats, while PDA can further enhance the performance and boost our stability, as indicated by a small standard deviation"

## [POSITIVE] Including Poisoned Data in LAC
Using poisoned samples (or a mixture of benign and poisoned data) as input during the LAC optimization process instead of only benign data

**Delta**: Faster convergence and more stable defense performance compared to benign-only data
**Condition**: When original training dataset (including poisoned samples) is accessible

**Evidence**: "using poisoned data or the mixture of benign and poisoned data can have a more stable defense performance and faster convergence than using benign data only"

## [POSITIVE] Label-free LAC Objective
LAC does not require label annotations or cross-entropy loss, relying only on activation alignment between full-precision and quantized models

**Delta**: Prevents backdoor reinforcement that occurs when CE loss is applied to poisoned data
**Condition**: Particularly beneficial when only the original (possibly poisoned) training dataset is available

**Evidence**: "LAC is free of label notations as well as the CE loss, thus the presence of poisoned data will not hinder the defense effects"

## [POSITIVE] PDA as Plug-in for Existing Defenses
Using PDA as a preprocessing augmentation step for existing backdoor defenses (e.g., NAD, FT-SAM) by adjusting inputs to approximate poisoned distribution before applying the original defense

**Delta**: NAD+PDA reduces ASR on Blended from 87.82% to 71.37%; on Input-aware from 67.91% to 42.56%; on LF from 83.80% to 56.67%
**Condition**: Applied to conventional backdoor attacks (BadNets, Blended, Input-aware, LF, SIG, ISSBA, WaNet) on CIFAR-10 with PreAct-ResNet18

**Evidence**: "in most cases, PDA can enhance the performance of state-of-the-art defenses, with a lower ASR and higher DER, especially in cases where the vanilla defense has only a modest effect (e.g., Blended, Input-aware, and LF on NAD)"

## [NEGATIVE] Vanilla Fine-tuning (FT) against QCBs
Standard fine-tuning of the quantized backdoored model on benign data with cross-entropy loss

**Delta**: BA: 85.29%, ASR: 98.97%, DER: 50.07% on PQBackdoor 8-bit (near-zero defense effectiveness)
**Condition**: Applied against PQBackdoor; partially effective against CompArtifact and Qu-Anti-zation

**Evidence**: "models backdoored by QCBs already fit benign samples well. As a result, most tuning-based defenses can only make minor changes to backdoor-related neurons, therefore failed to mitigate QCBs well"

## [NEGATIVE] NAD (Neural Attention Distillation) against QCBs
Existing backdoor purification defense using attention distillation applied to quantization-conditioned backdoors

**Delta**: BA drops to ~40% on PQBackdoor (approximately 40% reduction in BA), DER: 73.56%
**Condition**: Applied against PQBackdoor on CIFAR-10

**Evidence**: "NAD, though somewhat effective against PQBackdoor, significantly impairs benign accuracy (with approximately a 40% reduction in BA), rendering it an impractical solution as reflected by its low DER"

## [NEGATIVE] FP (Fine-Pruning) against QCBs
Existing defense combining pruning and fine-tuning applied to quantization-conditioned backdoors

**Delta**: ASR remains 99.86% on CompArtifact 8-bit; 99.08% on Qu-Anti-zation 8-bit
**Condition**: Applied against CompArtifact and Qu-Anti-zation on CIFAR-10

**Evidence**: "existing defenses have limited effects on mitigating QCBs... they are insufficient in defending against QCBs"

## [POSITIVE] Activation Drift Analysis of Backdoor Neurons
Empirical observation that backdoor neurons exhibit significant distributional drift in activation after quantization on both benign and poisoned samples, while benign neurons show minimal drift

**Delta**: Drift is more pronounced on poisoned samples than benign samples for backdoor neurons
**Condition**: Observed on ResNet-18 trained with PQBackdoor on CIFAR-10; motivates the LAC defense design

**Evidence**: "backdoor neurons generally show a significant distribution deviation from the original activation after quantization, while benign neurons only have a small difference on activation distribution before and after quantization"

## [NEGATIVE] Adaptive Attack with Activation Alignment Loss
An adaptive attack that adds a loss term to align full-precision and quantized model activations during backdoor training, attempting to bypass LAC defense

**Delta**: Attack still fails: BA 92.29%, ASR 01.65% after defense on CIFAR-10
**Condition**: Evaluated on CIFAR-10 with Qu-ANTI-zation protocol; adaptive attacker aware of LAC defense design

**Evidence**: "this adaptive strategy has a high ASR when our method is not applied. However, the attack still fails to hack our method, as reflected by a high BA and low ASR"

## [POSITIVE] l-infinity Norm Bound in PDA
Using l-infinity norm as the constraint in the PDA optimization to avoid overfitting to BN statistics and maintain sample-wise diversity

**Delta**: Maintains stable BA and ASR across gamma values from 1e-4 to 1e-2
**Condition**: Used in PDA optimization; evaluated across different gamma hyperparameter values on CIFAR-10 and Tiny-ImageNet

**Evidence**: "The subject term in Eq.(4) is a lp bound to avoid overfitting to the BN statistics as well as keeping sample-wise diversity... the backdoor-removal and accuracy maintaining effect of our method is not sensitive"

## [POSITIVE] Layer-by-layer Processing Order (PDA then LAC)
For each layer, first applying PDA to rectify inputs, then using LAC to align activations, processed sequentially layer-by-layer

**Delta**: Best DER achieved in majority of attack/dataset combinations
**Condition**: Applied during defense optimization with Adam optimizer, learning rate 1e-3, batch size 32

**Evidence**: "For each layer, we first use PDA to rectify the inputs then use LAC to align the activation. This process is conducted layer-by-layer"

## [POSITIVE] BN Statistics as Poisoned Distribution Proxy
Leveraging running mean and variance stored in batch normalization layers of the full-precision model to approximate the poisoned training data distribution

**Delta**: PDA effectively rectifies benign data to align with poisoned data statistics as shown in Figure 3
**Condition**: Applicable only to model architectures containing BN layers; BN statistics encode mixture of benign and poisoned distribution

**Evidence**: "These layers store running means and variances of the activations, and thus it implicitly encodes rich statistical information about the training data... we leverage the BN statistics to approximate the activation distribution of the poisoned training data"

## [POSITIVE] Cross-architecture Generalization of LAC+PDA
Applying the proposed defense across different model architectures including AlexNet, VGG19-BN, MobileNet-V2, ViT, and EfficientViT

**Delta**: AlexNet: ASR 1.98%; VGG19-BN: ASR 1.34%; MobileNet-V2: ASR 1.24%; ViT: ASR 0.60%; EfficientViT: ASR 0.62%
**Condition**: Evaluated on 4-bit Qu-ANTI-zation attack; PDA omitted for architectures without BN layers

**Evidence**: "our method has high transferability across model architectures, with consistently high BA and low ASR"
