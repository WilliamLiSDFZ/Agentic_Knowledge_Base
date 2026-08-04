# HyperFields: Towards Zero-Shot Generation of NeRFs from Text

**Source**: https://proceedings.mlr.press/v235/babu24a.html

## [POSITIVE] Dynamic Hypernetwork
A hypernetwork architecture where each MLP module predicts NeRF weights conditioned on both a text conditioning token and the activations from the previous NeRF MLP layer, enabling weights to change dynamically based on layer-wise signals.

**Delta**: prevents collapse of scene attributes; essential for fitting 100+ scenes
**Condition**: Multi-scene packing; required for expressivity when fitting many distinct scenes

**Evidence**: "Row 2 shows that even in the simple case of 4 scenes the static hypernetwork collapses the 'glacier' and 'origami' styles, and the 'plaid' and 'stained glass' styles."

## [POSITIVE] NeRF Distillation Training
A two-stage training framework where individual teacher NeRFs are first trained using SDS, then the hypernetwork is trained with a photometric loss against teacher NeRF renders, replacing direct SDS training of the hypernetwork.

**Delta**: enables scaling to 100 scenes without quality degradation; prevents mode collapse in geometry
**Condition**: Multi-scene hypernetwork training; critical for scene quality and scale

**Evidence**: "The iterative optimization of score distillation causes mode collapse in geometry. See Fig. 10 for an example of this mode collapse."

## [NEGATIVE] Score Distillation Sampling (SDS) for Hypernetwork Training
Directly using SDS loss from DreamFusion to train the hypernetwork to pack multiple scenes, without teacher NeRF distillation.

**Delta**: causes mode collapse in geometry across scenes
**Condition**: When used as the sole training signal for multi-scene hypernetwork packing

**Evidence**: "If we attempt to pack the dynamic hypernetwork using just Score Distillation Sampling (SDS) from DreamFusion, we experience a type of mode collapse in which the SDS optimization guides similar shapes towards the same common geometry."

## [POSITIVE] Stop Gradients on Activations
Applying stop gradient operators on the NeRF activations before passing them into the MLP modules of the dynamic hypernetwork to stabilize training.

**Delta**: stabilizes training (qualitative)
**Condition**: Dynamic hypernetwork training

**Evidence**: "We include stop gradients (SG) to stabilize training."

## [POSITIVE] Adaptive Instance Normalization on Activations
Performing adaptive instance normalization on NeRF activations before passing them into the MLP modules of the dynamic hypernetwork.

**Delta**: contributes to stable training (qualitative)
**Condition**: Dynamic hypernetwork training

**Evidence**: "Furthermore, we perform adaptive instance normalization before passing the activations into the MLP modules of the dynamic hypernetwork and also put a stop gradient operator on the activations being passed into the MLP modules."

## [NEUTRAL] Frozen BERT Text Encoder
Using a frozen pretrained BERT model to encode text prompts into embeddings for conditioning the hypernetwork.

**Delta**: similar but marginally worse than alternatives like T5 and CLIP
**Condition**: Text encoding for hypernetwork conditioning

**Evidence**: "We condition our model with BERT tokens, though we experiment with T5 and CLIP embeddings as well with similar but marginally worse success."

## [POSITIVE] Multiresolution Hash Grid (InstantNGP)
Using the multiresolution hash grid from InstantNGP for fast inference with low memory overhead as the positional encoding for the NeRF.

**Delta**: fast inference with low memory overhead (qualitative)
**Condition**: NeRF architecture within HyperFields

**Evidence**: "We use the multiresolution hash grid developed in InstantNGP Muller et al. (2022) for its fast inference with low memory overhead."

## [POSITIVE] Sinusoidal Positional Encodings
Using sinusoidal encodings to combat the known spectral bias of neural networks in the NeRF MLP.

**Delta**: combats spectral bias (qualitative)
**Condition**: NeRF MLP architecture

**Evidence**: "sinusoidal encodings γ to combat the known spectral bias of neural networks (Rahaman et al., 2018)."

## [POSITIVE] Skip Connections in NeRF MLP
Adding skip connections every two layers in the 6-layer NeRF MLP.

