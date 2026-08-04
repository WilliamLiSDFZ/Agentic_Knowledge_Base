# Learning Scale-Aware Spatio-temporal Implicit Representation for Event-based Motion Deblurring

**Source**: https://proceedings.mlr.press/v235/yu24g.html

## [POSITIVE] Spatial Implicit Representation Module (SIRM)
Aggregates spatial correlation at any resolution through event encoding sampling, using spatial-aware encoding sampling and implicit MLP decoding to focus on highly blurred local areas at arbitrary spatial scales.

**Delta**: +0.82 dB PSNR
**Condition**: Ablation on GoPro dataset, compared to baseline without SIRM

**Evidence**: "SIRM and TIRM achieve average improvements of 0.82 dB and 2.12 dB in PSNR."

## [POSITIVE] Temporal Implicit Representation Module (TIRM)
Learns temporal correlation via temporal shift operations with long-term aggregation to tackle global motion blur of varying magnitudes at arbitrary temporal scales.

**Delta**: +2.12 dB PSNR
**Condition**: Ablation on GoPro dataset, compared to baseline without TIRM

**Evidence**: "SIRM and TIRM achieve average improvements of 0.82 dB and 2.12 dB in PSNR."

## [POSITIVE] Combined Spatio-Temporal Implicit Representation (SIRM + TIRM)
Full combination of both spatial and temporal implicit representation modules for scale-aware event-based motion deblurring.

**Delta**: +2.66 dB PSNR
**Condition**: Ablation on GoPro dataset, compared to baseline with neither module

**Evidence**: "the result of ID #4 indicates that our spatio-temporal implicit representation achieves an improvement in PSNR by 2.66 dB."

## [POSITIVE] Spatial-Aware Encoding Sampling (SAES)
Encodes event features and uses a querying coordinate grid to sample local features closest to eight points for 2D feature sampling, adaptively adjusting receptive field range according to input spatial scale.

**Delta**: +0.27 dB PSNR
**Condition**: Ablation on GoPro dataset within SIRM component analysis

**Evidence**: "With 'SAES', our method adaptively adjusts the receptive field range of the fusion network from events to images according to the input spatial scale Rs, which achieves a 0.27 dB improvement in terms of PSNR on the GoPro dataset."

## [POSITIVE] Implicit MLP Decoding in SIRM
Uses a two-layer MLP decoder to convert sampled spatial features into continuous feature representation, enabling arbitrary spatial scale generalization.

**Delta**: +0.37 dB PSNR (28.45 to 28.82)
**Condition**: Ablation on GoPro dataset, SIRM component analysis (implicit decoding contribution)

**Evidence**: "w/o SAES: 28.45/0.8712, w SAES: 28.82/0.8811"

## [POSITIVE] Time-Aware Event Selection (TAES)
Selectively modulates events based on input temporal scale using point-wise convolution to maintain temporal features within actual exposure time, enabling long-term bidirectional aggregation.

**Delta**: +0.44 dB PSNR
**Condition**: Ablation on GoPro dataset within TIRM component analysis

**Evidence**: "TAES and TGS improve performance by 0.44 dB and 0.81 dB respectively."

## [POSITIVE] Temporal Grouped Shift (TGS)
Divides selected features into m=4 groups along temporal dimension with different shift lengths and directions to implicitly learn correlations between event temporal and motion via large-range spatial shifts.

**Delta**: +0.81 dB PSNR
**Condition**: Ablation on GoPro dataset within TIRM component analysis

**Evidence**: "TAES and TGS improve performance by 0.44 dB and 0.81 dB respectively."

## [POSITIVE] SIRM vs. Transposed Convolution
Comparison of implicit spatial representation (SIRM) against explicit transposed convolution upsampling.

**Delta**: +0.70 dB PSNR (28.82 vs 28.12)
**Condition**: Spatial representation ablation on GoPro dataset

**Evidence**: "Transposed Conv: 28.12/0.8639 vs SIRM (Ours): 28.82/0.8811"

## [POSITIVE] SIRM vs. Pixel Shuffle
Comparison of implicit spatial representation (SIRM) against explicit pixel shuffle upsampling.

**Delta**: +0.39 dB PSNR (28.82 vs 28.43)
**Condition**: Spatial representation ablation on GoPro dataset

