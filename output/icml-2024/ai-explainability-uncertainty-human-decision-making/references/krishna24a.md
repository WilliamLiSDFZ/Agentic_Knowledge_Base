---
title: "Understanding the Effects of Iterative Prompting on Truthfulness"
source: "https://proceedings.mlr.press/v235/krishna24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/krishna24a/krishna24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'ai-explainability-uncertainty-human-decision-making']
tags: ['iterative-prompting', 'truthfulness', 'LLM-reliability']
venue: "ICML 2024"
tldr: "An investigation into whether iterative prompting strategies improve truthfulness and reliability in large language models."
---

# Understanding the Effects of Iterative Prompting on Truthfulness

**Source**: [https://proceedings.mlr.press/v235/krishna24a.html](https://proceedings.mlr.press/v235/krishna24a.html)

**TLDR**: An investigation into whether iterative prompting strategies improve truthfulness and reliability in large language models.

## Abstract

The development of Large Language Models (LLMs) has notably transformed numerous sectors, offering impressive text generation capabilities. Yet, the reliability and truthfulness of these models remain pressing concerns. To this end, we investigate iterative prompting, a strategy hypothesized to refine LLM responses, assessing its impact on LLM truthfulness, an area which has not been thoroughly explored. Our extensive experiments explore the intricacies of iterative prompting variants, examining their influence on the accuracy and calibration of model responses. Our findings reveal that naive prompting methods significantly undermine truthfulness, leading to exacerbated calibration errors. In response to these challenges, we introduce several prompting variants designed to address the identified issues. These variants demonstrate marked improvements over existing baselines, signaling a promising direction for future research. Our work provides a nuanced understanding of iterative prompting and introduces novel approaches to enhance the truthfulness of LLMs, thereby contributing to the development of more accurate and trustworthy AI systems