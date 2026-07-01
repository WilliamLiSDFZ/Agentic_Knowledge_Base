---
title: "IWBVT: Instance Weighting-based Bias-Variance Trade-off for Crowdsourcing"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/9baf31febefde7bd76023c2d2f13cbd7-Abstract-Conference.html"
categories: ['machine-learning-theory-and-evaluation-methods', 'statistical-inference-and-text-generation-methods\n\nhmm,-let-me-reconsider---looking-more-carefully-at-the-cluster:\n\n**score-matching-and-sampling-methods**']
tags: ['crowdsourcing', 'bias-variance-tradeoff', 'instance-weighting', 'label-integration', 'noise-correction']
venue: "NeurIPS 2024"
tldr: "Proposes an instance weighting framework to balance bias-variance tradeoff for improving label quality in crowdsourcing settings."
---

# IWBVT: Instance Weighting-based Bias-Variance Trade-off for Crowdsourcing

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/9baf31febefde7bd76023c2d2f13cbd7-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/9baf31febefde7bd76023c2d2f13cbd7-Abstract-Conference.html)

**TLDR**: Proposes an instance weighting framework to balance bias-variance tradeoff for improving label quality in crowdsourcing settings.

## Abstract

In recent years, a large number of algorithms for label integration and noise correction have been proposed to infer the unknown true labels of instances in crowdsourcing. They have made great advances in improving the label quality of crowdsourced datasets. However, due to the presence of intractable instances, these algorithms are usually not as significant in improving the model quality as they are in improving the label quality. To improve the model quality, this paper proposes an instance weighting-based bias-variance trade-off (IWBVT) approach. IWBVT at first proposes a novel instance weighting method based on the complementary set and entropy, which mitigates the impact of intractable instances and thus makes the bias and variance of trained models closer to the unknown true results. Then, IWBVT performs probabilistic loss regressions based on the bias-variance decomposition, which achieves the bias-variance trade-off and thus reduces the generalization error of trained models. Experimental results indicate that IWBVT can serve as a universal post-processing approach to significantly improving the model quality of existing state-of-the-art label integration algorithms and noise correction algorithms.