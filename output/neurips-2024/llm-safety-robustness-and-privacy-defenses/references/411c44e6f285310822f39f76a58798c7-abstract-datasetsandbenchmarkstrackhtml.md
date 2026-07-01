---
title: "Dataset and Lessons Learned from the 2024 SaTML LLM Capture-the-Flag Competition"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/411c44e6f285310822f39f76a58798c7-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-safety-robustness-and-privacy-defenses', 'ai-benchmarking-and-evaluation-methodology']
tags: ['llm-security', 'prompt-injection', 'capture-the-flag']
venue: "NeurIPS 2024"
tldr: "A capture-the-flag competition dataset and lessons learned are presented for studying LLM prompt injection and data leakage attacks."
---

# Dataset and Lessons Learned from the 2024 SaTML LLM Capture-the-Flag Competition

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/411c44e6f285310822f39f76a58798c7-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/411c44e6f285310822f39f76a58798c7-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A capture-the-flag competition dataset and lessons learned are presented for studying LLM prompt injection and data leakage attacks.

## Abstract

Large language model systems face significant security risks from maliciously crafted messages that aim to overwrite the system's original instructions or leak private data. To study this problem, we organized a capture-the-flag competition at IEEE SaTML 2024, where the flag is a secret string in the LLM system prompt. The competition was organized in two phases. In the first phase, teams developed defenses to prevent the model from leaking the secret. During the second phase, teams were challenged to extract the secrets hidden for defenses proposed by the other teams. This report summarizes the main insights from the competition. Notably, we found that all defenses were bypassed at least once, highlighting the difficulty of designing a successful defense and the necessity for additional research to protect LLM systems. To foster future research in this direction, we compiled a dataset with over 137k multi-turn attack chats and open-sourced the platform.