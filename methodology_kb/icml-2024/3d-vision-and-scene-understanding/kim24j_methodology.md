# Synergistic Integration of Coordinate Network and Tensorial Feature for Improving Neural Radiance Fields from Sparse Inputs

**Source**: https://proceedings.mlr.press/v235/kim24j.html

## [POSITIVE] Synergistic Integration of Coordinate Network and Multi-Plane Representation
Combining coordinate-based MLP networks (for low-frequency bias) with multi-plane tensorial features (for high-frequency fine-grained details) in a single framework, where each component handles a distinct spectral range.

**Delta**: +1.10 PSNR over HexPlane at 25 poses (25.34 vs 24.15); +24.56 avg PSNR vs 24.24 for K-Planes in static NeRF
**Condition**: Sparse input static and dynamic NeRF tasks

**Evidence**: "The proposed method outperforms every setting of HexPlane in all metrics in the D-NeRFs... our proposed method not only outperforms baseline models for both static and dynamic NeRFs with sparse inputs, but also achieves comparable results with fewer parameters."

## [POSITIVE] Residual Concatenation of Coordinates and Multi-Plane Features
Residual concatenation of coordinate values and multi-plane features across the first two hidden layer blocks, using ReLU activation to maintain low-frequency spectral bias from coordinate networks without interference from multi-plane features.

**Delta**: +5.97 avg PSNR vs Type 1 (skip at every layer): 24.74 vs 18.77; +5.51 vs Type 2 (no skip): 24.74 vs 19.23
**Condition**: Static NeRF with 8 views; ablation study comparing residual connection variants

**Evidence**: "We observe that the straightforward implementation of residual connection leads to ineffective training for sparse inputs. However, the proposed method gains remarkable performance gap than others, highlighting the necessity of careful design for handling two heterogeneous features."

## [NEGATIVE] Skip Connection at Every Layer (Type 1)
A residual connection design where skip connections are placed at every MLP layer, as opposed to only the first two blocks.

**Delta**: -5.97 avg PSNR vs proposed method: 18.77 vs 24.74
**Condition**: Static NeRF with 8 views; ablation study

**Evidence**: "We observe that the straightforward implementation of residual connection leads to ineffective training for sparse inputs."

## [NEGATIVE] No Skip Connection (Type 2)
Architecture variant with no residual/skip connections between coordinate and multi-plane features.

**Delta**: -5.51 avg PSNR vs proposed method: 19.23 vs 24.74
**Condition**: Static NeRF with 8 views; ablation study

**Evidence**: "The quantitative result is presented in Table 4. We observe that the straightforward implementation of residual connection leads to ineffective training for sparse inputs."

## [NEGATIVE] Coordinate-Only Residual Concatenation (Type 3)
Architecture variant where only the coordinate value is residually concatenated, without multi-plane features in the residual path.

**Delta**: -5.67 avg PSNR vs proposed method: 19.07 vs 24.74
**Condition**: Static NeRF with 8 views; ablation study

**Evidence**: "Table 4: Performance evaluation by varying residual connection candidates on the static NeRF dataset with 8 views... Type 3: 19.07 PSNR"

## [POSITIVE] Curriculum Weighting for Multi-Plane Encoding (Progressive Training)
A channel-wise weighting strategy that gradually increases the engagement of multi-plane feature channels over training iterations, training the coordinate network first and then progressively enabling multi-plane channels to prevent all channels from converging to similar patterns.

**Delta**: +0.2 to +0.4 avg PSNR in static NeRF; +0.6 avg PSNR in standup dynamic NeRF; variance reduction of 2.8 in Mic scene
**Condition**: Challenging scenes with heavy occlusion or rapid motion (e.g., drums, standup); sparse input static and dynamic NeRF

**Evidence**: "In static NeRFs, we observe that CL consistently has a positive impact on performance improvement to Average PSNR, despite the fact that their improvement on reconstruction is minor, ranging from 0.2 to 0.4 in all cases... The effectiveness of progressive training is more pronounced in dynamic NeRFs... it evidently enhances performance in the standup case, leading to 0.6 increase in average PSNR."

## [POSITIVE] ReLU Activation in Coordinate Network
Using ReLU activation in the coordinate-based MLP to enforce low-frequency spectral bias, as opposed to sinusoidal activations.

**Delta**: outperforms baseline
**Condition**: Coordinate network component of the proposed architecture

**Evidence**: "We employ ReLU activation h to lean toward low-frequency spectral bias."

