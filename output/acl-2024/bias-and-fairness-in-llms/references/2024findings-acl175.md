---
title: "Disperse-Then-Merge: Pushing the Limits of Instruction Tuning via Alignment Tax Reduction"
source: "https://aclanthology.org/2024.findings-acl.175/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'bias-and-fairness-in-llms']
tags: ['instruction-tuning', 'alignment-tax', 'supervised-fine-tuning']
venue: "ACL 2024"
tldr: "Proposes a disperse-then-merge SFT strategy to reduce alignment tax and improve LLM performance on knowledge benchmarks."
---

# Disperse-Then-Merge: Pushing the Limits of Instruction Tuning via Alignment Tax Reduction

**Source**: [https://aclanthology.org/2024.findings-acl.175/](https://aclanthology.org/2024.findings-acl.175/)

**TLDR**: Proposes a disperse-then-merge SFT strategy to reduce alignment tax and improve LLM performance on knowledge benchmarks.

## Abstract

AbstractSupervised fine-tuning (SFT) on instruction-following corpus is a crucial approach toward the alignment of large language models (LLMs). However, the performance of LLMs on standard knowledge and reasoning benchmarks tends to suffer from deterioration at the latter stage of the SFT process, echoing the phenomenon of alignment tax. Through our pilot study, we put a hypothesis that the data biases are probably one cause behind the phenomenon. To address the issue, we introduce a simple disperse-then-merge framework. To be concrete, we disperse the instruction-following data into portions and then train multiple sub-models using different data portions. Lastly, we merge multiple models into a single one via model merging techniques. Despite its simplicity, our framework outperforms various sophisticated methods such as data curation and training regularization on a series of standard knowledge and reasoning benchmarks.