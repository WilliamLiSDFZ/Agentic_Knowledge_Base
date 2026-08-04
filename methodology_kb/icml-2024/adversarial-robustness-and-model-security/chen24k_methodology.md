# Robust Classification via a Single Diffusion Model

**Source**: https://proceedings.mlr.press/v235/chen24k.html

## [POSITIVE] Robust Diffusion Classifier (RDC)
A generative classifier constructed from a pre-trained diffusion model that computes class probabilities via Bayes' theorem using conditional likelihood estimated by the diffusion model

**Delta**: +4.77% over state-of-the-art adversarial training (AT-EDM) on CIFAR-10 ℓ∞ norm
**Condition**: CIFAR-10, ℓ∞ norm with ϵ∞ = 8/255, adaptive attacks via AutoAttack

**Evidence**: "RDC achieves 75.67% robust accuracy against various ℓ∞ norm-bounded adaptive attacks with ϵ∞ = 8/255 on CIFAR-10, surpassing the previous state-of-the-art adversarial training models by +4.77%."

## [POSITIVE] Likelihood Maximization (LM)
A pre-optimization step that minimizes the unconditional diffusion loss to move input data to regions of high likelihood before feeding into the diffusion classifier, constrained by an ℓ∞ budget η

**Delta**: Improves DC from 35.94% to 75.67% robust accuracy under ℓ∞ norm
**Condition**: CIFAR-10, ℓ∞ and ℓ2 norm threat models, used as pre-processing before diffusion classifier

**Evidence**: "RDC can further improve the performance over DC, which achieves 75.67% and 82.03% robust accuracy under the two settings."

## [POSITIVE] Multi-head Diffusion Backbone
A modified UNet backbone where the last convolutional layer outputs noise predictions for all K classes simultaneously, reducing NFEs from K×T to T

**Delta**: Reduces time complexity from K×T NFEs to T NFEs
**Condition**: CIFAR-10 with K=10 classes, inference time complexity reduction

**Evidence**: "To obtain the predictions of all classes in a single forward pass, we propose to modify the last convolutional layer in the UNet backbone to predict noises for K classes (i.e., K × 3 dimensions) simultaneously. Thus, it only requires T NFEs for a single image."

## [POSITIVE] Deterministic Timestep Expectation (Variance Reduction)
Computing the expectation over timestep t directly rather than sampling t via Monte Carlo, to reduce variance in diffusion loss estimation

**Delta**: Reduces variance while maintaining performance; sampling one ε is sufficient
**Condition**: Diffusion classifier inference, timestep expectation estimation

**Evidence**: "To reduce the variance with affordable computational cost, we directly compute the expectation over t instead of sampling t... we show that sampling only one ε is sufficient to achieve good performance."

## [POSITIVE] Single Timestep Sampling for LM
During likelihood maximization, sampling only a single timestep uniformly per iteration instead of computing over all timesteps, reducing complexity from O(N×T) to O(N)

**Delta**: Reduces time complexity from O(N×T) to O(N) and greatly improves robustness
**Condition**: Likelihood maximization step, CIFAR-10

**Evidence**: "Surprisingly, this modification not only reduces the time complexity of likelihood maximization from O(N × T) to O(N), but also greatly improves the robustness. This is because this likelihood maximization induces more randomness, thus it is more effective to smooth the local extrema."

## [POSITIVE] Generative Classifier via Bayes' Theorem
Using a diffusion model as a generative classifier by computing p(y|x) ∝ p(x|y)p(y) rather than directly learning discriminative probabilities

**Delta**: DC improves robust accuracy over JEM by +27.74% under ℓ∞ norm and +50.58% under ℓ2 norm
**Condition**: CIFAR-10, compared against prior generative classifiers (JEM, SBGC, HybViT)

**Evidence**: "the robustness of DC outperforms all previous generative classifiers by a large margin. Specifically, DC improves the robust accuracy over JEM by +27.74% under the ℓ∞ norm and +50.58% under the ℓ2 norm."

## [POSITIVE] Threat-Model-Agnostic Design
RDC does not train on specific adversarial attacks, making it generalizable across unseen threat models including ℓ∞, ℓ2, and StAdv

**Delta**: >30% improvement over baselines on average robustness across unseen threats; 87.50–93.55% under StAdv vs. baselines below ~50%
**Condition**: Unseen threat models: ℓ∞, ℓ2, StAdv on CIFAR-10

**Evidence**: "the average robustness of our methods surpasses the baselines by more than 30%... LM, DC and RDC achieve 87.50%, 93.55% and 89.45% robustness under StAdv, surpassing previous methods by more than 53.90%."

## [NEUTRAL] BPDA Adaptive Attack Evaluation
Using Backward Pass Differentiable Approximation (BPDA) as the default adaptive attack for evaluating RDC, approximating gradient with identity mapping

