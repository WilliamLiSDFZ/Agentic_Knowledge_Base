# Enhancing Implicit Shape Generators Using Topological Regularizations

**Source**: https://proceedings.mlr.press/v235/chen24bk.html

## [POSITIVE] PD Generator (Point Cloud Generator for Persistent Diagrams)
A PointNet-based point cloud generator that synthesizes persistent diagrams (PDs) as 2D point clouds, used to provide smooth PD interpolations and regularize the implicit shape generator.

**Delta**: Wasserstein PD distribution distance reduced from 2.41 to 0.46 vs training shapes
**Condition**: When used to provide PD targets for implicit shape generator regularization on ShapeNet chair/table/sofa

**Evidence**: "if we measure the Wasserstein distance between the training shapes and 350 synthetic PDs learned from the PD generator. The resulting Wasserstein distance between them is 0.46, which is much smaller [than 2.41]."

## [POSITIVE] Rectification Layer for PD Validity
A non-linear layer R(x,y) = (x, x + RELU(y)) applied to PointNet output to enforce that all PD points satisfy x <= y, while allowing varying numbers of diagonal points.

**Delta**: enables valid PD generation with varying topology
**Condition**: Applied to PD generator output to enforce topological validity constraints

**Evidence**: "The RELU operation RELU(y) = max(0, y) ensures that all points (x, y) ∈ PD^{k,φ}(z) have x ≤ y. On the other hand, it allows that each PD^{k,φ}(z) has a varying number of points on the diagonal, a desired property for modeling shapes with varying topological features."

## [POSITIVE] PD Distribution Alignment Loss
A loss that aligns the PDs of each synthetic shape with the outputs of the PD generator, ensuring synthetic shape PDs match the learned PD distribution of training shapes.

**Delta**: PD-LAP improvement of ~71.3%/69.2% on chair/table over DeepSDF-VAD baseline
**Condition**: Applied during joint training of implicit shape generator and PD generator on ShapeNet

**Evidence**: "Quantitatively, on chair/table, Ours-DeepSDF outperforms DeepSDF-VAD by 14.4%/8.99% and 71.3%/69.2% in CD-mean and PD-LAP."

## [POSITIVE] PD Smoothness Loss on PD Generator
A regularization loss that penalizes differences between PD^{k,φ}(z) and PD^{k,φ}(z + εv) to enforce smooth PD interpolations across the latent space.

**Delta**: Removing it increases PD-LAP by 6.49%/4.55% and CD-mean by 7.32%/9.77% on chair/table
**Condition**: Applied to PD generator during joint training; addresses weak regularization when only PD alignment is used

**Evidence**: "We drop the PD smoothness loss to train the shape generator and the PD generator together. In this case, the PD-LAP and CD-mean scores increase by 6.49%/4.55% and 7.32%/9.77% on chair/table, respectively."

## [POSITIVE] Laplacian Regularization on SDF
A normal Laplacian smoothing regularization applied to each synthetic shape's SDF to stabilize PD optimization and avoid local minima, using the normal Laplacian from StEik.

**Delta**: analytically shown to be optimal choice for PD matching regularization
**Condition**: Applied per synthetic shape during PD optimization; uses normal Laplacian which has less effect on smoothing shape details than standard Laplacian

**Evidence**: "This result indicates that to address the degenerate issue of PD matching, Laplacian smoothing is the optimal choice."

## [POSITIVE] Two-Stage Training (Pre-training + Joint Training)
First pre-trains the implicit shape generator and PD generator separately, then jointly trains all components together to avoid the PD generator adversely fitting the implicit generator.

**Delta**: Removing PD pre-training increases PD-LAP by 85.71%/86.37% and CD-mean by 23.17%/16.54% on chair/table
**Condition**: Critical for training stability; without pre-training PD generators can adversely affect the implicit shape generator

**Evidence**: "We remove the data term that aligns the PD generators with the training shape PDs...the PD-LAP and CD-mean scores increase by 85.71%/86.37% and 23.17%/16.54% on chair/table, respectively. These numbers are even higher than those from dropping the PD smoothness term."

