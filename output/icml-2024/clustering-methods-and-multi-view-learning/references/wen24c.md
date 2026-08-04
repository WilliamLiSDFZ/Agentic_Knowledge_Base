---
title: "Diffusion-based Missing-view Generation With the Application on Incomplete Multi-view Clustering"
source: "https://proceedings.mlr.press/v235/wen24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wen24c/wen24c.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'generative-models-and-variational-inference']
tags: ['diffusion-models', 'missing-view-generation', 'multi-view-clustering', 'incomplete-data']
venue: "ICML 2024"
tldr: "A diffusion-based generative approach reconstructs missing views to enable effective incomplete multi-view clustering."
---

# Diffusion-based Missing-view Generation With the Application on Incomplete Multi-view Clustering

**Source**: [https://proceedings.mlr.press/v235/wen24c.html](https://proceedings.mlr.press/v235/wen24c.html)

**TLDR**: A diffusion-based generative approach reconstructs missing views to enable effective incomplete multi-view clustering.

## Abstract

As a branch of clustering, multi-view clustering has received much attention in recent years. In practical applications, a common phenomenon is that partial views of some samples may be missing in the collected multi-view data, which poses a severe challenge to design the multi-view learning model and explore complementary and consistent information. Currently, most of the incomplete multi-view clustering methods only focus on exploring the information of available views while few works study the missing view recovery for incomplete multi-view learning. To this end, we propose an innovative diffusion-based missing view generation (DMVG) network. Moreover, for the scenarios with high missing rates, we further propose an incomplete multi-view data augmentation strategy to enhance the recovery quality for the missing views. Extensive experimental results show that the proposed DMVG can not only accurately predict missing views, but also further enhance the subsequent clustering performance in comparison with several state-of-the-art incomplete multi-view clustering methods.