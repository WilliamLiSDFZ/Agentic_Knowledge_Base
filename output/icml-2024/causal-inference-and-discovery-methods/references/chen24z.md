---
title: "Identifiability Matters: Revealing the Hidden Recoverable Condition in Unbiased Learning to Rank"
source: "https://proceedings.mlr.press/v235/chen24z.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24z/chen24z.pdf"
categories: ['information-retrieval-and-recommendation-systems', 'causal-inference-and-discovery-methods']
tags: ['unbiased-learning-to-rank', 'click-models', 'identifiability', 'examination-hypothesis']
venue: "ICML 2024"
tldr: "Reveals a hidden identifiability condition that determines when true relevance is recoverable in unbiased learning-to-rank from biased click logs."
---

# Identifiability Matters: Revealing the Hidden Recoverable Condition in Unbiased Learning to Rank

**Source**: [https://proceedings.mlr.press/v235/chen24z.html](https://proceedings.mlr.press/v235/chen24z.html)

**TLDR**: Reveals a hidden identifiability condition that determines when true relevance is recoverable in unbiased learning-to-rank from biased click logs.

## Abstract

Unbiased Learning to Rank (ULTR) aims to train unbiased ranking models from biased click logs, by explicitly modeling a generation process for user behavior and fitting click data based on examination hypothesis. Previous research found empirically that the true latent relevance is mostly recoverable through click fitting. However, we demonstrate that this is not always achievable, resulting in a significant reduction in ranking performance. This research investigates the conditions under which relevance can be recovered from click data in the first principle. We initially characterize a ranking model as identifiable if it can recover the true relevance up to a scaling transformation, a criterion sufficient for the pairwise ranking objective. Subsequently, we investigate an equivalent condition for identifiability, articulated as a graph connectivity test problem: the recovery of relevance is feasible if and only if the identifiability graph (IG), derived from the underlying structure of the dataset, is connected. The presence of a disconnected IG may lead to degenerate cases and suboptimal ranking performance. To tackle this challenge, we introduce two methods, namely node intervention and node merging, designed to modify the dataset and restore the connectivity of the IG. Empirical results derived from a simulated dataset and two real-world LTR benchmark datasets not only validate our proposed theory, but also demonstrate the effectiveness of our methods in alleviating data bias when the relevance model is unidentifiable.