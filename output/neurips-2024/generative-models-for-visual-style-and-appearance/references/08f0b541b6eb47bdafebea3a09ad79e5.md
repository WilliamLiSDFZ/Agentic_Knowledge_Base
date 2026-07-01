---
title: "HairDiffusion: Vivid Multi-Colored Hair Editing via Latent Diffusion"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/08f0b541b6eb47bdafebea3a09ad79e5-Abstract-Conference.html"
categories: ['generative-models-for-visual-style-and-appearance', 'diffusion-based-generative-modeling-and-inference']
tags: ['hair-editing', 'latent-diffusion', 'text-guided-image-synthesis']
venue: "NeurIPS 2024"
tldr: "HairDiffusion uses latent diffusion models to enable vivid multi-colored hair editing via text or reference images while preserving identity."
---

# HairDiffusion: Vivid Multi-Colored Hair Editing via Latent Diffusion

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/08f0b541b6eb47bdafebea3a09ad79e5-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/08f0b541b6eb47bdafebea3a09ad79e5-Abstract-Conference.html)

**TLDR**: HairDiffusion uses latent diffusion models to enable vivid multi-colored hair editing via text or reference images while preserving identity.

## Abstract

Hair editing is a critical image synthesis task that aims to edit hair color and hairstyle using text descriptions or reference images, while preserving irrelevant attributes (e.g., identity, background, cloth). Many existing methods are based on StyleGAN to address this task. However, due to the limited spatial distribution of StyleGAN, it struggles with multiple hair color editing and facial preservation. Considering the advancements in diffusion models, we utilize Latent Diffusion Models (LDMs) for hairstyle editing. Our approach introduces Multi-stage Hairstyle Blend (MHB), effectively separating control of hair color and hairstyle in diffusion latent space. Additionally, we train a warping module to align the hair color with the target region. To further enhance multi-color hairstyle editing, we fine-tuned a CLIP model using a multi-color hairstyle dataset. Our method not only tackles the complexity of multi-color hairstyles but also addresses the challenge of preserving original colors during diffusion editing. Extensive experiments showcase the superiority of our method in editing multi-color hairstyles while preserving facial attributes given textual descriptions and reference images.