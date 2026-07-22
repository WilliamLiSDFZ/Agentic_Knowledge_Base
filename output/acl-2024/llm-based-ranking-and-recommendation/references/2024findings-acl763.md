---
title: "Measuring and Addressing Indexical Bias in Information Retrieval"
source: "https://aclanthology.org/2024.findings-acl.763/"
pdf_url: ""
categories: ['bias-and-fairness-in-llms', 'llm-based-ranking-and-recommendation']
tags: ['information-retrieval', 'bias', 'fairness', 'ranking', 'indexical-bias']
venue: "ACL 2024"
tldr: "This paper identifies and addresses indexical bias in IR systems, where document ordering introduces unfair or non-neutral positional biases."
---

# Measuring and Addressing Indexical Bias in Information Retrieval

**Source**: [https://aclanthology.org/2024.findings-acl.763/](https://aclanthology.org/2024.findings-acl.763/)

**TLDR**: This paper identifies and addresses indexical bias in IR systems, where document ordering introduces unfair or non-neutral positional biases.

## Abstract

AbstractInformation Retrieval (IR) systems are designed to deliver relevant content, but traditional systems may not optimize rankings for fairness, neutrality, or the balance of ideas. Consequently, IR can often introduce indexical biases, or biases in the positional order of documents. Although indexical bias can demonstrably affect people’s opinion, voting patterns, and other behaviors, these issues remain understudied as the field lacks reliable metrics and procedures for automatically measuring indexical bias. Towards this end, we introduce the PAIR framework, which supports automatic bias audits for ranked documents or entire IR systems. After introducing DUO, the first general-purpose automatic bias metric, we run an extensive evaluation of 8 IR systems on a new corpus of 32k synthetic and 4.7k natural documents, with 4k queries spanning 1.4k controversial issue topics. A human behavioral study validates our approach, showing that our bias metric can help predict when and how indexical bias will shift a reader’s opinion.