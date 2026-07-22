---
title: "Understanding Fine-grained Distortions in Reports of Scientific Findings"
source: "https://aclanthology.org/2024.findings-acl.369/"
categories: ['computational-misinformation-narrative-framing-detection', 'llm-based-scientific-misinformation-detection']
tags: ['science-communication', 'distortion-detection', 'misinformation']
venue: "ACL 2024"
tldr: "A fine-grained framework for understanding and detecting distortions in how scientific findings are reported in popular media."
---

# Understanding Fine-grained Distortions in Reports of Scientific Findings

**Source**: [https://aclanthology.org/2024.findings-acl.369/](https://aclanthology.org/2024.findings-acl.369/)

**TLDR**: A fine-grained framework for understanding and detecting distortions in how scientific findings are reported in popular media.

## Abstract

AbstractDistorted science communication harms individuals and society as it can lead to unhealthy behavior change and decrease trust in scientific institutions. Given the rapidly increasing volume of science communication in recent years, a fine-grained understanding of how findings from scientific publications are reported to the general public, and methods to detect distortions from the original work automatically, are crucial. Prior work focused on individual aspects of distortions or worked with unpaired data. In this work, we make three foundational contributions towards addressing this problem: (1) annotating 1,600 instances of scientific findings from academic papers paired with corresponding findings as reported in news articles and tweets wrt. four characteristics: causality, certainty, generality and sensationalism; (2) establishing baselines for automatically detecting these characteristics; and (3) analyzing the prevalence of changes in these characteristics in both human-annotated and large-scale unlabeled data. Our results show that scientific findings frequently undergo subtle distortions when reported. Tweets distort findings more often than science news reports. Detecting fine-grained distortions automatically poses a challenging task. In our experiments, fine-tuned task-specific models consistently outperform few-shot LLM prompting.