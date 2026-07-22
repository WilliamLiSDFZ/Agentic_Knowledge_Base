---
title: "Deciphering the Impact of Pretraining Data on Large Language Models through Machine Unlearning"
source: "https://aclanthology.org/2024.findings-acl.559/"
categories: ['llm-training-alignment-and-evaluation', 'nlp-for-asian-languages']
tags: ['machine-unlearning', 'pretraining-data', 'llm-analysis']
venue: "ACL 2024"
tldr: "Machine unlearning is applied to decipher the contribution of individual pretraining corpus components to LLM capabilities and behaviors."
---

# Deciphering the Impact of Pretraining Data on Large Language Models through Machine Unlearning

**Source**: [https://aclanthology.org/2024.findings-acl.559/](https://aclanthology.org/2024.findings-acl.559/)

**TLDR**: Machine unlearning is applied to decipher the contribution of individual pretraining corpus components to LLM capabilities and behaviors.

## Abstract

AbstractThrough pretraining on a corpus with various sources, Large Language Models (LLMs) have gained impressive performance. However, the impact of each component of the pretraining corpus remains opaque. As a result, the organization of the pretraining corpus is still empirical and may deviate from the optimal. To address this issue, we systematically analyze the impact of 48 datasets from 5 major categories of pretraining data of LLMs and measure their impacts on LLMs using benchmarks about nine major categories of model capabilities. Our analyses provide empirical results about the contribution of multiple corpora on the performances of LLMs, along with their joint impact patterns, including complementary, orthogonal, and correlational relationships. We also identify a set of “high-impact data” such as Books that is significantly related to a set of model capabilities. These findings provide insights into the organization of data to support more efficient pretraining of LLMs.