---
title: "Reducing sequential change detection to sequential estimation"
source: "https://proceedings.mlr.press/v235/shekhar24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shekhar24a/shekhar24a.pdf"
categories: ['sequential-change-detection-theory-and-algorithms', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['sequential-change-detection', 'sequential-estimation', 'distribution-free']
venue: "ICML 2024"
tldr: "This paper reduces sequential change detection to sequential estimation under minimal distributional assumptions, enabling small detection delay with controlled false alarms."
---

# Reducing sequential change detection to sequential estimation

**Source**: [https://proceedings.mlr.press/v235/shekhar24a.html](https://proceedings.mlr.press/v235/shekhar24a.html)

**TLDR**: This paper reduces sequential change detection to sequential estimation under minimal distributional assumptions, enabling small detection delay with controlled false alarms.

## Abstract

We consider the problem of sequential change detection under minimal assumptions on the distribution generating the stream of observations. Formally, our goal is to design a scheme for detecting any changes in a parameter or functional $\theta$ of the data stream distribution that has small detection delay, but guarantees control on the frequency of false alarms in the absence of changes. We describe a simple reduction from sequential change detection to sequential estimation using confidence sequences (CSs): begin a new level-$(1-\alpha)$ CS at each time step, and proclaim a change as soon as the intersection of all active CSs becomes empty. We prove that the average run length of our scheme is at least $1/\alpha$, resulting in a change detection scheme with minimal structural assumptions (thus allowing for possibly dependent observations, and nonparametric distribution classes), but strong guarantees. We also describe an interesting parallel with Lorden’s reduction from change detection to sequential testing and connections to the recent ”e-detector” framework.