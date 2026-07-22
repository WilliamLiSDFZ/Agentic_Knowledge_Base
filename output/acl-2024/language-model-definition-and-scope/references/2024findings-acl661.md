---
title: "Definition Generation for Automatically Induced Semantic Frame"
source: "https://aclanthology.org/2024.findings-acl.661/"
categories: ['language-model-definition-and-scope', 'concept-embedding-taxonomy-hierarchy-representation']
tags: ['semantic-frames', 'definition-generation', 'framenet']
venue: "ACL 2024"
tldr: "Proposes a method to automatically generate definition sentences for computationally induced semantic frames, reducing manual annotation cost."
---

# Definition Generation for Automatically Induced Semantic Frame

**Source**: [https://aclanthology.org/2024.findings-acl.661/](https://aclanthology.org/2024.findings-acl.661/)

**TLDR**: Proposes a method to automatically generate definition sentences for computationally induced semantic frames, reducing manual annotation cost.

## Abstract

AbstractIn a semantic frame resource such as FrameNet, the definition sentence of a frame is essential for humans to understand the meaning of the frame intuitively. Recently, several attempts have been made to induce semantic frames from large corpora, but the cost of creating the definition sentences for such frames is significant. In this paper, we address a new task of generating frame definitions from a set of frame-evoking words. Specifically, given a cluster of frame-evoking words and associated exemplars induced as the same semantic frame, we utilize a large language model to generate frame definitions. We demonstrate that incorporating frame element reasoning as chain-of-thought can enhance the inclusion of correct frame elements in the generated definitions.