## [NEGATIVE] Lipschitz Regularization for SDF Smoothness (baseline)
Regularization that minimizes the Lipschitz constant of the SDF generator to enforce smooth interpolations, used in the Liu et al. 2022a baseline.

**Delta**: still introduces topological artifacts in interpolations
**Condition**: When used alone without explicit PD regularization; bound (6) is not tight so SDF smoothness does not guarantee PD smoothness

**Evidence**: "The generator is trained with the Lipschitz regularization loss introduced in (Liu et al., 2022a), which minimizes the right-hand side of (6). We can see that the interpolation introduces some unwanted topological artifacts."

## [POSITIVE] Topological Regularization on DeepSDF-SE (Ours-DeepSDF-SE)
Combining the proposed topological regularization with DeepSDF + StEik geometric regularization backbone.

**Delta**: 13.41%/15.79% improvement in CD-mean and 72.9%/70.9% improvement in PD-LAP on chair/table vs DeepSDF-SE-VAD
**Condition**: Applied on top of StEik geometric regularization; topological and geometric regularizations are complementary

**Evidence**: "When comparing Ours-DeepSDF-SE and DeepSDF-SE-VAD, we still see that Ours-DeepSDF-SE reduces the topological artifacts in DeepSDF-SE-VAD. Quantitatively, the relative improvements on chair/table are 13.41%/15.79% and 72.9%/70.9% in CD-mean and PD-LAP."

## [POSITIVE] StEik Geometric Regularization (DeepSDF-SE-VAD baseline)
State-of-the-art geometric regularization loss for neural implicit shape representations that suppresses small topological artifacts.

**Delta**: DeepSDF-SE-VAD outperforms DeepSDF-VAD in both PD-LAP and CD-mean
**Condition**: Applied as standalone geometric regularization without topological regularization; improvements are smaller than with topological regularization

**Evidence**: "DeepSDF-SE-VAD, due to the use of a novel geometric regularization loss, outperforms DeepSDF-VAD in both PD-LAP and CD-mean. The improvement in PD-LAP comes mainly from the fact that DeepSDF-SE-VAD suppresses many small topological artifacts in synthetic shapes."

## [NEUTRAL] Wasserstein Distance for PD Distribution Comparison (PD-LAP metric)
Using Wasserstein distance between PD distributions of synthetic and test shapes as an evaluation metric for topological generalization quality.

**Delta**: used as evaluation metric, not a training technique
**Condition**: Used as evaluation metric across all methods on ShapeNet chair, table, sofa

**Evidence**: "The second is PD-LAP, which uses Eq. 2 to measure the Wasserstein distance between PD distributions of synthetic shapes and PD distributions of test shapes. In other words, CD-mean evaluates geometric accuracy while PD-LAP quantifies topological generalization."

## [NEUTRAL] Latent Code KL Regularization (VAD)
Variational auto-decoder regularization that enforces the empirical distribution of latent codes to match a prior Normal distribution.

**Delta**: standard component of all evaluated methods
**Condition**: Applied as standard component in all model variants

**Evidence**: "The second term of (9) enforces that the empirical distribution of latent codes z_i agrees with the prior Normal distribution."

## [NEGATIVE] Removing PD Pre-training (ablation)
Training both the PD generator and implicit shape generator from scratch without pre-training the PD generator on training shape PDs.

**Delta**: PD-LAP increases by 85.71%/86.37%, CD-mean increases by 23.17%/16.54% on chair/table
**Condition**: Ablation of Ours-DeepSDF-SE; PD generators can adversely affect the implicit shape generator when trained from scratch

**Evidence**: "We remove the data term that aligns the PD generators with the training shape PDs. In this case, both the PD generator and the implicit shape generator are trained from scratch...the PD-LAP and CD-mean scores increase by 85.71%/86.37% and 23.17%/16.54% on chair/table, respectively."
