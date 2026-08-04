---
title: "DE-COP: Detecting Copyrighted Content in Language Models Training Data"
source: "https://proceedings.mlr.press/v235/duarte24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/duarte24a/duarte24a.pdf"
categories: ['open-ai-governance-and-data-ethics']
tags: ['copyright-detection', 'LLM-training-data', 'membership-inference', 'data-ethics']
venue: "ICML 2024"
tldr: "DE-COP is a method to detect whether copyrighted content was used in LLM training by testing the model's ability to identify verbatim excerpts."
---

# DE-COP: Detecting Copyrighted Content in Language Models Training Data

**Source**: [https://proceedings.mlr.press/v235/duarte24a.html](https://proceedings.mlr.press/v235/duarte24a.html)

**TLDR**: DE-COP is a method to detect whether copyrighted content was used in LLM training by testing the model's ability to identify verbatim excerpts.

## Abstract

How can we detect if copyrighted content was used in the training process of a language model, considering that the training data is typically undisclosed? We are motivated by the premise that a language model is likely to identify verbatim excerpts from its training text. We propose DE-COP, a method to determine whether a piece of copyrighted content is included in training. DE-COP’s core approach is to probe an LLM with multiple-choice questions, whose options include both verbatim text and their paraphrases. We construct BookTection, a benchmark with excerpts from 165 books published prior and subsequent to a model’s training cutoff, along with their paraphrases. Our experiments show that DE-COP outperforms the prior best method by 8.6% in detection accuracy (AUC) on models with logits available. Moreover, DE-COP also achieves an average accuracy of 72% for detecting suspect books on fully black-box models where prior methods give approximately 0% accuracy. The code and datasets are available at https://github.com/LeiLiLab/DE-COP.