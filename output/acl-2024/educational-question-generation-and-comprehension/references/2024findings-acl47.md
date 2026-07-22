---
title: "Unsupervised Distractor Generation via Large Language Model Distilling and Counterfactual Contrastive Decoding"
source: "https://aclanthology.org/2024.findings-acl.47/"
pdf_url: ""
categories: ['educational-question-generation-and-comprehension', 'llm-training-alignment-and-evaluation']
tags: ['distractor-generation', 'counterfactual-decoding', 'reading-comprehension']
venue: "ACL 2024"
tldr: "Proposes an unsupervised distractor generation method using LLM distillation and counterfactual contrastive decoding for reading comprehension."
---

# Unsupervised Distractor Generation via Large Language Model Distilling and Counterfactual Contrastive Decoding

**Source**: [https://aclanthology.org/2024.findings-acl.47/](https://aclanthology.org/2024.findings-acl.47/)

**TLDR**: Proposes an unsupervised distractor generation method using LLM distillation and counterfactual contrastive decoding for reading comprehension.

## Abstract

AbstractWithin the context of reading comprehension, the task of Distractor Generation (DG) aims to generate several incorrect options to confuse readers. In recent years, the emergence of Large Language Models (LLMs) provides a potential for unsupervised DG without expensive human-annotated distractor labels. In this paper, we leverage LLMs as a cost-effective annotator to enhance the DG capability of smaller student models. To perform knowledge distilling, we propose a dual task training framework that integrates pseudo distractors from LLMs and answer information as the objective target with a two-stage training process. Moreover, we devise a counterfactual contrastive decoding mechanism for increasing the distracting capability of the DG model. Experiments show that our unsupervised generation method with Bart-base greatly surpasses GPT-3.5-turbo zero-shot performance with only 200× fewer model parameters. Our proposed unsupervised DG method offers a cost-effective framework for practical reading comprehension applications, without the need of laborious distractor annotation and costly large-size models.