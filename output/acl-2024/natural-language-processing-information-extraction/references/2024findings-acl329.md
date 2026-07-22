---
title: "Improving the Robustness of Distantly-Supervised Named Entity Recognition via Uncertainty-Aware Teacher Learning and Student-Student Collaborative Learning"
source: "https://aclanthology.org/2024.findings-acl.329/"
categories: ['label-noise-robust-annotation-learning', 'natural-language-processing-information-extraction']
tags: ['distant-supervision', 'named-entity-recognition', 'label-noise', 'teacher-student', 'collaborative-learning']
venue: "ACL 2024"
tldr: "Proposes uncertainty-aware teacher learning and student-student collaborative learning to improve robustness of distantly-supervised NER against label noise."
---

# Improving the Robustness of Distantly-Supervised Named Entity Recognition via Uncertainty-Aware Teacher Learning and Student-Student Collaborative Learning

**Source**: [https://aclanthology.org/2024.findings-acl.329/](https://aclanthology.org/2024.findings-acl.329/)

**TLDR**: Proposes uncertainty-aware teacher learning and student-student collaborative learning to improve robustness of distantly-supervised NER against label noise.

## Abstract

AbstractDistantly-Supervised Named Entity Recognition (DS-NER) effectively alleviates the burden of annotation, but meanwhile suffers from the label noise. Recent works attempt to adopt the teacher-student framework to gradually refine the training labels and improve the overall robustness. However, we argue that these teacher-student methods achieve limited performance because the poor calibration of the teacher network produces incorrectly pseudo-labeled samples, leading to error propagation. Therefore, we attempt to mitigate this issue by proposing: (1) Uncertainty-Aware Teacher Learning that leverages the prediction uncertainty to reduce the number of incorrect pseudo labels in the self-training stage; (2) Student-Student Collaborative Learning that allows the transfer of reliable labels between two student networks instead of indiscriminately relying on all pseudo labels from its teacher. This approach further enables a full exploration of mislabeled samples rather than simply filtering unreliable pseudo-labeled samples. We evaluate our proposed method on five DS-NER datasets, demonstrating that our method is superior to the state-of-the-art DS-NER denoising methods.