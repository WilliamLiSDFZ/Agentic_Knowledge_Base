---
title: "ProgressGym: Alignment with a Millennium of Moral Progress"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1a6d49c1a298ebb799d005b7b90ab31d-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-alignment-and-social-choice-aggregation', 'llm-values-ethics-alignment-evaluation']
tags: ['ai-alignment', 'moral-progress', 'rlhf', 'epistemology', 'value-lock-in']
venue: "NeurIPS 2024"
tldr: "ProgressGym introduces a benchmark for aligning AI systems with evolving human moral values across a millennium of historical moral progress."
---

# ProgressGym: Alignment with a Millennium of Moral Progress

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1a6d49c1a298ebb799d005b7b90ab31d-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/1a6d49c1a298ebb799d005b7b90ab31d-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: ProgressGym introduces a benchmark for aligning AI systems with evolving human moral values across a millennium of historical moral progress.

## Abstract

Frontier AI systems, including large language models (LLMs), hold increasing influence over the epistemology of human users. Such influence can reinforce prevailing societal values, potentially contributing to the lock-in of misguided moral beliefs and, consequently, the perpetuation of problematic moral practices on a broad scale. We introduce progress alignment as a technical solution to mitigate this imminent risk. Progress alignment algorithms learn to emulate the mechanics of human moral progress, thereby addressing the susceptibility of existing alignment methods to contemporary moral blindspots. To empower research in progress alignment, we introduce ProgressGym, an experimental framework allowing the learning of moral progress mechanics from history, in order to facilitate future progress in real-world moral decisions. Leveraging 9 centuries of historical text and 18 historical LLMs, ProgressGym enables codification of real-world progress alignment challenges into concrete benchmarks. Specifically, we introduce three core challenges: tracking evolving values (PG-Follow), preemptively anticipating moral progress (PG-Predict), and regulating the feedback loop between human and AI value shifts (PG-Coevolve). Alignment methods without a temporal dimension are inapplicable to these tasks. In response, we present lifelong and extrapolative algorithms as baseline methods of progress alignment, and build an open leaderboard soliciting novel algorithms and challenges.