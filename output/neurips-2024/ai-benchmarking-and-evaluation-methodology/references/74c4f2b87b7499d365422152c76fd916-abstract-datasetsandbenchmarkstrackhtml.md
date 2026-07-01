---
title: "SurgicAI: A Hierarchical Platform for Fine-Grained Surgical Policy Learning and Benchmarking"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/74c4f2b87b7499d365422152c76fd916-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['surgical-robotics', 'reinforcement-learning', 'hierarchical-benchmarking']
venue: "NeurIPS 2024"
tldr: "Presents SurgicAI, a hierarchical simulation platform for fine-grained surgical policy learning and benchmarking using reinforcement and imitation learning."
---

# SurgicAI: A Hierarchical Platform for Fine-Grained Surgical Policy Learning and Benchmarking

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/74c4f2b87b7499d365422152c76fd916-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/74c4f2b87b7499d365422152c76fd916-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents SurgicAI, a hierarchical simulation platform for fine-grained surgical policy learning and benchmarking using reinforcement and imitation learning.

## Abstract

Despite advancements in robotic-assisted surgery, automating complex tasks like suturing remains challenging due to the need for adaptability and precision. Learning-based approaches, particularly reinforcement learning (RL) and imitation learning (IL), require realistic simulation environments for efficient data collection. However, current platforms often include only relatively simple, non-dexterous manipulations and lack the flexibility required for effective learning and generalization. We introduce SurgicAI, a novel platform for development and benchmarking that addresses these challenges by providing the flexibility to accommodate both modular subtasks and more importantly task decomposition in RL-based surgical robotics. Compatible with the da Vinci Surgical System, SurgicAI offers a standardized pipeline for collecting and utilizing expert demonstrations. It supports the deployment of multiple RL and IL approaches, and the training of both singular and compositional subtasks in suturing scenarios, featuring high dexterity and modularization. Meanwhile, SurgicAI sets clear metrics and benchmarks for the assessment of learned policies. We implemented and evaluated multiple RL and IL algorithms on SurgicAI. Our detailed benchmark analysis underscores SurgicAI's potential to advance policy learning in surgical robotics. Details: https://github.com/surgical-robotics-ai/SurgicAI