---
title: "Dissecting Multimodality in VideoQA Transformer Models by Impairing Modality Fusion"
source: "https://proceedings.mlr.press/v235/rawal24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/rawal24a/rawal24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'learning-with-imperfect-data-and-bias']
tags: ['VideoQA', 'multimodal', 'transformers', 'modality-fusion', 'bias']
venue: "ICML 2024"
tldr: "This paper dissects multimodal fusion in VideoQA transformers by systematically impairing modality fusion to reveal whether models truly leverage multimodal structure or exploit dataset biases."
---

# Dissecting Multimodality in VideoQA Transformer Models by Impairing Modality Fusion

**Source**: [https://proceedings.mlr.press/v235/rawal24a.html](https://proceedings.mlr.press/v235/rawal24a.html)

**TLDR**: This paper dissects multimodal fusion in VideoQA transformers by systematically impairing modality fusion to reveal whether models truly leverage multimodal structure or exploit dataset biases.

## Abstract

While VideoQA Transformer models demonstrate competitive performance on standard benchmarks, the reasons behind their success are not fully understood. Do these models capture the rich multimodal structures and dynamics from video and text jointly? Or are they achieving high scores by exploiting biases and spurious features? Hence, to provide insights, we design QUAG (QUadrant AveraGe), a lightweight and non-parametric probe, to conduct dataset-model combined representation analysis by impairing modality fusion. We find that the models achieve high performance on many datasets without leveraging multimodal representations. To validate QUAG further, we design QUAG-attention, a less-expressive replacement of self-attention with restricted token interactions. Models with QUAG-attention achieve similar performance with significantly fewer multiplication operations without any finetuning. Our findings raise doubts about the current models’ abilities to learn highly-coupled multimodal representations. Hence, we design the CLAVI (Complements in LAnguage and VIdeo) dataset, a stress-test dataset curated by augmenting real-world videos to have high modality coupling. Consistent with the findings of QUAG, we find that most of the models achieve near-trivial performance on CLAVI. This reasserts the limitations of current models for learning highly-coupled multimodal representations, that is not evaluated by the current datasets.