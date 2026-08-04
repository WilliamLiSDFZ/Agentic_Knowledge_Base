---
title: "In-Context Principle Learning from Mistakes"
source: "https://proceedings.mlr.press/v235/zhang24at.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24at/zhang24at.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'online-learning-and-sequential-decision-making']
tags: ['in-context-learning', 'principle-learning', 'mistake-correction']
venue: "ICML 2024"
tldr: "Proposes learning task-specific principles from LLM mistakes during in-context learning to improve few-shot prompting performance."
---

# In-Context Principle Learning from Mistakes

**Source**: [https://proceedings.mlr.press/v235/zhang24at.html](https://proceedings.mlr.press/v235/zhang24at.html)

**TLDR**: Proposes learning task-specific principles from LLM mistakes during in-context learning to improve few-shot prompting performance.

## Abstract

In-context learning (ICL, also known as few-shot prompting) has been the standard method of adapting LLMs to downstream tasks, by learning from a few input-output examples. Nonetheless, all ICL-based approaches only learn from correct input-output pairs. In this paper, we revisit this paradigm, by learning more from the few given input-output examples. We introduce Learning Principles (LEAP): First, we intentionally induce the model to make mistakes on these few examples; then we reflect on these mistakes, and learn explicit task-specific “principles” from them, which help solve similar problems and avoid common mistakes; finally, we prompt the model to answer unseen test questions using the original few-shot examples and these learned general principles. We evaluate LEAP on a wide range of benchmarks, including multi-hop question answering (Hotpot QA), textual QA (DROP), Big-Bench Hard reasoning, and math problems (GSM8K and MATH); in all these benchmarks, LEAP improves the strongest available LLMs such as GPT-3.5-turbo, GPT-4, GPT-4-turbo and Claude-2.1. For example, LEAP improves over the standard few-shot prompting using GPT-4 by 7.5% in DROP, and by 3.3% in HotpotQA. Importantly, LEAP does not require any more input or examples than the standard few-shot prompting settings.