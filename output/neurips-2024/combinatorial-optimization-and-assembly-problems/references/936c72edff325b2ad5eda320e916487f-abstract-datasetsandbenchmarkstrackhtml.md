---
title: "IKEA Manuals at Work: 4D Grounding of Assembly Instructions on Internet Videos"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/936c72edff325b2ad5eda320e916487f-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['combinatorial-optimization-and-assembly-problems']
tags: ['shape-assembly', '4D-grounding', 'IKEA', 'instruction-following', 'video-understanding']
venue: "NeurIPS 2024"
tldr: "A new dataset and benchmark is introduced for 4D grounding of IKEA assembly instructions in internet videos to advance autonomous assembly agents."
---

# IKEA Manuals at Work: 4D Grounding of Assembly Instructions on Internet Videos

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/936c72edff325b2ad5eda320e916487f-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/936c72edff325b2ad5eda320e916487f-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A new dataset and benchmark is introduced for 4D grounding of IKEA assembly instructions in internet videos to advance autonomous assembly agents.

## Abstract

Shape assembly is a ubiquitous task in daily life, integral for constructing complex 3D structures like IKEA furniture. While significant progress has been made in developing autonomous agents for shape assembly, existing datasets have not yet tackled the 4D grounding of assembly instructions in videos, essential for a holistic understanding of assembly in 3D space over time. We introduce IKEA Video Manuals, a dataset that features 3D models of furniture parts, instructional manuals, assembly videos from the Internet, and most importantly, annotations of dense spatio-temporal alignments between these data modalities. To demonstrate the utility of IKEA Video Manuals, we present five applications essential for shape assembly: assembly plan generation, part-conditioned segmentation, part-conditioned pose estimation, video object segmentation, and furniture assembly based on instructional video manuals. For each application, we provide evaluation metrics and baseline methods. Through experiments on our annotated data, we highlight many challenges in grounding assembly instructions in videos to improve shape assembly, including handling occlusions, varying viewpoints, and extended assembly sequences.