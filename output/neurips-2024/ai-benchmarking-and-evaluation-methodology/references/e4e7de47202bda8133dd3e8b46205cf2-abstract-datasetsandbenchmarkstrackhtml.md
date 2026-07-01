---
title: "GeoPlant: Spatial Plant Species Prediction Dataset"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e4e7de47202bda8133dd3e8b46205cf2-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'graph-neural-networks-and-representation-learning']
tags: ['species-distribution-models', 'spatial-prediction', 'biodiversity-monitoring']
venue: "NeurIPS 2024"
tldr: "GeoPlant introduces a large-scale spatial dataset for predicting plant species distributions using spatially explicit environmental features."
---

# GeoPlant: Spatial Plant Species Prediction Dataset

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e4e7de47202bda8133dd3e8b46205cf2-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/e4e7de47202bda8133dd3e8b46205cf2-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: GeoPlant introduces a large-scale spatial dataset for predicting plant species distributions using spatially explicit environmental features.

## Abstract

The difficulty of monitoring biodiversity at fine scales and over large areas limits ecological knowledge and conservation efforts. To fill this gap, Species Distribution Models (SDMs) predict species across space from spatially explicit features. Yet, they face the challenge of integrating the rich but heterogeneous data made available over the past decade, notably millions of opportunistic species observations and standardized surveys, as well as multi-modal remote sensing data.In light of that, we have designed and developed a new European-scale dataset for SDMs at high spatial resolution (10--50m), including more than 10k species (i.e., most of the European flora). The dataset comprises 5M heterogeneous Presence-Only records and 90k exhaustive Presence-Absence survey records, all accompanied by diverse environmental rasters (e.g., elevation, human footprint, and soil) traditionally used in SDMs. In addition, it provides Sentinel-2 RGB and NIR satellite images with 10 m resolution, a 20-year time series of climatic variables, and satellite time series from the Landsat program.In addition to the data, we provide an openly accessible SDM benchmark (hosted on Kaggle), which has already attracted an active community and a set of strong baselines for single predictor/modality and multimodal approaches.All resources, e.g., the dataset, pre-trained models, and baseline methods (in the form of notebooks), are available on Kaggle, allowing one to start with our dataset literally with two mouse clicks.