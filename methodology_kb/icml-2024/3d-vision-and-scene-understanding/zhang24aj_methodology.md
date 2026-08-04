# Multi-Factor Adaptive Vision Selection for Egocentric Video Question Answering

**Source**: https://proceedings.mlr.press/v235/zhang24aj.html

## [POSITIVE] Patch Partition and Merging Module (PPM)
Extends TimeSformer with multi-scale processing by splitting video frames into patches and sub-patches, using dual spatial embeddings (sub-spatial and spatial) and a twin spatial-temporal attention structure with down-sampling/up-sampling to integrate multi-scale visual cues for small object recognition.

**Delta**: +0.69% overall accuracy on EgoTaskQA indirect split (when removed, accuracy drops by 0.69%)
**Condition**: EgoTaskQA indirect split ablation study

**Evidence**: "when the patch partition and merging module is removed and replaced by a combination of RoBERTa and the original TimeSformer, there is a 0.69% decrease in overall accuracy"

## [POSITIVE] Prior-guided Patch Selection Module (PS)
Synthesizes a pre-defined prior matrix (based on egocentric gaze habits centered on hand-object interaction zones) with spatial and temporal attention scores to dynamically select the top-k most important sub-patches per frame, suppressing noise and redundancy.

**Delta**: +1.45% overall accuracy on EgoTaskQA indirect split (when removed, accuracy drops by 1.45%)
**Condition**: EgoTaskQA indirect split ablation study; most impactful single component

**Evidence**: "the omission of the prior-guided patch selection module results in a more substantial drop of 1.45% in accuracy"

## [POSITIVE] Hierarchical Aggregation Network (HA)
Multi-layer spatial-temporal cross-attention network that progressively aggregates video semantics from sub-patch to patch to frame to video level, guided by question representations, with down-sampling in the final three layers.

**Delta**: +0.88% overall accuracy on EgoTaskQA indirect split (when replaced with standard cross-attention, accuracy drops by 0.88%)
**Condition**: EgoTaskQA indirect split ablation study

**Evidence**: "replacing the hierarchical aggregation network with a standard cross-attention network leads to a decrease of 0.88% in accuracy"

## [POSITIVE] Full MFAS Framework
Combined framework integrating PPM, prior-guided patch selection, and hierarchical aggregation network for egocentric VideoQA.

**Delta**: +2.43% on EgoTaskQA direct All metric; +3.12% on EgoTaskQA indirect All metric over EgoVLPv2
**Condition**: EgoTaskQA dataset, compared to EgoVLPv2 baseline

**Evidence**: "under both the direct and indirect settings of EgoTaskQA, MFAS achieves absolute gains of 2.43% and 3.12%, respectively, in the 'All' metric"

## [POSITIVE] LSE Ranking Supervision (L_LSE)
Log-Sum-Exp ranking loss added to the cross-entropy loss for QAEgo4D, using timestamp annotations to select positive frames and two negative frames from different video segments per target moment.

**Delta**: +1.4% Acc, +3.2% BLEU, +0.7% METEOR, +1.2% ROUGE in generative setting; +2.2% Acc, +3.5% BLEU, +0.3% METEOR, +0.3% ROUGE in discriminative setting on QAEgo4D
**Condition**: QAEgo4D dataset, both generative and discriminative settings

**Evidence**: "MFAS† (Ours) achieves 11.9, 8.6, 18.9, 28.2 vs MFAS (Ours) 9.9, 5.4, 17.6, 26.2 in generative; 12.7, 9.3, 18.3, 27.0 vs 10.5, 5.8, 18.0, 26.7 in discriminative"

## [POSITIVE] TimeSformer-B as Video Backbone
Uses pre-trained TimeSformer-B as the foundational video encoder, extended with multi-scale patch processing.

**Delta**: outperforms baseline
**Condition**: Both EgoTaskQA and QAEgo4D datasets

**Evidence**: "following the precedent set (Pramanick et al., 2023), we utilized TimeSformer-B (Bertasius et al., 2021) and RoBERTa-B (Liu et al., 2019) as the foundational backbones for video and question processing, respectively"

## [POSITIVE] RoBERTa-B as Question Encoder
Uses pre-trained RoBERTa-B to extract question representations, producing token embeddings including a [CLS] token.

**Delta**: outperforms baseline
**Condition**: Both EgoTaskQA and QAEgo4D datasets

**Evidence**: "For the question q, we use RoBERTa (Liu et al., 2019) as our backbone to extract its representations"

## [POSITIVE] Dual Spatial Embedding Scheme
Each sub-patch receives both a sub-spatial embedding (position in sub-space) and a spatial embedding (position in full frame space), in addition to temporal embedding, updating the original positional encoding of TimeSformer.

**Delta**: contributes to overall PPM improvement
**Condition**: Patch partition and merging module, small object recognition

**Evidence**: "we introduce a dual spatial information scheme for each sub-patch. This includes the sub-patch's positional data in both subspace and space, allowing for an innovative update to the original position embedding"

## [POSITIVE] First-order Neighborhood Connectivity Constraint
During patch selection, expansion of selected regions is restricted to the immediate one-hop neighborhood (left, right, up, down) of regions identified in the preceding frame, ensuring temporal coherence of selected patches.

