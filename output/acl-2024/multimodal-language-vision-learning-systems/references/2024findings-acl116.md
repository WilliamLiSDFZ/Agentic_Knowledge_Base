---
title: "MolTC: Towards Molecular Relational Modeling In Language Models"
source: "https://aclanthology.org/2024.findings-acl.116/"
categories: ['llm-agents-for-scientific-data-tasks', 'multimodal-language-vision-learning-systems']
tags: ['molecular-relational-learning', 'drug-interaction', 'multimodal-llm']
venue: "ACL 2024"
tldr: "Presents MolTC, a framework for molecular relational modeling that integrates molecular pair interaction understanding into large language models."
---

# MolTC: Towards Molecular Relational Modeling In Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.116/](https://aclanthology.org/2024.findings-acl.116/)

**TLDR**: Presents MolTC, a framework for molecular relational modeling that integrates molecular pair interaction understanding into large language models.

## Abstract

AbstractMolecular Relational Learning (MRL), aiming to understand interactions between molecular pairs, plays a pivotal role in advancing biochemical research. Recently, the adoption of large language models (LLMs), known for their vast knowledge repositories and advanced logical inference capabilities, has emerged as a promising way for efficient and effective MRL. Despite their potential, these methods predominantly rely on textual data, thus not fully harnessing the wealth of structural information inherent in molecular graphs. Moreover, the absence of a unified framework exacerbates the issue of insufficient data exploitation, as it hinders the sharing of interaction mechanism learned across various datasets. To address these challenges, this work proposes a novel LLM-based multi-modal framework for molecular interaction modeling following Chain-of-Thought (CoT) theory, termed MolTC, which effectively integrate graphical information of two molecules in pair. To train this integrated framework efficiently, we introduce a *multi-hierarchical CoT theory* to refine its training paradigm, and conduct a comprehensive *Molecular Interactive Instructions* dataset for the development of biochemical LLMs involving MRL.Our experiments,conducted across various datasets involving over 4,000,000 molecular pairs, exhibit the superiority of our method over current GNN and LLM-based baselines. Code is available at https://github.com/MangoKiller/MolTC.