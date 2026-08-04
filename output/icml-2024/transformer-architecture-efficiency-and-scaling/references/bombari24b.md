---
title: "Towards Understanding the Word Sensitivity of Attention Layers: A Study via Random Features"
source: "https://proceedings.mlr.press/v235/bombari24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bombari24b/bombari24b.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'neural-network-learning-dynamics-theory']
tags: ['attention-mechanisms', 'transformers', 'word-sensitivity', 'random-features']
venue: "ICML 2024"
tldr: "This paper theoretically analyzes the word sensitivity of attention layers in transformers using random feature approximations to explain their NLP success."
---

# Towards Understanding the Word Sensitivity of Attention Layers: A Study via Random Features

**Source**: [https://proceedings.mlr.press/v235/bombari24b.html](https://proceedings.mlr.press/v235/bombari24b.html)

**TLDR**: This paper theoretically analyzes the word sensitivity of attention layers in transformers using random feature approximations to explain their NLP success.

## Abstract

Understanding the reasons behind the exceptional success of transformers requires a better analysis of why attention layers are suitable for NLP tasks. In particular, such tasks require predictive models to capture contextual meaning which often depends on one or few words, even if the sentence is long. Our work studies this key property, dubbed word sensitivity (WS), in the prototypical setting of random features. We show that attention layers enjoy high WS, namely, there exists a vector in the space of embeddings that largely perturbs the random attention features map. The argument critically exploits the role of the softmax in the attention layer, highlighting its benefit compared to other activations (e.g., ReLU). In contrast, the WS of standard random features is of order $1/\sqrt{n}$, $n$ being the number of words in the textual sample, and thus it decays with the length of the context. We then translate these results on the word sensitivity into generalization bounds: due to their low WS, random features provably cannot learn to distinguish between two sentences that differ only in a single word; in contrast, due to their high WS, random attention features have higher generalization capabilities. We validate our theoretical results with experimental evidence over the BERT-Base word embeddings of the imdb review dataset.