---
title: "Model Editing at Scale leads to Gradual and Catastrophic Forgetting"
source: "https://aclanthology.org/2024.findings-acl.902/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'continual-learning-for-nlp-tasks']
tags: ['model-editing', 'catastrophic-forgetting', 'knowledge-updating']
venue: "ACL 2024"
tldr: "This paper shows that scaling model editing operations leads to gradual and catastrophic forgetting of previously learned knowledge in LLMs."
---

# Model Editing at Scale leads to Gradual and Catastrophic Forgetting

**Source**: [https://aclanthology.org/2024.findings-acl.902/](https://aclanthology.org/2024.findings-acl.902/)

**TLDR**: This paper shows that scaling model editing operations leads to gradual and catastrophic forgetting of previously learned knowledge in LLMs.

## Abstract

AbstractEditing knowledge in large language models is an attractive capability that allows us to correct incorrectly learned facts during pre-training, as well as update the model with an ever-growing list of new facts. While existing model editing techniques have shown promise, they are usually evaluated using metrics for reliability, specificity and generalization over one or few edits. We argue that for model editing to have practical utility, we must be able to make multiple edits to the same model. With this in mind, we evaluate current model editing methods at scale, focusing on two state of the art methods - ROME and MEMIT. With the lens of scalability, we evaluate model editing methods for three crucial properties - editing proficiency, fact forgetting and downstream performance. We find that as a model is edited sequentially with multiple facts, it continually becomes less editable, forgets previously edited facts and loses the ability to perform downstream tasks. For ROME and MEMIT, this “forgetting” happens in two phases - an initial gradual but progressive forgetting phase followed by an abrupt or catastrophic forgetting. Both gradual and catastrophic forgetting limit the usefulness of model editing methods at scale - the former makes model editing less effective as multiple edits are made to the model while the latter caps the scalability of such model editing methods. Our analysis also highlights other key limitations of ROME and MEMIT at scale. With our work, we push for better evaluation of model editing and development of model editing methods keeping scalability in mind.