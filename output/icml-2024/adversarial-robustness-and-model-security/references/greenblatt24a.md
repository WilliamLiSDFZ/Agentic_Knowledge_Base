---
title: "AI Control: Improving Safety Despite Intentional Subversion"
source: "https://proceedings.mlr.press/v235/greenblatt24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/greenblatt24a/greenblatt24a.pdf"
categories: ['ai-safety-governance-alignment-positions', 'adversarial-robustness-and-model-security']
tags: ['ai-safety', 'llm-control', 'red-teaming']
venue: "ICML 2024"
tldr: "AI Control proposes safety protocols that maintain robustness against intentional subversion by untrusted LLMs during autonomous deployment."
---

# AI Control: Improving Safety Despite Intentional Subversion

**Source**: [https://proceedings.mlr.press/v235/greenblatt24a.html](https://proceedings.mlr.press/v235/greenblatt24a.html)

**TLDR**: AI Control proposes safety protocols that maintain robustness against intentional subversion by untrusted LLMs during autonomous deployment.

## Abstract

As large language models (LLMs) become more powerful and are deployed more autonomously, it will be increasingly important to prevent them from causing harmful outcomes. To do so, safety measures either aim at making LLMs try to avoid harmful outcomes or aim at preventing LLMs from causing harmful outcomes, even if they try to cause them. In this paper, we focus on this second layer of defense. We develop and evaluate pipelines of safety techniques (protocols) that try to ensure safety despite intentional subversion - an approach we call AI control. We investigate a setting in which we want to solve a sequence of programming problems without ever submitting subtly wrong code, using access to a powerful but untrusted model (in our case, GPT-4), access to a less powerful trusted model (in our case, GPT-3.5), and limited access to high-quality trusted labor. We investigate a range of protocols and red-team them by exploring strategies that the untrusted model could use to subvert them. We find that using the trusted model to edit untrusted-model code or using the untrusted model as a monitor substantially improves on simple baselines.