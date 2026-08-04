---
title: "InterLUDE: Interactions between Labeled and Unlabeled Data to Enhance Semi-Supervised Learning"
source: "https://proceedings.mlr.press/v235/huang24af.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24af/huang24af.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'data-selection-and-active-learning-methods']
tags: ['semi-supervised-learning', 'labeled-unlabeled-interaction', 'image-classification', 'consistency-regularization', 'data-augmentation']
venue: "ICML 2024"
tldr: "Enhances semi-supervised learning by explicitly modeling interactions between labeled and unlabeled data beyond additive loss combinations."
---

# InterLUDE: Interactions between Labeled and Unlabeled Data to Enhance Semi-Supervised Learning

**Source**: [https://proceedings.mlr.press/v235/huang24af.html](https://proceedings.mlr.press/v235/huang24af.html)

**TLDR**: Enhances semi-supervised learning by explicitly modeling interactions between labeled and unlabeled data beyond additive loss combinations.

## Abstract

Semi-supervised learning (SSL) seeks to enhance task performance by training on both labeled and unlabeled data. Mainstream SSL image classification methods mostly optimize a loss that additively combines a supervised classification objective with a regularization term derived solely from unlabeled data. This formulation often neglects the potential for interaction between labeled and unlabeled images. In this paper, we introduce InterLUDE, a new approach to enhance SSL made of two parts that each benefit from labeled-unlabeled interaction. The first part, embedding fusion, interpolates between labeled and unlabeled embeddings to improve representation learning. The second part is a new loss, grounded in the principle of consistency regularization, that aims to minimize discrepancies in the model’s predictions between labeled versus unlabeled inputs. Experiments on standard closed-set SSL benchmarks and a medical SSL task with an uncurated unlabeled set show clear benefits to our approach. On the STL-10 dataset with only 40 labels, InterLUDE achieves 3.2% error rate, while the best previous method reports 6.3%.