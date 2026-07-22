---
title: "Aligning Speech Segments Beyond Pure Semantics"
source: "https://aclanthology.org/2024.findings-acl.216/"
categories: ['speech-and-language-multimodal-generation-systems', 'language-technology-cultural-linguistic-diversity']
tags: ['speech-alignment', 'expressive-speech', 'multilingual']
venue: "ACL 2024"
tldr: "Proposes methods to align speech segments beyond pure semantics to preserve prosody for expressive speech translation."
---

# Aligning Speech Segments Beyond Pure Semantics

**Source**: [https://aclanthology.org/2024.findings-acl.216/](https://aclanthology.org/2024.findings-acl.216/)

**TLDR**: Proposes methods to align speech segments beyond pure semantics to preserve prosody for expressive speech translation.

## Abstract

AbstractMultilingual parallel data for speech-to-speech translation is scarce and expensive to create from scratch. This is all the more true for expressive speech translation, which aims at preserving not only the semantics, but also the overall prosody (e.g. style, emotion, rate-of-speech). Existing corpora contain speech utterances with the same meaning, yet the overall prosody is typically different, as human annotators are not tasked with reproducing these aspects, or crowed-sourced efforts do not specifically target this kind of alignment in priority. In this paper, we propose a novel alignment algorithm, which automatically forms pairs of speech segments aligned not only in meaning, but also in expressivity. In order to validate our approach, we train an expressive multilingual speech-to-speech translation system on the automatically aligned data. Our experiments show that in comparison to semantic-only approaches, expressively aligned data yields large improvements in source expressivity preservation (e.g. 43% uplift in speech rate preservation on average), while still maintaining content translation quality. In some scenarios, results also indicate that this alignment algorithm can outperform standard, semantic-focused approaches even on content translation quality.