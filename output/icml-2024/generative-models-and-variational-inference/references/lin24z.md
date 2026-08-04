---
title: "PPFLOW: Target-Aware Peptide Design with Torsional Flow Matching"
source: "https://proceedings.mlr.press/v235/lin24z.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24z/lin24z.pdf"
categories: ['generative-models-for-molecular-protein-design', 'generative-models-and-variational-inference']
tags: ['peptide-design', 'flow-matching', 'torsional-geometry']
venue: "ICML 2024"
tldr: "PPFlow is a target-aware peptide design method using conditional torsional flow matching for therapeutic drug discovery."
---

# PPFLOW: Target-Aware Peptide Design with Torsional Flow Matching

**Source**: [https://proceedings.mlr.press/v235/lin24z.html](https://proceedings.mlr.press/v235/lin24z.html)

**TLDR**: PPFlow is a target-aware peptide design method using conditional torsional flow matching for therapeutic drug discovery.

## Abstract

Therapeutic peptides have proven to have great pharmaceutical value and potential in recent decades. However, methods of AI-assisted peptide drug discovery are not fully explored. To fill the gap, we propose a target-aware peptide design method called PPFlow, based on conditional flow matching on torus manifolds, to model the internal geometries of torsion angles for the peptide structure design. Besides, we establish a protein-peptide binding dataset named PPBench2024 to fill the void of massive data for the task of structure-based peptide drug design and to allow the training of deep learning methods. Extensive experiments show that PPFlow reaches state-of-the-art performance in tasks of peptide drug generation and optimization in comparison with baseline models, and can be generalized to other tasks including docking and side-chain packing.