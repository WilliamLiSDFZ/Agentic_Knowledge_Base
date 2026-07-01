---
title: "EHRCon: Dataset for Checking Consistency between Unstructured Notes and Structured Tables in Electronic Health Records"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a291dad965af9bc2e39ffeb2ca1c6dc0-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-benchmarks-for-clinical-healthcare']
tags: ['electronic-health-records', 'consistency-checking', 'clinical-notes']
venue: "NeurIPS 2024"
tldr: "EHRCon is a dataset for verifying consistency between unstructured clinical notes and structured tables in electronic health records."
---

# EHRCon: Dataset for Checking Consistency between Unstructured Notes and Structured Tables in Electronic Health Records

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a291dad965af9bc2e39ffeb2ca1c6dc0-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/a291dad965af9bc2e39ffeb2ca1c6dc0-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: EHRCon is a dataset for verifying consistency between unstructured clinical notes and structured tables in electronic health records.

## Abstract

Electronic Health Records (EHRs) are integral for storing comprehensive patient medical records, combining structured data (e.g., medications) with detailed clinical notes (e.g., physician notes). These elements are essential for straightforward data retrieval and provide deep, contextual insights into patient care. However, they often suffer from discrepancies due to unintuitive EHR system designs and human errors, posing serious risks to patient safety. To address this, we developed EHRCon, a new dataset and task specifically designed to ensure data consistency between structured tables and unstructured notes in EHRs.EHRCon was crafted in collaboration with healthcare professionals using the MIMIC-III EHR dataset, and includes manual annotations of 3,943 entities across 105 clinical notes checked against database entries for consistency.EHRCon has two versions, one using the original MIMIC-III schema, and another using the OMOP CDM schema, in order to increase its applicability and generalizability. Furthermore, leveraging the capabilities of large language models, we introduce CheckEHR, a novel framework for verifying the consistency between clinical notes and database tables. CheckEHR utilizes an eight-stage process and shows promising results in both few-shot and zero-shot settings. The code is available at \url{https://github.com/dustn1259/EHRCon}.