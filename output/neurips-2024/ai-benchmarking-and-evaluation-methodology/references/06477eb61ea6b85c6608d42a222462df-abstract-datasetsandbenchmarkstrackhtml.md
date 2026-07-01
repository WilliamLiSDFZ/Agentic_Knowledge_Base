---
title: "SolarCube: An Integrative Benchmark Dataset Harnessing Satellite and In-situ Observations for Large-scale Solar Energy Forecasting"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/06477eb61ea6b85c6608d42a222462df-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['time-series-forecasting-and-analysis', 'ai-benchmarking-and-evaluation-methodology']
tags: ['solar-energy-forecasting', 'benchmark-dataset', 'satellite-observations']
venue: "NeurIPS 2024"
tldr: "SolarCube provides an integrative benchmark dataset combining satellite and in-situ observations for large-scale solar energy forecasting."
---

# SolarCube: An Integrative Benchmark Dataset Harnessing Satellite and In-situ Observations for Large-scale Solar Energy Forecasting

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/06477eb61ea6b85c6608d42a222462df-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/06477eb61ea6b85c6608d42a222462df-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: SolarCube provides an integrative benchmark dataset combining satellite and in-situ observations for large-scale solar energy forecasting.

## Abstract

Solar power is a critical source of renewable energy, offering significant potential to lower greenhouse gas emissions and mitigate climate change. However, the cloud induced-variability of solar radiation reaching the earth’s surface presents a challenge for integrating solar power into the grid (e.g., storage and backup management). The new generation of geostationary satellites such as GOES-16 has become an important data source for large-scale and high temporal frequency solar radiation forecasting. However, no machine-learning-ready dataset has integrated geostationary satellite data with fine-grained solar radiation information to support forecasting model development and benchmarking with consistent metrics. We present SolarCube, a new ML-ready benchmark dataset for solar radiation forecasting. SolarCube covers 19 study areas distributed over multiple continents: North America, South America, Asia, and Oceania. The dataset supports short (i.e., 30 minutes to 6 hours) and long-term (i.e., day-ahead or longer) solar radiation forecasting at both point-level (i.e., specific locations of monitoring stations) and area-level, by processing and integrating data from multiple sources, including geostationary satellite images, physics-derived solar radiation, and ground station observations from different monitoring networks over the globe. We also evaluated a set of forecasting models for point- and image-based time-series data to develop performance benchmarks under different testing scenarios. The dataset is available at https://doi.org/10.5281/zenodo.11498739. A Python library is available to conveniently generate different variations of the dataset based on user needs, along with baseline models at https://github.com/Ruohan-Li/SolarCube.