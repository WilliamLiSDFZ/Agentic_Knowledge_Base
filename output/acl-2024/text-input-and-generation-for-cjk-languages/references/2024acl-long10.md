---
title: "CSCD-NS: a Chinese Spelling Check Dataset for Native Speakers"
source: "https://aclanthology.org/2024.acl-long.10/"
categories: ['text-input-and-generation-for-cjk-languages']
tags: ['chinese-spelling-check', 'native-speakers', 'dataset']
venue: "ACL 2024"
tldr: "Presents CSCD-NS, the first large-scale Chinese spelling check dataset targeting native speakers from social media."
---

# CSCD-NS: a Chinese Spelling Check Dataset for Native Speakers

**Source**: [https://aclanthology.org/2024.acl-long.10/](https://aclanthology.org/2024.acl-long.10/)

**TLDR**: Presents CSCD-NS, the first large-scale Chinese spelling check dataset targeting native speakers from social media.

## Abstract

AbstractIn this paper, we present CSCD-NS, the first Chinese spelling check (CSC) dataset designed for native speakers, containing 40,000 samples from a Chinese social platform. Compared with existing CSC datasets aimed at Chinese learners, CSCD-NS is ten times larger in scale and exhibits a distinct error distribution, with a significantly higher proportion of word-level errors. To further enhance the data resource, we propose a novel method that simulates the input process through an input method, generating large-scale and high-quality pseudo data that closely resembles the actual error distribution and outperforms existing methods. Moreover, we investigate the performance of various models in this scenario, including large language models (LLMs), such as ChatGPT. The result indicates that generative models underperform BERT-like classification models due to strict length and pronunciation constraints. The high prevalence of word-level errors also makes CSC for native speakers challenging enough, leaving substantial room for improvement.