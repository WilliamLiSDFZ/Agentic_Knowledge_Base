---
title: "Fundus: A Simple-to-Use News Scraper Optimized for High Quality Extractions"
source: "https://aclanthology.org/2024.acl-demos.29/"
pdf_url: ""
categories: ['web-data-quality-and-llm-evaluation', 'natural-language-processing-information-extraction']
tags: ['news-scraping', 'data-collection', 'web-extraction']
venue: "ACL 2024"
tldr: "Fundus is a user-friendly news scraper using bespoke extractors that yields high-quality article extractions across many publishers."
---

# Fundus: A Simple-to-Use News Scraper Optimized for High Quality Extractions

**Source**: [https://aclanthology.org/2024.acl-demos.29/](https://aclanthology.org/2024.acl-demos.29/)

**TLDR**: Fundus is a user-friendly news scraper using bespoke extractors that yields high-quality article extractions across many publishers.

## Abstract

AbstractThis paper introduces Fundus, a user-friendly news scraper that enables users to obtain millions of high-quality news articles with just a few lines of code. Unlike existing news scrapers, we use manually crafted, bespoke content extractors that are specifically tailored to the formatting guidelines of each supported online newspaper. This allows us to optimize our scraping for quality such that retrieved news articles are textually complete and without HTML artifacts. Further, our framework combines both crawling (retrieving HTML from the web or large web archives) and content extraction into a single pipeline. By providing a unified interface for a predefined collection of newspapers, we aim to make Fundus broadly usable even for non-technical users. This paper gives an overview of the framework, discusses our design choices, and presents a comparative evaluation against other popular news scrapers. Our evaluation shows that Fundus yields significantly higher quality extractions (complete and artifact-free news articles) than prior work.The framework is available on GitHub under https://github.com/flairNLP/fundus and can be simply installed using pip.