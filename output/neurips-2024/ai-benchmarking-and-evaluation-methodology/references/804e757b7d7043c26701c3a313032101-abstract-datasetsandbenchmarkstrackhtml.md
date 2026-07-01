---
title: "VideoGUI: A Benchmark for GUI Automation from Instructional Videos"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/804e757b7d7043c26701c3a313032101-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['gui-automation', 'instructional-videos', 'benchmark']
venue: "NeurIPS 2024"
tldr: "Introduces VideoGUI, a benchmark for evaluating GUI automation agents on complex tasks derived from instructional videos."
---

# VideoGUI: A Benchmark for GUI Automation from Instructional Videos

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/804e757b7d7043c26701c3a313032101-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/804e757b7d7043c26701c3a313032101-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces VideoGUI, a benchmark for evaluating GUI automation agents on complex tasks derived from instructional videos.

## Abstract

Graphical User Interface (GUI) automation holds significant promise for enhancing human productivity by assisting with computer tasks. Existing task formulations primarily focus on simple tasks that can be specified by a single, language-only instruction, such as “Insert a new slide.” In this work, we introduce VideoGUI, a novel multi-modal benchmark designed to evaluate GUI assistants on visual-centric GUI tasks. Sourced from high-quality web instructional videos, our benchmark focuses on tasks involving professional and novel software (e.g., Adobe Pho- toshop or Stable Diffusion WebUI) and complex activities (e.g., video editing). VideoGUI evaluates GUI assistants through a hierarchical process, allowing for identification of the specific levels at which they may fail: (i) high-level planning: reconstruct procedural subtasks from visual conditions without language descrip- tions; (ii) middle-level planning: generate sequences of precise action narrations based on visual state (i.e., screenshot) and goals; (iii) atomic action execution: perform specific actions such as accurately clicking designated elements. For each level, we design evaluation metrics across individual dimensions to provide clear signals, such as individual performance in clicking, dragging, typing, and scrolling for atomic action execution. Our evaluation on VideoGUI reveals that even the SoTA large multimodal model GPT4o performs poorly on visual-centric GUI tasks, especially for high-level planning. The data and code are available at https://github.com/showlab/videogui.