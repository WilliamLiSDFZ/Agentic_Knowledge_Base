---
title: "BitDistiller: Unleashing the Potential of Sub-4-Bit LLMs via Self-Distillation"
source: "https://aclanthology.org/2024.acl-long.7/"
pdf_url: ""
categories: ['collaborative-llm-deployment-and-inference-optimization', 'transformer-architecture-analysis-and-design']
tags: ['quantization', 'self-distillation', 'sub-4-bit']
venue: "ACL 2024"
tldr: "BitDistiller enables high-quality sub-4-bit LLM weight quantization through a self-distillation framework to reduce deployment costs."
---

# BitDistiller: Unleashing the Potential of Sub-4-Bit LLMs via Self-Distillation

**Source**: [https://aclanthology.org/2024.acl-long.7/](https://aclanthology.org/2024.acl-long.7/)

**TLDR**: BitDistiller enables high-quality sub-4-bit LLM weight quantization through a self-distillation framework to reduce deployment costs.

## Abstract

AbstractThe upscaling of Large Language Models (LLMs) has yielded impressive advances in natural language processing, yet it also poses significant deployment challenges. Weight quantization has emerged as a widely embraced solution to reduce memory and computational demands. This paper introduces BitDistiller, a framework that synergizes Quantization-Aware Training (QAT) with Knowledge Distillation (KD) to boost the performance of LLMs at ultra-low precisions (sub-4-bit). Specifically, BitDistiller first incorporates a tailored asymmetric quantization and clipping technique to maximally preserve the fidelity of quantized weights, and then proposes a novel Confidence-Aware Kullback-Leibler Divergence (CAKLD) objective, which is employed in a self-distillation manner to enable faster convergence and superior model performance. Empirical evaluations demonstrate that BitDistiller significantly surpasses existing methods in both 3-bit and 2-bit configurations on general language understanding and complex reasoning benchmarks. Notably, BitDistiller is shown to be more cost-effective, demanding fewer data and training resources. The code is available at https://github.com/DD-DuDa/BitDistiller.