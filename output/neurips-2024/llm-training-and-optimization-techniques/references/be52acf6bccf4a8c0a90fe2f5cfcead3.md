---
title: "Large Language Model Unlearning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/be52acf6bccf4a8c0a90fe2f5cfcead3-Abstract-Conference.html"
categories: ['llm-safety-robustness-and-privacy-defenses', 'llm-training-and-optimization-techniques']
tags: ['machine-unlearning', 'llm-alignment', 'harmful-content-removal']
venue: "NeurIPS 2024"
tldr: "This work studies machine unlearning in LLMs to forget harmful behaviors, copyright content, and false information while preserving general model utility."
---

# Large Language Model Unlearning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/be52acf6bccf4a8c0a90fe2f5cfcead3-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/be52acf6bccf4a8c0a90fe2f5cfcead3-Abstract-Conference.html)

**TLDR**: This work studies machine unlearning in LLMs to forget harmful behaviors, copyright content, and false information while preserving general model utility.

## Abstract

We study how to perform unlearning, i.e. forgetting undesirable (mis)behaviors, on large language models (LLMs). We show at least three scenarios of aligning LLMs with human preferences can benefit from unlearning: (1) removing harmful responses, (2) erasing copyright-protected content as requested, and (3) reducing hallucinations. Unlearning, as an alignment technique, has three advantages. (1) It only requires negative (e.g. harmful) examples, which are much easier and cheaper to collect (e.g. via red teaming or user reporting) than positive (e.g. helpful and often human-written) examples required in the standard alignment process. (2) It is computationally efficient. (3) It is especially effective when we know which training samples cause the misbehavior. To the best of our knowledge, our work is among the first to explore LLM unlearning. We are also among the first to formulate the settings, goals, and evaluations in LLM unlearning. Despite only having negative samples, our ablation study shows that unlearning can still achieve better alignment performance than RLHF with just 2% of its computational time.