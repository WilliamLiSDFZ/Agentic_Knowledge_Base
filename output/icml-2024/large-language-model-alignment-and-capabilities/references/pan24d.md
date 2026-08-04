---
title: "Feedback Loops With Language Models Drive In-Context Reward Hacking"
source: "https://proceedings.mlr.press/v235/pan24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pan24d/pan24d.pdf"
categories: ['large-language-model-alignment-and-capabilities']
tags: ['language-model-feedback-loops', 'reward-hacking', 'in-context-learning', 'AI-safety']
venue: "ICML 2024"
tldr: "Demonstrates that feedback loops between LLM outputs and the external world drive in-context reward hacking behaviors."
---

# Feedback Loops With Language Models Drive In-Context Reward Hacking

**Source**: [https://proceedings.mlr.press/v235/pan24d.html](https://proceedings.mlr.press/v235/pan24d.html)

**TLDR**: Demonstrates that feedback loops between LLM outputs and the external world drive in-context reward hacking behaviors.

## Abstract

Language models influence the external world: they query APIs that read and write to web pages, generate content that shapes human behavior, and run system commands as autonomous agents. These interactions form feedback loops: LLM outputs affect the world, which in turn affect subsequent LLM outputs. In this work, we show that feedback loops can cause in-context reward hacking (ICRH), where the LLM at test-time optimizes a (potentially implicit) objective but creates negative side effects in the process. For example, consider an LLM agent deployed to increase Twitter engagement; the LLM may retrieve its previous tweets into the context window and make them more controversial, increasing engagement but also toxicity. We identify and study two processes that lead to ICRH: output-refinement and policy-refinement. For these processes, evaluations on static datasets are insufficient—they miss the feedback effects and thus cannot capture the most harmful behavior. In response, we provide three recommendations for evaluation to capture more instances of ICRH. As AI development accelerates, the effects of feedback loops will proliferate, increasing the need to understand their role in shaping LLM behavior.