---
title: "Improving Multilingual Neural Machine Translation by Utilizing Semantic and Linguistic Features"
source: "https://aclanthology.org/2024.findings-acl.620/"
pdf_url: ""
categories: ['multilingual-text-classification-and-sentiment-analysis']
tags: ['multilingual-NMT', 'semantic-features', 'zero-shot-translation']
venue: "ACL 2024"
tldr: "Improves multilingual neural machine translation by incorporating both semantic and linguistic features to enhance zero-shot translation."
---

# Improving Multilingual Neural Machine Translation by Utilizing Semantic and Linguistic Features

**Source**: [https://aclanthology.org/2024.findings-acl.620/](https://aclanthology.org/2024.findings-acl.620/)

**TLDR**: Improves multilingual neural machine translation by incorporating both semantic and linguistic features to enhance zero-shot translation.

## Abstract

AbstractThe many-to-many multilingual neural machine translation can be regarded as the process of integrating semantic features from the source sentences and linguistic features from the target sentences. To enhance zero-shot translation, models need to share knowledge across languages, which can be achieved through auxiliary tasks for learning a universal representation or cross-lingual mapping. To this end, we propose to exploit both semantic and linguistic features between multiple languages to enhance multilingual translation. On the encoder side, we introduce a disentangling learning task that aligns encoder representations by disentangling semantic and linguistic features, thus facilitating knowledge transfer while preserving complete information. On the decoder side, we leverage a linguistic encoder to integrate low-level linguistic features to assist in the target language generation. Experimental results on multilingual datasets demonstrate significant improvement in zero-shot translation compared to the baseline system, while maintaining performance in supervised translation. Further analysis validates the effectiveness of our method in leveraging both semantic and linguistic features.