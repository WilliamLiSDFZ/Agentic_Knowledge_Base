---
title: "FiVA: Fine-grained Visual Attribute Dataset for Text-to-Image Diffusion Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/3870e6fe5fc75307508ee1458e81e27c-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['generative-models-for-visual-style-and-appearance', 'diffusion-based-generative-modeling-and-inference']
tags: ['text-to-image', 'visual-attributes', 'diffusion-models']
venue: "NeurIPS 2024"
tldr: "Introduces FiVA, a fine-grained visual attribute dataset to improve attribute control in text-to-image diffusion models."
---

# FiVA: Fine-grained Visual Attribute Dataset for Text-to-Image Diffusion Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/3870e6fe5fc75307508ee1458e81e27c-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/3870e6fe5fc75307508ee1458e81e27c-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces FiVA, a fine-grained visual attribute dataset to improve attribute control in text-to-image diffusion models.

## Abstract

Recent advances in text-to-image generation have enabled the creation of high-quality images with diverse applications. However, accurately describing desired visual attributes can be challenging, especially for non-experts in art and photography. An intuitive solution involves adopting favorable attributes from source images. Current methods attempt to distill identity and style from source images. However, "style" is a broad concept that includes texture, color, and artistic elements, but does not cover other important attributes like lighting and dynamics. Additionally, a simplified "style" adaptation prevents combining multiple attributes from different sources into one generated image. In this work, we formulate a more effective approach to decompose the aesthetics of a picture into specific visual attributes, letting users apply characteristics like lighting, texture, and dynamics from different images. To achieve this goal, we constructed the first fine-grained visual attributes dataset (FiVA) to the best of our knowledge. This FiVA dataset features a well-organized taxonomy for visual attributes and includes 1 M high-quality generated images with visual attribute annotations. Leveraging this dataset, we propose a fine-grained visual attributes adaptation framework (FiVA-Adapter) , which decouples and adapts visual attributes from one or more source images into a generated one. This approach enhances user-friendly customization, allowing users to selectively apply desired attributes to create images that meet their unique preferences and specific content requirements.