---
title: "Enhancing Sentence Simplification in Portuguese: Leveraging Paraphrases, Context, and Linguistic Features"
source: "https://aclanthology.org/2024.findings-acl.895/"
categories: ['text-simplification-evaluation-and-methods', 'language-technology-cultural-linguistic-diversity']
tags: ['text-simplification', 'portuguese', 'paraphrase']
venue: "ACL 2024"
tldr: "Presents a new approach to automatic sentence simplification in Portuguese leveraging paraphrases, context, and linguistic features."
---

# Enhancing Sentence Simplification in Portuguese: Leveraging Paraphrases, Context, and Linguistic Features

**Source**: [https://aclanthology.org/2024.findings-acl.895/](https://aclanthology.org/2024.findings-acl.895/)

**TLDR**: Presents a new approach to automatic sentence simplification in Portuguese leveraging paraphrases, context, and linguistic features.

## Abstract

AbstractAutomatic text simplification focuses on transforming texts into a more comprehensible version without sacrificing their precision. However, automatic methods usually require (paired) datasets that can be rather scarce in languages other than English. This paper presents a new approach to automatic sentence simplification that leverages paraphrases, context, and linguistic attributes to overcome the absence of paired texts in Portuguese.We frame the simplification problem as a textual style transfer task and learn a style representation using the sentences around the target sentence in the document and its linguistic attributes. Moreover, unlike most unsupervised approaches that require style-labeled training data, we fine-tune strong pre-trained models using sentence-level paraphrases instead of annotated data. Our experiments show that our model achieves remarkable results, surpassing the current state-of-the-art (BART+ACCESS) while competitively matching a Large Language Model.