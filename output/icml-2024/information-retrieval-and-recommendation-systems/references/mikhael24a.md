---
title: "CLIPZyme: Reaction-Conditioned Virtual Screening of Enzymes"
source: "https://proceedings.mlr.press/v235/mikhael24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mikhael24a/mikhael24a.pdf"
categories: ['generative-models-for-molecular-protein-design', 'information-retrieval-and-recommendation-systems']
tags: ['enzyme-screening', 'contrastive-learning', 'reaction-conditioned']
venue: "ICML 2024"
tldr: "Introduces CLIPZyme, a reaction-conditioned virtual screening model for efficiently identifying enzyme catalysts from large protein sequence databases."
---

# CLIPZyme: Reaction-Conditioned Virtual Screening of Enzymes

**Source**: [https://proceedings.mlr.press/v235/mikhael24a.html](https://proceedings.mlr.press/v235/mikhael24a.html)

**TLDR**: Introduces CLIPZyme, a reaction-conditioned virtual screening model for efficiently identifying enzyme catalysts from large protein sequence databases.

## Abstract

Computational screening of naturally occurring proteins has the potential to identify efficient catalysts among the hundreds of millions of sequences that remain uncharacterized. Current experimental methods remain time, cost and labor intensive, limiting the number of enzymes they can reasonably screen. In this work, we propose a computational framework for in-silico enzyme screening. Through a contrastive objective, we train CLIPZyme to encode and align representations of enzyme structures and reaction pairs. With no standard computational baseline, we compare CLIPZyme to existing EC (enzyme commission) predictors applied to virtual enzyme screening and show improved performance in scenarios where limited information on the reaction is available (BEDROC$_{85}$ of 44.69%). Additionally, we evaluate combining EC predictors with CLIPZyme and show its generalization capacity on both unseen reactions and protein clusters.