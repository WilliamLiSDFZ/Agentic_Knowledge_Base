---
title: "QuIP$#$: Even Better LLM Quantization with Hadamard Incoherence and Lattice Codebooks"
source: "https://proceedings.mlr.press/v235/tseng24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tseng24a/tseng24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'llm-serving-systems-and-infrastructure']
tags: ['LLM-quantization', 'Hadamard-incoherence', 'lattice-codebooks']
venue: "ICML 2024"
tldr: "QuIP# achieves state-of-the-art LLM post-training quantization at extreme compression using Hadamard incoherence and lattice codebooks."
---

# QuIP$#$: Even Better LLM Quantization with Hadamard Incoherence and Lattice Codebooks

**Source**: [https://proceedings.mlr.press/v235/tseng24a.html](https://proceedings.mlr.press/v235/tseng24a.html)

**TLDR**: QuIP# achieves state-of-the-art LLM post-training quantization at extreme compression using Hadamard incoherence and lattice codebooks.

## Abstract

Post-training quantization (PTQ) reduces the memory footprint of LLMs by quantizing their weights to low-precision. In this work, we introduce QuIP#, a weight-only PTQ method that achieves state-of-the-art results in extreme compression regimes ($\le$ 4 bits per weight) using three novel techniques. First, QuIP# improves QuIP’s (Chee et al., 2023) incoherence processing by using the randomized Hadamard transform, which is faster and has better theoretical properties. Second, QuIP# uses vector quantization to take advantage of the ball-shaped sub-Gaussian distribution that incoherent weights possess: specifically, we introduce a set of hardware-efficient codebooks based on the highly symmetric $E_8$ lattice, which achieves the optimal 8-dimension unit ball packing. Third, QuIP# uses fine-tuning to improve fidelity to the original model. Our experiments show that QuIP# outperforms existing PTQ methods, enables new behaviors in PTQ scaling, and supports fast inference. Our code can be found at https://github.com/Cornell-RelaxML/quip-sharp.