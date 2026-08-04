---
title: "BAGEL: Bootstrapping Agents by Guiding Exploration with Language"
source: "https://proceedings.mlr.press/v235/murty24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/murty24a/murty24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-driven-automated-system-optimization']
tags: ['LLM-agents', 'exploration', 'language-instructions', 'digital-environments']
venue: "ICML 2024"
tldr: "BAGEL bootstraps language model agents in digital environments by using language-guided exploration to generate demonstrations without human supervision."
---

# BAGEL: Bootstrapping Agents by Guiding Exploration with Language

**Source**: [https://proceedings.mlr.press/v235/murty24a.html](https://proceedings.mlr.press/v235/murty24a.html)

**TLDR**: BAGEL bootstraps language model agents in digital environments by using language-guided exploration to generate demonstrations without human supervision.

## Abstract

Following natural language instructions by executing actions in digital environments (e.g. web-browsers and REST APIs) is a challenging task for language model (LM) agents. Unfortunately, LM agents often fail to generalize to new environments without human demonstrations. This work presents BAGEL, a method for bootstrapping LM agents without human supervision. BAGEL converts a seed set of randomly explored trajectories to synthetic demonstrations via round-trips between two noisy LM components: an LM labeler which converts a trajectory into a synthetic instruction, and a zero-shot LM agent which maps the synthetic instruction into a refined trajectory. By performing these round-trips iteratively, BAGEL quickly converts the initial distribution of trajectories towards those that are well-described by natural language. We adapt the base LM agent at test time with in-context learning by retrieving relevant BAGEL demonstrations based on the instruction, and find improvements of over 2-13% absolute on ToolQA and MiniWob++, with up to 13x reduction in execution failures.