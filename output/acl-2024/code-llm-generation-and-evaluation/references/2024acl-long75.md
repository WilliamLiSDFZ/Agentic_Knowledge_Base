---
title: "Rewriting the Code: A Simple Method for Large Language Model Augmented Code Search"
source: "https://aclanthology.org/2024.acl-long.75/"
pdf_url: ""
categories: ['code-llm-generation-and-evaluation']
tags: ['code-search', 'generation-augmented-retrieval', 'query-augmentation', 'modality-alignment']
venue: "ACL 2024"
tldr: "Proposes rewriting natural language queries into code-like forms to improve LLM-augmented code search via generation-augmented retrieval."
---

# Rewriting the Code: A Simple Method for Large Language Model Augmented Code Search

**Source**: [https://aclanthology.org/2024.acl-long.75/](https://aclanthology.org/2024.acl-long.75/)

**TLDR**: Proposes rewriting natural language queries into code-like forms to improve LLM-augmented code search via generation-augmented retrieval.

## Abstract

AbstractIn code search, the Generation-Augmented Retrieval (GAR) framework, which generates exemplar code snippets to augment queries, has emerged as a promising strategy to address the principal challenge of modality misalignment between code snippets and natural language queries, particularly with the demonstrated code generation capabilities of Large Language Models (LLMs). Nevertheless, our preliminary investigations indicate that the improvements conferred by such an LLM-augmented framework are somewhat constrained. This limitation could potentially be ascribed to the fact that the generated codes, albeit functionally accurate, frequently display a pronounced stylistic deviation from the ground truth code in the codebase. In this paper, we extend the foundational GAR framework and propose a simple yet effective method that additionally Rewrites the Code (ReCo) within the codebase for style normalization. Experimental results demonstrate that ReCo significantly boosts retrieval accuracy across sparse (up to 35.7%), zero-shot dense (up to 27.6%), and fine-tuned dense (up to 23.6%) retrieval settings in diverse search scenarios. To further elucidate the advantages of ReCo and stimulate research in code style normalization, we introduce Code Style Similarity, the first metric tailored to quantify stylistic similarities in code. Notably, our empirical findings reveal the inadequacy of existing metrics in capturing stylistic nuances. The source code and data are available at https://github.com/Alex-HaochenLi/ReCo.