**Evidence**: "Pixel Shuffle: 28.43/0.8701 vs SIRM (Ours): 28.82/0.8811"

## [POSITIVE] SIRM vs. Learnable Upsample
Comparison of implicit spatial representation (SIRM) against learnable upsample, with SIRM achieving better performance at lower computational cost.

**Delta**: +0.21 dB PSNR with fewer parameters (+0.001M vs +0.227M)
**Condition**: Spatial representation ablation on GoPro dataset

**Evidence**: "Learnable Upsample: 28.61/0.8741, 1.688M(+0.227), 43.86G(+0.60) vs SIRM (Ours): 28.82/0.8811, 1.462M(+0.001), 43.35G(+0.09)"

## [POSITIVE] TIRM vs. VIT Self-Attention
Comparison of TIRM against VIT self-attention for temporal representation, achieving comparable performance at much lower computational cost.

**Delta**: comparable PSNR (28.82 vs 28.84) at 43.35G vs 77.83G FLOPs
**Condition**: Temporal representation ablation on GoPro dataset

**Evidence**: "TIRM requires only 2.96 GFLOPs to achieve performance equivalent to 37.44 GFLOPs of VIT, which is attributed to our straightforward group shift operation."

## [POSITIVE] TIRM vs. Deformable Convolution
Comparison of TIRM against deformable convolution for temporal representation.

**Delta**: +0.56 dB PSNR (28.82 vs 28.26)
**Condition**: Temporal representation ablation on GoPro dataset

**Evidence**: "Compared with lightweight deformable convolution, TIRM achieves a performance gain of 0.56 dB (from 28.26 to 28.82), benefiting from the large receptive field provided by the grouped shift operation."

## [POSITIVE] TIRM vs. Optical Flow
Comparison of TIRM against optical flow for temporal representation, with TIRM achieving better performance at lower computational cost.

**Delta**: +0.83 dB PSNR (28.82 vs 27.99) with fewer FLOPs (43.35G vs 51.30G)
**Condition**: Temporal representation ablation on GoPro dataset

**Evidence**: "Optical Flow: 27.99/0.8678, 1.5387M, 51.30G vs TIRM (Ours): 28.82/0.8811, 1.462M, 43.35G"

## [POSITIVE] Event Voxel Grid Bin Size
Number of temporal bins in the event voxel grid representation; larger bin sizes capture more temporal detail.

**Delta**: PSNR increases from 25.43 (8 bins) to 28.97 (32 bins)
**Condition**: GoPro dataset; bin size 16 used in final model matching EFNet setting

**Evidence**: "Table 7 shows the correlation between the size of the event voxel grid and performance. It can be observed that performance and bin sizes are directly proportional."

## [POSITIVE] Event-guided vs. Frame-only Deblurring
Using event streams alongside RGB images compared to frame-only deblurring methods.

**Delta**: +0.66 dB PSNR on GoPro, +1.29 dB on H2D
**Condition**: Comparison on GoPro and H2D datasets

**Evidence**: "our method with event data achieves PSNR improvements by 0.66 dB and 1.29 dB on GoPro and our H2D datasets, respectively, which indicates events are very useful in assisting RGB image deblurring."

## [POSITIVE] SASNet vs. SOTA Event-based Methods (GoPro)
Overall SASNet performance compared to best event-based competitors on GoPro dataset at Rs=4, Rt=1.

**Delta**: +0.74 dB PSNR over EFNet (28.82 vs 28.08)
**Condition**: GoPro dataset, Rs=4, Rt=1

**Evidence**: "Compared to the event-guided method, our approach consistently outperforms with an average improvement of 1.96 dB on the GoPro dataset and 2.5 dB on the H2D dataset."

## [POSITIVE] SASNet vs. SOTA Event-based Methods (H2D)
Overall SASNet performance compared to best event-based competitors on H2D dataset at Rs=2, Rt=1.

**Delta**: +1.13 dB PSNR over EFNet (35.72 vs 34.59)
**Condition**: H2D dataset, Rs=2, Rt=1

**Evidence**: "Compared to the event-guided method, our approach consistently outperforms with an average improvement of 1.96 dB on the GoPro dataset and 2.5 dB on the H2D dataset."

