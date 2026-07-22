---
title: "Refining and Synthesis: A Simple yet Effective Data Augmentation Framework for Cross-Domain Aspect-based Sentiment Analysis"
source: "https://aclanthology.org/2024.findings-acl.615/"
pdf_url: ""
categories: ['multilingual-text-classification-and-sentiment-analysis', 'natural-language-processing-information-extraction']
tags: ['aspect-based-sentiment-analysis', 'data-augmentation', 'cross-domain']
venue: "ACL 2024"
tldr: "A data augmentation framework using refining and synthesis improves cross-domain aspect-based sentiment analysis by addressing data sparsity."
---

# Refining and Synthesis: A Simple yet Effective Data Augmentation Framework for Cross-Domain Aspect-based Sentiment Analysis

**Source**: [https://aclanthology.org/2024.findings-acl.615/](https://aclanthology.org/2024.findings-acl.615/)

**TLDR**: A data augmentation framework using refining and synthesis improves cross-domain aspect-based sentiment analysis by addressing data sparsity.

## Abstract

AbstractAspect-based Sentiment Analysis (ABSA) is extensively researched in the NLP community, yet related models face challenges due to data sparsity when shifting to a new domain. Hence, data augmentation for cross-domain ABSA has attracted increasing attention in recent years. However, two key points have been neglected in prior studies: First, target domain unlabeled data are labeled with pseudo labels by the model trained in the source domain with little quality control, leading to inaccuracy and error propagation. Second, the label and text patterns of generated labeled data are monotonous, thus limiting the robustness and generalization ability of trained ABSA models. In this paper, we aim to design a simple yet effective framework to address the above shortages in ABSA data augmentation, called Refining and Synthesis Data Augmentation (RSDA). Our framework roughly includes two steps: First, it refines generated labeled data using a natural language inference (NLI) filter to control data quality. Second, it synthesizes diverse labeled data via novel label composition and paraphrase approaches. We conduct experiments on 4 kinds of ABSA subtasks, and our framework outperforms 7 strong baselines, demonstrating its effectiveness.