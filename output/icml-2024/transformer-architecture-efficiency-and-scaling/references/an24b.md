---
title: "Training-Free Long-Context Scaling of Large Language Models"
source: "https://proceedings.mlr.press/v235/an24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/an24b/an24b.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'large-language-model-alignment-and-capabilities']
tags: ['long-context-LLM', 'training-free', 'context-window-extension']
venue: "ICML 2024"
tldr: "This paper proposes a training-free dual-attention method to extend LLM context windows beyond pretraining length without fine-tuning."
---

# Training-Free Long-Context Scaling of Large Language Models

**Source**: [https://proceedings.mlr.press/v235/an24b.html](https://proceedings.mlr.press/v235/an24b.html)

**TLDR**: This paper proposes a training-free dual-attention method to extend LLM context windows beyond pretraining length without fine-tuning.

## Abstract

The ability of Large Language Models (LLMs) to process and generate coherent text is markedly weakened when the number of input tokens exceeds their pretraining length. Given the expensive overhead of finetuning large-scale models with longer sequences, we propose a training-free approach named Dual Chunk Attention (DCA), which enables Llama2 70B to support context windows of up to 100k tokens. By decomposing the attention computation for long sequences into chunk-based modules, DCA manages to effectively capture the relative positional information of tokens within the same chunk (Intra-Chunk) and across distinct chunks (Inter-Chunk), as well as integrates seamlessly with Flash Attention. In addition to its impressive extrapolation capability, DCA achieves performance on practical long-context tasks that is comparable to or even better than that of models built through continual training. All code and data used in this work are released at https://github.com/HKUNLP/ChunkLlama.