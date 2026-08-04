---
title: "A Touch, Vision, and Language Dataset for Multimodal Alignment"
source: "https://proceedings.mlr.press/v235/fu24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fu24b/fu24b.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'generative-models-and-variational-inference']
tags: ['tactile-sensing', 'multimodal-alignment', 'vision-language']
venue: "ICML 2024"
tldr: "A touch-vision-language dataset is introduced to enable multimodal alignment between tactile, visual, and textual modalities."
---

# A Touch, Vision, and Language Dataset for Multimodal Alignment

**Source**: [https://proceedings.mlr.press/v235/fu24b.html](https://proceedings.mlr.press/v235/fu24b.html)

**TLDR**: A touch-vision-language dataset is introduced to enable multimodal alignment between tactile, visual, and textual modalities.

## Abstract

Touch is an important sensing modality for humans, but it has not yet been incorporated into a multimodal generative language model. This is partially due to the difficulty of obtaining natural language labels for tactile data and the complexity of aligning tactile readings with both visual observations and language descriptions. As a step towards bridging that gap, this work introduces a new dataset of 44K in-the-wild visiontouch pairs, with English language labels annotated by humans (10%) and textual pseudo-labels from GPT-4V (90%). We use this dataset to train a vision-language-aligned tactile encoder for open-vocabulary classification and a touch-visionlanguage (TVL) model for text generation using the trained encoder. Results suggest that by incorporating touch, the TVL model improves (+29% classification accuracy) tactile-vision-language alignment over existing models trained on any pair of those modalities. Although only a small fraction of the dataset is human labeled, the TVL model demonstrates improved visual-tactile understanding over GPT-4V (+12%) and open-source vision-language models (+32%) on a new touch-vision understanding benchmark. Code, checkpoints and data are available on https: //tactile-vlm.github.io.