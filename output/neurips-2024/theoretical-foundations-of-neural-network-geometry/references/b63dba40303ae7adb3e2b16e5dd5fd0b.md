---
title: "Geometry of naturalistic object representations in recurrent neural network models of working memory"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/b63dba40303ae7adb3e2b16e5dd5fd0b-Abstract-Conference.html"
categories: ['recurrent-and-spiking-neural-network-dynamics', 'theoretical-foundations-of-neural-network-geometry']
tags: ['working-memory', 'recurrent-neural-networks', 'naturalistic-inputs', 'geometry', 'cognitive-modeling']
venue: "NeurIPS 2024"
tldr: "Investigates the geometry of naturalistic object representations in RNN models of working memory using ecologically-relevant stimuli."
---

# Geometry of naturalistic object representations in recurrent neural network models of working memory

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/b63dba40303ae7adb3e2b16e5dd5fd0b-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/b63dba40303ae7adb3e2b16e5dd5fd0b-Abstract-Conference.html)

**TLDR**: Investigates the geometry of naturalistic object representations in RNN models of working memory using ecologically-relevant stimuli.

## Abstract

Working memory is a central cognitive ability crucial for intelligent decision-making. Recent experimental and computational work studying working memory has primarily used categorical (i.e., one-hot) inputs, rather than ecologically-relevant, multidimensional naturalistic ones. Moreover, studies have primarily investigated working memory during single or few number of cognitive tasks. As a result, an understanding of how naturalistic object information is maintained in working memory in neural networks is still lacking. To bridge this gap, we developed sensory-cognitive models, comprising of a convolutional neural network (CNN) coupled with a recurrent neural network (RNN), and trained them on nine distinct N-back tasks using naturalistic stimuli. By examining the RNN’s latent space, we found that: 1) Multi-task RNNs represent both task-relevant and irrelevant information simultaneously while performing tasks; 2) While the latent subspaces used to maintain specific object properties in vanilla RNNs are largely shared across tasks, they are highly task-specific in gated RNNs such as GRU and LSTM; 3) Surprisingly, RNNs embed objects in new representational spaces in which individual object features are less orthogonalized relative to the perceptual space; 4) Interestingly, the transformation of WM encodings (i.e., embedding of visual inputs in the RNN latent space) into memory was shared across stimuli, yet the transformations governing the retention of a memory in the face of incoming distractor stimuli were distinct across time. Our findings indicate that goal-driven RNNs employ chronological memory subspaces to track information over short time spans, enabling testable predictions with neural data.