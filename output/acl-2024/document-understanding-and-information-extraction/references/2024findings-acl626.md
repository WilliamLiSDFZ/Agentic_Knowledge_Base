---
title: "PPTSER: A Plug-and-Play Tag-guided Method for Few-shot Semantic Entity Recognition on Visually-rich Documents"
source: "https://aclanthology.org/2024.findings-acl.626/"
pdf_url: ""
categories: ['document-understanding-and-information-extraction', 'multimodal-language-vision-learning-systems']
tags: ['few-shot-learning', 'semantic-entity-recognition', 'visually-rich-documents']
venue: "ACL 2024"
tldr: "Proposes a plug-and-play tag-guided method for few-shot semantic entity recognition on visually-rich documents."
---

# PPTSER: A Plug-and-Play Tag-guided Method for Few-shot Semantic Entity Recognition on Visually-rich Documents

**Source**: [https://aclanthology.org/2024.findings-acl.626/](https://aclanthology.org/2024.findings-acl.626/)

**TLDR**: Proposes a plug-and-play tag-guided method for few-shot semantic entity recognition on visually-rich documents.

## Abstract

AbstractVisually-rich document information extraction (VIE) is a vital aspect of document understanding, wherein Semantic Entity Recognition (SER) plays a significant role. However, few-shot SER on visually-rich documents remains relatively unexplored despite its considerable potential for practical applications. To address this issue, we propose a simple yet effective Plug-and-Play Tag-guided method for few-shot Semantic Entity Recognition (PPTSER) on visually-rich documents. PPTSER is built upon off-the-shelf multi-modal pre-trained models. It leverages the semantics of the tags to guide the SER task, reformulating SER into entity typing and span detection, handling both tasks simultaneously via cross-attention. Experimental results illustrate that PPTSER outperforms existing fine-tuning and few-shot methods, especially in low-data regimes. With full training data, PPTSER achieves comparable or superior performance to fine-tuning baseline. For instance, on the FUNSD benchmark, our method improves the performance of LayoutLMv3-base in 1-shot, 3-shot and 5-shot scenarios by 15.61%, 2.13%, and 2.01%, respectively. Overall, PPTSER demonstrates promising generalizability, effectiveness, and plug-and-play nature for few-shot SER on visually-rich documents. The codes will be available at [https://github.com/whlscut/PPTSER](https://github.com/whlscut/PPTSER).