**Delta**: standard architectural improvement (qualitative)
**Condition**: NeRF MLP architecture

**Evidence**: "The NeRF MLP has 6 layers (with weights predicted by the dynamic hypernetwork), with skip connections every two layers."

## [POSITIVE] Transformer Module for Text Conditioning
A 6-layer self-attention Transformer with 12 heads processes BERT text embeddings to produce a conditioning token used by all hypernetwork MLP modules.

**Delta**: enables semantically meaningful mapping from text to NeRF weights (qualitative)
**Condition**: Text-to-NeRF mapping in hypernetwork

**Evidence**: "The text is then encoded by a frozen pretrained BERT model, and the text embedding z is processed by T. Let conditioning token CT = T(z) be the intermediate representation used to provide the current scene information to the MLP modules."

## [POSITIVE] Minibatch Activation Averaging for Dynamic Conditioning
During training with non-trivial minibatch sizes, activations are averaged over the minibatch index to produce a single representative activation vector for weight generation.

**Delta**: enables practical training while maintaining adaptive weight generation (qualitative)
**Condition**: Training with minibatch size > 1

**Evidence**: "In order to generate a unique set of weights for a given minibatch we do the following: Where µ(.) averages over the minibatch index. This adaptive nature of the predicted NeRF MLP weights leads to the increased flexibility of the model."

## [POSITIVE] HyperNet Latent Space Interpolation
Interpolating in the hypernetwork's learned latent space rather than in the BERT token input space.

**Delta**: smoother interpolation than BERT token interpolation
**Condition**: Scene interpolation experiments

**Evidence**: "our HyperNet token interpolation shown in Figure 10 demonstrates a smooth and gradual transition of colors across the interpolation range. This demonstrates that our HyperNet learns a smoother latent space of NeRFs than the original BERT tokens correspond to."

## [NEGATIVE] BERT Token Input Interpolation
Interpolating directly in the BERT token embedding space to generate intermediate scenes.

**Delta**: non-smooth interpolation with discontinuities
**Condition**: Scene interpolation in input embedding space

**Evidence**: "The interpolation is highly non-smooth, with a single intermediate color shown at δ = 0.4 and discontinuities on either end at δ − 0.3 and δ = 0.5."

## [POSITIVE] Plug-and-Play Teacher NeRF Compatibility
NeRF distillation is agnostic to the choice of text-to-3D teacher model, allowing HyperFields to inherit quality from the latest generative models like ProlificDreamer.

**Delta**: higher visual quality and complexity than ATT3D; no quality degradation when distilling ProlificDreamer scenes
**Condition**: When using high-quality teacher models such as ProlificDreamer

**Evidence**: "NeRF distillation is agnostic to the choice of text-to-3D model, so that HyperFields can learn high-quality and complex scenes from the latest generative model in a plug-and-play fashion. Our model generates the distilled scenes with virtually no quality degradation."

## [POSITIVE] Fine-tuning with SDS for Out-of-Distribution Scenes
After hypernetwork pretraining, fine-tuning HyperFields on SDS loss for out-of-distribution prompts to achieve accelerated convergence compared to training from scratch.

**Delta**: 5x to 10x faster convergence than DreamFusion baselines
**Condition**: Out-of-distribution scene generation requiring unseen shapes or attributes

**Evidence**: "Finetuning HyperFields benefits from accelerated convergence thanks to the learned general map, and is capable of synthesizing novel scenes 5 to 10 times faster than existing neural optimization-based methods."

## [POSITIVE] Zero-Shot In-Distribution Generation
Single forward pass generation of novel scenes whose component attributes (e.g., shape and color) were seen during training but whose specific combination was not.

**Delta**: Top-1 CLIP retrieval 57.1% unseen vs 69.5% seen; Top-10 retrieval 95.2% unseen vs 96.6% seen
**Condition**: In-distribution generalization where component attributes are seen but combinations are novel

**Evidence**: "We achieve similar scores between the seen and unseen prompts, indicating that our zero-shot generations are of similar quality to the training scenes."
