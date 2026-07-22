---
title: "Every Answer Matters: Evaluating Commonsense with Probabilistic Measures"
source: "https://aclanthology.org/2024.acl-long.29/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['commonsense-reasoning', 'probabilistic-evaluation', 'multiple-choice']
venue: "ACL 2024"
tldr: "This paper proposes probabilistic evaluation measures for commonsense tasks to account for multiple valid answers and reduce bias exploitation."
---

# Every Answer Matters: Evaluating Commonsense with Probabilistic Measures

**Source**: [https://aclanthology.org/2024.acl-long.29/](https://aclanthology.org/2024.acl-long.29/)

**TLDR**: This paper proposes probabilistic evaluation measures for commonsense tasks to account for multiple valid answers and reduce bias exploitation.

## Abstract

AbstractLarge language models have demonstrated impressive performance on commonsense tasks; however, these tasks are often posed as multiple-choice questions, allowing models to exploit systematic biases. Commonsense is also inherently probabilistic with multiple correct answers. The purpose of “boiling water” could be making tea, cooking but also could be killing germs. Existing tasks do not capture the probabilistic nature of common sense. To this end, we present commonsense frame completion (CFC), a new generative task that evaluates common sense via multiple open-ended generations. We also propose a method of probabilistic evaluation that strongly correlates with human judgments. Humans drastically outperform strong language model baselines on our dataset, indicating this approach is both a challenging and useful evaluation of machine common sense.