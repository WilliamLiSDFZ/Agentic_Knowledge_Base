---
title: "Annotating FrameNet via Structure-Conditioned Language Generation"
source: "https://aclanthology.org/2024.acl-short.63/"
categories: ['natural-language-processing-information-extraction']
tags: ['framenet', 'structure-conditioned-generation', 'linguistic-annotation']
venue: "ACL 2024"
tldr: "This paper investigates using structure-conditioned language generation to automatically annotate new FrameNet sentences preserving given semantic frame structures."
---

# Annotating FrameNet via Structure-Conditioned Language Generation

**Source**: [https://aclanthology.org/2024.acl-short.63/](https://aclanthology.org/2024.acl-short.63/)

**TLDR**: This paper investigates using structure-conditioned language generation to automatically annotate new FrameNet sentences preserving given semantic frame structures.

## Abstract

AbstractDespite the remarkable generative capabilities of language models in producing naturalistic language, their effectiveness on explicit manipulation and generation of linguistic structures remain understudied. In this paper, we investigate the task of generating new sentences preserving a given semantic structure, following the FrameNet formalism. We propose a framework to produce novel frame-semantically annotated sentences following an overgenerate-and-filter approach. Our results show that conditioning on rich, explicit semantic information tends to produce generations with high human acceptance, under both prompting and finetuning. Our generated frame-semantic structured annotations are effective at training data augmentation for frame-semantic role labeling in low-resource settings; however, we do not see benefits under higher resource settings. Our study concludes that while generating high-quality, semantically rich data might be within reach, the downstream utility of such generations remains to be seen, highlighting the outstanding challenges with automating linguistic annotation tasks.