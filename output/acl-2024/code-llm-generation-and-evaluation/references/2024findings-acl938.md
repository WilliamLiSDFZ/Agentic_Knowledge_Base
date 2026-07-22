---
title: "Fine-tuning Language Models for Joint Rewriting and Completion of Code with Potential Bugs"
source: "https://aclanthology.org/2024.findings-acl.938/"
pdf_url: ""
categories: ['code-llm-generation-and-evaluation', 'llm-training-alignment-and-evaluation']
tags: ['code-completion', 'bug-repair', 'fine-tuning', 'CodeLLM']
venue: "ACL 2024"
tldr: "Fine-tunes language models for jointly rewriting and completing partial code containing potential bugs in real-time code suggestion applications."
---

# Fine-tuning Language Models for Joint Rewriting and Completion of Code with Potential Bugs

**Source**: [https://aclanthology.org/2024.findings-acl.938/](https://aclanthology.org/2024.findings-acl.938/)

**TLDR**: Fine-tunes language models for jointly rewriting and completing partial code containing potential bugs in real-time code suggestion applications.

## Abstract

AbstractHandling drafty partial code remains a notable challenge in real-time code suggestion applications. Previous work has demonstrated shortcomings of large language models of code (CodeLLMs) in completing partial code with potential bugs. In this study, we view partial code as implementation hints and fine-tune CodeLLMs to jointly rewrite and complete partial code into functional full programs. We explore two strategies: one-pass generation and multi-pass iterative refinement. We construct new training and testing datasets using semantic-altering code transformations and iterative self-generations.We conduct comprehensive experiments over three representative open-sourced CodeLLMs – InCoder, CodeGen, and StarCoder.Results show that CodeLLMs fine-tuned using our approach achieve superior pass rates compared to the previous baselines across existing and newly-created benchmarks, effectively handle both potentially buggy and clean code, and largely preserve the integrity of the original partial implementations. We further present findings on the properties of the potential bugs we tested and on the design choices of our methods.