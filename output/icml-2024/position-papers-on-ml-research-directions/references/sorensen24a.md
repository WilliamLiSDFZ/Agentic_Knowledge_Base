---
title: "Position: A Roadmap to Pluralistic Alignment"
source: "https://proceedings.mlr.press/v235/sorensen24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sorensen24a/sorensen24a.pdf"
categories: ['ai-safety-governance-alignment-positions', 'position-papers-on-ml-research-directions']
tags: ['pluralistic-alignment', 'AI-values', 'diversity', 'position-paper']
venue: "ICML 2024"
tldr: "This position paper presents a roadmap for aligning AI systems to pluralistic human values and diverse perspectives across populations."
---

# Position: A Roadmap to Pluralistic Alignment

**Source**: [https://proceedings.mlr.press/v235/sorensen24a.html](https://proceedings.mlr.press/v235/sorensen24a.html)

**TLDR**: This position paper presents a roadmap for aligning AI systems to pluralistic human values and diverse perspectives across populations.

## Abstract

With increased power and prevalence of AI systems, it is ever more critical that AI systems are designed to serve all, i.e., people with diverse values and perspectives. However, aligning models to serve pluralistic human values remains an open research question. In this piece, we propose a roadmap to pluralistic alignment, specifically using large language models as a test bed. We identify and formalize three possible ways to define and operationalize pluralism in AI systems: 1) Overton pluralistic models that present a spectrum of reasonable responses; 2) Steerably pluralistic models that can steer to reflect certain perspectives; and 3) Distributionally pluralistic models that are well-calibrated to a given population in distribution. We also formalize and discuss three possible classes of pluralistic benchmarks: 1) Multi-objective benchmarks, 2) Trade-off steerable benchmarks that incentivize models to steer to arbitrary trade-offs, and 3) Jury-pluralistic benchmarks that explicitly model diverse human ratings. We use this framework to argue that current alignment techniques may be fundamentally limited for pluralistic AI; indeed, we highlight empirical evidence, both from our own experiments and from other work, that standard alignment procedures might reduce distributional pluralism in models, motivating the need for further research on pluralistic alignment.