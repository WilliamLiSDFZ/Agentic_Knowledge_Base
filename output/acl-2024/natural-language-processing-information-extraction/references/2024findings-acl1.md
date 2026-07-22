---
title: "Controllable Data Augmentation for Few-Shot Text Mining with Chain-of-Thought Attribute Manipulation"
source: "https://aclanthology.org/2024.findings-acl.1/"
pdf_url: ""
categories: ['text-clustering-with-limited-labels', 'natural-language-processing-information-extraction']
tags: ['data-augmentation', 'few-shot-learning', 'chain-of-thought']
venue: "ACL 2024"
tldr: "CoTAM uses chain-of-thought attribute manipulation to generate augmented training data for few-shot NLP tasks via LLM prompting."
---

# Controllable Data Augmentation for Few-Shot Text Mining with Chain-of-Thought Attribute Manipulation

**Source**: [https://aclanthology.org/2024.findings-acl.1/](https://aclanthology.org/2024.findings-acl.1/)

**TLDR**: CoTAM uses chain-of-thought attribute manipulation to generate augmented training data for few-shot NLP tasks via LLM prompting.

## Abstract

AbstractPrompting large language models (LLMs) for data augmentation has recently become a common practice in few-shot NLP tasks. In this paper, we propose Chain-of-Thought Attribute Manipulation (CoTAM), a novel approach that generates new data from existing examples by only tweaking in the user-provided, task-specific attribute, e.g., sentiment polarity or topic in movie reviews. Instead of conventional latent representation controlling, we leverage the chain-of-thought prompting to directly edit the text in three steps, (1) attribute decomposition, (2) manipulation proposal, and (3) sentence reconstruction. Extensive results on various tasks, such as text (pair) classification and aspect-based sentiment analysis, verify the superiority of CoTAM over other LLM-based augmentation methods with the same number of training examples for both fine-tuning and in-context learning. Remarkably, the 2D visualization of the augmented dataset using principle component analysis revealed a human-recognizable decision boundary that is likely hinted by the attribute manipulation, demonstrating the potential of our proposed approach.