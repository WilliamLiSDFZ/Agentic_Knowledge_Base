---
title: "Subgoal-based Demonstration Learning for Formal Theorem Proving"
source: "https://proceedings.mlr.press/v235/zhao24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhao24h/zhao24h.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'neural-symbolic-combinatorial-optimization-learning']
tags: ['theorem-proving', 'LLM', 'in-context-learning']
venue: "ICML 2024"
tldr: "Improves LLM-based formal theorem proving by organizing demonstrative examples around subgoal-based structures."
---

# Subgoal-based Demonstration Learning for Formal Theorem Proving

**Source**: [https://proceedings.mlr.press/v235/zhao24h.html](https://proceedings.mlr.press/v235/zhao24h.html)

**TLDR**: Improves LLM-based formal theorem proving by organizing demonstrative examples around subgoal-based structures.

## Abstract

Large language models (LLMs) present a promising pathway for advancing the domain of formal theorem proving. In this paper, we aim to improve the performance of LLMs in formal theorem proving by thoroughly examining the structure and organization of demonstrative in-context examples. We introduce a subgoal-based demonstration learning framework, specifically designed to enhance the efficiency of proof search in LLMs. First, drawing upon the insights of subgoal learning from reinforcement learning and robotics, we propose the construction of distinct subgoals for each demonstration example and refine these subgoals in accordance with the pertinent theories of subgoal learning. Second, we build upon recent advances in diffusion models to predict the optimal organization, simultaneously addressing two intricate issues that persist within the domain of demonstration organization: subset selection and order determination. Our integration of subgoal-based learning has notably increased proof accuracy from 38.9% to 44.1% on the miniF2F benchmark. Furthermore, the adoption of diffusion models for demonstration organization can lead to an additional enhancement in accuracy to 45.5%, or a $5\times$ improvement in sampling efficiency compared to previously established methods.