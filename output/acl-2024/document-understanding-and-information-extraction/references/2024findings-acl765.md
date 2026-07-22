---
title: "RadGraph-XL: A Large-Scale Expert-Annotated Dataset for Entity and Relation Extraction from Radiology Reports"
source: "https://aclanthology.org/2024.findings-acl.765/"
pdf_url: ""
categories: ['llms-for-biomedical-and-clinical-nlp', 'document-understanding-and-information-extraction']
tags: ['radiology', 'entity-extraction', 'relation-extraction', 'clinical-NLP', 'annotation']
venue: "ACL 2024"
tldr: "RadGraph-XL is a large expert-annotated dataset of 2,300 radiology reports for clinical entity and relation extraction."
---

# RadGraph-XL: A Large-Scale Expert-Annotated Dataset for Entity and Relation Extraction from Radiology Reports

**Source**: [https://aclanthology.org/2024.findings-acl.765/](https://aclanthology.org/2024.findings-acl.765/)

**TLDR**: RadGraph-XL is a large expert-annotated dataset of 2,300 radiology reports for clinical entity and relation extraction.

## Abstract

AbstractIn order to enable extraction of structured clinical data from unstructured radiology reports, we introduce RadGraph-XL, a large-scale, expert-annotated dataset for clinical entity and relation extraction. RadGraph-XL consists of 2,300 radiology reports, which are annotated with over 410,000 entities and relations by board-certified radiologists. Whereas previous approaches focus solely on chest X-rays, RadGraph-XL includes data from four anatomy-modality pairs - chest CT, abdomen/pelvis CT, brain MR, and chest X-rays. Then, in order to automate structured information extraction, we use RadGraph-XL to train transformer-based models for clinical entity and relation extraction. Our evaluations include comprehensive ablation studies as well as an expert reader study that evaluates trained models on out-of-domain data. Results demonstrate that our model surpasses the performance of previous methods by up to 52% and notably outperforms GPT-4 in this domain. We release RadGraph-XL as well as our trained model to foster further innovation and research in structured clinical information extraction.