---
title: "AuctionNet: A Novel Benchmark for Decision-Making in Large-Scale Games"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/ab9b7c23edfea0011507f7e1eae82cd2-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'ai-benchmarking-and-evaluation-methodology']
tags: ['benchmark', 'large-scale-games', 'decision-making']
venue: "NeurIPS 2024"
tldr: "Presents AuctionNet, a realistic large-scale auction game benchmark for advancing AI research in decision-making under competitive multi-agent settings."
---

# AuctionNet: A Novel Benchmark for Decision-Making in Large-Scale Games

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/ab9b7c23edfea0011507f7e1eae82cd2-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/ab9b7c23edfea0011507f7e1eae82cd2-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents AuctionNet, a realistic large-scale auction game benchmark for advancing AI research in decision-making under competitive multi-agent settings.

## Abstract

Decision-making in large-scale games is an essential research area in artificial intelligence (AI) with significant real-world impact. However, the limited access to realistic large-scale game environments has hindered research progress in this area. In this paper, we present AuctionNet, a benchmark for bid decision-making in large-scale ad auctions derived from a real-world online advertising platform. AuctionNet is composed of three parts: an ad auction environment, a pre-generated dataset based on the environment, and performance evaluations of several baseline bid decision-making algorithms. More specifically, the environment effectively replicates the integrity and complexity of real-world ad auctions through the interaction of several modules: the ad opportunity generation module employs deep generative networks to bridge the gap between simulated and real-world data while mitigating the risk of sensitive data exposure; the bidding module implements diverse auto-bidding agents trained with different decision-making algorithms; and the auction module is anchored in the classic Generalized Second Price (GSP) auction but also allows for customization of auction mechanisms as needed. To facilitate research and provide insights into the environment, we have also pre-generated a substantial dataset based on the environment. The dataset contains 10 million ad opportunities, 48 diverse auto-bidding agents, and over 500 million auction records. Performance evaluations of baseline algorithms such as linear programming, reinforcement learning, and generative models for bid decision-making are also presented as a part of AuctionNet. AuctionNet has powered the NeurIPS 2024 Auto-Bidding in Large-Scale Auctions competition, providing competition environments for over 1,500 teams. We believe that AuctionNet is applicable not only to research on bid decision-making in ad auctions but also to the general area of decision-making in large-scale games. Code: https://github.com/alimama-tech/AuctionNet.