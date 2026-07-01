---
title: "Bench2Drive: Towards Multi-Ability Benchmarking of Closed-Loop End-To-End Autonomous Driving"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/017761f94a1cd66d01c041aff85492c4-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['autonomous-driving-and-trajectory-prediction', 'ai-benchmarking-and-evaluation-methodology']
tags: ['autonomous-driving', 'end-to-end', 'closed-loop-benchmark']
venue: "NeurIPS 2024"
tldr: "Bench2Drive introduces a multi-ability closed-loop benchmark for evaluating end-to-end autonomous driving methods at scale."
---

# Bench2Drive: Towards Multi-Ability Benchmarking of Closed-Loop End-To-End Autonomous Driving

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/017761f94a1cd66d01c041aff85492c4-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/017761f94a1cd66d01c041aff85492c4-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Bench2Drive introduces a multi-ability closed-loop benchmark for evaluating end-to-end autonomous driving methods at scale.

## Abstract

In an era marked by the rapid scaling of foundation models, autonomous driving technologies are approaching a transformative threshold where end-to-end autonomous driving (E2E-AD) emerges due to its potential of scaling up in the data-driven manner. However, existing E2E-AD methods are mostly evaluated under the open-loop log-replay manner with L2 errors and collision rate as metrics (e.g., in nuScenes), which could not fully reflect the driving performance of algorithms as recently acknowledged in the community. For those E2E-AD methods evaluated under the closed-loop protocol, they are tested in fixed routes (e.g., Town05Long and Longest6 in CARLA) with the driving score as metrics, which is known for high variance due to the unsmoothed metric function and large randomness in the long route. Besides, these methods usually collect their own data for training, which makes algorithm-level fair comparison infeasible.    To fulfill the paramount need of comprehensive, realistic, and fair testing environments for Full Self-Driving (FSD), we present Bench2Drive, the first benchmark for evaluating E2E-AD systems' multiple abilities in a closed-loop manner. Bench2Drive's official training data consists of 2 million fully annotated frames, collected from 10000 short clips uniformly distributed under 44 interactive scenarios (cut-in, overtaking, detour, etc), 23 weathers (sunny, foggy, rainy, etc), and 12 towns (urban, village, university, etc) in CARLA v2. Its evaluation protocol requires E2E-AD models to pass 44 interactive scenarios under different locations and weathers which sums up to 220 routes and thus provides a comprehensive and disentangled assessment about their driving capability under different situations. We implement state-of-the-art E2E-AD models and evaluate them in Bench2Drive, providing insights regarding current status and future directions.