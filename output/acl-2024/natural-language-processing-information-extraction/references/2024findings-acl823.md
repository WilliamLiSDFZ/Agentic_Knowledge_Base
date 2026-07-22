---
title: "MultiSQL: A Schema-Integrated Context-Dependent Text2SQL Dataset with Diverse SQL Operations"
source: "https://aclanthology.org/2024.findings-acl.823/"
categories: ['text-to-sql-parsing-and-benchmarks', 'natural-language-processing-information-extraction']
tags: ['text-to-SQL', 'context-dependent', 'multi-turn-dialogue']
venue: "ACL 2024"
tldr: "Introduces MultiSQL, a schema-integrated context-dependent Text2SQL dataset with diverse and realistic SQL operations."
---

# MultiSQL: A Schema-Integrated Context-Dependent Text2SQL Dataset with Diverse SQL Operations

**Source**: [https://aclanthology.org/2024.findings-acl.823/](https://aclanthology.org/2024.findings-acl.823/)

**TLDR**: Introduces MultiSQL, a schema-integrated context-dependent Text2SQL dataset with diverse and realistic SQL operations.

## Abstract

AbstractText2SQL is a task that translates natural language into SQL statements. Context-dependent Text2SQL offers a more natural database interaction by simulating dialogues between users and databases, with CoSQL and SparC as representative datasets. Yet, these datasets struggle to accurately replicate real-world situations. To address this, we introduce MultiSQL, which extends them in three key aspects: (1) Diverse SQL Operations. We incorporate diverse SQL types such as Create, Update, and Insert to broaden the scope of SQL operations. (2) Schema-Integrated Context. We integrated query context with database schema dependencies to better depict database complexity. (3) Extended Dialogues. We expand dialogue length to better simulate long conversations and complex interactions. This multi-type, schema-integrated, context-dependent Text2SQL dataset comprises nearly 800 dialogue groups and over 9,000 interaction turns across 166 complex databases, offering a better benchmark for interactive user-database dialogue.Addressing MultiSQL’s challenges, we refined evaluation metrics to better capture diverse SQL types and schema dependencies. We designed a prompt framework that leverages historical data and self-refinement to accurately capture the dependency between text queries and database structures. Experiments with GPT-3.5, GPT-4, and LLaMA2-7B show both the effectiveness of our strategies and the challenges of MultiSQL. The datasets is available at https://github.com/grandchicken/MultiSQL.