**Delta**: BPDA yields ~0.39% higher robust accuracy than exact gradient (69.92% vs 69.53%)
**Condition**: RDC with N=1 LM steps, ℓ∞ norm, CIFAR-10

**Evidence**: "our RDC with N = 1 achieves 69.53% robust accuracy under the exact gradient attack, about 0.39% lower than BPDA. This result suggests that BPDA suffices for evaluating RDC."

## [NEUTRAL] Lagrange Adaptive Attack
An adaptive attack that adds a penalty term to minimize diffusion loss while inducing misclassification, tested with multiple penalty weights

**Delta**: No more effective than BPDA (77.54% robust accuracy vs 75.67% under BPDA with N=5)
**Condition**: RDC with N=5 LM steps, ℓ∞ norm, CIFAR-10

**Evidence**: "As shown in Table 2, this adaptive attack is no more effective than BPDA."

## [POSITIVE] Optimization Budget η for LM
Constraining the ℓ∞ norm of the perturbation during likelihood maximization to prevent moving inputs into regions of other classes

**Delta**: Robust accuracy peaks at η=8/255; too small or too large degrades performance
**Condition**: CIFAR-10, ℓ∞ norm, ablation over η values

**Evidence**: "the robust accuracy first increases and then decreases as η becomes larger. When η is small, we could not move x out of the adversarial region. However, when η is too large, we may optimize x into an image of another class."

## [NEGATIVE] Reduced Timestep Sampling (T')
Reducing the number of timesteps used in computing the diffusion loss, either by using only the first T' timesteps or by uniform systematic sampling

**Delta**: Significant drop in robust accuracy with reduced T', while clean accuracy is largely unaffected
**Condition**: Diffusion Classifier on CIFAR-10, ℓ∞ norm ablation

**Evidence**: "Although a significant reduction of T′ does not lead to an obvious drop in clean accuracy, it will significantly affect robust accuracy due to the reason discussed in Sec. 3.5."

## [NEUTRAL] Multiple ε Sampling
Sampling ε multiple times or keeping ε the same across timesteps/classes to improve estimation of the noise prediction expectation

**Delta**: No improvement in robustness or accuracy
**Condition**: Diffusion Classifier on CIFAR-10, ablation study

**Evidence**: "we also attempt to improve the estimation of Eε[wt∥ϵθ(xt, t, y) − ε∥²₂] by sampling ε multiple times or keeping ε the same for different timesteps or different classes. However, these increase neither robustness nor accuracy because we have already computed T times for the expectation over t."

## [NEGATIVE] DiffPure Adaptive Attack (Exact Gradient + EOT)
Evaluating DiffPure with exact gradient computation via gradient checkpoints and Expectation Over Time (EOT) to reduce randomness impact

**Delta**: Reduces DiffPure robust accuracy from 71.29% to 44.53% under ℓ∞ (ϵ=8/255) and from 80.60% to 75.59% under ℓ2
**Condition**: DiffPure baseline, CIFAR-10, adaptive attack evaluation

**Evidence**: "We lower the robust accuracy of DiffPure (Nie et al., 2022) from 71.29% to 44.53% under the ℓ∞ norm with ϵ∞ = 8/255, and from 80.60% to 75.59% under the ℓ2 norm with ϵ2 = 0.5"

## [POSITIVE] Low Gradient Variance in RDC
RDC exhibits exceptionally low gradient variance compared to DiffPure, indicating absence of obfuscated gradients

**Delta**: DiffPure is more than 640× as random as DC/RDC and ~16× as random as LM in gradient cosine similarity
**Condition**: Gradient randomness analysis on CIFAR-10, cosine similarity metric

**Evidence**: "the gradients of our methods exhibit low randomness, while DiffPure is more than 640 times as random as DC, RDC, and about 16 times as random as LM. Thus, the robustness of our methods is not primarily due to the stochasticity of gradients."

## [POSITIVE] Adversarial Training with Diffusion-Generated Data (AT-EDM)
Training discriminative classifiers adversarially using data generated by EDM diffusion models

**Delta**: 70.90% robust accuracy under ℓ∞, best prior method before RDC
**Condition**: CIFAR-10, ℓ∞ norm, WRN70-16 architecture; limited generalization to unseen threats

**Evidence**: "Notably, RDC outperforms the previous state-of-the-art model AT-EDM (Wang et al., 2023b) by +4.77% under the ℓ∞ norm."

## [NEUTRAL] Uniform Prior p(y)=1/K
Assuming a uniform class prior when computing posterior class probabilities via Bayes' theorem

**Delta**: Not quantified separately; method also supports non-uniform priors
**Condition**: CIFAR-10 and ImageNet with balanced class distributions

**Evidence**: "we assume a uniform prior p(y) = 1/K for simplicity, which is common for most of the datasets... our method is also applicable for non-uniform priors by adding log p(y) to the logit of class y"
