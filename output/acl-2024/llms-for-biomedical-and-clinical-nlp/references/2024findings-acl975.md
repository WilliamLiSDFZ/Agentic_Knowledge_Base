---
title: "MedDec: A Dataset for Extracting Medical Decisions from Discharge Summaries"
source: "https://aclanthology.org/2024.findings-acl.975/"
pdf_url: ""
categories: ['llms-for-biomedical-and-clinical-nlp', 'document-understanding-and-information-extraction']
tags: ['clinical-nlp', 'medical-decision-extraction', 'discharge-summaries']
venue: "ACL 2024"
tldr: "MedDec is a new dataset for extracting medical decision spans from clinical discharge summaries across multiple disease types."
---

# MedDec: A Dataset for Extracting Medical Decisions from Discharge Summaries

**Source**: [https://aclanthology.org/2024.findings-acl.975/](https://aclanthology.org/2024.findings-acl.975/)

**TLDR**: MedDec is a new dataset for extracting medical decision spans from clinical discharge summaries across multiple disease types.

## Abstract

AbstractMedical decisions directly impact individuals’ health and well-being. Extracting decision spans from clinical notes plays a crucial role in understanding medical decision-making processes. In this paper, we develop a new dataset called “MedDec,” which contains clinical notes of eleven different phenotypes (diseases) annotated by ten types of medical decisions. We introduce the task of medical decision extraction, aiming to jointly extract and classify different types of medical decisions within clinical notes. We provide a comprehensive analysis of the dataset, develop a span detection model as a baseline for this task, evaluate recent span detection approaches, and employ a few metrics to measure the complexity of data samples. Our findings shed light on the complexities inherent in clinical decision extraction and enable future work in this area of research. The dataset and code are available through https://github.com/CLU-UML/MedDec.