---
title: "Do Models Explain Themselves? Counterfactual Simulatability of Natural Language Explanations"
source: "https://proceedings.mlr.press/v235/chen24bl.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24bl/chen24bl.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'large-language-model-alignment-and-capabilities']
tags: ['counterfactual-simulatability', 'LLM-explanations', 'human-mental-models']
venue: "ICML 2024"
tldr: "Counterfactual simulatability is proposed as a metric to evaluate whether LLM-generated natural language explanations help users predict model behavior on new inputs."
---

# Do Models Explain Themselves? Counterfactual Simulatability of Natural Language Explanations

**Source**: [https://proceedings.mlr.press/v235/chen24bl.html](https://proceedings.mlr.press/v235/chen24bl.html)

**TLDR**: Counterfactual simulatability is proposed as a metric to evaluate whether LLM-generated natural language explanations help users predict model behavior on new inputs.

## Abstract

Large language models (LLMs) are trained to imitate humans to explain human decisions. However, do LLMs explain themselves? Can they help humans build mental models of how LLMs process different inputs? To answer these questions, we propose to evaluate $\textbf{counterfactual simulatability}$ of natural language explanations: whether an explanation can enable humans to precisely infer the model’s outputs on diverse counterfactuals of the explained input. For example, if a model answers ”$\textit{yes}$” to the input question ”$\textit{Can eagles fly?}$” with the explanation ”$\textit{all birds can fly}$”, then humans would infer from the explanation that it would also answer ”$\textit{yes}$” to the counterfactual input ”$\textit{Can penguins fly?}$”. If the explanation is precise, then the model’s answer should match humans’ expectations. We implemented two metrics based on counterfactual simulatability: precision and generality. We generated diverse counterfactuals automatically using LLMs. We then used these metrics to evaluate state-of-the-art LLMs (e.g., GPT-4) on two tasks: multi-hop factual reasoning and reward modeling. We found that LLM’s explanations have low precision and that precision does not correlate with plausibility. Therefore, naively optimizing human approvals (e.g., RLHF) may be insufficient.