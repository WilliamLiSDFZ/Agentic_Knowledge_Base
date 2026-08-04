---
title: "Entropy-Reinforced Planning with Large Language Models for Drug Discovery"
source: "https://proceedings.mlr.press/v235/liu24be.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24be/liu24be.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'bayesian-optimization-and-surrogate-methods']
tags: ['drug-discovery', 'llm-planning', 'entropy-reinforced']
venue: "ICML 2024"
tldr: "An entropy-reinforced planning framework that augments LLM-based molecule generation with diversity-driven search to improve drug discovery beyond token-likelihood optimization."
---

# Entropy-Reinforced Planning with Large Language Models for Drug Discovery

**Source**: [https://proceedings.mlr.press/v235/liu24be.html](https://proceedings.mlr.press/v235/liu24be.html)

**TLDR**: An entropy-reinforced planning framework that augments LLM-based molecule generation with diversity-driven search to improve drug discovery beyond token-likelihood optimization.

## Abstract

The objective of drug discovery is to identify chemical compounds that possess specific pharmaceutical properties toward a binding target. Existing large language models (LLMS) can achieve high token matching scores in terms of likelihood for molecule generation. However, relying solely on LLM decoding often results in the generation of molecules that are either invalid due to a single misused token, or suboptimal due to unbalanced exploration and exploitation as a consequence of the LLM’s prior experience. Here we propose ERP, Entropy-Reinforced Planning for Transformer Decoding, which employs an entropy-reinforced planning algorithm to enhance the Transformer decoding process and strike a balance between exploitation and exploration. ERP aims to achieve improvements in multiple properties compared to direct sampling from the Transformer. We evaluated ERP on the SARS-CoV-2 virus (3CLPro) and human cancer cell target protein (RTCB) benchmarks and demonstrated that, in both benchmarks, ERP consistently outperforms the current state-of-the-art algorithm by 1-5 percent, and baselines by 5-10 percent, respectively. Moreover, such improvement is robust across Transformer models trained with different objectives. Finally, to further illustrate the capabilities of ERP, we tested our algorithm on three code generation benchmarks and outperformed the current state-of-the-art approach as well. Our code is publicly available at: https://github.com/xuefeng-cs/ERP.