---
title: "Visual Representation Learning with Stochastic Frame Prediction"
source: "https://proceedings.mlr.press/v235/jang24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jang24c/jang24c.pdf"
categories: ['generative-models-and-variational-inference', 'test-time-adaptation-methods-and-evaluation']
tags: ['self-supervised-learning', 'video-prediction', 'stochastic-frame-prediction', 'visual-representation', 'uncertainty']
venue: "ICML 2024"
tldr: "A self-supervised visual representation learning framework uses stochastic future frame prediction to handle the multi-modal uncertainty of video."
---

# Visual Representation Learning with Stochastic Frame Prediction

**Source**: [https://proceedings.mlr.press/v235/jang24c.html](https://proceedings.mlr.press/v235/jang24c.html)

**TLDR**: A self-supervised visual representation learning framework uses stochastic future frame prediction to handle the multi-modal uncertainty of video.

## Abstract

Self-supervised learning of image representations by predicting future frames is a promising direction but still remains a challenge. This is because of the under-determined nature of frame prediction; multiple potential futures can arise from a single current frame. To tackle this challenge, in this paper, we revisit the idea of stochastic video generation that learns to capture uncertainty in frame prediction and explore its effectiveness for representation learning. Specifically, we design a framework that trains a stochastic frame prediction model to learn temporal information between frames. Moreover, to learn dense information within each frame, we introduce an auxiliary masked image modeling objective along with a shared decoder architecture. We find this architecture allows for combining both objectives in a synergistic and compute-efficient manner. We demonstrate the effectiveness of our framework on a variety of tasks from video label propagation and vision-based robot learning domains, such as video segmentation, pose tracking, vision-based robotic locomotion, and manipulation tasks. Code is available on the project webpage: https://sites.google.com/view/2024rsp.