---
title: "Token Alignment via Character Matching for Subword Completion"
source: "https://aclanthology.org/2024.findings-acl.929/"
pdf_url: ""
categories: ['language-model-representations-and-embedding-spaces', 'llm-training-alignment-and-evaluation']
tags: ['tokenization', 'subword', 'partial-token']
venue: "ACL 2024"
tldr: "Proposes a token alignment method via character matching to handle partial-token prompts that fall out of distribution during inference in generative models."
---

# Token Alignment via Character Matching for Subword Completion

**Source**: [https://aclanthology.org/2024.findings-acl.929/](https://aclanthology.org/2024.findings-acl.929/)

**TLDR**: Proposes a token alignment method via character matching to handle partial-token prompts that fall out of distribution during inference in generative models.

## Abstract

AbstractGenerative models, widely utilized in various applications, can often struggle with prompts corresponding to partial tokens. This struggle stems from tokenization, where partial tokens fall out of distribution during inference, leading to incorrect or nonsensical outputs. This paper examines a technique to alleviate the tokenization artifact on text completion in generative models, maintaining performance even in regular non-subword cases. The method, termed token alignment, involves backtracking to the last complete tokens and ensuring the model’s generation aligns with the prompt. This approach showcases marked improvement across many partial token scenarios, including nuanced cases like space-prefix and partial indentation, with only a minor time increase. The technique and analysis detailed in this paper contribute to the continuous advancement of generative models in handling partial inputs, bearing relevance for applications like code completion and text.