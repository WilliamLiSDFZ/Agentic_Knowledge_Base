---
title: "Meta-Reasoning: Semantics-Symbol Deconstruction for Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.34/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-agents-reasoning-and-planning']
tags: ['neural-symbolic', 'meta-reasoning', 'formal-language']
venue: "ACL 2024"
tldr: "Proposes a semantics-symbol deconstruction approach enabling LLMs to perform meta-reasoning beyond rigid syntactic mappings to formal languages."
---

# Meta-Reasoning: Semantics-Symbol Deconstruction for Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.34/](https://aclanthology.org/2024.findings-acl.34/)

**TLDR**: Proposes a semantics-symbol deconstruction approach enabling LLMs to perform meta-reasoning beyond rigid syntactic mappings to formal languages.

## Abstract

AbstractNeural-symbolic methods have demonstrated efficiency in enhancing the reasoning abilities of large language models (LLMs). However, existing methods mainly rely on syntactically mapping natural languages to complete formal languages like Python and SQL. Those methods require that reasoning tasks be convertible into programs, which cater to the computer execution mindset and deviate from human reasoning habits. To broaden symbolic methods’ applicability and adaptability in the real world, we propose Meta-Reasoning from a linguistic perspective. This method empowers LLMs to deconstruct reasoning-independent semantic information into generic symbolic representations, thereby efficiently capturing more generalized reasoning knowledge. We conduct extensive experiments on more than ten datasets encompassing conventional reasoning tasks like arithmetic, symbolic, and logical reasoning, and the more complex interactive reasoning tasks like theory-of-mind reasoning. Experimental results demonstrate that Meta-Reasoning significantly enhances in-context reasoning accuracy, learning efficiency, out-of-domain generalization, and output stability compared to the Chain-of-Thought technique.