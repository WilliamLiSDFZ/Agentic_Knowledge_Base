---
title: "MARPLE: A Benchmark for Long-Horizon Inference"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/c4c6b9642f3d1c2bf036bb9575f7b5bf-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'visual-language-multimodal-generation-reasoning']
tags: ['benchmark', 'long-horizon-inference', 'multimodal-reasoning', 'event-reconstruction', 'visual-language']
venue: "NeurIPS 2024"
tldr: "Introduces MARPLE, a benchmark for evaluating long-horizon inference requiring integration of visual, language, and auditory evidence."
---

# MARPLE: A Benchmark for Long-Horizon Inference

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/c4c6b9642f3d1c2bf036bb9575f7b5bf-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/c4c6b9642f3d1c2bf036bb9575f7b5bf-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces MARPLE, a benchmark for evaluating long-horizon inference requiring integration of visual, language, and auditory evidence.

## Abstract

Reconstructing past events requires reasoning across long time horizons. To figure out what happened, humans draw on prior knowledge about the world and human behavior and integrate insights from various sources of evidence including visual, language, and auditory cues. We introduce MARPLE, a benchmark for evaluating long-horizon inference capabilities using multi-modal evidence. Our benchmark features agents interacting with simulated households, supporting vision, language, and auditory stimuli, as well as procedurally generated environments and agent behaviors. Inspired by classic ``whodunit'' stories, we ask AI models and human participants to infer which agent caused a change in the environment based on a step-by-step replay of what actually happened. The goal is to correctly identify the culprit as early as possible. Our findings show that human participants outperform both traditional Monte Carlo simulation methods and an LLM baseline (GPT-4) on this task. Compared to humans, traditional inference models are less robust and performant, while GPT-4 has difficulty comprehending environmental changes. We analyze factors influencing inference performance and ablate different modes of evidence, finding that all modes are valuable for performance. Overall, our experiments demonstrate that the long-horizon, multimodal inference tasks in our benchmark present a challenge to current models. Project website: https://marple-benchmark.github.io/.