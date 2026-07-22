---
title: "Tox-BART: Leveraging Toxicity Attributes for Explanation Generation of Implicit Hate Speech"
source: "https://aclanthology.org/2024.findings-acl.831/"
pdf_url: ""
categories: ['hate-speech-and-toxic-content-detection', 'moral-figurative-language-nlp-analysis']
tags: ['implicit-hate-speech', 'explanation-generation', 'knowledge-graph']
venue: "ACL 2024"
tldr: "Leverages toxicity attributes and knowledge graph tuples with BART to generate explanations for implicit hate speech."
---

# Tox-BART: Leveraging Toxicity Attributes for Explanation Generation of Implicit Hate Speech

**Source**: [https://aclanthology.org/2024.findings-acl.831/](https://aclanthology.org/2024.findings-acl.831/)

**TLDR**: Leverages toxicity attributes and knowledge graph tuples with BART to generate explanations for implicit hate speech.

## Abstract

AbstractEmploying language models to generate explanations for an incoming implicit hate post is an active area of research. The explanation is intended to make explicit the underlying stereotype and aid content moderators. The training often combines top-k relevant knowledge graph (KG) tuples to provide world knowledge and improve performance on standard metrics. Interestingly, our study presents conflicting evidence for the role of the quality of KG tuples in generating implicit explanations. Consequently, simpler models incorporating external toxicity signals outperform KG-infused models. Compared to the KG-based setup, we observe a comparable performance for SBIC (LatentHatred) datasets with a performance variation of +0.44 (+0.49), +1.83 (-1.56), and -4.59 (+0.77) in BLEU, ROUGE-L, and BERTScore. Further human evaluation and error analysis reveal that our proposed setup produces more precise explanations than zero-shot GPT-3.5, highlighting the intricate nature of the task.