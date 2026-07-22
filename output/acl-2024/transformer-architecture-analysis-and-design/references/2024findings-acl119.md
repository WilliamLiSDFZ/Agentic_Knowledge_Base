---
title: "LoRA Meets Dropout under a Unified Framework"
source: "https://aclanthology.org/2024.findings-acl.119/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'transformer-architecture-analysis-and-design']
tags: ['LoRA', 'dropout', 'parameter-efficient-finetuning', 'regularization', 'unified-framework']
venue: "ACL 2024"
tldr: "Presents a unified framework that integrates LoRA with various dropout techniques for improved parameter-efficient LLM fine-tuning."
---

# LoRA Meets Dropout under a Unified Framework

**Source**: [https://aclanthology.org/2024.findings-acl.119/](https://aclanthology.org/2024.findings-acl.119/)

**TLDR**: Presents a unified framework that integrates LoRA with various dropout techniques for improved parameter-efficient LLM fine-tuning.

## Abstract

AbstractWith the remarkable capabilities, large language models (LLMs) have emergedas essential elements in numerous NLP applications, while parameter-efficientfinetuning, especially LoRA, has gained popularity as a lightweight approachfor model customization. Meanwhile, various dropout methods, initially designedfor full finetuning with all the parameters updated, alleviates overfittingassociated with excessive parameter redundancy. Hence, a possible contradictionarises from negligible trainable parameters of LoRA and the effectiveness ofprevious dropout methods, which has been largely overlooked. To fill this gap,we first confirm that parameter-efficient LoRA is also overfitting-prone. Wethen revisit transformer-specific dropout methods, and establish theirequivalence and distinctions mathematically and empirically. Building upon thiscomparative analysis, we introduce a unified framework for a comprehensiveinvestigation, which instantiates these methods based on dropping position,structural pattern and compensation measure. Through this framework, we revealthe new preferences and performance comparisons of them when involved withlimited trainable parameters. This framework also allows us to amalgamate themost favorable aspects into a novel dropout method named HiddenKey. Extensiveexperiments verify the remarkable superiority and sufficiency of HiddenKeyacross multiple models and tasks, which highlights it as the preferred approachfor high-performance and parameter-efficient finetuning of LLMs.