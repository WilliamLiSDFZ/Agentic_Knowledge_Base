---
title: "Slicing Mutual Information Generalization Bounds for Neural Networks"
source: "https://proceedings.mlr.press/v235/nadjahi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nadjahi24a/nadjahi24a.pdf"
categories: ['neural-network-learning-dynamics-theory']
tags: ['generalization-bounds', 'mutual-information', 'slicing']
venue: "ICML 2024"
tldr: "Sliced mutual information is proposed as a tighter information-theoretic generalization bound for neural networks compared to standard MI bounds."
---

# Slicing Mutual Information Generalization Bounds for Neural Networks

**Source**: [https://proceedings.mlr.press/v235/nadjahi24a.html](https://proceedings.mlr.press/v235/nadjahi24a.html)

**TLDR**: Sliced mutual information is proposed as a tighter information-theoretic generalization bound for neural networks compared to standard MI bounds.

## Abstract

The ability of machine learning (ML) algorithms to generalize well to unseen data has been studied through the lens of information theory, by bounding the generalization error with the input-output mutual information (MI), i.e., the MI between the training data and the learned hypothesis. Yet, these bounds have limited practicality for modern ML applications (e.g., deep learning), due to the difficulty of evaluating MI in high dimensions. Motivated by recent findings on the compressibility of neural networks, we consider algorithms that operate by slicing the parameter space, i.e., trained on random lower-dimensional subspaces. We introduce new, tighter information-theoretic generalization bounds tailored for such algorithms, demonstrating that slicing improves generalization. Our bounds offer significant computational and statistical advantages over standard MI bounds, as they rely on scalable alternative measures of dependence, i.e., disintegrated mutual information and $k$-sliced mutual information. Then, we extend our analysis to algorithms whose parameters do not need to exactly lie on random subspaces, by leveraging rate-distortion theory. This strategy yields generalization bounds that incorporate a distortion term measuring model compressibility under slicing, thereby tightening existing bounds without compromising performance or requiring model compression. Building on this, we propose a regularization scheme enabling practitioners to control generalization through compressibility. Finally, we empirically validate our results and achieve the computation of non-vacuous information-theoretic generalization bounds for neural networks, a task that was previously out of reach.