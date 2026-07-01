---
title: "Multi-Label Open Set Recognition"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/0aee38a6fe9fffc8b658cfb1d872c1d5-Abstract-Conference.html"
categories: ['machine-learning-theory-and-evaluation-methods', 'ai-benchmarking-and-evaluation-methodology']
tags: ['multi-label-learning', 'open-set-recognition', 'unknown-classes']
venue: "NeurIPS 2024"
tldr: "A framework extending multi-label learning to open set scenarios where test data may contain classes unseen during training."
---

# Multi-Label Open Set Recognition

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/0aee38a6fe9fffc8b658cfb1d872c1d5-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/0aee38a6fe9fffc8b658cfb1d872c1d5-Abstract-Conference.html)

**TLDR**: A framework extending multi-label learning to open set scenarios where test data may contain classes unseen during training.

## Abstract

In multi-label learning, each training instance is associated with multiple labels simultaneously. Traditional multi-label learning studies primarily focus on closed set scenario, i.e. the class label set of test data is identical to those used in training phase. Nevertheless, in numerous real-world scenarios, the environment is open and dynamic where unknown labels may emerge gradually during testing. In this paper, the problem of multi-label open set recognition (MLOSR) is investigated, which poses significant challenges in classifying and recognizing instances with unknown labels in multi-label setting. To enable open set multi-label prediction, a novel approach named SLAN is proposed by leveraging sub-labeling information enriched by structural information in the feature space. Accordingly, unknown labels are recognized by differentiating the sub-labeling information from holistic supervision. Experimental results on various datasets validate the effectiveness of the proposed approach in dealing with the MLOSR problem.