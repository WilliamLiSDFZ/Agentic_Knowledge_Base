---
title: "MmCows: A Multimodal Dataset for Dairy Cattle Monitoring"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/6d8f3f71b22f9d2e9320d7bdb73acea7-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['wearable-biosignal-gesture-activity-benchmarks']
tags: ['multimodal-dataset', 'livestock-monitoring', 'precision-agriculture', 'sensor-fusion']
venue: "NeurIPS 2024"
tldr: "Presents MmCows, a multimodal dataset combining multiple sensing modalities for machine learning-driven dairy cattle monitoring."
---

# MmCows: A Multimodal Dataset for Dairy Cattle Monitoring

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/6d8f3f71b22f9d2e9320d7bdb73acea7-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/6d8f3f71b22f9d2e9320d7bdb73acea7-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents MmCows, a multimodal dataset combining multiple sensing modalities for machine learning-driven dairy cattle monitoring.

## Abstract

Precision livestock farming (PLF) has been transformed by machine learning (ML), enabling more precise and timely interventions that enhance overall farm productivity, animal welfare, and environmental sustainability. However, despite the availability of various sensing technologies, few datasets leverage multiple modalities, which are crucial for developing more accurate and efficient monitoring devices and ML models. To address this gap, we present MmCows, a multimodal dataset for dairy cattle monitoring. This dataset comprises a large amount of synchronized, high-quality measurement data on behavioral, physiological, and environmental factors. It includes two weeks of data collected using wearable and implantable sensors deployed on ten milking Holstein cows, such as ultra-wideband (UWB) sensors, inertial sensors, and body temperature sensors. In addition, it features 4.8 million frames of high-resolution image sequences from four isometric view cameras, as well as temperature and humidity data from environmental sensors. We also gathered milk yield data and outdoor weather conditions. One full day’s worth of image data is annotated as ground truth, totaling 20,000 frames with 213,000 bounding boxes of 16 cows, along with their 3D locations and behavior labels. An extensive analysis of MmCows is provided to evaluate the modalities individually and their complementary benefits. The release of MmCows and its benchmarks will facilitate research on multimodal monitoring of dairy cattle, thereby promoting sustainable dairy farming. The dataset and the code for benchmarks are available at https://github.com/neis-lab/mmcows.