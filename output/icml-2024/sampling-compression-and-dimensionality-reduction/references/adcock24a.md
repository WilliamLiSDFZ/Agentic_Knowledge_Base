---
title: "A Unified Framework for Learning with Nonlinear Model Classes from Arbitrary Linear Samples"
source: "https://proceedings.mlr.press/v235/adcock24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/adcock24a/adcock24a.pdf"
categories: ['sampling-compression-and-dimensionality-reduction']
tags: ['nonlinear-model-classes', 'hilbert-spaces', 'linear-measurements', 'sample-complexity']
venue: "ICML 2024"
tldr: "Presents a unified framework for learning nonlinear model classes from arbitrary linear samples in Hilbert spaces."
---

# A Unified Framework for Learning with Nonlinear Model Classes from Arbitrary Linear Samples

**Source**: [https://proceedings.mlr.press/v235/adcock24a.html](https://proceedings.mlr.press/v235/adcock24a.html)

**TLDR**: Presents a unified framework for learning nonlinear model classes from arbitrary linear samples in Hilbert spaces.

## Abstract

This work considers the fundamental problem of learning an unknown object from training data using a given model class. We introduce a framework that allows for objects in arbitrary Hilbert spaces, general types of (random) linear measurements as training data and general types of nonlinear model classes. We establish a series of learning guarantees for this framework, which provide explicit relations between the amount of training data and the model class to ensure near-best generalization bounds. In doing so, we introduce the key notion of the variation of a model class with respect to a distribution of sampling operators. We show that this framework can accommodate many different types of well-known problems of interest, such as matrix sketching by random sampling, compressed sensing with isotropic vectors, active learning in regression and compressed sensing with generative models. In all cases, known results become straightforward corollaries of our general theory. Hence, this work provides a powerful framework for studying and analyzing many different types of learning problems.