---
title: "An Image is Worth Multiple Words: Discovering Object Level Concepts using Multi-Concept Prompt Learning"
source: "https://proceedings.mlr.press/v235/jin24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jin24g/jin24g.pdf"
categories: ['generative-models-and-variational-inference', 'quantum-algorithms-for-machine-learning-optimization']
tags: ['textual-inversion', 'multi-concept-learning', 'prompt-learning', 'generative-models']
venue: "ICML 2024"
tldr: "A multi-concept prompt learning method discovers multiple object-level concepts within a single image for controllable novel image synthesis."
---

# An Image is Worth Multiple Words: Discovering Object Level Concepts using Multi-Concept Prompt Learning

**Source**: [https://proceedings.mlr.press/v235/jin24g.html](https://proceedings.mlr.press/v235/jin24g.html)

**TLDR**: A multi-concept prompt learning method discovers multiple object-level concepts within a single image for controllable novel image synthesis.

## Abstract

Textural Inversion, a prompt learning method, learns a singular text embedding for a new "word" to represent image style and appearance, allowing it to be integrated into natural language sentences to generate novel synthesised images. However, identifying multiple unknown object-level concepts within one scene remains a complex challenge. While recent methods have resorted to cropping or masking individual images to learn multiple concepts, these techniques often require prior knowledge of new concepts and are labour-intensive. To address this challenge, we introduce Multi-Concept Prompt Learning (MCPL), where multiple unknown "words" are simultaneously learned from a single sentence-image pair, without any imagery annotations. To enhance the accuracy of word-concept correlation and refine attention mask boundaries, we propose three regularisation techniques: Attention Masking, Prompts Contrastive Loss, and Bind Adjective. Extensive quantitative comparisons with both real-world categories and biomedical images demonstrate that our method can learn new semantically disentangled concepts. Our approach emphasises learning solely from textual embeddings, using less than 10% of the storage space compared to others. The project page, code, and data are available at https://astrazeneca.github.io/mcpl.github.io.