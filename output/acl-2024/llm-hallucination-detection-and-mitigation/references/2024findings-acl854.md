---
title: "Unsupervised Real-Time Hallucination Detection based on the Internal States of Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.854/"
categories: ['llm-hallucination-detection-and-mitigation']
tags: ['hallucination-detection', 'internal-states', 'real-time', 'unsupervised']
venue: "ACL 2024"
tldr: "Proposes an unsupervised real-time hallucination detection method based on monitoring the internal states of LLMs."
---

# Unsupervised Real-Time Hallucination Detection based on the Internal States of Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.854/](https://aclanthology.org/2024.findings-acl.854/)

**TLDR**: Proposes an unsupervised real-time hallucination detection method based on monitoring the internal states of LLMs.

## Abstract

AbstractHallucinations in large language models (LLMs) refer to the phenomenon of LLMs producing responses that are coherent yet factually inaccurate. This issue undermines the effectiveness of LLMs in practical applications, necessitating research into detecting and mitigating hallucinations of LLMs. Previous studies have mainly concentrated on post-processing techniques for hallucination detection, which tend to be computationally intensive and limited in effectiveness due to their separation from the LLM’s inference process. To overcome these limitations, we introduce MIND, an unsupervised training framework that leverages the internal states of LLMs for real-time hallucination detection without requiring manual annotations. Additionally, we present HELM, a new benchmark for evaluating hallucination detection across multiple LLMs, featuring diverse LLM outputs and the internal states of LLMs during their inference process. Our experiments demonstrate that MIND outperforms existing state-of-the-art methods in hallucination detection.