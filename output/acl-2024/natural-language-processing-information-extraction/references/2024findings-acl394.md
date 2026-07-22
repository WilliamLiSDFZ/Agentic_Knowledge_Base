---
title: "It is Simple Sometimes: A Study On Improving Aspect-Based Sentiment Analysis Performance"
source: "https://aclanthology.org/2024.findings-acl.394/"
categories: ['multilingual-text-classification-and-sentiment-analysis', 'natural-language-processing-information-extraction']
tags: ['aspect-based-sentiment', 'ABSA', 'text-classification']
venue: "ACL 2024"
tldr: "A study showing that simpler approaches can match or outperform complex ad hoc designs for aspect-based sentiment analysis subtasks."
---

# It is Simple Sometimes: A Study On Improving Aspect-Based Sentiment Analysis Performance

**Source**: [https://aclanthology.org/2024.findings-acl.394/](https://aclanthology.org/2024.findings-acl.394/)

**TLDR**: A study showing that simpler approaches can match or outperform complex ad hoc designs for aspect-based sentiment analysis subtasks.

## Abstract

AbstractAspect-Based Sentiment Analysis (ABSA) involves extracting opinions from textual data about specific entities and their corresponding aspects through various complementary subtasks. Several prior research has focused on developing ad hoc designs of varying complexities for these subtasks. In this paper, we build upon the instruction tuned model proposed by Scaria et al. (2023), who present an instruction-based model with task descriptions followed by in-context examples on ABSA subtasks. We propose PFInstruct, an extension to this instruction learning paradigm by appending an NLP-related task prefix to the task description. This simple approach leads to improved performance across all tested SemEval subtasks, surpassing previous state-of-the-art (SOTA) on the ATE subtask (Rest14) by +3.28 F1-score, and on the AOOE subtask by an average of +5.43 F1-score across SemEval datasets. Furthermore, we explore the impact of the prefix-enhanced prompt quality on the ABSA subtasks and find that even a noisy prefix enhances model performance compared to the baseline. Our method also achieves competitive results on a biomedical domain dataset (ERSA).