---
title: "GRATH: Gradual Self-Truthifying for Large Language Models"
source: "https://proceedings.mlr.press/v235/chen24aj.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24aj/chen24aj.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'test-time-adaptation-methods-and-evaluation']
tags: ['LLM-truthfulness', 'self-training', 'TruthfulQA', 'alignment']
venue: "ICML 2024"
tldr: "Proposes GRATH, a gradual self-truthifying method to iteratively improve LLM truthfulness without human-labeled data."
---

# GRATH: Gradual Self-Truthifying for Large Language Models

**Source**: [https://proceedings.mlr.press/v235/chen24aj.html](https://proceedings.mlr.press/v235/chen24aj.html)

**TLDR**: Proposes GRATH, a gradual self-truthifying method to iteratively improve LLM truthfulness without human-labeled data.

## Abstract

Truthfulness is paramount for large language models (LLMs) as they are increasingly deployed in real-world applications. However, existing LLMs still struggle with generating truthful content, as evidenced by their modest performance on benchmarks like TruthfulQA. To address this issue, we propose GRAdual self-truTHifying (GRATH), a novel post-processing method to enhance truthfulness of LLMs. GRATH utilizes out-of-domain question prompts to generate pairwise truthfulness training data with each pair containing a question and its correct and incorrect answers, and then optimizes the model via direct preference optimization (DPO) to learn from the truthfulness difference between answer pairs. GRATH iteratively refines truthfulness data and updates the model, leading to a gradual improvement in model truthfulness in a self-supervised manner. Empirically, we evaluate GRATH using different 7B-LLMs and compare with LLMs with similar or even larger sizes on benchmark datasets. Our results show that GRATH effectively improves LLMs’ truthfulness without compromising other core capabilities. Notably, GRATH achieves state-of-the-art performance on TruthfulQA, with MC1 accuracy of 54.71% and MC2 accuracy of 69.10%, which even surpass those on 70B-LLMs. The code is available at https://github.com/chenweixin107/GRATH.