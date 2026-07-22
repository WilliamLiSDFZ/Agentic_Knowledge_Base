---
title: "Two Issues with Chinese Spelling Correction and A Refinement Solution"
source: "https://aclanthology.org/2024.acl-short.19/"
pdf_url: ""
categories: ['nlp-for-asian-languages', 'natural-language-processing-information-extraction']
tags: ['Chinese-spelling-correction', 'transformer', 'character-features']
venue: "ACL 2024"
tldr: "Identifies two key issues in Chinese spelling correction and proposes a refinement solution using improved character feature modeling."
---

# Two Issues with Chinese Spelling Correction and A Refinement Solution

**Source**: [https://aclanthology.org/2024.acl-short.19/](https://aclanthology.org/2024.acl-short.19/)

**TLDR**: Identifies two key issues in Chinese spelling correction and proposes a refinement solution using improved character feature modeling.

## Abstract

AbstractThe Chinese Spelling Correction (CSC) task aims to detect and correct misspelled characters in Chinese text, and has received lots of attention in the past few years. Most recent studies adopt a Transformer-based model and leverage different features of characters such as pronunciation, glyph and contextual information to enhance the model’s ability to complete the task. Despite their state-of-the-art performance, we observe two issues that should be addressed to further advance the CSC task. First, the widely-used benchmark datasets SIGHAN13, SIGHAN14 and SIGHAN15, contain many mistakes. Hence the performance of existing models is not accurate and should be re-evaluated. Second, existing models seem to have reached a performance bottleneck, where the improvements on the SIGHAN’s testing sets are increasingly smaller and unstable. To deal with the two issues, we make two contributions: (1) we manually fix the SIGHAN datasets and re-evaluate four representative CSC models using the fixed datasets; (2) we analyze the new results to identify the spelling errors that none of the four models successfully corrects, based on which we propose a simple yet effective refinement solution. Experimental results show that our solution improves the four models in all metrics by notable margins.