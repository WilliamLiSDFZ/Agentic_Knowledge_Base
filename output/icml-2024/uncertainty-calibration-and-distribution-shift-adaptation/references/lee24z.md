---
title: "Improving Instruction Following in Language Models through Proxy-Based Uncertainty Estimation"
source: "https://proceedings.mlr.press/v235/lee24z.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24z/lee24z.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['instruction-following', 'uncertainty-estimation', 'proxy-model', 'LLM-alignment']
venue: "ICML 2024"
tldr: "Improves instruction following in LLMs by using proxy-based uncertainty estimation to better assess response quality."
---

# Improving Instruction Following in Language Models through Proxy-Based Uncertainty Estimation

**Source**: [https://proceedings.mlr.press/v235/lee24z.html](https://proceedings.mlr.press/v235/lee24z.html)

**TLDR**: Improves instruction following in LLMs by using proxy-based uncertainty estimation to better assess response quality.

## Abstract

Assessing response quality to instructions in language models is vital but challenging due to the complexity of human language across different contexts. This complexity often results in ambiguous or inconsistent interpretations, making accurate assessment difficult. To address this issue, we propose a novel Uncertainty-aware Reward Model (URM) that introduces a robust uncertainty estimation for the quality of paired responses based on Bayesian approximation. Trained with preference datasets, our uncertainty-enabled proxy not only scores rewards for responses but also evaluates their inherent uncertainty. Empirical results demonstrate significant benefits of incorporating the proposed proxy into language model training. Our method boosts the instruction following capability of language models by refining data curation for training and improving policy optimization objectives, thereby surpassing existing methods by a large margin on benchmarks such as Vicuna and MT-bench. These findings highlight that our proposed approach substantially advances language model training and paves a new way of harnessing uncertainty within language models.