---
title: "A Cross-Domain Benchmark for Active Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/72de9826cfe582e175520f404eaad473-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'machine-learning-theory-and-evaluation-methods']
tags: ['active-learning', 'benchmark', 'cross-domain', 'data-annotation', 'experimental-evaluation']
venue: "NeurIPS 2024"
tldr: "Introduces a cross-domain benchmark to rigorously evaluate active learning methods across diverse tasks and repetitions."
---

# A Cross-Domain Benchmark for Active Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/72de9826cfe582e175520f404eaad473-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/72de9826cfe582e175520f404eaad473-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces a cross-domain benchmark to rigorously evaluate active learning methods across diverse tasks and repetitions.

## Abstract

Active Learning (AL) deals with identifying the most informative samples forlabeling to reduce data annotation costs for supervised learning tasks. ALresearch suffers from the fact that lifts from literature generalize poorly andthat only a small number of repetitions of experiments are conducted. To overcomethese obstacles, we propose CDALBench, the first active learning benchmarkwhich includes tasks in computer vision, natural language processing and tabularlearning. Furthermore, by providing an efficient, greedy oracle, CDALBenchcan be evaluated with 50 runs for each experiment. We show, that both thecross-domain character and a large amount of repetitions are crucial forsophisticated evaluation of AL research. Concretely, we show that thesuperiority of specific methods varies over the different domains, making itimportant to evaluate Active Learning with a cross-domain benchmark.Additionally, we show that having a large amount of runs is crucial. With onlyconducting three runs as often done in the literature, the superiority ofspecific methods can strongly vary with the specific runs. This effect is so strong, that, depending on the seed, even a well-established method's performance can be significantly better and significantlyworse than random for the same dataset.