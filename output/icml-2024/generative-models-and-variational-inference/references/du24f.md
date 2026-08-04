---
title: "Learning Iterative Reasoning through Energy Diffusion"
source: "https://proceedings.mlr.press/v235/du24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/du24f/du24f.pdf"
categories: ['generative-models-and-variational-inference', 'neural-symbolic-combinatorial-optimization-learning']
tags: ['energy-based-models', 'diffusion', 'iterative-reasoning', 'decision-making']
venue: "ICML 2024"
tldr: "IRED frames reasoning and decision-making as energy-based optimization learned via diffusion to enable iterative refinement for diverse tasks."
---

# Learning Iterative Reasoning through Energy Diffusion

**Source**: [https://proceedings.mlr.press/v235/du24f.html](https://proceedings.mlr.press/v235/du24f.html)

**TLDR**: IRED frames reasoning and decision-making as energy-based optimization learned via diffusion to enable iterative refinement for diverse tasks.

## Abstract

We introduce iterative reasoning through energy diffusion (IRED), a novel framework for learning to reason for a variety of tasks by formulating reasoning and decision-making problems with energy-based optimization. IRED learns energy functions to represent the constraints between input conditions and desired outputs. After training, IRED adapts the number of optimization steps during inference based on problem difficulty, enabling it to solve problems outside its training distribution — such as more complex Sudoku puzzles, matrix completion with large value magnitudes, and path finding in larger graphs. Key to our method’s success is two novel techniques: learning a sequence of annealed energy landscapes for easier inference and a combination of score function and energy landscape supervision for faster and more stable training. Our experiments show that IRED outperforms existing methods in continuous-space reasoning, discrete-space reasoning, and planning tasks, particularly in more challenging scenarios.