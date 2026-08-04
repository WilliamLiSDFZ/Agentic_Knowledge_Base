---
title: "Antibody Design Using a Score-based Diffusion Model Guided by Evolutionary, Physical and Geometric Constraints"
source: "https://proceedings.mlr.press/v235/zhu24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhu24j/zhu24j.pdf"
categories: ['geometry-aware-antibody-design-optimization', 'generative-models-for-molecular-protein-design']
tags: ['antibody-design', 'diffusion-model', 'evolutionary-constraints', 'geometric-constraints', 'protein-design']
venue: "ICML 2024"
tldr: "This paper proposes a score-based diffusion model for antibody design guided by evolutionary, physical, and geometric constraints."
---

# Antibody Design Using a Score-based Diffusion Model Guided by Evolutionary, Physical and Geometric Constraints

**Source**: [https://proceedings.mlr.press/v235/zhu24j.html](https://proceedings.mlr.press/v235/zhu24j.html)

**TLDR**: This paper proposes a score-based diffusion model for antibody design guided by evolutionary, physical, and geometric constraints.

## Abstract

Antibodies are central proteins in adaptive immune responses, responsible for protecting against viruses and other pathogens. Rational antibody design has proven effective in the diagnosis and treatment of various diseases like cancers and virus infections. While recent diffusion-based generative models show promise in designing antigen-specific antibodies, the primary challenge lies in the scarcity of labeled antibody-antigen complex data and binding affinity data. We present AbX, a new score-based diffusion generative model guided by evolutionary, physical, and geometric constraints for antibody design. These constraints serve to narrow the search space and provide priors for plausible antibody sequences and structures. Specifically, we leverage a pre-trained protein language model as priors for evolutionary plausible antibodies and introduce additional training objectives for geometric and physical constraints like van der Waals forces. Furthermore, as far as we know, AbX is the first score-based diffusion model with continuous timesteps for antibody design, jointly modeling the discrete sequence space and the $\mathrm{SE}(3)$ structure space. Evaluated on two independent testing sets, we show that AbX outperforms other published methods, achieving higher accuracy in sequence and structure generation and enhanced antibody-antigen binding affinity. Ablation studies highlight the clear contributions of the introduced constraints to antibody design.