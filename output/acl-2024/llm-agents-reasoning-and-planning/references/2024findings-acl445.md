---
title: "Balancing Speciality and Versatility: a Coarse to Fine Framework for Supervised Fine-tuning Large Language Model"
source: "https://aclanthology.org/2024.findings-acl.445/"
categories: ['llm-training-alignment-and-evaluation', 'llm-agents-reasoning-and-planning']
tags: ['supervised-fine-tuning', 'LLM-alignment', 'coarse-to-fine']
venue: "ACL 2024"
tldr: "A coarse-to-fine framework for supervised fine-tuning balances LLM versatility and domain speciality without catastrophic forgetting."
---

# Balancing Speciality and Versatility: a Coarse to Fine Framework for Supervised Fine-tuning Large Language Model

**Source**: [https://aclanthology.org/2024.findings-acl.445/](https://aclanthology.org/2024.findings-acl.445/)

**TLDR**: A coarse-to-fine framework for supervised fine-tuning balances LLM versatility and domain speciality without catastrophic forgetting.

## Abstract

AbstractAligned Large Language Models (LLMs) showcase remarkable versatility, capable of handling diverse real-world tasks. Meanwhile, aligned LLMs are also expected to exhibit speciality, excelling in specific applications. However, fine-tuning with extra data, a common practice to gain speciality, often leads to catastrophic forgetting (CF) of previously acquired versatility, hindering the model’s performance across diverse tasks. In response to this challenge, we propose CoFiTune, a coarse to fine framework in an attempt to strike the balance between speciality and versatility. At the coarse-grained level, an empirical tree-search algorithm is utilized to pinpoint and update specific modules that are crucial for speciality, while keeping other parameters frozen; at the fine-grained level, a soft-masking mechanism regulates the update to the LLMs, mitigating the CF issue without harming speciality. In an overall evaluation of both speciality and versatility, CoFiTune consistently outperforms baseline methods across diverse tasks and model scales. Compared to the full-parameter SFT, CoFiTune leads to about 14% versatility improvement and marginal speciality loss on a 13B model. Lastly, based on further analysis, we provide a speculative insight into the information forwarding process in LLMs, which helps explain the effectiveness of the proposed method. The code is available at https://github.com/rattlesnakey/CoFiTune.