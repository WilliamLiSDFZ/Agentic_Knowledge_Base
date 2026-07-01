---
title: "Information-theoretic Limits of Online Classification with Noisy Labels"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/cea5ebedc384c5f4b4ef6b6eb29c197f-Abstract-Conference.html"
categories: ['machine-learning-theory-and-evaluation-methods', 'online-learning-augmented-algorithms-and-optimization']
tags: ['online-learning', 'noisy-labels', 'information-theoretic-limits']
venue: "NeurIPS 2024"
tldr: "Derives information-theoretic limits for online classification with noisy labels under adversarial feature generation."
---

# Information-theoretic Limits of Online Classification with Noisy Labels

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/cea5ebedc384c5f4b4ef6b6eb29c197f-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/cea5ebedc384c5f4b4ef6b6eb29c197f-Abstract-Conference.html)

**TLDR**: Derives information-theoretic limits for online classification with noisy labels under adversarial feature generation.

## Abstract

We study online classification with general hypothesis classes where the true labels are determined by some function within the class, but are corrupted by unknown stochastic noise, and the features are generated adversarially. Predictions are made using observed noisy labels and noiseless features, while the performance is  measured via minimax risk when comparing against true labels. The noisy mechanism is modeled via a general noisy kernel that specifies, for any individual data point, a set of distributions from which the actual noisy label distribution is chosen. We show that minimax risk is tightly characterized (up to a logarithmic factor of the hypothesis class size) by the Hellinger gap of the noisy label distributions induced by the kernel, independent of other properties such as the means and variances of the noise. Our main technique is based on a novel reduction to an online comparison scheme of two hypotheses, along with a new conditional version of Le Cam-Birgé testing suitable for online settings. Our work provides the first comprehensive characterization of noisy online classification with guarantees that apply to the ground truth while addressing general noisy observations.