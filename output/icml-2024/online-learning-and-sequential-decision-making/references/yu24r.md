---
title: "A Unified Adaptive Testing System Enabled by Hierarchical Structure Search"
source: "https://proceedings.mlr.press/v235/yu24r.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yu24r/yu24r.pdf"
categories: ['information-retrieval-and-recommendation-systems', 'online-learning-and-sequential-decision-making']
tags: ['adaptive-testing', 'hierarchical-structure', 'knowledge-assessment']
venue: "ICML 2024"
tldr: "A unified adaptive testing system using hierarchical structure search to provide personalized ability assessment dynamically."
---

# A Unified Adaptive Testing System Enabled by Hierarchical Structure Search

**Source**: [https://proceedings.mlr.press/v235/yu24r.html](https://proceedings.mlr.press/v235/yu24r.html)

**TLDR**: A unified adaptive testing system using hierarchical structure search to provide personalized ability assessment dynamically.

## Abstract

Adaptive Testing System (ATS) is a promising testing mode, extensively utilized in standardized tests like the GRE. It offers personalized ability assessment by dynamically adjusting questions based on individual ability levels. Compared to traditional exams, ATS can improve the accuracy of ability estimates while simultaneously reducing the number of questions required. Despite the diverse testing formats of ATS, tailored to different adaptability requirements in various testing scenarios, there is a notable absence of a unified framework for modeling them. In this paper, we introduce a unified data-driven ATS framework that conceptualizes the various testing formats as a hierarchical test structure search problem. It can learn directly from data to solve for the optimal questions for each student, eliminating the need for manual test design. The proposed solution algorithm comes with theoretical guarantees for estimation error and convergence. Empirical results show that our framework maintains assessment accuracy while reducing question count by 20% on average and improving training stability.