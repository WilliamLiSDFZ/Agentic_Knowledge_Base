---
title: "LLMFactor: Extracting Profitable Factors through Prompts for Explainable Stock Movement Prediction"
source: "https://aclanthology.org/2024.findings-acl.185/"
categories: ['financial-reasoning-llm-benchmarks-and-datasets', 'natural-language-processing-information-extraction']
tags: ['stock-prediction', 'factor-extraction', 'financial-nlp']
venue: "ACL 2024"
tldr: "Uses LLM prompting to extract interpretable factors from financial text for explainable stock movement prediction."
---

# LLMFactor: Extracting Profitable Factors through Prompts for Explainable Stock Movement Prediction

**Source**: [https://aclanthology.org/2024.findings-acl.185/](https://aclanthology.org/2024.findings-acl.185/)

**TLDR**: Uses LLM prompting to extract interpretable factors from financial text for explainable stock movement prediction.

## Abstract

AbstractRecently, Large Language Models (LLMs) have attracted significant attention for their exceptional performance across a broad range of tasks, particularly in text analysis. However, the finance sector presents a distinct challenge due to its dependence on time-series data for complex forecasting tasks. In this study, we introduce a novel framework called LLMFactor, which employs Sequential Knowledge-Guided Prompting (SKGP) to identify factors that influence stock movements using LLMs. Unlike previous methods that relied on keyphrases or sentiment analysis, this approach focuses on extracting factors more directly related to stock market dynamics, providing clear explanations for complex temporal changes. Our framework directs the LLMs to create background knowledge through a fill-in-the-blank strategy and then discerns potential factors affecting stock prices from related news. Guided by background knowledge and identified factors, we leverage historical stock prices in textual format to predict stock movement. An extensive evaluation of the LLMFactor framework across four benchmark datasets from both the U.S. and Chinese stock markets demonstrates its superiority over existing state-of-the-art methods and its effectiveness in financial time-series forecasting.