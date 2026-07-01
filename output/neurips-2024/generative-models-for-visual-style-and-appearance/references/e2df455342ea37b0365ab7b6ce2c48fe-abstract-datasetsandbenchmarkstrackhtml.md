---
title: "GS-Blur: A 3D Scene-Based Dataset for Realistic Image Deblurring"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e2df455342ea37b0365ab7b6ce2c48fe-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['generative-models-for-visual-style-and-appearance', 'computational-imaging-reconstruction-deep-learning']
tags: ['image-deblurring', '3D-scene-synthesis', 'dataset-generation']
venue: "NeurIPS 2024"
tldr: "GS-Blur is a novel 3D scene-based dataset for realistic image deblurring that generates paired blurry and sharp images using 3D Gaussian splatting to overcome limitations of existing synthetic and real-blur datasets."
---

# GS-Blur: A 3D Scene-Based Dataset for Realistic Image Deblurring

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e2df455342ea37b0365ab7b6ce2c48fe-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/e2df455342ea37b0365ab7b6ce2c48fe-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: GS-Blur is a novel 3D scene-based dataset for realistic image deblurring that generates paired blurry and sharp images using 3D Gaussian splatting to overcome limitations of existing synthetic and real-blur datasets.

## Abstract

To train a deblurring network, an appropriate dataset with paired blurry and sharp images is essential.Existing datasets collect blurry images either synthetically by aggregating consecutive sharp frames or using sophisticated camera systems to capture real blur.However, these methods offer limited diversity in blur types (blur trajectories) or require extensive human effort to reconstruct large-scale datasets, failing to fully reflect real-world blur scenarios.To address this, we propose GS-Blur, a dataset of synthesized realistic blurry images created using a novel approach.To this end, we first reconstruct 3D scenes from multi-view images using 3D Gaussian Splatting~(3DGS), then render blurry images by moving the camera view along the randomly generated motion trajectories.By adopting various camera trajectories in reconstructing our GS-Blur, our dataset contains realistic and diverse types of blur, offering a large-scale dataset that generalizes well to real-world blur.Using GS-Blur with various deblurring methods, we demonstrate its ability to generalize effectively compared to previous synthetic or real blur datasets, showing significant improvements in deblurring performance.We will publicly release our dataset.