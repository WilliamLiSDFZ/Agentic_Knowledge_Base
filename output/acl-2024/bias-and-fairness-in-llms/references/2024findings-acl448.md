---
title: "Building Bridges: A Dataset for Evaluating Gender-Fair Machine Translation into German"
source: "https://aclanthology.org/2024.findings-acl.448/"
categories: ['bias-and-fairness-in-llms', 'language-technology-cultural-linguistic-diversity']
tags: ['gender-fair-language', 'machine-translation', 'german']
venue: "ACL 2024"
tldr: "Introduces a dataset for evaluating gender-fair translation of gender-neutral English terms into German."
---

# Building Bridges: A Dataset for Evaluating Gender-Fair Machine Translation into German

**Source**: [https://aclanthology.org/2024.findings-acl.448/](https://aclanthology.org/2024.findings-acl.448/)

**TLDR**: Introduces a dataset for evaluating gender-fair translation of gender-neutral English terms into German.

## Abstract

AbstractThe translation of gender-neutral person-referring terms (e.g.,the students) is often non-trivial.Translating from English into German poses an interesting case—in German, person-referring nouns are usually gender-specific, and if the gender of the referent(s) is unknown or diverse, the generic masculine (die Studenten (m.)) is commonly used. This solution, however, reduces the visibility of other genders, such as women and non-binary people. To counteract gender discrimination, a societal movement towards using gender-fair language exists (e.g., by adopting neosystems). However, gender-fair German is currently barely supported in machine translation (MT), requiring post-editing or manual translations. We address this research gap by studying gender-fair language in English-to-German MT. Concretely, we enrich a community-created gender-fair language dictionary and sample multi-sentence test instances from encyclopedic text and parliamentary speeches.Using these novel resources, we conduct the first benchmark study involving two commercial systems and six neural MT models for translating words in isolation and natural contexts across two domains. Our findings show that most systems produce mainly masculine forms and rarely gender-neutral variants, highlighting the need for future research. We release code and data at https://github.com/g8a9/building-bridges-gender-fair-german-mt.