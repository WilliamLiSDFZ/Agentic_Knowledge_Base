---
title: "Improving Low-Resource Machine Translation for Formosan Languages Using Bilingual Lexical Resources"
source: "https://aclanthology.org/2024.findings-acl.670/"
pdf_url: ""
categories: ['language-technology-cultural-linguistic-diversity', 'nlp-for-asian-languages']
tags: ['low-resource-mt', 'formosan-languages', 'bilingual-lexicon', 'endangered-languages', 'mandarin']
venue: "ACL 2024"
tldr: "Incorporates bilingual lexical resources during training to improve machine translation for critically endangered Formosan languages."
---

# Improving Low-Resource Machine Translation for Formosan Languages Using Bilingual Lexical Resources

**Source**: [https://aclanthology.org/2024.findings-acl.670/](https://aclanthology.org/2024.findings-acl.670/)

**TLDR**: Incorporates bilingual lexical resources during training to improve machine translation for critically endangered Formosan languages.

## Abstract

AbstractThis paper investigates how machine translation for low-resource languages can be improved by incorporating information from bilingual lexicons during the training process for mainly translation between Mandarin and Formosan languages, which are all moribund or critically endangered, and we also show that our techniques work for translation between Spanish and Nahuatl, a language pair consisting of languages from completely different language families. About 70% of the approximately 7,000 languages of the world have data in the form of lexicons, a valuable resource for improving low-resource language translation. We collect a dataset of parallel data and bilingual lexicons between Mandarin and 16 different Formosan languages and examine mainly three different approaches: (1) simply using lexical data as additional parallel data, (2) generating pseudo-parallel sentence data to use during training by replacing words in the original parallel sentence data using the lexicon, and (3) a combination of (1) and (2). All three approaches give us gains in both Bleu scores and chrF scores, and we found that (3) provided the most gains, followed by (1) and then (2), which we observed for both translation between Mandarin and the Formosan languages and Spanish-Nahuatl. With technique (3), we saw an average increase of 5.55 in Bleu scores and 10.33 in chrF scores.