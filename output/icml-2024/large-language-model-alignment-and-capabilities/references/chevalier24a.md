---
title: "Language Models as Science Tutors"
source: "https://proceedings.mlr.press/v235/chevalier24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chevalier24a/chevalier24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'continual-learning-memory-plasticity']
tags: ['science-tutoring', 'language-models', 'educational-NLP']
venue: "ICML 2024"
tldr: "Language models are evaluated and developed as science tutors capable of processing long scientific documents for real-world educational applications."
---

# Language Models as Science Tutors

**Source**: [https://proceedings.mlr.press/v235/chevalier24a.html](https://proceedings.mlr.press/v235/chevalier24a.html)

**TLDR**: Language models are evaluated and developed as science tutors capable of processing long scientific documents for real-world educational applications.

## Abstract

NLP has recently made exciting progress toward training language models (LMs) with strong scientific problem-solving skills. However, model development has not focused on real-life use-cases of LMs for science, including applications in education that require processing long scientific documents. To address this, we introduce TutorEval and TutorChat. TutorEval is a diverse question-answering benchmark consisting of questions about long chapters from STEM textbooks, written by experts. TutorEval helps measure real-life usability of LMs as scientific assistants, and it is the first benchmark combining long contexts, free-form generation, and multi-disciplinary scientific knowledge. Moreover, we show that fine-tuning base models with existing dialogue datasets leads to poor performance on TutorEval. Therefore, we create TutorChat, a dataset of 80,000 long synthetic dialogues about textbooks. We use TutorChat to fine-tune Llemma models with 7B and 34B parameters. These LM tutors specialized in math have a 32K-token context window, and they excel at TutorEval while performing strongly on GSM8K and MATH. Our datasets build on open-source materials, and we release our models, data, and evaluations publicly.