# S3O: A Dual-Phase Approach for Reconstructing Dynamic Shape and Skeleton of Articulated Objects from Single Monocular Video

**Source**: https://proceedings.mlr.press/v235/zhang24ae.html

## [POSITIVE] Dual-Phase Training (S3O)
A two-phase approach that first learns coarse parametric models (shape and skeleton), then progresses to motion learning and fine detail addition, rather than learning all parameters simultaneously.

**Delta**: +5.7 keypoint transfer accuracy on DAVIS, +3.4 on PlanetZoo; 60% training time reduction
**Condition**: Articulated object reconstruction from single monocular video

**Evidence**: "S3O consistently surpasses both LASR and ViSER across all animal subjects and requires approximately 40% less training time... reduces the training time by approximately 60% compared to the state-of-the-art"

## [POSITIVE] Dynamic Rigidity (DR) Loss
A loss function that provides more deformation freedom to vertices near joints and less freedom to vertices along bones, based on entropy of skinning weight distributions, replacing the conventional As-Rigid-As-Possible (ARAP) loss.

**Delta**: outperforms baseline (qualitative improvement shown in Fig.6)
**Condition**: Mesh deformation regularization during articulated object reconstruction

**Evidence**: "incorporating Dynamic Rigidity into our reconstruction process yields a shape that adheres more closely to physical reality compared to methods utilizing As-Rigid-As-Possible (ARAP) modeling and without both regularization terms."

## [NEGATIVE] As-Rigid-As-Possible (ARAP) Loss
Conventional regularization that encourages constant distance between adjacent vertices, limiting movement near joints.

**Delta**: worse physical plausibility than DR loss (qualitative, Fig.6)
**Condition**: Used as baseline comparison against Dynamic Rigidity

**Evidence**: "The latter encourages the constant distance between the adjacent vertices, which limits the movement and deformation of the vertices near the joints."

## [POSITIVE] DINO Feature Loss in Coarse Phase
Using DINO self-supervised vision transformer features as a loss term during the coarse shape learning phase to quickly learn an initial model.

**Delta**: aids in quickly learning a coarse model in the initial phase
**Condition**: Coarse shape phase only

**Evidence**: "the use of DINO features effectively aids in quickly learning a coarse model in the initial phase"

## [NEGATIVE] DINO Feature Loss in Fine Phase
Continuing to use DINO feature loss during the fine shape learning phase.

**Delta**: hampers acquisition of more detailed shape
**Condition**: Fine shape phase; removed in S3O's fine phase

**Evidence**: "their limited accuracy eventually hampers the acquisition of a more detailed shape in later stages"

## [POSITIVE] Physical Skeleton vs Virtual Bones
Using a physical skeleton with bones placed according to anatomical structure and motion dynamics, rather than virtual bones determined by k-means clustering on mesh vertices.

**Delta**: outperforms LASR and ViSER; avoids rigid treatment of limbs
**Condition**: Skeleton-based articulated motion modeling

**Evidence**: "methods like LASR, ViSER, and BANMo use k-means clustering on meshes to determine virtual bone positions. This often results in larger areas like the torso getting more bones, while slender limbs have fewer... Such skewed distribution leads to a rigid treatment of entire limbs, as seen in LASR, preventing natural bending."

## [POSITIVE] 2D Optical Flow for Bone Motion Estimation
Using 2D optical flow warping to estimate bone motion trajectories rather than using predicted SE(3) transformations of each bone.

**Delta**: more reliable than SE(3)-based bone motion estimation during synchronous skeleton updates
**Condition**: Bone motion estimation during synchronous skeleton and parameter updates

**Evidence**: "the fluctuating SE(3) values may not be as reliable as the consistent 2D optical flow, which can be derived using existing models... for arbitrary views, the direction indicated by optical flow is sufficient, and the use of SE(3) becomes unnecessary."

## [NEGATIVE] SE(3)-Based Bone Motion Estimation
Using predicted 3D SE(3) transformations of each bone to determine bone motion direction, as used in WIM.

**Delta**: results were not as anticipated
**Condition**: Bone motion estimation when skeleton and parameters are updated synchronously

**Evidence**: "We experimented with using the estimated bone formation (SE(3)) for each bone as the basis for determining bone motion... However, our results were not as anticipated for two main reasons: (1) The SE(3) of bones are predicted, meaning the motion calculated for each part is only accurate when these predictions are highly stable and precise."

## [POSITIVE] Canonical Frame Selection via Horizontal-to-Vertical Ratio
Automatically selecting the canonical frame from a video by computing the skeleton's horizontal-to-vertical distance ratio and choosing the frame with the highest ratio, representing a standard side-view pose.

**Delta**: enables automatic canonical frame extraction without human annotation
**Condition**: Canonical frame selection for coarse model initialization

**Evidence**: "By computing the skeleton's horizontal-to-vertical distance ratio across all frames, the frame with the highest ratio is selected as the canonical frame."

## [POSITIVE] Skeleton Growing
Automatically extending the skeleton during the fine phase by identifying end parts and subdividing them when the maximum distance within an end part exceeds twice the initial value, to capture fine structures like limbs.

