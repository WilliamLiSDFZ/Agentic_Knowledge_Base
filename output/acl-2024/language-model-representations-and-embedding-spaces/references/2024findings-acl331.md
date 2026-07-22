---
title: "SSS: Editing Factual Knowledge in Language Models towards Semantic Sparse Space"
source: "https://aclanthology.org/2024.findings-acl.331/"
pdf_url: ""
categories: ['continual-learning-for-nlp-tasks', 'language-model-representations-and-embedding-spaces']
tags: ['knowledge-editing', 'sparse-representation', 'factual-updates']
venue: "ACL 2024"
tldr: "SSE edits factual knowledge in language models by steering updates toward semantically sparse representation spaces."
---

# SSS: Editing Factual Knowledge in Language Models towards Semantic Sparse Space

**Source**: [https://aclanthology.org/2024.findings-acl.331/](https://aclanthology.org/2024.findings-acl.331/)

**TLDR**: SSE edits factual knowledge in language models by steering updates toward semantically sparse representation spaces.

## Abstract

AbstractLanguage Models (LMs) acquire factual knowledge during pre-training and store it in the parameters, which can be valuable for downstream tasks. As world evolves, some facts may be incorrectly induced or become obsolete over time. Various model editing methods have been proposed to modify specific examples in LMs. However, existing training-based methods still suffer from sub-optimal locality, where irrelevant neighborhood examples can be adversely influenced. Model’s gradients are still struggling to identify the appropriate direction when updating the parameters. To address this issue, we find that directing the hidden state of the edit example towards spaces where semantics are sparse tends to help preserve the semantics of irrelevant neighborhood examples. Based on this hypothesis, we propose a novel metric, named SSS, to evaluate the degree of sparsity around a sentence embedding in the semantic space without any human or machine annotation. Subsequently, we incorporate SSS into the original loss function of the existing training-based methods to enhance locality. Experiments conducted on two datasets across various models demonstrate that SSS is effective in improving both locality and reasoning capability.