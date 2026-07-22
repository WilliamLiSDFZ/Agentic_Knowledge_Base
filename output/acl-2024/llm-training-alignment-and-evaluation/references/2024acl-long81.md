---
title: "Feature-Adaptive and Data-Scalable In-Context Learning"
source: "https://aclanthology.org/2024.acl-long.81/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'language-model-representations-and-embedding-spaces']
tags: ['in-context-learning', 'feature-adaptation', 'data-scaling', 'demonstration-selection', 'LLM']
venue: "ACL 2024"
tldr: "Proposes feature-adaptive and data-scalable in-context learning to overcome context length constraints and improve ICL with more training data."
---

# Feature-Adaptive and Data-Scalable In-Context Learning

**Source**: [https://aclanthology.org/2024.acl-long.81/](https://aclanthology.org/2024.acl-long.81/)

**TLDR**: Proposes feature-adaptive and data-scalable in-context learning to overcome context length constraints and improve ICL with more training data.

## Abstract

AbstractIn-context learning (ICL), which promotes inference with several demonstrations, has become a widespread paradigm to stimulate LLM capabilities for downstream tasks. Due to context length constraints, it cannot be further improved in spite of more training data, and general features directly from LLMs in ICL are not adaptive to the specific downstream task. In this paper, we propose a feature-adaptive and data-scalable in-context learning framework (FADS-ICL), which can leverage task-adaptive features to promote inference on the downstream task, with the supervision of beyond-context samples.Specifically, it first extracts general features of beyond-context samples via the LLM with ICL input form one by one, and introduces a task-specific modulator to perform feature refinement and prediction after fitting a specific downstream task. We conduct extensive experiments on FADS-ICL under varying data settings (4~128 shots) and LLM scale (0.8~70B) settings. Experimental results show that FADS-ICL consistently outperforms previous state-of-the-art methods by a significant margin under all settings, verifying the effectiveness and superiority of FADS-ICL. For example, under the 1.5B and 32 shots setting, FADS-ICL can achieve +14.3 average accuracy from feature adaptation over vanilla ICL on 10 datasets, with +6.2 average accuracy over the previous state-of-the-art method, and the performance can further improve with increasing training data.