---
title: "Few-Shot Character Understanding in Movies as an Assessment to Meta-Learning of Theory-of-Mind"
source: "https://proceedings.mlr.press/v235/yu24n.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yu24n/yu24n.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'ai-explainability-uncertainty-human-decision-making']
tags: ['theory-of-mind', 'few-shot-learning', 'meta-learning', 'character-understanding']
venue: "ICML 2024"
tldr: "Proposes movie character understanding as a benchmark for evaluating meta-learning of theory-of-mind through few-shot analogical reasoning."
---

# Few-Shot Character Understanding in Movies as an Assessment to Meta-Learning of Theory-of-Mind

**Source**: [https://proceedings.mlr.press/v235/yu24n.html](https://proceedings.mlr.press/v235/yu24n.html)

**TLDR**: Proposes movie character understanding as a benchmark for evaluating meta-learning of theory-of-mind through few-shot analogical reasoning.

## Abstract

When reading a story, humans can quickly understand new fictional characters with a few observations, mainly by drawing analogies to fictional and real people they already know. This reflects the few-shot and meta-learning essence of humans’ inference of characters’ mental states, i.e., theory-of-mind (ToM), which is largely ignored in existing research. We fill this gap with a novel NLP dataset in a realistic narrative understanding scenario, ToM-in-AMC. Our dataset consists of $\sim$1,000 parsed movie scripts, each corresponding to a few-shot character understanding task that requires models to mimic humans’ ability of fast digesting characters with a few starting scenes in a new movie. We further propose a novel ToM prompting approach designed to explicitly assess the influence of multiple ToM dimensions. It surpasses existing baseline models, underscoring the significance of modeling multiple ToM dimensions for our task. Our extensive human study verifies that humans are capable of solving our problem by inferring characters’ mental states based on their previously seen movies. In comparison, all the AI systems lag $>20%$ behind humans, highlighting a notable limitation in existing approaches’ ToM capabilities. Code and data are available at https://github.com/ShunchiZhang/ToM-in-AMC