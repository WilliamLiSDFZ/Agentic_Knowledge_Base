---
title: "Flexible Weight Tuning and Weight Fusion Strategies for Continual Named Entity Recognition"
source: "https://aclanthology.org/2024.findings-acl.79/"
pdf_url: ""
categories: ['continual-learning-for-nlp-tasks', 'natural-language-processing-information-extraction']
tags: ['continual-learning', 'named-entity-recognition', 'catastrophic-forgetting', 'weight-fusion', 'knowledge-distillation']
venue: "ACL 2024"
tldr: "Proposes flexible weight tuning and fusion strategies for continual named entity recognition to mitigate catastrophic forgetting of old entity types."
---

# Flexible Weight Tuning and Weight Fusion Strategies for Continual Named Entity Recognition

**Source**: [https://aclanthology.org/2024.findings-acl.79/](https://aclanthology.org/2024.findings-acl.79/)

**TLDR**: Proposes flexible weight tuning and fusion strategies for continual named entity recognition to mitigate catastrophic forgetting of old entity types.

## Abstract

AbstractContinual Named Entity Recognition (CNER) is dedicated to sequentially learning new entity types while mitigating catastrophic forgetting of old entity types. Traditional CNER approaches commonly employ knowledge distillation to retain old knowledge within the current model. However, because only the representations of old and new models are constrained to be consistent, the reliance solely on distillation in existing methods still suffers from catastrophic forgetting. To further alleviate the forgetting issue of old entity types, this paper introduces flexible Weight Tuning (WT) and Weight Fusion (WF) strategies for CNER. The WT strategy, applied at each training step, employs a learning rate schedule on the parameters of the current model. After learning the current task, the WF strategy dynamically integrates knowledge from both the current and previous models for inference. Notably, these two strategies are model-agnostic and seamlessly integrate with existing State-Of-The-Art (SOTA) models. Extensive experiments demonstrate that the WT and WF strategies consistently enhance the performance of previous SOTA methods across ten CNER settings in three datasets.