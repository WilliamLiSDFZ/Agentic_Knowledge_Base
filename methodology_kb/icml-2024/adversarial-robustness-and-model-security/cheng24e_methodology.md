# BadPart: Unified Black-box Adversarial Patch Attacks against Pixel-wise Regression Tasks

**Source**: https://proceedings.mlr.press/v235/cheng24e.html

## [POSITIVE] Square-based Patch Optimization Framework
Iteratively optimizes a square-shaped sub-area within the patch region, dynamically altering the location and size of the target square area to constrain the large search space inherent to the entire patch

**Delta**: outperforms baseline
**Condition**: Applied across all 7 models on MDE and OFE tasks under black-box settings

**Evidence**: "BADPART obtains the best attack performance on all models under various patch sizes. The performance of BADPART is even close to the white-box attack reference on some models (e.g., Monodepth2, DepthHints and SQLDepth)."

## [POSITIVE] Probabilistic Square Sampling (PS)
After an initialization phase of uniform sampling, uses the pixel-wise error map as an indicator of vulnerable areas to calculate a probability distribution for square location sampling, giving higher probability to areas with larger errors

**Delta**: most significant individual contribution among the three design choices
**Condition**: Applied after initialization period K iterations; evaluated on Monodepth2 and FlowNet2 with 300K queries

**Evidence**: "When considering each design individually, PS makes the most significant contribution and delivers the second-best performance."

## [POSITIVE] Score Normalization (SN)
Normalizes positive and negative noise scores by scaling them to [0,1] and [0,-1] respectively to handle small and imbalanced scores

**Delta**: contributes to best combined performance of 60.46 DEE on Monodepth2 and 17.13 EPE on FlowNet2
**Condition**: Used in score-based gradient estimation; evaluated on Monodepth2 and FlowNet2

**Evidence**: "the integration of all three design choices yielded the best attack performance for both models... The other two designs can also enhance the performance to some extent."

## [POSITIVE] Adaptive Scaling (AS)
Divides positive (or negative) scores by the number of positive (or negative) elements to allocate greater weights to the side with fewer elements, inspired by HardBeat but adapted for regression tasks

**Delta**: contributes to best combined performance of 60.46 DEE on Monodepth2 and 17.13 EPE on FlowNet2
**Condition**: Used in score-based gradient estimation; evaluated on Monodepth2 and FlowNet2

**Evidence**: "the integration of all three design choices yielded the best attack performance for both models... The other two designs can also enhance the performance to some extent."

## [POSITIVE] Score-based Gradient Estimation
Generates a batch of b random binary noises constrained by threshold epsilon on the square area, evaluates each noise's impact on attack performance as a score, then computes weighted average of noises to estimate gradients

**Delta**: outperforms baseline gradient estimation methods
**Condition**: Applied per optimization step on a randomly sampled training image

**Evidence**: "This efficiency is attributable to the more precise gradient estimation within the strategically selected square areas in BADPART."

## [POSITIVE] Number of Trials b=20
Using 20 random noise samples per gradient estimation step, balancing query efficiency and gradient accuracy

**Delta**: best balance between accuracy and efficiency
**Condition**: Ablation on Monodepth2 and FlowNet2; compared against b=1,10,15,20,30

**Evidence**: "b=20 achieves a good balance in our study and is utilized as the default settings."

## [NEGATIVE] Low Number of Trials b=1
Using only 1 random noise sample per gradient estimation step

**Delta**: decreased attack performance relative to b=20
**Condition**: Ablation study on Monodepth2 and FlowNet2

**Evidence**: "less trials (e.g., b=1) could decrease the accuracy of gradient estimation, hence impacting the attack performance"

## [NEGATIVE] High Number of Trials b=30
Using 30 random noise samples per gradient estimation step

**Delta**: degraded efficiency requiring more queries
**Condition**: Ablation study on Monodepth2 and FlowNet2

**Evidence**: "large trials (e.g., b=30) would require more query times and degrade the efficiency."

## [POSITIVE] Intra-square Threshold T1=1
Controls tolerance for negative update steps within a square area; at T1=1, a different square location is chosen after just 1 non-improving step

**Delta**: optimal performance on both Monodepth2 and FlowNet2
**Condition**: Ablation on Monodepth2 and FlowNet2; compared against T1=1,3,5,10,15

**Evidence**: "BADPART yields optimal performance on both models when T1 is set to 1, and it is adopted as our default setting."

