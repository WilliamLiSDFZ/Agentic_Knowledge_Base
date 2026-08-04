---
title: "A Statistical Framework for Data-dependent Retrieval-Augmented Models"
source: "https://proceedings.mlr.press/v235/basu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/basu24a/basu24a.pdf"
categories: ['information-retrieval-and-recommendation-systems', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['retrieval-augmented-generation', 'statistical-framework', 'training', 'prediction', 'information-retrieval']
venue: "ICML 2024"
tldr: "Introduces a statistical framework to study the fundamental properties and training of retrieval-augmented machine learning models."
---

# A Statistical Framework for Data-dependent Retrieval-Augmented Models

**Source**: [https://proceedings.mlr.press/v235/basu24a.html](https://proceedings.mlr.press/v235/basu24a.html)

**TLDR**: Introduces a statistical framework to study the fundamental properties and training of retrieval-augmented machine learning models.

## Abstract

Modern ML systems increasingly augment input instances with additional relevant information to enhance final prediction. Despite growing interest in such retrieval-augmented models, their fundamental properties and training are not well understood. We propose a statistical framework to study such models with two components: 1) a retriever to identify the relevant information out of a large corpus via a data-dependent metric; and 2) a predictor that consumes the input instances along with the retrieved information to make the final predictions. We present a principled method for end-to-end training of both components and draw connections with various training approaches in the literature. Furthermore, we establish excess risk bounds for retrieval-augmented models while delineating the contributions of both retriever and predictor towards the model performance.We validate the utility of our proposed training methods along with the key takeaways from our statistical analysis on open domain question answering task where retrieval augmentation is important.