---
title: "Improving Factuality and Reasoning in Language Models through Multiagent Debate"
source: "https://proceedings.mlr.press/v235/du24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/du24e/du24e.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['multiagent-debate', 'LLM-reasoning', 'factuality', 'chain-of-thought']
venue: "ICML 2024"
tldr: "A multiagent debate framework where multiple LLM instances iteratively argue and refine answers to improve factuality and reasoning."
---

# Improving Factuality and Reasoning in Language Models through Multiagent Debate

**Source**: [https://proceedings.mlr.press/v235/du24e.html](https://proceedings.mlr.press/v235/du24e.html)

**TLDR**: A multiagent debate framework where multiple LLM instances iteratively argue and refine answers to improve factuality and reasoning.

## Abstract

Large language models (LLMs) have demonstrated remarkable capabilities in language generation, understanding, and few-shot learning in recent years. An extensive body of work has explored how their performance may be further improved through the tools of prompting, ranging from verification, self-consistency, or intermediate scratchpads. In this paper, we present a complementary approach to improve language responses where multiple language model instances propose and debate their individual responses and reasoning processes over multiple rounds to arrive at a common final answer. Our findings indicate that this approach significantly enhances mathematical and strategic reasoning across a number of tasks. We also demonstrate that our approach improves the factual validity of generated content, reducing fallacious answers and hallucinations that contemporary models are prone to. Our approach may be directly applied to existing black-box models and uses identical procedure and prompts for all tasks we investigate. Overall, our findings suggest that such "society of minds" approach has the potential to significantly advance the capabilities of LLMs and pave the way for further breakthroughs in language generation and understanding.