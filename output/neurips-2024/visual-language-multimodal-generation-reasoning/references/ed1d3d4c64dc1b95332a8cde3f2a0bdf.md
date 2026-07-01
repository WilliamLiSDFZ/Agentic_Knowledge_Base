---
title: "CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Abstract-Conference.html"
categories: ['visual-language-multimodal-generation-reasoning', 'llm-training-and-optimization-techniques']
tags: ['multimodal-llm', 'mixture-of-experts', 'upcycling']
venue: "NeurIPS 2024"
tldr: "Scales multimodal LLMs using co-upcycled Mixture-of-Experts modules for improved efficiency and performance."
---

# CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Abstract-Conference.html)

**TLDR**: Scales multimodal LLMs using co-upcycled Mixture-of-Experts modules for improved efficiency and performance.

## Abstract

Recent advancements in Multimodal Large Language Models (LLMs) have focused primarily on scaling by increasing text-image pair data and enhancing LLMs to improve performance on multimodal tasks. However, these scaling approaches are computationally expensive and overlook the significance of efficiently improving model capabilities from the vision side. Inspired by the successful applications of Mixture-of-Experts (MoE) in LLMs, which improves model scalability during training while keeping inference costs similar to those of smaller models, we propose CuMo, which incorporates Co-upcycled Top-K sparsely-gated Mixture-of-experts blocks into both the vision encoder and the MLP connector, thereby enhancing the multimodal LLMs with neglectable additional activated parameters during inference.CuMo first pre-trains the MLP blocks and then initializes each expert in the MoE block from the pre-trained MLP block during the visual instruction tuning stage, with auxiliary losses to ensure a balanced loading of experts.CuMo outperforms state-of-the-art multimodal LLMs across various VQA and visual-instruction-following benchmarks within each model size group, all while training exclusively on open-sourced datasets.