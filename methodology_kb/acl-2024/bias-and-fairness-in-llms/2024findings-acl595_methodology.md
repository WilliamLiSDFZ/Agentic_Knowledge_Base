# Fair Federated Learning with Biased Vision-Language Models

**Source**: https://aclanthology.org/2024.findings-acl.595/

## [POSITIVE] Fairness-aware Deep Visual Prompting (DVP)
A sequence of learnable parameters prepended to the visual tokens at the embedding layer and transformer layers of the CLIP image encoder, designed to remove demographic-related information from CLIP features while preserving domain-generalized information.

**Delta**: ~87% reduction in Φeq bias on smiling detection compared to CLIP zero-shot
**Condition**: Federated learning with biased CLIP for face attribute recognition (FAR) tasks

**Evidence**: "compared to CLIP (zero-shot), the model bias is reduced by approximately 87% w.r.t. Φeq on smiling detection"

## [POSITIVE] Contrastive Loss for DVP Training
CLIP contrastive loss optimized jointly with the fairness loss to maintain overall high performance while adapting the deep visual prompts to task-specific data.

**Delta**: Without it: AB drops from 0.905 to 0.435 on smiling detection; Φeq worsens from 0.028 to 0.160
**Condition**: Training fairness-aware DVP on FAR tasks; critical for model convergence

**Evidence**: "without the contrastive loss (as well as Lfair), the adaptation basically fails. For instance, without the contrastive loss, AB drops from 0.905±0.005 to 0.435±0.096 on smiling detection"

## [POSITIVE] Modality-fused Classification Head (fcls)
A shared lightweight two-layer fully connected network that fuses prompted visual representations and text representations from both modalities, trained with cross-entropy loss and a fairness regularizer on each client.

**Delta**: Without fcls: Φdemo worsens from 0.026 to 0.112 and Φeq from 0.053 to 0.224 on age detection (CelebA)
**Condition**: Client-specific knowledge and fairness constraint learning in FL; dropped at inference time

**Evidence**: "the model fairness w.r.t demographic parity and equalized odds increase without using fcls, indicating the contribution of fcls to fair representation learning"

## [POSITIVE] Demographic-only Prompts with KL Divergence Fairness Loss
Text prompts depicting only demographic information (e.g., 'a photo of a male') used to compute KL divergence between the prompted visual representation's similarity distribution and a uniform distribution, minimizing demographic signal in visual features.

**Delta**: Contributes to ~87% reduction in Φeq on smiling detection vs CLIP zero-shot
**Condition**: Debiasing CLIP features w.r.t. demographic attributes in FL

**Evidence**: "By minimizing Equation 8, all demographic-only text prompts become equally relevant to z̃. This indicates that CLIP can no longer distinguish which demographic group is more related to z̃ than others, thereby, debiasing CLIP."

## [POSITIVE] Frozen CLIP Encoder Weights
The weights of CLIP image and text encoders are not updated or exchanged during FL training; only the visual prompts and classification heads are trained and aggregated.

**Delta**: Enables convergence where baseline methods fail; outperforms baselines on all metrics
**Condition**: Communication-efficient FL with large VLMs; reduces communication burden

**Evidence**: "FF-DVP is a parameter-efficient method... the weights of CLIP encoders are not updated and exchanged... FF-DVP achieves better training convergence than the baseline methods."

## [POSITIVE] Prompting All Transformer Layers (Deep Prompting)
Inserting visual prompts at every transformer layer of the CLIP image encoder rather than only at the input or a subset of layers.

**Delta**: More intervened layers generally improve performance; FF-LoRA (all layers) outperforms FF-ADP (output layer only)
**Condition**: Fairness-aware PEFT for CLIP in FL; trade-off with communication cost

**Evidence**: "we found that more intervened layers would generally improve the performance... FF-ADP only intervenes the output layer of the image encoder, which makes FF-ADP perform worse than FF-DVP and FF-LoRA. In comparison, FF-LoRA intervenes in all layers of the image encoder, and FF-LoRA generally achieves better performance than the others."

## [POSITIVE] Optimal Visual Prompt Length (20 tokens)
Setting the number of tunable visual prompt tokens to 20, balancing model expressiveness and training stability.

**Delta**: AB=0.905 with 20 tokens vs 0.708 with 10 tokens and 0.843 with 30 tokens on smiling detection (CelebA)
**Condition**: Smiling detection on CelebA; optimal value may vary by dataset

**Evidence**: "there exists an optimal length of 20 to use the deep visual prompting. With shorter prompts, the expressive power of the model is reduced... with more tunable tokens, the training becomes slower and unstable."

