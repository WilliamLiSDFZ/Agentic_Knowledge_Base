---
title: "A Tale of Two Revisions: Summarizing Changes Across Document Versions"
source: "https://aclanthology.org/2024.findings-acl.190/"
pdf_url: ""
categories: ['document-understanding-and-information-extraction', 'natural-language-processing-information-extraction']
tags: ['document-revision', 'change-summarization', 'collaborative-writing']
venue: "ACL 2024"
tldr: "Proposes a system for summarizing changes across document versions to support collaborative writing workflows."
---

# A Tale of Two Revisions: Summarizing Changes Across Document Versions

**Source**: [https://aclanthology.org/2024.findings-acl.190/](https://aclanthology.org/2024.findings-acl.190/)

**TLDR**: Proposes a system for summarizing changes across document versions to support collaborative writing workflows.

## Abstract

AbstractDocument revision is a crucial aspect of the writing process, particularly in collaborative environments where multiple authors contribute simultaneously. However, current tools lack an efficient way to provide a comprehensive overview of changes between versions, leading to difficulties in understanding revisions. To address this, we propose a novel task of providing thematic summary of changes between document versions, organizing individual edits based on shared themes. We assess capabilities of LLMs on this task and further introduce three strategies to tackle this task: (i) representing the input of two documents along with edits in the ‘diff’ format (ii) a two-stage task decomposition with individual edit description generation as an intermediate task and (iii) clustering based chunking and subsequent merging techniques for handling longer documents. Our experiments demonstrate the effectiveness of our approach in improving the model’s capacity to handle this complex task. Additionally, we introduce ChangeSumm, a curated dataset comprising human-written thematic summaries for pairs of document versions, to facilitate evaluation and further research in this direction.