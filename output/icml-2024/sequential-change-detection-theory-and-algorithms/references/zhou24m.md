---
title: "Sequential Kernel Goodness-of-fit Testing"
source: "https://proceedings.mlr.press/v235/zhou24m.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhou24m/zhou24m.pdf"
categories: ['sequential-change-detection-theory-and-algorithms', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['sequential-testing', 'kernel-goodness-of-fit', 'anytime-valid']
venue: "ICML 2024"
tldr: "Develops sequential kernel goodness-of-fit tests that adapt sample size to problem complexity, providing anytime-valid inference beyond fixed-sample batch testing."
---

# Sequential Kernel Goodness-of-fit Testing

**Source**: [https://proceedings.mlr.press/v235/zhou24m.html](https://proceedings.mlr.press/v235/zhou24m.html)

**TLDR**: Develops sequential kernel goodness-of-fit tests that adapt sample size to problem complexity, providing anytime-valid inference beyond fixed-sample batch testing.

## Abstract

Goodness-of-fit testing, a classical statistical tool, has been extensively explored in the batch setting, where the sample size is predetermined. However, practitioners often prefer methods that adapt to the complexity of a problem rather than fixing the sample size beforehand. Classical batch tests are generally unsuitable for streaming data, as valid inference after data peeking requires multiple testing corrections, resulting in reduced statistical power. To address this issue, we delve into the design of consistent sequential goodness-of-fit tests. Following the principle of testing by betting, we reframe this task as selecting a sequence of payoff functions that maximize the wealth of a fictitious bettor, betting against the null in a repeated game. We conduct experiments to demonstrate the adaptability of our sequential test across varying difficulty levels of problems while maintaining control over type-I errors.