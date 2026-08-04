---
title: "Sparse is Enough in Fine-tuning Pre-trained Large Language Models"
source: "https://proceedings.mlr.press/v235/song24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/song24e/song24e.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'knowledge-distillation-methods-and-applications']
tags: ['parameter-efficient-fine-tuning', 'sparse-updates', 'LLMs', 'LoRA']
venue: "ICML 2024"
tldr: "A sparse fine-tuning method is proposed that achieves competitive performance with dense PEFT methods while significantly reducing the number of updated parameters."
---

# Sparse is Enough in Fine-tuning Pre-trained Large Language Models

**Source**: [https://proceedings.mlr.press/v235/song24e.html](https://proceedings.mlr.press/v235/song24e.html)

**TLDR**: A sparse fine-tuning method is proposed that achieves competitive performance with dense PEFT methods while significantly reducing the number of updated parameters.

## Abstract

With the prevalence of pre-training-fine-tuning paradigm, how to efficiently adapt the pre-trained model to the downstream tasks has been an intriguing issue. $\textbf{P}$arameter-$\textbf{E}$fficient $\textbf{F}$ine-$\textbf{T}$uning(PEFT) methods have been proposed for low-cost adaptation. Although PEFT has demonstrated effectiveness and been widely applied, the underlying principles are still unclear. In this paper, we adopt the PAC-Bayesian generalization error bound, viewing pre-training as a shift of prior distribution which leads to a tighter bound for generalization error. We validate this shift from the perspectives of oscillations in the loss landscape and the quasi-sparsity in gradient distribution. Based on this, we propose a gradient-based sparse fine-tuning algorithm, named $\textbf{S}$parse $\textbf{I}$ncrement $\textbf{F}$ine-$\textbf{T}$uning(SIFT), and validate its effectiveness on a range of tasks including the GLUE Benchmark and Instruction-tuning. The code is accessible at https://github.com/song-wx/SIFT/.