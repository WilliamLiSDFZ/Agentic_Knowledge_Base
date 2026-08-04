---
title: "Mol-AE: Auto-Encoder Based Molecular Representation Learning With 3D Cloze Test Objective"
source: "https://proceedings.mlr.press/v235/yang24al.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24al/yang24al.pdf"
categories: ['generative-models-for-molecular-protein-design']
tags: ['molecular-representation', '3D-molecules', 'auto-encoder', 'cloze-test']
venue: "ICML 2024"
tldr: "An auto-encoder framework with a 3D cloze test objective is proposed for improved molecular representation learning over encoder-only denoising approaches."
---

# Mol-AE: Auto-Encoder Based Molecular Representation Learning With 3D Cloze Test Objective

**Source**: [https://proceedings.mlr.press/v235/yang24al.html](https://proceedings.mlr.press/v235/yang24al.html)

**TLDR**: An auto-encoder framework with a 3D cloze test objective is proposed for improved molecular representation learning over encoder-only denoising approaches.

## Abstract

3D molecular representation learning has gained tremendous interest and achieved promising performance in various downstream tasks. A series of recent approaches follow a prevalent framework: an encoder-only model coupled with a coordinate denoising objective. However, through a series of analytical experiments, we prove that the encoder-only model with coordinate denoising objective exhibits inconsistency between pre-training and downstream objectives, as well as issues with disrupted atomic identifiers. To address these two issues, we propose Mol-AE for molecular representation learning, an auto-encoder model using positional encoding as atomic identifiers. We also propose a new training objective named 3D Cloze Test to make the model learn better atom spatial relationships from real molecular substructures. Empirical results demonstrate that Mol-AE achieves a large margin performance gain compared to the current state-of-the-art 3D molecular modeling approach.