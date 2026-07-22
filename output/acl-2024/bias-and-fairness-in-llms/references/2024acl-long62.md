---
title: "InstructProtein: Aligning Human and Protein Language via Knowledge Instruction"
source: "https://aclanthology.org/2024.acl-long.62/"
pdf_url: ""
categories: ['llms-for-biomedical-and-clinical-nlp', 'bias-and-fairness-in-llms']
tags: ['protein-language', 'LLM-alignment', 'biological-sequences', 'instruction-tuning', 'bidirectional-generation']
venue: "ACL 2024"
tldr: "InstructProtein aligns human and protein language by enabling LLMs to bidirectionally generate and comprehend protein sequences using knowledge instructions."
---

# InstructProtein: Aligning Human and Protein Language via Knowledge Instruction

**Source**: [https://aclanthology.org/2024.acl-long.62/](https://aclanthology.org/2024.acl-long.62/)

**TLDR**: InstructProtein aligns human and protein language by enabling LLMs to bidirectionally generate and comprehend protein sequences using knowledge instructions.

## Abstract

AbstractLarge Language Models (LLMs) have revolutionized the field of natural language processing, but they fall short in comprehending biological sequences such as proteins. To address this challenge, we propose InstructProtein, an innovative LLM that possesses bidirectional generation capabilities in both human and protein languages: (i) taking a protein sequence as input to predict its textual function description and (ii) using natural language to prompt protein sequence generation. To achieve this, we first pre-train an LLM on both protein and natural language corpora, enabling it to comprehend individual languages. Then supervised instruction tuning is employed to facilitate the alignment of these two distinct languages. Herein, we introduce a knowledge graph-based instruction generation framework to construct a high-quality instruction dataset, addressing the annotation imbalance and the absence of instructional signals in the existing protein-text corpus. In particular, the instructions inherit the structural relations between proteins and function annotations in knowledge graphs, which empowers our model to engage in the causal modeling of protein functions, akin to the chain-of-thought processes in natural languages. Extensive experiments on bidirectional protein-text generation tasks show that InstructProtein outperforms state-of-the-art LLMs by a large margin.