---
title: "Learning to Predict Mutational Effects of Protein-Protein Interactions by Microenvironment-aware Hierarchical Prompt Learning"
source: "https://proceedings.mlr.press/v235/wu24y.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24y/wu24y.pdf"
categories: ['generative-models-for-molecular-protein-design', 'knowledge-distillation-methods-and-applications']
tags: ['protein-protein-interaction', 'mutation-effects', 'hierarchical-prompting', 'microenvironment', 'pre-training']
venue: "ICML 2024"
tldr: "Proposes microenvironment-aware hierarchical prompt learning to predict mutational effects on protein-protein binding using pre-training with unlabeled data."
---

# Learning to Predict Mutational Effects of Protein-Protein Interactions by Microenvironment-aware Hierarchical Prompt Learning

**Source**: [https://proceedings.mlr.press/v235/wu24y.html](https://proceedings.mlr.press/v235/wu24y.html)

**TLDR**: Proposes microenvironment-aware hierarchical prompt learning to predict mutational effects on protein-protein binding using pre-training with unlabeled data.

## Abstract

Protein-protein bindings play a key role in a variety of fundamental biological processes, and thus predicting the effects of amino acid mutations on protein-protein binding is crucial. To tackle the scarcity of annotated mutation data, pre-training with massive unlabeled data has emerged as a promising solution. However, this process faces a series of challenges: (1) complex higher-order dependencies among multiple (more than paired) structural scales have not yet been fully captured; (2) it is rarely explored how mutations alter the local conformation of the surrounding microenvironment; (3) pre-training is costly, both in data size and computational burden. In this paper, we first construct a hierarchical prompt codebook to record common microenvironmental patterns at different structural scales independently. Then, we develop a novel codebook pre-training task, namely masked microenvironment modeling, to model the joint distribution of each mutation with their residue types, angular statistics, and local conformational changes in the microenvironment. With the constructed prompt codebook, we encode the microenvironment around each mutation into multiple hierarchical prompts and combine them to flexibly provide information to wild-type and mutated protein complexes about their microenvironmental differences. Such a hierarchical prompt learning framework has demonstrated superior performance and training efficiency over state-of-the-art pre-training-based methods in mutation effect prediction and a case study of optimizing human antibodies against SARS-CoV-2.