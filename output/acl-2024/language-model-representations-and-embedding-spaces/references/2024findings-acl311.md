---
title: "SDA: Semantic Discrepancy Alignment for Text-conditioned Image Retrieval"
source: "https://aclanthology.org/2024.findings-acl.311/"
categories: ['multimodal-language-vision-learning-systems', 'language-model-representations-and-embedding-spaces']
tags: ['image-retrieval', 'text-conditioned-retrieval', 'semantic-alignment']
venue: "ACL 2024"
tldr: "Semantic Discrepancy Alignment addresses embedding mismatches in text-conditioned image retrieval with small-scale datasets."
---

# SDA: Semantic Discrepancy Alignment for Text-conditioned Image Retrieval

**Source**: [https://aclanthology.org/2024.findings-acl.311/](https://aclanthology.org/2024.findings-acl.311/)

**TLDR**: Semantic Discrepancy Alignment addresses embedding mismatches in text-conditioned image retrieval with small-scale datasets.

## Abstract

AbstractIn the realm of text-conditioned image retrieval, models utilize a query composed of a reference image and modification text to retrieve corresponding images. Despite its significance, this task is fraught with challenges, including small-scale datasets due to labeling costs and the complexity of attributes in modification texts. These challenges often result in models learning a generalized representation of the query, thereby missing the semantic correlations of image and text attributes.In this paper, we introduce a general boosting framework designed to address these issues by employing semantic discrepancy alignment. Our framework first leverages the ChatGPT to augment text data by modifying the original modification text’s attributes. The augmented text is then combined with the original reference image to create an augmented composed query. Then we generate corresponding images using GPT-4 for the augmented composed query.We realize the cross-modal semantic discrepancy alignment by formulating distance consistency and neighbor consistency between the image and text domains. Through this novel approach, attribute in the text domain can be more effectively transferred to the image domain, enhancing retrieval performance. Extensive experiments on three prominent datasets validate the effectiveness of our approach, with state-of-the-art results on a majority of evaluation metrics compared to various baseline methods.