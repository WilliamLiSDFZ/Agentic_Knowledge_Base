# Understanding and Diagnosing Deep Reinforcement Learning

**Source**: https://proceedings.mlr.press/v235/korkmaz24a.html

## [POSITIVE] RA-NLD (Robustness Analysis via Non-Lipschitz Directions)
A method that computes the principal non-Lipschitz direction by aggregating gradient information of the softmax cross-entropy loss across states visited by the policy, then extracting the dominant eigenvector of the resulting matrix to identify correlated directions of instability in the deep neural policy manifold.

**Delta**: outperforms baseline
**Condition**: Applied to deep reinforcement learning policies in the Arcade Learning Environment for diagnosing non-robust features

**Evidence**: "Through experiments in the Arcade Learning Environment (ALE), we demonstrate the effectiveness of our technique for identifying correlated directions of instability, and for measuring how sample shifts remold the set of sensitive directions in the neural policy landscape."

## [NEGATIVE] Certified Adversarial Training (SA-DDQN)
State-Adversarial Double Deep Q-Network that adds a regularizer to the temporal difference loss during training to certify robustness against adversarial perturbations on state observations.

**Delta**: dramatically larger oscillations over time
**Condition**: Applied to deep reinforcement learning policies in RoadRunner, Pong, Freeway, and BankHeist environments

**Evidence**: "state-of-the-art robust training techniques yield learning of disjoint unstable directions, with dramatically larger oscillations over time, when compared to standard training."

## [NEGATIVE] Certified Adversarial Training - Disjoint Non-Robust Features
Certified adversarial training causes the policy to learn non-robust features that are tightly concentrated on disjoint coordinates, shifted from where they appear under vanilla training.

**Delta**: descriptive: features concentrated on disjoint coordinates with significant location shift
**Condition**: SA-DDQN adversarial training compared to vanilla DDQN training

**Evidence**: "The non-robust features of the adversarially trained deep neural policies are much more tightly concentrated on disjoint coordinates in the state observations, and these areas of concentration have moved significantly from where they were under vanilla training."

## [NEGATIVE] Certified Adversarial Training - Temporal Instability
Adversarially trained policies exhibit much higher variance in gradient norm across states compared to vanilla trained policies.

**Delta**: much higher variance in gradient norm
**Condition**: Measured via l2-norm of gradient across states in RoadRunner, Pong, and Freeway

**Evidence**: "In both RoadRunner and Freeway, the adversarially trained policy has much higher variance in the gradient norm and thus in the level of instability. This is in contrast to the vanilla trained policy which tends to have a much smoother distribution which remains closer to the mean."

## [POSITIVE] Feature Correlation Quotient (FCQ)
A scalar metric bounded between 0 and 1 that quantifies how correlated the non-robust features from a transformed set of states are to those from a baseline set, enabling quantitative comparison of vulnerability patterns under different conditions.

**Delta**: descriptive: provides bounded quantitative measure consistent with qualitative visualizations
**Condition**: Used to compare non-robust feature sets across adversarial attacks, distributional shifts, and independent runs

**Evidence**: "the results for Λ(S_Ψ, S) help us to quantitatively understand the effects of the environmental changes in the MDP, while agreeing well with the qualitative results of the RA-NLD outputs."

## [NEGATIVE] Carlini & Wagner Adversarial Attack
Distance-minimization based adversarial perturbation method that computes the smallest perturbation to change the network output, applied to deep RL policy state observations.

**Delta**: Λ drops from 0.9917 to 0.9499 (Freeway), 0.8360 to 0.2837 (BankHeist), 0.7652 to 0.1621 (RoadRunner), 0.4934 to 0.0408 (Pong)
**Condition**: Applied to vanilla-trained DDQN policies across four Atari games

**Evidence**: "while the Carlini&Wagner formulation leaves a distinct signature on the vulnerable representation pattern... sorting from largest to smallest correlation quotient for BankHeist yields Nesterov momentum, Elastic-Net, and then Carlini&Wagner."

## [NEGATIVE] Nesterov Momentum Adversarial Attack
Adversarial perturbation method using Nesterov momentum to compute epsilon-bounded perturbations for deep RL policies by computing gradients at a lookahead point.

**Delta**: Λ drops from 0.9917 to 0.7868 (Freeway), 0.8360 to 0.3407 (BankHeist), 0.7652 to 0.3826 (RoadRunner), 0.4934 to 0.3444 (Pong)
**Condition**: Applied to vanilla-trained DDQN policies; produces least disruption to non-robust feature patterns among tested attacks

**Evidence**: "the non-robust features under Nesterov momentum appear most similar to those of the untransformed states."

## [NEGATIVE] DeepFool Adversarial Attack
Adversarial perturbation method that repeatedly computes projections to the closest separating hyperplane of a linearization of the deep neural network.

**Delta**: Λ drops from 0.9917 to 0.6869 (Freeway), 0.8360 to 0.1748 (BankHeist), 0.7652 to 0.5353 (RoadRunner), 0.4934 to 0.3277 (Pong)
**Condition**: Applied to vanilla-trained DDQN policies across four Atari games

**Evidence**: "the qualitative similarity between the visualizations in Figure 1 of the different transformed states is matched by their ranking under Λ(S_Ψ, S)"

## [NEGATIVE] Elastic-Net Adversarial Attack
Adversarial perturbation method based on l1-regularization of the l2-norm bounded Carlini & Wagner formulation.

**Delta**: Λ drops from 0.9917 to 0.7259 (Freeway), 0.8360 to 0.3092 (BankHeist), 0.7652 to 0.5251 (RoadRunner), 0.4934 to 0.1053 (Pong)
**Condition**: Applied to vanilla-trained DDQN policies across four Atari games

