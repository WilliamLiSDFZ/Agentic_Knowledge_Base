# Scale-Free Image Keypoints Using Differentiable Persistent Homology

**Source**: https://proceedings.mlr.press/v235/barbarani24a.html

## [POSITIVE] Persistent Homology-Based Keypoint Modeling
Models keypoints as local maxima of CNN feature maps using persistent homology (H1 generators of cubical complex), providing a scale-independent topological characterization instead of patch-wise heuristics.

**Delta**: best or second best across illumination and viewpoint repeatability columns in HPatches
**Condition**: HPatches benchmark, illumination and viewpoint splits

**Evidence**: "We show that thanks to the theoretical guarantees that underpin our method, we outperform previous sparse detectors in terms of repeatability and scale invariance."

## [POSITIVE] Boundary Similarity Loss Term (Sim)
A penalty term in the detector loss that penalizes topological features (local maxima) that are not reproducible across corresponding image pairs, computed via correspondences map U.

**Delta**: repeatability rises from ~1-6 (α=0) to 40-47 (α=10) on HPatches viewpoint split
**Condition**: HPatches viewpoint repeatability; required for any meaningful learning

**Evidence**: "The results show that the model's performance is poor in the absence of the Sim loss term (i.e. α = 0). Conversely, increasing α increases performance across all considered keypoint quantities."

## [POSITIVE] Persistence Term in Detector Loss
A peaky term that maximizes the prominence (death minus birth value) of topological features, acting as a weight that focuses optimization on prominent peaks and suppresses noisy low-intensity ones.

**Delta**: contributes to overall competitive repeatability scores; without Sim term alone leads to trivial grid solution
**Condition**: Must be combined with boundary similarity term; alone (α=0) leads to degenerate solution

**Evidence**: "The persistence also takes on the role of a weight term that multiplies the total contribution of the feature to the loss, and this prevents the optimization process from getting overwhelmed by thousands of noisy, low-intensity peaks, instead focusing on the refinement of the promising features."

## [NEGATIVE] Training Without Boundary Similarity (α=0)
Training using only the persistence maximization term without the boundary similarity penalty, which simplifies to maximizing squared persistence.

**Delta**: repeatability of 1.0-5.9 across keypoint counts vs 40.6-47.2 for α=10
**Condition**: HPatches viewpoint split ablation study

**Evidence**: "without the Sim component yields an output that resembles the trivial solution... training without the Sim component yields an output that resembles the trivial solution, a grid of 1s surrounded by 0s in every 3×3 image patch, disregarding the input image value."

## [POSITIVE] Hyperparameter α=10 (Loss Trade-off)
Setting the trade-off hyperparameter α between persistence and boundary similarity to 10, balancing keypoint quantity and quality.

**Delta**: repeatability 40.6-47.2 across keypoint counts; best at higher keypoint counts (2000-4000)
**Condition**: HPatches viewpoint split; optimal for larger keypoint budgets

**Evidence**: "The final hyperparameters configuration included α = 10... At α = 20 the repeatability continues to rise when the number of keypoints is limited but does not gain additional benefits from allowing a more significant number of keypoints, suggesting a trade-off imposed by the parameter's value."

## [NEUTRAL] Hyperparameter α=20 (Higher Loss Trade-off)
Setting α to 20, increasing the weight of the boundary similarity penalty relative to persistence.

**Delta**: best at low keypoint counts (250-1000: 44.0, 44.8, 45.3) but no gain at higher counts (45.1, 44.9 vs 46.1, 47.2 for α=10)
**Condition**: HPatches viewpoint split; better for small keypoint budgets, worse for large

**Evidence**: "At α = 20 the repeatability continues to rise when the number of keypoints is limited but does not gain additional benefits from allowing a more significant number of keypoints, suggesting a trade-off imposed by the parameter's value, balancing the quantity and quality of detected keypoints."

## [POSITIVE] Scale-Free Topological Keypoint Characterization
Using persistent homology to define keypoints without a fixed patch size, making detection scale-independent as persistence depends only on peak prominence not spatial extent.

**Delta**: second-best average scale repeatability (62.2); outperforms all other learnable methods; beats SIFT at 75% resize by 6.3 points
**Condition**: Scale repeatability experiment on resized HPatches images

**Evidence**: "MorseDet shines with 75% image resize (i.e. to images of 750×750), outperforming the second best method, SIFT, by 6.3 points... MorseDet performs significantly better than every other learnable method in this task. This is a direct consequence of the fact that previous learnable methods lack a principled framework for modeling local maxima."

