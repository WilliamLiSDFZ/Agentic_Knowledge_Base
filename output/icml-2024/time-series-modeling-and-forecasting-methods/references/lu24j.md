---
title: "NeWRF: A Deep Learning Framework for Wireless Radiation Field Reconstruction and Channel Prediction"
source: "https://proceedings.mlr.press/v235/lu24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lu24j/lu24j.pdf"
categories: ['neural-operators-for-pde-solving', 'time-series-modeling-and-forecasting-methods']
tags: ['wireless-channel-prediction', 'NeRF', 'deep-learning', 'radiation-field', 'channel-modeling']
venue: "ICML 2024"
tldr: "Presents NeWRF, a NeRF-inspired deep learning framework for wireless radiation field reconstruction and channel prediction."
---

# NeWRF: A Deep Learning Framework for Wireless Radiation Field Reconstruction and Channel Prediction

**Source**: [https://proceedings.mlr.press/v235/lu24j.html](https://proceedings.mlr.press/v235/lu24j.html)

**TLDR**: Presents NeWRF, a NeRF-inspired deep learning framework for wireless radiation field reconstruction and channel prediction.

## Abstract

We present NeWRF, a novel deep-learning-based framework for predicting wireless channels. Wireless channel prediction is a long-standing problem in the wireless community and is a key technology for improving the coverage of wireless network deployments. Today, a wireless deployment is evaluated by a site survey which is a cumbersome process requiring an experienced engineer to perform extensive channel measurements. To reduce the cost of site surveys, we develop NeWRF, which is based on recent advances in Neural Radiance Fields (NeRF). NeWRF trains a neural network model with a sparse set of channel measurements, and predicts the wireless channel accurately at any location in the site. We introduce a series of techniques that integrate wireless propagation properties into the NeRF framework to account for the fundamental differences between the behavior of light and wireless signals. We conduct extensive evaluations of our framework and show that our approach can accurately predict channels at unvisited locations with significantly lower measurement density than prior state-of-the-art.