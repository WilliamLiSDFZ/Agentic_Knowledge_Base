---
title: "diff History for Neural Language Agents"
source: "https://proceedings.mlr.press/v235/piterbarg24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/piterbarg24a/piterbarg24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'sequence-models-for-memory-and-state']
tags: ['language-agents', 'embodied-control', 'observation-compression']
venue: "ICML 2024"
tldr: "Uses diff-based history compression to reduce verbose textual prompts for LM-based embodied agents."
---

# diff History for Neural Language Agents

**Source**: [https://proceedings.mlr.press/v235/piterbarg24a.html](https://proceedings.mlr.press/v235/piterbarg24a.html)

**TLDR**: Uses diff-based history compression to reduce verbose textual prompts for LM-based embodied agents.

## Abstract

Neural Language Models (LMs) offer an exciting solution for general-purpose embodied control. However, a key technical issue arises when using an LM-based controller: environment observations must be converted to text, which coupled with history, results in long and verbose textual prompts. As a result, prior work in LM agents is limited to restricted domains with small observation size as well as minimal needs for interaction history or instruction finetuning. In this paper, we introduce diff history, a simple and highly effective solution to these issues. By applying the Unix diff command on consecutive text observations in the interaction histories used to prompt LM policies, we can both abstract away redundant information and focus the content of textual inputs on the salient changes in the environment. On NetHack, an unsolved video game that requires long-horizon reasoning for decision-making, LMs tuned with diff history match state-of-the-art performance for neural agents while needing 1800X fewer training examples compared to prior work. Even on the simpler BabyAI-Text environment with concise text observations, we find that although diff history increases the length of prompts, the representation it provides offers a 25% improvement in the efficiency of low-sample instruction finetuning. Further, we show that diff history scales favorably across different finetuning dataset sizes. We open-source our code and data to https://diffhistory.github.io.