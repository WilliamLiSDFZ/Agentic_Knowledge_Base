# Et Tu Certifications: Robustness Certificates Yield Better Adversarial Examples

**Source**: https://proceedings.mlr.press/v235/cullen24a.html

## [POSITIVE] Certification Aware Attack (CAA)
A two-stage adversarial attack framework that exploits robustness certifications to (1) use certification radii as step-size guidance to speed up initial search, and (2) refine found adversarial examples by moving within certified radii of already-found adversarial examples to minimize perturbation norm.

**Delta**: 74% more often finds adversarial examples than comparable attacks; reduces median perturbation norm by more than 10%; up to 55% decrease in adversarial perturbation size relative to next best technique; 24% reduction in median attack size relative to next best attack when controlling for certified radii
**Condition**: Attacking certified models (randomised smoothing and IBP) on MNIST, CIFAR-10, and ImageNet

**Evidence**: "Our new Certification Aware Attack exploits certifications to produce computationally efficient norm-minimising adversarial examples 74% more often than comparable attacks, while reducing the median perturbation norm by more than 10%."

## [POSITIVE] Certification-Based Step Size Control
Using the certified radius at each iterative step to set a minimum step size, ensuring the next candidate point lies outside the certified region of all previously visited same-class points, enabling larger and more informative jumps during the search phase.

**Delta**: Speeds up initial stages of search with larger and more informative jumps; contributes to overall 74% improvement in finding adversarial examples
**Condition**: Initial search phase of CAA before an adversarial example is found

**Evidence**: "Exploiting certifications allows our new attack framework to (i) speed up the initial stages of the search with larger and more informative jumps, and (ii) to reduce the total adversarial perturbation"

## [POSITIVE] Certification-Based Adversarial Example Refinement
Once an adversarial example is found, using the certified radius at that adversarial point to take norm-minimizing steps back toward the original input while guaranteeing the point remains adversarial, since any point within the certified radius of a known adversarial example is also adversarial.

**Delta**: Produces median certification 11% smaller for MNIST, 12% smaller for CIFAR-10, and 52% smaller for ImageNet compared to other attacks
**Condition**: Refinement phase of CAA after an adversarial example has been identified

**Evidence**: "Our approach produces a median certification that is on average 11% smaller for MNIST, 12% for CIFAR-10, and 52% smaller in the case of Imagenet."

## [POSITIVE] Attacking Class Expectations Instead of Individual Noise Draws
Attacking the concentrated expectation of the smoothed classifier rather than individual draws under noise (as in Expectation Over Transformation), exploiting the high concentration of expectations for sufficiently large Monte Carlo sample sizes.

**Delta**: More numerically efficient than Expectation Over Transformation approach
**Condition**: Attacking randomised smoothing certified models

**Evidence**: "This contrasts with approaches like Expectation Over Transformation (Athalye et al., 2018), in which each sample under noise is attacked in a numerically inefficient manner."

## [POSITIVE] Gumbel Softmax Reparameterization for arg max
Replacing the non-differentiable arg max final layer with a Gumbel Softmax to enable gradient-based attacks, minimizing the impact of ensuring differentiability while maximizing difficulty to the attacker.

**Delta**: Enables gradient-based attacks on models with non-differentiable arg max layers without requiring alternative interventions
**Condition**: Models with non-differentiable arg max output layers under randomised smoothing

**Evidence**: "To both minimise the impact of ensuring differentiability and maximise the difficulty to the attacker, within this work we assume that the final arg max layer can be replaced with a Gumbel Softmax"

## [NEGATIVE] Constraining Adversarial Examples to Share Same Class as First Found Example
The refinement stage constrains all subsequent adversarial examples to share the same predicted class as the first identified adversarial example, which limits the search space but simplifies the algorithm.

**Delta**: May miss adversarial examples of smaller norm in other classes; particularly noted as a potential issue for 1000-class ImageNet
**Condition**: Refinement phase of CAA, especially on large-class datasets like ImageNet

**Evidence**: "One feature noted within Section 4.2 was that all adversarial examples identified by our Certification Aware Attack framework must share the same class prediction as the first identified adversarial example. Intuitively it would appear that such a drawback would induce a disproportionate increase in the median certified radii for the 1000-class ImageNet"

