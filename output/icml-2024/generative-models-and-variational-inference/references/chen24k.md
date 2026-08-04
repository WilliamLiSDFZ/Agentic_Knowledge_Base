---
title: "Robust Classification via a Single Diffusion Model"
source: "https://proceedings.mlr.press/v235/chen24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24k/chen24k.pdf"
categories: ['adversarial-robustness-and-model-security', 'generative-models-and-variational-inference']
tags: ['adversarial-robustness', 'diffusion-purification', 'classifier-training', 'adaptive-attacks']
venue: "ICML 2024"
tldr: "A method that leverages a single diffusion model to achieve robust classification by combining purification and adversarial training objectives."
---

# Robust Classification via a Single Diffusion Model

**Source**: [https://proceedings.mlr.press/v235/chen24k.html](https://proceedings.mlr.press/v235/chen24k.html)

**TLDR**: A method that leverages a single diffusion model to achieve robust classification by combining purification and adversarial training objectives.

## Abstract

Diffusion models have been applied to improve adversarial robustness of image classifiers by purifying the adversarial noises or generating realistic data for adversarial training. However, diffusion-based purification can be evaded by stronger adaptive attacks while adversarial training does not perform well under unseen threats, exhibiting inevitable limitations of these methods. To better harness the expressive power of diffusion models, this paper proposes Robust Diffusion Classifier (RDC), a generative classifier that is constructed from a pre-trained diffusion model to be adversarially robust. RDC first maximizes the data likelihood of a given input and then predicts the class probabilities of the optimized input using the conditional likelihood estimated by the diffusion model through Bayes’ theorem. To further reduce the computational cost, we propose a new diffusion backbone called multi-head diffusion and develop efficient sampling strategies. As RDC does not require training on particular adversarial attacks, we demonstrate that it is more generalizable to defend against multiple unseen threats. In particular, RDC achieves $75.67%$ robust accuracy against various $\ell_\infty$ norm-bounded adaptive attacks with $\epsilon_\infty=8/255$ on CIFAR-10, surpassing the previous state-of-the-art adversarial training models by $+4.77%$. The results highlight the potential of generative classifiers by employing pre-trained diffusion models for adversarial robustness compared with the commonly studied discriminative classifiers.