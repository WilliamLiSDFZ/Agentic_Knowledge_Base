---
title: "Benchmarking Estimators for Natural Experiments: A Novel Dataset and a Doubly Robust Algorithm"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/9687f7801396bc0eecc9f7edfd8267d5-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['causal-discovery-and-inference-methods', 'ai-benchmarking-and-evaluation-methodology']
tags: ['natural-experiments', 'causal-inference', 'doubly-robust', 'treatment-effect', 'benchmark-dataset']
venue: "NeurIPS 2024"
tldr: "Introduces a novel natural experiment dataset from a literacy nonprofit and proposes a doubly robust algorithm, benchmarking over 20 treatment effect estimators."
---

# Benchmarking Estimators for Natural Experiments: A Novel Dataset and a Doubly Robust Algorithm

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/9687f7801396bc0eecc9f7edfd8267d5-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/9687f7801396bc0eecc9f7edfd8267d5-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces a novel natural experiment dataset from a literacy nonprofit and proposes a doubly robust algorithm, benchmarking over 20 treatment effect estimators.

## Abstract

Estimating the effect of treatments from natural experiments, where treatments are pre-assigned, is an important and well-studied problem. We introduce a novel natural experiment dataset obtained from an early childhood literacy nonprofit. Surprisingly, applying over 20 established estimators to the dataset produces inconsistent results in evaluating the nonprofits efficacy. To address this, we create a benchmark to evaluate estimator accuracy using synthetic outcomes, whose design was guided by domain experts. The benchmark extensively explores performance as real world conditions like sample size, treatment correlation, and propensity score accuracy vary. Based on our benchmark, we observe that the class of doubly robust treatment effect estimators, which are based on simple and intuitive regression adjustment, generally outperform other more complicated estimators by orders of magnitude. To better support our theoretical understanding of doubly robust estimators, we derive a closed form expression for the variance of any such estimator that uses dataset splitting to obtain an unbiased estimate. This expression motivates the design of a new doubly robust estimator that uses a novel loss function when fitting functions for regression adjustment. We release the dataset and benchmark in a Python package; the package is built in a modular way to facilitate new datasets and estimators. https://github.com/rtealwitter/naturalexperiments