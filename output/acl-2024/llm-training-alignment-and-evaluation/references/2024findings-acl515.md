---
title: "Fact-and-Reflection (FaR) Improves Confidence Calibration of Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.515/"
categories: ['llm-hallucination-detection-and-mitigation', 'llm-training-alignment-and-evaluation']
tags: ['confidence-calibration', 'prompting', 'fact-and-reflection']
venue: "ACL 2024"
tldr: "A Fact-and-Reflection prompting strategy improves confidence calibration of LLMs by encouraging self-reflection before committing to answers."
---

# Fact-and-Reflection (FaR) Improves Confidence Calibration of Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.515/](https://aclanthology.org/2024.findings-acl.515/)

**TLDR**: A Fact-and-Reflection prompting strategy improves confidence calibration of LLMs by encouraging self-reflection before committing to answers.

## Abstract

AbstractFor a LLM to be trustworthy, its confidence level should be well-calibrated with its actual performance. While it is now common sense that LLM performances are greatly impacted by prompts, the confidence calibration in prompting LLMs has yet to be thoroughly explored.In this paper, we explore how different prompting strategies influence LLM confidence calibration and how it could be improved. We conduct extensive experiments on six prompting methods in the question-answering context and we observe that, while these methods help improve the expected LLM calibration, they also trigger LLMs to be over-confident when responding to some instances.Inspired by human cognition, we propose Fact-and-Reflection (FaR) prompting, which improves the LLM calibration in two steps. First, FaR elicits the known “facts” that are relevant to the input prompt from the LLM. And then it asks the model to “reflect” over them to generate the final answer.Experiments show that FaR prompting achieves significantly better calibration; it lowers the Expected Calibration Error by 23.5% on our multi-purpose QA tasks. Notably, FaR prompting even elicits the capability of verbally expressing concerns in less confident scenarios, which helps trigger retrieval augmentation for solving these harder instances.