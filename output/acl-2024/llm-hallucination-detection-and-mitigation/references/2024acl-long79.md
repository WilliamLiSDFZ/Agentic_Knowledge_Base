---
title: "Citation-Enhanced Generation for LLM-based Chatbots"
source: "https://aclanthology.org/2024.acl-long.79/"
pdf_url: ""
categories: ['llm-hallucination-detection-and-mitigation', 'natural-language-processing-information-extraction']
tags: ['hallucination-mitigation', 'citation-grounding', 'llm-chatbots']
venue: "ACL 2024"
tldr: "A citation-enhanced generation framework reduces hallucinated content in LLM-based chatbots by grounding responses with retrieved citations."
---

# Citation-Enhanced Generation for LLM-based Chatbots

**Source**: [https://aclanthology.org/2024.acl-long.79/](https://aclanthology.org/2024.acl-long.79/)

**TLDR**: A citation-enhanced generation framework reduces hallucinated content in LLM-based chatbots by grounding responses with retrieved citations.

## Abstract

AbstractLarge language models (LLMs) exhibit powerful general intelligence across diverse scenarios, including their integration into chatbots. However, a vital challenge of LLM-based chatbots is that they may produce hallucinated content in responses, which significantly limits their applicability. Various efforts have been made to alleviate hallucination, such as retrieval augmented generation and reinforcement learning with human feedback, but most of them require additional training and data annotation. In this paper, we propose a novel post-hoc Citation-Enhanced Generation (CEG) approach combined with retrieval argumentation. Unlike previous studies that focus on preventing hallucinations during generation, our method addresses this issue in a post-hoc way. It incorporates a retrieval module to search for supporting documents relevant to the generated content, and employs a natural language inference-based citation generation module. Once the statements in the generated content lack of reference, our model can regenerate responses until all statements are supported by citations. Note that our method is a training-free plug-and-play plugin that is capable of various LLMs. Experiments on various hallucination-related datasets show our framework outperforms state-of-the-art methods in both hallucination detection and response regeneration on three benchmarks. Our code and datasets can be found at https://github.com/Tsinghua-dhy/CEG.