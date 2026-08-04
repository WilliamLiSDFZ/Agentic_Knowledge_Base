---
title: "AlphaFold Meets Flow Matching for Generating Protein Ensembles"
source: "https://proceedings.mlr.press/v235/jing24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jing24a/jing24a.pdf"
categories: ['generative-models-for-molecular-protein-design', 'generative-models-and-variational-inference']
tags: ['protein-conformational-ensembles', 'flow-matching', 'alphafold', 'generative-modeling']
venue: "ICML 2024"
tldr: "A flow matching generative model repurposes AlphaFold and ESMFold to learn and sample diverse protein conformational ensembles."
---

# AlphaFold Meets Flow Matching for Generating Protein Ensembles

**Source**: [https://proceedings.mlr.press/v235/jing24a.html](https://proceedings.mlr.press/v235/jing24a.html)

**TLDR**: A flow matching generative model repurposes AlphaFold and ESMFold to learn and sample diverse protein conformational ensembles.

## Abstract

The biological functions of proteins often depend on dynamic structural ensembles. In this work, we develop a flow-based generative modeling approach for learning and sampling the conformational landscapes of proteins. We repurpose highly accurate single-state predictors such as AlphaFold and ESMFold and fine-tune them under a custom flow matching framework to obtain sequence-conditioned generative models of protein structure called AlphaFlow and ESMFlow. When trained and evaluated on the PDB, our method provides a superior combination of precision and diversity compared to AlphaFold with MSA subsampling. When further trained on ensembles from all-atom MD, our method accurately captures conformational flexibility, positional distributions, and higher-order ensemble observables for unseen proteins. Moreover, our method can diversify a static PDB structure with faster wall-clock convergence to certain equilibrium properties than replicate MD trajectories, demonstrating its potential as a proxy for expensive physics-based simulations. Code is available at https://github.com/bjing2016/alphaflow.