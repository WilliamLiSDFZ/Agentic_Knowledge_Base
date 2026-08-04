---
title: "An Efficient Self-Learning Framework For Interactive Spoken Dialog Systems"
source: "https://proceedings.mlr.press/v235/tulsiani24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tulsiani24a/tulsiani24a.pdf"
categories: ['continual-learning-memory-plasticity', 'test-time-adaptation-methods-and-evaluation']
tags: ['spoken-dialog', 'ASR', 'self-learning']
venue: "ICML 2024"
tldr: "Presents an efficient self-learning framework for interactive spoken dialog systems that adapts using conversational context across turns."
---

# An Efficient Self-Learning Framework For Interactive Spoken Dialog Systems

**Source**: [https://proceedings.mlr.press/v235/tulsiani24a.html](https://proceedings.mlr.press/v235/tulsiani24a.html)

**TLDR**: Presents an efficient self-learning framework for interactive spoken dialog systems that adapts using conversational context across turns.

## Abstract

Dialog systems, such as voice assistants, are expected to engage with users in complex, evolving conversations. Unfortunately, traditional automatic speech recognition (ASR) systems deployed in such applications are usually trained to recognize each turn independently and lack the ability to adapt to the conversational context or incorporate user feedback. In this work, we introduce a general framework for ASR in dialog systems that can go beyond learning from single-turn utterances and learn over time how to adapt to both explicit supervision and implicit user feedback present in multi-turn conversations. We accomplish that by leveraging advances in student-teacher learning and context-aware dialog processing, and designing contrastive self-supervision approaches with Ohm, a new online hard-negative mining approach. We show that leveraging our new framework compared to traditional training leads to relative WER reductions of close to 10% in real-world dialog systems, and up to 26% on public synthetic data.