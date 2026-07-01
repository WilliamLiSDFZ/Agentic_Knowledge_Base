---
title: "Robust Sleep Staging over Incomplete Multimodal Physiological Signals via Contrastive Imagination"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/cb0f9020c00fc52a9f6c9dbfacc6ac58-Abstract-Conference.html"
categories: ['wearable-biosignal-gesture-activity-benchmarks', 'missing-data-imputation-methods-and-applications']
tags: ['sleep-staging', 'multimodal-physiological-signals', 'missing-modality']
venue: "NeurIPS 2024"
tldr: "Proposes a contrastive imagination method for robust automated sleep staging under incomplete multimodal physiological signal conditions."
---

# Robust Sleep Staging over Incomplete Multimodal Physiological Signals via Contrastive Imagination

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/cb0f9020c00fc52a9f6c9dbfacc6ac58-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/cb0f9020c00fc52a9f6c9dbfacc6ac58-Abstract-Conference.html)

**TLDR**: Proposes a contrastive imagination method for robust automated sleep staging under incomplete multimodal physiological signal conditions.

## Abstract

Multimodal physiological signals, such as EEG, EOG and EMG, provide rich and reliable physiological information for automated sleep staging (ASS). However, in the real world, the completeness of various modalities is difficult to guarantee, which seriously affects the performance of ASS based on multimodal learning. Furthermore, the exploration of temporal context information within PTSs is also a serious challenge. To this end, we propose a robust multimodal sleep staging framework named contrastive imagination modality sleep network (CIMSleepNet). Specifically, CIMSleepNet handles the issue of arbitrary modal missing through the combination of modal awareness imagination module (MAIM) and semantic & modal calibration contrastive learning (SMCCL). Among them, MAIM can capture the interaction among modalities by learning the shared representation distribution of all modalities. Meanwhile, SMCCL introduces prior information of semantics and modalities to check semantic consistency while maintaining the uniqueness of each modality. Utilizing the calibration of SMCCL, the data distribution recovered by MAIM is aligned with the real data distribution. We further design a multi-level cross-branch temporal attention mechanism, which can facilitate the mining of interactive temporal context representations at both the intra-epoch and inter-epoch levels. Extensive experiments on five multimodal sleep datasets demonstrate that CIMSleepNet remarkably outperforms other competitive methods under various missing modality patterns. The source code is available at: https://github.com/SQAIYY/CIMSleepNet.