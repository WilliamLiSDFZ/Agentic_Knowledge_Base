---
title: "FVEL: Interactive Formal Verification Environment with Large Language Models via Theorem Proving"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/62c6d7893b13a13c659cb815852dd00d-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['neural-networks-for-formal-reasoning-and-verification']
tags: ['formal-verification', 'theorem-proving', 'LLM-agents']
venue: "NeurIPS 2024"
tldr: "FVEL introduces an interactive formal verification environment leveraging LLMs for theorem proving to enable flexible and extensive program verification."
---

# FVEL: Interactive Formal Verification Environment with Large Language Models via Theorem Proving

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/62c6d7893b13a13c659cb815852dd00d-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/62c6d7893b13a13c659cb815852dd00d-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: FVEL introduces an interactive formal verification environment leveraging LLMs for theorem proving to enable flexible and extensive program verification.

## Abstract

Formal verification (FV) has witnessed growing significance with current emerging program synthesis by the evolving large language models (LLMs). However, current formal verification mainly resorts to symbolic verifiers or hand-craft rules, resulting in limitations for extensive and flexible verification. On the other hand, formal languages for automated theorem proving, such as Isabelle, as another line of rigorous verification, are maintained with comprehensive rules and theorems. In this paper, we propose FVEL, an interactive Formal Verification Environment with LLMs. Specifically, FVEL transforms a given code to be verified into Isabelle, and then conducts verification via neural automated theorem proving with an LLM. The joined paradigm leverages the rigorous yet abundant formulated and organized rules in Isabelle and is also convenient for introducing and adjusting cutting-edge LLMs. To achieve this goal, we extract a large-scale FVELER. The FVELER dataset includes code dependencies and verification processes that are formulated in Isabelle, containing 758 theories, 29,304 lemmas, and 201,498 proof steps in total with in-depth dependencies. We benchmark FVELER in the FVEL environment by first fine-tuning LLMs with FVELER and then evaluating them on Code2Inv and SV-COMP. The results show that FVEL with FVELER fine-tuned Llama3-8B solves 17.39% (69→81) more problems, and Mistral-7B 12% (75→84) more problems in SV-COMP. And the proportion of proof errors is reduced. Project page: https://fveler.github.io/.