## [NEUTRAL] Vertical Strip Patch Initialization
Initializes the patch region with vertical strips where the color of each stripe is sampled uniformly at random from {0,1}^3

**Delta**: not quantified separately
**Condition**: Used as starting point for all patch optimization experiments

**Evidence**: "we initialize the patch region with vertical strips, where the color of each stripe is sampled uniformly at random from {0,1}^3"

## [POSITIVE] Noise Bound Decay
The threshold epsilon for noise is initialized as alpha=0.1 and decays by factor gamma=0.98 when best attack performance is not updated for T2 iterations of square selection

**Delta**: not substantially impacted except for large T2 values
**Condition**: Inter-square threshold ablation on Monodepth2 and FlowNet2

**Evidence**: "its influence on the attack performance is not substantial, except for a large value setting on FlowNet2 (e.g., T2=15). Consequently, we have set T2 to 1 in our main experiments."

## [POSITIVE] Binary Noise Values {-epsilon, epsilon}
Constraining noise tensor values to either epsilon or -epsilon rather than continuous values

**Delta**: not quantified separately
**Condition**: Applied in score-based gradient estimation for all experiments

**Evidence**: "Values of the noise tensor are either epsilon or -epsilon as (Moon et al., 2019) has indicated that the optimal adversarial noise is mostly found on vertices of the bound."

## [POSITIVE] Adam Optimizer for Patch Update
Uses Adam optimizer with learning rate 0.1 and beta1=beta2=0.5 to update the square area using estimated gradients

**Delta**: not quantified separately
**Condition**: Applied in all main experiments

**Evidence**: "we update the square area with Adam optimizer using the estimated gradients (step 6)"

## [NEGATIVE] Universal Attack vs Single-image Attack
Generating a single patch that works across arbitrary unseen images rather than optimizing per-image

**Delta**: requires more queries (e.g., 50K) compared to single-image attack which achieves significant errors at 10K queries
**Condition**: Comparison between universal and single-image attack settings

**Evidence**: "Although the patch generation process could require more queries, it is a one-time effort and the generated patch can attack arbitrary unseen images without further queries... for both the MDE and OFE tasks, the errors caused by our single-image attack are already significant at 10K queries."

## [POSITIVE] Random Noise Addition to Bypass Blacklight Defense
Adding random noise on each attack sample to bypass the Blacklight query-based defense, which relies on hash similarity between consecutive queries

**Delta**: 0% detection rate under 800K queries
**Condition**: Applied when evaluating against Blacklight defense on Monodepth2 and FlowNet2

**Evidence**: "for both MDE and OFE tasks, the detection rate remains zero under 800K queries, while the attack performance is not affected and continues to increase with more queries."

## [POSITIVE] Error Map Smoothing with Square-sized Kernel
Smoothing the pixel-wise error map with a filter kernel of the same size as the current square before computing sampling probabilities, to avoid extreme values at certain locations

**Delta**: not quantified separately
**Condition**: Applied in probabilistic square sampling after initialization period

**Evidence**: "We first smooth the pixel-wise error map M with a filter kernel that has the same size of the square, which is to avoid extreme values at certain locations"

## [POSITIVE] Coarse-to-fine Square Size Schedule
Using a predefined schedule that reduces square size as iteration index increases, transitioning from coarse to fine-grained optimization

**Delta**: not quantified separately
**Condition**: Applied across all experiments with schedule set at 100,500,1500,3000,5000,10000 iterations

**Evidence**: "As the index escalates, the size diminishes, indicative of a transition from coarse to fine-grained optimization"

## [NEGATIVE] GenAttack Baseline (Genetic Algorithm)
Genetic algorithm-based black-box patch attack adapted from classification to pixel-wise regression tasks

**Delta**: nearly no effect; worst performing baseline
**Condition**: Evaluated on all 7 models across MDE and OFE tasks

**Evidence**: "GenAttack performs the worse and has nearly no effect."

## [POSITIVE] Gradient Estimation vs Random Search
Using gradient estimation (BADPART) rather than single-step random search (SquareAttack-style) for updating each square area

**Delta**: outperforms baseline
**Condition**: Compared against SquareAttack-inspired Patch-RS baseline

**Evidence**: "Unlike SquareAttack, BADPART iteratively updates each square area using novel gradient estimation rather than a single-step trial. This refinement transforms our approach into a more precise optimization process rather than random search, thereby strengthening the attack's effectiveness."
