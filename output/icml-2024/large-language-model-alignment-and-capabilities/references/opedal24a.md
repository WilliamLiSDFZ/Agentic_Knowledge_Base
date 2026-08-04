---
title: "Do Language Models Exhibit the Same Cognitive Biases in Problem Solving as Human Learners?"
source: "https://proceedings.mlr.press/v235/opedal24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/opedal24a/opedal24a.pdf"
categories: ['large-language-model-alignment-and-capabilities']
tags: ['large-language-models', 'cognitive-biases', 'problem-solving', 'cognitive-modeling']
venue: "ICML 2024"
tldr: "Studies whether LLMs exhibit similar cognitive biases to human learners in problem-solving tasks."
---

# Do Language Models Exhibit the Same Cognitive Biases in Problem Solving as Human Learners?

**Source**: [https://proceedings.mlr.press/v235/opedal24a.html](https://proceedings.mlr.press/v235/opedal24a.html)

**TLDR**: Studies whether LLMs exhibit similar cognitive biases to human learners in problem-solving tasks.

## Abstract

There is increasing interest in employing large language models (LLMs) as cognitive models. For such purposes, it is central to understand which properties of human cognition are well-modeled by LLMs, and which are not. In this work, we study the biases of LLMs in relation to those known in children when solving arithmetic word problems. Surveying the learning science literature, we posit that the problem-solving process can be split into three distinct steps: text comprehension, solution planning and solution execution. We construct tests for each one in order to understand whether current LLMs display the same cognitive biases as children in these steps. We generate a novel set of word problems for each of these tests, using a neuro-symbolic approach that enables fine-grained control over the problem features. We find evidence that LLMs, with and without instruction-tuning, exhibit human-like biases in both the text-comprehension and the solution-planning steps of the solving process, but not in the final step, in which the arithmetic expressions are executed to obtain the answer.