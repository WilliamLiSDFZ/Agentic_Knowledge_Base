---
title: "Rethinking Efficient Multilingual Text Summarization Meta-Evaluation"
source: "https://aclanthology.org/2024.findings-acl.930/"
pdf_url: ""
categories: ['multilingual-text-classification-and-sentiment-analysis', 'llm-training-alignment-and-evaluation']
tags: ['multilingual-summarization', 'meta-evaluation', 'machine-translation', 'evaluation-metrics', 'NLP']
venue: "ACL 2024"
tldr: "Investigates an efficient multilingual summarization meta-evaluation framework that leverages machine translation to reduce human annotation costs."
---

# Rethinking Efficient Multilingual Text Summarization Meta-Evaluation

**Source**: [https://aclanthology.org/2024.findings-acl.930/](https://aclanthology.org/2024.findings-acl.930/)

**TLDR**: Investigates an efficient multilingual summarization meta-evaluation framework that leverages machine translation to reduce human annotation costs.

## Abstract

AbstractEvaluating multilingual summarization evaluation metrics, i.e., meta-evaluation, is challenging because of the difficulty of human annotation collection. Therefore, we investigate an efficient multilingual meta-evaluation framework that uses machine translation systems to transform a monolingual meta-evaluation dataset into multilingual versions. To this end, we introduce a statistical test to verify the transformed dataset quality by checking the meta-evaluation result consistency on the original dataset and back-translated dataset. With this quality verification method, we transform an existing English summarization meta-evaluation dataset, RoSE, into 30 languages, and conduct a multilingual meta-evaluation of several representative automatic evaluation metrics. In our meta-evaluation, we find that metric performance varies in different languages and neural metrics generally outperform classical text-matching-based metrics in non-English languages. Moreover, we identify a two-stage evaluation method with superior performance, which first translates multilingual texts into English and then performs evaluation. We make the transformed datasets publicly available to facilitate future research.