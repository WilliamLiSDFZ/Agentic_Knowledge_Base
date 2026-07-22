---
title: "XMoE: Sparse Models with Fine-grained and Adaptive Expert Selection"
source: "https://aclanthology.org/2024.findings-acl.694/"
pdf_url: ""
categories: ['transformer-architecture-analysis-and-design', 'collaborative-llm-deployment-and-inference-optimization']
tags: ['mixture-of-experts', 'sparse-models', 'adaptive-routing']
venue: "ACL 2024"
tldr: "Introduces XMoE, a fine-grained adaptive expert selection mechanism to improve efficiency of sparse MoE Transformer models."
---

# XMoE: Sparse Models with Fine-grained and Adaptive Expert Selection

**Source**: [https://aclanthology.org/2024.findings-acl.694/](https://aclanthology.org/2024.findings-acl.694/)

**TLDR**: Introduces XMoE, a fine-grained adaptive expert selection mechanism to improve efficiency of sparse MoE Transformer models.

## Abstract

AbstractSparse models, including sparse Mixture-of-Experts (MoE) models, have emerged as an effective approach for scaling Transformer models. However, they often suffer from computational inefficiency since a significant number of parameters are unnecessarily involved in computations by multiplying values by zero or low activation values. To address this issue, we present XMoE, a novel MoE designed to enhance both the efficacy and efficiency of sparse MoE models. XMoE leverages small experts and a threshold-based router to enable tokens to selectively engage only essential parameters. Our extensive experiments on language modeling and machine translation tasks demonstrate that enhances model performance and can decrease the computation load at MoE layers by over 50% without sacrificing performance. Furthermore, we present the versatility of by applying it to dense models, enabling sparse computation during inference. We provide a comprehensive analysis and make our code available at https://anonymous.4open.science/r/XMoE.