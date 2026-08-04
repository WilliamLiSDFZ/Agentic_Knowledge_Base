---
title: "Debating with More Persuasive LLMs Leads to More Truthful Answers"
source: "https://proceedings.mlr.press/v235/khan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/khan24a/khan24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['LLM-debate', 'truthfulness', 'scalable-oversight']
venue: "ICML 2024"
tldr: "Demonstrates that debates between more persuasive LLMs lead non-expert humans to more truthful answers, supporting scalable oversight approaches."
---

# Debating with More Persuasive LLMs Leads to More Truthful Answers

**Source**: [https://proceedings.mlr.press/v235/khan24a.html](https://proceedings.mlr.press/v235/khan24a.html)

**TLDR**: Demonstrates that debates between more persuasive LLMs lead non-expert humans to more truthful answers, supporting scalable oversight approaches.

## Abstract

Common methods for aligning large language models (LLMs) with desired behaviour heavily rely on human-labelled data. However, as models grow increasingly sophisticated, they will surpass human expertise, and the role of human evaluation will evolve into non-experts overseeing experts. In anticipation of this, we ask: can weaker models assess the correctness of stronger models? We investigate this question in an analogous setting, where stronger models (experts) possess the necessary information to answer questions and weaker models (non-experts) lack this information. The method we evaluate is debate, where two LLM experts each argue for a different answer, and a non-expert selects the answer. We find that debate consistently helps both non-expert models and humans answer questions, achieving 76% and 88% accuracy respectively (naive baselines obtain 48% and 60%). Furthermore, optimising expert debaters for persuasiveness in an unsupervised manner improves non-expert ability to identify the truth in debates. Our results provide encouraging empirical evidence for the viability of aligning models with debate in the absence of ground truth.