# Parallelized Spatiotemporal Slot Binding for Videos

**Source**: https://proceedings.mlr.press/v235/singh24g.html

## [POSITIVE] Parallelizable Spatiotemporal Binder (PSB)
A temporally-parallelizable slot learning architecture that produces object-centric slot representations for all time-steps in parallel using causal attention, replacing RNN-based sequential processing.

**Delta**: 1.6x faster training speed; 14.7-26.8% improvement in FG-ARI; 2.9-7.6% improvement in reconstruction PSNR for 2D videos; 7.3-121% improvement in slot linear-probing for 3D scenes; 4-8% improvement in PSNR for novel view synthesis
**Condition**: 2D unposed videos and dynamic 3D posed multi-camera videos

**Evidence**: "our architecture demonstrates stable training on longer sequences, achieves parallelization that results in a 60% increase in training speed, and yields performance that is on par with or better on unsupervised 2D and 3D object-centric scene decomposition and understanding"

## [NEUTRAL] Causal Masking in Attention
Optional causal masking applied to cross-attention and self-attention to prevent slots from accessing future time-step inputs, enabling use as a perception module in agent-learning settings.

**Delta**: None
**Condition**: Agent-learning settings requiring causal processing

**Evidence**: "we provide an option to apply causal masking to prevent the slots from seeing the inputs of the future time-steps. This makes our model useful as a perception module in agent-learning settings where the agent typically does not have access to future observations."

## [POSITIVE] Inverted Attention and Renormalization
Replaces standard dot-product attention with inverted attention and renormalization in the bottom-up attention step to introduce competition among slots and help them specialize to distinct objects.

**Delta**: worse FG-ARI without it
**Condition**: Bottom-up cross-attention step in PSB block for 2D video segmentation

**Evidence**: "Without inverted attention, we find that the video decomposition performance as measured by FG-ARI becomes worse, suggesting that inverted attention is a beneficial inductive bias to keep."

## [POSITIVE] Relative Positional Bias
Uses relative positional bias instead of absolute positional embeddings to incorporate temporal position information, providing invariance to translation-in-time and enabling generalization to arbitrary sequence lengths.

**Delta**: None
**Condition**: Temporal attention in PSB block

**Evidence**: "to incorporate invariance to translation-in-time and to help the encoder generalize to any sequence length, we recommend using relative positional bias (Raffel et al., 2020) instead of absolute positional embedding (Vaswani et al., 2017) to incorporate the temporal position information in the attention process."

## [POSITIVE] Decoupled Time-Axis and Object-Axis Self-Attention
Separates slot self-attention into two steps: time-axis self-attention (same-index slots across time) and object-axis self-attention (all slots at same time-step), instead of a single joint self-attention over all NT slots.

**Delta**: reduces memory from O(N^2 T^2) to O(NT^2) + O(N^2 T)
**Condition**: Slot interaction step in PSB block; benefit is primarily in memory/scalability rather than raw performance

**Evidence**: "In terms of performance alone, we do not notice a clear advantage of either version. However, it is also important to acknowledge the memory complexity: the joint interaction version requires O(N^2 T^2) memory which can be costlier and hurt scalability compared to using the decoupled version which requires a lower O(NT^2) + O(N^2 T) memory."

## [POSITIVE] Learned Parameter Slot Initialization
Initializes slots as fixed learned parameters rather than randomly sampling from a learned Gaussian distribution.

**Delta**: generally better performance than random initialization
**Condition**: Slot initialization in PSB for both 2D and 3D settings

**Evidence**: "we evaluate the impact of initializing slots by randomly sampling them from a learned Gaussian. In this variant, we note a generally worse performance compared to initializing slots as learned parameters."

## [NEGATIVE] Random Slot Initialization from Learned Gaussian
Initializes slots by sampling from a learned Gaussian distribution instead of using fixed learned parameters.

**Delta**: generally worse performance
**Condition**: Slot initialization in PSB

**Evidence**: "we evaluate the impact of initializing slots by randomly sampling them from a learned Gaussian. In this variant, we note a generally worse performance compared to initializing slots as learned parameters."

## [POSITIVE] Static-Dynamic Field Decoupling in NeRF Decoder
Incorporates a static field and a sky field in the NeRF decoder to decouple static field modeling from dynamic field modeling.

**Delta**: improved linear-probing and unsupervised segmentation; more marked improvement on CLEVR-Natural-Ego
**Condition**: NeRF decoder for dynamic 3D scenes, especially visually complex egocentric datasets

**Evidence**: "We find that static-dynamic decoupling improves performance both in terms of representation quality as suggested by the linear-probing result as well as in terms of unsupervised segmentation. The improvement is more marked in the visually complex and egocentric CLEVR-Natural-Ego dataset."

## [POSITIVE] Autoregressive Image-Transformer Decoder
Uses an autoregressive transformer decoder trained with cross-entropy loss on DVAE representations for visually complex video datasets, paired with the PSB encoder.

**Delta**: competitive or slightly worse FG-ARI vs STEVE baseline but with better efficiency
**Condition**: Visually complex datasets (MOVi-C, D, E)

**Evidence**: "we find that while our segmentation performance is slightly worse, the difference is not substantial. Therefore, in scenarios where training efficiency and stability are prioritized, our proposed encoder with powerful decoders remains a preferred option."

## [NEGATIVE] RNN-based Sequential Slot Binding (baseline)
Conventional recurrent approach (SAVi) that sequentially updates slots through iteration over the input sequence, used as the comparison baseline.

**Delta**: training instability on longer sequences; linear time complexity in sequence length; 1.6x slower than PSB
**Condition**: Longer sequences (T=12 vs T=6); general sequential object-centric learning

**Evidence**: "RNNs lead to major scaling issues—training instability on longer sequences due to gradient vanishing or exploding leads to degenerated performance and an increased training time complexity linear in sequence length"

## [POSITIVE] Sliding Window Approach for Length Generalization
Applies the model trained on short sequences (length 6) to longer sequences by using a sliding window of the most recent 6 frames.

**Delta**: None
**Condition**: Inference on sequences longer than training length (lengths 12, 18, 24 when trained on length 6)

**Evidence**: "For our model, we use a sliding-window approach to apply the model on longer sequence i.e., the slots of each time-step are inferred from the sequence of most recent 6 frames."

## [NEUTRAL] Set Latent Scene Representation (SLSR) Backbone
Encodes multiple camera views per time-step using a CNN followed by a transformer to produce a set latent scene representation before passing to PSB.

**Delta**: None
**Condition**: 3D posed multi-camera video setting; used identically across all compared models for fair comparison

**Evidence**: "we adopt the backbone of Sajjadi et al. (2022). For each time-step, we feed the K' (out of K) visible views to a CNN to obtain a feature map... The transformer's output is known as Set Latent Scene Representation or SLSR"

## [POSITIVE] Residual Connections in PSB Block
All operations in the PSB block are performed through residual connections to enable deep stacking of PSB blocks.

**Delta**: None
**Condition**: Deep PSB architectures with multiple stacked blocks

**Evidence**: "Note that all operations described above are performed through residual connections, making the PSB block suitable for deep stacking (He et al., 2016)."

## [NEGATIVE] Quadratic Memory Complexity from Attention
Replacing RNNs with attention mechanisms introduces quadratic memory complexity with respect to sequence length.

**Delta**: None
**Condition**: Very long sequences; a known limitation of the transformer-based approach

**Evidence**: "while our proposed design replaces RNNs with attention, thus providing the benefit of speed and parallelization, it also incurs a quadratic memory complexity in terms of sequence length."
