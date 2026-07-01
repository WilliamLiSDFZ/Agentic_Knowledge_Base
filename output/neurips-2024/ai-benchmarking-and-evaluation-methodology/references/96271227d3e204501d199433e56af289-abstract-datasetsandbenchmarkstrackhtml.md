---
title: "UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/96271227d3e204501d199433e56af289-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'visual-language-multimodal-generation-reasoning']
tags: ['vision-language-models', 'benchmarking', 'visual-reasoning']
venue: "NeurIPS 2024"
tldr: "Presents UniBench, a unified evaluation framework revealing that scaling alone is insufficient for robust visual reasoning in VLMs."
---

# UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/96271227d3e204501d199433e56af289-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/96271227d3e204501d199433e56af289-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents UniBench, a unified evaluation framework revealing that scaling alone is insufficient for robust visual reasoning in VLMs.

## Abstract

Significant research efforts have been made to scale and improve vision-language model (VLM) training approaches. Yet, with an ever-growing number of benchmarks,researchers are tasked with the heavy burden of implementing each protocol, bearing a non-trivial computational cost, and making sense of how all these benchmarks translate into meaningful axes of progress.To facilitate a systematic evaluation of VLM progress, we introduce UniBench: a unified implementation of 50+ VLM benchmarks spanning a range of carefully categorized vision-centric capabilities from object recognition to spatial awareness, counting, and much more. We showcase the utility of UniBench for measuring progress by evaluating nearly 60 publicly available vision-language models, trained on scales of up to 12.8B samples. We find that while scaling training data or model size can boost many vision-language model capabilities, scaling offers little benefit for reasoning or relations.  Surprisingly, we also discover today's best VLMs struggle on simple digit recognition and counting tasks, e.g. MNIST, which much simpler networks can solve. Where scale falls short, we find that more precise interventions, such as data quality or tailored-learning objectives offer more promise. For practitioners, we also offer guidance on selecting a suitable VLM for a given application. Finally, we release an easy-to-run UniBench code-base with the full set of 50+ benchmarks and comparisons across 59 models as well as a distilled, representative set of benchmarks that runs in 5 minutes on a single GPU. UniBench with model evaluations on all benchmarks are provided as a toolbox at: https://github.com/facebookresearch/unibench