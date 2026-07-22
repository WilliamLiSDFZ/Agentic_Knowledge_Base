---
title: "DATA-CUBE: Data Curriculum for Instruction-based Sentence Representation Learning"
source: "https://aclanthology.org/2024.findings-acl.816/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'language-model-representations-and-embedding-spaces']
tags: ['sentence-representation', 'instruction-tuning', 'data-curriculum', 'multi-task', 'contrastive-learning']
venue: "ACL 2024"
tldr: "Proposes DATA-CUBE, a data curriculum strategy for multi-task instruction-based sentence representation learning to improve generalization."
---

# DATA-CUBE: Data Curriculum for Instruction-based Sentence Representation Learning

**Source**: [https://aclanthology.org/2024.findings-acl.816/](https://aclanthology.org/2024.findings-acl.816/)

**TLDR**: Proposes DATA-CUBE, a data curriculum strategy for multi-task instruction-based sentence representation learning to improve generalization.

## Abstract

AbstractRecently, multi-task instruction tuning has been utilized to improve sentence representation learning (SRL). It enables SRL models to generate task-specific representations with the guidance of task instruction, thus exhibiting strong generalization ability on unseen tasks. However, these methods mostly neglect the potential interference problems across different tasks and instances, which may affect the training of the model.To address this issue, we propose a data curriculum method, namely **Data-CUBE**, that arranges the order of all the multi-task data for training, to minimize the interference risks from two aspects.At the task level, we aim to find the optimal task order to minimize the total cross-task interference risk and formulate this problem as the traveling salesman problem, which is further solved by a specially designed simulated annealing algorithm. At the instance level, we propose a measurement method to quantify the difficulty of all instances per task, and then arrange instances in an easy-to-difficult order for training.Experimental results show that our approach can boost the performance of state-of-the-art methods. Our code and data will be publicly released.