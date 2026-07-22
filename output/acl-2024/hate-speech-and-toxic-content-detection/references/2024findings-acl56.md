---
title: "Implanting LLM’s Knowledge via Reading Comprehension Tree for Toxicity Detection"
source: "https://aclanthology.org/2024.findings-acl.56/"
categories: ['hate-speech-and-toxic-content-detection', 'llms-for-biomedical-and-clinical-nlp']
tags: ['toxicity-detection', 'knowledge-distillation', 'reading-comprehension']
venue: "ACL 2024"
tldr: "A reading comprehension tree method transfers LLM knowledge into smaller models to improve toxicity detection without embedded biases."
---

# Implanting LLM’s Knowledge via Reading Comprehension Tree for Toxicity Detection

**Source**: [https://aclanthology.org/2024.findings-acl.56/](https://aclanthology.org/2024.findings-acl.56/)

**TLDR**: A reading comprehension tree method transfers LLM knowledge into smaller models to improve toxicity detection without embedded biases.

## Abstract

AbstractToxicity detection plays a crucial role in maintaining the peace of the society. Existing methods can be roughly categorized as small language model (SLM) based and large language model (LLM) based. However, due to the limitation of SLMs on general knowledge and the potential embedded bias in LLMs despite their large amount of knowledge, it is not a good idea to detect toxicity only with either SLM or LLM based method.In this work, we propose to implant LLM’s knowledge into SLM based methods such that we can stick to both types of models’ strengths. To this end, we develop a reading comprehension (RC) tree to transfer knowledge between two models. Specifically, we first construct the RC tree, from an extensive to intensive reading perspective, to capture the local and global information in the text. We then model samples encoded by SLM and knowledge extracted from LLM as two distributions using the constructed RT tree. We finally transfer knowledge via optimal transportation between two distributions. Extensive experiments prove the effectiveness of our method on real-world and machine-generated datasets.