---
title: "More than Minorities and Majorities: Understanding Multilateral Bias in Language Generation"
source: "https://aclanthology.org/2024.findings-acl.594/"
categories: ['bias-and-fairness-in-llms', 'multilingual-text-classification-and-sentiment-analysis']
tags: ['bias-mitigation', 'demographic-groups', 'multilateral-bias']
venue: "ACL 2024"
tldr: "Proposes a framework for understanding and mitigating bias in language generation beyond binary demographic group comparisons to address multilateral bias across multiple groups simultaneously."
---

# More than Minorities and Majorities: Understanding Multilateral Bias in Language Generation

**Source**: [https://aclanthology.org/2024.findings-acl.594/](https://aclanthology.org/2024.findings-acl.594/)

**TLDR**: Proposes a framework for understanding and mitigating bias in language generation beyond binary demographic group comparisons to address multilateral bias across multiple groups simultaneously.

## Abstract

AbstractPretrained models learned from real corpora can often capture undesirable features, leading to bias issues against different demographic groups. Most existing studies on bias dataset construction or bias mitigation methods only focus on one demographic group pair to study a certain bias, e.g. black vs. white for racial bias. However, in real-world applications, there are more than two demographic groups that are at risk of the same bias. In this paper, we propose to analyze and reduce biases across multiple demographic groups. We collect and build a multi-demographic bias dataset including five commonly discussed bias dimensions. To mitigate multi-demographic bias, we adopt several novel debiasing methods, including regularisation-based and augmentation-based methods, as well as appropriate evaluation metrics for multi-demographic bias measurement. Experimental results on the proposed multi-demographic dataset show that a fairer model can be achieved using a multi-demographic debiasing approach. Also, the model debiased using the proposed multi-demographic debiasing methods can better transfer to unseen demographics without sacrificing the performance of the pretrained model.