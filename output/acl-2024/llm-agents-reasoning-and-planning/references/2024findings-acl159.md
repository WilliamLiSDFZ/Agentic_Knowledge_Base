---
title: "Chain of Logic: Rule-Based Reasoning with Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.159/"
pdf_url: ""
categories: ['legal-nlp-benchmarks-and-applications', 'llm-agents-reasoning-and-planning']
tags: ['rule-based-reasoning', 'legal-reasoning', 'chain-of-thought']
venue: "ACL 2024"
tldr: "Chain of Logic prompting enables LLMs to perform compositional rule-based legal reasoning more accurately."
---

# Chain of Logic: Rule-Based Reasoning with Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.159/](https://aclanthology.org/2024.findings-acl.159/)

**TLDR**: Chain of Logic prompting enables LLMs to perform compositional rule-based legal reasoning more accurately.

## Abstract

AbstractRule-based reasoning, a fundamental type of legal reasoning, enables us to draw conclusions by accurately applying a rule to a set of facts. We explore causal language models as rule-based reasoners, specifically with respect to compositional rules - rules consisting of multiple elements which form a complex logical expression. Reasoning about compositional rules is challenging because it requires multiple reasoning steps, and attending to the logical relationships between elements. We introduce a new prompting method, Chain of Logic, which elicits rule-based reasoning through decomposition (solving elements as independent threads of logic), and recomposition (recombining these sub-answers to resolve the underlying logical expression). This method was inspired by the IRAC (Issue, Rule, Application, Conclusion) framework, a sequential reasoning approach used by lawyers. We evaluate chain of logic across eight rule-based reasoning tasks involving three distinct compositional rules from the LegalBench benchmark and demonstrate it consistently outperforms other prompting methods, including chain of thought and self-ask, using open-source and commercial language models.