---
title: "PLaD: Preference-based Large Language Model Distillation with Pseudo-Preference Pairs"
source: "https://aclanthology.org/2024.findings-acl.923/"
categories: ['llm-training-alignment-and-evaluation']
tags: ['knowledge-distillation', 'preference-learning', 'pseudo-preference-pairs', 'llm-compression']
venue: "ACL 2024"
tldr: "Proposes PLaD, a preference-based LLM distillation method using pseudo-preference pairs to train compact student models."
---

# PLaD: Preference-based Large Language Model Distillation with Pseudo-Preference Pairs

**Source**: [https://aclanthology.org/2024.findings-acl.923/](https://aclanthology.org/2024.findings-acl.923/)

**TLDR**: Proposes PLaD, a preference-based LLM distillation method using pseudo-preference pairs to train compact student models.

## Abstract

AbstractLarge Language Models (LLMs) have exhibited impressive capabilities in various tasks, yet their vast parameter sizes restrict their applicability in resource-constrained settings. Knowledge distillation (KD) offers a viable solution by transferring expertise from large teacher models to compact student models. However, traditional KD techniques face specific challenges when applied to LLMs, including restricted access to LLM outputs, significant teacher-student capacity gaps, and the inherited mis-calibration issue. In this work, we present PLaD, a novel preference-based LLM distillation framework. PLaD exploits the teacher-student capacity discrepancy to generate pseudo-preference pairs where teacher outputs are preferred over student outputs. Then, PLaD leverages a ranking loss to re-calibrate the student’s estimation of sequence likelihood, which steers the student’s focus towards understanding the relative quality of outputs instead of simply imitating the teacher. PLaD bypasses the need for access to teacher LLM’s internal states, tackles the student’s expressivity limitations, and mitigates the student mis-calibration issue. Through extensive experiments on two sequence generation tasks and with various LLMs, we demonstrate the effectiveness of our proposed PLaD framework.