**Delta**: contributes to prior-guided patch selection module improvement
**Condition**: Prior-guided patch selection module, temporal consistency

**Evidence**: "This approach ensures a coherent and connected representation of sub-patches by restricting expansion to the immediate neighborhood of regions identified in the preceding frame."

## [POSITIVE] Mask Retention for Initial R-3 Layers
The visual mask A remains unchanged through the first R-3 cross-attention layers, only being down-sampled in the final 3 layers, to preserve fine-grained interactions for robust high-level aggregation.

**Delta**: contributes to hierarchical aggregation network improvement
**Condition**: Hierarchical aggregation network

**Evidence**: "This mask remains unchanged as A through the initial R − 3 layers, where R stands for the total count of spatial-temporal cross-attention layers. This consistency underscores our belief in the criticality of detailed, fine-grained interactions for achieving robust high-level hierarchical aggregation."

## [POSITIVE] LSTM Generative Decoder
Lightweight LSTM coupled with a fully-connected layer used for auto-regressive answer generation on QAEgo4D, with the [CLS] token of video representations as the initial hidden state.

**Delta**: MFAS achieves 9.9 Acc vs 9.0 (BlindVQA), 9.3 (SimpleVQA†), 3.0 (Longformer) in generative setting without LSE
**Condition**: QAEgo4D generative setting

**Evidence**: "we employ a lightweight Long Short-Term Memory (LSTM) model, coupled with an FC layer, to enable this functionality"

## [POSITIVE] MLP Discriminative Decoder
Multi-Layer Perceptron used to map fused video-question representations to a probability distribution over candidate answers for multiple-choice QA.

**Delta**: +2.2% absolute accuracy improvement over EgoVLPv2 in discriminative setting on QAEgo4D
**Condition**: QAEgo4D discriminative setting

**Evidence**: "MFAS achieves an absolute accuracy improvement of 2.2% in the discriminative setting and 0.8% in the generative setting, compared to these optimal baselines"

## [POSITIVE] Sampled Video Frames (vs Full Video)
MFAS uses sampled frames (16 for EgoTaskQA, 32 for QAEgo4D) rather than full video, reducing computational cost while maintaining performance.

**Delta**: MFAS (Sample) outperforms several Full-video baselines including SimpleVQA†, Longformer†, CMCIR, EgoVLP on QAEgo4D
**Condition**: QAEgo4D dataset, generative setting

**Evidence**: "MFAS (Ours) Sample achieves 11.9, 8.6, 18.9, 28.2 compared to Longformer† Full 6.7, 5.4, 16.9, 24.4"

## [POSITIVE] Selection Threshold k=3
Hyperparameter controlling the number of top sub-patches selected per frame in the prior-guided patch selection module.

**Delta**: peak accuracy at k=3; accuracy increases then decreases as k varies from 0 to 5
**Condition**: EgoTaskQA direct split, prior-guided patch selection module

**Evidence**: "This graph reveals an initial increase in accuracy with rising k values, peaking at k=3, before experiencing a subsequent decline."

## [POSITIVE] Balance Coefficient λ=2
Hyperparameter balancing cross-entropy loss and LSE ranking loss in the combined loss function for QAEgo4D.

**Delta**: peak accuracy at λ=2 on QAEgo4D
**Condition**: QAEgo4D dataset with LSE supervision

**Evidence**: "the accuracy of our model achieves its zenith at λ=2, highlighting the critical role of this parameter in attaining peak performance"

## [POSITIVE] Object Recognition Enhancement via PPM
The patch partition and merging module specifically improves object-category question accuracy by leveraging multi-scale patch information.

**Delta**: +6.38% on object category (direct split); +3.92% on object category (indirect split) over EgoVLPv2
**Condition**: EgoTaskQA object-category questions, direct and indirect splits

**Evidence**: "MFAS demonstrates significant accuracy improvements, notably outperforming the EgoVLPv2 baseline with absolute gains of 6.38% and 3.92% under direct and indirect settings, respectively. This underscores the effectiveness of our patch partition and merging strategy in enhancing object recognition capabilities."

## [NEGATIVE] Action Category Performance Degradation
MFAS underperforms CMCIR on action-category questions in the direct setting, possibly due to CMCIR using more comprehensive video information and the straightforward nature of direct questions.

**Delta**: -12.74% on action category (direct split) vs CMCIR
**Condition**: EgoTaskQA direct split, action-category questions

**Evidence**: "our model shows a notable performance dip in the 'action' category when compared to the CMCIR baseline. This could be attributed to CMCIR's utilization of more comprehensive video information and the straightforward nature of the questions that require minimal inference."

## [POSITIVE] MaxPool in Attention Masking
MaxPool operation applied within the spatial-temporal cross-attention mechanism of the hierarchical aggregation network, combined with mask-based suppression of non-selected patches.

**Delta**: contributes to hierarchical aggregation network improvement
**Condition**: Hierarchical aggregation network spatial-temporal cross-attention layers

**Evidence**: "These mechanisms are defined by the expression Softmax(MaxPool(ee⊤)/√d + (−∞ · ¬Ar−1))e, where e is the embedding input and ¬ signifies the negation operation"
