---
title: "DISCRET: Synthesizing Faithful Explanations For Treatment Effect Estimation"
source: "https://proceedings.mlr.press/v235/wu24n.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24n/wu24n.pdf"
categories: ['causal-ml-for-clinical-decision-making', 'ai-explainability-uncertainty-human-decision-making']
tags: ['treatment-effect-estimation', 'faithful-explanations', 'individual-treatment-effect', 'causal-inference', 'healthcare']
venue: "ICML 2024"
tldr: "Proposes DISCRET, a method for synthesizing faithful explanations for individual treatment effect estimation models deployed in critical healthcare settings."
---

# DISCRET: Synthesizing Faithful Explanations For Treatment Effect Estimation

**Source**: [https://proceedings.mlr.press/v235/wu24n.html](https://proceedings.mlr.press/v235/wu24n.html)

**TLDR**: Proposes DISCRET, a method for synthesizing faithful explanations for individual treatment effect estimation models deployed in critical healthcare settings.

## Abstract

Designing faithful yet accurate AI models is challenging, particularly in the field of individual treatment effect estimation (ITE). ITE prediction models deployed in critical settings such as healthcare should ideally be (i) accurate, and (ii) provide faithful explanations. However, current solutions are inadequate: state-of-the-art black-box models do not supply explanations, post-hoc explainers for black-box models lack faithfulness guarantees, and self-interpretable models greatly compromise accuracy. To address these issues, we propose DISCRET, a self-interpretable ITE framework that synthesizes faithful, rule-based explanations for each sample. A key insight behind DISCRET is that explanations can serve dually as database queries to identify similar subgroups of samples. We provide a novel RL algorithm to efficiently synthesize these explanations from a large search space. We evaluate DISCRET on diverse tasks involving tabular, image, and text data. DISCRET outperforms the best self-interpretable models and has accuracy comparable to the best black-box models while providing faithful explanations. DISCRET is available at https://github.com/wuyinjun-1993/DISCRET-ICML2024.