---
title: "Multi-modal Situated Reasoning in 3D Scenes"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/feaeec8ec2d3cb131fe18517ff14ec1f-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'multi-view-clustering-and-3d-perception']
tags: ['3D-scene-reasoning', 'situated-awareness', 'multimodal-benchmark']
venue: "NeurIPS 2024"
tldr: "Proposes Multi-modal Situated Reasoning, a large-scale benchmark for 3D scene understanding with diverse modalities and situated reasoning tasks."
---

# Multi-modal Situated Reasoning in 3D Scenes

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/feaeec8ec2d3cb131fe18517ff14ec1f-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/feaeec8ec2d3cb131fe18517ff14ec1f-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Proposes Multi-modal Situated Reasoning, a large-scale benchmark for 3D scene understanding with diverse modalities and situated reasoning tasks.

## Abstract

Situation awareness is essential for understanding and reasoning about 3D scenes in embodied AI agents. However, existing datasets and benchmarks for situated understanding suffer from severe limitations in data modality, scope, diversity, and scale. To address these limitations, we propose Multi-modal Situated Question Answering (MSQA), a large-scale multi-modal situated reasoning dataset, scalably collected leveraging 3D scene graphs and vision-language models (VLMs) across a diverse range of real-world 3D scenes. MSQA includes 251K situated questionanswering pairs across 9 distinct question categories, covering complex scenarios and object modalities within 3D scenes. We introduce a novel interleaved multimodal input setting in our benchmark to provide both texts, images, and point clouds for situation and question description, aiming to resolve ambiguity in describing situations with single-modality inputs (e.g., texts). Additionally, we devise the Multi-modal Next-step Navigation (MSNN) benchmark to evaluate models’ grounding of actions and transitions between situations. Comprehensive evaluations on reasoning and navigation tasks highlight the limitations of existing vision-language models and underscore the importance of handling multi-modal interleaved inputs and situation modeling. Experiments on data scaling and crossdomain transfer further demonstrate the effectiveness of leveraging MSQA as a pre-training dataset for developing more powerful situated reasoning models, contributing to advancements in 3D scene understanding for embodied AI.