---
title: "Improving In-Context Learning with Prediction Feedback for Sentiment Analysis"
source: "https://aclanthology.org/2024.findings-acl.232/"
pdf_url: ""
categories: ['multilingual-text-classification-and-sentiment-analysis', 'llm-training-alignment-and-evaluation']
tags: ['sentiment-analysis', 'in-context-learning', 'prediction-feedback']
venue: "ACL 2024"
tldr: "Improves LLM sentiment analysis via a feedback-driven in-context learning mechanism that iteratively refines predictions."
---

# Improving In-Context Learning with Prediction Feedback for Sentiment Analysis

**Source**: [https://aclanthology.org/2024.findings-acl.232/](https://aclanthology.org/2024.findings-acl.232/)

**TLDR**: Improves LLM sentiment analysis via a feedback-driven in-context learning mechanism that iteratively refines predictions.

## Abstract

AbstractLarge language models (LLMs) have achieved promising results in sentiment analysis through the in-context learning (ICL) paradigm. However, their ability to distinguish subtle sentiments still remains a challenge. Inspired by the human ability to adjust understanding via feedback, this paper enhances ICL by incorporating prior predictions and feedback, aiming to rectify sentiment misinterpretation of LLMs. Specifically, the proposed framework consists of three steps: (1) acquiring prior predictions of LLMs, (2) devising predictive feedback based on correctness, and (3) leveraging a feedback-driven prompt to refine sentiment understanding. Experimental results across nine sentiment analysis datasets demonstrate the superiority of our framework over conventional ICL methods, with an average F1 improvement of 5.95%.