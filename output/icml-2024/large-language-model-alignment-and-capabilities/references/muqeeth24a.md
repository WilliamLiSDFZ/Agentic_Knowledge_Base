---
title: "Learning to Route Among Specialized Experts for Zero-Shot Generalization"
source: "https://proceedings.mlr.press/v235/muqeeth24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/muqeeth24a/muqeeth24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'knowledge-distillation-methods-and-applications']
tags: ['mixture-of-experts', 'zero-shot-generalization', 'model-routing', 'parameter-efficient-finetuning']
venue: "ICML 2024"
tldr: "A routing mechanism is learned over collections of specialized expert language models to improve zero-shot generalization to unseen tasks."
---

# Learning to Route Among Specialized Experts for Zero-Shot Generalization

**Source**: [https://proceedings.mlr.press/v235/muqeeth24a.html](https://proceedings.mlr.press/v235/muqeeth24a.html)

**TLDR**: A routing mechanism is learned over collections of specialized expert language models to improve zero-shot generalization to unseen tasks.

## Abstract

Recently, there has been a widespread proliferation of "expert" language models that are specialized to a specific task or domain through parameter-efficient fine-tuning. How can we recycle large collections of expert language models to improve zero-shot generalization to unseen tasks? In this work, we propose $\textbf{P}$ost-$\textbf{H}$oc $\textbf{A}$daptive $\textbf{T}$okenwise $\textbf{G}$ating $\textbf{O}$ver an $\textbf{O}$cean of $\textbf{S}$pecialized $\textbf{E}$xperts (PHATGOOSE), which learns to route among specialized modules that were produced through parameter-efficient fine-tuning. Unlike past methods that learn to route among specialized models, PHATGOOSE explores the possibility that zero-shot generalization will be improved if different experts can be adaptively chosen for each token and at each layer in the model. Crucially, our method is post-hoc - it does not require simultaneous access to the datasets used to create the specialized models and only requires a modest amount of additional compute after each expert model is trained. In experiments covering a range of specialized model collections and zero-shot generalization benchmarks, we find that PHATGOOSE outperforms past methods for post-hoc routing and, in some cases, outperforms explicit multitask training (which requires simultaneous data access). To better understand the routing strategy learned by PHATGOOSE, we perform qualitative experiments to validate that PHATGOOSE’s performance stems from its ability to make adaptive per-token and per-module expert choices.