---
title: "Exploring Reasoning Biases in Large Language Models Through Syllogism: Insights from the NeuBAROCO Dataset"
source: "https://aclanthology.org/2024.findings-acl.950/"
categories: ['language-model-human-cognitive-linguistic-alignment', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['syllogistic-reasoning', 'cognitive-bias', 'llm-evaluation']
venue: "ACL 2024"
tldr: "LLMs exhibit human-like reasoning biases in syllogistic tasks, as revealed by evaluation on the NeuBAROCO dataset."
---

# Exploring Reasoning Biases in Large Language Models Through Syllogism: Insights from the NeuBAROCO Dataset

**Source**: [https://aclanthology.org/2024.findings-acl.950/](https://aclanthology.org/2024.findings-acl.950/)

**TLDR**: LLMs exhibit human-like reasoning biases in syllogistic tasks, as revealed by evaluation on the NeuBAROCO dataset.

## Abstract

AbstractThis paper explores the question of how accurately current large language models can perform logical reasoning in natural language, with an emphasis on whether these models exhibit reasoning biases similar to humans. Specifically, our study focuses on syllogistic reasoning, a form of deductive reasoning extensively studied in cognitive science as a natural form of human reasoning. We present a syllogism dataset called NeuBAROCO, which consists of syllogistic reasoning problems in English and Japanese. This dataset was originally designed for psychological experiments to assess human reasoning capabilities using various forms of syllogisms. Our experiments with leading large language models indicate that these models exhibit reasoning biases similar to humans, along with other error tendencies. Notably, there is significant room for improvement in reasoning problems where the relationship between premises and hypotheses is neither entailment nor contradiction. We also present experimental results and in-depth analysis using a new Chain-of-Thought prompting method, which asks LLMs to translate syllogisms into abstract logical expressions and then explain their reasoning process. Our analysis using this method suggests that the primary limitations of LLMs lie in the reasoning process itself rather than the interpretation of syllogisms.