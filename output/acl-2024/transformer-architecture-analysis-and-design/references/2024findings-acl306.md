---
title: "Extending Context Window of Large Language Models via Semantic Compression"
source: "https://aclanthology.org/2024.findings-acl.306/"
pdf_url: ""
categories: ['transformer-architecture-analysis-and-design']
tags: ['context-window-extension', 'semantic-compression', 'long-text', 'transformer']
venue: "ACL 2024"
tldr: "Proposes semantic compression to extend the effective context window of transformer-based LLMs for long-text scenarios."
---

# Extending Context Window of Large Language Models via Semantic Compression

**Source**: [https://aclanthology.org/2024.findings-acl.306/](https://aclanthology.org/2024.findings-acl.306/)

**TLDR**: Proposes semantic compression to extend the effective context window of transformer-based LLMs for long-text scenarios.

## Abstract

AbstractTransformer based Large Language Models (LLMs) often impose limitations on the length of the text input to ensure the generation of fluent and relevant responses due to the quadratic complexity. These constraints restrict their applicability in long text scenarios. In this paper, we propose a novel semantic compression method that enables generalization to texts that are 6-8 times longer without incurring significant computational costs or requiring fine-tuning. Our proposed framework draws inspiration from source coding in information theory and employs a pre-trained model to reduce the semantic redundancy of long inputs before passing them to the LLMs for downstream tasks. Experimental results demonstrate that our method effectively extends the context window of LLMs across a range of tasks including question answering, summarization, few-shot learning, and information retrieval. Furthermore, the proposed semantic compression method exhibits consistent fluency in text generation while reducing the associated computational overhead.