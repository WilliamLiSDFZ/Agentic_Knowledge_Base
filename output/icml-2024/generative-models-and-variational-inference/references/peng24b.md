---
title: "UPAM: Unified Prompt Attack in Text-to-Image Generation Models Against Both Textual Filters and Visual Checkers"
source: "https://proceedings.mlr.press/v235/peng24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/peng24b/peng24b.pdf"
categories: ['adversarial-robustness-and-model-security', 'generative-models-and-variational-inference']
tags: ['adversarial-attacks', 'text-to-image', 'prompt-attack', 'safety-filters', 'robustness']
venue: "ICML 2024"
tldr: "Proposes UPAM, a unified framework to attack text-to-image models by simultaneously bypassing both textual filters and visual safety checkers."
---

# UPAM: Unified Prompt Attack in Text-to-Image Generation Models Against Both Textual Filters and Visual Checkers

**Source**: [https://proceedings.mlr.press/v235/peng24b.html](https://proceedings.mlr.press/v235/peng24b.html)

**TLDR**: Proposes UPAM, a unified framework to attack text-to-image models by simultaneously bypassing both textual filters and visual safety checkers.

## Abstract

Text-to-Image (T2I) models have raised security concerns due to their potential to generate inappropriate or harmful images. In this paper, we propose UPAM, a novel framework that investigates the robustness of T2I models from the attack perspective. Unlike most existing attack methods that focus on deceiving textual defenses, UPAM aims to deceive both textual and visual defenses in T2I models. UPAM enables gradient-based optimization, offering greater effectiveness and efficiency than previous methods. Given that T2I models might not return results due to defense mechanisms, we introduce a Sphere-Probing Learning (SPL) scheme to support gradient optimization even when no results are returned. Additionally, we devise a Semantic-Enhancing Learning (SEL) scheme to finetune UPAM for generating target-aligned images. Our framework also ensures attack stealthiness. Extensive experiments demonstrate UPAM’s effectiveness and efficiency.