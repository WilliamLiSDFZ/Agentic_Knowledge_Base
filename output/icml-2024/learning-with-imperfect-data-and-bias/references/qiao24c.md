---
title: "ULAREF: A Unified Label Refinement Framework for Learning with Inaccurate Supervision"
source: "https://proceedings.mlr.press/v235/qiao24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/qiao24c/qiao24c.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'data-selection-and-active-learning-methods']
tags: ['weak-supervision', 'label-noise', 'inaccurate-annotations', 'label-refinement', 'unified-framework']
venue: "ICML 2024"
tldr: "A unified label refinement framework that handles multiple forms of inaccurate supervision under a common paradigm."
---

# ULAREF: A Unified Label Refinement Framework for Learning with Inaccurate Supervision

**Source**: [https://proceedings.mlr.press/v235/qiao24c.html](https://proceedings.mlr.press/v235/qiao24c.html)

**TLDR**: A unified label refinement framework that handles multiple forms of inaccurate supervision under a common paradigm.

## Abstract

Learning with inaccurate supervision is often encountered in weakly supervised learning, and researchers have invested a considerable amount of time and effort in designing specialized algorithms for different forms of annotations in inaccurate supervision. In fact, different forms of these annotations share the fundamental characteristic that they all still incorporate some portion of correct labeling information. This commonality can serve as a lever, enabling the creation of a cohesive framework designed to tackle the challenges associated with various forms of annotations in learning with inaccurate supervision. In this paper, we propose a unified label refinement framework named ULAREF, i.e., a Unified LAbel REfinement Framework for learning with inaccurate supervision, which is capable of leveraging label refinement to handle inaccurate supervision. Specifically, our framework trains the predictive model with refined labels through global detection of reliability and local enhancement using an enhanced model fine-tuned by a proposed consistency loss. Also, we theoretically justify that the enhanced model in local enhancement can achieve higher accuracy than the predictive model on the detected unreliable set under mild assumptions.