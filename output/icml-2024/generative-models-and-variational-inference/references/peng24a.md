---
title: "Knowledge Distillation with Auxiliary Variable"
source: "https://proceedings.mlr.press/v235/peng24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/peng24a/peng24a.pdf"
categories: ['knowledge-distillation-methods-and-applications', 'generative-models-and-variational-inference']
tags: ['knowledge-distillation', 'auxiliary-variables', 'predictive-distributions', 'teacher-student', 'model-compression']
venue: "ICML 2024"
tldr: "Enhances knowledge distillation by introducing auxiliary variables to formulate richer student predictive distributions beyond the teacher's strategy."
---

# Knowledge Distillation with Auxiliary Variable

**Source**: [https://proceedings.mlr.press/v235/peng24a.html](https://proceedings.mlr.press/v235/peng24a.html)

**TLDR**: Enhances knowledge distillation by introducing auxiliary variables to formulate richer student predictive distributions beyond the teacher's strategy.

## Abstract

Knowledge distillation (KD) provides an efficient framework for transferring knowledge from a teacher model to a student model by aligning their predictive distributions. The existing KD methods adopt the same strategy as the teacher to formulate the student’s predictive distribution. However, employing the same distribution-modeling strategy typically causes sub-optimal knowledge transfer due to the discrepancy in model capacity between teacher and student models. Designing student-friendly teachers contributes to alleviating the capacity discrepancy, while it requires either complicated or student-specific training schemes. To cast off this dilemma, we propose to introduce an auxiliary variable to promote the ability of the student to model predictive distribution. The auxiliary variable is defined to be related to target variables, which will boost the model prediction. Specifically, we reformulate the predictive distribution with the auxiliary variable, deriving a novel objective function of KD. Theoretically, we provide insights to explain why the proposed objective function can outperform the existing KD methods. Experimentally, we demonstrate that the proposed objective function can considerably and consistently outperform existing KD methods.