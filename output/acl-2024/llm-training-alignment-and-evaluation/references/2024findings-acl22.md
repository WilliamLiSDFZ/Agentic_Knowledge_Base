---
title: "ASPIRE: Language-Guided Data Augmentation for Improving Robustness Against Spurious Correlations"
source: "https://aclanthology.org/2024.findings-acl.22/"
categories: ['multimodal-language-vision-learning-systems', 'llm-training-alignment-and-evaluation']
tags: ['data-augmentation', 'spurious-correlations', 'robustness', 'image-classification', 'language-guided']
venue: "ACL 2024"
tldr: "Proposes a language-guided data augmentation method to improve neural image classifier robustness against spurious feature correlations."
---

# ASPIRE: Language-Guided Data Augmentation for Improving Robustness Against Spurious Correlations

**Source**: [https://aclanthology.org/2024.findings-acl.22/](https://aclanthology.org/2024.findings-acl.22/)

**TLDR**: Proposes a language-guided data augmentation method to improve neural image classifier robustness against spurious feature correlations.

## Abstract

AbstractNeural image classifiers can often learn to make predictions by overly relying on non-predictive features that are spuriously correlated with the class labels in the training data. This leads to poor performance in real-world atypical scenarios where such features are absent. This paper presents ASPIRE (Language-guided Data Augmentation for SPurIous correlation REmoval), a simple yet effective solution for supplementing the training dataset with images without spurious features, for robust learning against spurious correlations via better generalization. ASPIRE, guided by language at various steps, can generate non-spurious images without requiring any group labeling or existing non-spurious images in the training set. Precisely, we employ LLMs to first extract foreground and background features from textual descriptions of an image, followed by advanced language-guided image editing to discover the features that are spuriously correlated with the class label. Finally, we personalize a text-to-image generation model using the edited images to generate diverse in-domain images without spurious features. ASPIRE is complementary to all prior robust training methods in literature, and we demonstrate its effectiveness across 4 datasets and 9 baselines and show that ASPIRE improves the worst-group classification accuracy of prior methods by 1% - 38%. We also contribute a novel test set for the challenging Hard ImageNet dataset.