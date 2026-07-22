---
title: "Recovering document annotations for sentence-level bitext"
source: "https://aclanthology.org/2024.findings-acl.589/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'natural-language-processing-information-extraction']
tags: ['machine-translation', 'document-level', 'bitext-annotation']
venue: "ACL 2024"
tldr: "Presents a method for recovering document-level annotations from sentence-level bitext to support context-aware machine translation."
---

# Recovering document annotations for sentence-level bitext

**Source**: [https://aclanthology.org/2024.findings-acl.589/](https://aclanthology.org/2024.findings-acl.589/)

**TLDR**: Presents a method for recovering document-level annotations from sentence-level bitext to support context-aware machine translation.

## Abstract

AbstractIn machine translation, historical models were incapable of handling longer contexts, so the lack of document-level datasets was less noticeable. Now, despite the emergence of long-sequence methods, we remain within a sentence-level paradigm and without data to adequately approach context-aware machine translation. Most large-scale datasets have been processed through a pipeline that discards document-level metadata. In this work, we reconstruct document-level information for three (ParaCrawl, News Commentary, and Europarl) large datasets in German, French, Spanish, Italian, Polish, and Portuguese (paired with English). We then introduce a document-level filtering technique as an alternative to traditional bitext filtering. We present this filtering with analysis to show that this method prefers context-consistent translations rather than those that may have been sentence-level machine translated. Last we train models on these longer contexts and demonstrate improvement in document-level translation without degradation of sentence-level translation. We release our dataset, ParaDocs, and resulting models as a resource to the community.