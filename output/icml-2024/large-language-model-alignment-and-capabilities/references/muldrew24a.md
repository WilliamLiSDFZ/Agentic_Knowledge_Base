---
title: "Active Preference Learning for Large Language Models"
source: "https://proceedings.mlr.press/v235/muldrew24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/muldrew24a/muldrew24a.pdf"
categories: ['data-selection-and-active-learning-methods', 'large-language-model-alignment-and-capabilities']
tags: ['active-learning', 'RLHF', 'preference-learning', 'LLM-alignment']
venue: "ICML 2024"
tldr: "An active preference learning approach is proposed to efficiently fine-tune LLMs by selecting maximally informative human feedback queries for alignment."
---

# Active Preference Learning for Large Language Models

**Source**: [https://proceedings.mlr.press/v235/muldrew24a.html](https://proceedings.mlr.press/v235/muldrew24a.html)

**TLDR**: An active preference learning approach is proposed to efficiently fine-tune LLMs by selecting maximally informative human feedback queries for alignment.

## Abstract

As large language models (LLMs) become more capable, fine-tuning techniques for aligning with human intent are increasingly important. A key consideration for aligning these models is how to most effectively use human resources, or model resources in the case where LLMs themselves are used as oracles. Reinforcement learning from Human or AI preferences (RLHF/RLAIF) is the most prominent example of such a technique, but is complex and often unstable. Direct Preference Optimization (DPO) has recently been proposed as a simpler and more stable alternative. In this work, we develop an active learning strategy for DPO to make better use of preference labels. We propose a practical acquisition function for prompt/completion pairs based on the predictive entropy of the language model and a measure of certainty of the implicit preference model optimized by DPO. We demonstrate how our approach improves both the rate of learning and final performance of fine-tuning on pairwise preference data.