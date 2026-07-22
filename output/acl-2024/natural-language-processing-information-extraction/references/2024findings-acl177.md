---
title: "Towards Precise Localization of Critical Errors in Machine Translation"
source: "https://aclanthology.org/2024.findings-acl.177/"
categories: ['natural-language-processing-information-extraction']
tags: ['machine-translation', 'error-localization', 'critical-errors']
venue: "ACL 2024"
tldr: "Proposes a method to precisely localize critical meaning-altering errors in machine translation output."
---

# Towards Precise Localization of Critical Errors in Machine Translation

**Source**: [https://aclanthology.org/2024.findings-acl.177/](https://aclanthology.org/2024.findings-acl.177/)

**TLDR**: Proposes a method to precisely localize critical meaning-altering errors in machine translation output.

## Abstract

AbstractThe advent of large language models has experienced a remarkable improvement in the field of machine translation. However, machine translation is still vulnerable to critical meaning deviations, which may incur catastrophic issues in social or ethical contexts. In particular, existing critical error detection primarily focuses on identifying sentence-level errors, leaving the precise localization of such errors within the sentence unaddressed. In this paper, we introduce a new task, word-level critical error detection (WCED), to detect critical errors at a fine-grained level in machine translation sentences. The task aims to identify the parts of a machine translation that contain catastrophic meaning distortions. We hypothesize that the ability to determine errors at the sentence level will positively influence the detection of more granular errors. We propose a sentence-level error detection module to predict which words in a sentence have critical errors. Experimental results demonstrate that our method outperforms existing methodologies and LLM in En-De, Zh-En, En-Ru, and En-Ko. Our method is helpful for determining the fine-grained location of errors. We hope that such studies will improve the capacity to address critical errors adeptly.