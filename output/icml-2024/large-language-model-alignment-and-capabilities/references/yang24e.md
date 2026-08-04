---
title: "A Dense Reward View on Aligning Text-to-Image Diffusion with Preference"
source: "https://proceedings.mlr.press/v235/yang24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24e/yang24e.pdf"
categories: ['generative-models-and-variational-inference', 'large-language-model-alignment-and-capabilities']
tags: ['text-to-image-diffusion', 'preference-alignment', 'dense-reward']
venue: "ICML 2024"
tldr: "Reformulates text-to-image diffusion alignment with preference as a dense reward optimization problem over the full reverse diffusion chain rather than a bandit assumption."
---

# A Dense Reward View on Aligning Text-to-Image Diffusion with Preference

**Source**: [https://proceedings.mlr.press/v235/yang24e.html](https://proceedings.mlr.press/v235/yang24e.html)

**TLDR**: Reformulates text-to-image diffusion alignment with preference as a dense reward optimization problem over the full reverse diffusion chain rather than a bandit assumption.

## Abstract

Aligning text-to-image diffusion model (T2I) with preference has been gaining increasing research attention. While prior works exist on directly optimizing T2I by preference data, these methods are developed under the bandit assumption of a latent reward on the entire diffusion reverse chain, while ignoring the sequential nature of the generation process. This may harm the efficacy and efficiency of preference alignment. In this paper, we take on a finer dense reward perspective and derive a tractable alignment objective that emphasizes the initial steps of the T2I reverse chain. In particular, we introduce temporal discounting into DPO-style explicit-reward-free objectives, to break the temporal symmetry therein and suit the T2I generation hierarchy. In experiments on single and multiple prompt generation, our method is competitive with strong relevant baselines, both quantitatively and qualitatively. Further investigations are conducted to illustrate the insight of our approach. Source code is available at https://github.com/Shentao-YANG/Dense_Reward_T2I .