---
title: "Topic-Conversation Relevance (TCR)  Dataset and Benchmarks"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/fd9b0883e4c9f0f0b3db673ce54dc8f2-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'statistical-inference-and-text-generation-methods\n\nhmm,-let-me-reconsider---looking-more-carefully-at-the-cluster:\n\n**score-matching-and-sampling-methods**']
tags: ['topic-relevance', 'meeting-effectiveness', 'benchmark-dataset', 'conversation-analysis', 'workplace']
venue: "NeurIPS 2024"
tldr: "A comprehensive Topic-Conversation Relevance dataset and benchmark for evaluating whether workplace meeting conversations remain on topic."
---

# Topic-Conversation Relevance (TCR)  Dataset and Benchmarks

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/fd9b0883e4c9f0f0b3db673ce54dc8f2-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/fd9b0883e4c9f0f0b3db673ce54dc8f2-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A comprehensive Topic-Conversation Relevance dataset and benchmark for evaluating whether workplace meeting conversations remain on topic.

## Abstract

Workplace meetings are vital to organizational collaboration, yet a large percentage of meetings are rated as ineffective. To help improve meeting effectiveness by understanding if the conversation is on topic, we create a comprehensive Topic-Conversation Relevance (TCR) dataset that covers a variety of domains and meeting styles. The TCR dataset includes 1,500 unique meetings, 22 million words in transcripts, and over 15,000 meeting topics, sourced from both newly collected Speech Interruption Meeting (SIM) data and existing public datasets. Along with the text data, we also open source scripts to generate synthetic meetings or create augmented meetings from the TCR dataset to enhance data diversity. For each data source, benchmarks are created using GPT-4 to evaluate the model accuracy in understanding transcription-topic relevance.