---
title: "$\nabla^2$DFT: A Universal Quantum Chemistry Dataset of Drug-Like Molecules and a Benchmark for Neural Network Potentials"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/40d45b1e23d00d5895e65778e85cf8ee-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['machine-learning-for-molecular-biology', 'ai-benchmarking-and-evaluation-methodology']
tags: ['quantum-chemistry', 'neural-network-potentials', 'drug-discovery']
venue: "NeurIPS 2024"
tldr: "A large universal quantum chemistry dataset of drug-like molecules is introduced as a benchmark for neural network potentials."
---

# $\nabla^2$DFT: A Universal Quantum Chemistry Dataset of Drug-Like Molecules and a Benchmark for Neural Network Potentials

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/40d45b1e23d00d5895e65778e85cf8ee-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/40d45b1e23d00d5895e65778e85cf8ee-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A large universal quantum chemistry dataset of drug-like molecules is introduced as a benchmark for neural network potentials.

## Abstract

Methods of computational quantum chemistry provide accurate approximations of molecular properties crucial for computer-aided drug discovery and other areas of chemical science. However, high computational complexity limits the scalability of their applications.Neural network potentials (NNPs) are a promising alternative to quantum chemistry methods, but they require large and diverse datasets for training.This work presents a new dataset and benchmark called $\nabla^2$DFT that is based on the nablaDFT.It contains twice as much molecular structures, three times more conformations, new data types and tasks, and state-of-the-art models.The dataset includes energies, forces, 17 molecular properties, Hamiltonian and overlap matrices, and a wavefunction object.All calculations were performed at the DFT level ($\omega$B97X-D/def2-SVP) for each conformation. Moreover, $\nabla^2$DFT is the first dataset that contains relaxation trajectories for a substantial number of drug-like molecules. We also introduce a novel benchmark for evaluating NNPs in molecular property prediction, Hamiltonian prediction, and conformational optimization tasks. Finally, we propose an extendable framework for training NNPs and implement 10 models within it.