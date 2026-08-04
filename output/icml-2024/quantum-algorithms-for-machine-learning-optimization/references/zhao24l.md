---
title: "Quantum Implicit Neural Representations"
source: "https://proceedings.mlr.press/v235/zhao24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhao24l/zhao24l.pdf"
categories: ['quantum-algorithms-for-machine-learning-optimization']
tags: ['quantum-neural-networks', 'implicit-representations', 'quantum-computing']
venue: "ICML 2024"
tldr: "This paper proposes quantum implicit neural representations that leverage quantum neural networks to parameterize implicit functions for signal representation tasks like images and sounds."
---

# Quantum Implicit Neural Representations

**Source**: [https://proceedings.mlr.press/v235/zhao24l.html](https://proceedings.mlr.press/v235/zhao24l.html)

**TLDR**: This paper proposes quantum implicit neural representations that leverage quantum neural networks to parameterize implicit functions for signal representation tasks like images and sounds.

## Abstract

Implicit neural representations have emerged as a powerful paradigm to represent signals such as images and sounds. This approach aims to utilize neural networks to parameterize the implicit function of the signal. However, when representing implicit functions, traditional neural networks such as ReLU-based multilayer perceptrons face challenges in accurately modeling high-frequency components of signals. Recent research has begun to explore the use of Fourier Neural Networks (FNNs) to overcome this limitation. In this paper, we propose Quantum Implicit Representation Network (QIREN), a novel quantum generalization of FNNs. Furthermore, through theoretical analysis, we demonstrate that QIREN possesses a quantum advantage over classical FNNs. Lastly, we conducted experiments in signal representation, image superresolution, and image generation tasks to show the superior performance of QIREN compared to state-of-the-art (SOTA) models. Our work not only incorporates quantum advantages into implicit neural representations but also uncovers a promising application direction for Quantum Neural Networks.