---
title: "Multi-Label Classification for Implicit Discourse Relation Recognition"
source: "https://aclanthology.org/2024.findings-acl.500/"
pdf_url: ""
categories: ['causal-reasoning-and-explanation-in-nlp', 'natural-language-processing-information-extraction']
tags: ['discourse-relations', 'multi-label-classification', 'PDTB']
venue: "ACL 2024"
tldr: "Multi-label classification is applied to implicit discourse relation recognition in PDTB-3 to handle ambiguous relation annotations."
---

# Multi-Label Classification for Implicit Discourse Relation Recognition

**Source**: [https://aclanthology.org/2024.findings-acl.500/](https://aclanthology.org/2024.findings-acl.500/)

**TLDR**: Multi-label classification is applied to implicit discourse relation recognition in PDTB-3 to handle ambiguous relation annotations.

## Abstract

AbstractDiscourse relations play a pivotal role in establishing coherence within textual content, uniting sentences and clauses into a cohesive narrative. The Penn Discourse Treebank (PDTB) stands as one of the most extensively utilized datasets in this domain. In PDTB-3, the annotators can assign multiple labels to an example, when they believe the simultaneous presence of multiple relations. Prior research in discourse relation recognition has treated these instances as separate examples during training, with a gold-standard prediction matching one of the labels considered correct at test time. However, this approach is inadequate, as it fails to account for the interdependence of labels in real-world contexts and to distinguish between cases where only one sense relation holds and cases where multiple relations hold simultaneously. In our work, we address this challenge by exploring various multi-label classification frameworks to handle implicit discourse relation recognition. We show that the methods for multi-label prediction don’t depress performance for single-label prediction. Additionally, we give comprehensive analysis of results and data. Our work contributes to advancing the understanding and application of discourse relations and provide a foundation for the future study.