## [POSITIVE] SASNet robustness to increasing blur frames
Performance degradation of SASNet vs. competitors as blur severity increases (more averaged frames).

**Delta**: SASNet drops only 0.29 dB (frames 3 to 9) vs EFNet drops 0.73 dB
**Condition**: H2D dataset, varying blur frames (3, 6, 9)

**Evidence**: "SASNet only decreases by 0.29 dB (from 35.72 to 35.43), while EFNet decreases by 0.73 dB (from 34.59 to 33.86)."

## [NEUTRAL] Lightweight Reconstruction Module
Using simple convolutional layers for spatio-temporal reconstruction instead of heavier transformer-based modules.

**Delta**: 28.82/0.8811 PSNR/SSIM vs DAT 28.89/0.8813 at 43.35G vs 149.27G FLOPs
**Condition**: Reconstruction module comparison on GoPro dataset

**Evidence**: "although DAT achieves the best performance in terms of PSNR and SSIM, its computational cost is about three times that of ours (149.27 GFLOPs vs. 43.35 GFLOPs). Overall, the proposed spatial-temporal reconstruction module achieves comparable performance while significantly reducing the number of parameters and computations."

## [POSITIVE] SWA (Stochastic Weight Averaging) Training Strategy
Adopts SWA to update model parameters with an update interval of 10 to accelerate convergence and improve generalization across different spatial and temporal scales.

**Delta**: descriptive: more robust and achieving wider generalization
**Condition**: Training on GoPro and H2D datasets

**Evidence**: "to accelerate convergence, we adopt the SWA strategy to update model parameters with an update interval of 10, making the training more robust and achieving wider generalization at different spatial and temporal scales."

## [POSITIVE] L1 Loss Only
Using only L1 loss as the training objective without perceptual or adversarial losses.

**Delta**: outperforms baseline (best among compared methods)
**Condition**: Training on GoPro and H2D datasets

**Evidence**: "We use the Adam optimizer with an initial learning rate of 10^-4 that linear decays by 0.5 for every 30 epoch and only employ L1 loss as the training loss."

## [POSITIVE] H2D Dataset with Hybrid EVS/CIS Sensor
Real-world high-resolution dataset collected using a hybrid sensor with naturally spatially aligned and temporally synchronized events at 1920x1080 resolution, avoiding manual alignment artifacts.

**Delta**: descriptive: enables evaluation at various scales with natural calibration
**Condition**: Real-world dataset collection and evaluation

**Evidence**: "such a novel bio-inspired hybrid camera enables our H2D to be a competitive dataset with multiple characteristics: (i) high spatial resolution; (ii) natural calibrations in both spatial and temporal domains of images and events; (iii) real-world scenes with abundant diversities in scene category, light change, and movement speed."

## [POSITIVE] Out-of-distribution Scale Generalization
Single model trained on Rs in [1,2] and Rt in (0.5,1] generalizes to other scale ranges without retraining.

**Delta**: descriptive: maintains excellent performance across all scales with a single model
**Condition**: Out-of-distribution spatial and temporal scales on H2D dataset

**Evidence**: "Our model is trained on scale ranges of Rs∈[1,2], Rt∈(0.5,1], which can generalize to other scale ranges without being re-trained and fine-tuned, making it advantageous for practical applications."

## [POSITIVE] Channel Attention Block (CAB) in TIRM
CAB with kernel sizes equal to shift lengths is employed to integrate various shift groups, achieving large receptive field and long-term aggregation for global motion deblur.

**Delta**: descriptive: achieves large receptive field and long-term aggregation
**Condition**: Within TIRM for global motion deblurring

**Evidence**: "To seamlessly integrate various shift groups, a CAB is employed with kernel sizes equal to the shift lengths, which achieves a large receptive field and long-term aggregation for global motion deblur."

## [POSITIVE] Grouped Shift with m=4 groups and shifts {-7,-3,3,7}
Temporal grouped shift divides features into 4 groups with shift lengths of 7 and 3 pixels in both directions to enlarge receptive field for handling large-range motion blur.

**Delta**: descriptive: enables handling large range of motion blur
**Condition**: TIRM temporal grouped shift operation

**Evidence**: "In our implementation, we set m=4 and ∆xm,∆ym∈{−7,−3,3,7} to enlarge the receptive field of temporal information aggregation for handling a large range of motion blur."
