---
title: "DistillMIKE: Editing Distillation of Massive In-Context Knowledge Editing in Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.455/"
categories: ['llm-training-alignment-and-evaluation', 'llm-hallucination-detection-and-mitigation']
tags: ['knowledge-editing', 'in-context-learning', 'distillation']
venue: "ACL 2024"
tldr: "Proposes DistillMIKE, which distills massive in-context knowledge editing into LLM parameters to improve efficiency and scalability."
---

# DistillMIKE: Editing Distillation of Massive In-Context Knowledge Editing in Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.455/](https://aclanthology.org/2024.findings-acl.455/)

**TLDR**: Proposes DistillMIKE, which distills massive in-context knowledge editing into LLM parameters to improve efficiency and scalability.

## Abstract

AbstractAmong the recently emerged knowledge editing methods, in-context knowledge editing (IKE) has shown respectable abilities on knowledge editing in terms of generalization and specificity. Noting the promising advantages but unexplored issues of IKE, we propose **DistillMIKE** as a novel extension of IKE, i.e., editing **distill**ation of "**M**assive” **I**n-context **K**nowledge **E**diting in large language models (LLMs), mainly consisting of two expansions; 1) *Massive in-context knowledge editing (MIKE)*, which extends IKE to a massive editing task, aiming to inject not a single edit but a set of massive edits to LLMs; To preserve specificity, our key novel extension is a “selective” retrieval augmentation, where the retrieval-augmented IKE is only applied to “in-scope” examples, whereas the unedited model without IKE is employed for “out-of-scope” ones. 2) *Editing distillation* of MIKE using low-rank adaptation (LoRA), which distills editing abilities of MIKE to parameters of LLMs in a manner of eliminating the need of lengthy in-context demonstrations, thus removing the computational overhead encountered at the inference time. Experimental results on the zsRE and CounterFact datasets demonstrate that MIKE shows the state-of-the-art perfomrances and DistilMIKE show comparable performances with MIKE. Our code is available at https://github.com/JoveReCode/DistillMIKE.git.