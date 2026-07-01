---
title: "What to Say and When to Say it: Live Fitness Coaching as a Testbed for Situated Interaction"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/8aa695b5d6bf9e958d4e56b22c9b859d-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'audio-visual-speech-processing-and-benchmarks']
tags: ['vision-language-models', 'situated-interaction', 'fitness-coaching']
venue: "NeurIPS 2024"
tldr: "Live fitness coaching is used as a testbed to study open-ended asynchronous situated interaction in vision-language models."
---

# What to Say and When to Say it: Live Fitness Coaching as a Testbed for Situated Interaction

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/8aa695b5d6bf9e958d4e56b22c9b859d-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/8aa695b5d6bf9e958d4e56b22c9b859d-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Live fitness coaching is used as a testbed to study open-ended asynchronous situated interaction in vision-language models.

## Abstract

Vision-language models have shown impressive progress in recent years. However, existing models are largely limited to turn-based interactions, where each turn must be stepped (i.e., prompted) by the user. Open-ended, asynchronous interactions, where an AI model may proactively deliver timely responses or feedback based on the unfolding situation in real-time, are an open challenge. In this work, we present the QEVD benchmark and dataset, which explores human-AI interaction in the challenging, yet controlled, real-world domain of fitness coaching – a task which intrinsically requires monitoring live user activity and providing immediate feedback. The benchmark requires vision-language models to recognize complex human actions, identify possible mistakes, and provide appropriate feedback in real-time. Our experiments reveal the limitations of existing state-of-the-art vision-language models for such asynchronous situated interactions. Motivated by this, we propose a simple end-to-end streaming baseline that can respond asynchronously to human actions with appropriate feedback at the appropriate time.