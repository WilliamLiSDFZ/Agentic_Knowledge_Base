---
title: "ImplicitAVE: An Open-Source Dataset and Multimodal LLMs Benchmark for Implicit Attribute Value Extraction"
source: "https://aclanthology.org/2024.findings-acl.20/"
categories: ['multimodal-language-vision-learning-systems', 'natural-language-processing-information-extraction']
tags: ['attribute-value-extraction', 'multimodal', 'implicit-attributes', 'e-commerce', 'benchmark']
venue: "ACL 2024"
tldr: "ImplicitAVE is an open-source multimodal benchmark for implicit attribute value extraction across diverse product domains."
---

# ImplicitAVE: An Open-Source Dataset and Multimodal LLMs Benchmark for Implicit Attribute Value Extraction

**Source**: [https://aclanthology.org/2024.findings-acl.20/](https://aclanthology.org/2024.findings-acl.20/)

**TLDR**: ImplicitAVE is an open-source multimodal benchmark for implicit attribute value extraction across diverse product domains.

## Abstract

AbstractExisting datasets for attribute value extraction (AVE) predominantly focus on explicit attribute values while neglecting the implicit ones, lack product images, are often not publicly available, and lack an in-depth human inspection across diverse domains. To address these limitations, we present ImplicitAVE, the first, publicly available multimodal dataset for implicit attribute value extraction. ImplicitAVE, sourced from the MAVE dataset, is carefully curated and expanded to include implicit AVE and multimodality, resulting in a refined dataset of 68k training and 1.6k testing data across five domains. We also explore the application of multimodal large language models (MLLMs) to implicit AVE, establishing a comprehensive benchmark for MLLMs on the ImplicitAVE dataset. Six recent MLLMs with eleven variants are evaluated across diverse settings, revealing that implicit value extraction remains a challenging task for MLLMs. The contributions of this work include the development and release of ImplicitAVE, and the exploration and benchmarking of various MLLMs for implicit AVE, providing valuable insights and potential future research directions. Dataset and code are available at https://github.com/HenryPengZou/ImplicitAVE.