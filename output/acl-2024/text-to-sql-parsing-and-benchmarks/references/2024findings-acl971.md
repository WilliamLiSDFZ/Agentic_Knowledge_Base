---
title: "EHR-SeqSQL : A Sequential Text-to-SQL Dataset For Interactively Exploring Electronic Health Records"
source: "https://aclanthology.org/2024.findings-acl.971/"
categories: ['text-to-sql-parsing-and-benchmarks', 'llms-for-biomedical-and-clinical-nlp']
tags: ['text-to-sql', 'electronic-health-records', 'sequential-parsing']
venue: "ACL 2024"
tldr: "Introduces EHR-SeqSQL, a sequential text-to-SQL dataset for interactively and compositionally querying electronic health record databases."
---

# EHR-SeqSQL : A Sequential Text-to-SQL Dataset For Interactively Exploring Electronic Health Records

**Source**: [https://aclanthology.org/2024.findings-acl.971/](https://aclanthology.org/2024.findings-acl.971/)

**TLDR**: Introduces EHR-SeqSQL, a sequential text-to-SQL dataset for interactively and compositionally querying electronic health record databases.

## Abstract

AbstractIn this paper, we introduce EHR-SeqSQL, a novel sequential text-to-SQL dataset for Electronic Health Record (EHR) databases. EHR-SeqSQL is designed to address critical yet underexplored aspects in text-to-SQL parsing: interactivity, compositionality, and efficiency. To the best of our knowledge, EHR-SeqSQL is not only the largest but also the first medical text-to-SQL dataset benchmark to include sequential and contextual questions. We provide a data split and the new test set designed to assess compositional generalization ability. Our experiments demonstrate the superiority of a multi-turn approach over a single-turn approach in learning compositionality. Additionally, our dataset integrates specially crafted tokens into SQL queries to improve execution efficiency. With EHR-SeqSQL, we aim to bridge the gap between practical needs and academic research in the text-to-SQL domain.