---
title: "MaskLID: Code-Switching Language Identification through Iterative Masking"
source: "https://aclanthology.org/2024.acl-short.43/"
pdf_url: ""
categories: ['language-technology-cultural-linguistic-diversity', 'multilingual-text-classification-and-sentiment-analysis']
tags: ['code-switching', 'language-identification', 'iterative-masking']
venue: "ACL 2024"
tldr: "MaskLID is a training-free iterative masking method for code-switching language identification that complements sentence-level classifiers."
---

# MaskLID: Code-Switching Language Identification through Iterative Masking

**Source**: [https://aclanthology.org/2024.acl-short.43/](https://aclanthology.org/2024.acl-short.43/)

**TLDR**: MaskLID is a training-free iterative masking method for code-switching language identification that complements sentence-level classifiers.

## Abstract

AbstractWe present MaskLID, a simple, yet effective, code-switching (CS) language identification (LID) method. MaskLID does not require any training and is designed to complement current high-performance sentence-level LIDs. Sentence-level LIDs are classifiers trained on monolingual texts to provide single labels, typically using a softmax layer to turn scores into probabilities. However, in cases where a sentence is composed in both L1 and L2 languages, the LID classifier often only returns the dominant label L1. To address this limitation, MaskLID employs a strategy to mask text features associated with L1, allowing the LID to classify the text as L2 in the next round. This method uses the LID itself to identify the features that require masking and does not rely on any external resource. In this work, we explore the use of MaskLID for two open-source LIDs (GlotLID and OpenLID), that are both based on the FastText architecture. Code and demo are available at https://github.com/cisnlp/MaskLID.