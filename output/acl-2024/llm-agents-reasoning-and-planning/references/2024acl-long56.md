---
title: "Reflect-RL: Two-Player Online RL Fine-Tuning for LMs"
source: "https://aclanthology.org/2024.acl-long.56/"
categories: ['llm-training-alignment-and-evaluation', 'llm-agents-reasoning-and-planning']
tags: ['reinforcement-learning', 'two-player', 'LLM-fine-tuning']
venue: "ACL 2024"
tldr: "Proposes Reflect-RL, a two-player online RL fine-tuning framework that improves LLMs on multi-round interactive tasks beyond supervised fine-tuning."
---

# Reflect-RL: Two-Player Online RL Fine-Tuning for LMs

**Source**: [https://aclanthology.org/2024.acl-long.56/](https://aclanthology.org/2024.acl-long.56/)

**TLDR**: Proposes Reflect-RL, a two-player online RL fine-tuning framework that improves LLMs on multi-round interactive tasks beyond supervised fine-tuning.

## Abstract

AbstractAs language models (LMs) demonstrate their capabilities in various fields, their application to tasks requiring multi-round interactions has become increasingly popular. These tasks usually have complex dynamics, so supervised fine-tuning (SFT) on a limited offline dataset does not yield good performance. However, only a few works attempted to directly train the LMs within interactive decision-making environments. We aim to create an effective approach to fine-tune LMs with online reinforcement learning (RL) in these environments. We propose Reflect-RL, a two-player system to fine-tune an LM using SFT and online RL, where a frozen reflection model (player) assists the policy model (player). To generate data for the warm-up SFT stage, we use negative example generation to enhance the error-correction ability of the reflection model. Furthermore, we designed single-prompt action enumeration and applied curriculum learning to allow the policy model to learn more efficiently. Empirically, we verify that Reflect-RL outperforms SFT and online RL without reflection. Testing results indicate GPT-2 XL 1.56B fine-tuned with Reflect-RL outperforms larger open-source LMs, such as Mistral 7B. The benchmarks, dataset, and code involved in this work are publicly available: https://github.com/zhourunlong/Reflect-RL.