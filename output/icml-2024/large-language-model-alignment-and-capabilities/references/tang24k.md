---
title: "MathScale: Scaling Instruction Tuning for Mathematical Reasoning"
source: "https://proceedings.mlr.press/v235/tang24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tang24k/tang24k.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'data-selection-and-active-learning-methods']
tags: ['mathematical-reasoning', 'instruction-tuning', 'data-synthesis']
venue: "ICML 2024"
tldr: "MathScale is a scalable method for generating high-quality mathematical reasoning training data using frontier LLMs to improve mathematical problem-solving capabilities."
---

# MathScale: Scaling Instruction Tuning for Mathematical Reasoning

**Source**: [https://proceedings.mlr.press/v235/tang24k.html](https://proceedings.mlr.press/v235/tang24k.html)

**TLDR**: MathScale is a scalable method for generating high-quality mathematical reasoning training data using frontier LLMs to improve mathematical problem-solving capabilities.

## Abstract

Large language models (LLMs) have demonstrated remarkable capabilities in problem-solving. However, their proficiency in solving mathematical problems remains inadequate. We propose MathScale, a simple and scalable method to create high-quality mathematical reasoning data using frontier LLMs (e.g., GPT-3.5). Inspired by the cognitive mechanism in human mathematical learning, it first extracts topics and knowledge points from seed math questions and then build a concept graph, which is subsequently used to generate new math questions. MathScale exhibits effective scalability along the size axis of the math dataset that we generate. As a result, we create a mathematical reasoning dataset (MathScaleQA) containing two million math question-answer pairs. To evaluate mathematical reasoning abilities of LLMs comprehensively, we construct MWPBench, a benchmark of Math Word Problems, which is a collection of 9 datasets (including GSM8K and MATH) covering K-12, college, and competition level math problems. We apply MathScaleQA to fine-tune open-source LLMs (e.g., LLaMA-2 and Mistral), resulting in significantly improved capabilities in mathematical reasoning. Evaluated on MWPBench, MathScale-7B achieves state-of-the-art performance across all datasets, surpassing its best peers of equivalent size by 42.8% in micro average accuracy and 43.6% in macro average accuracy, respectively.