---
title: "PuzzleVQA: Diagnosing Multimodal Reasoning Challenges of Language Models with Abstract Visual Patterns"
source: "https://aclanthology.org/2024.findings-acl.962/"
categories: ['multimodal-language-vision-learning-systems', 'nlp-benchmark-design-and-interpretability']
tags: ['multimodal-reasoning', 'abstract-visual-patterns', 'benchmark']
venue: "ACL 2024"
tldr: "PuzzleVQA diagnoses multimodal LLM reasoning limitations on abstract visual pattern recognition tasks through structured puzzle benchmarks."
---

# PuzzleVQA: Diagnosing Multimodal Reasoning Challenges of Language Models with Abstract Visual Patterns

**Source**: [https://aclanthology.org/2024.findings-acl.962/](https://aclanthology.org/2024.findings-acl.962/)

**TLDR**: PuzzleVQA diagnoses multimodal LLM reasoning limitations on abstract visual pattern recognition tasks through structured puzzle benchmarks.

## Abstract

AbstractLarge multimodal models extend the impressive capabilities of large language models by integrating multimodal understanding abilities. However, it is not clear how they can emulate the general intelligence and reasoning ability of humans. As recognizing patterns and abstracting concepts are key to general intelligence, we introduce PuzzleVQA, a collection of 2000 puzzle instances based on abstract patterns. With this dataset, we evaluate large multimodal models with abstract patterns based on fundamental concepts, including colors, numbers, sizes, and shapes. Through our experiments on state-of-the-art large multimodal models, we find that they are not able to generalize well to simple abstract patterns. Notably, GPT-4V achieves a score of 46.4% on single-concept puzzles, which shows that state-of-the-art models struggle on our dataset. To diagnose the reasoning challenges in large multimodal models, we progressively guide the models with our ground truth reasoning explanations for visual perception, inductive reasoning, and deductive reasoning. Our systematic analysis finds that the main bottlenecks of GPT-4V are weaker visual perception and inductive reasoning abilities. Through this work, we hope to shed light on the limitations of large multimodal models and how they can better emulate human cognitive processes in the future.