**Evidence**: "sorting from largest to smallest correlation quotient for BankHeist yields Nesterov momentum, Elastic-Net, and then Carlini&Wagner."

## [NEGATIVE] Rotation Distributional Shift
Natural imperceptible transformation applying rotation modification to state observations to evaluate distributional shift effects on learned non-robust representations.

**Delta**: Λ drops from 0.9917 to 0.1381 (Freeway), 0.8360 to 0.2951 (BankHeist), 0.7652 to 0.3350 (RoadRunner), 0.4934 to 0.1365 (Pong)
**Condition**: Applied to vanilla-trained DDQN policies; causes large shift in non-robust feature locations

**Evidence**: "perspective transform, blurring, rotation, and B&C causing the emphasized region to move to different locations."

## [NEGATIVE] Blurring Distributional Shift
Natural imperceptible transformation applying blurring to state observations to evaluate distributional shift effects on learned non-robust representations.

**Delta**: Λ drops from 0.9917 to 0.2657 (Freeway), 0.8360 to 0.0954 (BankHeist), 0.7652 to 0.2496 (RoadRunner), 0.4934 to 0.0847 (Pong)
**Condition**: Applied to vanilla-trained DDQN policies; among the most disruptive natural transformations

**Evidence**: "distributional shifts introduce different sets of correlated non-robust features compared to adversarial attacks."

## [NEGATIVE] Compression Artifacts Distributional Shift
Natural imperceptible transformation applying JPEG compression artifacts (diminution in high frequency components) to state observations.

**Delta**: Λ drops from 0.9917 to 0.9056 (Freeway), 0.8360 to 0.3881 (BankHeist), 0.7652 to 0.2436 (RoadRunner); Pong largely unaffected at 0.4934 to 0.4934
**Condition**: Applied to vanilla-trained DDQN policies; least disruptive natural transformation in some environments

**Evidence**: "in Pong the second highest value for Λ(S_Ψ, S) occurs for S_Ψ collected with compression artifacts, as this corresponds precisely to the qualitative similarity between the regions emphasized in the visualization of G_S for untransformed and compression artifacts."

## [NEGATIVE] Brightness and Contrast Distributional Shift
Natural imperceptible transformation applying linear brightness and contrast modification to state observations.

**Delta**: Λ drops from 0.9917 to 0.8676 (Freeway), 0.8360 to 0.3095 (BankHeist), 0.7652 to 0.4369 (RoadRunner), 0.4934 to 0.1678 (Pong)
**Condition**: Applied to vanilla-trained DDQN policies across four Atari games

**Evidence**: "perspective transform, blurring, rotation, and B&C causing the emphasized region to move to different locations."

## [NEGATIVE] Perspective Transform Distributional Shift
Natural imperceptible transformation applying perspective transformation to state observations to evaluate distributional shift effects.

**Delta**: Λ drops from 0.9917 to 0.3010 (Freeway), 0.8360 to 0.1723 (BankHeist), 0.7652 to 0.3308 (RoadRunner), 0.4934 to 0.4278 (Pong)
**Condition**: Applied to vanilla-trained DDQN policies across four Atari games

**Evidence**: "perspective transform, blurring, rotation, and B&C causing the emphasized region to move to different locations."

## [POSITIVE] Softmax Cross-Entropy Approximation for Non-Lipschitz Direction
Using the softmax cross-entropy loss between the softmax policy and the argmax policy to approximate the maximization objective in the non-Lipschitz direction definition, enabling efficient gradient-based computation.

**Delta**: descriptive: enables tractable computation of non-Lipschitz directions
**Condition**: Used as the core computational step in Algorithm 1 (RA-NLD)

**Evidence**: "Eqn 5 can be approximated by using the softmax cross entropy loss... Setting v = sg − s, shows that maximizing the softmax cross entropy approximates the maximization in Definition 5."

## [POSITIVE] Principal Component Analysis via Eigendecomposition for Aggregating Non-Robust Directions
Computing the dominant eigenvector of the sum of outer products of per-state non-Lipschitz directions to obtain a single principal direction capturing correlated non-robust features across multiple states.

**Delta**: descriptive: provides a single interpretable direction capturing aggregate vulnerability information
**Condition**: Applied over sets of states collected across 10 episodes in the ALE

**Evidence**: "GS is the eigenvector corresponding to the largest eigenvalue of L(S)... the dominant eigenvector corresponds to GS, the largest correlation with non-Lipschitz directions across time, which follows from the standard analysis of principal component analysis."

## [NEUTRAL] Double Deep Q-Network (DDQN) with Dueling Architecture
Standard (vanilla) training using Double DQN algorithm with the dueling network architecture and experience replay as the baseline policy training method.

**Delta**: descriptive: smoother gradient norm distribution closer to mean compared to adversarially trained policies
**Condition**: Used as baseline comparison against SA-DDQN adversarial training in RoadRunner, Pong, Freeway, BankHeist

**Evidence**: "the vanilla trained policy which tends to have a much smoother distribution which remains closer to the mean."

## [POSITIVE] Fourier Transform Analysis of Principal Non-Lipschitz Direction
Applying Fourier transform to the principal non-Lipschitz direction GS to reveal differences in spatial frequency content between vanilla and adversarially trained policies.

**Delta**: descriptive: reveals consistent distinguishable signature between adversarial and vanilla training
**Condition**: Applied to GS computed from vanilla and adversarially trained policies in RoadRunner, BankHeist, Pong, and Freeway

**Evidence**: "The Fourier transform reveals clear differences in the spatial frequencies occupied by GS under vanilla and adversarial training. There is a consistent trend that the larger entries of the Fourier transform are more evenly and smoothly spread out for the adversarially trained policies. Thus, adversarial training leaves a consistent signature on the non-robust features detectable via the Fourier transform of GS."
