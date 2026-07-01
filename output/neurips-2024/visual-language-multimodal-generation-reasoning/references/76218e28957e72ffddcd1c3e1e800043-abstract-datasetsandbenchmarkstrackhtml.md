---
title: "Map It Anywhere: Empowering BEV Map Prediction using Large-scale Public Datasets"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/76218e28957e72ffddcd1c3e1e800043-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['autonomous-driving-and-trajectory-prediction', 'visual-language-multimodal-generation-reasoning']
tags: ['BEV-map-prediction', 'autonomous-navigation', 'large-scale-datasets']
venue: "NeurIPS 2024"
tldr: "Proposes Map It Anywhere, a framework leveraging large-scale public datasets to improve generalizable Bird's Eye View map prediction for robot navigation."
---

# Map It Anywhere: Empowering BEV Map Prediction using Large-scale Public Datasets

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/76218e28957e72ffddcd1c3e1e800043-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/76218e28957e72ffddcd1c3e1e800043-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Proposes Map It Anywhere, a framework leveraging large-scale public datasets to improve generalizable Bird's Eye View map prediction for robot navigation.

## Abstract

Top-down Bird's Eye View (BEV) maps are a popular perception representation for ground robot navigation due to their richness and flexibility for downstream tasks. While recent methods have shown promise for predicting BEV maps from First-Person View (FPV) images, their generalizability is limited to small regions captured by current autonomous vehicle-based datasets. In this context, we show that a more scalable approach towards generalizable map prediction can be enabled by using two large-scale crowd-sourced mapping platforms, Mapillary for FPV images and OpenStreetMap for BEV semantic maps.We introduce Map It Anywhere (MIA), a data engine that enables seamless curation and modeling of labeled map prediction data from existing open-source map platforms. Using our MIA data engine, we display the ease of automatically collecting a 1.2 million FPV & BEV pair dataset encompassing diverse geographies, landscapes, environmental factors, camera models & capture scenarios. We further train a simple camera model-agnostic model on this data for BEV map prediction.Extensive evaluations using established benchmarks and our dataset show that the data curated by MIA enables effective pretraining for generalizable BEV map prediction, with zero-shot performance far exceeding baselines trained on existing datasets by 35%. Our analysis highlights the promise of using large-scale public maps for developing & testing generalizable BEV perception, paving the way for more robust autonomous navigation.Website: mapitanywhere.github.io