---
title: "Two Heads are Actually Better than One: Towards Better Adversarial Robustness via Transduction and Rejection"
source: "https://proceedings.mlr.press/v235/palumbo24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/palumbo24a/palumbo24a.pdf"
categories: ['adversarial-robustness-and-model-security']
tags: ['adversarial-robustness', 'transduction', 'rejection', 'provable-guarantees']
venue: "ICML 2024"
tldr: "Shows that combining transduction and rejection practically and provably improves adversarial robustness beyond either technique alone."
---

# Two Heads are Actually Better than One: Towards Better Adversarial Robustness via Transduction and Rejection

**Source**: [https://proceedings.mlr.press/v235/palumbo24a.html](https://proceedings.mlr.press/v235/palumbo24a.html)

**TLDR**: Shows that combining transduction and rejection practically and provably improves adversarial robustness beyond either technique alone.

## Abstract

Both transduction and rejection have emerged as important techniques for defending against adversarial perturbations. A recent work by Goldwasser et. al showed that rejection combined with transduction can give provable guarantees (for certain problems) that cannot be achieved otherwise. Nevertheless, under recent strong adversarial attacks (GMSA), Goldwasser et al.’s work was shown to have low performance in a practical deep-learning setting. In this paper, we take a step towards realizing the promise of transduction+rejection in more realistic scenarios. Our key observation is that a novel application of a reduction technique by Tramèr, which was until now only used to demonstrate the vulnerability of certain defenses, can be used to actually construct effective defenses. Theoretically, we show that a careful application of this technique in the transductive setting can give significantly improved sample-complexity for robust generalization. Our theory guides us to design a new transductive algorithm for learning a selective model; extensive experiments using state of the art attacks (AutoAttack, GMSA) show that our approach provides significantly better robust accuracy (81.6% on CIFAR-10 and 57.9% on CIFAR-100 under $l_\infty$ with budget 8/255) than existing techniques. The implementation is available at https://github.com/nilspalumbo/transduction-rejection.