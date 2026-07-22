---
title: "Revisiting OPRO: The Limitations of Small-Scale LLMs as Optimizers"
source: "https://aclanthology.org/2024.findings-acl.100/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'llm-agents-reasoning-and-planning']
tags: ['prompt-optimization', 'llm-limitations', 'opro']
venue: "ACL 2024"
tldr: "Revisits the OPRO prompting optimization approach and reveals limitations of small-scale LLMs as optimizers."
---

# Revisiting OPRO: The Limitations of Small-Scale LLMs as Optimizers

**Source**: [https://aclanthology.org/2024.findings-acl.100/](https://aclanthology.org/2024.findings-acl.100/)

**TLDR**: Revisits the OPRO prompting optimization approach and reveals limitations of small-scale LLMs as optimizers.

## Abstract

AbstractNumerous recent works aim to enhance the efficacy of Large Language Models (LLMs) through strategic prompting. In particular, the Optimization by PROmpting (OPRO) approach provides state-of-the-art performance by leveraging LLMs as optimizers where the optimization task is to find instructions that maximize the task accuracy. In this paper, we revisit OPRO for automated prompting with relatively small-scale LLMs, such as LLaMa-2 family and Mistral 7B. Our investigation reveals that OPRO shows limited effectiveness in small-scale LLMs, with limited inference capabilities constraining optimization ability. We suggest future automatic prompting engineering to consider both model capabilities and computational costs. Additionally, for small-scale LLMs, we recommend direct instructions that clearly outline objectives and methodologies as robust prompt baselines, ensuring efficient and effective prompt engineering in ongoing research.