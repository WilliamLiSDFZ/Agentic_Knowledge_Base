---
title: "Optimal Transport Guided Correlation Assignment for Multimodal Entity Linking"
source: "https://aclanthology.org/2024.findings-acl.243/"
categories: ['multimodal-language-vision-learning-systems', 'concept-embedding-taxonomy-hierarchy-representation']
tags: ['multimodal-entity-linking', 'optimal-transport', 'knowledge-graph', 'modality-gap', 'correlation']
venue: "ACL 2024"
tldr: "Uses optimal transport to guide correlation assignment for fine-grained multimodal entity linking across modality gaps."
---

# Optimal Transport Guided Correlation Assignment for Multimodal Entity Linking

**Source**: [https://aclanthology.org/2024.findings-acl.243/](https://aclanthology.org/2024.findings-acl.243/)

**TLDR**: Uses optimal transport to guide correlation assignment for fine-grained multimodal entity linking across modality gaps.

## Abstract

AbstractMultimodal entity linking (MEL) aims to link ambiguous mentions in multimodal contexts to entities in a multimodal knowledge graph. A pivotal challenge is to fully leverage multi-element correlations between mentions and entities to bridge modality gap and enable fine-grained semantic matching. Existing methods attempt several local correlative mechanisms, relying heavily on the automatically learned attention weights, which may over-concentrate on partial correlations. To mitigate this issue, we formulate the correlation assignment problem as an optimal transport (OT) problem, and propose a novel MEL framework, namely OT-MEL, with OT-guided correlation assignment. Thereby, we exploit the correlation between multimodal features to enhance multimodal fusion, and the correlation between mentions and entities to enhance fine-grained matching. To accelerate model prediction, we further leverage knowledge distillation to transfer OT assignment knowledge to attention mechanism. Experimental results show that our model significantly outperforms previous state-of-the-art baselines and confirm the effectiveness of the OT-guided correlation assignment.