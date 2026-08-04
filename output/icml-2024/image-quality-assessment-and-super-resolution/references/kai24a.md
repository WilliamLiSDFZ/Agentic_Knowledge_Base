---
title: "EvTexture: Event-driven Texture Enhancement for Video Super-Resolution"
source: "https://proceedings.mlr.press/v235/kai24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kai24a/kai24a.pdf"
categories: ['image-quality-assessment-and-super-resolution', 'time-series-modeling-and-forecasting-methods']
tags: ['event-camera', 'video-super-resolution', 'texture-enhancement', 'temporal']
venue: "ICML 2024"
tldr: "Proposes EvTexture, an event-driven method for texture enhancement in video super-resolution leveraging high-temporal-resolution event data."
---

# EvTexture: Event-driven Texture Enhancement for Video Super-Resolution

**Source**: [https://proceedings.mlr.press/v235/kai24a.html](https://proceedings.mlr.press/v235/kai24a.html)

**TLDR**: Proposes EvTexture, an event-driven method for texture enhancement in video super-resolution leveraging high-temporal-resolution event data.

## Abstract

Event-based vision has drawn increasing attention due to its unique characteristics, such as high temporal resolution and high dynamic range. It has been used in video super-resolution (VSR) recently to enhance the flow estimation and temporal alignment. Rather than for motion learning, we propose in this paper the first VSR method that utilizes event signals for texture enhancement. Our method, called EvTexture, leverages high-frequency details of events to better recover texture regions in VSR. In our EvTexture, a new texture enhancement branch is presented. We further introduce an iterative texture enhancement module to progressively explore the high-temporal-resolution event information for texture restoration. This allows for gradual refinement of texture regions across multiple iterations, leading to more accurate and rich high-resolution details. Experimental results show that our EvTexture achieves state-of-the-art performance on four datasets. For the Vid4 dataset with rich textures, our method can get up to 4.67dB gain compared with recent event-based methods. Code: https://github.com/DachunKai/EvTexture.