---
title: "Remembering to Be Fair: Non-Markovian Fairness in Sequential Decision Making"
source: "https://proceedings.mlr.press/v235/alamdari24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/alamdari24a/alamdari24a.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['fairness', 'sequential-decision-making', 'non-Markovian']
venue: "ICML 2024"
tldr: "This paper introduces a non-Markovian notion of fairness in sequential decision making that accounts for historical context across multiple stakeholders."
---

# Remembering to Be Fair: Non-Markovian Fairness in Sequential Decision Making

**Source**: [https://proceedings.mlr.press/v235/alamdari24a.html](https://proceedings.mlr.press/v235/alamdari24a.html)

**TLDR**: This paper introduces a non-Markovian notion of fairness in sequential decision making that accounts for historical context across multiple stakeholders.

## Abstract

Fair decision making has largely been studied with respect to a single decision. Here we investigate the notion of fairness in the context of sequential decision making where multiple stakeholders can be affected by the outcomes of decisions. We observe that fairness often depends on the history of the sequential decision-making process, and in this sense that it is inherently non-Markovian. We further observe that fairness often needs to be assessed at time points within the process, not just at the end of the process. To advance our understanding of this class of fairness problems, we explore the notion of non-Markovian fairness in the context of sequential decision making. We identify properties of non-Markovian fairness, including notions of long-term, anytime, periodic, and bounded fairness. We explore the interplay between non-Markovian fairness and memory and how memory can support construction of fair policies. Finally, we introduce the FairQCM algorithm, which can automatically augment its training data to improve sample efficiency in the synthesis of fair policies via reinforcement learning.