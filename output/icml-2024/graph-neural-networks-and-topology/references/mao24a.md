---
title: "Position: Graph Foundation Models Are Already Here"
source: "https://proceedings.mlr.press/v235/mao24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mao24a/mao24a.pdf"
categories: ['position-papers-on-ml-research-directions', 'graph-neural-networks-and-topology']
tags: ['graph-foundation-models', 'position-paper', 'graph-neural-networks']
venue: "ICML 2024"
tldr: "A position paper arguing that graph foundation models have arrived and outlining the unique challenges and opportunities in developing them across diverse graph tasks."
---

# Position: Graph Foundation Models Are Already Here

**Source**: [https://proceedings.mlr.press/v235/mao24a.html](https://proceedings.mlr.press/v235/mao24a.html)

**TLDR**: A position paper arguing that graph foundation models have arrived and outlining the unique challenges and opportunities in developing them across diverse graph tasks.

## Abstract

Graph Foundation Models (GFMs) are emerging as a significant research topic in the graph domain, aiming to develop graph models trained on extensive and diverse data to enhance their applicability across various tasks and domains. Developing GFMs presents unique challenges over traditional Graph Neural Networks (GNNs), which are typically trained from scratch for specific tasks on particular datasets. The primary challenge in constructing GFMs lies in effectively leveraging vast and diverse graph data to achieve positive transfer. Drawing inspiration from existing foundation models in the CV and NLP domains, we propose a novel perspective for the GFM development by advocating for a "graph vocabulary”, in which the basic transferable units underlying graphs encode the invariance on graphs. We ground the graph vocabulary construction from essential aspects including network analysis, expressiveness, and stability. Such a vocabulary perspective can potentially advance the future GFM design in line with the neural scaling laws. All relevant resources with GFM design can be found here.