---
title: "Estimating Canopy Height at Scale"
source: "https://proceedings.mlr.press/v235/pauls24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pauls24a/pauls24a.pdf"
categories: ['large-scale-canopy-height-estimation', 'neural-operators-for-pde-solving']
tags: ['canopy-height-estimation', 'remote-sensing', 'satellite-data', 'geospatial']
venue: "ICML 2024"
tldr: "Proposes a global-scale canopy height estimation framework using satellite data with novel loss functions to handle geolocation inaccuracies in ground-truth measurements."
---

# Estimating Canopy Height at Scale

**Source**: [https://proceedings.mlr.press/v235/pauls24a.html](https://proceedings.mlr.press/v235/pauls24a.html)

**TLDR**: Proposes a global-scale canopy height estimation framework using satellite data with novel loss functions to handle geolocation inaccuracies in ground-truth measurements.

## Abstract

We propose a framework for global-scale canopy height estimation based on satellite data. Our model leverages advanced data preprocessing techniques, resorts to a novel loss function designed to counter geolocation inaccuracies inherent in the ground-truth height measurements, and employs data from the Shuttle Radar Topography Mission to effectively filter out erroneous labels in mountainous regions, enhancing the reliability of our predictions in those areas. A comparison between predictions and ground-truth labels yields an MAE/RMSE of 2.43 / 4.73 (meters) overall and 4.45 / 6.72 (meters) for trees taller than five meters, which depicts a substantial improvement compared to existing global-scale products. The resulting height map as well as the underlying framework will facilitate and enhance ecological analyses at a global scale, including, but not limited to, large-scale forest and biomass monitoring.