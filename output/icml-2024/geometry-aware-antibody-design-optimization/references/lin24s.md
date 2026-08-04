---
title: "GeoAB: Towards Realistic Antibody Design and Reliable Affinity Maturation"
source: "https://proceedings.mlr.press/v235/lin24s.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24s/lin24s.pdf"
categories: ['geometry-aware-antibody-design-optimization', 'generative-models-for-molecular-protein-design']
tags: ['antibody-design', 'CDR-generation', 'affinity-maturation']
venue: "ICML 2024"
tldr: "GeoAB is a geometry-aware framework for realistic antibody structure generation and reliable affinity maturation in CDR design."
---

# GeoAB: Towards Realistic Antibody Design and Reliable Affinity Maturation

**Source**: [https://proceedings.mlr.press/v235/lin24s.html](https://proceedings.mlr.press/v235/lin24s.html)

**TLDR**: GeoAB is a geometry-aware framework for realistic antibody structure generation and reliable affinity maturation in CDR design.

## Abstract

Increasing works for antibody design are emerging to generate sequences and structures in Complementarity Determining Regions (CDRs), but problems still exist. We focus on two of them: (i) authenticity of the generated structure and (ii) rationality of the affinity maturation, and propose GeoAB as a solution. In specific, GeoAB-Designergenerates CDR structures with realistic internal geometries, composed of a generative geometry initializer (Geo-Initializer) and a position refiner (Geo-Refiner); GeoAB-Optimizer achieves affinity maturation by accurately predicting both the mutation effects and structures of mutant antibodies with the same network architecture as Geo-Refiner. Experiments show that GeoAB achieves state-of-the-art performance in CDR co-design and mutation effect predictions, and fulfills the discussed tasks effectively.