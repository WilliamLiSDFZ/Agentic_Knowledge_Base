---
title: "WildPPG: A Real-World PPG Dataset of Long Continuous Recordings"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/0433292a3eb101df8f4d72a63f5410d4-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['wearable-biosignal-gesture-activity-benchmarks', 'time-series-forecasting-and-analysis']
tags: ['photoplethysmography', 'wearable-sensing', 'heart-rate-dataset']
venue: "NeurIPS 2024"
tldr: "WildPPG is a real-world long-duration PPG dataset captured from wearables under diverse activity conditions to benchmark heart rate estimation."
---

# WildPPG: A Real-World PPG Dataset of Long Continuous Recordings

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/0433292a3eb101df8f4d72a63f5410d4-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/0433292a3eb101df8f4d72a63f5410d4-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: WildPPG is a real-world long-duration PPG dataset captured from wearables under diverse activity conditions to benchmark heart rate estimation.

## Abstract

Reflective photoplethysmography (PPG) has become the default sensing technique in wearable devices to monitor cardiac activity via a person’s heart rate (HR). However, PPG-based HR estimates can be substantially impacted by factors such as the wearer’s activities, sensor placement and resulting motion artifacts, as well as environmental characteristics such as temperature and ambient light. These and other factors can significantly impact and decrease HR prediction reliability. In this paper, we show that state-of-the-art HR estimation methods struggle when processing representative data from everyday activities in outdoor environments, likely because they rely on existing datasets that captured controlled conditions. We introduce a novel multimodal dataset and benchmark results for continuous PPG recordings during outdoor activities from 16 participants over 13.5 hours, captured from four wearable sensors, each worn at a different location on the body, totaling 216 hours. Our recordings include accelerometer, temperature, and altitude data, as well as a synchronized Lead I-based electrocardiogram for ground-truth HR references. Participants completed a round trip from Zurich to Jungfraujoch, a tall mountain in Switzerland over the course of one day. The trip included outdoor and indoor activities such as walking, hiking, stair climbing, eating, drinking, and resting at various temperatures and altitudes (up to 3,571 m above sea level) as well as using cars, trains, cable cars, and lifts for transport—all of which impacted participants’ physiological dynamics. We also present a novel method that estimates HR values more robustly in such real-world scenarios than existing baselines.Dataset & code for HR estimation: https://siplab.org/projects/WildPPG