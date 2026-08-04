---
title: "AutoOS: Make Your OS More Powerful by Exploiting Large Language Models"
source: "https://proceedings.mlr.press/v235/chen24at.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24at/chen24at.pdf"
categories: ['llm-driven-automated-system-optimization', 'llm-serving-systems-and-infrastructure']
tags: ['LLM-optimization', 'operating-system', 'kernel-configuration', 'AIoT']
venue: "ICML 2024"
tldr: "Proposes AutoOS, leveraging LLMs to automatically optimize OS kernel configurations for diverse AIoT application scenarios."
---

# AutoOS: Make Your OS More Powerful by Exploiting Large Language Models

**Source**: [https://proceedings.mlr.press/v235/chen24at.html](https://proceedings.mlr.press/v235/chen24at.html)

**TLDR**: Proposes AutoOS, leveraging LLMs to automatically optimize OS kernel configurations for diverse AIoT application scenarios.

## Abstract

With the rapid development of Artificial Intelligence of Things (AIoT), customizing and optimizing operating system (OS) kernel configurations for various AIoT application scenarios is crucial for maximizing system performance. However, existing approaches falter due to the overwhelming problem complexity (i.e., over 15,000 configuration options in the Linux kernel), together with the huge evaluation costs and error-prone options that may result in OS boot-up failure, which all make it an unresolved problem to optimize the Linux kernel automatically. In this paper, we introduce AutoOS, a novel framework exploiting Large Language Models for customizing and optimizing OS kernel configurations automatically for various AIoT application scenarios.Inspired by the inherently directory-structured kernel configuration process, we first formulate our research problem as optimizing on a dynamic tree. We then propose a novel framework integrating a state machine-based traversal algorithm as the observe-prune-propose-act-correct loop, which can effectively refine the optimization space and ensure a successful OS boot-up.Experimental results show that AutoOS can automatically customize and optimize the OS kernel configurations without human effort. More importantly, AutoOS even achieves better performance by up to 25% than vendor-provided configuration.