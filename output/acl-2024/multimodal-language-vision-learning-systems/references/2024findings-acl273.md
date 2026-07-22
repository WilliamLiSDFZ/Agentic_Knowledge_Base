---
title: "Tell Me What’s Next: Textual Foresight for Generic UI Representations"
source: "https://aclanthology.org/2024.findings-acl.273/"
categories: ['multimodal-language-vision-learning-systems', 'document-understanding-and-information-extraction']
tags: ['UI-representation', 'textual-foresight', 'mobile-apps']
venue: "ACL 2024"
tldr: "Proposes textual foresight as a self-supervised objective for learning generic representations of mobile UI elements."
---

# Tell Me What’s Next: Textual Foresight for Generic UI Representations

**Source**: [https://aclanthology.org/2024.findings-acl.273/](https://aclanthology.org/2024.findings-acl.273/)

**TLDR**: Proposes textual foresight as a self-supervised objective for learning generic representations of mobile UI elements.

## Abstract

AbstractMobile app user interfaces (UIs) are rich with action, text, structure, and image content that can be utilized to learn generic UI representations for tasks like automating user commands, summarizing content, and evaluating the accessibility of user interfaces. Prior work has learned strong visual representations with local or global captioning losses, but fails to retain both granularities.To combat this, we propose Textual Foresight, a novel pretraining objective for learning UI screen representations. Textual Foresight generates global text descriptions of future UI states given a current UI and local action taken. Our approach requires joint reasoning over elements and entire screens, resulting in improved UI features: on generation tasks, UI agents trained with Textual Foresight outperform state-of-the-art by 2% with 28x fewer images. We train with our newly constructed mobile app dataset, OpenApp, which results in the first public dataset for app UI representation learning. OpenApp enables new baselines, and we find Textual Foresight improves average task performance over them by 5.7% while having access to 2x less data.