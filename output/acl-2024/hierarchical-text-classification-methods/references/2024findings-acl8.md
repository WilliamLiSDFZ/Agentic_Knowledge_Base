---
title: "CHIME: LLM-Assisted Hierarchical Organization of Scientific Studies for Literature Review Support"
source: "https://aclanthology.org/2024.findings-acl.8/"
pdf_url: ""
categories: ['hierarchical-text-classification-methods']
tags: ['literature-review', 'hierarchical-organization', 'scientific-studies']
venue: "ACL 2024"
tldr: "CHIME uses LLMs to produce hierarchical organizations of scientific studies to assist researchers in literature review."
---

# CHIME: LLM-Assisted Hierarchical Organization of Scientific Studies for Literature Review Support

**Source**: [https://aclanthology.org/2024.findings-acl.8/](https://aclanthology.org/2024.findings-acl.8/)

**TLDR**: CHIME uses LLMs to produce hierarchical organizations of scientific studies to assist researchers in literature review.

## Abstract

AbstractLiterature review requires researchers to synthesize a large amount of information and is increasingly challenging as the scientific literature expands. In this work, we investigate the potential of LLMs for producing hierarchical organizations of scientific studies to assist researchers with literature review. We define hierarchical organizations as tree structures where nodes refer to topical categories and every node is linked to the studies assigned to that category. Our naive LLM-based pipeline for hierarchy generation from a set of studies produces promising yet imperfect hierarchies, motivating us to collect CHIME, an expert-curated dataset for this task focused on biomedicine. Given the challenging and time-consuming nature of building hierarchies from scratch, we use a human-in-the-loop process in which experts correct errors (both links between categories and study assignment) in LLM-generated hierarchies. CHIME contains 2,174 LLM-generated hierarchies covering 472 topics, and expert-corrected hierarchies for a subset of 100 topics. Expert corrections allow us to quantify LLM performance, and we find that while they are quite good at generating and organizing categories, their assignment of studies to categories could be improved. We attempt to train a corrector model with human feedback which improves study assignment by 12.6 F1 points. We release our dataset and models to encourage research on developing better assistive tools for literature review.