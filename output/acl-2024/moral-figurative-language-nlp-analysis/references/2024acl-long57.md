---
title: "Can ChatGPT’s Performance be Improved on Verb Metaphor Detection Tasks? Bootstrapping and Combining Tacit Knowledge"
source: "https://aclanthology.org/2024.acl-long.57/"
pdf_url: ""
categories: ['moral-figurative-language-nlp-analysis', 'llm-training-alignment-and-evaluation']
tags: ['metaphor-detection', 'chatgpt', 'bootstrapping']
venue: "ACL 2024"
tldr: "This paper improves ChatGPT's verb metaphor detection by bootstrapping and combining tacit knowledge without large labeled datasets."
---

# Can ChatGPT’s Performance be Improved on Verb Metaphor Detection Tasks? Bootstrapping and Combining Tacit Knowledge

**Source**: [https://aclanthology.org/2024.acl-long.57/](https://aclanthology.org/2024.acl-long.57/)

**TLDR**: This paper improves ChatGPT's verb metaphor detection by bootstrapping and combining tacit knowledge without large labeled datasets.

## Abstract

AbstractMetaphors detection, as an important task in the field of NLP, has been receiving sustained academic attention in recent years. Current researches focus supervised metaphors detection systems, which usually require large-scale, high-quality labeled data support. The emerge of large language models (e.g., ChatGPT) has made many NLP tasks (e.g., automatic summarization and dialogue systems) a qualitative leap. However, it is worth noting that the use of ChatGPT for unsupervised metaphors detection is often challenged with less-than-expected performance. Therefore, the aim of our work is to explore how to bootstrap and combine ChatGPT by detecting the most prevalent verb metaphors among metaphors. Our approach first utilizes ChatGPT to obtain literal collocations of target verbs and subject-object pairs of verbs in the text to be detected. Subsequently, these literal collocations and subject-object pairs are mapped to the same set of topics, and finally the verb metaphors are detected through the analysis of entailment relations. The experimental results show that our method achieves the best performance on the unsupervised verb metaphors detection task compared to existing unsupervised methods or direct prediction using ChatGPT. Our code is available at https://github.com/VILAN-Lab/Unsupervised-Metaphor-Detection.