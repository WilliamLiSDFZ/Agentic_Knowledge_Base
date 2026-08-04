---
title: "Position: Rethinking Post-Hoc Search-Based Neural Approaches for Solving Large-Scale Traveling Salesman Problems"
source: "https://proceedings.mlr.press/v235/xia24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xia24f/xia24f.pdf"
categories: ['position-papers-on-ml-research-directions', 'neural-symbolic-combinatorial-optimization-learning']
tags: ['TSP', 'heatmap-guided', 'MCTS']
venue: "ICML 2024"
tldr: "A position paper rethinking post-hoc search-based neural approaches for large-scale TSP, questioning the effectiveness of heatmap-guided MCTS paradigms."
---

# Position: Rethinking Post-Hoc Search-Based Neural Approaches for Solving Large-Scale Traveling Salesman Problems

**Source**: [https://proceedings.mlr.press/v235/xia24f.html](https://proceedings.mlr.press/v235/xia24f.html)

**TLDR**: A position paper rethinking post-hoc search-based neural approaches for large-scale TSP, questioning the effectiveness of heatmap-guided MCTS paradigms.

## Abstract

Recent advancements in solving large-scale traveling salesman problems (TSP) utilize the heatmap-guided Monte Carlo tree search (MCTS) paradigm, where machine learning (ML) models generate heatmaps, indicating the probability distribution of each edge being part of the optimal solution, to guide MCTS in solution finding. However, our theoretical and experimental analysis raises doubts about the effectiveness of ML-based heatmap generation. In support of this, we demonstrate that a simple baseline method can outperform complex ML approaches in heatmap generation. Furthermore, we question the practical value of the heatmap-guided MCTS paradigm. To substantiate this, our findings show its inferiority to the LKH-3 heuristic despite the paradigm’s reliance on problem-specific, hand-crafted strategies. For the future, we suggest research directions focused on developing more theoretically sound heatmap generation methods and exploring autonomous, generalizable ML approaches for combinatorial problems. The code is available for review: https://github.com/xyfffff/rethink_mcts_for_tsp.