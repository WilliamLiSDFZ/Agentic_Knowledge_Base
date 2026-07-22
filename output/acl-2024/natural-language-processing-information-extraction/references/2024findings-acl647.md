---
title: "Improving Grammatical Error Correction via Contextual Data Augmentation"
source: "https://aclanthology.org/2024.findings-acl.647/"
pdf_url: ""
categories: ['natural-language-processing-information-extraction', 'continual-learning-for-nlp-tasks']
tags: ['grammatical-error-correction', 'data-augmentation', 'contextual-synthesis']
venue: "ACL 2024"
tldr: "A contextual data augmentation strategy is proposed to improve grammatical error correction during the fine-tuning phase with limited labeled data."
---

# Improving Grammatical Error Correction via Contextual Data Augmentation

**Source**: [https://aclanthology.org/2024.findings-acl.647/](https://aclanthology.org/2024.findings-acl.647/)

**TLDR**: A contextual data augmentation strategy is proposed to improve grammatical error correction during the fine-tuning phase with limited labeled data.

## Abstract

AbstractNowadays, data augmentation through synthetic data has been widely used in the field of Grammatical Error Correction (GEC) to alleviate the problem of data scarcity. However, these synthetic data are mainly used in the pre-training phase rather than the data-limited fine tuning phase due to inconsistent error distribution and noisy labels. In this paper, we propose a synthetic data construction method based on contextual augmentation, which can ensure an efficient augmentation of the original data with a more consistent error distribution. Specifically, we combine rule-based substitution with model-based generation, using the generation model to generate a richer context for the extracted error patterns. Besides, we also propose a relabeling-based data cleaning method to mitigate the effects of noisy labels in synthetic data. Experiments on CoNLL14 and BEA19-Test show that our proposed augmentation method consistently and substantially outperforms strong baselines and achieves the state-of-the-art level with only a few synthetic data.