---
title: "MediSwift: Efficient Sparse Pre-trained Biomedical Language Models"
source: "https://aclanthology.org/2024.findings-acl.14/"
pdf_url: ""
categories: ['llms-for-biomedical-and-clinical-nlp', 'llm-training-alignment-and-evaluation']
tags: ['biomedical-nlp', 'sparse-pretraining', 'domain-specific-llm', 'efficient-language-models', 'biomedicine']
venue: "ACL 2024"
tldr: "MediSwift introduces efficient sparse pre-trained biomedical language models that reduce computational costs while maintaining strong domain-specific performance."
---

# MediSwift: Efficient Sparse Pre-trained Biomedical Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.14/](https://aclanthology.org/2024.findings-acl.14/)

**TLDR**: MediSwift introduces efficient sparse pre-trained biomedical language models that reduce computational costs while maintaining strong domain-specific performance.

## Abstract

AbstractLarge language models (LLMs) are typically trained on general source data forvarious domains, but a recent surge in domain-specific LLMs has shown theirpotential to outperform general-purpose models in domain-specific tasks (e.g.,biomedicine). Although domain-specific pre-training enhances efficiency andleads to smaller models, the computational costs of training these LLMs remainhigh, posing budgeting challenges. We introduce MediSwift, a suite of biomedicalLMs that leverage sparse pre-training on domain-specific biomedical text data.By inducing up to 75% weight sparsity during the pre-training phase, MediSwiftachieves a 2-2.5x reduction in training FLOPs. Notably, all sparse pre-trainingwas performed on the Cerebras CS-2 system, which is specifically designed torealize the acceleration benefits from unstructured weight sparsity, therebysignificantly enhancing the efficiency of the MediSwift models. Throughsubsequent dense fine-tuning and strategic soft prompting, MediSwift modelsoutperform existing LLMs up to 7B parameters on biomedical tasks, setting newbenchmarks w.r.t efficiency-accuracy on tasks such as PubMedQA. Our results showthat sparse pre-training, along with dense fine-tuning and soft prompting,offers an effective method for creating high-performing, computationallyefficient models in specialized domains.