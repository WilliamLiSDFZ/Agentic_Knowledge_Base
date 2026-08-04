---
title: "WISER: Weak Supervision and Supervised Representation Learning to Improve Drug Response Prediction in Cancer"
source: "https://proceedings.mlr.press/v235/shubham24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shubham24a/shubham24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'data-selection-and-active-learning-methods']
tags: ['drug-response-prediction', 'weak-supervision', 'representation-learning']
venue: "ICML 2024"
tldr: "Combines weak supervision and supervised representation learning to improve drug response prediction in cancer cell lines."
---

# WISER: Weak Supervision and Supervised Representation Learning to Improve Drug Response Prediction in Cancer

**Source**: [https://proceedings.mlr.press/v235/shubham24a.html](https://proceedings.mlr.press/v235/shubham24a.html)

**TLDR**: Combines weak supervision and supervised representation learning to improve drug response prediction in cancer cell lines.

## Abstract

Cancer, a leading cause of death globally, occurs due to genomic changes and manifests heterogeneously across patients. To advance research on personalized treatment strategies, the effectiveness of various drugs on cells derived from cancers (’cell lines’) is experimentally determined in laboratory settings. Nevertheless, variations in the distribution of genomic data and drug responses between cell lines and humans arise due to biological and environmental differences. Moreover, while genomic profiles of many cancer patients are readily available, the scarcity of corresponding drug response data limits the ability to train machine learning models that can predict drug response in patients effectively. Recent cancer drug response prediction methods have largely followed the paradigm of unsupervised domain-invariant representation learning followed by a downstream drug response classification step. Introducing supervision in both stages is challenging due to heterogeneous patient response to drugs and limited drug response data. This paper addresses these challenges through a novel representation learning method in the first phase and weak supervision in the second. Experimental results on real patient data demonstrate the efficacy of our method WISER (Weak supervISion and supErvised Representation learning) over state-of-the-art alternatives on predicting personalized drug response. Our implementation is available at https://github.com/kyrs/WISER