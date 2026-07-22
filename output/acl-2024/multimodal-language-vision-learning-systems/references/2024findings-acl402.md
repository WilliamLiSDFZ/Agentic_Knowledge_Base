---
title: "VISREAS: Complex Visual Reasoning with Unanswerable Questions"
source: "https://aclanthology.org/2024.findings-acl.402/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems']
tags: ['visual-reasoning', 'unanswerable-questions', 'VQA']
venue: "ACL 2024"
tldr: "VISREAS is a benchmark for complex visual reasoning that requires models to identify and communicate unanswerable questions."
---

# VISREAS: Complex Visual Reasoning with Unanswerable Questions

**Source**: [https://aclanthology.org/2024.findings-acl.402/](https://aclanthology.org/2024.findings-acl.402/)

**TLDR**: VISREAS is a benchmark for complex visual reasoning that requires models to identify and communicate unanswerable questions.

## Abstract

AbstractVerifying a question’s validity before answering is crucial in real-world applications, where users may provide imperfect instructions. In this scenario, an ideal model should address the discrepancies in the query and convey them to the users rather than generating the best possible answer. Addressing this requirement, we introduce a new compositional visual question-answering dataset, VisReas, that consists of answerable and unanswerable visual queries formulated by traversing and perturbing commonalities and differences among objects, attributes, and relations. VisReas contains 2.07M semantically diverse queries generated automatically using Visual Genome scene graphs. The unique feature of this task, validating question answerability with respect to an image before answering, and the poor performance of state-of-the-art models inspired the design of a new modular baseline, Logic2Vision that reasons by producing and executing pseudocode without any external modules to generate the answer. Logic2Vision outperforms generative models in VisReas (+4.82% over LLaVA-1.5; +12.23% over InstructBLIP) and achieves a significant gain in performance against the classification models.