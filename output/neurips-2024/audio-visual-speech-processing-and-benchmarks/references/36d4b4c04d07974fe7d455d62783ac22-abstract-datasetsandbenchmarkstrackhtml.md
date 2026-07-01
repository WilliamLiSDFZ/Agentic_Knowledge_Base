---
title: "Language Without Borders: A Dataset and Benchmark for Code-Switching Lip Reading"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/36d4b4c04d07974fe7d455d62783ac22-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['audio-visual-speech-processing-and-benchmarks', 'ai-benchmarking-and-evaluation-methodology']
tags: ['lip-reading', 'code-switching', 'multilingual', 'video-speech', 'benchmark-dataset']
venue: "NeurIPS 2024"
tldr: "A dataset and benchmark for code-switching lip reading that handles multilingual continuous lip movement recognition in practical scenarios."
---

# Language Without Borders: A Dataset and Benchmark for Code-Switching Lip Reading

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/36d4b4c04d07974fe7d455d62783ac22-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/36d4b4c04d07974fe7d455d62783ac22-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A dataset and benchmark for code-switching lip reading that handles multilingual continuous lip movement recognition in practical scenarios.

## Abstract

Lip reading aims at transforming the videos of continuous lip movement into textual contents, and has achieved significant progress over the past decade. It serves as a critical yet practical assistance for speech-impaired individuals, with more practicability than speech recognition in noisy environments. With the increasing interpersonal communications in social media owing to globalization, the existing monolingual datasets for lip reading may not be sufficient to meet the exponential proliferation of bilingual and even multilingual users. However, to our best knowledge, research on code-switching is only explored in speech recognition, while the attempts in lip reading are seriously neglected. To bridge this gap, we have collected a bilingual code-switching lip reading benchmark composed of Chinese and English, dubbed CSLR. As the pioneering work, we recruited 62 speakers with proficient foundations in bothspoken Chinese and English to express sentences containing both involved languages. Through rigorous criteria in data selection, CSLR benchmark has accumulated 85,560 video samples with a resolution of 1080x1920, totaling over 71.3 hours of high-quality code-switching lip movement data. To systematically evaluate the technical challenges in CSLR, we implement commonly-used lip reading backbones, as well as competitive solutions in code-switching speech for benchmark testing. Experiments show CSLR to be a challenging and under-explored lip reading task. We hope our proposed benchmark will extend the applicability of code-switching lip reading, and further contribute to the communities of cross-lingual communication and collaboration. Our dataset and benchmark are accessible at https://github.com/cslr-lipreading/CSLR.