---
title: "SMART: Submodular Data Mixture Strategy for Instruction Tuning"
source: "https://aclanthology.org/2024.findings-acl.766/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'text-clustering-with-limited-labels']
tags: ['instruction-tuning', 'data-mixture', 'submodular-optimization']
venue: "ACL 2024"
tldr: "SMART uses a submodular optimization strategy to select balanced and diverse data mixtures for instruction tuning of language models."
---

# SMART: Submodular Data Mixture Strategy for Instruction Tuning

**Source**: [https://aclanthology.org/2024.findings-acl.766/](https://aclanthology.org/2024.findings-acl.766/)

**TLDR**: SMART uses a submodular optimization strategy to select balanced and diverse data mixtures for instruction tuning of language models.

## Abstract

AbstractInstruction Tuning involves finetuning a language model on a collection of instruction-formatted datasets in order to enhance the generalizability of the model to unseen tasks. Studies have shown the importance of balancing different task proportions during finetuning, but finding the right balance remains challenging. Unfortunately, there’s currently no systematic method beyond manual tuning or relying on practitioners’ intuition. In this paper, we introduce SMART (Submodular data Mixture strAtegy for instRuction Tuning) — a novel data mixture strategy which makes use of a submodular function to assign importance scores to tasks which are then used to determine the mixture weights. Given a fine-tuning budget, SMART redistributes the budget among tasks and selects non-redundant samples from each task. Experimental results demonstrate that SMART significantly outperforms traditional methods such as examples proportional mixing and equal mixing. Furthermore, SMART facilitates the creation of data mixtures based on a few representative subsets of tasks alone and through task pruning analysis, we reveal that in a limited budget setting, allocating budget among a subset of representative tasks yields superior performance compared to distributing the budget among all tasks. The code for reproducing our results is open-sourced at https://github.com/kowndinya-renduchintala/SMART.