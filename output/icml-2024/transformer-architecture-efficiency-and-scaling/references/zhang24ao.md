---
title: "Wukong: Towards a Scaling Law for Large-Scale Recommendation"
source: "https://proceedings.mlr.press/v235/zhang24ao.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24ao/zhang24ao.pdf"
categories: ['information-retrieval-and-recommendation-systems', 'transformer-architecture-efficiency-and-scaling']
tags: ['recommendation-systems', 'scaling-laws', 'large-scale-models']
venue: "ICML 2024"
tldr: "Proposes Wukong, a recommendation model architecture that achieves scaling law behavior analogous to large language models."
---

# Wukong: Towards a Scaling Law for Large-Scale Recommendation

**Source**: [https://proceedings.mlr.press/v235/zhang24ao.html](https://proceedings.mlr.press/v235/zhang24ao.html)

**TLDR**: Proposes Wukong, a recommendation model architecture that achieves scaling law behavior analogous to large language models.

## Abstract

Scaling laws play an instrumental role in the sustainable improvement in model quality. Unfortunately, recommendation models to date do not exhibit such laws similar to those observed in the domain of large language models, due to the inefficiencies of their upscaling mechanisms. This limitation poses significant challenges in adapting these models to increasingly more complex real-world datasets. In this paper, we propose an effective network architecture based purely on stacked factorization machines, and a synergistic upscaling strategy, collectively dubbed Wukong, to establish a scaling law in the domain of recommendation. Wukong’s unique design makes it possible to capture diverse, any-order of interactions simply through taller and wider layers. We conducted extensive evaluations on six public datasets, and our results demonstrate that Wukong consistently outperforms state-of-the-art models quality-wise. Further, we assessed Wukong’s scalability on an internal, large-scale dataset. The results show that Wukong retains its superiority in quality over state-of-the-art models, while holding the scaling law across two orders of magnitude in model complexity, extending beyond 100 GFLOP/example, where prior arts fall short.