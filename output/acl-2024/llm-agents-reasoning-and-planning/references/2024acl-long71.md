---
title: "Grounding Language Model with Chunking-Free In-Context Retrieval"
source: "https://aclanthology.org/2024.acl-long.71/"
categories: ['llm-hallucination-detection-and-mitigation', 'llm-agents-reasoning-and-planning']
tags: ['retrieval-augmented-generation', 'chunking-free', 'in-context-retrieval']
venue: "ACL 2024"
tldr: "Presents a chunking-free in-context retrieval approach for RAG systems that improves evidence grounding over long documents."
---

# Grounding Language Model with Chunking-Free In-Context Retrieval

**Source**: [https://aclanthology.org/2024.acl-long.71/](https://aclanthology.org/2024.acl-long.71/)

**TLDR**: Presents a chunking-free in-context retrieval approach for RAG systems that improves evidence grounding over long documents.

## Abstract

AbstractThis paper presents a novel Chunking-Free In-Context (CFIC) retrieval approach, specifically tailored for Retrieval-Augmented Generation (RAG) systems. Traditional RAG systems often struggle with grounding responses using precise evidence text due to the challenges of processing lengthy documents and filtering out irrelevant content. Commonly employed solutions, such as document chunking and adapting language models to handle longer contexts, have their limitations. These methods either disrupt the semantic coherence of the text or fail to effectively address the issues of noise and inaccuracy in evidence retrieval.The CFIC approach addresses these challenges by circumventing the conventional chunking process. It utilizes the encoded hidden states of documents for in-context retrieval, employing auto-aggressive decoding to accurately identify the specific evidence text required for user queries, eliminating the need for chunking. CFIC is further enhanced by incorporating two innovative decoding strategies, namely Constrained Sentence Prefix Decoding and Skip Decoding. These strategies not only improve the efficiency of the retrieval process but also ensure that the fidelity of the generated grounding text evidence is maintained.Our evaluations of CFIC on a range of open question answering datasets demonstrate its superiority in retrieving relevant and accurate information, offering a significant improvement over traditional methods. By doing away with the need for document chunking, CFIC presents a more streamlined, effective, and efficient retrieval solution, making it a valuable advancement in the field of RAG systems.