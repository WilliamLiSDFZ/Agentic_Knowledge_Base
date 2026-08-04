---
title: "One for All: A Universal Generator for Concept Unlearnability via Multi-Modal Alignment"
source: "https://proceedings.mlr.press/v235/chen24bc.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24bc/chen24bc.pdf"
categories: ['adversarial-robustness-and-model-security', 'learning-with-imperfect-data-and-bias']
tags: ['unlearnable-examples', 'data-protection', 'multi-modal-alignment']
venue: "ICML 2024"
tldr: "A universal generator creates unlearnable examples to protect personal data from unauthorized use via multi-modal alignment."
---

# One for All: A Universal Generator for Concept Unlearnability via Multi-Modal Alignment

**Source**: [https://proceedings.mlr.press/v235/chen24bc.html](https://proceedings.mlr.press/v235/chen24bc.html)

**TLDR**: A universal generator creates unlearnable examples to protect personal data from unauthorized use via multi-modal alignment.

## Abstract

The abundance of free internet data offers unprecedented opportunities for researchers and developers, but it also poses privacy risks. Utilizing data without explicit consent raises critical challenges in protecting personal information.Unlearnable examples have emerged as a feasible protection approach, which renders the data unlearnable, i.e., useless to third parties, by injecting imperceptible perturbations. However, these perturbations only exhibit unlearnable effects on either a particular dataset or label-consistent scenarios, thereby lacking broad applicability. To address both issues concurrently, we propose a universal perturbation generator that harnesses data with concept unlearnability, thereby broadening the scope of unlearnability beyond specific datasets or labels. Specifically, we leverage multi-modal pre-trained models to establish a connection between the data concepts in a shared embedding space. This connection enables the information transformation from image data to text concepts. Consequently, we can align the text embedding using concept-wise discriminant loss, and render the data unlearnable. Extensive experiments conducted on real-world datasets demonstrate the concept unlearnability, i.e., cross-dataset transferability and label-agnostic utility, of our proposed unlearnable examples, as well as their robustness against attacks.