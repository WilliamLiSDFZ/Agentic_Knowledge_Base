---
title: "Phased Instruction Fine-Tuning for Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.341/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'continual-learning-for-nlp-tasks']
tags: ['instruction-tuning', 'fine-tuning', 'curriculum-learning']
venue: "ACL 2024"
tldr: "Phased instruction fine-tuning improves LLM alignment by progressively training on diverse instruction datasets in ordered stages."
---

# Phased Instruction Fine-Tuning for Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.341/](https://aclanthology.org/2024.findings-acl.341/)

**TLDR**: Phased instruction fine-tuning improves LLM alignment by progressively training on diverse instruction datasets in ordered stages.

## Abstract

AbstractInstruction Fine-Tuning, a method enhancing pre-trained language models’ capabilities from mere next-word prediction to complex instruction following, often employs a one-off training approach on diverse instruction dataset. However, this method may not effectively enhance models’ adherence to instructions due to the simultaneous handling of varying instruction complexities. To address this, we propose a novel phased instruction fine-tuning (Phased IFT) method, grounded in the hypothesis of progressive alignment, which posits that the transition of a pre-trained language model from simple next-word prediction to sophisticated instruction following is a gradual learning process. Specifically, we obtain the score of difficulty for each instruction via GPT-4, stratify the instruction data into subsets of increasing difficulty, and sequentially uptrain on these subsets using the standard supervised loss. Through extensive experiments on the pre-trained models Llama-2 7B/13B, and Mistral-7B using the 52K Alpaca instruction data, we demonstrate that Phased IFT significantly surpasses traditional one-off instruction fine-tuning (One-off IFT) method in win rate, empirically validating the progressive alignment hypothesis. Our findings suggest that Phased IFT offers a simple yet effective pathway for elevating the instruction-following capabilities of pre-trained language models.