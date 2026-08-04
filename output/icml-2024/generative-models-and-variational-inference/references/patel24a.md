---
title: "Variational Inference with Coverage Guarantees in Simulation-Based Inference"
source: "https://proceedings.mlr.press/v235/patel24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/patel24a/patel24a.pdf"
categories: ['generative-models-and-variational-inference', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['variational-inference', 'simulation-based-inference', 'conformal-prediction', 'coverage-guarantees']
venue: "ICML 2024"
tldr: "Proposes Conformal Amortized Variational Inference, adding coverage guarantees to amortized posterior approximations in simulation-based inference via conformal prediction."
---

# Variational Inference with Coverage Guarantees in Simulation-Based Inference

**Source**: [https://proceedings.mlr.press/v235/patel24a.html](https://proceedings.mlr.press/v235/patel24a.html)

**TLDR**: Proposes Conformal Amortized Variational Inference, adding coverage guarantees to amortized posterior approximations in simulation-based inference via conformal prediction.

## Abstract

Amortized variational inference is an often employed framework in simulation-based inference that produces a posterior approximation that can be rapidly computed given any new observation. Unfortunately, there are few guarantees about the quality of these approximate posteriors. We propose Conformalized Amortized Neural Variational Inference (CANVI), a procedure that is scalable, easily implemented, and provides guaranteed marginal coverage. Given a collection of candidate amortized posterior approximators, CANVI constructs conformalized predictors based on each candidate, compares the predictors using a metric known as predictive efficiency, and returns the most efficient predictor. CANVI ensures that the resulting predictor constructs regions that contain the truth with a user-specified level of probability. CANVI is agnostic to design decisions in formulating the candidate approximators and only requires access to samples from the forward model, permitting its use in likelihood-free settings. We prove lower bounds on the predictive efficiency of the regions produced by CANVI and explore how the quality of a posterior approximation relates to the predictive efficiency of prediction regions based on that approximation. Finally, we demonstrate the accurate calibration and high predictive efficiency of CANVI on a suite of simulation-based inference benchmark tasks and an important scientific task: analyzing galaxy emission spectra.