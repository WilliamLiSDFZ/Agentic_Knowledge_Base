---
title: "IBD-PSC: Input-level Backdoor Detection via Parameter-oriented Scaling Consistency"
source: "https://proceedings.mlr.press/v235/hou24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hou24a/hou24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'anomaly-and-out-of-distribution-detection']
tags: ['backdoor-detection', 'adversarial', 'deep-neural-networks', 'input-level', 'parameter-scaling']
venue: "ICML 2024"
tldr: "Proposes IBD-PSC, an input-level backdoor detection method leveraging parameter-oriented scaling consistency to filter backdoor-triggered inputs."
---

# IBD-PSC: Input-level Backdoor Detection via Parameter-oriented Scaling Consistency

**Source**: [https://proceedings.mlr.press/v235/hou24a.html](https://proceedings.mlr.press/v235/hou24a.html)

**TLDR**: Proposes IBD-PSC, an input-level backdoor detection method leveraging parameter-oriented scaling consistency to filter backdoor-triggered inputs.

## Abstract

Deep neural networks (DNNs) are vulnerable to backdoor attacks, where adversaries can maliciously trigger model misclassifications by implanting a hidden backdoor during model training. This paper proposes a simple yet effective input-level backdoor detection (dubbed IBD-PSC) as a ‘firewall’ to filter out malicious testing images. Our method is motivated by an intriguing phenomenon, i.e., parameter-oriented scaling consistency (PSC), where the prediction confidences of poisoned samples are significantly more consistent than those of benign ones when amplifying model parameters. In particular, we provide theoretical analysis to safeguard the foundations of the PSC phenomenon. We also design an adaptive method to select BN layers to scale up for effective detection. Extensive experiments are conducted on benchmark datasets, verifying the effectiveness and efficiency of our IBD-PSC method and its resistance to adaptive attacks. Codes are available at https://github.com/THUYimingLi/BackdoorBox.