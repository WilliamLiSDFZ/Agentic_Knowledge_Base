# Proactive Detection of Voice Cloning with Localized Watermarking

**Source**: https://proceedings.mlr.press/v235/san-roman24a.html

## [POSITIVE] Generator/Detector Joint Training
Jointly trains a watermark generator (predicts additive watermark waveform) and a detector (outputs probability of watermark presence at each sample) end-to-end

**Delta**: average AUC 0.97 vs 0.84 for WavMark
**Condition**: Detection robustness across 15 audio editing operations

**Evidence**: "AudioSeal is overall more robust, with an average AUC of 0.97 vs. 0.84 for WavMark"

## [POSITIVE] Localized Watermark Detection (Sample-Level)
Detector outputs detection logits at every time step enabling sample-level localization, trained with watermark masking augmentation

**Delta**: IoU of 0.99 vs WavMark's 0.35 for 1-second watermarked segment
**Condition**: Localization of watermarked segments in 10-second audio clips

**Evidence**: "AudioSeal achieves an IoU of 0.99 when just one second of speech is AI-manipulated, compared to WavMark's 0.35"

## [POSITIVE] TF-Loudness Perceptual Loss
Novel time-frequency loudness loss based on auditory masking psychoacoustic principle; computes loudness difference between watermark and original signal in time-frequency windows using ITU-R BS.1770-4, with softmax weighting

**Delta**: PESQ 4.470 vs 4.302, ViSQOL 4.829 vs 4.730, MUSHRA 77.07 vs 71.52 compared to WavMark
**Condition**: Perceptual quality of watermarked audio

**Evidence**: "a novel perceptual loss inspired by auditory masking, that enables AudioSeal to achieve better imperceptibility"

## [POSITIVE] Masked Sample-Level Detection Loss (Localization Loss)
Binary cross-entropy loss computed at each time step between detector output and ground truth label (0 for non-watermarked, 1 for watermarked), enabling precise localization

**Delta**: IoU 0.99 vs WavMark 0.35 at 1-second watermark duration
**Condition**: Sample-level watermark localization

**Evidence**: "A localization loss ensures that the detection of watermarked audio is done at the level of individual samples. For each time step t, we compute the binary cross entropy (BCE) between the detector's output D(s)t and the ground truth label"

## [POSITIVE] Watermark Masking Augmentation
During training, randomly selects k starting points and alters segments by reverting to original audio (p=0.4), replacing with zeros (p=0.2), substituting with different audio (p=0.2), or no modification (p=0.2) to enable localized detection

**Delta**: Enables sample-level IoU of 0.99 vs WavMark's 0.35
**Condition**: Training for localized watermark detection

**Evidence**: "To enable sample-level localization, we adopt an augmentation strategy focused on watermark masking with silences and other original audios"

## [POSITIVE] Differentiable Audio Augmentations with Straight-Through Estimator
Applies differentiable audio editing augmentations (bandpass, echo, noise, etc.) during training; uses straight-through estimator for non-differentiable augmentations like MP3 compression to allow gradient backpropagation

**Delta**: Average AUC 0.97 across 15 augmentation types including MP3 (AUC 1.00) and AAC (AUC 1.00)
**Condition**: Robustness to real-life audio manipulations

**Evidence**: "We implemented these augmentations in a differentiable way when possible, and otherwise (e.g. MP3 compression) with the straight-through estimator (Yin et al., 2019) that allows the gradients to back-propagate to the generator"

## [POSITIVE] Augmentation Probability Proportional to Inverse Detection Accuracy
Sampling probability of each augmentation during training is proportional to the inverse of its evaluation detection accuracy, focusing training on harder augmentations

**Delta**: State-of-the-art average AUC 0.97 across diverse augmentations
**Condition**: Training robustness across diverse audio edits

**Evidence**: "the probability of sampling a given augmentation is proportional to the inverse of its evaluation detection accuracy"

## [POSITIVE] Single-Pass Detector Architecture
Detector runs once over the audio and yields detection logits at every time-step, eliminating need for sliding window synchronization search

**Delta**: Up to 485x faster detection than WavMark when no watermark present; two orders of magnitude faster on average
**Condition**: Detection speed, especially on non-watermarked content

