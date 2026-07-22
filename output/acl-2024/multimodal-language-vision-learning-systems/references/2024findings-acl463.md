---
title: "ChartAssistant: A Universal Chart Multimodal Language Model via Chart-to-Table Pre-training and Multitask Instruction Tuning"
source: "https://aclanthology.org/2024.findings-acl.463/"
categories: ['multimodal-language-vision-learning-systems']
tags: ['chart-understanding', 'multimodal-llm', 'chart-to-table']
venue: "ACL 2024"
tldr: "ChartAssistant uses chart-to-table pre-training and multitask instruction tuning to build a universal chart multimodal language model."
---

# ChartAssistant: A Universal Chart Multimodal Language Model via Chart-to-Table Pre-training and Multitask Instruction Tuning

**Source**: [https://aclanthology.org/2024.findings-acl.463/](https://aclanthology.org/2024.findings-acl.463/)

**TLDR**: ChartAssistant uses chart-to-table pre-training and multitask instruction tuning to build a universal chart multimodal language model.

## Abstract

AbstractCharts play a vital role in data visualization, understanding data patterns, and informed decision-making. However, their unique combination of graphical elements (e.g., bars, lines) and textual components (e.g., labels, legends) poses challenges for general-purpose multimodal models. While vision-language models trained on chart data excel in comprehension, they struggle with generalization. To address these challenges, we propose ChartAssistant, a chart-based vision-language model for universal chart comprehension and reasoning. ChartAssistant leverages ChartSFT, a comprehensive dataset covering diverse chart-related tasks with basic (e.g. bars and pies) and specialized (e.g. radars, and bubbles) chart types. It undergoes a two-stage training process, starting with pre-training on chart-to-table parsing to align chart and text, followed by multitask instruction-following fine-tuning. This approach enables ChartAssistant to achieve competitive performance across various chart tasks. Experimental results demonstrate significant performance gains over the state-of-the-art UniChart and ChartLlama methods, especially outperforming them on real-world chart data with zero-shot setting. The code and data are available at https://github.com/OpenGVLab/ChartAst.