---
title: "Spike Distance Function as a Learning Objective for Spike Prediction"
source: "https://proceedings.mlr.press/v235/doran24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/doran24a/doran24a.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['spiking-neurons', 'spike-prediction', 'learning-objective', 'temporal-coding']
venue: "ICML 2024"
tldr: "A spike distance function is proposed as a learning objective for spike prediction to capture precise spike timing beyond coarse Poisson models."
---

# Spike Distance Function as a Learning Objective for Spike Prediction

**Source**: [https://proceedings.mlr.press/v235/doran24a.html](https://proceedings.mlr.press/v235/doran24a.html)

**TLDR**: A spike distance function is proposed as a learning objective for spike prediction to capture precise spike timing beyond coarse Poisson models.

## Abstract

Approaches to predicting neuronal spike responses commonly use a Poisson learning objective. This objective quantizes responses into spike counts within a fixed summation interval, typically on the order of 10 to 100 milliseconds in duration; however, neuronal responses are often time accurate down to a few milliseconds, and Poisson models struggle to precisely model them at these timescales. We propose the concept of a spike distance function that maps points in time to the temporal distance to the nearest spike. We show that neural networks can be trained to approximate spike distance functions, and we present an efficient algorithm for inferring spike trains from the outputs of these models. Using recordings of chicken and frog retinal ganglion cells responding to visual stimuli, we compare the performance of our approach to that of Poisson models trained with various summation intervals. We show that our approach outperforms the use of Poisson models at spike train inference.