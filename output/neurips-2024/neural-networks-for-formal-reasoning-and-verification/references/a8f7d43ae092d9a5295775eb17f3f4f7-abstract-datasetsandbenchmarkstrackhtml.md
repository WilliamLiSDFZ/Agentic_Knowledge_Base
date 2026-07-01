---
title: "InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a8f7d43ae092d9a5295775eb17f3f4f7-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'neural-networks-for-formal-reasoning-and-verification']
tags: ['mechanistic-interpretability', 'circuit-discovery', 'semi-synthetic-transformers', 'evaluation', 'benchmarking']
venue: "NeurIPS 2024"
tldr: "InterpBench provides semi-synthetic transformers with known circuits to rigorously evaluate mechanistic interpretability techniques."
---

# InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a8f7d43ae092d9a5295775eb17f3f4f7-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/a8f7d43ae092d9a5295775eb17f3f4f7-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: InterpBench provides semi-synthetic transformers with known circuits to rigorously evaluate mechanistic interpretability techniques.

## Abstract

Mechanistic interpretability methods aim to identify the algorithm a neural network implements, but it is difficult to validate such methods when the true algorithm is unknown. This work presents InterpBench, a collection of semi-synthetic yet realistic transformers with known circuits for evaluating these techniques. We train simple neural networks using a stricter version of Interchange Intervention Training (IIT) which we call Strict IIT (SIIT). Like the original, SIIT trains neural networks by aligning their internal computation with a desired high-level causal model, but it also prevents non-circuit nodes from affecting the model's output. We evaluate SIIT on sparse transformers produced by the Tracr tool and find that SIIT models maintain Tracr's original circuit while being more realistic. SIIT can also train transformers with larger circuits, like Indirect Object Identification (IOI). Finally, we use our benchmark to evaluate existing circuit discovery techniques.