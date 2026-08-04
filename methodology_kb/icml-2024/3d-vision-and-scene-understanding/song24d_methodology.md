# OSN: Infinite Representations of Dynamic 3D Scenes from Monocular Videos

**Source**: https://proceedings.mlr.press/v235/song24d.html

## [POSITIVE] Object Scale Network (OSN)
A simple MLP-based network (4 hidden layers, 64 nodes) that takes sampled multi-object scale combinations as input and predicts a validity score between 0 and 1, learning valid scale ranges for all dynamic objects in a scene.

**Delta**: PSNR 25.984 vs best baseline 24.695 on Dynamic Indoor Scene; SSIMAE 0.094 vs best baseline 0.137
**Condition**: Dynamic novel view synthesis from monocular video on Dynamic Indoor Scene, Oxford Multimotion, and NVIDIA Dynamic Scene datasets

**Evidence**: "Our OSN clearly surpasses all baselines in dynamic novel view RGB synthesis on all datasets... Most notably, our method achieves superior accuracy in novel view depth estimation with the lowest SSIMAE score of 0.094 on the Dynamic Indoor Scene Dataset"

## [POSITIVE] Scaled Composite Rendering
A rendering technique that combines shape, color, and scale information of all K objects by transforming sampled points between object spaces using object scales and camera poses, generating composite RGB, depth, and segmentation outputs.

**Delta**: outperforms baseline
**Condition**: Joint optimization of object scale-invariant representations and object scale network during training

**Evidence**: "we propose the following two techniques: scaled composite rendering and soft Z-buffer rendering... driving both object scale-invariant representations and object scale ranges to be accurately learned"

## [POSITIVE] Soft Z-buffer Rendering
A fast rendering strategy inspired by rasterization Z-buffer that determines object segmentation for sampled scale combinations by comparing scaled depth values across object spaces, avoiding repeated full volume rendering queries.

**Delta**: nearly H times faster than scaled composite rendering for H scale combination samples
**Condition**: Generating pseudo ground truth validity labels for training the object scale network

**Evidence**: "the scaled composite rendering needs to query all K object scale-invariant networks H times, while the soft Z-buffer rendering only needs to query once followed by H times of a simple operation in Equation 18, being nearly H times faster overall"

## [POSITIVE] Two-stage Joint Training (Bootstrapping + Alternating Optimization)
A training procedure with Stage 1 bootstrapping per-object representations independently, followed by Stage 2 alternating optimization between object scale-invariant networks and the object scale network for R rounds.

**Delta**: R=5 achieves PSNR 25.984, SSIMAE 0.094, PQ 92.211, mIoU 92.451 vs R=1 PSNR 23.123, SSIMAE 0.266, PQ 75.558, mIoU 78.896
**Condition**: Joint optimization on Dynamic Indoor Scene Dataset

**Evidence**: "Optimizing only one round is not sufficient for the object scale network and the object scale-invariant networks to benefit each other. 2) The early independent per-object optimization is indeed helpful, but our framework would not collapse without it."

## [POSITIVE] Bootstrapping Per-object Representations (Stage 1)
Independent volume rendering optimization for each object separately using RGB and depth losses before joint optimization begins.

**Delta**: w/o bootstrapping: PSNR 24.467, SSIMAE 0.174, PQ 89.139 vs with bootstrapping (R=5): PSNR 25.984, SSIMAE 0.094, PQ 92.211
**Condition**: Ablation study on Dynamic Indoor Scene Dataset

**Evidence**: "The early independent per-object optimization is indeed helpful, but our framework would not collapse without it."

## [NEGATIVE] Excessive Alternating Optimization Rounds (R=10)
Running more than the default 5 rounds of alternating optimization between object scale-invariant networks and the object scale network.

**Delta**: R=10: PSNR 25.065, SSIMAE 0.108 vs R=5: PSNR 25.984, SSIMAE 0.094
**Condition**: Ablation study on Dynamic Indoor Scene Dataset

**Evidence**: "Excessively training many rounds may not be necessary, as incorrect scale combinations may slip in and lead to inferior object representations over time."

## [POSITIVE] Object Scale-Invariant Representation Module (TensoRF-based)
Per-object shape and appearance representation using TensoRF with VM decomposition within a unit 3D volume, treating each object as static by using its N timestamp frames as multi-view images.

**Delta**: outperforms baseline
**Condition**: Per-object 3D representation in the OSN framework

**Evidence**: "we simply regard each object as static by treating its total N timestamp RGB frames as multi-view images, and then use a single network to represent each object respectively. In particular, we adopt an existing TensoRF (Chen et al., 2022) to represent each object"