**Delta**: completes incomplete coarse skeleton by capturing extremity structures
**Condition**: Fine shape phase skeleton refinement

**Evidence**: "The coarse shape often fails to accurately reconstruct the fine structures at the extremities of an object, such as limbs, which mostly need to be built during the second phase. This results resulting in an incomplete coarse skeleton. To complete it during the second phase, we introduce the skeleton growth that automatically extends the skeleton based on the new extremity structures formed by the mesh."

## [POSITIVE] Physically Constrained Bone Merging
Merging bones that exhibit synchronized movements across all frames (cosine similarity threshold) and establishing joints between bones showing significant distance variations, to enforce physical plausibility.

**Delta**: enables controllable skeleton granularity while preserving critical bones
**Condition**: Physically constrained skeleton refinement in fine phase

**Evidence**: "by employing thresholds of 0.99, 0.95, and 0.90, we progressively reduce the granularity of the skeleton predictions, while still preserving the most critical bones and structural integrity."

## [POSITIVE] EM-Style Alternating Optimization
Alternating between E-step (fixing skeleton, updating shape and motion parameters) and M-step (adapting skeleton to current mesh using physical constraints), similar to Expectation-Maximization.

**Delta**: reduces interdependencies and errors compared to simultaneous learning
**Condition**: Motion and fine shape phase optimization

**Evidence**: "Conventional strategies typically learn all parameters simultaneously, leading to interdependencies where a single incorrect prediction can result in significant errors. In contrast, S3O adopts a phased approach... This method substantially lowers computational complexity and enhances robustness in reconstruction from limited viewpoints."

## [POSITIVE] Instance-Specific Mesh Initialization from 2D Skeleton
Initializing the mesh using 2D skeleton extraction and DINO features from the canonical frame, rather than using a generic sphere or ellipsoid initialization.

**Delta**: enables quicker learning of accurate camera parameters
**Condition**: Mesh initialization in coarse shape phase

**Evidence**: "we use the extraction of 2D skeletons from the canonical frame and DINO feature information to obtain an instance-specified initial mesh... this coarse mesh can greatly assist us in learning accurate camera parameters more quickly"

## [POSITIVE] Visibility Matrix for Optical Flow
Creating a visibility matrix via ray-casting to identify and disregard optical flow for occluded vertices when computing bone motion trajectories.

**Delta**: corrects inaccuracy from applying optical flow to occluded surface vertices
**Condition**: Bone motion estimation from optical flow

**Evidence**: "a visibility matrix V^t is created, reflecting the current mesh configuration and viewpoint at time t, determined via ray-casting. Optical flow for obscured vertices is thus disregarded."

## [POSITIVE] Even Resampling (2-Manifold Processing)
Periodically resampling mesh vertices every 1,500 iterations to maintain roughly uniform vertex distribution on the geometry surface during training.

**Delta**: prevents highly uneven vertex distribution during shape deformation
**Condition**: Fine shape phase during significant mesh deformations

**Evidence**: "only the outermost points on the camel's legs initially move downward, thereby elongating the entire leg... the distribution of vertices is highly uneven, with the lower half of the leg having very few points. Therefore, every 1,500 iterations, we perform an Evenly Resampling (2-Manifold Processing), which makes the vertices roughly uniformly distributed on the geometry surface."

## [POSITIVE] Gaussian Ellipsoid Skinning Weights
Modeling skinning weights as a mixture of B Gaussian ellipsoids, where each vertex's weight for a bone is determined by its Mahalanobis distance to the bone's Gaussian center.

**Delta**: enables physically meaningful bone-to-vertex assignment based on spatial proximity and orientation
**Condition**: Skinning weight computation for blend skinning

**Evidence**: "the skinning weights are modeled by the mixture of B Gaussian ellipsoids (semi-rigid parts)... In each Gaussian ellipsoid, C denotes Gaussian centers, V defines the orientation and Λ denotes the diagonal scale matrix."

## [NEGATIVE] Requiring Multiple Videos and Camera Poses (NeRF-based methods)
Methods like BANMo, RAC, CAMM requiring multiple videos from wide viewpoints and accurate camera calibration as input.

**Delta**: struggle to produce plausible outcomes from monocular short video
**Condition**: Single monocular video input scenario

**Evidence**: "existing NeRF-based (Neural Radiance Fields) approaches, often require a substantial number of input videos, acquired from a wide range of viewpoints and precise camera poses. Therefore, when the input is a monocular short video, these methods struggle to produce plausible outcomes."

## [NEGATIVE] Predefined Shape and Skeleton Templates
Using category-specific ground truth shape and skeleton templates as inputs for reconstruction methods.

**Delta**: limited generalizability to out-of-distribution objects
**Condition**: Out-of-distribution object reconstruction

**Evidence**: "model-based methods use pre-defined shape and skeleton templates to attain a physically plausible skeleton and bone distribution; however, they require these as category-specific ground truth inputs, instead of estimating them from the video. This diminishes their generalizability to out-of-distribution (OOD) objects."
