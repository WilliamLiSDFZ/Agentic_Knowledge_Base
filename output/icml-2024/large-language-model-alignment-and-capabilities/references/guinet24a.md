---
title: "Automated Evaluation of Retrieval-Augmented Language Models with Task-Specific Exam Generation"
source: "https://proceedings.mlr.press/v235/guinet24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/guinet24a/guinet24a.pdf"
categories: ['information-retrieval-and-recommendation-systems', 'large-language-model-alignment-and-capabilities']
tags: ['retrieval-augmented-generation', 'evaluation', 'synthetic-exam', 'question-generation', 'RAG']
venue: "ICML 2024"
tldr: "An automated method to evaluate RAG systems by generating synthetic multiple-choice exams from task-specific document corpora."
---

# Automated Evaluation of Retrieval-Augmented Language Models with Task-Specific Exam Generation

**Source**: [https://proceedings.mlr.press/v235/guinet24a.html](https://proceedings.mlr.press/v235/guinet24a.html)

**TLDR**: An automated method to evaluate RAG systems by generating synthetic multiple-choice exams from task-specific document corpora.

## Abstract

We propose a new method to measure the task-specific accuracy of Retrieval-Augmented Large Language Models (RAG). Evaluation is performed by scoring the RAG on an automatically-generated synthetic exam composed of multiple choice questions based on the corpus of documents associated with the task. Our method is an automated, cost-efficient, interpretable, and robust strategy to select the optimal components for a RAG system. We leverage Item Response Theory (IRT) to estimate the quality of an exam and its informativeness on task-specific accuracy. IRT also provides a natural way to iteratively improve the exam by eliminating the exam questions that are not sufficiently informative about a model’s ability. We demonstrate our approach on four new open-ended Question-Answering tasks based on Arxiv abstracts, StackExchange questions, AWS DevOps troubleshooting guides, and SEC filings. In addition, our experiments reveal more general insights into factors impacting RAG performance like size, retrieval mechanism, prompting and fine-tuning. Most notably, our findings show that choosing the right retrieval algorithms often leads to bigger performance gains than simply using a larger language model.