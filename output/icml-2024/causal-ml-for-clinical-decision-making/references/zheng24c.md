---
title: "Exploiting Negative Samples: A Catalyst for Cohort Discovery in Healthcare Analytics"
source: "https://proceedings.mlr.press/v235/zheng24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zheng24c/zheng24c.pdf"
categories: ['causal-ml-for-clinical-decision-making']
tags: ['healthcare-analytics', 'negative-samples', 'cohort-discovery', 'clinical-data']
venue: "ICML 2024"
tldr: "This paper proposes leveraging negative samples as a catalyst to improve cohort discovery in healthcare binary diagnosis and prognosis tasks."
---

# Exploiting Negative Samples: A Catalyst for Cohort Discovery in Healthcare Analytics

**Source**: [https://proceedings.mlr.press/v235/zheng24c.html](https://proceedings.mlr.press/v235/zheng24c.html)

**TLDR**: This paper proposes leveraging negative samples as a catalyst to improve cohort discovery in healthcare binary diagnosis and prognosis tasks.

## Abstract

In healthcare analytics, addressing binary diagnosis or prognosis tasks presents unique challenges due to the inherent asymmetry between positive and negative samples. While positive samples, indicating patients with a disease, are defined based on stringent medical criteria, negative samples are defined in an open-ended manner and remain underexplored in prior research. To bridge this gap, we propose an innovative approach to facilitate cohort discovery within negative samples, leveraging a Shapley-based exploration of interrelationships between these samples, which holds promise for uncovering valuable insights concerning the studied disease, and related comorbidity and complications. We quantify each sample’s contribution using data Shapley values, subsequently constructing the Negative Sample Shapley Field to model the distribution of all negative samples. Next, we transform this field through manifold learning, preserving the essential data structure information while imposing an isotropy constraint in data Shapley values. Within this transformed space, we pinpoint cohorts of medical interest via density-based clustering. We empirically evaluate the effectiveness of our approach on the real-world electronic medical records from National University Hospital in Singapore, yielding clinically valuable insights aligned with existing knowledge, and benefiting medical research and clinical decision-making.