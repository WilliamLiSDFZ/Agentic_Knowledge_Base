---
title: "It Is Not About What You Say, It Is About How You Say It: A Surprisingly Simple Approach for Improving Reading Comprehension"
source: "https://aclanthology.org/2024.findings-acl.491/"
pdf_url: ""
categories: ['nlp-benchmark-design-and-interpretability', 'educational-question-generation-and-comprehension']
tags: ['reading-comprehension', 'input-formatting', 'question-answering', 'NLP-practices']
venue: "ACL 2024"
tldr: "Shows that simple changes in how reading comprehension inputs are ordered can significantly improve model performance."
---

# It Is Not About What You Say, It Is About How You Say It: A Surprisingly Simple Approach for Improving Reading Comprehension

**Source**: [https://aclanthology.org/2024.findings-acl.491/](https://aclanthology.org/2024.findings-acl.491/)

**TLDR**: Shows that simple changes in how reading comprehension inputs are ordered can significantly improve model performance.

## Abstract

AbstractNatural language processing has seen rapid progress over the past decade. Due to the speed of developments, some practices get established without proper evaluation. Considering one such case and focusing on reading comprehension, we ask our first research question: 1) How does the order of inputs – i.e., question and context – affect model performance? Additionally, given recent advancements in input emphasis, we ask a second research question: 2) Does emphasizing either the question, the context, or both enhance performance? Experimenting with 9 large language models across 3 datasets, we find that presenting the context before the question improves model performance, with an accuracy increase of up to 31%. Furthermore, emphasizing the context yields superior results compared to question emphasis, and in general, emphasizing parts of the input is particularly effective for addressing questions that models lack the parametric knowledge to answer. Experimenting with both prompt-based and attention-based emphasis methods, we additionally find that the best method is surprisingly simple: it only requires concatenating a few tokens to the input and results in an ac- curacy improvement of up to 36%, allowing smaller models to outperform their significantly larger counterparts.