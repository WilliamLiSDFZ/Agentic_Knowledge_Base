---
title: "MMScan: A Multi-Modal 3D Scene Dataset with Hierarchical Grounded Language Annotations"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/5aed0d900297bd5593afc14ff452d4a8-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'multi-view-clustering-and-3d-perception']
tags: ['3d-scene-understanding', 'multimodal-dataset', 'grounded-language']
venue: "NeurIPS 2024"
tldr: "Presents MMScan, a multi-modal 3D scene dataset with hierarchical grounded language annotations for advancing 3D perception with LLMs."
---

# MMScan: A Multi-Modal 3D Scene Dataset with Hierarchical Grounded Language Annotations

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/5aed0d900297bd5593afc14ff452d4a8-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/5aed0d900297bd5593afc14ff452d4a8-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents MMScan, a multi-modal 3D scene dataset with hierarchical grounded language annotations for advancing 3D perception with LLMs.

## Abstract

With the emergence of LLMs and their integration with other data modalities, multi-modal 3D perception attracts more attention due to its connectivity to the physical world and makes rapid progress. However, limited by existing datasets, previous works mainly focus on understanding object properties or inter-object spatial relationships in a 3D scene. To tackle this problem, this paper builds the first largest ever multi-modal 3D scene dataset and benchmark with hierarchical grounded language annotations, MMScan. It is constructed based on a top-down logic, from region to object level, from a single target to inter-target relationships, covering holistic aspects of spatial and attribute understanding. The overall pipeline incorporates powerful VLMs via carefully designed prompts to initialize the annotations efficiently and further involve humans' correction in the loop to ensure the annotations are natural, correct, and comprehensive. Built upon existing 3D scanning data, the resulting multi-modal 3D dataset encompasses 1.4M meta-annotated captions on 109k objects and 7.7k regions as well as over 3.04M diverse samples for 3D visual grounding and question-answering benchmarks. We evaluate representative baselines on our benchmarks, analyze their capabilities in different aspects, and showcase the key problems to be addressed in the future. Furthermore, we use this high-quality dataset to train state-of-the-art 3D visual grounding and LLMs and obtain remarkable performance improvement both on existing benchmarks and in-the-wild evaluation.