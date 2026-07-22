---
title: "Addressing Entity Translation Problem via Translation Difficulty and Context Diversity"
source: "https://aclanthology.org/2024.findings-acl.691/"
categories: ['natural-language-processing-information-extraction', 'language-technology-cultural-linguistic-diversity']
tags: ['named-entity-translation', 'NMT', 'context-diversity']
venue: "ACL 2024"
tldr: "Analyzes translation difficulty and context diversity to improve named entity translation in neural machine translation."
---

# Addressing Entity Translation Problem via Translation Difficulty and Context Diversity

**Source**: [https://aclanthology.org/2024.findings-acl.691/](https://aclanthology.org/2024.findings-acl.691/)

**TLDR**: Analyzes translation difficulty and context diversity to improve named entity translation in neural machine translation.

## Abstract

AbstractNeural machine translation (NMT) systems often produce inadequate translations for named entities. In this study, we conducted preliminary experiments to examine the factors affecting the translation accuracy of named entities, specifically focusing on their translation difficulty and context diversity. Based on our observations, we propose a novel data augmentation strategy to enhance the accuracy of named entity translation. The main concept behind our approach is to increase both the context diversity and translation probability for the targeted named entity pair. To achieve this, we construct additional samples for named entities that exhibit high translation difficulty or low context diversity and use the augmented training data to re-train the final translation model. Furthermore, we propose an entity-aware machine translation metric that prefers the translation output to generate more accurate named entities. Our experimental results demonstrate significant improvements over the baseline in terms of general translation performance and named entity translation accuracy across various test sets, such as WMT news translation and terminology test sets.