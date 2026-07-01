---
title: "Unraveling Molecular Structure: A Multimodal Spectroscopic Dataset for Chemistry"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e38e60b33bb2c6993e0865160cdb5cf1-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['machine-learning-for-molecular-biology', 'visual-language-multimodal-generation-reasoning']
tags: ['spectroscopic-dataset', 'molecular-structure', 'multimodal-chemistry']
venue: "NeurIPS 2024"
tldr: "A large multimodal spectroscopic dataset combining NMR, IR, and mass spectrometry data is introduced to support machine learning for molecular structure elucidation."
---

# Unraveling Molecular Structure: A Multimodal Spectroscopic Dataset for Chemistry

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e38e60b33bb2c6993e0865160cdb5cf1-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/e38e60b33bb2c6993e0865160cdb5cf1-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A large multimodal spectroscopic dataset combining NMR, IR, and mass spectrometry data is introduced to support machine learning for molecular structure elucidation.

## Abstract

Spectroscopic techniques are essential tools for determining the structure of molecules. Different spectroscopic techniques, such as Nuclear magnetic resonance (NMR), Infrared spectroscopy, and Mass Spectrometry, provide insight into the molecular structure, including the presence or absence of functional groups. Chemists leverage the complementary nature of the different methods to their advantage. However, the lack of a comprehensive multimodal dataset, containing spectra from a variety of spectroscopic techniques, has limited machine-learning approaches mostly to single-modality tasks for predicting molecular structures from spectra. Here we introduce a dataset comprising simulated $^1$H-NMR, $^{13}$C-NMR, HSQC-NMR, Infrared, and Mass spectra (positive and negative ion modes) for 790k molecules extracted from chemical reactions in patent data. This dataset enables the development of foundation models for integrating information from multiple spectroscopic modalities, emulating the approach employed by human experts. Additionally, we provide benchmarks for evaluating single-modality tasks such as structure elucidation, predicting the spectra for a target molecule, and functional group predictions. This dataset has the potential automate structure elucidation, streamlining the molecular discovery pipeline from synthesis to structure determination. The dataset and code for the benchmarks can be found at https://rxn4chemistry.github.io/multimodal-spectroscopic-dataset (Available upon submission of the supporting information).