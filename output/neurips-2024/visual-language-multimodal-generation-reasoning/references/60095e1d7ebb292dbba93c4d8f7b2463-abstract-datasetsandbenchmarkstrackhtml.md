---
title: "AllClear: A Comprehensive Dataset and Benchmark for Cloud Removal in Satellite Imagery"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/60095e1d7ebb292dbba93c4d8f7b2463-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'visual-language-multimodal-generation-reasoning']
tags: ['cloud-removal', 'satellite-imagery', 'benchmark-dataset']
venue: "NeurIPS 2024"
tldr: "AllClear introduces the largest public dataset and benchmark for cloud removal in satellite imagery to advance remote sensing research."
---

# AllClear: A Comprehensive Dataset and Benchmark for Cloud Removal in Satellite Imagery

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/60095e1d7ebb292dbba93c4d8f7b2463-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/60095e1d7ebb292dbba93c4d8f7b2463-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: AllClear introduces the largest public dataset and benchmark for cloud removal in satellite imagery to advance remote sensing research.

## Abstract

Clouds in satellite imagery pose a significant challenge for downstream applications.A major challenge in current cloud removal research is the absence of a comprehensive benchmark and a sufficiently large and diverse training dataset.To address this problem, we introduce the largest public dataset -- *AllClear* for cloud removal, featuring 23,742 globally distributed regions of interest (ROIs) with diverse land-use patterns, comprising 4 million images in total. Each ROI includes complete temporal captures from the year 2022, with (1) multi-spectral optical imagery from Sentinel-2 and Landsat 8/9, (2) synthetic aperture radar (SAR) imagery from Sentinel-1, and (3) auxiliary remote sensing products such as cloud masks and land cover maps.We validate the effectiveness of our dataset by benchmarking performance, demonstrating the scaling law - the PSNR rises from $28.47$ to $33.87$ with $30\times$ more data, and conducting ablation studies on the temporal length and the importance of individual modalities. This dataset aims to provide comprehensive coverage of the Earth's surface and promote better cloud removal results.