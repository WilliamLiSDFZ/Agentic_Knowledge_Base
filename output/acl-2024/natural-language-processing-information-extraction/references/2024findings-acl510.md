---
title: "Stronger, Lighter, Better: Towards Life-Long Attribute Value Extraction for E-Commerce Products"
source: "https://aclanthology.org/2024.findings-acl.510/"
pdf_url: ""
categories: ['natural-language-processing-information-extraction', 'continual-learning-for-nlp-tasks']
tags: ['attribute-value-extraction', 'e-commerce', 'continual-learning']
venue: "ACL 2024"
tldr: "A lifelong learning framework for attribute value extraction that adapts to new product categories and attributes in e-commerce."
---

# Stronger, Lighter, Better: Towards Life-Long Attribute Value Extraction for E-Commerce Products

**Source**: [https://aclanthology.org/2024.findings-acl.510/](https://aclanthology.org/2024.findings-acl.510/)

**TLDR**: A lifelong learning framework for attribute value extraction that adapts to new product categories and attributes in e-commerce.

## Abstract

AbstractAttribute value extraction involves identifying the value spans of predetermined attributes in product texts. This area of research has traditionally operated under a closed-world assumption, focusing on products from a static set of categories and their associated attributes. However, products in e-commerce stores are ever-increasing and evolving, calling for life-long learning. If continuously trained on the fast-increasing products and attributes, most existing solutions not only struggle for parameter efficiency but also endure foreseeable defects due to data contamination, catastrophic forgetting, etc. As a remedy, we propose and study a new task, which aims to effectively maintain a strong single model for many domains in a life-long learning fashion, without jeopardizing the model performance and parameter efficiency. We introduce factorization into the model and make it domain-aware by decoupling the modeling of product type and attribute, as a way to promote de-contamination and parameter efficiency while scaling up. Tuning the model with distillation prevents forgetting historical knowledge and enables continuous learning from emerging domains. Experiments on hundreds of domains showed that our model attains the near state-of-the-art performance with affordable parameter size, the least historical knowledge forgetting, and the greatest robustness against noises, whilst adding only a few parameters per domain when compared with competitive baselines.