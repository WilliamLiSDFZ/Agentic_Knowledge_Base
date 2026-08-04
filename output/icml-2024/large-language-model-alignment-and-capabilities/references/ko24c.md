---
title: "DistiLLM: Towards Streamlined Distillation for Large Language Models"
source: "https://proceedings.mlr.press/v235/ko24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ko24c/ko24c.pdf"
categories: ['knowledge-distillation-methods-and-applications', 'large-language-model-alignment-and-capabilities']
tags: ['knowledge-distillation', 'large-language-models', 'autoregressive', 'sequence-models', 'compression']
venue: "ICML 2024"
tldr: "A streamlined knowledge distillation framework for LLMs that addresses distribution mismatch issues in autoregressive sequence model distillation."
---

# DistiLLM: Towards Streamlined Distillation for Large Language Models

**Source**: [https://proceedings.mlr.press/v235/ko24c.html](https://proceedings.mlr.press/v235/ko24c.html)

**TLDR**: A streamlined knowledge distillation framework for LLMs that addresses distribution mismatch issues in autoregressive sequence model distillation.

## Abstract

Knowledge distillation (KD) is widely used for compressing a teacher model to a smaller student model, reducing its inference cost and memory footprint while preserving model capabilities. However, current KD methods for auto-regressive sequence models (e.g., large language models) suffer from missing a standardized objective function. Moreover, the recent use of student-generated outputs to address training-inference mismatches has significantly escalated computational costs. To tackle these issues, we introduce DistiLLM, a more effective and efficient KD framework for auto-regressive language models. DistiLLM comprises two components: (1) a novel skew Kullback-Leibler divergence loss, where we unveil and leverage its theoretical properties, and (2) an adaptive off-policy approach designed to enhance the efficiency in utilizing student-generated outputs. Extensive experiments, including instruction-following tasks, demonstrate the effectiveness of DistiLLM in building high-performing student models while achieving up to 4.3$\times$ speedup compared to recent KD methods.