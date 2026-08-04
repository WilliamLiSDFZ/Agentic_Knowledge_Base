---
title: "ED-Copilot: Reduce Emergency Department Wait Time with Language Model Diagnostic Assistance"
source: "https://proceedings.mlr.press/v235/sun24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sun24a/sun24a.pdf"
categories: ['causal-ml-for-clinical-decision-making', 'large-language-model-alignment-and-capabilities']
tags: ['emergency-department', 'LLM', 'diagnostic-assistance', 'sequential-decision-making', 'cost-effective']
venue: "ICML 2024"
tldr: "ED-Copilot uses language models to provide time cost-effective diagnostic assistance in emergency departments to reduce patient wait times."
---

# ED-Copilot: Reduce Emergency Department Wait Time with Language Model Diagnostic Assistance

**Source**: [https://proceedings.mlr.press/v235/sun24a.html](https://proceedings.mlr.press/v235/sun24a.html)

**TLDR**: ED-Copilot uses language models to provide time cost-effective diagnostic assistance in emergency departments to reduce patient wait times.

## Abstract

In the emergency department (ED), patients undergo triage and multiple laboratory tests before diagnosis. This time-consuming process causes ED crowding which impacts patient mortality, medical errors, staff burnout, etc. This work proposes (time) cost-effective diagnostic assistance that leverages artificial intelligence systems to help ED clinicians make efficient and accurate diagnoses. In collaboration with ED clinicians, we use public patient data to curate MIMIC-ED-Assist, a benchmark for AI systems to suggest laboratory tests that minimize wait time while accurately predicting critical outcomes such as death. With MIMIC-ED-Assist, we develop ED-Copilot which sequentially suggests patient-specific laboratory tests and makes diagnostic predictions. ED-Copilot employs a pre-trained bio-medical language model to encode patient information and uses reinforcement learning to minimize ED wait time and maximize prediction accuracy. On MIMIC-ED-Assist, ED-Copilot improves prediction accuracy over baselines while halving average wait time from four hours to two hours. ED-Copilot can also effectively personalize treatment recommendations based on patient severity, further highlighting its potential as a diagnostic assistant. Since MIMIC-ED-Assist is a retrospective benchmark, ED-Copilot is restricted to recommend only observed tests. We show ED-Copilot achieves competitive performance without this restriction as the maximum allowed time increases. Our code is available at https://github.com/cxcscmu/ED-Copilot.