**Evidence**: "AudioSeal outperforms WavMark with two orders of magnitude faster performance on average, notably 485x faster in scenarios where there is no watermark"

## [POSITIVE] EnCodec-Based Architecture
Generator and detector architectures derived from EnCodec's design with convolutional blocks, LSTM layers, and transposed convolutions

**Delta**: State-of-the-art robustness AUC 0.97 and 14x faster generation than WavMark
**Condition**: Overall system performance and efficiency

**Evidence**: "The architectures of the models are based on EnCodec (Défossez et al., 2022)"

## [POSITIVE] Multi-Bit Watermarking Extension
Adds message processing layer in generator middle and b linear layers at detector end to embed and decode b-bit binary messages for model attribution, decoupled from detection signal

**Delta**: Attribution accuracy 59.3% vs WavMark 56.6% at N=1000 models; higher FAR (8.96% vs 1.87%) but better overall accuracy
**Condition**: Multi-model attribution at FPR=10^-3

**Evidence**: "decoupling detection and attribution achieves better detection rate and makes the global accuracy better, at the cost of occasional false attributions"

## [POSITIVE] Detector Weight Confidentiality
Keeping detector weights private as a security measure against adversarial watermark removal attacks

**Delta**: White-box attack increases detection error by ~80% at high audio quality (PESQ>4); black-box attack requires significant audio quality degradation for similar effect
**Condition**: Security against adversarial watermark removal

**Evidence**: "The effectiveness of these attacks is limited as long as the detector remains confidential"

## [POSITIVE] Perceptual Quality Optimization over SI-SNR
Optimizing for perceptual quality metrics (PESQ, ViSQOL, MUSHRA) rather than SI-SNR, resulting in lower SI-SNR but better perceptual quality

**Delta**: MUSHRA 77.07 vs 71.52 for WavMark; PESQ 4.470 vs 4.302; SI-SNR 26.00 vs 38.25 (lower)
**Condition**: Perceptual audio quality evaluation

**Evidence**: "AudioSeal is not optimized for SI-SNR but rather for perceptual quality of speech. This is better captured by the other metrics (PESQ, STOI, ViSQOL), where AudioSeal consistently achieves better performance"

## [POSITIVE] Proactive Detection vs Passive Classification
Using watermark-based proactive detection instead of training binary classifiers to distinguish real from AI-generated audio

**Delta**: AudioSeal achieves TPR=1.0, FPR=0.0 on re-synthesized vs AI-generated; passive classifier drops to accuracy 0.704-0.907
**Condition**: Detection of re-synthesized audio (out-of-distribution for passive classifiers)

**Evidence**: "our proactive detection does not rely on model-specific artifacts but on the watermark presence. This allows for perfect detection over all the audio clips"

## [NEUTRAL] Gradient Balancing for Multiple Losses
Balances multiple training losses (l1, multi-scale mel spectrogram, adversarial, TF-loudness, localization, decoding) by scaling their gradients

**Delta**: Weights: λl1=0.1, λmsspec=2.0, λadv=4.0, λloud=10.0, λloc=10.0, λdec=1.0
**Condition**: Multi-objective training stability

**Evidence**: "We balance them during training by scaling their gradients as done by Défossez et al. (2022)"

## [NEGATIVE] Highpass Filter Robustness Weakness
AudioSeal embeds watermarks in frequency ranges affected by highpass filtering, leading to reduced robustness to this specific augmentation

**Delta**: AUC 0.61 for highpass filter vs WavMark's 1.00
**Condition**: Highpass filter audio editing attack

**Evidence**: "The performance for lowpass and highpass filters indicates that AudioSeal embeds watermarks neither in the low nor in the high frequencies (WavMark focuses on high frequencies)"

## [POSITIVE] Zero-Bit Watermarking Approach
Using zero-bit (detection only) watermarking as primary signal rather than multi-bit, reducing payload to minimum to maximize robustness

**Delta**: Average AUC 0.97 vs WavMark (multi-bit) 0.84
**Condition**: Detection robustness across audio manipulations

**Evidence**: "Our rationale is that robustness increases as the message payload is reduced to the bare minimum (Furon, 2007)"
