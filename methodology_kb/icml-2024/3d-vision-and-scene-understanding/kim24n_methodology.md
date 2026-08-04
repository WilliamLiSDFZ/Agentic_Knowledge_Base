# Scene Graph Generation Strategy with Co-occurrence Knowledge and Learnable Term Frequency

**Source**: https://proceedings.mlr.press/v235/kim24n.html

## [POSITIVE] Co-occurrence Knowledge (CooK)
A matrix encoding the probability of object classes co-occurring in the same image, extracted from training data and incorporated into the MPNN attention mechanism to reflect prior knowledge about object correlations during feature updates.

**Delta**: +2.1%/+2.3% mR@50/100 on PredCls (VG); +0.4%/+0.5% mR@50/100 on SGGen (VG)
**Condition**: Applied to MPNN-based SGG models on Visual Genome dataset; improvement is larger when ground-truth object labels are available (PredCls) than when predicted labels are used (SGCls, SGGen)

**Evidence**: "For CooK, which includes the co-occurrence knowledge between objects, PredCls showed a performance improvement of 2.1% / 2.3% on mR@50 / 100 because the object GT was reflected in CooK."

## [POSITIVE] Learnable TF-l-IDF Layer
A layer that computes term frequency-inverse document frequency scores over object class labels in a batch and uses them to reweight node features, boosting tail/body class features and suppressing head class features. Includes trainable parameters epsilon and gamma.

**Delta**: +2.4% average performance improvement over non-learnable version (ablation); similar improvement levels across PredCls, SGCls, SGGen
**Condition**: Applied after MPNN block on Visual Genome dataset; effectiveness scales with batch size

**Evidence**: "As can be seen in Table 4, the use of learnable parameters led to an average 2.4% performance improvement when compared to the case where they were not used. This is because learnable parameters can mitigate the cases in which a specific label is oversampled during training."

## [POSITIVE] CooK + TF-l-IDF Combined
Joint application of co-occurrence knowledge injection into MPNN and the learnable TF-l-IDF layer for node feature reweighting, forming the full proposed pipeline.

**Delta**: +3.8% on SGGen subtask vs. state-of-the-art; mR@50/100 of 14.2/16.3 on SGGen VG; score_wtd of 45.1 on OI
**Condition**: Applied to MPNN-based SGG models on both Visual Genome and Open Images datasets

**Evidence**: "The results showed a performance improvement of up to 3.8% compared with existing state-of-the-art models in SGGen subtask... the largest performance improvement was observed when using information for both CooK and TF-l-IDF."

## [POSITIVE] Learnable Parameters in IDF (epsilon and gamma)
Trainable scalar parameters added to the log term of the IDF calculation to dynamically adjust for oversampling of body or tail labels during training.

**Delta**: +2.4% average across PredCls, SGCls, SGGen on VG
**Condition**: Ablation on Visual Genome dataset comparing TF-l-IDF with and without learnable parameters

**Evidence**: "To address potential biases introduced during training owing to uneven sampling, we add trainable parameters ϵ and γ. These parameters allow for dynamic adjustments to the log term, thereby minimizing the impact of scenarios in which the body or tail labels are oversampled."

## [POSITIVE] Advanced CooK (Multi-dataset)
CooK matrix constructed by combining co-occurrence statistics from both Visual Genome and Open Images datasets via a hand-crafted mapping function, providing broader and more generalized object co-occurrence knowledge.

**Delta**: +0.3%/+0.7%/+0.8% mR@20/50/100 on SGGen VG compared to single-dataset CooK
**Condition**: Applied on Visual Genome SGGen task; OI-to-VG mapping is hand-crafted and excludes OI-only labels with no VG equivalent

**Evidence**: "Similar to the general improvement effect of knowledge, the advanced CooK achieved a higher performance than individual CooK. This demonstrates that CooK can improve the performance if the task uses knowledge obtained from similar datasets."

## [POSITIVE] Larger Batch Size for TF-l-IDF
Increasing the batch size used during training with the TF-l-IDF layer, since the IDF computation relies on label frequency statistics across the batch.

**Delta**: Monotonically increasing performance across all subtasks as batch size increases (quantitative values shown in Figure 3)
**Condition**: Applies to TF-l-IDF layer on Visual Genome PredCls, SGCls, and SGGen subtasks

**Evidence**: "As shown in the figure, the performance gradually increased for all subtasks as the batch size increased. Therefore, it is necessary to increase the batch size to perform more sophisticated feature updates."

## [POSITIVE] CooK Integration into MPNN Attention
Replacing the standard attention score between nodes u and v in the MPNN with a product that includes the CooK co-occurrence probability value, so that object co-occurrence knowledge modulates message passing.

**Delta**: Mean improvement of 17.6% mR@50 and 22.6% mR@100 on SGGen across G-RCNN, GPS-Net, BGNN
**Condition**: Applied to G-RCNN, GPS-Net, and BGNN on Visual Genome SGGen subtask

**Evidence**: "As shown in Table 3, we can confirm that there was a performance improvement in all MPNN-based models. This shows that the proposed method can be broadly applied to MPNN-based SGG tasks and can achieve high generalization performance."

## [POSITIVE] Long-tail Mitigation via TF-l-IDF Feature Reweighting
Using TF-l-IDF scores to upweight features of rare (tail/body) object classes and downweight features of frequent (head) classes, addressing the long-tail distribution in scene graph datasets.

**Delta**: mR@100 for head classes decreased; mR@100 for body and tail classes increased significantly (Figure 4)
**Condition**: Evaluated on Visual Genome SGGen task comparing G-RCNN, GPS-Net, BGNN, HetSGG, CooK-only, TF-l-IDF-only, and CooK+TF-l-IDF

**Evidence**: "As illustrated in the figure, the mR@100 value for the head decreased, whereas those for the body and tail parts increased significantly. This demonstrates that CooK's 'knowledge of object co-occurrence' and TF-l-IDF's 'feature update' were successfully applied to each class part."

## [POSITIVE] CooK-only (without TF-l-IDF) on SGCls/SGGen
Applying only the co-occurrence knowledge module without the TF-l-IDF layer in subtasks where object labels are predicted rather than given.

**Delta**: +0.3%/+0.1% mR@50/100 on SGCls; +0.4%/+0.5% mR@50/100 on SGGen
**Condition**: Visual Genome SGCls and SGGen subtasks where predicted (not ground-truth) object labels are used

**Evidence**: "SGCls and SGGen each improved the performance by 0.3% / 0.1% and 0.4% / 0.5% on mR@50 / 100, respectively, but the performance improvements were smaller than those of PredCls. This is because neither method reflects CooK information and uses object labels directly predicted by the model."

## [NEUTRAL] GloVe Word Embeddings for Object Features
Using pre-trained GloVe embeddings as the word embedding method for object label representations in the SGG pipeline.

**Delta**: Not quantified separately
**Condition**: Used as a standard component in all experiments on both VG and OI datasets

**Evidence**: "GloVe (Pennington et al., 2014) was used to word embedding method."

## [NEUTRAL] Faster R-CNN with ResNeXt-101-FPN Object Detector
Using Faster R-CNN with a ResNeXt-101-FPN backbone as the object detector to extract visual features and bounding boxes for SGG.

**Delta**: Not quantified separately
**Condition**: Used as a standard backbone in all experiments; consistent with prior SGG works

**Evidence**: "To detect objects in the image, we adopted the Faster R-CNN (Ren et al., 2015) with ResNeXt-101FPN (Xie et al., 2017)."
