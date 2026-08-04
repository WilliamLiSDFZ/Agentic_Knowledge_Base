# Bringing Motion Taxonomies to Continuous Domains via GPLVM on Hyperbolic manifolds

**Source**: https://proceedings.mlr.press/v235/jaquier24a.html

## [POSITIVE] Hyperbolic Latent Space (GPHLVM)
Extending GPLVM to use a hyperbolic manifold as the latent space instead of Euclidean space, leveraging the exponential volume growth property of hyperbolic geometry to better embed hierarchical/tree-like data

**Delta**: lower stress values across all taxonomies in 2D; e.g., bimanual: 0.11±0.33 vs 0.13±0.33 (GPLVM) with stress prior
**Condition**: Taxonomies with tree-like hierarchical structure (bimanual manipulation, hand grasps); less pronounced for cyclic graph structures

**Evidence**: "All regularized GPHLVMs with 2-dimensional latent spaces outperform their Euclidean counterparts."

## [POSITIVE] Stress Prior / Graph-Distance Regularizer
Augmenting the GPHLVM loss with a stress loss that encourages geodesic distances in the latent space to match taxonomy graph distances, acting as a global structure-preserving regularizer

**Delta**: bimanual GPHLVM: stress reduced from 0.98±1.26 (no regularizer) to 0.11±0.33 (stress prior)
**Condition**: Applied to all taxonomy types; essential for meaningful distance structure in latent space

**Evidence**: "the models with stress prior result in embeddings that comply with the taxonomy graph structure: The embeddings are grouped and organized according to the taxonomy nodes, the geodesic distances match the graph ones"

## [POSITIVE] Back Constraints with Graph Kernel
Defining latent variables as a function of observations using a combined kernel that encodes both observation-space similarity and graph-distance relationships, ensuring local similarity preservation and enabling encoding of unseen data

**Delta**: bimanual GPHLVM BC+stress: 0.09±0.12 vs 0.11±0.33 (stress only)
**Condition**: Used in combination with stress prior; requires both observation kernel and graph kernel together

**Evidence**: "the GPHLVM with back constraints further organizes the embeddings inside a class according to the similarity between their observations"

## [NEGATIVE] No Regularization (Vanilla GPHLVM/GPLVM)
Training GPHLVM or GPLVM without any graph-distance priors or back constraints

**Delta**: bimanual GPHLVM no regularizer: 0.98±1.26 stress vs 0.11±0.33 with stress prior
**Condition**: All taxonomies tested

**Evidence**: "the models without regularization do not encode any meaningful distance structure in latent space"

## [POSITIVE] Hyperbolic Geometry for Tree-like Taxonomies
Using hyperbolic space specifically for taxonomies with tree-like (non-cyclic) graph structures, exploiting exponential volume growth

**Delta**: bimanual and hand grasps: hyperbolic 3D outperforms Euclidean 3D models
**Condition**: Taxonomies with tree-like hierarchical structure

**Evidence**: "the hyperbolic models of the bimanual manipulation and hand grasps taxonomies also outperform the Euclidean models with 3-dimensional latent spaces...the volume of balls in hyperbolic space increases exponentially with respect to the radius of the ball rather than polynomially as in Euclidean space"

## [NEUTRAL] Hyperbolic Geometry for Cyclic Graph Taxonomies
Applying hyperbolic latent space to taxonomies with cyclic graph structure (support pose taxonomy)

**Delta**: support poses 3D: GPLVM R3 stress 0.29±0.39 vs GPHLVM L3 0.35±0.45 (BC+stress); Euclidean slightly better in 3D
**Condition**: Cyclic graph structure taxonomies; hyperbolic still wins in 2D even for cyclic graphs

**Evidence**: "In the case of the support pose taxonomy, the Euclidean models with 3-dimensional latent space slightly outperform the 3-dimensional hyperbolic embeddings. We attribute this to the cyclic graph structure of the taxonomy."

## [POSITIVE] Higher Dimensional Latent Space (3D vs 2D)
Increasing the latent space dimensionality from 2 to 3 dimensions

**Delta**: bimanual GPLVM: stress 0.13±0.33 (R2) vs 0.01±0.01 (R3) with stress prior
**Condition**: All taxonomies and both Euclidean and hyperbolic models

**Evidence**: "we observe a prominent stress reduction for the Euclidean and hyperbolic 3-dimensional latent spaces compared to the 2-dimensional ones. This is due to the increase of volume available to match the graph structure in 3-dimensional spaces relative to 2-dimensional ones."

## [POSITIVE] Positive Semidefinite Hyperbolic Kernel Approximation
Monte Carlo approximation of the hyperbolic heat kernel using an inner product formulation in complex space C^L, guaranteeing positive semidefiniteness

**Delta**: guarantees positive semidefiniteness unlike naive truncated Gaussian MC approximation
**Condition**: Required for 2D hyperbolic latent space; computationally expensive (414.67s±30.87 training vs 2.978s±0.082 for Euclidean)

**Evidence**: "the righthand side of (6) is easily recognized to be an inner product in the space C^L, which implies its positive semidefiniteness"

## [POSITIVE] Riemannian Adam Optimization
Using Riemannian adaptive optimization (Riemannian Adam) to optimize parameters that lie on the hyperbolic manifold, respecting the manifold geometry during gradient updates

**Delta**: enables valid optimization on hyperbolic manifold
**Condition**: Required for all GPHLVM training; Lorentz model chosen over Poincaré for numerical stability

