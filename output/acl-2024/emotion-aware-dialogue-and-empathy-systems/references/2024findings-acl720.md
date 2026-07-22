---
title: "EmoTransKG: An Innovative Emotion Knowledge Graph to Reveal Emotion Transformation"
source: "https://aclanthology.org/2024.findings-acl.720/"
categories: ['emotion-aware-dialogue-and-empathy-systems', 'concept-embedding-taxonomy-hierarchy-representation']
tags: ['emotion-knowledge-graph', 'emotion-transformation', 'open-text']
venue: "ACL 2024"
tldr: "Introduces EmoTransKG, a knowledge graph capturing emotion connections and transformations across diverse open-textual events."
---

# EmoTransKG: An Innovative Emotion Knowledge Graph to Reveal Emotion Transformation

**Source**: [https://aclanthology.org/2024.findings-acl.720/](https://aclanthology.org/2024.findings-acl.720/)

**TLDR**: Introduces EmoTransKG, a knowledge graph capturing emotion connections and transformations across diverse open-textual events.

## Abstract

AbstractThis paper introduces EmoTransKG, an innovative Emotion Knowledge Graph (EKG) that establishes connections and transformations between emotions across diverse open-textual events. Compared to existing EKGs, which primarily focus on linking emotion keywords to related terms or on assigning sentiment dimension ratings to emotion words by humans, EmoTransKG aims to represent the general knowledge involved in emotion transformation. Specifically, in conversations, successive emotions expressed by a single speaker are temporally considered as the head and tail entities, with open-text utterances (events) occurring between them representing the relation. To explore the knowledge of emotion transformations described in EmoTransKG, we develop a Transformer-based translational model called EmoTransNet, which predictively trains tail entities by interpreting the relation as an operation that transforms the source emotion into the target emotion. Particularly, our designed EmoTransNet serves as a plug-in module that seamlessly integrates with any conversational emotion recognition (CER) models for emotion retrofitting. Experimental results on two CER datasets demonstrate that the incorporation of EmoTransNet with baseline models results in substantial improvements, and the qualitative visualization of entities and relations clearly clarify their unique roles in emotion transformations. These experiments confirm the quality and effectiveness of EmoTransKG.