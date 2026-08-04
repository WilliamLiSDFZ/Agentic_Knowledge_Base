---
title: "Full-Atom Peptide Design based on Multi-modal Flow Matching"
source: "https://proceedings.mlr.press/v235/li24o.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24o/li24o.pdf"
categories: ['generative-models-for-molecular-protein-design', 'generative-models-and-variational-inference']
tags: ['peptide-design', 'flow-matching', 'multi-modal', 'full-atom', 'drug-discovery']
venue: "ICML 2024"
tldr: "Presents PepFlow, a multi-modal flow matching generative model for full-atom peptide design targeting drug discovery applications."
---

# Full-Atom Peptide Design based on Multi-modal Flow Matching

**Source**: [https://proceedings.mlr.press/v235/li24o.html](https://proceedings.mlr.press/v235/li24o.html)

**TLDR**: Presents PepFlow, a multi-modal flow matching generative model for full-atom peptide design targeting drug discovery applications.

## Abstract

Peptides, short chains of amino acid residues, play a vital role in numerous biological processes by interacting with other target molecules, offering substantial potential in drug discovery. In this work, we present PepFlow, the first multi-modal deep generative model grounded in the flow-matching framework for the design of full-atom peptides that target specific protein receptors. Drawing inspiration from the crucial roles of residue backbone orientations and side-chain dynamics in protein-peptide interactions, we characterize the peptide structure using rigid backbone frames within the $\mathrm{SE}(3)$ manifold and side-chain angles on high-dimensional tori. Furthermore, we represent discrete residue types in the peptide sequence as categorical distributions on the probability simplex. By learning the joint distributions of each modality using derived flows and vector fields on corresponding manifolds, our method excels in the fine-grained design of full-atom peptides. Harnessing the multi-modal paradigm, our approach adeptly tackles various tasks such as fix-backbone sequence design and side-chain packing through partial sampling. Through meticulously crafted experiments, we demonstrate that PepFlow exhibits superior performance in comprehensive benchmarks, highlighting its significant potential in computational peptide design and analysis.