---
title: "SHDocs: A dataset, benchmark, and method to efficiently generate high-quality, real-world specular highlight data with near-perfect alignment"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/af9199ef7d5ff267451a667170124c04-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'scene-text-and-document-recognition']
tags: ['specular-highlights', 'dataset', 'document-recognition']
venue: "NeurIPS 2024"
tldr: "Presents a dataset, benchmark, and method for generating high-quality aligned real-world specular highlight data to aid vision-based reasoning tasks."
---

# SHDocs: A dataset, benchmark, and method to efficiently generate high-quality, real-world specular highlight data with near-perfect alignment

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/af9199ef7d5ff267451a667170124c04-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/af9199ef7d5ff267451a667170124c04-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents a dataset, benchmark, and method for generating high-quality aligned real-world specular highlight data to aid vision-based reasoning tasks.

## Abstract

A frequent problem in vision-based reasoning tasks such as object detection and optical character recognition (OCR) is the persistence of specular highlights. Specular highlights appear as bright spots of glare that occur due to the concentrated reflection of light; these spots manifest as image artifacts which occlude computer vision models and are challenging to reconstruct. Despite this, specular highlight removal receives relatively little attention due to the difficulty of acquiring high-quality, real-world data. We introduce a method to generate specular highlight data with near-perfect alignment and present SHDocs—a dataset of specular highlights on document images created using our method. Through our benchmark, we demonstrate that our dataset enables us to surpass the performance of state-of-the-art specular highlight removal models and downstream OCR tasks. We release our dataset, code, and methods publicly to motivate further exploration of image enhancement for practical computer vision challenges.