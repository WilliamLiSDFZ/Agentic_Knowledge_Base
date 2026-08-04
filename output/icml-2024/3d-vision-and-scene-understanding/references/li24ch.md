---
title: "GeoReasoner: Geo-localization with Reasoning in Street Views using a Large Vision-Language Model"
source: "https://proceedings.mlr.press/v235/li24ch.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24ch/li24ch.pdf"
categories: ['3d-vision-and-scene-understanding']
tags: ['geo-localization', 'vision-language-model', 'street-view']
venue: "ICML 2024"
tldr: "GeoReasoner leverages a large vision-language model augmented with human inference knowledge for street-view geo-localization."
---

# GeoReasoner: Geo-localization with Reasoning in Street Views using a Large Vision-Language Model

**Source**: [https://proceedings.mlr.press/v235/li24ch.html](https://proceedings.mlr.press/v235/li24ch.html)

**TLDR**: GeoReasoner leverages a large vision-language model augmented with human inference knowledge for street-view geo-localization.

## Abstract

This work tackles the problem of geo-localization with a new paradigm using a large vision-language model (LVLM) augmented with human inference knowledge. A primary challenge here is the scarcity of data for training the LVLM - existing street-view datasets often contain numerous low-quality images lacking visual clues, and lack any reasoning inference. To address the data-quality issue, we devise a CLIP-based network to quantify the degree of street-view images being locatable, leading to the creation of a new dataset comprising highly locatable street views. To enhance reasoning inference, we integrate external knowledge obtained from real geo-localization games, tapping into valuable human inference capabilities. The data are utilized to train GeoReasoner, which undergoes fine-tuning through dedicated reasoning and location-tuning stages. Qualitative and quantitative evaluations illustrate that GeoReasoner outperforms counterpart LVLMs by more than 25% at country-level and 38% at city-level geo-localization tasks, and surpasses StreetCLIP performance while requiring fewer training resources. The data and code are available at https://github.com/lingli1996/GeoReasoner.