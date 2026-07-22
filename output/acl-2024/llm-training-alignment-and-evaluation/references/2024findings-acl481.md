---
title: "Deterministic Reversible Data Augmentation for Neural Machine Translation"
source: "https://aclanthology.org/2024.findings-acl.481/"
categories: ['natural-language-processing-information-extraction', 'llm-training-alignment-and-evaluation']
tags: ['data-augmentation', 'neural-machine-translation', 'semantic-consistency', 'reversible-operations']
venue: "ACL 2024"
tldr: "This paper presents a deterministic reversible data augmentation method for neural machine translation that maintains semantic consistency while diversifying training corpora."
---

# Deterministic Reversible Data Augmentation for Neural Machine Translation

**Source**: [https://aclanthology.org/2024.findings-acl.481/](https://aclanthology.org/2024.findings-acl.481/)

**TLDR**: This paper presents a deterministic reversible data augmentation method for neural machine translation that maintains semantic consistency while diversifying training corpora.

## Abstract

AbstractData augmentation is an effective way to diversify corpora in machine translation, but previous methods may introduce semantic inconsistency between original and augmented data because of irreversible operations and random subword sampling procedures. To generate both symbolically diverse and semantically consistent augmentation data, we propose Deterministic Reversible Data Augmentation (DRDA), a simple but effective data augmentation method for neural machine translation. DRDA adopts deterministic segmentations and reversible operations to generate multi-granularity subword representations and pulls them closer together with multi-view techniques. With no extra corpora or model changes required, DRDA outperforms strong baselines on several translation tasks with a clear margin (up to 4.3 BLEU gain over Transformer) and exhibits good robustness in noisy, low-resource, and cross-domain datasets.