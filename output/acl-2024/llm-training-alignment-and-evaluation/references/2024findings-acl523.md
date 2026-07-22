---
title: "Revisiting Parallel Context Windows: A Frustratingly Simple Alternative and Chain-of-Thought Deterioration"
source: "https://aclanthology.org/2024.findings-acl.523/"
categories: ['llm-training-alignment-and-evaluation']
tags: ['parallel-context-windows', 'long-context', 'chain-of-thought', 'evaluation']
venue: "ACL 2024"
tldr: "This paper exposes evaluation limitations of Parallel Context Windows and shows chain-of-thought reasoning deteriorates under this method."
---

# Revisiting Parallel Context Windows: A Frustratingly Simple Alternative and Chain-of-Thought Deterioration

**Source**: [https://aclanthology.org/2024.findings-acl.523/](https://aclanthology.org/2024.findings-acl.523/)

**TLDR**: This paper exposes evaluation limitations of Parallel Context Windows and shows chain-of-thought reasoning deteriorates under this method.

## Abstract

AbstractWe identify two crucial limitations in the evaluation of recent parallel-integrated method Parallel Context Windows (PCW), which extends the maximum context lengths of language models, e.g., 2048 for LLaMA, by harnessing window-wise attention and positional embedding techniques. We first show that a simple yet strong baseline, weighted sum ensemble, is missing for the in-context few-shot classification. Moreover, on more challenging Chain-of-Thought (CoT) reasoning (e.g., HotpotQA), PCW would present unexpected deterioration regarding question miscomprehension and false inference. Based on our findings, we suggest that the existing PCW design may not guarantee sufficient improvement and practicality in handling lengthy documents in real-world applications. More community efforts on enabling language models’ long context understanding ability should be paid.