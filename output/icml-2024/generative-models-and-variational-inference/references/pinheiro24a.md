---
title: "Structure-based drug design by denoising voxel grids"
source: "https://proceedings.mlr.press/v235/pinheiro24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pinheiro24a/pinheiro24a.pdf"
categories: ['generative-models-for-molecular-protein-design', 'generative-models-and-variational-inference']
tags: ['drug-design', 'voxel-grids', 'score-based-generative-model']
venue: "ICML 2024"
tldr: "VoxBind is a score-based generative model for structure-based drug design that represents molecules as 3D atomic density grids."
---

# Structure-based drug design by denoising voxel grids

**Source**: [https://proceedings.mlr.press/v235/pinheiro24a.html](https://proceedings.mlr.press/v235/pinheiro24a.html)

**TLDR**: VoxBind is a score-based generative model for structure-based drug design that represents molecules as 3D atomic density grids.

## Abstract

We presents VoxBind, a new score-based generative model for 3D molecules conditioned on protein structures. Our approach represents molecules as 3D atomic density grids and leverages a 3D voxel-denoising network for learning and generation. We extend the neural empirical Bayes formalism (Saremi & Hyvärinen, 2019) to the conditional setting and generate structure-conditioned molecules with a two-step procedure: (i) sample noisy molecules from the Gaussian-smoothed conditional distribution with underdamped Langevin MCMC using the learned score function and (ii) estimate clean molecules from the noisy samples with single-step denoising. Compared to the current state of the art, our model is simpler to train, significantly faster to sample from, and achieves better results on extensive in silico benchmarks—the generated molecules are more diverse, exhibit fewer steric clashes, and bind with higher affinity to protein pockets.