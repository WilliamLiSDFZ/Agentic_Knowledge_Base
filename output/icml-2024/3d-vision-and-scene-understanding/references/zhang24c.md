---
title: "SAM-E: Leveraging Visual Foundation Model with Sequence Imitation for Embodied Manipulation"
source: "https://proceedings.mlr.press/v235/zhang24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24c/zhang24c.pdf"
categories: ['simulation-scaling-limits-for-robot-manipulation', '3d-vision-and-scene-understanding']
tags: ['imitation-learning', '3D-manipulation', 'foundation-models']
venue: "ICML 2024"
tldr: "SAM-E leverages visual foundation models with sequence imitation for efficient multi-task 3D robot manipulation."
---

# SAM-E: Leveraging Visual Foundation Model with Sequence Imitation for Embodied Manipulation

**Source**: [https://proceedings.mlr.press/v235/zhang24c.html](https://proceedings.mlr.press/v235/zhang24c.html)

**TLDR**: SAM-E leverages visual foundation models with sequence imitation for efficient multi-task 3D robot manipulation.

## Abstract

Acquiring a multi-task imitation policy in 3D manipulation poses challenges in terms of scene understanding and action prediction. Current methods employ both 3D representation and multi-view 2D representation to predict the poses of the robot’s end-effector. However, they still require a considerable amount of high-quality robot trajectories, and suffer from limited generalization in unseen tasks and inefficient execution in long-horizon reasoning. In this paper, we propose SAM-E, a novel architecture for robot manipulation by leveraging a vision-foundation model for generalizable scene understanding and sequence imitation for long-term action reasoning. Specifically, we adopt Segment Anything (SAM) pre-trained on a huge number of images and promptable masks as the foundation model for extracting task-relevant features, and employ parameter-efficient fine-tuning on robot data for a better understanding of embodied scenarios. To address long-horizon reasoning, we develop a novel multi-channel heatmap that enables the prediction of the action sequence in a single pass, notably enhancing execution efficiency. Experimental results from various instruction-following tasks demonstrate that SAM-E achieves superior performance with higher execution efficiency compared to the baselines, and also significantly improves generalization in few-shot adaptation to new tasks.