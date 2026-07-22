---
title: "Resisting the Lure of the Skyline: Grounding Practices in Active Learning for Morphological Inflection"
source: "https://aclanthology.org/2024.acl-short.4/"
pdf_url: ""
categories: ['nlp-research-culture-and-practices']
tags: ['active-learning', 'morphological-inflection', 'experimental-design', 'language-documentation']
venue: "ACL 2024"
tldr: "Examines experimental design pitfalls in active learning for morphological inflection in language documentation settings."
---

# Resisting the Lure of the Skyline: Grounding Practices in Active Learning for Morphological Inflection

**Source**: [https://aclanthology.org/2024.acl-short.4/](https://aclanthology.org/2024.acl-short.4/)

**TLDR**: Examines experimental design pitfalls in active learning for morphological inflection in language documentation settings.

## Abstract

AbstractActive learning (AL) aims to lower the demand of annotation by selecting informative unannotated samples for the model building. In this paper, we explore the importance of conscious experimental design in the language documentation and description setting, particularly the distribution of the unannotated sample pool. We focus on the task of morphological inflection using a Transformer model. We propose context motivated benchmarks: a baseline and skyline. The baseline describes the frequency weighted distribution encountered in natural speech. We simulate this using Wikipedia texts. The skyline defines the more common approach, uniform sampling from a large, balanced corpus (UniMorph, in our case), which often yields mixed results. We note the unrealistic nature of this unannotated pool. When these factors are considered, our results show a clear benefit to targeted sampling.