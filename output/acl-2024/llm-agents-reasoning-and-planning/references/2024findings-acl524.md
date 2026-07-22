---
title: "Rationales for Answers to Simple Math Word Problems Confuse Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.524/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-agents-reasoning-and-planning']
tags: ['math-reasoning', 'chain-of-thought', 'rationale-confusion']
venue: "ACL 2024"
tldr: "Finds that providing rationales for simple math word problems can confuse LLMs rather than help them."
---

# Rationales for Answers to Simple Math Word Problems Confuse Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.524/](https://aclanthology.org/2024.findings-acl.524/)

**TLDR**: Finds that providing rationales for simple math word problems can confuse LLMs rather than help them.

## Abstract

AbstractRecently, large language models (LLMs) have demonstrated breakthrough mathematical problem-solving capabilities in grade school math word problems (MWP). For example, on the MWP benchmark GSM8K, the accuracy of GPT-3.5-Turbo and MetaMath-70B reaches 80.80% and 82.30%, respectively. One question arises, does it mean that LLMs have truly mastered related mathematical problem-solving abilities? In this paper, by presenting two types of benchmarks, where MCGSM8K aims at selecting one correct solution from four solutions, while GSM8K-Judgement judges whether a solution to a given question is true or false, we demonstrate that the ability of most LLMs to evaluate the mathematical reasoning process of MWP is far from sufficient. To compensate for this issue, we propose hybrid supervised fine-tuning data from the training data of GSM8K, MCGSM8K, and GSM8K-Judgement, which significantly improves performance on the proposed reasoning process evaluation benchmarks. For example, fine-tuning improves the performance of LLaMA-2-13B from 33.51% to 70.89% on MCGSM8K. In conclusion, we experimentally demonstrate that most LLMs have limited ability to evaluate the mathematical reasoning process of MWP, which can be enhanced through fine-tuning.