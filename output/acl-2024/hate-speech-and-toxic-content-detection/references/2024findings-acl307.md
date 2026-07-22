---
title: "Plausible Extractive Rationalization through Semi-Supervised Entailment Signal"
source: "https://aclanthology.org/2024.findings-acl.307/"
categories: ['causal-reasoning-and-explanation-in-nlp', 'hate-speech-and-toxic-content-detection']
tags: ['extractive-rationalization', 'semi-supervised', 'entailment']
venue: "ACL 2024"
tldr: "Proposes a semi-supervised entailment signal approach for producing plausible extractive rationalizations in interpretable models."
---

# Plausible Extractive Rationalization through Semi-Supervised Entailment Signal

**Source**: [https://aclanthology.org/2024.findings-acl.307/](https://aclanthology.org/2024.findings-acl.307/)

**TLDR**: Proposes a semi-supervised entailment signal approach for producing plausible extractive rationalizations in interpretable models.

## Abstract

AbstractThe increasing use of complex and opaque black box models requires the adoption of interpretable measures, one such option is extractive rationalizing models, which serve as a more interpretable alternative. These models, also known as Explain-Then-Predict models, employ an explainer model to extract rationales and subsequently condition the predictor with the extracted information. Their primary objective is to provide precise and faithful explanations, represented by the extracted rationales. In this paper, we take a semi-supervised approach to optimize for the plausibility of extracted rationales. We adopt a pre-trained natural language inference (NLI) model and further fine-tune it on a small set of supervised rationales (10%). The NLI predictor is leveraged as a source of supervisory signals to the explainer via entailment alignment. We show that, by enforcing the alignment agreement between the explanation and answer in a question-answering task, the performance can be improved without access to ground truth labels. We evaluate our approach on the ERASER dataset and show that our approach achieves comparable results with supervised extractive models and outperforms unsupervised approaches by > 100%.