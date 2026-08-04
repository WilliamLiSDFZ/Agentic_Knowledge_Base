---
title: "S3O: A Dual-Phase Approach for Reconstructing Dynamic Shape and Skeleton of Articulated Objects from Single Monocular Video"
source: "https://proceedings.mlr.press/v235/zhang24ae.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24ae/zhang24ae.pdf"
categories: ['3d-vision-and-scene-understanding', 'generative-models-and-variational-inference']
tags: ['articulated-object-reconstruction', 'monocular-video', 'skeleton-estimation']
venue: "ICML 2024"
tldr: "A dual-phase method for reconstructing dynamic shape and skeleton of articulated objects from a single monocular video."
---

# S3O: A Dual-Phase Approach for Reconstructing Dynamic Shape and Skeleton of Articulated Objects from Single Monocular Video

**Source**: [https://proceedings.mlr.press/v235/zhang24ae.html](https://proceedings.mlr.press/v235/zhang24ae.html)

**TLDR**: A dual-phase method for reconstructing dynamic shape and skeleton of articulated objects from a single monocular video.

## Abstract

Reconstructing dynamic articulated objects from a singular monocular video is challenging, requiring joint estimation of shape, motion, and camera parameters from limited views. Current methods typically demand extensive computational resources and training time, and require additional human annotations such as predefined parametric models, camera poses, and key points, limiting their generalizability. We propose Synergistic Shape and Skeleton Optimization (S3O), a novel two-phase method that forgoes these prerequisites and efficiently learns parametric models including visible shapes and underlying skeletons. Conventional strategies typically learn all parameters simultaneously, leading to interdependencies where a single incorrect prediction can result in significant errors. In contrast, S3O adopts a phased approach: it first focuses on learning coarse parametric models, then progresses to motion learning and detail addition. This method substantially lowers computational complexity and enhances robustness in reconstruction from limited viewpoints, all without requiring additional annotations. To address the current inadequacies in 3D reconstruction from monocular video benchmarks, we collected the PlanetZoo dataset. Our experimental evaluations on standard benchmarks and the PlanetZoo dataset affirm that S3O provides more accurate 3D reconstruction, and plausible skeletons, and reduces the training time by approximately 60% compared to the state-of-the-art, thus advancing the state of the art in dynamic object reconstruction.