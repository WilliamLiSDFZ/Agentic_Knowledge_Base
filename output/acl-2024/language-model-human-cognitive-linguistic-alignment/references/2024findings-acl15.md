---
title: "Lexicon-Level Contrastive Visual-Grounding Improves Language Modeling"
source: "https://aclanthology.org/2024.findings-acl.15/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems', 'language-model-human-cognitive-linguistic-alignment']
tags: ['visual-grounding', 'contrastive-learning', 'language-modeling']
venue: "ACL 2024"
tldr: "Shows that lexicon-level contrastive visual-grounding supervision improves language model representations and prediction accuracy."
---

# Lexicon-Level Contrastive Visual-Grounding Improves Language Modeling

**Source**: [https://aclanthology.org/2024.findings-acl.15/](https://aclanthology.org/2024.findings-acl.15/)

**TLDR**: Shows that lexicon-level contrastive visual-grounding supervision improves language model representations and prediction accuracy.

## Abstract

AbstractToday’s most accurate language models are trained on orders of magnitude more language data than human language learners receive— but with no supervision from other sensory modalities that play a crucial role in human learning. Can we make LMs’ representations and predictions more accurate (and more human-like) with more ecologically plausible supervision? This paper describes LexiContrastive Grounding (LCG), a grounded language learning procedure that leverages visual supervision to improve textual representations. LexiContrastive Grounding combines a next-token prediction strategy with a contrastive visual grounding objective, focusing on early-layerrepresentations that encode lexical information. Across multiple word-learning and sentence-understanding benchmarks, LexiContrastiveGrounding not only outperforms standard language-only models in terms of learning efficiency in small and developmentally plausible data regimes, but also improves upon vision-and-language learning procedures including CLIP, GIT, Flamingo, and Vokenization.Moreover, LexiContrastive Grounding improves perplexity by around 5% on multiple language modeling tasks compared to other models trained on the same amount of text data. This work underscores the potential of incorporating visual grounding into language models, aligning more closely with the multimodal nature of human language acquisition.