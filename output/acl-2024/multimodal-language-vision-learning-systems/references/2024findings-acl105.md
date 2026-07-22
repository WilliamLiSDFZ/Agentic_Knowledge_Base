---
title: "VALOR-EVAL: Holistic Coverage and Faithfulness Evaluation of Large Vision-Language Models"
source: "https://aclanthology.org/2024.findings-acl.105/"
categories: ['multimodal-language-vision-learning-systems']
tags: ['vision-language-models', 'hallucination', 'evaluation']
venue: "ACL 2024"
tldr: "Proposes VALOR-EVAL, a holistic benchmark for evaluating coverage and faithfulness of large vision-language model outputs."
---

# VALOR-EVAL: Holistic Coverage and Faithfulness Evaluation of Large Vision-Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.105/](https://aclanthology.org/2024.findings-acl.105/)

**TLDR**: Proposes VALOR-EVAL, a holistic benchmark for evaluating coverage and faithfulness of large vision-language model outputs.

## Abstract

AbstractLarge Vision-Language Models (LVLMs) suffer from hallucination issues, wherein the models generate plausible-sounding but factually incorrect outputs, undermining their reliability. A comprehensive quantitative evaluation is necessary to identify and understand the extent of hallucinations in these models. However, existing benchmarks are often limited in scope, focusing mainly on object hallucinations. Furthermore, current evaluation methods struggle to effectively address the subtle semantic distinctions between model outputs and reference data, as well as the balance between hallucination and informativeness. To address these issues, we introduce a multi-dimensional benchmark covering objects, attributes, and relations, with challenging images selected based on associative biases. Moreover, we propose a large language model (LLM)-based two-stage evaluation framework that generalizes the popular CHAIR metric and incorporates both faithfulness and coverage into the evaluation. Experiments on 10 established LVLMs demonstrate that our evaluation metric is more comprehensive and better correlated with humans than existing work when evaluating on our challenging human-annotated benchmark dataset. Our work also highlights the critical balance between faithfulness and coverage of model outputs, and encourages future works to address hallucinations in LVLMs while keeping their outputs informative.