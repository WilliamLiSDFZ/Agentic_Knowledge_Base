---
title: "Finite Volume Features, Global Geometry Representations, and Residual Training for Deep Learning-based CFD Simulation"
source: "https://proceedings.mlr.press/v235/jessica24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jessica24a/jessica24a.pdf"
categories: ['neural-operators-for-pde-solving', 'graph-neural-networks-and-topology']
tags: ['CFD-simulation', 'graph-neural-networks', 'finite-volume', 'deep-learning', 'fluid-dynamics']
venue: "ICML 2024"
tldr: "This paper introduces finite volume features and global geometry representations with residual training to improve GNN-based deep learning CFD simulations."
---

# Finite Volume Features, Global Geometry Representations, and Residual Training for Deep Learning-based CFD Simulation

**Source**: [https://proceedings.mlr.press/v235/jessica24a.html](https://proceedings.mlr.press/v235/jessica24a.html)

**TLDR**: This paper introduces finite volume features and global geometry representations with residual training to improve GNN-based deep learning CFD simulations.

## Abstract

Computational fluid dynamics (CFD) simulation is an irreplaceable modelling step in many engineering designs, but it is often computationally expensive. Some graph neural network (GNN)-based CFD methods have been proposed. However, the current methods inherit the weakness of traditional numerical simulators, as well as ignore the cell characteristics in the mesh used in the finite volume method, a common method in practical CFD applications. Specifically, the input nodes in these GNN methods have very limited information about any object immersed in the simulation domain and its surrounding environment. Also, the cell characteristics of the mesh such as cell volume, face surface area, and face centroid are not included in the message-passing operations in the GNN methods. To address these weaknesses, this work proposes two novel geometric representations: Shortest Vector (SV) and Directional Integrated Distance (DID). Extracted from the mesh, the SV and DID provide global geometry perspective to each input node, thus removing the need to collect this information through message-passing. This work also introduces the use of Finite Volume Features (FVF) in the graph convolutions as node and edge attributes, enabling its message-passing operations to adjust to different nodes. Finally, this work is the first to demonstrate how residual training, with the availability of low-resolution data, can be adopted to improve the flow field prediction accuracy. Experimental results on two datasets with five different state-of-the-art GNN methods for CFD indicate that SV, DID, FVF and residual training can effectively reduce the predictive error of current GNN-based methods by as much as 41%. Our codes and datasets are available at https://github.com/toggled/FvFGeo.