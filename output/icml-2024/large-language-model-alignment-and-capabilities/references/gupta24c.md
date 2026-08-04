---
title: "GistScore: Learning Better Representations for In-Context Example Selection with Gist Bottlenecks"
source: "https://proceedings.mlr.press/v235/gupta24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gupta24c/gupta24c.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'information-retrieval-and-recommendation-systems']
tags: ['in-context-learning', 'example-selection', 'gist-bottleneck', 'representation-learning', 'LLMs']
venue: "ICML 2024"
tldr: "A gist bottleneck-based representation learning approach for better in-context example selection in LLMs."
---

# GistScore: Learning Better Representations for In-Context Example Selection with Gist Bottlenecks

**Source**: [https://proceedings.mlr.press/v235/gupta24c.html](https://proceedings.mlr.press/v235/gupta24c.html)

**TLDR**: A gist bottleneck-based representation learning approach for better in-context example selection in LLMs.

## Abstract

In-Context Learning (ICL) is the ability of Large Language Models (LLMs) to perform new tasks when conditioned on prompts comprising a few task examples. However, ICL performance can be critically sensitive to the choice of examples. To dynamically select the best examples for every test input, we propose Example Gisting, a novel approach for training example encoders through supervised finetuning with an attention bottleneck between the inputs and outputs. These gist models form the basis for GistScore, a novel metric for scoring and selecting informative examples. Further, we experiment with two variations: (1) finetuning gist models for each dataset and (2) multi-task training a single model on a large collection of datasets. The latter can be used for new tasks out-of-the-box, enabling a training-free ICL pipeline. Evaluations with 21 datasets spanning 9 tasks and 8 diverse LLMs show that our fine-tuned models get state-of-the-art ICL performance with over 20% absolute gain over off-the-shelf retrievers and 5% over the best prior methods. Further, our multi-task model generalizes well to new tasks, datasets, and prompt templates. Selection using this model matches or outperforms prior methods while being three orders of magnitude faster than the strongest training-free baseline.