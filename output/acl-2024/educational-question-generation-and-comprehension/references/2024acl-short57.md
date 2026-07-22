---
title: "Consistency Training by Synthetic Question Generation for Conversational Question Answering"
source: "https://aclanthology.org/2024.acl-short.57/"
pdf_url: ""
categories: ['educational-question-generation-and-comprehension', 'coreference-resolution-and-dialogue-understanding']
tags: ['conversational-QA', 'question-generation', 'consistency-training', 'history-modeling', 'dialogue']
venue: "ACL 2024"
tldr: "Proposes synthetic question generation with consistency training to improve handling of conversational history in dialogue QA systems."
---

# Consistency Training by Synthetic Question Generation for Conversational Question Answering

**Source**: [https://aclanthology.org/2024.acl-short.57/](https://aclanthology.org/2024.acl-short.57/)

**TLDR**: Proposes synthetic question generation with consistency training to improve handling of conversational history in dialogue QA systems.

## Abstract

AbstractEfficiently modeling historical information is a critical component in addressing user queries within a conversational question-answering (QA) context, as historical context plays a vital role in clarifying the user’s questions. However, irrelevant history induces noise in the reasoning process, especially for those questions with a considerable historical context. In our novel model-agnostic approach, referred to as **CoTaH** (**Co**nsistency-**T**rained **a**ugmented **H**istory), we augment the historical information with synthetic questions and subsequently employ consistency training to train a model that utilizes both real and augmented historical data to implicitly make the reasoning robust to irrelevant history. To the best of our knowledge, this is the first instance of research using synthetic question generation as a form of data augmentation to model conversational QA settings. By citing a common modeling error prevalent in previous research, we introduce a new baseline and compare our model’s performance against it, demonstrating an improvement in results, particularly in later turns of the conversation, when dealing with questions that include a large historical context.