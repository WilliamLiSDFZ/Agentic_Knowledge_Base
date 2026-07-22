---
title: "Are LLMs classical or nonmonotonic reasoners? Lessons from generics"
source: "https://aclanthology.org/2024.acl-short.51/"
pdf_url: ""
categories: ['language-model-human-cognitive-linguistic-alignment', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['nonmonotonic-reasoning', 'generics', 'LLM-evaluation']
venue: "ACL 2024"
tldr: "LLMs are evaluated on nonmonotonic reasoning using generic sentences, revealing limitations in flexible defeasible inference."
---

# Are LLMs classical or nonmonotonic reasoners? Lessons from generics

**Source**: [https://aclanthology.org/2024.acl-short.51/](https://aclanthology.org/2024.acl-short.51/)

**TLDR**: LLMs are evaluated on nonmonotonic reasoning using generic sentences, revealing limitations in flexible defeasible inference.

## Abstract

AbstractRecent scholarship on reasoning in LLMs has supplied evidence of impressive performance and flexible adaptation to machine generated or human critique. Nonmonotonic reasoning, crucial to human cognition for navigating the real world, remains a challenging, yet understudied task. In this work, we study nonmonotonic reasoning capabilities of seven state-of-the-art LLMs in one abstract and one commonsense reasoning task featuring generics, such as ‘Birds fly’, and exceptions, ‘Penguins don’t fly’ (see Fig. 1). While LLMs exhibit reasoning patterns in accordance with human nonmonotonic reasoning abilities, they fail to maintain stable beliefs on truth conditions of generics at the addition of supporting examples (‘Owls fly’) or unrelated information (‘Lions have manes’).Our findings highlight pitfalls in attributing human reasoning behaviours to LLMs as long as consistent reasoning remains elusive.