---
title: "Reasoning Like a Doctor: Improving Medical Dialogue Systems via Diagnostic Reasoning Process Alignment"
source: "https://aclanthology.org/2024.findings-acl.406/"
pdf_url: ""
categories: ['llms-for-biomedical-and-clinical-nlp', 'emotion-aware-dialogue-and-empathy-systems']
tags: ['medical-dialogue', 'diagnostic-reasoning', 'process-alignment']
venue: "ACL 2024"
tldr: "Improves medical dialogue systems by aligning LLM outputs with clinicians' structured diagnostic reasoning processes for more accurate medical assistance."
---

# Reasoning Like a Doctor: Improving Medical Dialogue Systems via Diagnostic Reasoning Process Alignment

**Source**: [https://aclanthology.org/2024.findings-acl.406/](https://aclanthology.org/2024.findings-acl.406/)

**TLDR**: Improves medical dialogue systems by aligning LLM outputs with clinicians' structured diagnostic reasoning processes for more accurate medical assistance.

## Abstract

AbstractMedical dialogue systems have attracted significant attention for their potential to act as medical assistants. Enabling these medical systems to emulate clinicians’ diagnostic reasoning process has been the long-standing research focus. Previous studies rudimentarily realized the simulation of clinicians’ diagnostic process by fine-tuning language models on high-quality dialogue datasets. Nonetheless, they overly focus on the outcomes of the clinician’s reasoning process while ignoring their internal thought processes and alignment with clinician preferences. Our work aims to build a medical dialogue system that aligns with clinicians’ diagnostic reasoning processes. We propose a novel framework, Emulation, designed to generate an appropriate response that relies on abductive and deductive diagnostic reasoning analyses and aligns with clinician preferences through thought process modeling. Experimental results on two datasets confirm the efficacy of Emulation. Crucially, our framework furnishes clear explanations for the generated responses, enhancing its transparency in medical consultations.