---
title: "Generating Chain-of-Thoughts with a Pairwise-Comparison Approach to Searching for the Most Promising Intermediate Thought"
source: "https://proceedings.mlr.press/v235/zhang24t.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24t/zhang24t.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'online-learning-and-sequential-decision-making']
tags: ['chain-of-thought', 'pairwise-comparison', 'LLM-reasoning']
venue: "ICML 2024"
tldr: "A pairwise-comparison search approach for selecting the most promising intermediate thoughts in chain-of-thought reasoning with LLMs."
---

# Generating Chain-of-Thoughts with a Pairwise-Comparison Approach to Searching for the Most Promising Intermediate Thought

**Source**: [https://proceedings.mlr.press/v235/zhang24t.html](https://proceedings.mlr.press/v235/zhang24t.html)

**TLDR**: A pairwise-comparison search approach for selecting the most promising intermediate thoughts in chain-of-thought reasoning with LLMs.

## Abstract

To improve the ability of the large language model (LLMs) to tackle complex reasoning problems, chain-of-thoughts (CoT) methods were proposed to guide LLMs to reason step-by-step, enabling problem solving from simple to complex. State-of-the-art methods for generating such a chain involve interactive collaboration, where the learner generates candidate intermediate thoughts, evaluated by the LLM, guiding the generation of subsequent thoughts. However, a widespread yet understudied problem is that the evaluation from the LLM is typically noisy and unreliable, potentially misleading the generation process in selecting promising intermediate thoughts. In this paper, motivated by Vapnik’s principle, we use pairwise-comparison evaluation instead of point-wise scoring to search for promising intermediate thoughts with the noisy feedback from the LLM. In each round, we randomly pair intermediate thoughts and directly prompt the LLM to select the more promising one from each pair, allowing us to identify the most promising thoughts through an iterative process. To further alleviate the noise in the comparison, we incorporate techniques from ensemble learning and dueling bandits, proposing two variants of the algorithm. Experiments on three real-world tasks demonstrate the effectiveness of our proposed algorithm and verify the rationale of the pairwise comparison mechanism.