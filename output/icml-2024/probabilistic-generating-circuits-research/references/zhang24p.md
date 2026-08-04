---
title: "MILP-FBGen: LP/MILP Instance Generation with Feasibility/Boundedness"
source: "https://proceedings.mlr.press/v235/zhang24p.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24p/zhang24p.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'probabilistic-generating-circuits-research']
tags: ['MILP', 'instance-generation', 'feasibility']
venue: "ICML 2024"
tldr: "A method for generating feasible and bounded LP/MILP instances that closely mirror real data distributions to support machine learning for combinatorial optimization."
---

# MILP-FBGen: LP/MILP Instance Generation with Feasibility/Boundedness

**Source**: [https://proceedings.mlr.press/v235/zhang24p.html](https://proceedings.mlr.press/v235/zhang24p.html)

**TLDR**: A method for generating feasible and bounded LP/MILP instances that closely mirror real data distributions to support machine learning for combinatorial optimization.

## Abstract

Machine learning (ML) has been actively adopted in Linear Programming (LP) and Mixed-Integer Linear Programming (MILP), whose potential is hindered by instance scarcity. Current synthetic instance generation methods often fall short in closely mirroring the distribution of original datasets or ensuring the feasibility and boundedness of the generated data — a critical requirement for obtaining reliable supervised labels in model training. In this paper, we present a diffusion-based LP/MILP instance generative framework called MILP-FBGen. It strikes a balance between structural similarity and novelty while maintaining feasibility/boundedness via a meticulously designed structure-preserving generation module and a feasibility/boundedness-constrained sampling module. Our method shows superiority on two fronts: 1) preservation of key properties (hardness, feasibility, and boundedness) of LP/MILP instances, and 2) enhanced performance on downstream tasks. Extensive studies show two-fold superiority that our method ensures higher distributional similarity and 100% feasibility in both easy and hard datasets, surpassing current state-of-the-art techniques.