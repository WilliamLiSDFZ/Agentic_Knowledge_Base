---
title: "Detection-Correction Structure via General Language Model for Grammatical Error Correction"
source: "https://aclanthology.org/2024.acl-long.96/"
pdf_url: ""
categories: ['natural-language-processing-information-extraction', 'llm-training-alignment-and-evaluation']
tags: ['grammatical-error-correction', 'detection-correction', 'language-model']
venue: "ACL 2024"
tldr: "Proposes a detection-correction architecture integrating both components for improved grammatical error correction."
---

# Detection-Correction Structure via General Language Model for Grammatical Error Correction

**Source**: [https://aclanthology.org/2024.acl-long.96/](https://aclanthology.org/2024.acl-long.96/)

**TLDR**: Proposes a detection-correction architecture integrating both components for improved grammatical error correction.

## Abstract

AbstractGrammatical error correction (GEC) is a task dedicated to rectifying texts with minimal edits, which can be decoupled into two components: detection and correction. However, previous works have predominantly focused on direct correction, with no prior efforts to integrate both into a single model. Moreover, the exploration of the detection-correction paradigm by large language models (LLMs) remains underdeveloped. This paper introduces an integrated detection-correction structure, named DeCoGLM, based on the General Language Model (GLM). The detection phase employs a fault-tolerant detection template, while the correction phase leverages autoregressive mask infilling for localized error correction. Through the strategic organization of input tokens and modification of attention masks, we facilitate multi-task learning within a single model. Our model demonstrates competitive performance against the state-of-the-art models on English and Chinese GEC datasets. Further experiments present the effectiveness of the detection-correction structure in LLMs, suggesting a promising direction for GEC.