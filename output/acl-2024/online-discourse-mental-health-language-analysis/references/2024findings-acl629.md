---
title: "Chinese MentalBERT: Domain-Adaptive Pre-training on Social Media for Chinese Mental Health Text Analysis"
source: "https://aclanthology.org/2024.findings-acl.629/"
categories: ['online-discourse-mental-health-language-analysis', 'llms-for-biomedical-and-clinical-nlp']
tags: ['mental-health-nlp', 'domain-adaptive-pretraining', 'chinese-social-media']
venue: "ACL 2024"
tldr: "Chinese MentalBERT is a domain-adaptive pre-trained model on Chinese social media text for improved mental health analysis."
---

# Chinese MentalBERT: Domain-Adaptive Pre-training on Social Media for Chinese Mental Health Text Analysis

**Source**: [https://aclanthology.org/2024.findings-acl.629/](https://aclanthology.org/2024.findings-acl.629/)

**TLDR**: Chinese MentalBERT is a domain-adaptive pre-trained model on Chinese social media text for improved mental health analysis.

## Abstract

AbstractIn the current environment, psychological issues are prevalent and widespread, with social media serving as a key outlet for individuals to share their feelings. This results in the generation of vast quantities of data daily, where negative emotions have the potential to precipitate crisis situations. There is a recognized need for models capable of efficient analysis. While pre-trained language models have demonstrated their effectiveness broadly, there’s a noticeable gap in pre-trained models tailored for specialized domains like psychology. To address this, we have collected a huge dataset from Chinese social media platforms and enriched it with publicly available datasets to create a comprehensive database encompassing 3.36 million text entries. To enhance the model’s applicability to psychological text analysis, we integrated psychological lexicons into the pre-training masking mechanism. Building on an existing Chinese language model, we performed adaptive training to develop a model specialized for the psychological domain. We evaluated our model’s performance across six public datasets, where it demonstrated improvements compared to eight other models. Additionally, in the qualitative comparison experiment, our model provided psychologically relevant predictions given the masked sentences. Due to concerns regarding data privacy, the dataset will not be made publicly available. However, we have made the pre-trained models and codes publicly accessible to the community via: https://github.com/zwzzzQAQ/Chinese-MentalBERT.