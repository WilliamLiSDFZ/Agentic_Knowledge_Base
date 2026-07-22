---
title: "An Empirical Analysis on Large Language Models in Debate Evaluation"
source: "https://aclanthology.org/2024.acl-short.44/"
categories: ['llm-training-alignment-and-evaluation', 'topic-modeling-and-essay-evaluation']
tags: ['debate-evaluation', 'LLM-bias', 'GPT-4', 'argumentation', 'benchmark']
venue: "ACL 2024"
tldr: "GPT-3.5 and GPT-4 outperform humans and fine-tuned models in debate evaluation but exhibit inherent positional biases."
---

# An Empirical Analysis on Large Language Models in Debate Evaluation

**Source**: [https://aclanthology.org/2024.acl-short.44/](https://aclanthology.org/2024.acl-short.44/)

**TLDR**: GPT-3.5 and GPT-4 outperform humans and fine-tuned models in debate evaluation but exhibit inherent positional biases.

## Abstract

AbstractIn this study, we investigate the capabilities and inherent biases of advanced large language models (LLMs) such as GPT-3.5 and GPT-4 in the context of debate evaluation. We discover that LLM’s performance exceeds humans and surpasses the performance of state-of-the-art methods fine-tuned on extensive datasets. We additionally explore and analyze biases present in LLMs, including positional bias, lexical bias, order bias, which may affect their evaluative judgments. Our findings reveal a consistent bias in both GPT-3.5 and GPT-4 towards the second candidate response presented, attributed to prompt design. We also uncover a lexical bias in both GPT-3.5 and GPT-4, especially when label sets carry connotations such as numerical or sequential, highlighting the critical need for careful label verbalizer selection in prompt design. Additionally, our analysis indicates a tendency of both models to favor the debate’s concluding side as the winner, suggesting an end-of-discussion bias.