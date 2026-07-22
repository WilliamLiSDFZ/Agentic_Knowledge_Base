---
title: "Hyperparameter-Free Approach for Faster Minimum Bayes Risk Decoding"
source: "https://aclanthology.org/2024.findings-acl.505/"
pdf_url: ""
categories: ['minimum-bayes-risk-decoding-efficiency', 'collaborative-llm-deployment-and-inference-optimization']
tags: ['minimum-bayes-risk', 'decoding-efficiency', 'hyperparameter-free']
venue: "ACL 2024"
tldr: "Proposes a hyperparameter-free approach to accelerate Minimum Bayes-Risk decoding for text generation tasks."
---

# Hyperparameter-Free Approach for Faster Minimum Bayes Risk Decoding

**Source**: [https://aclanthology.org/2024.findings-acl.505/](https://aclanthology.org/2024.findings-acl.505/)

**TLDR**: Proposes a hyperparameter-free approach to accelerate Minimum Bayes-Risk decoding for text generation tasks.

## Abstract

AbstractMinimum Bayes-Risk (MBR) decoding is shown to be a powerful alternative to beam search decoding for a wide range of text generation tasks. However, MBR requires a huge amount of time for inference to compute the MBR objective, which makes the method infeasible in many situations where response time is critical. Confidence-based pruning (CBP) (Cheng and Vlachos, 2023) has recently been proposed to reduce the inference time in machine translation tasks. Although it is shown to significantly reduce the amount of computation, it requires hyperparameter tuning using a development set to be effective. To this end, we propose Adaptive Minimum Bayes-Risk (AMBR) decoding, a hyperparameter-free method to run MBR decoding efficiently. AMBR is derived from the observation that the problem of computing the sample-based MBR objective is the medoid identification problem. AMBR uses the Correlated Sequential Halving (CSH) algorithm (Baharav and Tse, 2019), the algorithm with the best performance guarantee to date for the medoid identification problem, to compute the sample-based MBR objective. We evaluate AMBR on machine translation, text summarization, and image captioning tasks. The results show that AMBR achieves on par with CBP, with CBP selecting hyperparameters through an Oracle for each given computation budget.