## [POSITIVE] Approximate sigma Estimation
Using an estimated or approximate value of the noise level sigma rather than the exact value when constructing the certification-aware attack, applicable when sigma is not directly accessible to the attacker.

**Delta**: Even over-estimating sigma by 50% can decrease the radius of identified adversarial perturbations under certain experimental conditions; still outperforms other frameworks
**Condition**: Limited threat model where attacker does not have direct access to sigma

**Evidence**: "even over-estimating σ by 50% can decrease the radius of the identified adversarial perturbation under certain experimental conditions... it also demonstrates the possibility of estimating σ as part of a surrogate model, in order to attack within a limited threat mode."

## [POSITIVE] MACER Training Objective
Augmenting the training loss to incorporate epsilon-robustness loss reflecting the proportion of training samples with robustness above a threshold, increasing average certified radius at the cost of significantly higher training cost.

**Delta**: Can increase average certified radius by 10-20%, but increases training cost by more than an order of magnitude
**Condition**: Training time; tested on CIFAR-10 with ResNet-110 architecture

**Evidence**: "In principle such a training-time modification can increase the average certified radius by 10–20%, however doing so does increase the overall training cost by more than an order of magnitude."

## [POSITIVE] Convex Relaxation Certification
Using linear relaxation to construct bounding output polytopes over input bounded perturbations for certification, generally providing tighter bounds than interval bound propagation.

**Delta**: Generally provides tighter bounds than IBP
**Condition**: Exact certification methods for neural network robustness

**Evidence**: "convex relaxation, which utilises linear relaxation to construct bounding output polytopes over input bounded perturbations (Salman et al., 2019b; Mirman et al., 2018; Weng et al., 2018; Zhang et al., 2018; Singh et al., 2019; Mohapatra et al., 2020), in a manner that generally provides tighter bounds than IBP"

## [NEGATIVE] Releasing Robustness Certifications Publicly
Publishing or releasing the robustness certificates alongside model predictions, which provides transparency but also gives attackers information to exploit for constructing smaller adversarial examples.

**Delta**: Enables attackers to produce adversarial examples 74% more often and with 10%+ smaller perturbation norms
**Condition**: Any deployed certified model where certifications are made available to potential attackers

**Evidence**: "these attacks can be used to assess the tightness of certification bounds, they also highlight that releasing certifications can paradoxically reduce security."

## [NEGATIVE] DeepFool Attack Against Certified Models
Applying the DeepFool attack (fast gradient-based minimal perturbation finder) against certified models as a baseline comparison.

**Delta**: Only 9% success rate on MNIST at sigma=0.5; failure to successfully identify norm-minimizing adversarial examples led to exclusion from broader parameter exploration
**Condition**: Test-time attacks against randomised smoothing certified models

**Evidence**: "while DeepFool is the fastest of all tested attacks, its failure to successfully identify norm minimising adversarial examples led to its exclusion from a broader parameter exploration."

## [NEUTRAL] Increasing Smoothing Noise Scale (sigma)
Using a larger additive noise scale in randomised smoothing, which increases certification size but also affects gradient smoothness and attack difficulty.

**Delta**: Leads to small increase in size of identified attacks relative to certified guarantees; ease of identifying attacks for larger sigma is offset by decreases in tightness of certified bound
**Condition**: Randomised smoothing certification; tested at sigma=0.5 and sigma=1.0

**Evidence**: "increasing σ leads to a small increase in the size of identified attacks, relative to certified guarantees. While this may at first appear contradictory, it suggests that the ease in identifying adversarial attacks for larger σ is offset by decreases in the tightness of the certified bound."

## [POSITIVE] Confident Adversarial Attack Requirement
Requiring that adversarial examples have a non-zero certified radius (i.e., the model is confidently wrong), rather than just finding any misclassified point, to avoid triggering inspection in operationalized certification systems.

**Delta**: Produces adversarial examples that are harder to detect in operationalized systems; avoids zero-radius adversarial examples that would trigger further inspection
**Condition**: Test-time attacks against deployed certified models

**Evidence**: "we introduce the idea of a confident adversarial attack against a certification mechanism being one in which a certification constructed at the adversarial example is non-zero... its certified radii would be 0, which would likely trigger further inspection in any operationalised certification system."
