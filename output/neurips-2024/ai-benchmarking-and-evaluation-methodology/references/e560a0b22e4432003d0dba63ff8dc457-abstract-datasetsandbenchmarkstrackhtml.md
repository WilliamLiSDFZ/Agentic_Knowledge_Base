---
title: "MEQA: A Benchmark for Multi-hop Event-centric Question Answering with Explanations"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e560a0b22e4432003d0dba63ff8dc457-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'statistical-inference-and-text-generation-methods\n\nhmm,-let-me-reconsider---looking-more-carefully-at-the-cluster:\n\n**score-matching-and-sampling-methods**']
tags: ['multi-hop-question-answering', 'event-centric-reasoning', 'benchmark']
venue: "NeurIPS 2024"
tldr: "MEQA is a benchmark for multi-hop event-centric question answering that evaluates models on reasoning about both events and entities with explanations."
---

# MEQA: A Benchmark for Multi-hop Event-centric Question Answering with Explanations

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e560a0b22e4432003d0dba63ff8dc457-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/e560a0b22e4432003d0dba63ff8dc457-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: MEQA is a benchmark for multi-hop event-centric question answering that evaluates models on reasoning about both events and entities with explanations.

## Abstract

Existing benchmarks for multi-hop question answering (QA) primarily evaluate models based on their ability to reason about entities and the relationships between them. However, there's a lack of insight into how these models perform in terms of both events and entities. In this paper, we introduce a novel semi-automatic question generation strategy by composing event structures from information extraction (IE) datasets and present the first Multi-hop Event-centric Question Answering (MEQA) benchmark. It contains (1) 2,243 challenging questions that require a diverse range of complex reasoning over entity-entity, entity-event, and event-event relations; (2) corresponding multi-step QA-format event reasoning chain (explanation) which leads to the answer for each question. We also introduce two metrics for evaluating explanations: completeness and logical consistency. We conduct comprehensive benchmarking and analysis, which shows that MEQA is challenging for the latest state-of-the-art models encompassing large language models (LLMs); and how they fall short of providing faithful explanations of the event-centric reasoning process.