---
title: "OAK: Enriching Document Representations using Auxiliary Knowledge for Extreme Classification"
source: "https://proceedings.mlr.press/v235/mohan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mohan24a/mohan24a.pdf"
categories: ['information-retrieval-and-recommendation-systems', 'data-selection-and-active-learning-methods']
tags: ['extreme-classification', 'auxiliary-knowledge', 'document-representation']
venue: "ICML 2024"
tldr: "Proposes OAK, a method enriching document representations with auxiliary knowledge to improve performance in extreme multi-label classification."
---

# OAK: Enriching Document Representations using Auxiliary Knowledge for Extreme Classification

**Source**: [https://proceedings.mlr.press/v235/mohan24a.html](https://proceedings.mlr.press/v235/mohan24a.html)

**TLDR**: Proposes OAK, a method enriching document representations with auxiliary knowledge to improve performance in extreme multi-label classification.

## Abstract

The objective in eXtreme Classification (XC) is to find relevant labels for a document from an exceptionally large label space. Most XC application scenarios have rich auxiliary data associated with the input documents, e.g., frequently clicked webpages for search queries in sponsored search. Unfortunately, most of the existing XC methods do not use any auxiliary data. In this paper, we propose a novel framework, Online Auxiliary Knowledge (OAK), which harnesses auxiliary information linked to the document to improve XC accuracy. OAK stores information learnt from the auxiliary data in a knowledge bank and during a forward pass, retrieves relevant auxiliary knowledge embeddings for a given document. An enriched embedding is obtained by fusing these auxiliary knowledge embeddings with the document’s embedding, thereby enabling much more precise candidate label selection and final classification. OAK training involves three stages. (1) Training a linker module to link documents to relevant auxiliary data points. (2) Learning an embedding for documents enriched using linked auxiliary information. (3) Using the enriched document embeddings to learn the final classifiers. OAK outperforms current state-of-the-art XC methods by up to $\sim 5 %$ on academic datasets, and by $\sim 3 %$ on an auxiliary data-augmented variant of LF-ORCAS-800K dataset in Precision@1. OAK also demonstrates statistically significant improvements in sponsored search metrics when deployed on a large scale search engine.