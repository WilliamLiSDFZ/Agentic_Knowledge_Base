---
title: "What Are You Token About? Differentiable Perturbed Top-k Token Selection for Scientific Document Summarization"
source: "https://aclanthology.org/2024.findings-acl.561/"
pdf_url: ""
categories: ['text-simplification-evaluation-and-methods']
tags: ['scientific-summarization', 'token-selection', 'differentiable']
venue: "ACL 2024"
tldr: "Introduces differentiable perturbed top-k token selection for scientific document summarization addressing source heterogeneity in datasets."
---

# What Are You Token About? Differentiable Perturbed Top-k Token Selection for Scientific Document Summarization

**Source**: [https://aclanthology.org/2024.findings-acl.561/](https://aclanthology.org/2024.findings-acl.561/)

**TLDR**: Introduces differentiable perturbed top-k token selection for scientific document summarization addressing source heterogeneity in datasets.

## Abstract

AbstractScientific document summarization aims to condense complex and long articles in both technical and plain-language terms to facilitate the accessibility and dissemination of scientific findings. Existing datasets suffer from a deficiency in source heterogeneity, as their data predominantly stem from a single common resource, hindering effective model training and generalizability. First, we introduce SciLay, a novel dataset that includes documents from multiple natural science journals with expert-authored technical and lay summaries. Second, we propose PrunePert, a new transformer-based model that incorporates a differentiable perturbed top-k encoder layer to prune irrelevant tokens in end-to-end learning. Experimental results show that our model achieves a nearly 2x speed-up compared to a state-of-the-art linear transformer, remaining comparable in effectiveness. Additional examinations underscore the importance of employing a training dataset that includes different sources to enhance the generalizability of the models. Code is available at https://github.com/disi-unibo-nlp/sci-lay.