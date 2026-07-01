---
title: "Job-SDF: A Multi-Granularity Dataset for Job Skill Demand Forecasting and Benchmarking"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e997325c6f4045aa646c81e674076297-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['time-series-forecasting-and-analysis', 'ai-benchmarking-and-evaluation-methodology']
tags: ['skill-demand-forecasting', 'job-market', 'benchmark-dataset', 'time-series', 'labor-economics']
venue: "NeurIPS 2024"
tldr: "Job-SDF is a multi-granularity benchmark dataset for forecasting and evaluating job skill demand in dynamic labor markets."
---

# Job-SDF: A Multi-Granularity Dataset for Job Skill Demand Forecasting and Benchmarking

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e997325c6f4045aa646c81e674076297-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/e997325c6f4045aa646c81e674076297-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Job-SDF is a multi-granularity benchmark dataset for forecasting and evaluating job skill demand in dynamic labor markets.

## Abstract

In a rapidly evolving job market, skill demand forecasting is crucial as it enables policymakers and businesses to anticipate and adapt to changes, ensuring that workforce skills align with market needs, thereby enhancing productivity and competitiveness. Additionally, by identifying emerging skill requirements, it directs individuals towards relevant training and education opportunities, promoting continuous self-learning and development. However, the absence of comprehensive datasets presents a significant challenge, impeding research and the advancement of this field. To bridge this gap, we present Job-SDF, a dataset designed to train and benchmark job-skill demand forecasting models. Based on millions of public job advertisements collected from online recruitment platforms, this dataset encompasses monthly recruitment demand.Our dataset uniquely enables evaluating skill demand forecasting models at various granularities, including occupation, company, and regional levels. We benchmark a range of models on this dataset, evaluating their performance in standard scenarios, in predictions focused on lower value ranges, and in the presence of structural breaks, providing new insights for further research. Our code and dataset are publicly accessible via the https://github.com/Job-SDF/benchmark.