## [NEGATIVE] Too Few Visual Prompt Tokens (<20)
Using fewer than 20 tunable visual tokens, reducing the expressive power of the prompts.

**Delta**: AB drops from 0.905 to 0.708 when reducing from 20 to 10 tokens on smiling detection
**Condition**: Smiling detection on CelebA with FF-DVP

**Evidence**: "With shorter prompts, the expressive power of the model is reduced, indicating both debiasing and adaptation process is under-fitting the data."

## [NEGATIVE] Too Many Visual Prompt Tokens (>20)
Using more than 20 tunable visual tokens, causing training instability due to insufficient text data.

**Delta**: AB drops to 0.785 with 50 tokens vs 0.848 with 20 tokens on FairFace age detection
**Condition**: Age detection on FairFace with FF-DVP; caused by text data scarcity

**Evidence**: "with more tunable tokens, the training becomes slower and unstable. The instability is caused by the scarcity of the textual modality: there is insufficient amount of text data to train such a large model. For instance, in FairFace age detection, the FL model only achieves 78.5% accuracy with even 50 visual tokens."

## [POSITIVE] Biased Prompts (with demographic information)
Using text prompts that include demographic information alongside class labels (e.g., 'A photo of a male, and he is smiling') as input to CLIP.

**Delta**: +10% zero-shot accuracy on smiling detection (84.8% vs 74.8% with unbiased prompts)
**Condition**: CLIP zero-shot inference for smiling detection on CelebA; FF-DVP can still debias even with biased prompts

**Evidence**: "With biased prompts, CLIP achieves zero-shot accuracy of 84.8% whereas with unbiased prompts, the zero-shot accuracy is only 74.8%. Therefore, we choose to use the biased prompts in our experiments."

## [NEGATIVE] Adapter-style Fine-tuning Extension (FF-ADP)
Combining the FF-DVP fairness framework with attention-based adapter modules inserted into CLIP, intervening only at the output layer of the image encoder.

**Delta**: FF-ADP Φeq=0.150 vs FF-DVP Φeq=0.028 on smiling detection; worse than both FF-DVP and FF-LoRA
**Condition**: Fairness-aware PEFT in FL; limited by single-layer intervention

**Evidence**: "FF-ADP only intervenes the output layer of the image encoder, which makes FF-ADP perform worse than FF-DVP and FF-LoRA."

## [POSITIVE] LoRA Extension (FF-LoRA)
Combining the FF-DVP fairness framework with Low-Rank Adaptation (rank=8) applied to all layers of the CLIP image encoder.

**Delta**: FF-LoRA AB=0.852 vs FF-DVP AB=0.839 on age detection (CelebA); Φeq=0.029 vs 0.053
**Condition**: Fairness-aware PEFT in FL; benefits from all-layer intervention

**Evidence**: "FF-LoRA intervenes in all layers of the image encoder, and FF-LoRA generally achieves better performance than the others."

## [POSITIVE] Pre-trained CLIP as Feature Extractor in FL
Using CLIP's strong generalization ability as the backbone for FL instead of smaller models like ResNet-18, enabling better convergence under high data complexity and heterogeneity.

**Delta**: Baseline methods (FedAvg, AFL, FairFed, FADE) with ResNet-18 barely converge; FF-DVP with CLIP achieves AB=0.905 on smiling vs best baseline 0.900
**Condition**: FL with non-i.i.d. heterogeneous data distributions across clients

**Evidence**: "FF-DVP achieves better training convergence than the baseline methods... We attribute the success of FF-DVP to the pre-trained foundation model as well as our novel fairness-aware adaptation strategy."

## [POSITIVE] Fairness Regularizer in Classification Head
Adding a differentiable fairness regularizer (e.g., demographic parity or equalized odds) to the cross-entropy loss when training the client-specific classification head.

**Delta**: Without fcls (which includes fairness regularizer): Φdemo worsens from 0.026 to 0.112 on age detection (CelebA)
**Condition**: Client-specific fairness constraint learning in FL

**Evidence**: "training fcls on local data contributes to learning client-specific knowledge and fairness constraints. This design improves the fairness of the model in terms of the ultimate prediction performance after the global model aggregation."

## [POSITIVE] Scalability to 40 Clients
Scaling FF-DVP to up to 40 federated clients with non-i.i.d. heterogeneous data distributions.

**Delta**: FF-DVP still converges and achieves similar or better fairness than CLIP zero-shot at 40 clients; baselines fail to converge
**Condition**: Scalability study on smiling detection with up to 40 clients

**Evidence**: "under a larger number of clients, our method could still converge and achieve similar or better fairness than the CLIP zero-shot performance... baseline methods could barely converge. They make predictions randomly and achieve almost perfect but trivial fairness."
