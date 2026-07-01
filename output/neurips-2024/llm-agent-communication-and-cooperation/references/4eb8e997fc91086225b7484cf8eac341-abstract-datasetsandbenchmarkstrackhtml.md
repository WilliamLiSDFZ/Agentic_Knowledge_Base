---
title: "Constrained Human-AI Cooperation: An Inclusive Embodied Social Intelligence Challenge"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/4eb8e997fc91086225b7484cf8eac341-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'llm-agent-communication-and-cooperation']
tags: ['embodied-agents', 'human-ai-cooperation', 'social-intelligence']
venue: "NeurIPS 2024"
tldr: "CHAIC is a benchmark challenge for testing social perception and constrained cooperation between embodied AI agents and humans with physical limitations."
---

# Constrained Human-AI Cooperation: An Inclusive Embodied Social Intelligence Challenge

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/4eb8e997fc91086225b7484cf8eac341-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/4eb8e997fc91086225b7484cf8eac341-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: CHAIC is a benchmark challenge for testing social perception and constrained cooperation between embodied AI agents and humans with physical limitations.

## Abstract

We introduce Constrained Human-AI Cooperation (CHAIC), an inclusive embodied social intelligence challenge designed to test social perception and cooperation in embodied agents. In CHAIC, the goal is for an embodied agent equipped with egocentric observations to assist a human who may be operating under physical constraints—e.g., unable to reach high places or confined to a wheelchair—in performing common household or outdoor tasks as efficiently as possible. To achieve this, a successful helper must: (1) infer the human's intents and constraints by following the human and observing their behaviors (social perception), and (2) make a cooperative plan tailored to the human partner to solve the task as quickly as possible, working together as a team (cooperative planning). To benchmark this challenge, we create four new agents with real physical constraints and eight long-horizon tasks featuring both indoor and outdoor scenes with various constraints, emergency events, and potential risks. We benchmark planning- and learning-based baselines on the challenge and introduce a new method that leverages large language models and behavior modeling. Empirical evaluations demonstrate the effectiveness of our benchmark in enabling systematic assessment of key aspects of machine social intelligence. Our benchmark and code are publicly available at https://github.com/UMass-Foundation-Model/CHAIC.