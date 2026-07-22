---
title: "SLIDE: A Framework Integrating Small and Large Language Models for Open-Domain Dialogues Evaluation"
source: "https://aclanthology.org/2024.findings-acl.911/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'emotion-aware-dialogue-and-empathy-systems']
tags: ['dialogue-evaluation', 'open-domain', 'LLM-judge']
venue: "ACL 2024"
tldr: "SLIDE combines small and large language models to better evaluate open-domain dialogue by addressing the one-to-many response problem."
---

# SLIDE: A Framework Integrating Small and Large Language Models for Open-Domain Dialogues Evaluation

**Source**: [https://aclanthology.org/2024.findings-acl.911/](https://aclanthology.org/2024.findings-acl.911/)

**TLDR**: SLIDE combines small and large language models to better evaluate open-domain dialogue by addressing the one-to-many response problem.

## Abstract

AbstractThe long-standing one-to-many problem of gold standard responses in open-domain dialogue systems presents challenges for automatic evaluation metrics. Though prior works have demonstrated some success by applying powerful Large Language Models (LLMs), existing approaches still struggle with the one-to-many problem, and exhibit subpar performance in domain-specific scenarios. We assume the commonsense reasoning biases within LLMs may hinder their performance in domain-specific evaluations. To address both issues, we propose a novel framework SLIDE (Small and Large Integrated for Dialogue Evaluation), that leverages both a small, specialised model (SLM), and LLMs for the evaluation of open domain dialogues. Our approach introduces several techniques: (1) Contrastive learning to differentiate between robust and non-robust response embeddings; (2) A novel metric for semantic sensitivity that combines embedding cosine distances with similarity learned through neural networks, and (3) A strategy for incorporating the evaluation results from both the SLM and LLMs. Our empirical results demonstrate that our approach achieves state-of-the-art performance in both the classification and evaluation tasks, and additionally the SLIDE evaluator exhibits better correlation with human judgements. Our code is available at https://github.com/hegehongcha/SLIDE-ACL2024.