---
name: transformer-architecture-analysis-and-design
description: >-
  This skill covers the analysis, optimization, and architectural modification of transformer-based language models, including techniques such as structured pruning, quantization, sparse activation, mixture-of-experts (MoE) routing/serving, positional encoding improvements (e.g., RoPE variants), and attention mechanism redesign (e.g., linear transformers, graph-based information flow).
---

# Transformer Architecture Analysis And Design

This skill covers the analysis, optimization, and architectural modification of transformer-based language models, including techniques such as structured pruning, quantization, sparse activation, mixture-of-experts (MoE) routing/serving, positional encoding improvements (e.g., RoPE variants), and attention mechanism redesign (e.g., linear transformers, graph-based information flow).

## Entry Index

| # | Title | Tags | File |
|---|-------|------|------|
| 1 | LM Transparency Tool: Interactive Tool for Analyzing Transfo | transformer-interpretability, interactive-tool, attention-analysis | 2024acl-demos6.md |
| 2 | DeepSeekMoE: Towards Ultimate Expert Specialization in Mixtu | mixture-of-experts, expert-specialization, model-scaling | 2024acl-long70.md |
| 3 | Fantastic Semantics and Where to Find Them: Investigating Wh | lexical-semantics, generative-llm, layer-analysis | 2024findings-acl866.md |
| 4 | UltraSparseBERT: 99% Conditionally Sparse Language Modelling | sparse-transformers, conditional-computation, efficient-inference | 2024acl-short10.md |
| 5 | Generative Pre-trained Speech Language Model with Efficient  | speech-language-model, hierarchical-transformer, audio-codec | 2024acl-long97.md |
| 6 | Your Transformer is Secretly Linear | transformer-decoders, linear-representation, layer-analysis | 2024acl-long293.md |
| 7 | Resonance RoPE: Improving Context Length Generalization of L | rotary-position-embedding, context-length-generalization, train-short-test-long | 2024findings-acl32.md |
| 8 | GNNavi: Navigating the Information Flow in Large Language Mo | graph-neural-networks, in-context-learning, fine-tuning | 2024findings-acl237.md |
| 9 | LRQuant: Learnable and Robust Post-Training Quantization for | quantization, post-training, llm-efficiency | 2024acl-long122.md |
| 10 | Pruning Large Language Models to Intra-module Low-rank Archi | structured-pruning, low-rank, llm-compression | 2024findings-acl582.md |
| 11 | MoExtend: Tuning New Experts for Modality and Task Extension | multimodal-LLM, mixture-of-experts, modality-extension | 2024acl-srw53.md |
| 12 | NeuroPrune: A Neuro-inspired Topological Sparse Training Alg | sparse-training, pruning, neuro-inspired | 2024findings-acl142.md |
| 13 | SwapMoE: Serving Off-the-shelf MoE-based Large Language Mode | MoE, memory-efficient-serving, LLM-inference | 2024acl-long363.md |
| 14 | Linear Transformers with Learnable Kernel Functions are Bett | linear-transformers, learnable-kernels, in-context-learning | 2024acl-long518.md |
| 15 | BranchNorm: Robustly Scaling Extremely Deep Transformers | deep-transformers, training-stability, normalization | 2024findings-acl695.md |
| 16 | Dodo: Dynamic Contextual Compression for Decoder-only LMs | context-compression, decoder-only, dynamic-hidden-states | 2024acl-long536.md |
| 17 | On the Representational Capacity of Neural Language Models w | chain-of-thought, representational-capacity, computational-expressiveness | 2024acl-long676.md |
| 18 | ETAS: Zero-Shot Transformer Architecture Search via Network  | transformer-architecture-search, zero-shot, trainability | 2024findings-acl405.md |
| 19 | Accelerating Multilingual Language Model for Excessively Tok | multilingual-tokenization, non-roman-scripts, inference-acceleration | 2024findings-acl660.md |
| 20 | Monotonic Representation of Numeric Attributes in Language M | numeric-attributes, monotonic-representation, language-model-editing | 2024acl-short18.md |
| 21 | Looking Right is Sometimes Right: Investigating the Capabili | decoder-only-llms, sequence-labeling, causal-language-models | 2024findings-acl843.md |
| 22 | AFLoRA: Adaptive Freezing of Low Rank Adaptation in Paramete | parameter-efficient-fine-tuning, LoRA, adaptive-freezing | 2024acl-short16.md |
| 23 | Modeling Emotional Trajectories in Written Stories Utilizing | emotional-trajectories, story-analysis, weakly-supervised | 2024findings-acl426.md |
| 24 | Raccoon: Prompt Extraction Benchmark of LLM-Integrated Appli | prompt-extraction, benchmark, LLM-security | 2024findings-acl791.md |
| 25 | Generalizability of Mixture of Domain-Specific Adapters from | adapter-fusion, parameter-efficient-fine-tuning, model-pruning | 2024acl-long700.md |
| 26 | LoRAPrune: Structured Pruning Meets Low-Rank Parameter-Effic | structured-pruning, LoRA, efficient-fine-tuning | 2024findings-acl178.md |
| 27 | Chunk, Align, Select: A Simple Long-sequence Processing Meth | long-sequence, transformer, chunking | 2024acl-long729.md |
| 28 | When Only Time Will Tell: Interpreting How Transformers Proc | incremental-processing, ambiguity-resolution, transformers | 2024acl-long260.md |
| 29 | AdaLomo: Low-memory Optimization with Adaptive Learning Rate | low-memory-optimization, adaptive-learning-rate, llm-training | 2024findings-acl742.md |
| 30 | LoRA Meets Dropout under a Unified Framework | LoRA, dropout, parameter-efficient-finetuning | 2024findings-acl119.md |
| 31 | Tree-Planted Transformers: Unidirectional Transformer Langua | syntactic-language-models, transformers, tree-planting | 2024findings-acl303.md |
| 32 | NACL: A General and Effective KV Cache Eviction Framework fo | KV-cache, inference-efficiency, LLMs | 2024acl-long428.md |
| 33 | Light-PEFT: Lightening Parameter-Efficient Fine-Tuning via E | parameter-efficient-fine-tuning, pruning, training-efficiency | 2024findings-acl447.md |
| 34 | Extending Context Window of Large Language Models via Semant | context-window-extension, semantic-compression, long-text | 2024findings-acl306.md |
| 35 | Mixture-of-Supernets: Improving Weight-Sharing Supernet Trai | neural-architecture-search, mixture-of-experts, weight-sharing | 2024findings-acl621.md |
| 36 | Dwell in the Beginning: How Language Models Embed Long Docum | positional-bias, dense-retrieval, document-encoding | 2024acl-short35.md |
| 37 | AFPQ: Asymmetric Floating Point Quantization for LLMs | quantization, floating-point, llm-inference | 2024findings-acl3.md |
| 38 | BadActs: A Universal Backdoor Defense in the Activation Spac | backdoor-defense, activation-space, neural-network-security | 2024findings-acl317.md |
| 39 | PyramidInfer: Pyramid KV Cache Compression for High-throughp | kv-cache, inference-efficiency, memory-compression | 2024findings-acl195.md |
| 40 | Not All Experts are Equal: Efficient Expert Pruning and Skip | mixture-of-experts, model-pruning, inference-efficiency | 2024acl-long334.md |
| 41 | Revisiting Knowledge Distillation for Autoregressive Languag | knowledge-distillation, language-model-compression, autoregressive-lm | 2024acl-long587.md |
| 42 | Analysing The Impact of Sequence Composition on Language Mod | pre-training, sequence-composition, document-concatenation | 2024acl-long427.md |
| 43 | Why are Sensitive Functions Hard for Transformers? | transformers, parity, boolean-functions | 2024acl-long800.md |
| 44 | Symmetric Dot-Product Attention for Efficient Training of BE | symmetric-attention, BERT, transformer | 2024findings-acl476.md |
| 45 | Layer-Condensed KV Cache for Efficient Inference of Large La | KV-cache, inference-efficiency, memory-optimization | 2024acl-long602.md |
| 46 | LayerSkip: Enabling Early Exit Inference and Self-Speculativ | early-exit, speculative-decoding, inference-efficiency | 2024acl-long681.md |
| 47 | A Meta-Learning Perspective on Transformers for Causal Langu | meta-learning, transformer-analysis, causal-language-modeling | 2024findings-acl922.md |
| 48 | HiRoPE: Length Extrapolation for Code Models Using Hierarchi | positional-encoding, context-length, code-generation | 2024acl-long735.md |
| 49 | Unlocking Efficiency in Large Language Model Inference: A Co | speculative-decoding, inference-efficiency, survey | 2024findings-acl456.md |
| 50 | Finding and Editing Multi-Modal Neurons in Pre-Trained Trans | multimodal-neurons, model-editing, transformers | 2024findings-acl60.md |
| 51 | NextLevelBERT: Masked Language Modeling with Higher-Level Re | masked-language-modeling, long-documents, hierarchical-representations | 2024acl-long256.md |
| 52 | Fast Randomized Low-Rank Adaptation of Pre-trained Language  | lora, parameter-efficient-fine-tuning, randomized-methods | 2024findings-acl310.md |
| 53 | BASS: Batched Attention-optimized Speculative Sampling | speculative-decoding, batched-inference, throughput-optimization | 2024findings-acl489.md |
| 54 | SparseFlow: Accelerating Transformers by Sparsifying Informa | sparse-attention, transformer-efficiency, information-flow | 2024acl-long323.md |
| 55 | Maverick: Efficient and Accurate Coreference Resolution Defy | coreference-resolution, efficient-models, task-specific-architecture | 2024acl-long722.md |
| 56 | Competition of Mechanisms: Tracing How Language Models Handl | mechanistic-interpretability, factual-recall, counterfactuals | 2024acl-long458.md |
| 57 | On the Impact of Calibration Data in Post-training Quantizat | quantization, pruning, calibration-data | 2024acl-long544.md |
| 58 | On the Effect of (Near) Duplicate Subwords in Language Model | tokenization, subword-duplication, language-modeling-efficiency | 2024findings-acl571.md |
| 59 | Long-Context Language Modeling with Parallel Context Encodin | long-context, language-modeling, parallel-context-encoding | 2024acl-long142.md |
| 60 | HyperMoE: Towards Better Mixture of Experts via Transferring | mixture-of-experts, knowledge-transfer, sparse-models | 2024acl-long571.md |
| 61 | Found in the middle: Calibrating Positional Attention Bias I | long-context, positional-bias, attention | 2024findings-acl890.md |
| 62 | Length Generalization of Causal Transformers without Positio | length-generalization, transformers, position-encoding | 2024findings-acl834.md |
| 63 | Identifying Semantic Induction Heads to Understand In-Contex | attention-heads, in-context-learning, interpretability | 2024findings-acl412.md |
| 64 | Surgical Feature-Space Decomposition of LLMs: Why, When and  | low-rank-approximation, feature-decomposition, inference-efficiency | 2024acl-long130.md |
| 65 | XMoE: Sparse Models with Fine-grained and Adaptive Expert Se | mixture-of-experts, sparse-models, adaptive-routing | 2024findings-acl694.md |
| 66 | What Makes Language Models Good-enough? | good-enough-processing, psycholinguistics, language-model-architecture | 2024findings-acl913.md |
| 67 | Understanding and Patching Compositional Reasoning in LLMs | compositional-reasoning, LLM-failure, implicit-relations | 2024findings-acl576.md |
| 68 | DoRA: Enhancing Parameter-Efficient Fine-Tuning with Dynamic | parameter-efficient-fine-tuning, dynamic-rank, LoRA | 2024acl-long626.md |
| 69 | Expedited Training of Visual Conditioned Language Generation | vision-language-pretraining, redundancy-reduction, efficient-training | 2024acl-long19.md |
| 70 | ResLoRA: Identity Residual Mapping in Low-Rank Adaption | parameter-efficient-fine-tuning, LoRA, residual-mapping | 2024findings-acl525.md |
| 71 | Anchor-based Large Language Models | anchor-tokens, KV-cache, efficient-transformer | 2024findings-acl295.md |
| 72 | E2-LLM: Efficient and Extreme Length Extension of Large Lang | long-context, LLM-extension, efficient-training | 2024findings-acl252.md |
| 73 | FreeCtrl: Constructing Control Centers with Feedforward Laye | controllable-text-generation, feedforward-layers, learning-free | 2024acl-long412.md |
| 74 | Integrating Pre-Trained Speech and Language Models for End-t | ASR, speech-recognition, pre-trained-models | 2024findings-acl787.md |
| 75 | Computational Expressivity of Neural Language Models | formal-language-theory, neural-language-models, expressivity | 2024acl-tutorials3.md |
| 76 | Fortify the Shortest Stave in Attention: Enhancing Context A | attention-mechanism, context-awareness, tool-use | 2024acl-long601.md |
| 77 | PEMT: Multi-Task Correlation Guided Mixture-of-Experts Enabl | parameter-efficient, mixture-of-experts, multi-task | 2024findings-acl410.md |
| 78 | SpikeVoice: High-Quality Text-to-Speech Via Efficient Spikin | spiking-neural-network, text-to-speech, brain-inspired | 2024acl-long429.md |
| 79 | IntactKV: Improving Large Language Model Quantization by Kee | LLM-quantization, KV-cache, pivot-tokens | 2024findings-acl460.md |
| 80 | Selective Prefix Tuning for Pre-trained Language Models | prefix-tuning, parameter-efficient, fine-tuning | 2024findings-acl164.md |
| 81 | BitDistiller: Unleashing the Potential of Sub-4-Bit LLMs via | quantization, self-distillation, sub-4-bit | 2024acl-long7.md |
| 82 | Neurons in Large Language Models: Dead, N-gram, Positional | neuron-analysis, OPT-models, FFN-activation | 2024findings-acl75.md |
| 83 | Harder Task Needs More Experts: Dynamic Routing in MoE Model | mixture-of-experts, dynamic-routing, computational-efficiency | 2024acl-long696.md |
| 84 | WRP: Weight Recover Prune for Structured Sparsity | model-pruning, structured-sparsity, LLM-compression | 2024acl-long347.md |
| 85 | VISPool: Enhancing Transformer Encoders with Vector Visibili | graph-neural-networks, transformer, text-representation | 2024findings-acl149.md |
| 86 | PartialFormer: Modeling Part Instead of Whole for Machine Tr | transformer, machine-translation, feed-forward-network | 2024findings-acl434.md |
| 87 | Instruction Position Matters in Sequence Generation with Lar | instruction-tuning, sequence-generation, position-sensitivity | 2024findings-acl693.md |
| 88 | CeeBERT: Cross-Domain Inference in Early Exit BERT | early-exit, bert, cross-domain-inference | 2024findings-acl101.md |
| 89 | A Mechanistic Analysis of a Transformer Trained on a Symboli | transformer-interpretability, mechanistic-analysis, symbolic-reasoning | 2024findings-acl242.md |
| 90 | PRoLoRA: Partial Rotation Empowers More Parameter-Efficient  | parameter-efficient-finetuning, LoRA, rotation | 2024acl-long156.md |
| 91 | Inducing Systematicity in Transformers by Attending to Struc | systematicity, transformers, compositional-generalization | 2024acl-long455.md |
| 92 | Efficient Domain Adaptation for Non-Autoregressive Machine T | domain-adaptation, non-autoregressive-MT, neural-machine-translation | 2024findings-acl810.md |
| 93 | CQIL: Inference Latency Optimization with Concurrent Computa | inference-optimization, parallel-computation, transformer-layers | 2024acl-long394.md |
| 94 | Parallel Structures in Pre-training Data Yield In-Context Le | in-context-learning, pretraining-data, parallel-structures | 2024acl-long465.md |
| 95 | LLM in a flash: Efficient Large Language Model Inference wit | llm-inference, flash-memory, memory-efficiency | 2024acl-long678.md |
| 96 | CoCA: Fusing Position Embedding with Collinear Constrained A | transformer-attention, positional-encoding, long-context | 2024acl-long233.md |
| 97 | EIT: Enhanced Interactive Transformer | multi-head-attention, complementarity, consensus-principle | 2024acl-long418.md |
