---
title: "CiteME: Can Language Models Accurately Cite Scientific Claims?"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/0ef47f7b768e1a012e3d995ac8d8fac7-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['scientific-document-retrieval-and-citation', 'ai-benchmarking-and-evaluation-methodology']
tags: ['scientific-citation', 'language-models', 'claim-attribution']
venue: "NeurIPS 2024"
tldr: "CiteME benchmarks whether language models can accurately identify and cite the source papers of scientific text excerpts."
---

# CiteME: Can Language Models Accurately Cite Scientific Claims?

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/0ef47f7b768e1a012e3d995ac8d8fac7-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/0ef47f7b768e1a012e3d995ac8d8fac7-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: CiteME benchmarks whether language models can accurately identify and cite the source papers of scientific text excerpts.

## Abstract

Thousands of new scientific papers are published each month. Such  information overload complicates researcher efforts to stay current with the state-of-the-art as well as to verify and correctly attribute claims. We pose the following research question: Given a text excerpt referencing a paper, could an LM act as a research assistant to correctly identify the referenced paper? We advance efforts to answer this question by building a benchmark that evaluates the abilities of LMs in citation attribution. Our benchmark, CiteME, consists  of text excerpts from recent machine learning papers, each referencing a single other paper. CiteME use reveals a large gap between frontier LMs and human performance, with LMs achieving only 4.2-18.5% accuracy and humans 69.7%. We close this gap by introducing CiteAgent, an autonomous system built on the GPT-4o LM that can also search and read papers, which achieves an accuracy of 35.3% on CiteME. Overall, CiteME serves as a challenging testbed for open-ended claim attribution, driving the research community towards a future where any claim made by an LM can be  automatically verified and discarded if found to be incorrect.