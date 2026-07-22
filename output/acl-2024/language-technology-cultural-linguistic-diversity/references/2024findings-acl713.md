---
title: "AustroTox: A Dataset for Target-Based Austrian German Offensive Language Detection"
source: "https://aclanthology.org/2024.findings-acl.713/"
pdf_url: ""
categories: ['hate-speech-and-toxic-content-detection', 'language-technology-cultural-linguistic-diversity']
tags: ['offensive-language', 'austrian-german', 'token-level-annotation']
venue: "ACL 2024"
tldr: "Presents AustroTox, a token-level annotated dataset for offensive language detection in Austrian German news forum comments."
---

# AustroTox: A Dataset for Target-Based Austrian German Offensive Language Detection

**Source**: [https://aclanthology.org/2024.findings-acl.713/](https://aclanthology.org/2024.findings-acl.713/)

**TLDR**: Presents AustroTox, a token-level annotated dataset for offensive language detection in Austrian German news forum comments.

## Abstract

AbstractModel interpretability in toxicity detection greatly profits from token-level annotations. However, currently, such annotations are only available in English. We introduce a dataset annotated for offensive language detection sourced from a news forum, notable for its incorporation of the Austrian German dialect, comprising 4,562 user comments. In addition to binary offensiveness classification, we identify spans within each comment constituting vulgar language or representing targets of offensive statements. We evaluate fine-tuned Transformer models as well as large language models in a zero- and few-shot fashion. The results indicate that while fine-tuned models excel in detecting linguistic peculiarities such as vulgar dialect, large language models demonstrate superior performance in detecting offensiveness in AustroTox.