---
title: "MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation"
source: "https://proceedings.mlr.press/v235/huang24y.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24y/huang24y.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-driven-automated-system-optimization']
tags: ['language-agents', 'ml-experimentation', 'benchmark', 'autonomous-agents', 'evaluation']
venue: "ICML 2024"
tldr: "Presents MLAgentBench, a benchmark for evaluating LLM-driven agents on end-to-end machine learning experimentation tasks."
---

# MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation

**Source**: [https://proceedings.mlr.press/v235/huang24y.html](https://proceedings.mlr.press/v235/huang24y.html)

**TLDR**: Presents MLAgentBench, a benchmark for evaluating LLM-driven agents on end-to-end machine learning experimentation tasks.

## Abstract

A central aspect of machine learning research is experimentation, the process of designing and running experiments, analyzing the results, and iterating towards some positive outcome (e.g., improving accuracy). Could agents driven by powerful language models perform machine learning experimentation effectively? To answer this question, we introduce MLAgentBench, a suite of 13 tasks ranging from improving model performance on CIFAR-10 to recent research problems like BabyLM. For each task, an agent can perform actions like reading/writing files, executing code, and inspecting outputs. We then construct an agent that can perform ML experimentation based on ReAct framework. We benchmark agents based on Claude v1.0, Claude v2.1, Claude v3 Opus, GPT-4, GPT-4-turbo, Gemini-Pro, and Mixtral and find that a Claude v3 Opus agent is the best in terms of success rate. It can build compelling ML models over many tasks in MLAgentBench with 37.5% average success rate. Our agents also display highly interpretable plans and actions. However, the success rates vary considerably; they span from 100% on well-established older datasets to as low as 0% on recent Kaggle challenges created potentially after the underlying LM was trained. Finally, we identify several key challenges for LM-based agents such as long-term planning and reducing hallucination.