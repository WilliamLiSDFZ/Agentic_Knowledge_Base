---
title: "ChartInstruct: Instruction Tuning for Chart Comprehension and Reasoning"
source: "https://aclanthology.org/2024.findings-acl.619/"
categories: ['multimodal-language-vision-learning-systems', 'educational-question-generation-and-comprehension']
tags: ['chart-comprehension', 'instruction-tuning', 'multimodal', 'question-answering', 'visual-reasoning']
venue: "ACL 2024"
tldr: "Introduces ChartInstruct, an instruction-tuned multimodal model for chart comprehension and reasoning across diverse chart-related tasks."
---

# ChartInstruct: Instruction Tuning for Chart Comprehension and Reasoning

**Source**: [https://aclanthology.org/2024.findings-acl.619/](https://aclanthology.org/2024.findings-acl.619/)

**TLDR**: Introduces ChartInstruct, an instruction-tuned multimodal model for chart comprehension and reasoning across diverse chart-related tasks.

## Abstract

AbstractCharts provide visual representations of data and are widely used for analyzing information, addressing queries, and conveying insights to others. Various chart-related downstream tasks have emerged recently, such as question-answering and summarization. A common strategy to solve these tasks is to fine-tune various models originally trained on vision tasks language. However, such task-specific models are not capable of solving a wide range of chart-related tasks, constraining their real-world applicability. To overcome these challenges, we introduce ChartInsruct: a novel chart-specific vision-language Instruction-following dataset comprising 191K instructions generated with 71K charts. We then present two distinct systems for instruction tuning on such datasets: (1) an end-to-end model that connects a vision encoder for chart understanding with a LLM; and (2) a pipeline model that employs a two-step approach to extract chart data tables and input them into the LLM. In experiments on four downstream tasks, we first show the effectiveness of our model–achieving a new set of state-of-the-art results. Further evaluation shows that our instruction-tuning approach supports a wide array of real-world chart comprehension and reasoning scenarios, thereby expanding the scope and applicability of our models to new kinds of tasks.