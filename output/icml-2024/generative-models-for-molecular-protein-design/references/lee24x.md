---
title: "Robust Optimization in Protein Fitness Landscapes Using Reinforcement Learning in Latent Space"
source: "https://proceedings.mlr.press/v235/lee24x.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24x/lee24x.pdf"
categories: ['generative-models-for-molecular-protein-design', 'online-learning-and-sequential-decision-making']
tags: ['protein-optimization', 'reinforcement-learning', 'latent-space', 'fitness-landscape']
venue: "ICML 2024"
tldr: "Uses reinforcement learning in a latent space to robustly optimize protein fitness landscapes starting from low-fitness sequences."
---

# Robust Optimization in Protein Fitness Landscapes Using Reinforcement Learning in Latent Space

**Source**: [https://proceedings.mlr.press/v235/lee24x.html](https://proceedings.mlr.press/v235/lee24x.html)

**TLDR**: Uses reinforcement learning in a latent space to robustly optimize protein fitness landscapes starting from low-fitness sequences.

## Abstract

Proteins are complex molecules responsible for different functions in nature. Enhancing the functionality of proteins and cellular fitness can significantly impact various industries. However, protein optimization using computational methods remains challenging, especially when starting from low-fitness sequences. We propose LatProtRL, an optimization method to efficiently traverse a latent space learned by an encoder-decoder leveraging a large protein language model. To escape local optima, our optimization is modeled as a Markov decision process using reinforcement learning acting directly in latent space. We evaluate our approach on two important fitness optimization tasks, demonstrating its ability to achieve comparable or superior fitness over baseline methods. Our findings and in vitro evaluation show that the generated sequences can reach high-fitness regions, suggesting a substantial potential of LatProtRL in lab-in-the-loop scenarios.