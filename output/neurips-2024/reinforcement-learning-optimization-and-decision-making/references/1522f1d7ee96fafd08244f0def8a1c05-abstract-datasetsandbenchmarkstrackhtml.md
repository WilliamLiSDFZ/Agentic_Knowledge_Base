---
title: "Personalized Instance-based Navigation Toward User-Specific Objects in Realistic Environments"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1522f1d7ee96fafd08244f0def8a1c05-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'visual-language-multimodal-generation-reasoning']
tags: ['visual-navigation', 'personalized-navigation', 'instance-based-goals']
venue: "NeurIPS 2024"
tldr: "A personalized instance-based navigation system is proposed that guides agents toward user-specific objects in photo-realistic indoor environments."
---

# Personalized Instance-based Navigation Toward User-Specific Objects in Realistic Environments

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1522f1d7ee96fafd08244f0def8a1c05-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/1522f1d7ee96fafd08244f0def8a1c05-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A personalized instance-based navigation system is proposed that guides agents toward user-specific objects in photo-realistic indoor environments.

## Abstract

In the last years, the research interest in visual navigation towards objects in indoor environments has grown significantly. This growth can be attributed to the recent availability of large navigation datasets in photo-realistic simulated environments, like Gibson and Matterport3D. However, the navigation tasks supported by these datasets are often restricted to the objects present in the environment at acquisition time. Also, they fail to account for the realistic scenario in which the target object is a user-specific instance that can be easily confused with similar objects and may be found in multiple locations within the environment. To address these limitations, we propose a new task denominated Personalized Instance-based Navigation (PIN), in which an embodied agent is tasked with locating and reaching a specific personal object by distinguishing it among multiple instances of the same category. The task is accompanied by PInNED, a dedicated new dataset composed of photo-realistic scenes augmented with additional 3D objects. In each episode, the target object is presented to the agent using two modalities: a set of visual reference images on a neutral background and manually annotated textual descriptions. Through comprehensive evaluations and analyses, we showcase the challenges of the PIN task as well as the performance and shortcomings of currently available methods designed for object-driven navigation, considering modular and end-to-end agents.