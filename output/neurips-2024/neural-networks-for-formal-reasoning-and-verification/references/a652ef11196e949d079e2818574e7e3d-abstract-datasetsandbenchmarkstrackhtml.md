---
title: "NN4SysBench: Characterizing Neural Network Verification for Computer Systems"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a652ef11196e949d079e2818574e7e3d-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['neural-networks-for-formal-reasoning-and-verification', 'ai-benchmarking-and-evaluation-methodology']
tags: ['neural-network-verification', 'computer-systems', 'benchmark']
venue: "NeurIPS 2024"
tldr: "Presents NN4SysBench, a benchmark suite for neural network verification composed of real neural network applications from the computer systems domain."
---

# NN4SysBench: Characterizing Neural Network Verification for Computer Systems

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a652ef11196e949d079e2818574e7e3d-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/a652ef11196e949d079e2818574e7e3d-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents NN4SysBench, a benchmark suite for neural network verification composed of real neural network applications from the computer systems domain.

## Abstract

We present NN4SysBench, a benchmark suite for neural network verification that is composed of applications from the domain of computer systems. We call these neural networks for computer systems or NN4Sys. NN4Sys is booming: there are many proposals for using neural networks in computer systems—for example, databases, OSes, and networked systems—many of which are safety critical. Neural network verification is a technique to formally verify whether neural networks satisfy safety properties. We however observe that NN4Sys has some unique characteristics that today’s verification tools overlook and have limited support. Therefore, this benchmark suite aims at bridging the gap between NN4Sys and the verification by using impactful NN4Sys applications as benchmarks to illustrate computer systems’ unique challenges. We also build a compatible version of NN4SysBench, so that today’s verifiers can also work on these benchmarks with approximately the same verification difficulties. The code is available at https://github.com/lydialin1212/NN4Sys_Benchmark.