# Neural NeRF Compression

**Source**: https://proceedings.mlr.press/v235/pham24a.html

## [POSITIVE] Per-scene optimization (encoder-free)
Instead of training a compression model on a large dataset, the latent codes are directly optimized per scene without an encoder, jointly with a lightweight decoder and entropy model.

**Delta**: +12.03 dB PSNR vs pre-trained NTC
**Condition**: Synthetic-NeRF dataset, Lego scene ablation

**Evidence**: "Compared to per-scene training, pre-trained NTC suffers from inferior reconstruction quality. More specifically, the maximum PSNR that the pre-trained NTC can achieve is only 24.52 dB, which is 12.03 dB lower than the uncompressed PSNR value (36.55 dB) and also much lower than the PSNR values of per-scene trained models."

## [POSITIVE] Encoder removal (iterative inference)
The encoder is removed and latent codes are directly learned, avoiding the amortization gap that degrades compression performance when using an encoder.

**Delta**: outperforms baseline with encoder across rate-distortion curve
**Condition**: Per-scene TensoRF-VM compression, shown in Figure 5 top

**Evidence**: "using an encoder for amortized inference leads to an irreducible amortization gap in optimization (Cremer et al., 2018; Marino et al., 2018), which has been shown to degrade compression performance... we remove the encoder and directly learn the three latent codes"

## [POSITIVE] Importance-weighted rate-distortion loss
Weight maps derived from rendering importance scores (transmittance-weighted) are used to re-weight the feature plane reconstruction loss, guiding the model to focus on high-density grid locations.

**Delta**: -0.67 MB file size at same PSNR (4.59 MB to 3.92 MB at 32.98 dB)
**Condition**: ECTensoRF-L on Synthetic-NeRF dataset

**Evidence**: "At an identical PSNR of 32.98 dB, employing importance weight in training our model helps reduce the file size from 4.59 MB to 3.92 MB."

## [POSITIVE] Masked entropy model (spike-and-slab prior)
A binary masking mechanism is introduced into the entropy model using a spike-and-slab prior, selectively compressing only non-zero/informative feature grid locations and skipping background regions.

**Delta**: -0.34 MB file size vs factorized prior at 32.98 dB PSNR (4.26 MB to 3.92 MB)
**Condition**: ECTensoRF-L on Synthetic-NeRF, medium to high-rate regime

**Evidence**: "for a PSNR value of 32.98 dB, the compressed file with the factorized prior occupies 4.26 MB. In contrast, our method employing the proposed masked entropy model results in a reduced file size of 3.92 MB."

## [NEGATIVE] Masked entropy model in low-rate regime
The masked entropy model introduces overhead from transmitting the masks, causing slightly worse performance than the standard factorized prior at low bitrates.

**Delta**: slightly worse than factorized prior at low rates
**Condition**: ECTensoRF-L on Synthetic-NeRF, low-rate regime

**Evidence**: "due to the additional overhead introduced by sending the masks, our results lag slightly behind the factorized prior in a low-rate setting."

## [POSITIVE] Lightweight two-layer transposed CNN decoder with SELU
A two-layer transposed convolutional neural network with SELU activation is used as the decoder, providing an upsampling factor of 4x total (stride 2 per layer), balancing decoding capacity with transmission cost.

**Delta**: outperforms baseline
**Condition**: General architecture choice for per-scene NeRF compression

**Evidence**: "We found that a two-layer transposed convolutional neural network with SELU activation (Klambauer et al., 2017) is effective for our needs."

## [NEUTRAL] Zero initialization of latent codes
Latent codes are initialized as zero tensors rather than random Gaussian values, exploiting the sparsity of feature planes.

**Delta**: negligible difference vs Gaussian init (e.g., 32.98 dB / 3.92 MB vs 32.98 dB / 3.94 MB at lambda=2e-4)
**Condition**: ECTensoRF-L on Synthetic-NeRF across all lambda values