## [POSITIVE] Sampling 1000 Scene Configurations at Test Time
At inference, sampling 1000 different scale combinations and reporting the best matching scores, exploiting the framework's ability to represent infinitely many valid 3D scene configurations.

**Delta**: OSN significantly outperforms all baselines on 50 ground truth scenes: PSNR 22.940±1.004 vs best baseline 18.978±1.249
**Condition**: Evaluation with multiple ground truths (50 configurations) on Gnome House scene

**Evidence**: "our OSN significantly outperforms all baselines regarding both the average performance and variance, since our method can easily produce an approximate solution (out of 1000 samples) for any group of ground truths, while baselines always provide the same solution regardless of different ground truth 3D scene configurations"

## [NEUTRAL] MiDaS Depth Supervision for Baselines
Using pretrained monocular depth estimator MiDaS to provide depth supervision with scales inherently aligned across multi-view for baseline methods.

**Delta**: mixed results: improves some baselines (e.g., DynNeRF PSNR 22.272 w/ MiDaS vs 21.479 w/o on Dynamic Indoor) but hurts others (e.g., HexPlane PSNR 17.968 w/ MiDaS vs 18.637 w/o)
**Condition**: Baseline methods on Dynamic Indoor Scene and Oxford Multimotion datasets

**Evidence**: "adding pretrained depth priors may incur unreliable geometry constraints and temporal inconsistency"

## [NEUTRAL] Per-object SfM for Pose and Depth Estimation
Using Structure-from-Motion independently per object to estimate camera-to-object relative poses and relative depth values via triangulation, without sharing scales across objects.

**Delta**: scales not aligned across objects; baselines with SfM depth perform comparably or worse than MiDaS depth variants
**Condition**: Data preprocessing stage for all methods using per-object SfM depth

**Evidence**: "Both the poses and depth values can only be estimated for each object, and the scales cannot be shared across multiple objects in the same scene, fundamentally because the motion and scale of each object are visually compounded with the unknown camera motion."

## [NEGATIVE] Separate Per-object Training (without composite rendering)
Training each object's TensoRF model independently without accounting for mutual visual occlusions from other objects.

**Delta**: inferior to joint optimization
**Condition**: Stage 1 bootstrapping only, without Stage 2 joint optimization

**Evidence**: "such a separate training scheme tends to be inferior, as it fails to take into account the mutual visual occlusions caused by other objects. Most importantly, the object scale network fmlp has yet to be optimized, and it can only be optimized by composing all scaled K objects."

## [POSITIVE] Normalized Scale Range Sampling [0,1)
Uniformly sampling object scales from a predefined normalized range [0,1) rather than an unbounded range, with a linear mapping back to the 3D scene volume.

**Delta**: enables stable optimization
**Condition**: Object scale network input during training and inference

**Evidence**: "the remaining K−1 object scales {s2, · · · , sK} are uniformly sampled from a predefined normalized range [0, 1). Note that, an unbounded/unnormalized range sampling would pose difficulties to optimize in practice."

## [POSITIVE] Validity Score Threshold (0.95) for Scale Sampling
Requiring sampled scale combinations to have a predicted validity score above 0.95 before using them in scaled composite rendering, with resampling if below threshold.

**Delta**: ensures valid scale combinations are used
**Condition**: Scaled composite rendering during joint optimization

**Evidence**: "their corresponding sampled scales [s1, · · · , sK] should be deemed as valid, meaning that the estimated validity score p = fmlp([s1, · · · , sK]) should be larger than a threshold, e.g., 0.95 in our implementation. Otherwise, we need to resample until the estimated score is above 0.95"

## [POSITIVE] Anchor Object Scale Fixing
Fixing the scale of one reference object (typically the largest, e.g., background) to 1 and only estimating relative scales of the remaining K-1 objects.

**Delta**: simplifies optimization
**Condition**: Object scale network design for multi-object scenes

**Evidence**: "we select one object (usually the largest object such as the background for simplicity) and set its scale as 1, i.e., s1 = 1, and the remaining K−1 object scales {s2, · · · , sK} are uniformly sampled from a predefined normalized range [0, 1)."

## [POSITIVE] OSN Scale Estimation Accuracy
The object scale network's ability to estimate accurate object scales compared to ground truth, measured by MSE.

**Delta**: Average MSE 0.064 vs best competing method Total-Recon 0.114 on Dynamic Indoor Scene Dataset
**Condition**: Scale estimation evaluation on Dynamic Indoor Scene Dataset with per-object SfM depth

**Evidence**: "Table 4 shows OSN achieves average MSE of 0.064 compared to Total-Recon's 0.114 and other baselines ranging from 0.163 to 2.072"
