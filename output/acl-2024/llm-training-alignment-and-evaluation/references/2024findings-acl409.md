---
title: "Learning to Maximize Mutual Information for Chain-of-Thought Distillation"
source: "https://aclanthology.org/2024.findings-acl.409/"
categories: ['llm-training-alignment-and-evaluation']
tags: ['knowledge-distillation', 'chain-of-thought', 'mutual-information']
venue: "ACL 2024"
tldr: "Proposes maximizing mutual information between rationales and labels to improve chain-of-thought distillation from large to small models."
---

# Learning to Maximize Mutual Information for Chain-of-Thought Distillation

**Source**: [https://aclanthology.org/2024.findings-acl.409/](https://aclanthology.org/2024.findings-acl.409/)

**TLDR**: Proposes maximizing mutual information between rationales and labels to improve chain-of-thought distillation from large to small models.

## Abstract

AbstractKnowledge distillation, the technique of transferring knowledge from large, complex models to smaller ones, marks a pivotal step towards efficient AI deployment. Distilling Step-by-Step (DSS), a novel method utilizing chain-of-thought (CoT) distillation, has demonstrated promise by imbuing smaller models with the superior reasoning capabilities of their larger counterparts. In DSS, the distilled model acquires the ability to generate rationales and predict labels concurrently through a multi-task learning framework. However, DSS overlooks the intrinsic relationship between the two training tasks, leading to ineffective integration of CoT knowledge with the task of label prediction. To this end, we investigate the mutual relationship of the two tasks from Information Bottleneck perspective and formulate it as maximizing the mutual information of the representation features of the two tasks. We propose a variational approach to solve this optimization problem using a learning-based method. Our experimental results across four datasets demonstrate that our method outperforms the state-of-the-art DSS. Our findings offer insightful guidance for future research on language model distillation as well as applications involving CoT. Codes are available at https://github.com/xinchen9/cot_distillation_ACL2024.