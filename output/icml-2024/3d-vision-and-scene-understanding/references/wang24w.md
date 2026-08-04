---
title: "EvGGS: A Collaborative Learning Framework for Event-based Generalizable Gaussian Splatting"
source: "https://proceedings.mlr.press/v235/wang24w.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24w/wang24w.pdf"
categories: ['3d-vision-and-scene-understanding', 'generative-models-and-variational-inference']
tags: ['event-cameras', 'gaussian-splatting', '3D-reconstruction', 'collaborative-learning', 'novel-view-synthesis']
venue: "ICML 2024"
tldr: "EvGGS is a collaborative learning framework for generalizable 3D Gaussian splatting from sparse event camera streams."
---

# EvGGS: A Collaborative Learning Framework for Event-based Generalizable Gaussian Splatting

**Source**: [https://proceedings.mlr.press/v235/wang24w.html](https://proceedings.mlr.press/v235/wang24w.html)

**TLDR**: EvGGS is a collaborative learning framework for generalizable 3D Gaussian splatting from sparse event camera streams.

## Abstract

Event cameras offer promising advantages such as high dynamic range and low latency, making them well-suited for challenging lighting conditions and fast-moving scenarios. However, reconstructing 3D scenes from raw event streams is difficult because event data is sparse and does not carry absolute color information. To release its potential in 3D reconstruction, we propose the first event-based generalizable 3D reconstruction framework, which reconstructs scenes as 3D Gaussians from only event input in a feedforward manner and can generalize to unseen cases without any retraining. This framework includes a depth estimation module, an intensity reconstruction module, and a Gaussian regression module. These submodules connect in a cascading manner, and we collaboratively train them with a designed joint loss to make them mutually promote. To facilitate related studies, we build a novel event-based 3D dataset with various material objects and calibrated labels of greyscale images, depth maps, camera poses, and silhouettes. Experiments show models that have jointly trained significantly outperform those trained individually. Our approach performs better than all baselines in reconstruction quality, and depth/intensity predictions with satisfactory rendering speed.