**Evidence**: "we used the Riemannian Adam (Becigneul & Ganea, 2019) implemented in Geoopt (Kochurov et al., 2020) to optimize the GPHLVM parameters"

## [POSITIVE] Lorentz Model over Poincaré Ball for Optimization
Choosing the Lorentz (hyperboloid) model representation for optimization while using Poincaré ball only for visualization

**Delta**: numerically more stable for Riemannian optimization
**Condition**: Model training and optimization phase

**Evidence**: "The latter representation is chosen here as it is numerically more stable than the former, and thus better suited for Riemannian optimization"

## [POSITIVE] Stress-Prior Initialization
Initializing GPHLVM embeddings by minimizing the stress loss before full model training

**Delta**: helps avoid local optima
**Condition**: All GPHLVM and GPLVM experiments

**Evidence**: "we initialize the embeddings of all GPLVMs by minimizing the stress associated with their taxonomy nodes, so that X = minX ℓstress...GPLVMs are generally prone to local optima during training, they benefit from a good initialization"

## [NEGATIVE] Distortion Loss as Graph Regularizer
Using a distortion loss (ratio of embedding distance to graph distance) instead of stress loss as the graph-distance regularizer

**Delta**: lackluster and numerically unstable results
**Condition**: Tested as alternative to stress loss; only defined for different classes (ci ≠ cj)

**Evidence**: "our empirical results using this loss were lackluster and numerically unstable (see App. F)"

## [POSITIVE] GPHLVM vs VAE-based Models
Comparing GPHLVM against vanilla and hyperbolic VAE baselines for taxonomy embedding

**Delta**: higher average stress and higher reconstruction error for VAEs compared to GPHLVMs (see Table 13)
**Condition**: All three taxonomies tested

**Evidence**: "the GPHLVM also outperformed vanilla and hyperbolic versions of a VAE to encode meaningful taxonomy information in the latent space...the embeddings of different taxonomy nodes are not as clearly separated as in the GPHLVMs. This is illustrated by the higher average stress of the VAEs' latent embeddings and their higher reconstruction error compared to the GPHLVMs'"

## [POSITIVE] Geodesic Trajectory Generation in Hyperbolic Latent Space
Generating motion trajectories by following geodesic paths between embeddings in the hyperbolic latent space

**Delta**: more realistic than linear interpolation in Euclidean GPLVM; competitive with VPoser
**Condition**: Low data regime; proof-of-concept trajectory generation between taxonomy poses

**Evidence**: "The obtained motions are more realistic than those obtained via linear interpolation in the GPLVM latent space and as realistic as those obtained via VPoser (Pavlakos et al., 2019)"

## [POSITIVE] Geodesic Paths Following Taxonomy Graph Transitions
Hyperbolic geodesics naturally following the shortest paths defined in the taxonomy graph, unlike Euclidean straight-line interpolation

**Delta**: Euclidean straight lines deviate from graph shortest paths, creating non-existent transitions
**Condition**: Trajectory generation between taxonomy embeddings

**Evidence**: "the geodesics in GPHLVMs latent space follow the transitions between classes defined in the taxonomy...Straight lines in the Euclidean embeddings are more likely to deviate from the graph shortest path, resulting in transitions that do not exist in the taxonomy"

## [NEGATIVE] 2D Hyperbolic Kernel Computational Cost
The Monte Carlo approximation of the 2D hyperbolic kernel requires many samples for accuracy, leading to significantly higher computational cost

**Delta**: training: 414.67s±30.87 (GPHLVM L2) vs 2.978s±0.082 (GPLVM R2); decoding: 2.74s±0.487 vs 6.256ms±0.314
**Condition**: 2D hyperbolic latent space only; 3D is much faster (6.887s±0.307 training)

**Evidence**: "The main computational burden arises in the GPHLVM with a 2-dimensional latent space...This increase in computational cost is mainly attributed to the 2-dimensional hyperbolic kernel"

## [POSITIVE] Combined Observation and Graph Kernel in Back Constraints
Using both an observation-space SE kernel and a graph Matérn kernel together in the back-constraint mapping, rather than either alone

**Delta**: using only graph kernel collapses observations to single point per node; using only observation kernel fails to separate dissimilar observations of same node
**Condition**: Back-constrained GPHLVM

**Evidence**: "Note that both kernels are required in (12): By defining the mapping as a function of the graph kernel only, the observations of each taxonomy node would be encoded by a single latent point. When using the observation kernel only, dissimilar observations of the same taxonomy node would be distant in the latent space"

## [POSITIVE] Hyperbolic Wrapped Gaussian Prior on Latent Space
Assigning a hyperbolic wrapped Gaussian distribution as prior on latent variables, centered at the origin of the hyperbolic manifold

**Delta**: enables probabilistic modeling respecting hyperbolic geometry
**Condition**: All GPHLVM variants

**Evidence**: "the latent variable x ∈ L^Q is assigned a hyperbolic wrapped Gaussian prior N_LQ(µ0, αI) based on (2), where µ0 is the origin of L^Q, and the parameter α controls the spread of the latent variables in L^Q"

## [POSITIVE] MAP Estimation for Small Datasets
Training GPHLVM via maximum a posteriori estimation for small datasets rather than variational inference

**Delta**: appropriate for low-data scenarios used in experiments
**Condition**: Small datasets (60-100 poses); variational inference available for larger datasets

**Evidence**: "Since our experiments deal with low-data scenarios, all models were trained via MAP estimation by maximizing the loss ℓ = ℓMAP − γℓstress"
