---
title: "IncomeSCM: From tabular data set to time-series simulator and causal estimation benchmark"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/f5c7fb98367440a5eb01d70294c180ca-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['causal-discovery-and-inference-methods']
tags: ['causal-estimation', 'benchmark', 'time-series-simulator']
venue: "NeurIPS 2024"
tldr: "IncomeSCM converts a tabular income dataset into a time-series causal simulator for benchmarking observational causal effect estimators."
---

# IncomeSCM: From tabular data set to time-series simulator and causal estimation benchmark

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/f5c7fb98367440a5eb01d70294c180ca-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/f5c7fb98367440a5eb01d70294c180ca-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: IncomeSCM converts a tabular income dataset into a time-series causal simulator for benchmarking observational causal effect estimators.

## Abstract

Evaluating observational estimators of causal effects demands information that is rarely available: unconfounded interventions and outcomes from the population of interest, created either by randomization or adjustment. As a result, it is customary to fall back on simulators when creating benchmark tasks. Simulators offer great control but are often too simplistic to make challenging tasks, either because they are hand-designed and lack the nuances of real-world data, or because they are fit to observational data without structural constraints. In this work, we propose a general, repeatable strategy for turning observational data into sequential structural causal models and challenging estimation tasks by following two simple principles: 1) fitting real-world data where possible, and 2) creating complexity by composing simple, hand-designed mechanisms. We implement these ideas in a highly configurable software package and apply it to the well-known Adult income data set to construct the IncomeSCM simulator. From this, we devise multiple estimation tasks and sample data sets to compare established estimators of causal effects. The tasks present a suitable challenge, with effect estimates varying greatly in quality between methods, despite similar performance in the modeling of factual outcomes, highlighting the need for dedicated causal estimators and model selection criteria.