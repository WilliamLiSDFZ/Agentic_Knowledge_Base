---
title: "Large Language Models Relearn Removed Concepts"
source: "https://aclanthology.org/2024.findings-acl.492/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'continual-learning-for-nlp-tasks']
tags: ['concept-relearning', 'neuron-pruning', 'model-editing']
venue: "ACL 2024"
tldr: "Models that have concepts removed via neuron pruning can reacquire those concepts after fine-tuning, undermining the effectiveness of editing-based safety interventions."
---

# Large Language Models Relearn Removed Concepts

**Source**: [https://aclanthology.org/2024.findings-acl.492/](https://aclanthology.org/2024.findings-acl.492/)

**TLDR**: Models that have concepts removed via neuron pruning can reacquire those concepts after fine-tuning, undermining the effectiveness of editing-based safety interventions.

## Abstract

AbstractAdvances in model editing through neuron pruning hold promise for removing undesirable concepts from large language models. However, it remains unclear whether models have the capacity to reacquire pruned concepts after editing. To investigate this, we evaluate concept relearning in models by tracking concept saliency and similarity in pruned neurons during retraining for named entity recognition tasks. Our findings reveal that models can quickly regain performance post-pruning by relocating advanced concepts to earlier layers and reallocating pruned concepts to primed neurons with similar semantics. This suggests that models exhibit polysemantic capacities and can blend old and new concepts in individual neurons. While neuron pruning provides interpretability into model concepts, our results highlight the challenges of permanent concept removal for improved model *safety*. Monitoring concept reemergence and developing techniques to mitigate relearning of unsafe concepts will be important directions for more robust model editing. Overall, our work strongly demonstrates the resilience and fluidity of concept representations in LLMs post concept removal.