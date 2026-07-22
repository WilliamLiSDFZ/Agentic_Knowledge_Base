---
title: "CIDAR: Culturally Relevant Instruction Dataset For Arabic"
source: "https://aclanthology.org/2024.findings-acl.764/"
pdf_url: ""
categories: ['language-technology-cultural-linguistic-diversity', 'llm-training-alignment-and-evaluation']
tags: ['arabic-instruction-tuning', 'cultural-relevance', 'dataset']
venue: "ACL 2024"
tldr: "Introduces CIDAR, a culturally relevant Arabic instruction dataset to reduce Western bias in LLM instruction tuning."
---

# CIDAR: Culturally Relevant Instruction Dataset For Arabic

**Source**: [https://aclanthology.org/2024.findings-acl.764/](https://aclanthology.org/2024.findings-acl.764/)

**TLDR**: Introduces CIDAR, a culturally relevant Arabic instruction dataset to reduce Western bias in LLM instruction tuning.

## Abstract

AbstractInstruction tuning has emerged as a prominent methodology for teaching Large Language Models (LLMs) to follow instructions. However, current instruction datasets predominantly cater to English or are derived from English-dominated LLMs, leading to inherent biases toward Western culture. This bias negatively impacts non-English languages such as Arabic and the unique culture of the Arab region. This paper addresses this limitation by introducing CIDAR, the first open Arabic instruction-tuning dataset culturally aligned by native Arabic speakers. CIDAR contains 10,000 instruction and output pairs that represent the Arab region. We discuss the cultural relevance of CIDAR via the analysis and comparison to a few models fine-tuned on other datasets. Our experiments indicate that models fine-tuned on CIDAR achieve better cultural alignment compared to those fine-tuned on 30x more data.