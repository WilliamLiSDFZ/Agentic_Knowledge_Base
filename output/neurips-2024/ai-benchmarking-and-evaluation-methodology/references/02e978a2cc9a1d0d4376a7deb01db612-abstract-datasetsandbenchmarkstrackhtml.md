---
title: "Sim2Real-Fire: A Multi-modal Simulation Dataset for Forecast and Backtracking of Real-world Forest Fire"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/02e978a2cc9a1d0d4376a7deb01db612-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['physics-informed-neural-operators-and-simulations', 'ai-benchmarking-and-evaluation-methodology']
tags: ['wildfire-simulation', 'sim-to-real', 'multimodal-dataset']
venue: "NeurIPS 2024"
tldr: "A multi-modal simulation dataset for training AI models to forecast and backtrack real-world forest fire spread patterns."
---

# Sim2Real-Fire: A Multi-modal Simulation Dataset for Forecast and Backtracking of Real-world Forest Fire

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/02e978a2cc9a1d0d4376a7deb01db612-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/02e978a2cc9a1d0d4376a7deb01db612-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A multi-modal simulation dataset for training AI models to forecast and backtrack real-world forest fire spread patterns.

## Abstract

The latest research on wildfire forecast and backtracking has adopted AI models, which require a large amount of data from wildfire scenarios to capture fire spread patterns. This paper explores using cost-effective simulated wildfire scenarios to train AI models and apply them to the analysis of real-world wildfire. This solution requires AI models to minimize the Sim2Real gap, a brand-new topic in the fire spread analysis research community. To investigate the possibility of minimizing the Sim2Real gap, we collect the Sim2Real-Fire dataset that contains 1M simulated scenarios with multi-modal environmental information for training AI models. We prepare 1K real-world wildfire scenarios for testing the AI models. We also propose a deep transformer, S2R-FireTr, which excels in considering the multi-modal environmental information for forecasting and backtracking the wildfire. S2R-FireTr surpasses state-of-the-art methods in real-world wildfire scenarios.