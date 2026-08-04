---
title: "Coactive Learning for Large Language Models using Implicit User Feedback"
source: "https://proceedings.mlr.press/v235/tucker24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tucker24a/tucker24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'online-learning-and-sequential-decision-making']
tags: ['coactive-learning', 'LLM-finetuning', 'implicit-feedback']
venue: "ICML 2024"
tldr: "Proposes coactive learning using implicit user edit feedback as a training signal for fine-tuning large language models."
---

# Coactive Learning for Large Language Models using Implicit User Feedback

**Source**: [https://proceedings.mlr.press/v235/tucker24a.html](https://proceedings.mlr.press/v235/tucker24a.html)

**TLDR**: Proposes coactive learning using implicit user edit feedback as a training signal for fine-tuning large language models.

## Abstract

We propose coactive learning as a model and feedback mechanism for training large language models (LLMs). The key insight is that users provide implicit feedback whenever they edit the text $y$ proposed by an LLM. While the edited text $\bar y$ is typically not a gold-standard example for supervised training, coactive learning merely requires that the edited text $\bar y$ is an improvement over the proposed text $y$. Note that such weak implicit preference feedback $\bar y \succ y$ is available in many application settings on a per-user basis, thus enabling the personalization of LLMs. In this paper, we develop the theoretical basis for coactive training of non-linear models, and we derive CoRLL as the first coactive learning algorithm for LLMs. Empirical results indicate that CoRLL is effective even for weak and noisy coactive preference feedback, making it a promising algorithm for training and personalization of LLMs from feedback that is naturally collected in many use cases.