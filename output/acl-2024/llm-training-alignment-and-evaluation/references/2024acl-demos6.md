---
title: "LM Transparency Tool: Interactive Tool for Analyzing Transformer Language Models"
source: "https://aclanthology.org/2024.acl-demos.6/"
categories: ['transformer-architecture-analysis-and-design', 'llm-training-alignment-and-evaluation']
tags: ['transformer-interpretability', 'interactive-tool', 'attention-analysis']
venue: "ACL 2024"
tldr: "Presents an open-source interactive toolkit for comprehensively analyzing the internal decision-making process of Transformer-based language models."
---

# LM Transparency Tool: Interactive Tool for Analyzing Transformer Language Models

**Source**: [https://aclanthology.org/2024.acl-demos.6/](https://aclanthology.org/2024.acl-demos.6/)

**TLDR**: Presents an open-source interactive toolkit for comprehensively analyzing the internal decision-making process of Transformer-based language models.

## Abstract

AbstractWe present the LM Transparency Tool (LM-TT), an open-source interactive toolkit for analyzing the internal workings of Transformer-based language models. Differently from previously existing tools that focus on isolated parts of the decision-making process, our framework is designed to make the entire prediction process transparent, and allows tracing back model behavior from the top-layer representation to very fine-grained parts of the model. Specifically, it (i) shows the important part of the whole input-to-output information flow, (ii) allows attributing any changes done by a model block to individual attention heads and feed-forward neurons, (iii) allows interpreting the functions of those heads or neurons. A crucial part of this pipeline is showing the importance of specific model components at each step. As a result, we are able to look at the roles of model components only in cases where they are important for a prediction. Since knowing which components should be inspected is key for analyzing large models where the number of these components is extremely high, we believe our tool will greatly support the interpretability community both in research settings and in practical applications.