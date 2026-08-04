---
title: "MLIP: Efficient Multi-Perspective Language-Image Pretraining with Exhaustive Data Utilization"
source: "https://proceedings.mlr.press/v235/zhang24cb.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24cb/zhang24cb.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'knowledge-distillation-methods-and-applications']
tags: ['contrastive-learning', 'CLIP', 'multimodal-pretraining']
venue: "ICML 2024"
tldr: "Introduces MLIP, an efficient multi-perspective language-image pretraining framework that improves data utilization over standard CLIP."
---

# MLIP: Efficient Multi-Perspective Language-Image Pretraining with Exhaustive Data Utilization

**Source**: [https://proceedings.mlr.press/v235/zhang24cb.html](https://proceedings.mlr.press/v235/zhang24cb.html)

**TLDR**: Introduces MLIP, an efficient multi-perspective language-image pretraining framework that improves data utilization over standard CLIP.

## Abstract

Contrastive Language-Image Pretraining (CLIP) has achieved remarkable success, leading to rapid advancements in multimodal studies. However, CLIP faces a notable challenge in terms of inefficient data utilization. It relies on a single contrastive supervision for each image-text pair during representation learning, disregarding a substantial amount of valuable information that could offer richer supervision. Additionally, the retention of non-informative tokens leads to increased computational demands and time costs, particularly in CLIP’s ViT image encoder. To address these issues, we propose Multi-Perspective Language-Image Pretraining (MLIP). In MLIP, we leverage the frequency transform’s sensitivity to both high and low-frequency variations, which complements the spatial domain’s sensitivity limited to low-frequency variations only. By incorporating frequency transforms and token-level alignment, we expand CILP’s single supervision into multi-domain and multi-level supervision, enabling a more thorough exploration of informative image features. Additionally, we introduce a token merging method guided by comprehensive semantics from the frequency and spatial domains. This allows us to merge tokens to multi-granularity tokens with a controllable compression rate to accelerate CLIP. Extensive experiments validate the effectiveness of our design.