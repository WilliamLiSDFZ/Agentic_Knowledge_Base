---
title: "Do Counterfactually Fair Image Classifiers Satisfy Group Fairness? -- A Theoretical and Empirical Study"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/65b4660c1fee9842472e1557b582c940-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['fairness-aware-machine-learning-methods', 'causal-discovery-and-inference-methods']
tags: ['counterfactual-fairness', 'group-fairness', 'image-classification']
venue: "NeurIPS 2024"
tldr: "This paper theoretically and empirically investigates the relationship between counterfactual fairness and group fairness in image classification tasks."
---

# Do Counterfactually Fair Image Classifiers Satisfy Group Fairness? -- A Theoretical and Empirical Study

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/65b4660c1fee9842472e1557b582c940-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/65b4660c1fee9842472e1557b582c940-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: This paper theoretically and empirically investigates the relationship between counterfactual fairness and group fairness in image classification tasks.

## Abstract

The notion of algorithmic fairness has been actively explored from various aspects of fairness, such as counterfactual fairness (CF) and group fairness (GF). However, the exact relationship between CF and GF remains to be unclear, especially in image classification tasks; the reason is because we often cannot collect counterfactual samples regarding a sensitive attribute, essential for evaluating CF, from the existing images (e.g., a photo of the same person but with different secondary sex characteristics). In this paper, we construct new image datasets for evaluating CF by using a high-quality image editing method and carefully labeling with human annotators. Our datasets, CelebA-CF and LFW-CF, build upon the popular image GF benchmarks; hence, we can evaluate CF and GF simultaneously. We empirically observe that CF does not imply GF in image classification, whereas previous studies on tabular datasets observed the opposite. We theoretically show that it could be due to the existence of a latent attribute $G$ that is correlated with, but not caused by, the sensitive attribute (e.g., secondary sex characteristics are highly correlated with hair length). From this observation, we propose a simple baseline,  Counterfactual Knowledge Distillation (CKD), to mitigate such correlation with the sensitive attributes. Extensive experimental results on CelebA-CF and LFW-CF demonstrate that CF-achieving models satisfy GF if we successfully reduce the reliance on $G$ (e.g., using CKD).