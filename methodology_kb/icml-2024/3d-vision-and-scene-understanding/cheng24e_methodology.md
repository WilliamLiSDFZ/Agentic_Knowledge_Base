# BadPart: Unified Black-box Adversarial Patch Attacks against Pixel-wise Regression Tasks

**Source**: https://proceedings.mlr.press/v235/cheng24e.html

## [POSITIVE] Square-based Patch Optimization Framework
Iteratively optimizes a square-shaped sub-area within the patch region, dynamically altering the location and size of the target square area to constrain the large search space inherent to the entire patch

**Delta**: outperforms baseline
**Condition**: Black-box adversarial patch attacks on pixel-wise regression tasks (MDE and OFE)

**Evidence**: "BADPART obtains the best attack performance on all models under various patch sizes. The performance of BADPART is even close to the white-box attack reference on some models (e.g., Monodepth2, DepthHints and SQLDepth)."

## [POSITIVE] Probabilistic Square Sampling (PS)
After an initialization phase of uniform sampling, uses the pixel-wise error map as an indication of vulnerable areas to calculate a probability distribution for square location sampling, giving higher probability to areas with larger errors

**Delta**: most significant individual contribution among the three design choices
**Condition**: Applied after initialization period K; used in combination with score normalization and adaptive scaling for best results

**Evidence**: "When considering each design individually, PS makes the most significant contribution and delivers the second-best performance."

## [POSITIVE] Score-based Gradient Estimation
Generates a batch of random binary noises on the selected square area, evaluates each noise's impact on attack performance as a score, then computes a weighted average of noises to estimate gradients

**Delta**: outperforms baseline
**Condition**: Used for optimizing each selected square area; more efficient than pixel-by-pixel zeroth-order optimization

**Evidence**: "This efficiency is attributable to the more precise gradient estimation within the strategically selected square areas in BADPART."

## [POSITIVE] Score Normalization (SN)
Normalizes positive scores to [0,1] and negative scores to [0,-1] to handle very small and imbalanced scores among positive and negative noise evaluations

**Delta**: contributes to best combined performance of 60.46 DEE on Monodepth2 and 17.13 EPE on FlowNet2
**Condition**: Part of score adjustment procedure in gradient estimation; best when combined with adaptive scaling and probabilistic sampling

**Evidence**: "the integration of all three design choices yielded the best attack performance for both models... The other two designs can also enhance the performance to some extent."

## [POSITIVE] Adaptive Scaling (AS)
Divides positive (or negative) scores by the number of positive (or negative) elements to allocate greater weights to the side with fewer elements, inspired by HardBeat but adapted for regression tasks

**Delta**: contributes to best combined performance of 60.46 DEE on Monodepth2 and 17.13 EPE on FlowNet2
**Condition**: Part of score adjustment procedure in gradient estimation; best when combined with score normalization and probabilistic sampling

**Evidence**: "the integration of all three design choices yielded the best attack performance for both models... The other two designs can also enhance the performance to some extent."

## [POSITIVE] Binary Noise Values {-ε, ε}
Constraining noise tensor values to either ε or -ε (vertices of the bound) rather than continuous values for gradient estimation

**Delta**: not quantified separately
**Condition**: Used in score-based gradient estimation step

**Evidence**: "Values of the noise tensor are either ε or −ε as (Moon et al., 2019) has indicated that the optimal adversarial noise is mostly found on vertices of the bound."

## [NEUTRAL] Noise Bound Decay
The threshold ε of the noise is initialized as α and decays by factor γ=0.98 if the best attack performance is not updated for T2 iterations of square selection

**Delta**: influence on attack performance is not substantial except for large T2 values
**Condition**: Inter-square threshold T2; large values (e.g., T2=15) can negatively impact FlowNet2 performance

**Evidence**: "its influence on the attack performance is not substantial, except for a large value setting on FlowNet2 (e.g., T2 = 15). Consequently, we have set T2 to 1 in our main experiments."

