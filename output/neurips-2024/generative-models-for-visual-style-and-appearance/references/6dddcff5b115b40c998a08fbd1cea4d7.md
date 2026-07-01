---
title: "Breaking Semantic Artifacts for Generalized AI-generated Image Detection"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/6dddcff5b115b40c998a08fbd1cea4d7-Abstract-Conference.html"
categories: ['generative-models-for-visual-style-and-appearance']
tags: ['ai-generated-image-detection', 'generalization', 'semantic-artifacts', 'forgery-detection']
venue: "NeurIPS 2024"
tldr: "A method to break semantic artifacts in AI-generated images to improve generalized detection across different generators and image scenes."
---

# Breaking Semantic Artifacts for Generalized AI-generated Image Detection

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/6dddcff5b115b40c998a08fbd1cea4d7-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/6dddcff5b115b40c998a08fbd1cea4d7-Abstract-Conference.html)

**TLDR**: A method to break semantic artifacts in AI-generated images to improve generalized detection across different generators and image scenes.

## Abstract

With the continuous evolution of AI-generated images, the generalized detection of them has become a crucial aspect of AI security. Existing detectors have focused on cross-generator generalization, while it remains unexplored whether these detectors can generalize across different image scenes, e.g., images from different datasets with different semantics. In this paper, we reveal that existing detectors suffer from substantial Accuracy drops in such cross-scene generalization. In particular, we attribute their failures to ''semantic artifacts'' in both real and generated images, to which detectors may overfit. To break such ''semantic artifacts'', we propose a simple yet effective approach based on conducting an image patch shuffle and then training an end-to-end patch-based classifier. We conduct a comprehensive open-world evaluation on 31 test sets, covering 7 Generative Adversarial Networks, 18 (variants of) Diffusion Models, and another 6 CNN-based generative models. The results demonstrate that our approach outperforms previous approaches by 2.08\% (absolute) on average regarding cross-scene detection Accuracy. We also notice the superiority of our approach in open-world generalization, with an average Accuracy improvement of 10.59\% (absolute) across all test sets. Our code is available at https://github.com/Zig-HS/FakeImageDetection.