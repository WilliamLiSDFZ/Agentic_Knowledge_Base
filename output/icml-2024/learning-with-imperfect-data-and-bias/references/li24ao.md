---
title: "Enhancing Class-Imbalanced Learning with Pre-Trained Guidance through Class-Conditional Knowledge Distillation"
source: "https://proceedings.mlr.press/v235/li24ao.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24ao/li24ao.pdf"
categories: ['knowledge-distillation-methods-and-applications', 'learning-with-imperfect-data-and-bias']
tags: ['class-imbalance', 'knowledge-distillation', 'pre-trained-models', 'minority-class', 'long-tail']
venue: "ICML 2024"
tldr: "Class-conditional knowledge distillation from pre-trained models improves generalization for minority classes in imbalanced learning."
---

# Enhancing Class-Imbalanced Learning with Pre-Trained Guidance through Class-Conditional Knowledge Distillation

**Source**: [https://proceedings.mlr.press/v235/li24ao.html](https://proceedings.mlr.press/v235/li24ao.html)

**TLDR**: Class-conditional knowledge distillation from pre-trained models improves generalization for minority classes in imbalanced learning.

## Abstract

In class-imbalanced learning, the scarcity of information about minority classes presents challenges in obtaining generalizable features for these classes. Leveraging large-scale pre-trained models with powerful generalization capabilities as teacher models can help fill this information gap. Traditional knowledge distillation transfers the label distribution $p(\boldsymbol{y}|\boldsymbol{x})$ predicted by the teacher model to the student model. However, this method falls short on imbalanced data as it fails to capture the class-conditional probability distribution $p(\boldsymbol{x}|\boldsymbol{y})$ from the teacher model, which is crucial for enhancing generalization. To overcome this, we propose Class-Conditional Knowledge Distillation (CCKD), a novel approach that enables learning of the teacher model’s class-conditional probability distribution during the distillation process. Additionally, we introduce Augmented CCKD (ACCKD), which involves distillation on a constructed class-balanced dataset (formed through data mixing) and feature imitation on the entire dataset to further facilitate the learning of features. Experimental results on various imbalanced datasets demonstrate an average accuracy improvement of 7.4% using our method.