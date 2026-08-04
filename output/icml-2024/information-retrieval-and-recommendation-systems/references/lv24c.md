---
title: "Coarse-to-Fine Highlighting: Reducing Knowledge Hallucination in Large Language Models"
source: "https://proceedings.mlr.press/v235/lv24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lv24c/lv24c.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'information-retrieval-and-recommendation-systems']
tags: ['hallucination', 'retrieval-augmented-generation', 'LLM', 'knowledge-grounding']
venue: "ICML 2024"
tldr: "A coarse-to-fine highlighting method reduces knowledge hallucination in LLMs by improving retrieval-augmented language model context utilization."
---

# Coarse-to-Fine Highlighting: Reducing Knowledge Hallucination in Large Language Models

**Source**: [https://proceedings.mlr.press/v235/lv24c.html](https://proceedings.mlr.press/v235/lv24c.html)

**TLDR**: A coarse-to-fine highlighting method reduces knowledge hallucination in LLMs by improving retrieval-augmented language model context utilization.

## Abstract

Generation of plausible but incorrect factual information, often termed hallucination, has attracted significant research interest. Retrieval-augmented language model (RALM)—which enhances models with up-to-date knowledge—emerges as a promising method to reduce hallucination. However, existing RALMs may instead exacerbate hallucination when retrieving lengthy contexts. To address this challenge, we propose COFT, a novel COarse-to-Fine highlighTing method to focus on different granularity-level key texts, thereby avoiding getting lost in lengthy contexts. Specifically, COFT consists of three components: recaller, scorer, and selector. First, recaller applies a knowledge graph to extract potential key entities in a given context. Second, scorer measures the importance of each entity by calculating its contextual weight. Finally, selector selects high contextual weight entities with a dynamic threshold algorithm and highlights the corresponding paragraphs, sentences, or words in a coarse-to-fine manner. Extensive experiments on knowledge hallucination benchmark demonstrate the effectiveness of COFT, leading to a superior performance over 30% in F1 score metric. Moreover, COFT also exhibits remarkable versatility across various long-form tasks, such as reading comprehension and question answering.