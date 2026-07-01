---
title: "DeepStack: Deeply Stacking Visual Tokens is Surprisingly Simple and Effective for LMMs"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/29cd7f8331d13ede6dc6d6ef3dfacb70-Abstract-Conference.html"
categories: ['visual-language-multimodal-generation-reasoning', 'llm-training-and-optimization-techniques']
tags: ['visual-token-compression', 'large-multimodal-models', 'deep-stacking']
venue: "NeurIPS 2024"
tldr: "DeepStack reduces computation in large multimodal models by deeply stacking visual tokens across LLM layers rather than feeding all tokens at the first layer."
---

# DeepStack: Deeply Stacking Visual Tokens is Surprisingly Simple and Effective for LMMs

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/29cd7f8331d13ede6dc6d6ef3dfacb70-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/29cd7f8331d13ede6dc6d6ef3dfacb70-Abstract-Conference.html)

**TLDR**: DeepStack reduces computation in large multimodal models by deeply stacking visual tokens across LLM layers rather than feeding all tokens at the first layer.

## Abstract

Most large multimodal models (LMMs) are implemented by feeding visual tokens as a sequence into the first layer of a large language model (LLM). The resulting architecture is simple but significantly increases computation and memory costs, as it has to handle a large number of additional tokens in its input layer. This paper presents a new architecture *DeepStack* for LMMs. Considering $N$ layers in the language and vision transformer of LMMs, we stack the visual tokens into $N$ groups and feed each group to its aligned transformer layer from bottom to top. Surprisingly, this simple method greatly enhances the power of LMMs to model interactions among visual tokens across layers but with minimal additional cost. We apply *DeepStack* to both language and vision transformer in LMMs, and validate the effectiveness of *DeepStack* LMMs with extensive empirical results. Using the same context length, our DeepStack 7B and 13B parameters surpass their counterparts by 2.7 and 2.9 on average across 9 benchmarks, respectively. Using only one-fifth of the context length, DeepStack rivals closely to the counterparts that use the full context length. These gains are particularly pronounced on high-resolution tasks, *e.g.*, 4.2, 11.0, and 4.0 improvements on TextVQA, DocVQA, and InfoVQA compared to LLaVA-1.5-7B, respectively. We further apply *DeepStack* to vision transformer layers, which brings us a similar amount of improvements, 3.8 on average compared with LLaVA-1.5-7B.