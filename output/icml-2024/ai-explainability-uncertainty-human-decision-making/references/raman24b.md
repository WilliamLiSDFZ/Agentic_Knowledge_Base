---
title: "STEER: Assessing the Economic Rationality of Large Language Models"
source: "https://proceedings.mlr.press/v235/raman24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/raman24b/raman24b.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'ai-explainability-uncertainty-human-decision-making']
tags: ['LLM-agents', 'economic-rationality', 'decision-making', 'evaluation', 'chain-of-thought']
venue: "ICML 2024"
tldr: "STEER is a benchmark assessing the economic rationality of LLMs across various prompting and reasoning strategies."
---

# STEER: Assessing the Economic Rationality of Large Language Models

**Source**: [https://proceedings.mlr.press/v235/raman24b.html](https://proceedings.mlr.press/v235/raman24b.html)

**TLDR**: STEER is a benchmark assessing the economic rationality of LLMs across various prompting and reasoning strategies.

## Abstract

There is increasing interest in using LLMs as decision-making "agents". Doing so includes many degrees of freedom: which model should be used; how should it be prompted; should it be asked to introspect, conduct chain-of-thought reasoning, etc? Settling these questions—and more broadly, determining whether an LLM agent is reliable enough to be trusted—requires a methodology for assessing such an agent’s economic rationality. In this paper, we provide one. We begin by surveying the economic literature on rational decision making, taxonomizing a large set of fine-grained "elements" that an agent should exhibit, along with dependencies between them. We then propose a benchmark distribution that quantitatively scores an LLMs performance on these elements and, combined with a user-provided rubric, produces a "rationality report card". Finally, we describe the results of a large-scale empirical experiment with 14 different LLMs, characterizing the both current state of the art and the impact of different model sizes on models’ ability to exhibit rational behavior.