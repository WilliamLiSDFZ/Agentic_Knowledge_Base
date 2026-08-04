---
title: "BetterV: Controlled Verilog Generation with Discriminative Guidance"
source: "https://proceedings.mlr.press/v235/pei24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pei24e/pei24e.pdf"
categories: ['llm-driven-automated-system-optimization', 'neural-symbolic-combinatorial-optimization-learning']
tags: ['Verilog-generation', 'hardware-design', 'LLM', 'discriminative-guidance', 'circuit-design']
venue: "ICML 2024"
tldr: "Proposes BetterV, a controlled Verilog generation framework using discriminative guidance to improve automated hardware design quality."
---

# BetterV: Controlled Verilog Generation with Discriminative Guidance

**Source**: [https://proceedings.mlr.press/v235/pei24e.html](https://proceedings.mlr.press/v235/pei24e.html)

**TLDR**: Proposes BetterV, a controlled Verilog generation framework using discriminative guidance to improve automated hardware design quality.

## Abstract

Due to the growing complexity of modern Integrated Circuits (ICs), there is a need for automated circuit design methods. Recent years have seen increasing research in hardware design language generation to facilitate the design process. In this work, we propose a Verilog generation framework, BetterV, which fine-tunes large language models (LLMs) on processed domain-specific datasets and incorporates generative discriminators for guidance on particular design demands. Verilog modules are collected, filtered, and processed from the internet to form a clean and abundant dataset. Instruct-tuning methods are specially designed to fine-tune the LLMs to understand knowledge about Verilog. Furthermore, data are augmented to enrich the training set and are also used to train a generative discriminator on particular downstream tasks, providing guidance for the LLMs to optimize Verilog implementation. BetterV has the ability to generate syntactically and functionally correct Verilog, outperforming GPT-4 on the VerilogEval benchmark. With the help of task-specific generative discriminators, BetterV achieves remarkable improvements on various electronic design automation (EDA) downstream tasks, including netlist node reduction for synthesis and verification runtime reduction with Boolean Satisfiability (SAT) solving.