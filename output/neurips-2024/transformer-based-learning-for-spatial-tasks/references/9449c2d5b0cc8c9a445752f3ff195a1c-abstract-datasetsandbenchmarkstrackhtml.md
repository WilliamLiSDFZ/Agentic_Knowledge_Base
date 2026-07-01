---
title: "TorchSpatial: A Location Encoding Framework and Benchmark for Spatial Representation Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/9449c2d5b0cc8c9a445752f3ff195a1c-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['transformer-based-learning-for-spatial-tasks', 'ai-benchmarking-and-evaluation-methodology']
tags: ['spatial-representation-learning', 'location-encoding', 'benchmark']
venue: "NeurIPS 2024"
tldr: "TorchSpatial provides a unified framework and benchmark for evaluating spatial representation learning across diverse spatial data types."
---

# TorchSpatial: A Location Encoding Framework and Benchmark for Spatial Representation Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/9449c2d5b0cc8c9a445752f3ff195a1c-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/9449c2d5b0cc8c9a445752f3ff195a1c-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: TorchSpatial provides a unified framework and benchmark for evaluating spatial representation learning across diverse spatial data types.

## Abstract

Spatial representation learning (SRL) aims at learning general-purpose neural network representations from various types of spatial data (e.g., points, polylines, polygons, networks, images, etc.) in their native formats. Learning good spatial representations is a fundamental problem for various downstream applications such as species distribution modeling, weather forecasting, trajectory generation, geographic question answering, etc. Even though SRL has become the foundation of almost all geospatial artificial intelligence (GeoAI) research, we have not yet seen significant efforts to develop an extensive deep learning framework and benchmark to support SRL model development and evaluation. To fill this gap, we propose TorchSpatial, a learning framework and benchmark for location (point) encoding,which is one of the most fundamental data types of spatial representation learning. TorchSpatial contains three key components: 1) a unified location encoding framework that consolidates 15 commonly recognized location encoders, ensuring scalability and reproducibility of the implementations; 2) the LocBench benchmark tasks encompassing 7 geo-aware image classification and 10 geo-aware imageregression datasets; 3) a comprehensive suite of evaluation metrics to quantify geo-aware models’ overall performance as well as their geographic bias, with a novel Geo-Bias Score metric. Finally, we provide a detailed analysis and insights into the model performance and geographic bias of different location encoders. We believe TorchSpatial will foster future advancement of spatial representationlearning and spatial fairness in GeoAI research. The TorchSpatial model framework and LocBench benchmark are available at https://github.com/seai-lab/TorchSpatial, and the Geo-Bias Score evaluation framework is available at https://github.com/seai-lab/PyGBS.