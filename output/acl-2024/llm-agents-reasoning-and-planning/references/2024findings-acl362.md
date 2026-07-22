---
title: "GeoAgent: To Empower LLMs using Geospatial Tools for Address Standardization"
source: "https://aclanthology.org/2024.findings-acl.362/"
categories: ['llm-based-geospatial-text-processing', 'llm-agents-reasoning-and-planning']
tags: ['address-standardization', 'geospatial-tools', 'LLM-agents']
venue: "ACL 2024"
tldr: "GeoAgent leverages LLMs with geospatial tools to standardize non-standard user-input addresses in modern applications."
---

# GeoAgent: To Empower LLMs using Geospatial Tools for Address Standardization

**Source**: [https://aclanthology.org/2024.findings-acl.362/](https://aclanthology.org/2024.findings-acl.362/)

**TLDR**: GeoAgent leverages LLMs with geospatial tools to standardize non-standard user-input addresses in modern applications.

## Abstract

AbstractThis paper presents a novel solution to tackle the challenges that posed by the abundance of non-standard addresses, which input by users in modern applications such as navigation maps, ride-hailing apps, food delivery platforms, and logistics services. These manually entered addresses often contain irregularities, such as missing information, spelling errors, colloquial descriptions, and directional offsets, which hinder address-related tasks like address matching and linking. To tackle these challenges, we propose GeoAgent, a new framework comprising two main components: a large language model (LLM) and a suite of geographical tools. By harnessing the semantic understanding capabilities of the LLM and integrating specific geospatial tools, GeoAgent incorporates spatial knowledge into address texts and achieves efficient address standardization. Further, to verify the effectiveness and practicality of our approach, we construct a comprehensive dataset of complex non-standard addresses, which fills the gaps in existing datasets and proves invaluable for training and evaluating the performance of address standardization models in this community. Experimental results demonstrate the efficacy of GeoAgent, showcasing substantial improvements in the performance of address-related models across various downstream tasks.