---
title: "Modelling Commonsense Commonalities with Multi-Facet Concept Embeddings"
source: "https://aclanthology.org/2024.findings-acl.86/"
pdf_url: ""
categories: ['concept-embedding-taxonomy-hierarchy-representation']
tags: ['concept-embeddings', 'commonsense-knowledge', 'multi-facet-representation']
venue: "ACL 2024"
tldr: "Proposes multi-facet concept embeddings to better capture commonsense commonalities among concepts."
---

# Modelling Commonsense Commonalities with Multi-Facet Concept Embeddings

**Source**: [https://aclanthology.org/2024.findings-acl.86/](https://aclanthology.org/2024.findings-acl.86/)

**TLDR**: Proposes multi-facet concept embeddings to better capture commonsense commonalities among concepts.

## Abstract

AbstractConcept embeddings offer a practical and efficient mechanism for injecting commonsense knowledge into downstream tasks. Their core purpose is often not to predict the commonsense properties of concepts themselves, but rather to identify commonalities, i.e. sets of concepts which share some property of interest. Such commonalities are the basis for inductive generalisation, hence high-quality concept embeddings can make learning easier and more robust. Unfortunately, standard embeddings primarily reflect basic taxonomic categories, making them unsuitable for finding commonalities that refer to more specific aspects (e.g. the colour of objects or the materials they are made of). In this paper, we address this limitation by explicitly modelling the different facets of interest when learning concept embeddings. We show that this leads to embeddings which capture a more diverse range of commonsense properties, and consistently improves results in downstream tasks such as ultra-fine entity typing and ontology completion.