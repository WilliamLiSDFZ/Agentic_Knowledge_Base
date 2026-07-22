---
title: "When is a Language Process a Language Model?"
source: "https://aclanthology.org/2024.findings-acl.659/"
pdf_url: ""
categories: ['language-model-definition-and-scope', 'neural-language-models-formal-language-theory']
tags: ['language-model-theory', 'stochastic-process', 'probability', 'formal-language', 'definition']
venue: "ACL 2024"
tldr: "Examines the theoretical conditions under which a stochastic process qualifies as a proper language model, addressing probability mass leakage on infinite strings."
---

# When is a Language Process a Language Model?

**Source**: [https://aclanthology.org/2024.findings-acl.659/](https://aclanthology.org/2024.findings-acl.659/)

**TLDR**: Examines the theoretical conditions under which a stochastic process qualifies as a proper language model, addressing probability mass leakage on infinite strings.

## Abstract

AbstractA language model may be viewed as a 𝛴-valued stochastic process for some alphabet 𝛴.However, in some pathological situations, such a stochastic process may “leak” probability mass onto the set of infinite strings and hence is not equivalent to the conventional view of a language model as a distribution over ordinary (finite) strings.Such ill-behaved language processes are referred to as *non-tight* in the literature.In this work, we study conditions of tightness through the lens of stochastic processes.In particular, by regarding the symbol as marking a stopping time and using results from martingale theory, we give characterizations of tightness that generalize our previous work [(Du et al. 2023)](https://arxiv.org/abs/2212.10502).