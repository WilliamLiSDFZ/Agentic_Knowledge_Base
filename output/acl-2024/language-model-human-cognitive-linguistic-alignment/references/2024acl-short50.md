---
title: "Naming, Describing, and Quantifying Visual Objects in Humans and LLMs"
source: "https://aclanthology.org/2024.acl-short.50/"
categories: ['multimodal-language-vision-learning-systems', 'language-model-human-cognitive-linguistic-alignment']
tags: ['vision-language-models', 'object-naming', 'pragmatic-description']
venue: "ACL 2024"
tldr: "Compares how humans and vision-language LLMs produce distributions of labels when describing visual objects, probing pragmatic alignment."
---

# Naming, Describing, and Quantifying Visual Objects in Humans and LLMs

**Source**: [https://aclanthology.org/2024.acl-short.50/](https://aclanthology.org/2024.acl-short.50/)

**TLDR**: Compares how humans and vision-language LLMs produce distributions of labels when describing visual objects, probing pragmatic alignment.

## Abstract

AbstractWhile human speakers use a variety of different expressions when describing the same object in an image, giving rise to a distribution of plausible labels driven by pragmatic constraints, the extent to which current Vision & Language Large Language Models (VLLMs) can mimic this crucial feature of language use is an open question. This applies to common, everyday objects, but it is particularly interesting for uncommon or novel objects for which a category label may be lacking or fuzzy. Furthermore, similar patterns of variation are observed among human speakers for highly context-sensitive expressions, such as the quantifiers ‘few’ or ‘most’. In our work, we evaluate VLLMs (FROMAGe, BLIP-2, LLaVA) on three categories (nouns, attributes, and quantifiers) where humans show great subjective variability concerning the distribution over plausible labels, using datasets and resources mostly under-explored in previous work. Our results reveal mixed evidence on the ability of VLLMs to capture human naming preferences at generation time: while some models are good at mimicking human distributions for nouns and attributes, all of them fail to assign quantifiers, a task that requires more accurate, high-level reasoning.