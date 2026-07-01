---
title: "AudioMarkBench: Benchmarking Robustness of Audio Watermarking"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/5d9b7775296a641a1913ab6b4425d5e8-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['audio-visual-speech-processing-and-benchmarks', 'ai-benchmarking-and-evaluation-methodology']
tags: ['audio-watermarking', 'benchmarking', 'robustness', 'synthetic-speech', 'text-to-speech']
venue: "NeurIPS 2024"
tldr: "Introduces AudioMarkBench, a benchmark for evaluating the robustness of audio watermarking methods against various attacks on AI-generated speech."
---

# AudioMarkBench: Benchmarking Robustness of Audio Watermarking

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/5d9b7775296a641a1913ab6b4425d5e8-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/5d9b7775296a641a1913ab6b4425d5e8-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces AudioMarkBench, a benchmark for evaluating the robustness of audio watermarking methods against various attacks on AI-generated speech.

## Abstract

The increasing realism of synthetic speech, driven by advancements in text-to-speech models, raises ethical concerns regarding impersonation and disinformation. Audio watermarking offers a promising solution via embedding human-imperceptible watermarks into AI-generated audios. However, the robustness of audio watermarking against common/adversarial perturbations remains understudied. We present AudioMarkBench, the first systematic benchmark for evaluating the robustness of audio watermarking against watermark removal and watermark forgery. AudioMarkBench includes a new dataset created from Common-Voice across languages, biological sexes, and ages, 3 state-of-the-art watermarking methods, and 15 types of perturbations. We benchmark the robustness of these methods against the perturbations in no-box, black-box, and white-box settings. Our findings highlight the vulnerabilities of current watermarking techniques and emphasize the need for more robust and fair audio watermarking solutions. Our dataset and code are publicly available at https://github.com/moyangkuo/AudioMarkBench.