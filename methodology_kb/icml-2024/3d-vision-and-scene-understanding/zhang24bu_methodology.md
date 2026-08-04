# NExT-Chat: An LMM for Chat, Detection and Segmentation

**Source**: https://proceedings.mlr.press/v235/zhang24bu.html

## [POSITIVE] pix2emb paradigm
Models object location as embeddings rather than text token sequences, using a special <trigger> token whose hidden states are decoded by separate box/mask decoders

**Delta**: outperforms baseline
**Condition**: Referring expression segmentation and region captioning tasks

**Evidence**: "NExT-Chat (71.3) vs. LISA (67.9) on referring expression segmentation task, and NExT-Chat (79.6) vs. Kosmos-2 (62.3) on region caption task"

## [POSITIVE] cycle consistency loss (Lcyc)
Aligns location input and output embedding spaces by encoding a bounding box and decoding it back, requiring the result to match the original; also applied to <trigger> hidden states

**Delta**: +3.6 CIDEr, +0.4 METEOR on region captioning; +2.1 to +3.6 Acc@0.5 on REC
**Condition**: Region captioning and referring expression comprehension tasks

**Evidence**: "the model with the Lcyc can achieve 68.7 for CIDEr and 11.3 for METEOR, while the model without Lcyc can only achieve 65.1 for CIDEr and 10.9 for METEOR"

## [POSITIVE] multi-stage training
Three-stage training: stage-1 pre-training with bounding box conversation data, stage-2 fine-tuning for enhanced conversation, stage-3 lightweight segmentation training with frozen LLM

**Delta**: outperforms LISA which uses order of magnitude more mask annotations
**Condition**: Referring expression segmentation with limited mask annotations (127k vs LISA's larger set)

**Evidence**: "Benefiting from the multi-stage training, our NExT-Chat can even achieve better performance than baselines using an order of magnitude larger mask annotations (e.g., LISA)"

## [POSITIVE] SAM as mask decoder with hidden state input
Uses SAM (Segment Anything Model) as the mask head, fed with the <trigger> hidden states projected via a linear projector rather than bounding box coordinates

**Delta**: >1 point cIoU improvement over using box input on all 3 RefCOCO splits
**Condition**: Referring expression segmentation (RES) task

**Evidence**: "we find that the embedding input has an obvious superiority over the box, where changing from box input to embedding input can result in an over 1 point improvement on all of the 3 splits"

## [NEGATIVE] combining box and embedding as SAM inputs
Feeding both the predicted bounding box and the <trigger> embedding into SAM's mask decoder simultaneously

**Delta**: slight degeneration compared to embedding-only input
**Condition**: Referring expression segmentation (RES) task

**Evidence**: "another interesting finding is that further combining the box and embedding will not improve the performance and even cause a slight degeneration. A potential explanation is that the location information has already been encoded in the embedding and the box can not provide any new information"

## [POSITIVE] stage-3 segmentation adaptation training
Training the linear projector between LMM and SAM plus SAM's decoder on referring segmentation data, with all other parameters frozen

**Delta**: significant improvement on RES; e.g., RefCOCO avg from ~69.6 (no training) to ~76.6 cIoU
**Condition**: Referring expression segmentation without task-specific fine-tuning

**Evidence**: "We find that the training can significantly improve the performance on RES task, which shows the necessity of the adaptation training"

## [POSITIVE] 2-layer MLP box decoder
A 2-layer MLP that takes the <trigger> hidden state embedding and regresses bounding box coordinates [x0, y0, x1, y1]

**Delta**: outperforms pix2seq classification-based methods in token efficiency (2 tokens vs 26 for num variant)
**Condition**: Bounding box prediction / referring expression comprehension

**Evidence**: "our pix2emb pattern can be 169 times more effective than num for processing a single bounding box considering the quadratic cost of LM's self-attention calculation"

## [POSITIVE] joint L1 and GIoU detection loss
Combines L1 loss and GIoU loss for bounding box regression with weights αd=2, βd=0.8 following DETR ratios

**Delta**: not explicitly quantified separately
**Condition**: Bounding box detection training

**Evidence**: "we employ a joint loss function comprising of the L1 loss and the GIoU loss (Rezatofighi et al., 2019) during training... αd = 2, βd = 0.8 follows the ratio in DETR"

## [POSITIVE] detection loss weight tuning (k=1)
Balancing the detection loss Ldet weight k relative to text loss Ltext; empirically k=1 found optimal

**Delta**: k=1 achieves 76.7/66.4/71.1 vs 74.6/64.6/68.4 (k=0.5) and 74.6/62.8/67.8 (k=2) on RefCOCO/RefCOCO+/RefCOCOg
**Condition**: Stage-1 pre-training for referring expression comprehension

**Evidence**: "We find that the balance of Ldet and Ltext is essential for the detection performance... empirically observe that k=1 is the best"

## [NEGATIVE] fixed detection loss weight
Using a fixed weight for the detection loss rather than a dynamic balance with the text loss

**Delta**: NExT-Chat slightly lower than Shikra-7B on REC
**Condition**: Referring expression comprehension compared to Shikra-7B

**Evidence**: "a fixed weight of the detection loss is sub-optimal and requires further exploration for a dynamic balance with the text loss"

## [POSITIVE] regression-based location output (vs classification)
Predicting bounding box coordinates as a regression task via MLP decoder rather than classifying into discrete bin tokens

**Delta**: outperforms VisionLLM (+3.3 Acc@0.5 on RefCOCO testA) and Kosmos-2
**Condition**: Referring expression comprehension task

**Evidence**: "our pix2emb is the only method to model the location output as a regression task, which conforms to the nature of coordinates prediction... our NExT-Chat can outperform both the VisionLLM and Kosmos-2 for the REC task"

## [POSITIVE] task-specific fine-tuning of full LLM
Fine-tuning the entire LLM parameters on task-specific data (RES or region captioning splits)

**Delta**: NExT-Chat (ft) achieves best performance across all RES splits vs LISA(ft) and GLaMM(ft); 114.0 CIDEr vs 105.0 for GLaMM(ft) on region captioning
**Condition**: Referring expression segmentation and region captioning with task-specific fine-tuning

**Evidence**: "NExT-Chat (ft) can achieve the best performance compared with LISA (ft) and GLaMM (ft) across all of the data splits, which demonstrates the benefits of boosting the segmentation ability with bounding box data"

## [NEUTRAL] CLIP ViT-L/14@336px image encoder (frozen in stage-1)
Uses CLIP ViT-L/14 at 336px resolution as vision encoder, kept frozen during stage-1 pre-training

**Delta**: not explicitly quantified
**Condition**: Stage-1 pre-training

**Evidence**: "we employ a CLIP ViTL/14@336px as the vision encoder. The input image is converted into 24×24 patch embeddings... keeping the image encoder frozen"

## [NEGATIVE] location encoder trained only via text generation loss
Training the 2-layer MLP location encoder solely through indirect supervision from the captioning/text generation loss without cycle consistency

**Delta**: -3.6 CIDEr, -0.4 METEOR on region captioning
**Condition**: Location input tasks (region captioning) without cycle consistency loss

**Evidence**: "we observe that the location encoder cannot be effectively trained solely through Ltext. Different from the location decoders that can be directly trained with Ldet or Lseg, the supervision from the Ltext is indirect and constrained by the amount of the location input data"
