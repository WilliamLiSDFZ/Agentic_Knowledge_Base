---
title: "An Element is Worth a Thousand Words: Enhancing Legal Case Retrieval by Incorporating Legal Elements"
source: "https://aclanthology.org/2024.findings-acl.139/"
pdf_url: ""
categories: ['legal-nlp-benchmarks-and-applications']
tags: ['legal-case-retrieval', 'legal-elements', 'relevance-modeling']
venue: "ACL 2024"
tldr: "This paper enhances legal case retrieval by incorporating legal elements to capture domain-specific relevance beyond semantic similarity."
---

# An Element is Worth a Thousand Words: Enhancing Legal Case Retrieval by Incorporating Legal Elements

**Source**: [https://aclanthology.org/2024.findings-acl.139/](https://aclanthology.org/2024.findings-acl.139/)

**TLDR**: This paper enhances legal case retrieval by incorporating legal elements to capture domain-specific relevance beyond semantic similarity.

## Abstract

AbstractLegal case retrieval plays an important role in promoting judicial justice and fairness. One of its greatest challenges is that the definition of relevance goes far beyond the common semantic relevance as in ad-hoc retrieval. In this paper, we reveal that the legal elements, which typically comprise key facts in a specialized legal context, can largely improve the relevance matching of legal case retrieval. To facilitate the use of legal elements, we construct a Chinese legal element dataset called LeCaRD-Elem based on the widely-used LeCaRD dataset, through a two-stage semi-automatic method with a minimized reliance on human labor. Meanwhile, we introduce two new models to enhance legal search using legal elements. The first, Elem4LCR-E, is a two-stage model that explicitly predicts legal elements from texts and then leverages them for improved ranking. Recognizing the potential benefits of more seamless integration, we further propose an end-to-end model called Elem4LCR-I, which internalizes the legal element knowledge into its model parameters using a tailored teacher-student training framework. Extensive experiments underscore the significant value of legal elements and demonstrate the superiority of our two proposed models in enhancing legal search over existing methods.