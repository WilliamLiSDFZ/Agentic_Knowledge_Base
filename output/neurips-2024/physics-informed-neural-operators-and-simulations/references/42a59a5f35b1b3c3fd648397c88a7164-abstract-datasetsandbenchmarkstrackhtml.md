---
title: "WindsorML: High-Fidelity Computational Fluid Dynamics Dataset For Automotive Aerodynamics"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/42a59a5f35b1b3c3fd648397c88a7164-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['physics-informed-neural-operators-and-simulations']
tags: ['CFD', 'automotive-aerodynamics', 'ML-dataset']
venue: "NeurIPS 2024"
tldr: "Presents WindsorML, a high-fidelity CFD dataset of 355 Windsor body variants for developing ML surrogate models in automotive aerodynamics."
---

# WindsorML: High-Fidelity Computational Fluid Dynamics Dataset For Automotive Aerodynamics

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/42a59a5f35b1b3c3fd648397c88a7164-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/42a59a5f35b1b3c3fd648397c88a7164-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents WindsorML, a high-fidelity CFD dataset of 355 Windsor body variants for developing ML surrogate models in automotive aerodynamics.

## Abstract

This paper presents a new open-source high-fidelity dataset for Machine Learning (ML) containing 355 geometric variants of the Windsor body, to help the development and testing of ML surrogate models for external automotive aerodynamics. Each Computational Fluid Dynamics (CFD) simulation was run with a GPU-native high-fidelity Wall-Modeled Large-Eddy Simulations (WMLES) using a Cartesian immersed-boundary method using more than 280M cells to ensure the greatest possible accuracy. The dataset contains geometry variants that exhibits a wide range of flow characteristics that are representative of those observed on road-cars. The dataset itself contains the 3D time-averaged volume &amp; boundary data as well as the geometry and force &amp; moment coefficients. This paper discusses the validation of the underlying CFD methods as well as contents and structure of the dataset. To the authors knowledge, this represents the first, large-scale high-fidelity CFD dataset for the Windsor body with a permissive open-source license (CC-BY-SA).