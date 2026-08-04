---
title: "Self-Alignment of Large Language Models via Monopolylogue-based Social Scene Simulation"
source: "https://proceedings.mlr.press/v235/pang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pang24a/pang24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['LLM-alignment', 'social-simulation', 'self-alignment', 'human-values']
venue: "ICML 2024"
tldr: "Proposes Monopolylogue-based Social Scene Simulation to enable self-alignment of LLMs with human values by simulating multi-party social perspectives."
---

# Self-Alignment of Large Language Models via Monopolylogue-based Social Scene Simulation

**Source**: [https://proceedings.mlr.press/v235/pang24a.html](https://proceedings.mlr.press/v235/pang24a.html)

**TLDR**: Proposes Monopolylogue-based Social Scene Simulation to enable self-alignment of LLMs with human values by simulating multi-party social perspectives.

## Abstract

Aligning large language models (LLMs) with human values is imperative to mitigate potential adverse effects resulting from their misuse. Drawing from the sociological insight that acknowledging all parties’ concerns is a key factor in shaping human values, this paper proposes a novel direction to align LLMs by themselves: social scene simulation. To achieve this, we present MATRIX, a novel social scene simulator that emulates realistic scenes around a user’s input query, enabling the LLM to take social consequences into account before responding. MATRIX serves as a virtual rehearsal space, akin to a Monopolylogue, where the LLM performs diverse roles related to the query and practice by itself. To inject this alignment, we fine-tune the LLM with MATRIX-simulated data, ensuring adherence to human values without compromising inference speed. We theoretically show that the LLM with MATRIX outperforms existing methods under mild assumptions. Finally, extensive experiments validate that our method outperforms over 10 baselines across 4 benchmarks. As evidenced by 875 user ratings, our tuned 13B-size LLM exceeds GPT-4 in aligning with human values. See our project page at https://shuotang123.github.io/MATRIX.