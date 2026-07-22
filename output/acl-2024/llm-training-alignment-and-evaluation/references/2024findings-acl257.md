---
title: "Multi-Objective Linguistic Control of Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.257/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'efficient-communication-principles-in-language']
tags: ['linguistic-control', 'output-complexity', 'controllable-generation']
venue: "ACL 2024"
tldr: "A framework for precisely controlling multiple linguistic attributes of LLM outputs to produce responses of desired complexity."
---

# Multi-Objective Linguistic Control of Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.257/](https://aclanthology.org/2024.findings-acl.257/)

**TLDR**: A framework for precisely controlling multiple linguistic attributes of LLM outputs to produce responses of desired complexity.

## Abstract

AbstractLarge language models (LLMs), despite their breakthroughs on many challenging benchmark tasks, prefer to generate verbose responses and lack the controllability of output complexity, which is usually preferred by human users in practice. In this paper, we study how to precisely control multiple linguistic complexities of LLM output by finetuning using off-the-shelf data. To this end, we propose multi-control tuning (MCTune), which includes multiple linguistic complexity values of ground-truth responses as controls in the input for instruction tuning. We finetune LLaMA2-7B on Alpaca-GPT4 and WizardLM datasets. Evaluations on widely used benchmarks demonstrate that our method does not only improve LLMs’ multi-complexity controllability substantially but also retains or even enhances the quality of the responses as a side benefit.