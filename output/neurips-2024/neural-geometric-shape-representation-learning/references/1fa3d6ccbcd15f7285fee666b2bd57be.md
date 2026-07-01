---
title: "From an Image to a Scene: Learning to Imagine the World from a Million 360° Videos"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1fa3d6ccbcd15f7285fee666b2bd57be-Abstract-Conference.html"
categories: ['visual-language-multimodal-generation-reasoning', 'neural-geometric-shape-representation-learning']
tags: ['3d-scene-generation', '360-video', 'world-models', 'novel-view-synthesis', 'video-understanding']
venue: "NeurIPS 2024"
tldr: "A model trained on millions of 360° videos learns to generate and imagine 3D scenes from a single image."
---

# From an Image to a Scene: Learning to Imagine the World from a Million 360° Videos

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1fa3d6ccbcd15f7285fee666b2bd57be-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/1fa3d6ccbcd15f7285fee666b2bd57be-Abstract-Conference.html)

**TLDR**: A model trained on millions of 360° videos learns to generate and imagine 3D scenes from a single image.

## Abstract

Three-dimensional (3D) understanding of objects and scenes play a key role in humans' ability to interact with the world and has been an active area of research in computer vision, graphics, and robotics. Large scale synthetic and object-centric 3D datasets have shown to be effective in training models that have 3D understanding of objects. However, applying a similar approach to real-world objects and scenes is difficult due to a lack of large-scale data. Videos are a potential source for real-world 3D data, but finding diverse yet corresponding views of the same content have shown to be difficult at scale. Furthermore, standard videos come with fixed viewpoints, determined at the time of capture. This restricts the ability to access scenes from a variety of more diverse and potentially useful perspectives. We argue that large scale ODIN videos can address these limitations to provide scalable corresponding frames from diverse views.  In this paper we introduce 360-1M, a 360° video dataset consisting of 1 million videos, and a process for efficiently finding corresponding frames from diverse viewpoints at scale. We train our diffusion-based model, ODIN, on 360-1M. Empowered by the largest real-world, multi-view dataset to date, ODIN is able to freely generate novel views of real-world scenes. Unlike previous methods, ODIN can move the camera through the environment, enabling the model to infer the geometry and layout of the scene. Additionally, we show improved performance on standard novel view synthesis and 3D reconstruction benchmarks.