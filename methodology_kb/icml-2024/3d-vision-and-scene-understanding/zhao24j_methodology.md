# Spider: A Unified Framework for Context-dependent Concept Segmentation

**Source**: https://proceedings.mlr.press/v235/zhao24j.html

## [POSITIVE] Concept Filter
A dynamic filtering mechanism driven by image-mask group prompts that generates object-aware weights and context-aware biases to act on the tail of the segmentation decoder, enabling task discrimination without task-specific heads.

**Delta**: more than 25% improvement over UNet baseline on all tasks
**Condition**: Applied in the dynamic head of the unified segmentation framework across all 8 CD tasks

**Evidence**: "image-group prompts have the basic ability to find task commonality from image group, which significantly improves the performance over UNet on all tasks by more than 25%"

## [POSITIVE] Background Mask-Group Prompts
Using background mask prompts in addition to foreground prompts to highlight the importance of surroundings for context-dependent concept expression, generating context-aware bias for the concept filter.

**Delta**: 40% performance gain compared to UNet baseline
**Condition**: Applied when both foreground and background descriptors are used in the concept filter

**Evidence**: "the background features are introduced to highlight the importance of the surroundings for concept expression, which achieves 40% performance gain compared to the baseline"

## [POSITIVE] Foreground Mask-Group Prompts
Using foreground mask prompts as queries in cross-attention to establish contrast between object queries and the whole image, generating foreground descriptors.

**Delta**: achieves similar performance to separate training model
**Condition**: Applied as an intermediate step before adding background prompts

**Evidence**: "the foreground features are used as the query of transformer to directly establish the contrast relationship between the object query and the whole image. In this way, '+ Mask-Group Prompts (Foreground)' achieves similar performance with the separate training model"

## [POSITIVE] Image-Group Prompts
Using a group of images (without mask information) as prompts encoded as key and value in the transformer to find task commonality.

**Delta**: more than 25% improvement over UNet baseline
**Condition**: Applied as the first step in the concept filter pipeline

**Evidence**: "image-group prompts have the basic ability to find task commonality from image group, which significantly improves the performance over UNet on all tasks by more than 25%"

## [NEGATIVE] Concept Filter with Addition Fusion (ablation)
Replacing the concept filter's high-level matching mechanism with element-wise addition fusion while keeping a similar number of parameters.

**Delta**: large performance drop across all tasks (e.g., Salient F from 0.8732 to 0.6534, Camouflaged from 0.7779 to 0.5742)
**Condition**: Ablation comparison showing the importance of the dynamic filtering approach over simple fusion

**Evidence**: "we replace the concept filter with the element-wise addition fusion (keeping similar number of parameters) to show the advantages of the proposed high-level concept matching mechanism"

## [POSITIVE] Joint Training with 100% Shared Parameters
Training a single model jointly on all 8 tasks simultaneously with fully shared encoder-decoder parameters, as opposed to training separate models per task.

**Delta**: consistently outperforms separately trained models on all tasks (e.g., Salient F: 0.8732 vs 0.8593, Camouflaged F: 0.7779 vs 0.7543)
**Condition**: Applied across all 8 context-dependent segmentation tasks

**Evidence**: "the jointly trained models consistently outperform the separately trained ones on all tasks. This indicates that our framework with 100% shared parameters can assimilate rich cross-domain knowledge"

## [POSITIVE] Balance FP - Unify BP Training Strategy
A training strategy that balances different tasks in forward propagation (equal batch sampling per task) and unifies gradient updates in back propagation to treat all task data as a whole.

**Delta**: outperforms Random FP - Unify BP and Balance FP - Separate BP variants across most tasks
**Condition**: Applied during unified multi-task training of Spider

**Evidence**: "'Balance FP - Unify BP' performs the best, which suggests that when training a unified model, all task data should be treated as a whole and each part is equally important. Belittling any one of them will produce negative effect to other tasks"

## [NEGATIVE] Random FP - Unify BP (ablation)
Using random data partition in forward propagation but unified gradient updates in back propagation.

**Delta**: lower performance than Balance FP - Unify BP (e.g., Salient F: 0.8608 vs 0.8732, COVID-19 mDice: 0.6340 vs 0.6925)
**Condition**: Ablation of training strategy in unified framework

**Evidence**: "We conduct the experiments in terms of forward and back propagation, including random data partition and separate gradient update for each task. We can see that 'Balance FP - Unify BP' performs the best"

## [NEGATIVE] Balance FP - Separate BP (ablation)
Using balanced data partition in forward propagation but separate gradient updates per task in back propagation.

**Delta**: lower performance than Balance FP - Unify BP (e.g., Salient F: 0.8422 vs 0.8732, Polyp mDice: 0.7979 vs 0.8211)
**Condition**: Ablation of training strategy in unified framework

**Evidence**: "We conduct the experiments in terms of forward and back propagation, including random data partition and separate gradient update for each task. We can see that 'Balance FP - Unify BP' performs the best"

## [NEUTRAL] K-means Clustering for Inference Prompt Selection
Selecting 64 representative group prompts per task at inference time using K-means clustering over high-level embeddings, instead of random selection.

**Delta**: almost the same performance as Random Selection (G=64)
**Condition**: Applied at inference time for stable and replicable predictions

