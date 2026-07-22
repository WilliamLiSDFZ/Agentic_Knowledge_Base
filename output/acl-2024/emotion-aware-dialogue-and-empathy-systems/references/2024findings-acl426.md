---
title: "Modeling Emotional Trajectories in Written Stories Utilizing Transformers and Weakly-Supervised Learning"
source: "https://aclanthology.org/2024.findings-acl.426/"
pdf_url: ""
categories: ['emotion-aware-dialogue-and-empathy-systems', 'transformer-architecture-analysis-and-design']
tags: ['emotional-trajectories', 'story-analysis', 'weakly-supervised']
venue: "ACL 2024"
tldr: "A transformer-based weakly-supervised approach for automatically modeling emotional arcs in written narratives."
---

# Modeling Emotional Trajectories in Written Stories Utilizing Transformers and Weakly-Supervised Learning

**Source**: [https://aclanthology.org/2024.findings-acl.426/](https://aclanthology.org/2024.findings-acl.426/)

**TLDR**: A transformer-based weakly-supervised approach for automatically modeling emotional arcs in written narratives.

## Abstract

AbstractTelling stories is an integral part of human communication which can evoke emotions and influence the affective states of the audience. Automatically modeling emotional trajectories in stories has thus attracted considerable scholarly interest. However, as most existing works have been limited to unsupervised dictionary-based approaches, there is no benchmark for this task. We address this gap by introducing continuous valence and arousal labels for an existing dataset of children’s stories originally annotated with discrete emotion categories. We collect additional annotations for this data and map the categorical labels to the continuous valence and arousal space. For predicting the thus obtained emotionality signals, we fine-tune a DeBERTa model and improve upon this baseline via a weakly supervised learning approach. The best configuration achieves a Concordance Correlation Coefficient (CCC) of .8221 for valence and .7125 for arousal on the test set, demonstrating the efficacy of our proposed approach. A detailed analysis shows the extent to which the results vary depending on factors such as the author, the individual story, or the section within the story. In addition, we uncover the weaknesses of our approach by investigating examples that prove to be difficult to predict.