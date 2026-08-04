---
title: "Online Speculative Decoding"
source: "https://proceedings.mlr.press/v235/liu24y.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24y/liu24y.pdf"
categories: ['llm-serving-systems-and-infrastructure']
tags: ['speculative-decoding', 'LLM-inference', 'online-learning']
venue: "ICML 2024"
tldr: "Online speculative decoding dynamically updates the draft model to improve predictive accuracy and accelerate LLM inference in distribution-shifting settings."
---

# Online Speculative Decoding

**Source**: [https://proceedings.mlr.press/v235/liu24y.html](https://proceedings.mlr.press/v235/liu24y.html)

**TLDR**: Online speculative decoding dynamically updates the draft model to improve predictive accuracy and accelerate LLM inference in distribution-shifting settings.

## Abstract

Speculative decoding is a pivotal technique to accelerate the inference of large language models (LLMs) by employing a smaller draft model to predict the target model’s outputs. However, its efficacy can be limited due to the low predictive accuracy of the draft model, particularly when faced with diverse text inputs and a significant capability gap between the draft and target models. We introduce online speculative decoding to address this challenge. The main idea is to continuously update the (multiple) draft model(s) on observed user query data. Adapting to query distribution mitigates the shifts between the training distribution of the draft model and the query distribution, enabling the draft model to more accurately predict the target model’s outputs. We develop a prototype of online speculative decoding based on knowledge distillation and evaluate it using both synthetic and real query data. The results show a substantial increase in the token acceptance rate by 0.1 to 0.65, bringing 1.42x to 2.17x latency reduction. Our code is available at https://github.com/LiuXiaoxuanPKU/OSD.