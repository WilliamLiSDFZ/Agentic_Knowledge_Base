---
title: "ConMe: Rethinking Evaluation of Compositional Reasoning for Modern VLMs"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/28aad3b3b315d86910d7f4ee2867dfa4-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['compositional-reasoning', 'vision-language-models', 'benchmark-evaluation']
venue: "NeurIPS 2024"
tldr: "A new benchmark and evaluation framework for testing compositional reasoning in modern VLMs by examining attributes, relations, and word order understanding."
---

# ConMe: Rethinking Evaluation of Compositional Reasoning for Modern VLMs

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/28aad3b3b315d86910d7f4ee2867dfa4-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/28aad3b3b315d86910d7f4ee2867dfa4-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A new benchmark and evaluation framework for testing compositional reasoning in modern VLMs by examining attributes, relations, and word order understanding.

## Abstract

Compositional Reasoning (CR) entails grasping the significance of attributes, relations, and word order. Recent Vision-Language Models (VLMs), comprising a visual encoder and a Large Language Model (LLM) decoder, have demonstrated remarkable proficiency in such reasoning tasks. This prompts a crucial question: have VLMs effectively tackled the CR challenge? We conjecture that existing CR benchmarks may not adequately push the boundaries of modern VLMs due to the reliance on an LLM only negative text generation pipeline. Consequently, the negatives produced either appear as outliers from the natural language distribution learned by VLMs' LLM decoders or as improbable within the corresponding image context. To address these limitations, we introduce ConMe\footnote{ConMe is an abbreviation for Confuse Me.} -- a compositional reasoning benchmark and a novel data generation pipeline leveraging VLMs to produce `hard CR Q&A'. Through a new concept of VLMs conversing with each other to collaboratively expose their weaknesses, our pipeline autonomously generates, evaluates, and selects challenging compositional reasoning questions, establishing a robust CR benchmark, also subsequently validated manually. Our benchmark provokes a noteworthy, up to 33%, decrease in CR performance compared to preceding benchmarks, reinstating the CR challenge even for state-of-the-art VLMs.