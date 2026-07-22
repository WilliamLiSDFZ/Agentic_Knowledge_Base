---
title: "Enhancing Adverse Drug Event Detection with Multimodal Dataset: Corpus Creation and Model Development"
source: "https://aclanthology.org/2024.findings-acl.667/"
pdf_url: ""
categories: ['llms-for-biomedical-and-clinical-nlp', 'multimodal-language-vision-learning-systems']
tags: ['adverse-drug-events', 'multimodal', 'pharmacovigilance', 'corpus', 'biomedical-NLP']
venue: "ACL 2024"
tldr: "This paper creates a multimodal dataset and develops models for improved adverse drug event detection to support pharmacovigilance."
---

# Enhancing Adverse Drug Event Detection with Multimodal Dataset: Corpus Creation and Model Development

**Source**: [https://aclanthology.org/2024.findings-acl.667/](https://aclanthology.org/2024.findings-acl.667/)

**TLDR**: This paper creates a multimodal dataset and develops models for improved adverse drug event detection to support pharmacovigilance.

## Abstract

AbstractThe mining of adverse drug events (ADEs) is pivotal in pharmacovigilance, enhancing patient safety by identifying potential risks associated with medications, facilitating early detection of adverse events, and guiding regulatory decision-making. Traditional ADE detection methods are reliable but slow, not easily adaptable to large-scale operations, and offer limited information. With the exponential increase in data sources like social media content, biomedical literature, and Electronic Medical Records (EMR), extracting relevant ADE-related information from these unstructured texts is imperative. Previous ADE mining studies have focused on text-based methodologies, overlooking visual cues, limiting contextual comprehension, and hindering accurate interpretation. To address this gap, we present a MultiModal Adverse Drug Event (MMADE) detection dataset, merging ADE-related textual information with visual aids. Additionally, we introduce a framework that leverages the capabilities of LLMs and VLMs for ADE detection by generating detailed descriptions of medical images depicting ADEs, aiding healthcare professionals in visually identifying adverse events. Using our MMADE dataset, we showcase the significance of integrating visual cues from images to enhance overall performance. This approach holds promise for patient safety, ADE awareness, and healthcare accessibility, paving the way for further exploration in personalized healthcare.