## [NEGATIVE] Laplacian Smoothing Regularization on Multi-Plane Features
Denoising regularization applied to multi-plane features to constrain similarity among adjacent features and remove floating artifacts.

**Delta**: TensoRF fails to converge when λ1 > 0.01; can introduce undesirable color disturbances
**Condition**: Baseline models (TensoRF, K-Planes, HexPlane) with high regularization weights; less problematic for proposed method

**Evidence**: "While increasing the value of λ1 allows the removal of floating artifacts by over-smoothing the multi-plane features, it creates undesirable deformation that looks authentic but is not present in the training data. In addition, too high a value for λ1 can increase learning instability due to excessive penalization."

## [POSITIVE] L1 Norm Regularization on Multi-Plane Features
L1 sparsity regularization applied to each plane feature to encourage sparse multi-plane representations.

**Delta**: part of overall loss contributing to outperforming baselines
**Condition**: Applied to both static and dynamic NeRF training

**Evidence**: "Additionally, we regularize each plane feature using the L1 norm for the sparsity of multi-plane features."

## [POSITIVE] Reduced Parameter Count via Coordinate Network Replacement of Low-Resolution Grid
Replacing the low-resolution spatial grid in multi-plane representations with coordinate-based features, reducing total parameter count while maintaining performance.

**Delta**: 1.0M parameter model (Ours-12) achieves 25.10 PSNR, surpassing full-parameter baselines like HexPlane(72) at 24.00 PSNR with 9.7M params
**Condition**: Dynamic NeRF with 25 poses; parameter efficiency experiments

**Evidence**: "The reduced model with only 1.0M parameters surpasses the other full parameterized baselines. This achievement is attributed to the disentanglement of two heterogeneous representations, as redundant multi-plane for low-resolution features are replaced with the coordinate network."

## [NEGATIVE] Multi-Plane Representation Alone (without Coordinate Network)
Using only multi-plane (tensorial) representations such as TensoRF, HexPlane, or K-Planes without integration of coordinate-based MLP for low-frequency handling.

**Delta**: HexPlane: 24.15 PSNR at 25 poses vs proposed 25.34; K-Planes: 22.68 vs 25.34
**Condition**: Sparse input NeRF, especially dynamic scenes

**Evidence**: "The recent works found those representations struggle with low-frequency detail and overfit to high-frequency signals, especially when applying for dynamic scenes, despite using multi-scale representations... HexPlane discretizes the continuous time axis into finite bins, making it less responsive to the time-variant motion of objects when the available training poses are sparse."

## [NEGATIVE] Sinusoidal Encoding-Based NeRF (e.g., FreeNeRF)
Using sinusoidal positional encoding with MLP networks for NeRF, progressively adjusting frequency spectrum to counteract overfitting.

**Delta**: FreeNeRF avg PSNR 23.40 vs proposed 24.56 in static NeRF; blurry details observed qualitatively
**Condition**: Static NeRF with 8 views; high-resolution structure scenes

**Evidence**: "Sinusoidal encoding-based networks fail to capture high-frequency details and are prone to underfit in data with high-resolution structures... FreeNeRF exhibits blurry details."

## [NEGATIVE] Coordinate-Based MLP Without Precise Integration with Explicit Features
Using coordinate-based MLP combined with grid/plane features without careful architectural design (e.g., CAM approach with sinusoidal embeddings).

**Delta**: CAM struggles to capture low-frequency details in image regression experiments
**Condition**: Image regression and sparse NeRF tasks

**Evidence**: "Surprisingly, CAM, despite incorporating various spectral sinusoidal embeddings, also struggles to capture low frequency details. This implies explicit representation such as grid or plane cannot effectively handle low frequency details without careful designs."

## [POSITIVE] Stability via Low Variance Across Test Viewpoints
The proposed method achieves lower PSNR variance across test viewpoints compared to explicit parameterization baselines, indicating less overfitting to training views.

**Delta**: Variance 18.23 vs iNGP 23.95, TensoRF 23.22, K-Planes 19.61; comparable to FreeNeRF 17.31
**Condition**: Static NeRF dataset with 8 views; 8000 test images across 8 scenes

**Evidence**: "Quantitatively, our method achieves comparable results to FreeNeRF. However, as shown in Table 3, FreeNeRF generally lacks reconstruction performance... our method consistently reconstructs all scenes with high quality, avoiding significant degradation."
