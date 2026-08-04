# Few-Shot Unsupervised Implicit Neural Shape Representation Learning with Spatial Adversaries

**Source**: https://proceedings.mlr.press/v235/ouasfi24a.html

## [POSITIVE] Adversarial Query Mining
Augmenting training query points with adversarial samples that maximize the loss in the vicinity of original queries, computed via first-order Taylor expansion and Cauchy-Schwarz inequality to find worst-case perturbations within a local radius.

**Delta**: outperforms baseline and state-of-the-art across all benchmarks; CD1 improves from 1.16 to 0.76 on ShapeNet, 0.58 to 0.49 on SRB sparse
**Condition**: Sparse and dense unoriented point cloud reconstruction; most impactful in sparse setting

**Evidence**: "Our method outperforms the baseline as well as the most related competition both quantitatively and qualitatively. We notice that our adversarial loss helps our model most in places where shape prediction is the hardest and most ambiguous, such as fine and detailed structures and body extremities."

## [POSITIVE] Local Adaptive Radii for Adversarial Samples
Using per-query local radii (rho_q = sigma_p * 10^-2) tied to the local input point cloud density, rather than a single global radius, to modulate adversarial sample density spatially.

**Delta**: CD1 improves from 0.98 (global radius) to 0.75 (local radius rho_q=sigma_p/100) on ShapeNet Table class
**Condition**: ShapeNet Table class ablation; applies when input point cloud has spatially varying density

**Evidence**: "We found empirically that using local radii {rho_q} in our context improves over using a single global radius rho and we provide an ablation later on of this design choice."

## [POSITIVE] Hybrid Multi-Task Loss with Learnable Weights
Combining the original NeuralPull projection loss with the adversarial loss using learnable scalar weights (lambda_1, lambda_2) following the multi-task learning strategy of Liebel & Korner 2018.

**Delta**: CD1 improves from 0.78 (adversarial loss alone) to 0.75 (hybrid loss) on ShapeNet Table class
**Condition**: ShapeNet Table class; important when shape-specific trade-off between adversarial regularization and original loss is needed for convergence

**Evidence**: "this strategy outperformed using the adversarial loss alone, leading to an improvement in CD1 from 0.78 to 0.75 in class Table of ShapeNet."

## [NEGATIVE] Adversarial Radius Too Small (rho_q = sigma_p/1000)
Setting the adversarial perturbation radius to a very small value (sigma_p/1000), reducing the range of hard query sampling.

**Delta**: CD1 degrades to 1.02 vs 0.75 at optimal radius on ShapeNet Table class
**Condition**: ShapeNet Table class ablation; when radius is too small to find meaningfully hard samples

**Evidence**: "Decreasing rho_q leads expectedly to worse results as less hard queries are available for sampling."

## [NEGATIVE] Adversarial Radius Too Large
Setting the adversarial perturbation radius to a very large value, causing adversarial samples to potentially have different nearest points in the input point cloud than their original queries, introducing spurious pseudo-supervision.

**Delta**: CD1 degrades from 0.75 at optimal to 0.92 at rho_q=sigma_p/10 on ShapeNet Table class
**Condition**: ShapeNet Table class ablation; when radius is too large relative to local point cloud density

**Evidence**: "we also note that very large values of rho_q can lead to spurious pseudo supervision, as adversarial samples q + delta run the risk of no longer having the same nearest point in the input point cloud as their original sample q."

## [NEGATIVE] Standard ERM Query Sampling (NeuralPull baseline)
Sampling query points from normal distributions centered at input point cloud samples with locally defined standard deviations, and minimizing empirical risk over these fixed queries without adversarial augmentation.

**Delta**: Validation Chamfer distance starts increasing early in training under sparse input; CD1=1.16 vs 0.76 for proposed method on ShapeNet
**Condition**: Sparse point cloud setting (1024 points); overfitting intensifies with sparser inputs

**Evidence**: "the validation error starts increasing quite early on in the training in the sparse input case for the baseline. This undesirable behaviour is remedied by our adversarial query mining."

## [NEUTRAL] Increasing Query Points Without Adversarial Strategy
Simply increasing the number of NeuralPull original query samples to match the total count used by the proposed method (original + adversarial queries), without the adversarial selection strategy.

**Delta**: Average Chamfer distance changes marginally from 0.581 to 0.576 on SRB
**Condition**: SRB benchmark; demonstrates that improvement comes from adversarial selection, not merely more samples

**Evidence**: "We find that the performance of NP with extra queries only leads occasionally to marginal improvement (On average Chamfer distance goes from 0.581 to 0.576 in SRB)."

## [POSITIVE] Validation Stabilization via Adversarial Training
The adversarial training strategy causes the validation Chamfer distance to stabilize and plateau at convergence rather than increasing, making evaluation epoch selection easier in unsupervised settings.

**Delta**: Validation stabilizes and plateaus vs. baseline where it increases early; best baseline performance surpassed within 4 minutes of training
**Condition**: Sparse point cloud setting; particularly relevant since ground truth is unavailable during unsupervised training

**Evidence**: "thanks to our method, and as illustrated in Figure 1, validation stabilizes and plateaus at convergence unlike our baseline, which makes it easier for us to decide the evaluation model epoch, given that evaluation measurements are normally unavailable in unsupervised settings."

## [POSITIVE] Optimal Local Radius (rho_q = sigma_p/100)
Setting the adversarial perturbation radius to sigma_p divided by 100, empirically found to be the best balance between finding hard samples and avoiding spurious supervision.

**Delta**: CD1=0.75 on ShapeNet Table class, best among all radius choices tested
**Condition**: ShapeNet Table class ablation; generalizes across datasets as default setting

**Evidence**: "A value of sigma_p * 10^-2 achieves empirically satisfactory results (p being the nearest point to the query q in the input point cloud)."
