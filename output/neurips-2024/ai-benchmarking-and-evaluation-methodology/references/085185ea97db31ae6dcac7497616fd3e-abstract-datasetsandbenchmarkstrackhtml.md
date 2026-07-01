---
title: "TaskBench: Benchmarking Large Language Models for Task Automation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/085185ea97db31ae6dcac7497616fd3e-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['llm-benchmarking', 'task-automation', 'tool-use']
venue: "NeurIPS 2024"
tldr: "Introduces TaskBench, a benchmark for evaluating large language models on complex task automation involving sub-task decomposition and tool invocation."
---

# TaskBench: Benchmarking Large Language Models for Task Automation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/085185ea97db31ae6dcac7497616fd3e-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/085185ea97db31ae6dcac7497616fd3e-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces TaskBench, a benchmark for evaluating large language models on complex task automation involving sub-task decomposition and tool invocation.

## Abstract

In recent years, the remarkable progress of large language models (LLMs) has sparked interest in task automation, which involves decomposing complex tasks described by user instructions into sub-tasks and invoking external tools to execute them, playing a central role in autonomous agents. However, there is a lack of systematic and standardized benchmarks to promote the development of LLMs in task automation. To address this, we introduce TaskBench, a comprehensive framework to evaluate the capability of LLMs in task automation. Specifically, task automation can be divided into three critical stages: task decomposition, tool selection, and parameter prediction. To tackle the complexities inherent in these stages, we introduce the concept of Tool Graph to represent decomposed tasks and adopt a back-instruct method to generate high-quality user instructions. We propose TaskEval, a multi-faceted evaluation methodology that assesses LLM performance across these three stages. Our approach combines automated construction with rigorous human verification, ensuring high consistency with human evaluation. Experimental results demonstrate that TaskBench effectively reflects the capabilities of various LLMs in task automation. It provides insights into model performance across different task complexities and domains, pushing the boundaries of what current models can achieve. TaskBench offers a scalable, adaptable, and reliable benchmark for advancing LLM-based autonomous agents.