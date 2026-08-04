---
title: "In-Context Learning Agents Are Asymmetric Belief Updaters"
source: "https://proceedings.mlr.press/v235/schubert24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/schubert24a/schubert24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'ai-explainability-uncertainty-human-decision-making']
tags: ['in-context-learning', 'belief-updating', 'asymmetric-learning', 'LLMs', 'cognitive-psychology']
venue: "ICML 2024"
tldr: "LLMs exhibit asymmetric belief updating in-context, learning more from positive than negative prediction errors, mirroring optimism biases seen in human cognition."
---

# In-Context Learning Agents Are Asymmetric Belief Updaters

**Source**: [https://proceedings.mlr.press/v235/schubert24a.html](https://proceedings.mlr.press/v235/schubert24a.html)

**TLDR**: LLMs exhibit asymmetric belief updating in-context, learning more from positive than negative prediction errors, mirroring optimism biases seen in human cognition.

## Abstract

We study the in-context learning dynamics of large language models (LLMs) using three instrumental learning tasks adapted from cognitive psychology. We find that LLMs update their beliefs in an asymmetric manner and learn more from better-than-expected outcomes than from worse-than-expected ones. Furthermore, we show that this effect reverses when learning about counterfactual feedback and disappears when no agency is implied. We corroborate these findings by investigating idealized in-context learning agents derived through meta-reinforcement learning, where we observe similar patterns. Taken together, our results contribute to our understanding of how in-context learning works by highlighting that the framing of a problem significantly influences how learning occurs, a phenomenon also observed in human cognition.