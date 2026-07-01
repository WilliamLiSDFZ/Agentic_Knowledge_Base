---
title: "Time-MMD: Multi-Domain Multimodal Dataset for Time Series Analysis"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/8e7768122f3eeec6d77cd2b424b72413-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['time-series-forecasting-and-analysis', 'ai-benchmarking-and-evaluation-methodology']
tags: ['time-series', 'multimodal-dataset', 'multi-domain']
venue: "NeurIPS 2024"
tldr: "Time-MMD introduces a multi-domain multimodal dataset pairing numerical time series with domain-specific knowledge to advance multimodal time series analysis."
---

# Time-MMD: Multi-Domain Multimodal Dataset for Time Series Analysis

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/8e7768122f3eeec6d77cd2b424b72413-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/8e7768122f3eeec6d77cd2b424b72413-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Time-MMD introduces a multi-domain multimodal dataset pairing numerical time series with domain-specific knowledge to advance multimodal time series analysis.

## Abstract

Time series data are ubiquitous across a wide range of real-world domains. Whilereal-world time series analysis (TSA) requires human experts to integrate numerical series data with multimodal domain-specific knowledge, most existing TSAmodels rely solely on numerical data, overlooking the significance of information beyond numerical series. This oversight is due to the untapped potentialof textual series data and the absence of a comprehensive, high-quality multimodal dataset. To overcome this obstacle, we introduce Time-MMD, the firstmulti-domain, multimodal time series dataset covering 9 primary data domains.Time-MMD ensures fine-grained modality alignment, eliminates data contamination, and provides high usability. Additionally, we develop MM-TSFlib, thefirst-cut multimodal time-series forecasting (TSF) library, seamlessly pipeliningmultimodal TSF evaluations based on Time-MMD for in-depth analyses. Extensiveexperiments conducted on Time-MMD through MM-TSFlib demonstrate significant performance enhancements by extending unimodal TSF to multimodality,evidenced by over 15% mean squared error reduction in general, and up to 40%in domains with rich textual data. More importantly, our datasets and libraryrevolutionize broader applications, impacts, research topics to advance TSA. Thedataset is available at https://github.com/AdityaLab/Time-MMD.