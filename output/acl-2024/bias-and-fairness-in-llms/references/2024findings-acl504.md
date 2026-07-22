---
title: "GATE X-E : A Challenge Set for Gender-Fair Translations from Weakly-Gendered Languages"
source: "https://aclanthology.org/2024.findings-acl.504/"
categories: ['language-technology-cultural-linguistic-diversity', 'bias-and-fairness-in-llms']
tags: ['gender-bias', 'machine-translation', 'benchmark', 'weakly-gendered-languages', 'gender-fair']
venue: "ACL 2024"
tldr: "Presents a challenge set for evaluating gender-fair neural machine translation from weakly-gendered source languages."
---

# GATE X-E : A Challenge Set for Gender-Fair Translations from Weakly-Gendered Languages

**Source**: [https://aclanthology.org/2024.findings-acl.504/](https://aclanthology.org/2024.findings-acl.504/)

**TLDR**: Presents a challenge set for evaluating gender-fair neural machine translation from weakly-gendered source languages.

## Abstract

AbstractNeural Machine Translation (NMT) continues to improve in quality and adoption, yet the in advertent perpetuation of gender bias remains a significant concern. Despite numerous studies on gender bias in translations into English from weakly gendered-languages, there are no benchmarks for evaluating this phenomenon or for assessing mitigation strategies. To address this gap, we introduce GATE X-E, an extension to the GATE (Rarrick et al., 2023) corpus, that consists of human translations from Turkish, Hungarian, Finnish, and Persian into English. Each translation is accompanied by feminine, masculine, and neutral variants. The dataset, which contains between 1250 and 1850 instances for each of the four language pairs, features natural sentences with a wide range of sentence lengths and domains, challenging translation rewriters on various linguistic phenomena. Additionally, we present a translation gender rewriting solution built with GPT-4 and use GATE X-E to evaluate it. We open source our contributions to encourage further research on gender debiasing.