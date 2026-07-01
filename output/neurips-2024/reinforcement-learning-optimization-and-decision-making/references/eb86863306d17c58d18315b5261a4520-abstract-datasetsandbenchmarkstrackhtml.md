---
title: "EpiCare: A Reinforcement Learning Benchmark for Dynamic Treatment Regimes"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/eb86863306d17c58d18315b5261a4520-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['reinforcement-learning-optimization-and-decision-making']
tags: ['healthcare-rl', 'dynamic-treatment-regimes', 'benchmark']
venue: "NeurIPS 2024"
tldr: "Introduces EpiCare, a reinforcement learning benchmark designed for dynamic treatment regime problems in healthcare settings."
---

# EpiCare: A Reinforcement Learning Benchmark for Dynamic Treatment Regimes

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/eb86863306d17c58d18315b5261a4520-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/eb86863306d17c58d18315b5261a4520-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces EpiCare, a reinforcement learning benchmark designed for dynamic treatment regime problems in healthcare settings.

## Abstract

Healthcare applications pose significant challenges to existing reinforcement learning (RL) methods due to implementation risks, low data availability, short treatment episodes, sparse rewards, partial observations, and heterogeneous treatment effects. Despite significant interest in using RL to generate dynamic treatment regimes for longitudinal patient care scenarios, no standardized benchmark has yet been developed.To fill this need we introduce Episodes of Care (EpiCare), a benchmark designed to mimic the challenges associated with applying RL to longitudinal healthcare settings. We leverage this benchmark to test five state-of-the-art offline RL models as well as five common off-policy evaluation (OPE) techniques.Our results suggest that while offline RL may be capable of improving upon existing standards of care given large data availability, its applicability does not appear to extend to the moderate to low data regimes typical of healthcare settings. Additionally, we demonstrate that several OPE techniques which have become standard in the the medical RL literature fail to perform adequately on our benchmark. These results suggest that the performance of RL models in dynamic treatment regimes may be difficult to meaningfully evaluate using current OPE methods, indicating that RL for this application may still be in its early stages. We hope that these results along with the benchmark itself will facilitate the comparison of existing methods and inspire further research into techniques that increase the practical applicability of medical RL.