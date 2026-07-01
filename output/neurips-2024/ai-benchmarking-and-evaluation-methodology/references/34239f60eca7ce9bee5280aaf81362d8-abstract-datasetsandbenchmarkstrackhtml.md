---
title: "DF40: Toward Next-Generation Deepfake Detection"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/34239f60eca7ce9bee5280aaf81362d8-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'generative-models-for-visual-style-and-appearance']
tags: ['deepfake-detection', 'benchmark', 'face-forgery', 'generalization', 'evaluation']
venue: "NeurIPS 2024"
tldr: "Introduces DF40, a comprehensive next-generation benchmark for evaluating deepfake detection across diverse forgery types and domains."
---

# DF40: Toward Next-Generation Deepfake Detection

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/34239f60eca7ce9bee5280aaf81362d8-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/34239f60eca7ce9bee5280aaf81362d8-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces DF40, a comprehensive next-generation benchmark for evaluating deepfake detection across diverse forgery types and domains.

## Abstract

We propose a new comprehensive benchmark to revolutionize the current deepfake detection field to the next generation. Predominantly, existing works identify top-notch detection algorithms and models by adhering to the common practice: training detectors on one specific dataset (e.g., FF++) and testing them on other prevalent deepfake datasets. This protocol is often regarded as a "golden compass" for navigating SoTA detectors. But can these stand-out "winners" be truly applied to tackle the myriad of realistic and diverse deepfakes lurking in the real world? If not, what underlying factors contribute to this gap? In this work, we found the dataset (both train and test) can be the "primary culprit" due to the following: (1) forgery diversity: Deepfake techniques are commonly referred to as both face forgery (face-swapping and face-reenactment) and entire image synthesis (AIGC, especially face). Most existing datasets only contain partial types of them, with limited forgery methods implemented (e.g., 2 swapping and 2 reenactment methods in FF++); (2) forgery realism: The dominated training dataset, FF++, contains out-of-date forgery techniques from the past four years. "Honing skills" on these forgeries makes it difficult to guarantee effective detection generalization toward nowadays' SoTA deepfakes; (3) evaluation protocol: Most detection works perform evaluations on one type, e.g., face-swapping types only, which hinders the development of universal deepfake detectors.To address this dilemma, we construct a highly diverse and large-scale deepfake detection dataset called DF40,  which comprises 40 distinct deepfake techniques (10 times larger than FF++). We then conduct comprehensive evaluations using 4 standard evaluation protocols and 8 representative detection methods, resulting in over 2,000 evaluations. Through these evaluations, we provide an extensive analysis from various perspectives, leading to 7 new insightful findings contributing to the field. We also open up 4 valuable yet previously underexplored research questions to inspire future works. We release our dataset, code, and pre-trained weights at https://github.com/YZY-stack/DF40.