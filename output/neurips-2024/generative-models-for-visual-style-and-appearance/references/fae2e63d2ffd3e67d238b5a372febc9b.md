---
title: "Novel Object Synthesis via Adaptive Text-Image Harmony"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/fae2e63d2ffd3e67d238b5a372febc9b-Abstract-Conference.html"
categories: ['generative-models-for-visual-style-and-appearance']
tags: ['object-synthesis', 'text-image-harmony', 'diffusion-models', 'adaptive-generation']
venue: "NeurIPS 2024"
tldr: "Proposes an adaptive text-image harmony method for novel object synthesis that balances contributions from text and image inputs in diffusion models."
---

# Novel Object Synthesis via Adaptive Text-Image Harmony

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/fae2e63d2ffd3e67d238b5a372febc9b-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/fae2e63d2ffd3e67d238b5a372febc9b-Abstract-Conference.html)

**TLDR**: Proposes an adaptive text-image harmony method for novel object synthesis that balances contributions from text and image inputs in diffusion models.

## Abstract

In this paper, we study an object synthesis task that combines an object text with an object image to create a new object image. However, most diffusion models struggle with this task, \textit{i.e.}, often generating an object that predominantly reflects either the text or the image due to an imbalance between their inputs. To address this issue, we propose a simple yet effective method called Adaptive Text-Image Harmony (ATIH) to generate novel and surprising objects.First, we introduce a scale factor and an injection step to balance text and image features in cross-attention and to preserve image information in self-attention during the text-image inversion diffusion process, respectively. Second, to better integrate object text and image, we design a balanced loss function with a noise parameter, ensuring both optimal editability and fidelity of the object image. Third, to adaptively adjust these parameters, we present a novel similarity score function that not only maximizes the similarities between the generated object image and the input text/image but also balances these similarities to harmonize text and image integration.  Extensive experiments demonstrate the effectiveness of our approach, showcasing remarkable object creations such as colobus-glass jar. https://xzr52.github.io/ATIH/