---
title: "Biomedical Visual Instruction Tuning with Clinician Preference Alignment"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/aec33ab89b5986605cd7c331396e7e5c-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-benchmarks-for-clinical-healthcare', 'visual-language-multimodal-generation-reasoning']
tags: ['biomedical-vision-language', 'instruction-tuning', 'clinician-preference']
venue: "NeurIPS 2024"
tldr: "A biomedical multimodal foundation model is developed via visual instruction tuning aligned with clinician preferences for medical image understanding."
---

# Biomedical Visual Instruction Tuning with Clinician Preference Alignment

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/aec33ab89b5986605cd7c331396e7e5c-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/aec33ab89b5986605cd7c331396e7e5c-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A biomedical multimodal foundation model is developed via visual instruction tuning aligned with clinician preferences for medical image understanding.

## Abstract

Recent advancements in multimodal foundation models have showcased impressive capabilities in understanding and reasoning with visual and textual information. Adapting these foundation models trained for general usage to specialized domains like biomedicine requires large-scale domain-specific instruction datasets. While existing works have explored curating such datasets automatically, the resultant datasets are not explicitly aligned with domain expertise. In this work, we propose a data-centric framework, Biomedical Visual Instruction Tuning with Clinician Preference Alignment (BioMed-VITAL), that incorporates clinician preferences into both stages of generating and selecting instruction data for tuning biomedical multimodal foundation models. First, during the generation stage, we prompt the GPT-4V generator with a diverse set of clinician-selected demonstrations for preference-aligned data candidate generation. Then, during the selection phase, we train a separate selection model, which explicitly distills clinician and policy-guided model preferences into a rating function to select high-quality data for medical instruction tuning. Results show that the model tuned with the instruction-following data from our method demonstrates a significant improvement in open visual chat (18.5% relatively) and medical VQA (win rate up to 81.73%). Our instruction-following data and models are available at https://BioMed-VITAL.github.io.