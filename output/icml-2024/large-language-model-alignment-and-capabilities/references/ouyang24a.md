---
title: "Structured Chemistry Reasoning with Large Language Models"
source: "https://proceedings.mlr.press/v235/ouyang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ouyang24a/ouyang24a.pdf"
categories: ['large-language-model-alignment-and-capabilities']
tags: ['large-language-models', 'chemistry-reasoning', 'structured-reasoning', 'scientific-AI']
venue: "ICML 2024"
tldr: "Presents a structured reasoning framework enabling LLMs to tackle complex multi-step chemistry problems."
---

# Structured Chemistry Reasoning with Large Language Models

**Source**: [https://proceedings.mlr.press/v235/ouyang24a.html](https://proceedings.mlr.press/v235/ouyang24a.html)

**TLDR**: Presents a structured reasoning framework enabling LLMs to tackle complex multi-step chemistry problems.

## Abstract

Large Language Models (LLMs) excel in diverse areas, yet struggle with complex scientific reasoning, especially in the field of chemistry. Different from the simple chemistry tasks (e.g., molecule classification) addressed in previous studies, complex chemistry problems require not only vast knowledge and precise calculation, but also compositional reasoning about rich dynamic interactions of different concepts (e.g., temperature changes). Our study shows that even advanced LLMs, like GPT-4, can fail easily in different ways. Interestingly, the errors often stem not from a lack of domain knowledge within the LLMs, but rather from the absence of an effective reasoning structure that guides the LLMs to elicit the right knowledge, incorporate the knowledge in step-by-step reasoning, and iteratively refine results for further improved quality. On this basis, we introduce StructChem, a simple yet effective prompting strategy that offers the desired guidance and substantially boosts the LLMs’ chemical reasoning capability. Testing across four chemistry areas—quantum chemistry, mechanics, physical chemistry, and kinetics—StructChem substantially enhances GPT-4’s performance, with up to 30% peak improvement. Our analysis also underscores the unique difficulties of precise grounded reasoning in science with LLMs, highlighting a need for more research in this area.