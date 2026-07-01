---
title: "Towards Open Respiratory Acoustic Foundation Models: Pretraining and Benchmarking"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/2f803abdcad9de35b45d5a656dade45c-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['audio-visual-speech-processing-and-benchmarks']
tags: ['respiratory-audio', 'foundation-models', 'pretraining', 'benchmarking', 'healthcare-audio']
venue: "NeurIPS 2024"
tldr: "Develops and benchmarks open respiratory acoustic foundation models pretrained on coughing and breathing sounds for healthcare applications."
---

# Towards Open Respiratory Acoustic Foundation Models: Pretraining and Benchmarking

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/2f803abdcad9de35b45d5a656dade45c-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/2f803abdcad9de35b45d5a656dade45c-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Develops and benchmarks open respiratory acoustic foundation models pretrained on coughing and breathing sounds for healthcare applications.

## Abstract

Respiratory audio, such as coughing and breathing sounds, has predictive power for a wide range of healthcare applications, yet is currently under-explored. The main problem for those applications arises from the difficulty in collecting large labeled task-specific data for model development. Generalizable respiratory acoustic foundation models pretrained with unlabeled data would offer appealing advantages and possibly unlock this impasse.  However, given the safety-critical nature of healthcare applications, it is pivotal to also ensure openness and replicability for any proposed foundation model solution. To this end, we introduce OPERA, an OPEn Respiratory Acoustic foundation model pretraining and benchmarking system, as the first approach answering this need. We curate large-scale respiratory audio datasets ($\sim$136K samples, over 400 hours), pretrain three pioneering foundation models, and build a benchmark consisting of 19 downstream respiratory health tasks for evaluation. Our pretrained models demonstrate superior performance (against existing acoustic models pretrained with general audio on 16 out of 19 tasks) and generalizability (to unseen datasets and new respiratory audio modalities). This highlights the great promise of respiratory acoustic foundation models and encourages more studies using OPERA as an open resource to accelerate research on respiratory audio for health. The system is accessible from https://github.com/evelyn0414/OPERA.