## [POSITIVE] Single-Channel Height Map Output
Modifying the backbone's last layer to output a single channel scalar map (height map) instead of multi-channel feature volume, enabling application of Morse theory.

**Delta**: enables topology-based detection; height map captures structural information emergently
**Condition**: Required architectural choice for MorseDet framework

**Evidence**: "we modify the last layer of the backbone used in R2D2 to output a single channel... the last layer distills the feature volume into a single-channel unified spatial representation, which we call height map... it exhibits an attractive emergent property by effectively capturing much of the input structure in its height map."

## [POSITIVE] Non-Maximum Suppression at Inference
At inference time, keypoints are detected by applying fast non-maximum suppression to select local maxima of the height map above a threshold γ=0.7.

**Delta**: enables efficient inference without topological computation overhead
**Condition**: Inference only; training uses full persistent homology computation

**Evidence**: "At inference time, the keypoints are simply obtained by performing a fast non-maximum suppression algorithm that selects the locations corresponding to a local maximum of the height map with a value above a given threshold γ."

## [NEGATIVE] CPU-Based Discrete Morse Theory Loss Computation
The persistent homology loss computation runs on CPU following Robins et al. (2011) methodology, as GPU implementations are not widely available.

**Delta**: training takes approximately 10 hours on a single TITAN X GPU
**Condition**: Training on single TITAN X GPU with 12GB VRAM

**Evidence**: "Our current implementation of the loss function, aligned with the methodologies of (Robins et al., 2011), operates on a CPU. Despite this, as detailed in sec. 5.3, training takes roughly 10 hours."

## [NEUTRAL] L2Net Backbone with Small Kernels
Using L2Net as the fully convolutional backbone with the R2D2 modification of smaller kernels in last layers to reduce computational cost.

**Delta**: not separately quantified; enables competitive performance
**Condition**: Architecture choice for feature extraction backbone

**Evidence**: "our backbone of choice is a simple fully convolutional network; in particular, we adopt the L2Net with the modification proposed in (Revaud et al., 2019) that employs smaller kernels in the last layers, in order to reduce its computational cost."

## [POSITIVE] WASF Training Dataset with Homographic Correspondences
Training on the WASF dataset from R2D2 which provides homographic correspondences between image pairs, used to compute the boundary similarity loss.

**Delta**: enables unsupervised learning of repeatability from data
**Condition**: Training data choice; same as R2D2 baseline for fair comparison

**Evidence**: "For training our detector, we adopt WASF, the dataset released in (Revaud et al., 2019) to train R2D2, which provides homographic correspondences between pairs of images."

## [NEGATIVE] Patch-wise Local Maxima Approximation (prior methods)
Competing methods (R2D2, ALIKE, ALIKED) model keypoints as local maxima within fixed N×N patches using softmax relaxation, hard-coding keypoint density as a hyperparameter.

**Delta**: leads to scale-dependent detection; R2D2 single-scale repeatability inferior to MorseDet across most settings
**Condition**: Applies to R2D2, ALIKE, ALIKED and similar patch-wise detectors

**Evidence**: "they lack an analytical tool to locate these local extrema reliably and rely typically on a softmax-based approximation inside local patches of predefined size, thus bounding the detection frequency to this hyperparameter and fails to achieve scale invariance."

## [NEUTRAL] Multi-Scale Inference (prior methods)
Processing the same image multiple times at different resolutions to partially compensate for scale dependency in patch-wise detectors.

**Delta**: partially mitigates scale issues but produces redundant predictions
**Condition**: Applied to R2D2 and D2-Net as a workaround for scale dependency

**Evidence**: "Although R2D2 partially mitigates some of these issues through multi-scale inference, it tends to produce redundant predictions by clustering keypoints around the same semantic feature while potentially missing other points of interest."

## [NEUTRAL] Revisited Repeatability Metric (Mutual Nearest Neighbor)
Evaluation metric requiring keypoints to be mutually nearest neighbors across image pairs, preventing a single keypoint from matching multiple counterparts and penalizing redundant detections.

**Delta**: provides fairer evaluation; penalizes clustered/redundant keypoint detectors
**Condition**: Evaluation metric choice; affects all compared methods equally

**Evidence**: "This addition helps unequivocally associate underlying features and penalizes redundant detections, favoring detectors more prone to cover image features with a limited number of keypoints comprehensively."
