---
title: "CLIP in Mirror: Disentangling text from visual images through reflection"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/2bda52aca6d214904eceffbce50f2e8c-Abstract-Conference.html"
categories: ['visual-language-multimodal-generation-reasoning']
tags: ['clip', 'text-visual-disentanglement', 'zero-shot']
venue: "NeurIPS 2024"
tldr: "MirrorCLIP is a zero-shot framework that disentangles textual and visual representations in CLIP for images containing both text and visual objects."
---

# CLIP in Mirror: Disentangling text from visual images through reflection

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/2bda52aca6d214904eceffbce50f2e8c-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/2bda52aca6d214904eceffbce50f2e8c-Abstract-Conference.html)

**TLDR**: MirrorCLIP is a zero-shot framework that disentangles textual and visual representations in CLIP for images containing both text and visual objects.

## Abstract

The CLIP network excels in various tasks, but struggles with text-visual images i.e., images that contain both text and visual objects; it risks confusing textual and visual representations. To address this issue, we propose MirrorCLIP, a zero-shot framework, which disentangles the image features of CLIP by exploiting the difference in the mirror effect between visual objects and text in the images. Specifically, MirrorCLIP takes both original and flipped images as inputs, comparing their features dimension-wise in the latent space to generate disentangling masks. With disentangling masks, we further design filters to separate textual and visual factors more precisely, and then get disentangled representations. Qualitative experiments using stable diffusion models and class activation mapping (CAM) validate the effectiveness of our disentanglement. Moreover, our proposed MirrorCLIP reduces confusion when encountering text-visual images and achieves a substantial improvement on typographic defense, further demonstrating its superior ability of disentanglement. Our code is available at https://github.com/tcwangbuaa/MirrorCLIP