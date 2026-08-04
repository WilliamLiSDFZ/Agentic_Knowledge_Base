---
title: "$\textttMoE-RBench$: Towards Building Reliable Language Models with Sparse Mixture-of-Experts"
source: "https://proceedings.mlr.press/v235/chen24bg.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24bg/chen24bg.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'large-language-model-alignment-and-capabilities']
tags: ['mixture-of-experts', 'LLM-reliability', 'model-robustness']
venue: "ICML 2024"
tldr: "MoE-RBench introduces a benchmark for evaluating the reliability of sparse Mixture-of-Experts language models including out-of-distribution and fine-tuning settings."
---

# $\textttMoE-RBench$: Towards Building Reliable Language Models with Sparse Mixture-of-Experts

**Source**: [https://proceedings.mlr.press/v235/chen24bg.html](https://proceedings.mlr.press/v235/chen24bg.html)

**TLDR**: MoE-RBench introduces a benchmark for evaluating the reliability of sparse Mixture-of-Experts language models including out-of-distribution and fine-tuning settings.

## Abstract

Mixture-of-Experts (MoE) has gained increasing popularity as a promising framework for scaling up large language models (LLMs). However, the reliability assessment of MoE lags behind its surging applications. Moreover, when transferred to new domains such as in fine-tuning MoE models sometimes underperform their dense counterparts. Motivated by the research gap and counter-intuitive phenomenon, we propose $\texttt{MoE-RBench}$, the first comprehensive assessment of SMoE reliability from three aspects: $\textit{(i)}$ safety and hallucination, $\textit{(ii)}$ resilience to adversarial attacks, and $\textit{(iii)}$ out-of-distribution robustness. Extensive models and datasets are tested to compare the MoE to dense networks from these reliability dimensions. Our empirical observations suggest that with appropriate hyperparameters, training recipes, and inference techniques, we can build the MoE model more reliably than the dense LLM. In particular, we find that the robustness of SMoE is sensitive to the basic training settings. We hope that this study can provide deeper insights into how to adapt the pre-trained MoE model to other tasks with higher-generation security, quality, and stability. Codes are available at https://github.com/UNITES-Lab/MoE-RBench.