---
title: "SRFUND: A Multi-Granularity Hierarchical Structure Reconstruction Benchmark in Form Understanding"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/cbeaff878d6446ed06c3e0ffa53477f2-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['form-understanding', 'document-benchmark', 'hierarchical-structure']
venue: "NeurIPS 2024"
tldr: "Introduces SRFUND, a multi-granularity hierarchical structure reconstruction benchmark for form understanding tasks."
---

# SRFUND: A Multi-Granularity Hierarchical Structure Reconstruction Benchmark in Form Understanding

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/cbeaff878d6446ed06c3e0ffa53477f2-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/cbeaff878d6446ed06c3e0ffa53477f2-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces SRFUND, a multi-granularity hierarchical structure reconstruction benchmark for form understanding tasks.

## Abstract

Accurately identifying and organizing textual content is crucial for the automation of document processing in the field of form understanding. Existing datasets, such as FUNSD and XFUND, support entity classification and relationship prediction tasks but are typically limited to local and entity-level annotations. This limitation overlooks the hierarchically structured representation of documents, constraining comprehensive understanding of complex forms. To address this issue, we present the SRFUND, a hierarchically structured multi-task form understanding benchmark. SRFUND provides refined annotations on top of the original FUNSD and XFUND datasets, encompassing five tasks: (1) word to text-line merging, (2) text-line to entity merging, (3) entity category classification, (4) item table localization, and (5) entity-based full-document hierarchical structure recovery. We meticulously supplemented the original dataset with missing annotations at various levels of granularity and added detailed annotations for multi-item table regions within the forms. Additionally, we introduce global hierarchical structure dependencies for entity relation prediction tasks, surpassing traditional local key-value associations. The SRFUND dataset includes eight languages including English, Chinese, Japanese, German, French, Spanish, Italian, and Portuguese, making it a powerful tool for cross-lingual form understanding. Extensive experimental results demonstrate that the SRFUND dataset presents new challenges and significant opportunities in handling diverse layouts and global hierarchical structures of forms, thus providing deep insights into the field of form understanding. The original dataset and implementations of baseline methods are available at https://sprateam-ustc.github.io/SRFUND.