**Evidence**: "We compare the performance of Gaussian initialization and Zero initialization of the latents code... [Table 4 shows nearly identical results]"

## [POSITIVE] Two-stage training (pre-trained NeRF + compression)
Compression model is trained on top of a pre-trained TensoRF model rather than end-to-end from scratch.

**Delta**: +5.45 dB PSNR at lambda=2e-2 (31.31 vs 25.86 dB)
**Condition**: ECTensoRF-L on Synthetic-NeRF dataset

**Evidence**: "Table 5: Comparison of End-to-End Training vs. Two Stages Training [shows consistently higher PSNR for two-stage training across all lambda values]"

## [POSITIVE] Hyperprior model with masking
A hyperprior (Balle et al. 2018) is added on top of the masked entropy model, with masking applied to both hyper-latents and latents, and both optimized without amortized inference.

**Delta**: -0.29 MB at lambda=1e-4 (3.95 MB vs 4.24 MB at same 33.00 dB PSNR)
**Condition**: ECTensoRF-L on Synthetic-NeRF, high-rate regime

**Evidence**: "At higher bit rates, the compression performance with the hyperprior method is better than using only a single entropy model, which aligns with prior observations in image compression."

## [NEGATIVE] Hyperprior model at low bitrates
Adding a hyperprior incurs extra cost to transmit the hyper decoder and hyper entropy model, hurting performance at low bitrates.

**Delta**: +0.06 MB at lambda=2e-2 (1.92 MB vs 1.86 MB at same 31.31 dB PSNR)
**Condition**: ECTensoRF-L on Synthetic-NeRF, low-rate regime

**Evidence**: "At lower bit rates, the hyperprior is slightly worse than the ECTensoRF-L baseline because of the irreducible cost to transmit the hyper decoder and hyper entropy model."

## [POSITIVE] Gumbel-Softmax with annealing temperature for mask learning
Straight-through Gumbel-Softmax estimator with temperature annealing from 10 to 0.1 is used to learn binary masks in a differentiable manner.

**Delta**: enables end-to-end training of binary masks
**Condition**: Masked entropy model training

**Evidence**: "we turn to the Gumbel-Softmax trick (Jang et al., 2016; Yang et al., 2020) to facilitate the learning of M_i... In practice, we use an annealing softmax temperature τ that decays from 10 to 0.1 to calculate the softmax gradients."

## [NEUTRAL] Entropy coding masks under hyperprior
Entropy-coding the binary masks under a hyperprior p(M) was considered but found to provide little benefit.

**Delta**: little benefit
**Condition**: Masked entropy model design

**Evidence**: "We stress that we could also entropy-code the masks under a hyperprior p(M), but found little benefit to do so in practice."

## [POSITIVE] ECTensoRF-L vs VQ-TensoRF overall
The proposed ECTensoRF-L method outperforms VQ-TensoRF baseline across multiple datasets in rate-distortion performance.

**Delta**: BD-PSNR: +0.279 dB (Synthetic-NeRF), +0.289 dB (Synthetic-NSVF), +0.344 dB (Tanks&Temples); BD-Rate: -28.827%, -21.104%, -16.717%
**Condition**: Synthetic-NeRF, Synthetic-NSVF, Tanks and Temples datasets

**Evidence**: "Table 2: Relative improvement of our method versus VQ-TensoRF. BD-PSNR and BD-rate measure the average difference in PSNR and bitrate between the two methods."

## [POSITIVE] Latent code spatial downsampling (4x)
Latent codes are initialized at 1/4 the spatial resolution of the feature planes (Wi/4 x Hi/4), with the decoder upsampling back via two stride-2 transposed conv layers.

**Delta**: enables compression while maintaining quality
**Condition**: Both ECTensoRF-H and ECTensoRF-L configurations

**Evidence**: "Given a feature plane sized Ci × Wi × Hi, we initialize the corresponding latent code Z_i to have the size of CZi × Wi/4 × Hi/4."
