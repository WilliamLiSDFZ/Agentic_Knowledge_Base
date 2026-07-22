---
title: "Deepfake Defense: Constructing and Evaluating a Specialized Urdu Deepfake Audio Dataset"
source: "https://aclanthology.org/2024.findings-acl.861/"
categories: ['urdu-deepfake-audio-detection-dataset']
tags: ['deepfake-audio', 'urdu', 'speaker-verification']
venue: "ACL 2024"
tldr: "Presents a novel Urdu deepfake audio dataset to support development of countermeasures against deepfake attacks on automatic speaker verification systems."
---

# Deepfake Defense: Constructing and Evaluating a Specialized Urdu Deepfake Audio Dataset

**Source**: [https://aclanthology.org/2024.findings-acl.861/](https://aclanthology.org/2024.findings-acl.861/)

**TLDR**: Presents a novel Urdu deepfake audio dataset to support development of countermeasures against deepfake attacks on automatic speaker verification systems.

## Abstract

AbstractDeepfakes, particularly in the auditory domain, have become a significant threat, necessitating the development of robust countermeasures. This paper addresses the escalating challenges posed by deepfake attacks on Automatic Speaker Verification (ASV) systems. We present a novel Urdu deepfake audio dataset for deepfake detection, focusing on two spoofing attacks – Tacotron and VITS TTS. The dataset construction involves careful consideration of phonemic cover and balance and comparison with existing corpora like PRUS and PronouncUR. Evaluation with AASIST-L model shows EERs of 0.495 and 0.524 for VITS TTS and Tacotron-generated audios, respectively, with variability across speakers. Further, this research implements a detailed human evaluation, incorporating a user study to gauge whether people are able to discern deepfake audios from real (bonafide) audios. The ROC curve analysis shows an area under the curve (AUC) of 0.63, indicating that individuals demonstrate a limited ability to detect deepfakes (approximately 1 in 3 fake audio samples are regarded as real). Our work contributes a valuable resource for training deepfake detection models in low-resource languages like Urdu, addressing the critical gap in existing datasets. The dataset is publicly available at: https://github.com/CSALT-LUMS/urdu-deepfake-dataset.