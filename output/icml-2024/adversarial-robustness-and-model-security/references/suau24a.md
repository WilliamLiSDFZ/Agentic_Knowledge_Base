---
title: "Whispering Experts: Neural Interventions for Toxicity Mitigation in Language Models"
source: "https://proceedings.mlr.press/v235/suau24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/suau24a/suau24a.pdf"
categories: ['llm-geometry-and-interpretability-research', 'adversarial-robustness-and-model-security']
tags: ['toxicity-mitigation', 'LLM', 'neural-interventions', 'toxic-neurons', 'language-model-safety']
venue: "ICML 2024"
tldr: "Neurons responsible for toxic language in LLMs are identified via discriminative power and mitigated through targeted neural interventions."
---

# Whispering Experts: Neural Interventions for Toxicity Mitigation in Language Models

**Source**: [https://proceedings.mlr.press/v235/suau24a.html](https://proceedings.mlr.press/v235/suau24a.html)

**TLDR**: Neurons responsible for toxic language in LLMs are identified via discriminative power and mitigated through targeted neural interventions.

## Abstract

An important issue with Large Language Models (LLMs) is their undesired ability to generate toxic language. In this work, we show that the neurons responsible for toxicity can be determined by their power to discriminate toxic sentences, and that toxic language can be mitigated by reducing their activation levels proportionally to this power. We propose AUROC adaptation (AurA), an intervention that can be applied to any pre-trained LLM to mitigate toxicity. As the intervention is proportional to the ability of each neuron to discriminate toxic content, it is free of any model-dependent hyperparameters. We show that AurA can achieve up to $2.2\times$ reduction in toxicity with only a $0.72$ perplexity increase. We also show that AurA is effective with models of different scale (from 1.5B to 40B parameters), and its effectiveness in mitigating toxic language, while preserving common-sense zero-shot abilities, holds across all scales. AurA can be combined with pre-prompting strategies, boosting its average mitigation potential from $1.28\times$ to $2.35\times$. Moreover, AurA can counteract adversarial pre-prompts that maliciously elicit toxic content, making it an effective method for deploying safer and less toxic models.