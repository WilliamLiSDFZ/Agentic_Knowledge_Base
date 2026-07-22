---
title: "REInstruct: Building Instruction Data from Unlabeled Corpus"
source: "https://aclanthology.org/2024.findings-acl.408/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'llms-for-biomedical-and-clinical-nlp']
tags: ['instruction-tuning', 'unlabeled-corpus', 'data-construction']
venue: "ACL 2024"
tldr: "REInstruct automatically builds instruction-tuning data from unlabeled corpora without relying on proprietary LLM distillation."
---

# REInstruct: Building Instruction Data from Unlabeled Corpus

**Source**: [https://aclanthology.org/2024.findings-acl.408/](https://aclanthology.org/2024.findings-acl.408/)

**TLDR**: REInstruct automatically builds instruction-tuning data from unlabeled corpora without relying on proprietary LLM distillation.

## Abstract

AbstractManually annotating instruction data for large language models is difficult, costly, and hard to scale. Meanwhile, current automatic annotation methods typically rely on distilling synthetic data from proprietary LLMs, which not only limits the upper bound of the quality of the instruction data but also raises potential copyright issues. In this paper, we propose REInstruct, a simple and scalable method to automatically build instruction data from an unlabeled corpus without heavy reliance on proprietary LLMs and human annotation.Specifically, REInstruct first selects a subset of unlabeled texts that potentially contain well-structured helpful and insightful content and then generates instructions for these texts. To generate accurate and relevant responses for effective and robust training, REInstruct further proposes a rewriting-based approach to improve the quality of the generated instruction data. By training Llama-7b on a combination of 3k seed data and 32k synthetic data from REInstruct, fine-tuned model achieves a 65.41% win rate on AlpacaEval leaderboard against text-davinci-003, outperforming other open-source, non-distilled instruction data construction methods. The code is publicly available at https://github.com/cs32963/REInstruct.