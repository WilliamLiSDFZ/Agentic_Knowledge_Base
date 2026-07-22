---
title: "TextEE: Benchmark, Reevaluation, Reflections, and Future Challenges in Event Extraction"
source: "https://aclanthology.org/2024.findings-acl.760/"
pdf_url: ""
categories: ['natural-language-processing-information-extraction', 'nlp-benchmark-design-and-interpretability']
tags: ['event-extraction', 'benchmark', 'reevaluation', 'information-extraction', 'evaluation-methodology']
venue: "ACL 2024"
tldr: "Identifies and addresses evaluation challenges in event extraction benchmarks, providing standardized re-evaluation and future directions."
---

# TextEE: Benchmark, Reevaluation, Reflections, and Future Challenges in Event Extraction

**Source**: [https://aclanthology.org/2024.findings-acl.760/](https://aclanthology.org/2024.findings-acl.760/)

**TLDR**: Identifies and addresses evaluation challenges in event extraction benchmarks, providing standardized re-evaluation and future directions.

## Abstract

AbstractEvent extraction has gained considerable interest due to its wide-ranging applications. However, recent studies draw attention to evaluation issues, suggesting that reported scores may not accurately reflect the true performance. In this work, we identify and address evaluation challenges, including inconsistency due to varying data assumptions or preprocessing steps, the insufficiency of current evaluation frameworks that may introduce dataset or data split bias, and the low reproducibility of some previous approaches. To address these challenges, we present TextEE, a standardized, fair, and reproducible benchmark for event extraction. TextEE comprises standardized data preprocessing scripts and splits for 16 datasets spanning eight diverse domains and includes 14 recent methodologies, conducting a comprehensive benchmark reevaluation. We also evaluate five varied large language models on our TextEE benchmark and demonstrate how they struggle to achieve satisfactory performance. Inspired by our reevaluation results and findings, we discuss the role of event extraction in the current NLP era, as well as future challenges and insights derived from TextEE. We believe TextEE, the first standardized comprehensive benchmarking tool, will significantly facilitate future event extraction research.