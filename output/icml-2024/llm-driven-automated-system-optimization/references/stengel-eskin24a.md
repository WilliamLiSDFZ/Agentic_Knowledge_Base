---
title: "ReGAL: Refactoring Programs to Discover Generalizable Abstractions"
source: "https://proceedings.mlr.press/v235/stengel-eskin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/stengel-eskin24a/stengel-eskin24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-driven-automated-system-optimization']
tags: ['program-synthesis', 'LLM', 'code-abstraction', 'refactoring', 'generalization']
venue: "ICML 2024"
tldr: "ReGAL refactors LLM-synthesized programs to discover reusable abstractions that improve generalization and efficiency in program synthesis."
---

# ReGAL: Refactoring Programs to Discover Generalizable Abstractions

**Source**: [https://proceedings.mlr.press/v235/stengel-eskin24a.html](https://proceedings.mlr.press/v235/stengel-eskin24a.html)

**TLDR**: ReGAL refactors LLM-synthesized programs to discover reusable abstractions that improve generalization and efficiency in program synthesis.

## Abstract

While large language models (LLMs) are increasingly being used for program synthesis, they lack the global view needed to develop useful abstractions; they generally predict programs one at a time, often repeating the same functionality. Generating redundant code from scratch is both inefficient and error-prone. To address this, we propose Refactoring for Generalizable Abstraction Learning (ReGAL), a gradient-free method for learning a library of reusable functions via code refactorization, i.e., restructuring code without changing its execution output. ReGAL learns from a small set of existing programs, iteratively verifying and refining its abstractions via execution. We find that the shared function libraries discovered by ReGAL make programs easier to predict across diverse domains. On five datasets – LOGO graphics generation, Date reasoning, TextCraft (a Minecraft-based text-game) MATH, and TabMWP – both open-source and proprietary LLMs improve in accuracy when predicting programs with REGAL functions. For CodeLlama-13B, REGAL results in absolute accuracy increases of 11.5% on LOGO, 26.1% on date understanding, and 8.1% on TextCraft, out-performing GPT-3.5 in two of three domains. Our analysis reveals REGAL’s abstractions encapsulate frequently-used subroutines as well as environment dynamics.