---
title: "SCALE: Synergized Collaboration of Asymmetric Language Translation Engines"
source: "https://aclanthology.org/2024.findings-acl.941/"
pdf_url: ""
categories: ['language-technology-cultural-linguistic-diversity', 'nlp-for-asian-languages']
tags: ['machine-translation', 'collaborative-framework', 'in-context-learning']
venue: "ACL 2024"
tldr: "SCALE synergizes a specialized translation model and a general-purpose LLM into a unified engine via triplet in-context demonstrations for improved translation."
---

# SCALE: Synergized Collaboration of Asymmetric Language Translation Engines

**Source**: [https://aclanthology.org/2024.findings-acl.941/](https://aclanthology.org/2024.findings-acl.941/)

**TLDR**: SCALE synergizes a specialized translation model and a general-purpose LLM into a unified engine via triplet in-context demonstrations for improved translation.

## Abstract

AbstractIn this paper, we introduce SCALE, a collaborative framework that connects a compact Specialized Translation Model (STM) and a general-purpose Large Language Model (LLM) as one unified translation engine. By introducing translation from STM into the triplet in-context demonstrations, SCALE unlocks refinement and pivoting ability of LLM, thus 1) mitigating language bias of LLMs and parallel data bias of STMs, 2) enhancing LLM speciality without sacrificing generality, and 3) facilitating continual learning in a LLM-tuning-free way.Our comprehensive experiments show that SCALE significantly outperforms both LLMs (GPT-4, GPT-3.5) and supervised models (NLLB, M2M) in either high-resource or challenging low-resource settings. Moreover SCALE shows great scalability by only updating the lightweight STM and witness consistent system improvement, an averaged 4 BLEURT score across 4 languages without tuning LLM. Interestingly, SCALE could also effectively exploit the existing language bias of LLMs by using an English-centric STM as a pivot to conduct translation between any language pairs, outperforming GPT-4 by an average of 6 COMET points across eight translation directions. Furthermore we provide an in-depth analysis of SCALE’s robustness, translation characteristics, latency costs and inherent language bias, providing solid foundation for future studies exploring the potential synergy between LLMs and more specialized models.