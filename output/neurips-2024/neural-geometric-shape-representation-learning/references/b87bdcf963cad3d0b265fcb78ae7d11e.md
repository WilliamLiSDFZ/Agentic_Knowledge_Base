---
title: "Learning to Decouple the Lights for 3D Face Texture Modeling"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/b87bdcf963cad3d0b265fcb78ae7d11e-Abstract-Conference.html"
categories: ['generative-models-for-visual-style-and-appearance', 'neural-geometric-shape-representation-learning']
tags: ['3D-face-reconstruction', 'texture-modeling', 'illumination-disentanglement']
venue: "NeurIPS 2024"
tldr: "A method to disentangle lighting from facial texture for accurate 3D face texture modeling under complex illumination conditions."
---

# Learning to Decouple the Lights for 3D Face Texture Modeling

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/b87bdcf963cad3d0b265fcb78ae7d11e-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/b87bdcf963cad3d0b265fcb78ae7d11e-Abstract-Conference.html)

**TLDR**: A method to disentangle lighting from facial texture for accurate 3D face texture modeling under complex illumination conditions.

## Abstract

Existing research has made impressive strides in reconstructing human facial shapes and textures from images with well-illuminated faces and minimal external occlusions. Nevertheless, it remains challenging to recover accurate facial textures from scenarios with complicated illumination affected by external occlusions, \eg a face that is partially obscured by items such as a hat. Existing works based on the assumption of single and uniform illumination cannot correctly process these data.In this work, we introduce a novel approach to model 3D facial textures under such unnatural illumination. Instead of assuming single illumination, our framework learns to imitate the unnatural illumination as a composition of multiple separate light conditions combined with learned neural representations, named Light Decoupling.According to experiments on both single images and video sequences, we demonstrate the effectiveness of our approach in modeling facial textures under challenging illumination affected by occlusions.