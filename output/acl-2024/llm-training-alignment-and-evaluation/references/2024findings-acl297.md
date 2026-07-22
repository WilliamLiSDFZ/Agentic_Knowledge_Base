---
title: "Disentangling Length from Quality in Direct Preference Optimization"
source: "https://aclanthology.org/2024.findings-acl.297/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'bias-and-fairness-in-llms']
tags: ['RLHF', 'DPO', 'verbosity-bias', 'length-bias', 'preference-optimization']
venue: "ACL 2024"
tldr: "This paper identifies and addresses verbosity bias in Direct Preference Optimization by disentangling response length from response quality during alignment training."
---

# Disentangling Length from Quality in Direct Preference Optimization

**Source**: [https://aclanthology.org/2024.findings-acl.297/](https://aclanthology.org/2024.findings-acl.297/)

**TLDR**: This paper identifies and addresses verbosity bias in Direct Preference Optimization by disentangling response length from response quality during alignment training.

## Abstract

AbstractReinforcement Learning from Human Feedback (RLHF) has been a crucial component in the recent success of Large Language Models. However, RLHF is know to exploit biases in human preferences, such as verbosity. A well-formatted and eloquent answer is often more highly rated by users, even when it is less helpful and objective. A number of approaches have been developed to control those biases in the classical RLHF literature, but the problem remains relatively under-explored for Direct Alignment Algorithms such as Direct Preference Optimization (DPO). Unlike classical RLHF, DPO does not train a separate reward model or use reinforcement learning directly, so previous approaches developed to control verbosity cannot be directly applied to this setting. Our work makes several contributions. For the first time, we study the length problem in the DPO setting, showing significant exploitation in DPO and linking it to out-of-distribution bootstrapping. We then develop a principled but simple regularization strategy that prevents length exploitation, while still maintaining improvements in model quality. We demonstrate these affects across datasets on summarization and dialogue, where we achieve up to 20% improvement in win rates when controlling for length, despite the GPT4 judge’s well-known verbosity bias.