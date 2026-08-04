---
title: "Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast"
source: "https://proceedings.mlr.press/v235/gu24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gu24e/gu24e.pdf"
categories: ['adversarial-robustness-and-model-security', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['jailbreak', 'multimodal-agents', 'adversarial-images', 'exponential-spreading', 'multi-agent-systems']
venue: "ICML 2024"
tldr: "A single adversarial image can exponentially propagate jailbreaks across a million networked multimodal LLM agents."
---

# Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast

**Source**: [https://proceedings.mlr.press/v235/gu24e.html](https://proceedings.mlr.press/v235/gu24e.html)

**TLDR**: A single adversarial image can exponentially propagate jailbreaks across a million networked multimodal LLM agents.

## Abstract

A multimodal large language model (MLLM) agent can receive instructions, capture images, retrieve histories from memory, and decide which tools to use. Nonetheless, red-teaming efforts have revealed that adversarial images/prompts can jailbreak an MLLM and cause unaligned behaviors. In this work, we report an even more severe safety issue in multi-agent environments, referred to as infectious jailbreak. It entails the adversary simply jailbreaking a single agent, and without any further intervention from the adversary, (almost) all agents will become infected exponentially fast and exhibit harmful behaviors. To validate the feasibility of infectious jailbreak, we simulate multi-agent environments containing up to one million LLaVA-1.5 agents, and employ randomized pair-wise chat as a proof-of-concept instantiation for multi-agent interaction. Our results show that feeding an (infectious) adversarial image into the memory of any randomly chosen agent is sufficient to achieve infectious jailbreak. Finally, we derive a simple principle for determining whether a defense mechanism can provably restrain the spread of infectious jailbreak, but how to design a practical defense that meets this principle remains an open question to investigate.