---
title: "Optimization Algorithm Design via Electric Circuits"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/7db2ffcbfd0bd361d47b7fa612bd2ba2-Abstract-Conference.html"
categories: ['deep-learning-optimization-and-generalization-theory']
tags: ['convex-optimization', 'RLC-circuits', 'algorithm-design']
venue: "NeurIPS 2024"
tldr: "Presents a methodology for designing convex optimization algorithms inspired by the continuous-time dynamics of electric RLC circuits."
---

# Optimization Algorithm Design via Electric Circuits

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/7db2ffcbfd0bd361d47b7fa612bd2ba2-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/7db2ffcbfd0bd361d47b7fa612bd2ba2-Abstract-Conference.html)

**TLDR**: Presents a methodology for designing convex optimization algorithms inspired by the continuous-time dynamics of electric RLC circuits.

## Abstract

We present a novel methodology for convex optimization algorithm design using ideas from electric RLC circuits. Given an optimization problem, the first stage of the methodology is to design an appropriate electric circuit whose continuous-time dynamics converge to the solution of the optimization problem at hand. Then, the second stage is an automated, computer-assisted discretization of the continuous-time dynamics, yielding a provably convergent discrete-time algorithm. Our methodology recovers many classical (distributed) optimization algorithms and enables users to quickly design and explore a wide range of new algorithms with convergence guarantees.