---
title: "ELAD: Explanation-Guided Large Language Models Active Distillation"
source: "https://aclanthology.org/2024.findings-acl.264/"
categories: ['llm-training-alignment-and-evaluation', 'collaborative-llm-deployment-and-inference-optimization']
tags: ['knowledge-distillation', 'LLM', 'active-learning', 'explanation-guided', 'model-compression']
venue: "ACL 2024"
tldr: "Proposes an explanation-guided active distillation framework to more effectively transfer LLM capabilities to smaller student models."
---

# ELAD: Explanation-Guided Large Language Models Active Distillation

**Source**: [https://aclanthology.org/2024.findings-acl.264/](https://aclanthology.org/2024.findings-acl.264/)

**TLDR**: Proposes an explanation-guided active distillation framework to more effectively transfer LLM capabilities to smaller student models.

## Abstract

AbstractThe deployment and application of Large Language Models (LLMs) is hindered by their memory inefficiency, computational demands, and the high costs of API inferences. Traditional distillation methods, which transfer the capabilities of LLMs to smaller models, often fail to determine whether the knowledge has been sufficiently transferred, potentially resulting in high costs or incomplete distillation. In this paper, we propose an Explanation-Guided LLMs Active Distillation (ELAD) framework that employs an active learning strategy to optimize the balance between annotation costs and model performance. To improve the efficiency of sample selection, we introduce an explanation-guided sample selection method that identifies samples challenging its reasoning by exploiting uncertainties in reasoning explanation steps. Additionally, we present a customized LLM-annotated explanation revision technique where the teacher model detects and corrects flaws in the student model’s reasoning. Our experiments across various reasoning datasets demonstrate that our framework significantly enhances the efficiency of LLMs knowledge distillation.