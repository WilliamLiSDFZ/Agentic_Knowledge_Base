---
title: "Deep Exploration of Cross-Lingual Zero-Shot Generalization in Instruction Tuning"
source: "https://aclanthology.org/2024.findings-acl.912/"
pdf_url: ""
categories: ['language-technology-cultural-linguistic-diversity', 'llm-training-alignment-and-evaluation']
tags: ['instruction-tuning', 'cross-lingual', 'zero-shot']
venue: "ACL 2024"
tldr: "A deep exploration of how instruction tuning enables cross-lingual zero-shot generalization in multilingual language models."
---

# Deep Exploration of Cross-Lingual Zero-Shot Generalization in Instruction Tuning

**Source**: [https://aclanthology.org/2024.findings-acl.912/](https://aclanthology.org/2024.findings-acl.912/)

**TLDR**: A deep exploration of how instruction tuning enables cross-lingual zero-shot generalization in multilingual language models.

## Abstract

AbstractInstruction tuning has emerged as a powerful technique, significantly boosting zero-shot performance on unseen tasks. While recent work has explored cross-lingual generalization by applying instruction tuning to multilingual models, previous studies have primarily focused on English, with a limited exploration of non-English tasks. For in-depth exploration of cross-lingual generalization in instruction tuning, we perform instruction tuning individually for two distinct language meta-datasets. Subsequently, we assess the performance on unseen tasks in the language different from the one used for training. To facilitate this investigation, we introduce a novel non-English meta-dataset named “KORANI” (Korean Natural Instruction), comprising 51 Korean benchmarks. Moreover, we design cross-lingual templates to mitigate discrepancies in language and instruction-format of the template between training and inference within the cross-lingual setting. Our experiments reveal consistent improvements through cross-lingual generalization in both English and Korean, outperforming baseline by average scores of 20.7% and 13.6%, respectively. Remarkably, these enhancements are comparable to those achieved by mono-lingual instruction tuning and even surpass them in some tasks. The result underscores the significance of relevant data acquisition across languages over linguistic congruence with unseen tasks during instruction tuning.