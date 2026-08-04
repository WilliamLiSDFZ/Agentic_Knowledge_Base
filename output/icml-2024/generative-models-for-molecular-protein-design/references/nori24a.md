---
title: "RNAFlow: RNA Structure & Sequence Design via Inverse Folding-Based Flow Matching"
source: "https://proceedings.mlr.press/v235/nori24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nori24a/nori24a.pdf"
categories: ['generative-models-for-molecular-protein-design', 'generative-models-and-variational-inference']
tags: ['RNA-design', 'flow-matching', 'inverse-folding']
venue: "ICML 2024"
tldr: "Presents RNAFlow, a flow matching model for joint RNA structure and sequence design via inverse folding to address RNA conformational flexibility."
---

# RNAFlow: RNA Structure & Sequence Design via Inverse Folding-Based Flow Matching

**Source**: [https://proceedings.mlr.press/v235/nori24a.html](https://proceedings.mlr.press/v235/nori24a.html)

**TLDR**: Presents RNAFlow, a flow matching model for joint RNA structure and sequence design via inverse folding to address RNA conformational flexibility.

## Abstract

The growing significance of RNA engineering in diverse biological applications has spurred interest in developing AI methods for structure-based RNA design. While diffusion models have excelled in protein design, adapting them for RNA presents new challenges due to RNA’s conformational flexibility and the computational cost of fine-tuning large structure prediction models. To this end, we propose RNAFlow, a flow matching model for protein-conditioned RNA sequence-structure design. Its denoising network integrates an RNA inverse folding model and a pre-trained RosettaFold2NA network for generation of RNA sequences and structures. The integration of inverse folding in the structure denoising process allows us to simplify training by fixing the structure prediction network. We further enhance the inverse folding model by conditioning it on inferred conformational ensembles to model dynamic RNA conformations. Evaluation on protein-conditioned RNA structure and sequence generation tasks demonstrates RNAFlow’s advantage over existing RNA design methods.