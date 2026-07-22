---
title: "When Do LLMs Need Retrieval Augmentation? Mitigating LLMs’ Overconfidence Helps Retrieval Augmentation"
source: "https://aclanthology.org/2024.findings-acl.675/"
pdf_url: ""
categories: ['llm-hallucination-detection-and-mitigation', 'llm-training-alignment-and-evaluation']
tags: ['retrieval-augmentation', 'hallucination-mitigation', 'overconfidence']
venue: "ACL 2024"
tldr: "Addresses LLM overconfidence to determine when retrieval augmentation is necessary for reducing hallucinations."
---

# When Do LLMs Need Retrieval Augmentation? Mitigating LLMs’ Overconfidence Helps Retrieval Augmentation

**Source**: [https://aclanthology.org/2024.findings-acl.675/](https://aclanthology.org/2024.findings-acl.675/)

**TLDR**: Addresses LLM overconfidence to determine when retrieval augmentation is necessary for reducing hallucinations.

## Abstract

AbstractLarge Language Models (LLMs) have been found to have difficulty knowing they do not possess certain knowledge and tend to provide specious answers in such cases. Retrieval Augmentation (RA) has been extensively studied to mitigate LLMs’ hallucinations. However, due to the extra overhead and unassured quality of retrieval, it may not be optimal to conduct RA all the time. A straightforward idea is to only conduct retrieval when LLMs are uncertain about a question. This motivates us to enhance the LLMs’ ability to perceive their knowledge boundaries to help RA. In this paper, we first quantitatively measure LLMs’ such ability and confirm their overconfidence. Then, we study how LLMs’ certainty about a question correlates with their dependence on external retrieved information. We propose several methods to enhance LLMs’ perception of knowledge boundaries and show that they are effective in reducing overconfidence. Additionally, equipped with these methods, LLMs can achieve comparable or even better performance of RA with much fewer retrieval calls.