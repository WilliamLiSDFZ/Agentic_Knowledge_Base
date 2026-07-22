---
title: "P4: Plug-and-Play Discrete Prompting for Large Language Models Personalization"
source: "https://aclanthology.org/2024.findings-acl.541/"
categories: ['llm-training-alignment-and-evaluation', 'privacy-risks-in-language-model-embeddings']
tags: ['personalization', 'discrete-prompting', 'plug-and-play']
venue: "ACL 2024"
tldr: "Introduces P4, a plug-and-play discrete prompting approach for personalizing LLMs with distinct human-like personality traits."
---

# P4: Plug-and-Play Discrete Prompting for Large Language Models Personalization

**Source**: [https://aclanthology.org/2024.findings-acl.541/](https://aclanthology.org/2024.findings-acl.541/)

**TLDR**: Introduces P4, a plug-and-play discrete prompting approach for personalizing LLMs with distinct human-like personality traits.

## Abstract

AbstractEmpowering Large Language Models (LLMs) with distinct human-like personality traits has become an innovative task for developing advanced dialog systems.Although LLMs demonstrate impressive capabilities in following instructions, directly prompting them to exhibit certain personalities through manually crafted instructions may result in sub-optimal performance.In this paper, we propose a plug-and-play prompting method to manipulate the LLMs’ personality traits.Specifically, we append discrete personalized suffixes, automatically generated through an aggregated gradient-based search method, to the user query or dialog histories and induce LLMs to respond with target personalities.In addition, due to the high redundancy of the search space, we adopt a reward-based strategy to prune the vocabulary and focus exclusively on influential tokens.Experiment results on four models ranging from 1.1B to 13B show that our method achieves 79.9% accuracy in customizing LLMs’ personalities, significantly outperforming other prompting methods (65.5%) and model editing methods.Our method also excels in generation fluency and quality with the lowest generation perplexity and the highest GPT-4 evaluation scores.