---
title: "Discourse Structure-Aware Prefix for Generation-Based End-to-End Argumentation Mining"
source: "https://aclanthology.org/2024.findings-acl.689/"
categories: ['causal-reasoning-and-explanation-in-nlp', 'natural-language-processing-information-extraction']
tags: ['argumentation-mining', 'discourse-structure', 'prefix-tuning']
venue: "ACL 2024"
tldr: "Discourse structure-aware prefixes improve generation-based end-to-end argumentation mining by capturing argument structure."
---

# Discourse Structure-Aware Prefix for Generation-Based End-to-End Argumentation Mining

**Source**: [https://aclanthology.org/2024.findings-acl.689/](https://aclanthology.org/2024.findings-acl.689/)

**TLDR**: Discourse structure-aware prefixes improve generation-based end-to-end argumentation mining by capturing argument structure.

## Abstract

AbstractEnd-to-end argumentation mining (AM) aims to extract the argumentation structure including argumentation components and their argumentation relations from text. Recent developments in end-to-end AM models have demonstrated significant progress by redefining the AM task as a sequence generation task, exhibiting simplicity and competitive performance. Nevertheless, these models overlook the integration of supplementary discourse structure information, a crucial factor for comprehending argumentation structures, resulting in suboptimal outcomes. In this study, we propose the DENIM framework, which generates discourse structure-aware prefixes for each layer of the generation model. These prefixes imbue the generation-based AM model with discourse structures, thereby augmenting the overall generation process. Moreover, we introduce a multi-task prompt coupled with a three-step decoding strategy, aiming to optimize the efficiency and effectiveness of argumentation structure decoding. Extensive experiments and analyses on two benchmark datasets show that DENIM achieves state-of-the-art performances on two AM benchmarks.