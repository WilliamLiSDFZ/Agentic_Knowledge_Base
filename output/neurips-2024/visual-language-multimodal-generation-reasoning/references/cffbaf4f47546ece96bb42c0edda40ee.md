---
title: "Q-VLM: Post-training Quantization for Large Vision-Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/cffbaf4f47546ece96bb42c0edda40ee-Abstract-Conference.html"
categories: ['visual-language-multimodal-generation-reasoning']
tags: ['quantization', 'vision-language-models', 'post-training', 'efficient-inference', 'multimodal']
venue: "NeurIPS 2024"
tldr: "Q-VLM proposes a post-training quantization framework for large vision-language models that jointly optimizes layer-wise rounding to minimize inference costs."
---

# Q-VLM: Post-training Quantization for Large Vision-Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/cffbaf4f47546ece96bb42c0edda40ee-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/cffbaf4f47546ece96bb42c0edda40ee-Abstract-Conference.html)

**TLDR**: Q-VLM proposes a post-training quantization framework for large vision-language models that jointly optimizes layer-wise rounding to minimize inference costs.

## Abstract

In this paper, we propose a post-training quantization framework of large vision-language models (LVLMs) for efficient multi-modal inference. Conventional quantization methods sequentially search the layer-wise rounding functions by minimizing activation discretization errors, which fails to acquire optimal quantization strategy without considering cross-layer dependency. On the contrary, we mine the cross-layer dependency that significantly influences discretization errors of the entire vision-language model, and embed this dependency into optimal quantization strategy searching with low search cost. Specifically, we observe the strong correlation between the activation entropy and the cross-layer dependency concerning output discretization errors. Therefore, we employ the entropy as the proxy to partition blocks optimally, which aims to achieve satisfying trade-offs between discretization errors and the search cost. Moreover, we optimize the visual encoder to disentangle the cross-layer dependency for fine-grained decomposition of search space, so that the search cost is further reduced without harming the quantization accuracy. Experimental results demonstrate that our method compresses the memory by 2.78x and increase generate speed by 1.44x about 13B LLaVA model without performance degradation on diverse multi-modal reasoning tasks.