## [POSITIVE] Intra-square Threshold T1=1
Controls tolerance for negative update steps within a square area; when set to 1, immediately moves to a new square location after any non-improving step

**Delta**: optimal performance on both Monodepth2 and FlowNet2
**Condition**: Controls when to stop optimizing current square and sample a new location

**Evidence**: "BADPART yields optimal performance on both models when T1 is set to 1, and it is adopted as our default setting."

## [POSITIVE] Number of Trials b=20
Using 20 random noise samples per gradient estimation step, balancing query efficiency and gradient accuracy

**Delta**: best balance between accuracy and efficiency
**Condition**: Gradient estimation in score-based optimization; b=1 decreases accuracy, b=30 degrades efficiency

**Evidence**: "b=20 achieves a good balance in our study and is utilized as the default settings."

## [NEGATIVE] Low Number of Trials (b=1)
Using only 1 random noise sample per gradient estimation step

**Delta**: decreased gradient estimation accuracy and attack performance
**Condition**: Gradient estimation step; reduces query count but hurts attack quality

**Evidence**: "less trials (e.g., b=1) could decrease the accuracy of gradient estimation, hence impacting the attack performance"

## [NEGATIVE] High Number of Trials (b=30)
Using 30 random noise samples per gradient estimation step

**Delta**: requires more query times, degrades efficiency
**Condition**: Gradient estimation step; improves gradient accuracy but at high query cost

**Evidence**: "large trials (e.g., b=30) would require more query times and degrade the efficiency."

## [NEUTRAL] Vertical Strip Patch Initialization
Initializes the patch region with vertical strips where the color of each stripe is sampled uniformly at random from {0,1}^3

**Delta**: not quantified
**Condition**: Patch initialization at the start of optimization

**Evidence**: "we initialize the patch region with vertical strips, where the color of each stripe is sampled uniformly at random from {0,1}^3"

## [POSITIVE] Coarse-to-Fine Square Size Schedule
Pre-defined schedule that reduces square size as iteration index increases, transitioning from coarse to fine-grained optimization

**Delta**: not quantified separately
**Condition**: Square area selection across iterations; inspired by SquareAttack

**Evidence**: "As the index escalates, the size diminishes, indicative of a transition from coarse to fine-grained optimization"

## [POSITIVE] Error Map Smoothing
Smoothing the pixel-wise error map with a filter kernel of the same size as the square before probabilistic sampling, to avoid extreme values at certain locations

**Delta**: not quantified separately
**Condition**: Applied during probabilistic square sampling after initialization period

**Evidence**: "We first smooth the pixel-wise error map M with a filter kernel that has the same size of the square, which is to avoid extreme values at certain locations"

## [POSITIVE] Universal Attack with Random Sample Training
Training a universal adversarial patch on diverse training images rather than a single image, with random noise added to bypass query-based defenses like Blacklight

**Delta**: 0% detection rate under 800K queries by Blacklight defense
**Condition**: Against Blacklight query-based defense; universal attack setting

**Evidence**: "BADPART is a universal adversarial patch attack that does not depend on sample similarity, and the randomness in different samples could potentially enhance the universal effectiveness of the generated patch. Hence we add random noise on each attack sample to by-pass the defense... the detection rate remains zero under 800K queries"

## [POSITIVE] Adam Optimizer for Patch Update
Using Adam optimizer with learning rate 0.1 and β1=β2=0.5 to update the square area using estimated gradients

**Delta**: not quantified separately
**Condition**: Patch optimization step after gradient estimation

**Evidence**: "Then we update the square area with Adam optimizer using the estimated gradients (step ❻)"

## [POSITIVE] Single-image Attack Adaptation
Adapting the universal attack to target a single image by using only the target image as both training and validation set

**Delta**: significant errors at 10K queries for both MDE (9.060 DEE) and OFE (13.141 EPE)
**Condition**: When attacker targets a specific image rather than universal patch; reduces required query budget

**Evidence**: "for both the MDE and OFE tasks, the errors caused by our single-image attack are already significant at 10K queries."
