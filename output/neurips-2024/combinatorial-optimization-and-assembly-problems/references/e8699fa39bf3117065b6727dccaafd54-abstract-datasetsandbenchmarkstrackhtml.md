---
title: "Slice-100K: A Multimodal Dataset for Extrusion-based 3D Printing"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e8699fa39bf3117065b6727dccaafd54-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'combinatorial-optimization-and-assembly-problems']
tags: ['3d-printing', 'gcode', 'multimodal-dataset']
venue: "NeurIPS 2024"
tldr: "Slice-100K is a large multimodal dataset of G-code instructions for extrusion-based 3D printing to support machine learning research."
---

# Slice-100K: A Multimodal Dataset for Extrusion-based 3D Printing

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e8699fa39bf3117065b6727dccaafd54-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/e8699fa39bf3117065b6727dccaafd54-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Slice-100K is a large multimodal dataset of G-code instructions for extrusion-based 3D printing to support machine learning research.

## Abstract

G-code (Geometric code) or RS-274 is the most widely used computer numerical control (CNC) and 3D printing programming language. G-code provides machine instructions for the movement of the 3D printer, especially for the nozzle, stage, and extrusion of material for extrusion-based additive manufacturing. Currently, there does not exist a large repository of curated CAD models along with their corresponding G-code files for additive manufacturing. To address this issue, we present Slice-100K, a first-of-its-kind dataset of over 100,000 G-code files, along with their tessellated CAD model, LVIS (Large Vocabulary Instance Segmentation) categories, geometric properties, and renderings. We build our dataset from triangulated meshes derived from Objaverse-XL and Thingi10K datasets. We demonstrate the utility of this dataset by finetuning GPT-2 on a subset of the dataset for G-code translation from a legacy G-code format (Sailfish) to a more modern, widely used format (Marlin). Our dataset can be found here. Slice-100K will be the first step in developing a multimodal foundation model for digital manufacturing.