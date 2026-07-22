---
title: "Mitigating Data Scarcity in Semantic Parsing across Languages with the Multilingual Semantic Layer and its Dataset"
source: "https://aclanthology.org/2024.findings-acl.836/"
pdf_url: ""
categories: ['text-to-sql-parsing-and-benchmarks', 'language-technology-cultural-linguistic-diversity']
tags: ['semantic-parsing', 'multilingual', 'low-resource']
venue: "ACL 2024"
tldr: "A multilingual semantic layer and dataset are introduced to mitigate data scarcity in semantic parsing across low-resource languages."
---

# Mitigating Data Scarcity in Semantic Parsing across Languages with the Multilingual Semantic Layer and its Dataset

**Source**: [https://aclanthology.org/2024.findings-acl.836/](https://aclanthology.org/2024.findings-acl.836/)

**TLDR**: A multilingual semantic layer and dataset are introduced to mitigate data scarcity in semantic parsing across low-resource languages.

## Abstract

AbstractData scarcity is a prevalent challenge in the era of Large Language Models (LLMs). The insatiable hunger of LLMs for large corpora becomes even more pronounced when dealing with non-English and low-resource languages. The issue is particularly exacerbated in Semantic Parsing (SP), i.e. the task of converting text into a formal representation. The complexity of semantic formalisms makes training human annotators and subsequent data annotation unfeasible on a large scale, especially across languages. To mitigate this, we first introduce the Multilingual Semantic Layer (MSL), a conceptual evolution of previous formalisms, which decouples from disambiguation and external inventories and simplifies the task. MSL provides the necessary tools to encode the meaning across languages, paving the way for developing a high-quality semantic parsing dataset across different languages in a semi-automatic strategy. Subsequently, we manually refine a portion of this dataset and fine-tune GPT-3.5 to propagate these refinements across the dataset. Then, we manually annotate 1,100 sentences in eleven languages, including low-resource ones. Finally, we assess our dataset’s quality, showcasing the performance gap reduction across languages in Semantic Parsing.