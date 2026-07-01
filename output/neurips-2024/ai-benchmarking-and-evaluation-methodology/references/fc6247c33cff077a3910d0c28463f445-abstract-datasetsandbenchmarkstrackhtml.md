---
title: "Dispelling the Mirage of Progress in Offline MARL through Standardised Baselines and Evaluation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/fc6247c33cff077a3910d0c28463f445-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'ai-benchmarking-and-evaluation-methodology']
tags: ['offline-MARL', 'evaluation-protocols', 'standardized-baselines']
venue: "NeurIPS 2024"
tldr: "A standardized evaluation framework exposing lack of consistent baselines in offline multi-agent reinforcement learning research."
---

# Dispelling the Mirage of Progress in Offline MARL through Standardised Baselines and Evaluation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/fc6247c33cff077a3910d0c28463f445-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/fc6247c33cff077a3910d0c28463f445-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A standardized evaluation framework exposing lack of consistent baselines in offline multi-agent reinforcement learning research.

## Abstract

Offline multi-agent reinforcement learning (MARL) is an emerging field with great promise for real-world applications. Unfortunately, the current state of research in offline MARL is plagued by inconsistencies in baselines and evaluation protocols, which ultimately makes it difficult to accurately assess progress, trust newly proposed innovations, and allow researchers to easily build upon prior work. In this paper, we firstly identify significant shortcomings in existing methodologies for measuring the performance of novel algorithms through a representative study of published offline MARL work. Secondly, by directly comparing to this prior work, we demonstrate that simple, well-implemented baselines can achieve state-of-the-art (SOTA) results across a wide range of tasks. Specifically, we show that on 35 out of 47 datasets used in prior work (almost 75\% of cases), we match or surpass the performance of the current purported SOTA. Strikingly, our baselines often substantially outperform these more sophisticated algorithms.  Finally, we correct for the shortcomings highlighted from this prior work by introducing a straightforward standardised methodology for evaluation and by providing our baseline implementations with statistically robust results across several scenarios, useful for comparisons in future work. Our proposal includes simple and sensible steps that are easy to adopt, which in combination with solid baselines and comparative results, could substantially improve the overall rigour of empirical science in offline MARL moving forward.