**Evidence**: "'Clustering Selection (G = 64)' has almost the same performance as 'Random Selection'. Thus, the strategy of random selection during training indeed makes Spider robust against different group prompts when testing"

## [POSITIVE] Increasing Number of Group Prompts (G)
Using more image-mask pairs as group prompts during inference, ranging from G=1 to G=64.

**Delta**: performance improves monotonically from G=1 to G=64 (e.g., Salient F: 0.7038 at G=1 to 0.8723 at G=64)
**Condition**: Applied during inference phase; performance stabilizes at G=64

**Evidence**: "the overall performance is the worst when G = 1. As the number increases, the performance is gradually elevated and stabilizes when G = 64"

## [POSITIVE] Random Combination of Group Prompts During Training
Randomly selecting G pairs of images and masks from each task at each training iteration as group prompts, similar in motivation to masked image modeling.

**Delta**: makes Spider robust against different group prompts when testing
**Condition**: Applied during training to improve inference robustness

**Evidence**: "This manner of random combination ensures the performance stability of the concept filter when facing different group prompts in practical applications, and its motivation and effects are similar to those of the masked image modeling (MIM) mechanism"

## [POSITIVE] Batch Normalization in Unified Training
Using batch normalization across all tasks in the unified training pipeline to make input distributions of each task closer.

**Delta**: helps model learn task-shared representations, improving and balancing overall performance
**Condition**: Applied during forward propagation in the Balance FP strategy

**Evidence**: "the batch normalization can make the input distribution of each task closer, which helps the model learn task-shared representations, improving and balancing the overall performance"

## [POSITIVE] Continuous Learning via Fine-tuning <1% Parameters
Fine-tuning only the last decoder layer and concept filter (less than 1% of parameters) to learn new tasks without retraining the full model.

**Delta**: performance degradation of less than 5% on old tasks while significantly improving new task performance
**Condition**: Applied when adding new tasks (T5-T8) after initial joint training on T1-T4

**Evidence**: "Spider's performance on new tasks is significantly improved, while there is only a negligible performance degradation of no more than 5% on the old tasks"

## [POSITIVE] Frozen Pre-trained Encoder for Prompt Stream
Using a frozen pre-trained encoder to process image group prompts, extracting rich high-level semantic features without updating these weights.

**Delta**: enables rich high-level semantic feature extraction for concept filter generation
**Condition**: Applied in the image prompt stream Si during both training and inference

**Evidence**: "we pass the image group to the frozen pre-trained encoder E to obtain rich high-level semantic features"

## [POSITIVE] Larger Backbone Scale (ConvNeXt-L vs smaller variants)
Using larger backbone architectures (e.g., ConvNeXt-L) compared to smaller ones (e.g., ViT-B, Swin-B, ConvNeXt-B).

**Delta**: Spider-ConvNeXt-L achieves best results on most tasks (e.g., Salient F: 0.8821 vs 0.8679 for ViT-B, Camouflaged F: 0.7893 vs 0.7532 for ViT-B)
**Condition**: Applied when computational resources allow; best performance on salient, camouflaged, shadow, polyp, COVID-19, and breast tasks

**Evidence**: "Our largest version, Spider-ConvNext-L, has the same 1.5G model size as SegGPT... Spider-ConvNeXt-L achieves best scores highlighted in red across most tasks"

## [POSITIVE] Multi-Head Cross-Attention for Descriptor Refinement
Using multi-head cross-attention (MHCA) where foreground/background descriptors act as queries and group prompt features act as keys and values, to refine descriptors by mining global semantic cues.

**Delta**: enables generation of high-quality object-aware weights and context-aware biases for concept filter
**Condition**: Applied within the concept filter generation module

**Evidence**: "We further refine the two descriptors by mining foreground/background related semantic cues in the global context from appearance-driven Fmem. This process is achieved through multi-head cross-attention (MHCA)"

## [POSITIVE] Masked Average Pooling for Descriptor Extraction
Using masked average pooling on group prompt features guided by foreground and background mask groups to extract rough foreground and background representations.

**Delta**: extracts rough representations about foreground and background specific to current task contexts
**Condition**: Applied as the initial step in concept filter generation before MHCA refinement

**Evidence**: "The foreground mask group Mfg and background mask group Mbg corresponding to the targets of interest in the image-group prompt guide to yield foreground descriptor Dfg and background descriptor Dbg by masked average pooling"

## [NEGATIVE] Single Image-Mask Pair Prompt (SegGPT baseline)
Using a single image-foreground mask pair as prompt for context-dependent segmentation, as done in SegGPT.

**Delta**: SegGPT achieves only 0.3874 F on Salient vs Spider's 0.8679; 0.4041 on Camouflaged vs Spider's 0.7532
**Condition**: Applied in SegGPT for context-dependent segmentation tasks

**Evidence**: "Limited by the prompt strategy based on a single image-mask pair, SegGPT cannot show the generalization ability across these tasks involving context-dependent concepts, even if it has been trained on more than 250,000 diverse images"

## [POSITIVE] Cross-Domain Data Augmentation (basic)
Using basic image augmentation techniques including random flipping, rotating, and border clipping to avoid overfitting.

**Delta**: helps avoid overfitting in unified training
**Condition**: Applied during training across all 8 tasks

**Evidence**: "We adopt some basic image augmentation techniques to avoid overfitting, including random flipping, rotating and border clipping"
