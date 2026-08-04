---
title: "See More Details: Efficient Image Super-Resolution by Experts Mining"
source: "https://proceedings.mlr.press/v235/zamfir24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zamfir24a/zamfir24a.pdf"
categories: ['image-quality-assessment-and-super-resolution', 'transformer-architecture-efficiency-and-scaling']
tags: ['image-super-resolution', 'mixture-of-experts', 'efficient-architecture']
venue: "ICML 2024"
tldr: "An efficient image super-resolution method using expert mining to selectively apply specialized operations for high-quality HR reconstruction."
---

# See More Details: Efficient Image Super-Resolution by Experts Mining

**Source**: [https://proceedings.mlr.press/v235/zamfir24a.html](https://proceedings.mlr.press/v235/zamfir24a.html)

**TLDR**: An efficient image super-resolution method using expert mining to selectively apply specialized operations for high-quality HR reconstruction.

## Abstract

Reconstructing high-resolution (HR) images from low-resolution (LR) inputs poses a significant challenge in image super-resolution (SR). While recent approaches have demonstrated the efficacy of intricate operations customized for various objectives, the straightforward stacking of these disparate operations can result in a substantial computational burden, hampering their practical utility. In response, we introduce SeemoRe, an efficient SR model employing expert mining. Our approach strategically incorporates experts at different levels, adopting a collaborative methodology. At the macro scale, our experts address rank-wise and spatial-wise informative features, providing a holistic understanding. Subsequently, the model delves into the subtleties of rank choice by leveraging a mixture of low-rank experts. By tapping into experts specialized in distinct key factors crucial for accurate SR, our model excels in uncovering intricate intra-feature details. This collaborative approach is reminiscent of the concept of “see more", allowing our model to achieve an optimal performance with minimal computational costs in efficient settings.