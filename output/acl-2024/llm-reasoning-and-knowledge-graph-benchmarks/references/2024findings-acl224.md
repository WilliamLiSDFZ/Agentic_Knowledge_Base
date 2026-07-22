---
title: "LLM as Prompter: Low-resource Inductive Reasoning on Arbitrary Knowledge Graphs"
source: "https://aclanthology.org/2024.findings-acl.224/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-agents-reasoning-and-planning']
tags: ['knowledge-graph', 'inductive-reasoning', 'low-resource']
venue: "ACL 2024"
tldr: "A method using LLMs as prompters to enable inductive reasoning on arbitrary knowledge graphs in low-resource settings."
---

# LLM as Prompter: Low-resource Inductive Reasoning on Arbitrary Knowledge Graphs

**Source**: [https://aclanthology.org/2024.findings-acl.224/](https://aclanthology.org/2024.findings-acl.224/)

**TLDR**: A method using LLMs as prompters to enable inductive reasoning on arbitrary knowledge graphs in low-resource settings.

## Abstract

AbstractKnowledge Graph (KG) inductive reasoning, which aims to infer missing facts from new KGs that are not seen during training, has been widely adopted in various applications. One critical challenge of KG inductive reasoning is handling low-resource scenarios with scarcity in both textual and structural aspects. In this paper, we attempt to address this challenge with Large Language Models (LLMs). Particularly, we utilize the state-of-the-art LLMs to generate a graph-structural prompt to enhance the pre-trained Graph Neural Networks (GNNs), which brings us new methodological insights into the KG inductive reasoning methods, as well as high generalizability in practice. On the methodological side, we introduce a novel pretraining and prompting framework ProLINK, designed for low-resource inductive reasoning across arbitrary KGs without requiring additional training. On the practical side, we experimentally evaluate our approach on 36 low-resource KG datasets and find that ProLINK outperforms previous methods in three-shot, one-shot, and zero-shot reasoning tasks, exhibiting average performance improvements by 20%, 45%, and 147%, respectively. Furthermore, ProLINK demonstrates strong robustness for various LLM promptings as well as full-shot scenarios.