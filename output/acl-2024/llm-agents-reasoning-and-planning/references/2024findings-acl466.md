---
title: "LSTPrompt: Large Language Models as Zero-Shot Time Series Forecasters by Long-Short-Term Prompting"
source: "https://aclanthology.org/2024.findings-acl.466/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'llm-training-alignment-and-evaluation']
tags: ['time-series-forecasting', 'zero-shot', 'prompting']
venue: "ACL 2024"
tldr: "LSTPrompt enables LLMs to perform zero-shot time-series forecasting by prompting with both long-term and short-term temporal patterns."
---

# LSTPrompt: Large Language Models as Zero-Shot Time Series Forecasters by Long-Short-Term Prompting

**Source**: [https://aclanthology.org/2024.findings-acl.466/](https://aclanthology.org/2024.findings-acl.466/)

**TLDR**: LSTPrompt enables LLMs to perform zero-shot time-series forecasting by prompting with both long-term and short-term temporal patterns.

## Abstract

AbstractTime-series forecasting (TSF) finds broad applications in real-world scenarios. Prompting off-the-shelf Large Language Models (LLMs) demonstrates strong zero-shot TSF capabilities while preserving computational efficiency. However, existing prompting methods oversimplify TSF as language next-token predictions, overlooking its dynamic nature and lack of integration with state-of-the-art prompt strategies such as Chain-of-Thought. Thus, we propose LSTPrompt, a novel approach for prompting LLMs in zero-shot TSF tasks. LSTPrompt decomposes TSF into short-term and long-term forecasting sub-tasks, tailoring prompts to each. LSTPrompt guides LLMs to regularly reassess forecasting mechanisms to enhance adaptability. Extensive evaluations demonstrate consistently better performance of LSTPrompt than existing prompting methods, and competitive results compared to foundation TSF models.