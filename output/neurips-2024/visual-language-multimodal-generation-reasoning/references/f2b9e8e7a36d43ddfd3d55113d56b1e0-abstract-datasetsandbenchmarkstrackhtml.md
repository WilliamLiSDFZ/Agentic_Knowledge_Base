---
title: "Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/f2b9e8e7a36d43ddfd3d55113d56b1e0-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['molecular-structure-elucidation', 'multimodal-benchmark', 'chemical-reasoning']
venue: "NeurIPS 2024"
tldr: "Introduces a multimodal benchmark for evaluating LLM proficiency at multi-step molecular structure elucidation from spectroscopic and chemical data."
---

# Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/f2b9e8e7a36d43ddfd3d55113d56b1e0-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/f2b9e8e7a36d43ddfd3d55113d56b1e0-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces a multimodal benchmark for evaluating LLM proficiency at multi-step molecular structure elucidation from spectroscopic and chemical data.

## Abstract

Large Language Models (LLMs)  have shown significant problem-solving capabilities across predictive and generative tasks in chemistry. However, their proficiency in multi-step chemical reasoning remains underexplored. We introduce a new challenge: molecular structure elucidation, which involves deducing a molecule’s structure from various types of spectral data. Solving such a molecular puzzle, akin to solving crossword puzzles, poses reasoning challenges that require integrating clues from diverse sources and engaging in iterative hypothesis testing. To address this challenging problem with LLMs, we present \textbf{MolPuzzle}, a benchmark comprising 217 instances of structure elucidation, which feature over 23,000 QA samples presented in a sequential puzzle-solving process, involving three interlinked sub-tasks: molecule understanding, spectrum interpretation, and molecule construction. Our evaluation of 12 LLMs reveals that the best-performing LLM, GPT-4o, performs significantly worse than humans, with only a small portion (1.4\%) of its answers exactly matching the ground truth. However, it performs nearly perfectly in the first subtask of molecule understanding, achieving accuracy close to 100\%. This discrepancy highlights the potential of developing advanced LLMs with improved chemical reasoning capabilities in the other two sub-tasks. Our MolPuzzle dataset and evaluation code are available at this  \href{https://github.com/KehanGuo2/MolPuzzle}{link}.