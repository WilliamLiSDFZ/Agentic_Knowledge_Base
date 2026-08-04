---
title: "Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs"
source: "https://proceedings.mlr.press/v235/smit24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/smit24a/smit24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['multi-agent-debate', 'LLMs', 'factual-accuracy', 'reasoning']
venue: "ICML 2024"
tldr: "This paper evaluates multi-agent debate strategies for LLMs and analyzes their effectiveness in improving accuracy and reliability of generated answers."
---

# Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs

**Source**: [https://proceedings.mlr.press/v235/smit24a.html](https://proceedings.mlr.press/v235/smit24a.html)

**TLDR**: This paper evaluates multi-agent debate strategies for LLMs and analyzes their effectiveness in improving accuracy and reliability of generated answers.

## Abstract

Recent advancements in large language models (LLMs) underscore their potential for responding to inquiries in various domains. However, ensuring that generative agents provide accurate and reliable answers remains an ongoing challenge. In this context, multi-agent debate (MAD) has emerged as a promising strategy for enhancing the truthfulness of LLMs. We benchmark a range of debating and prompting strategies to explore the trade-offs between cost, time, and accuracy. Importantly, we find that multi-agent debating systems, in their current form, do not reliably outperform other proposed prompting strategies, such as self-consistency and ensembling using multiple reasoning paths. However, when performing hyperparameter tuning, several MAD systems, such as Multi-Persona, perform better. This suggests that MAD protocols might not be inherently worse than other approaches, but that they are more sensitive to different hyperparameter settings and difficult to optimize. We build on these results to offer insights into improving debating strategies, such as adjusting agent agreement levels, which can significantly enhance performance and even surpass all other non-debate protocols we evaluated. We provide an open-source repository to the community with several state-of-the-art protocols together with evaluation scripts to benchmark across popular research datasets.