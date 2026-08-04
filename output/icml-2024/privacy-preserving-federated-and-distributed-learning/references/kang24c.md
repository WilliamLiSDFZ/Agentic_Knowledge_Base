---
title: "Certifiably Byzantine-Robust Federated Conformal Prediction"
source: "https://proceedings.mlr.press/v235/kang24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kang24c/kang24c.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['federated-learning', 'conformal-prediction', 'Byzantine-robustness', 'prediction-sets']
venue: "ICML 2024"
tldr: "Proposes certifiably Byzantine-robust federated conformal prediction for constructing valid prediction sets under adversarial clients."
---

# Certifiably Byzantine-Robust Federated Conformal Prediction

**Source**: [https://proceedings.mlr.press/v235/kang24c.html](https://proceedings.mlr.press/v235/kang24c.html)

**TLDR**: Proposes certifiably Byzantine-robust federated conformal prediction for constructing valid prediction sets under adversarial clients.

## Abstract

Conformal prediction has shown impressive capacity in constructing statistically rigorous prediction sets for machine learning models with exchangeable data samples. The siloed datasets, coupled with the escalating privacy concerns related to local data sharing, have inspired recent innovations extending conformal prediction into federated environments with distributed data samples. However, this framework for distributed uncertainty quantification is susceptible to Byzantine failures. A minor subset of malicious clients can significantly compromise the practicality of coverage guarantees. To address this vulnerability, we introduce a novel framework Rob-FCP, which executes robust federated conformal prediction, effectively countering malicious clients capable of reporting arbitrary statistics with the conformal calibration process. We theoretically provide the conformal coverage bound of Rob-FCP in the Byzantine setting and show that the coverage of Rob-FCP is asymptotically close to the desired coverage level. We also propose a malicious client number estimator to tackle a more challenging setting where the number of malicious clients is unknown to the defender and theoretically shows its effectiveness. We empirically demonstrate the robustness of Rob-FCP against diverse proportions of malicious clients under a variety of Byzantine attacks on five standard benchmark and real-world healthcare datasets.