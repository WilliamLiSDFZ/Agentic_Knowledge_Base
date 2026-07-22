---
title: "Word Sense Linking: Disambiguating Outside the Sandbox"
source: "https://aclanthology.org/2024.findings-acl.851/"
pdf_url: ""
categories: ['natural-language-processing-information-extraction', 'concept-embedding-taxonomy-hierarchy-representation']
tags: ['word-sense-disambiguation', 'sense-linking', 'knowledge-bases']
venue: "ACL 2024"
tldr: "A new task of word sense linking that extends WSD beyond fixed inventories to disambiguate words against open sense repositories."
---

# Word Sense Linking: Disambiguating Outside the Sandbox

**Source**: [https://aclanthology.org/2024.findings-acl.851/](https://aclanthology.org/2024.findings-acl.851/)

**TLDR**: A new task of word sense linking that extends WSD beyond fixed inventories to disambiguate words against open sense repositories.

## Abstract

AbstractWord Sense Disambiguation (WSD) is the task of associating a word in a given context with its most suitable meaning among a set of possible candidates. While the task has recently witnessed renewed interest, with systems achieving performances above the estimated inter-annotator agreement, at the time of writing it still struggles to find downstream applications. We argue that one of the reasons behind this is the difficulty of applying WSD to plain text. Indeed, in the standard formulation, models work under the assumptions that a) all the spans to disambiguate have already been identified, and b) all the possible candidate senses of each span are provided, both of which are requirements that are far from trivial. In this work, we present a new task called Word Sense Linking (WSL) where, given an input text and a reference sense inventory, systems have to both identify which spans to disambiguate and then link them to their most suitable meaning.We put forward a transformer-based architecture for the task and thoroughly evaluate both its performance and those of state-of-the-art WSD systems scaled to WSL, iteratively relaxing the assumptions of WSD. We hope that our work will foster easier integration of lexical semantics into downstream applications.