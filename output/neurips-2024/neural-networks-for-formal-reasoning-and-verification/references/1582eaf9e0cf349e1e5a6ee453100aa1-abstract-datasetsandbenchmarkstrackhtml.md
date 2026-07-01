---
title: "PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1582eaf9e0cf349e1e5a6ee453100aa1-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['neural-networks-for-formal-reasoning-and-verification', 'ai-benchmarking-and-evaluation-methodology']
tags: ['neural-theorem-proving', 'competition-mathematics', 'formal-verification']
venue: "NeurIPS 2024"
tldr: "Introduces PutnamBench, a multi-language benchmark of 1692 formalizations from Putnam competition problems for evaluating neural theorem-provers."
---

# PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1582eaf9e0cf349e1e5a6ee453100aa1-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/1582eaf9e0cf349e1e5a6ee453100aa1-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces PutnamBench, a multi-language benchmark of 1692 formalizations from Putnam competition problems for evaluating neural theorem-provers.

## Abstract

We present PutnamBench, a new multi-language benchmark for evaluating the ability of neural theorem-provers to solve competition mathematics problems. PutnamBench consists of 1692 hand-constructed formalizations of 640 theorems sourced from the William Lowell Putnam Mathematical Competition, the premier undergraduate-level mathematics competition in North America. All the problems have formalizations in Lean 4 and Isabelle; a substantial subset also has Coq formalizations. PutnamBench requires significant problem-solving ability and proficiency in a broad range of topics taught in undergraduate mathematics courses. We use PutnamBench to evaluate several established neural and symbolic theorem-provers. These approaches can only solve a handful of the PutnamBench problems, establishing the benchmark as a difficult open challenge for research on neural theorem-proving. PutnamBench is available at https://github.com/trishullab/PutnamBench.