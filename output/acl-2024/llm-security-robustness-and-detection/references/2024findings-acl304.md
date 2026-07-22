---
title: "Play Guessing Game with LLM: Indirect Jailbreak Attack with Implicit Clues"
source: "https://aclanthology.org/2024.findings-acl.304/"
categories: ['llm-security-robustness-and-detection']
tags: ['jailbreak', 'indirect-attack', 'LLM-security']
venue: "ACL 2024"
tldr: "This work proposes an indirect jailbreak attack on LLMs using implicit clues rather than explicit harmful content to bypass safety mechanisms."
---

# Play Guessing Game with LLM: Indirect Jailbreak Attack with Implicit Clues

**Source**: [https://aclanthology.org/2024.findings-acl.304/](https://aclanthology.org/2024.findings-acl.304/)

**TLDR**: This work proposes an indirect jailbreak attack on LLMs using implicit clues rather than explicit harmful content to bypass safety mechanisms.

## Abstract

AbstractWith the development of LLMs, the security threats of LLMs are getting more and more attention. Numerous jailbreak attacks have been proposed to assess the security defense of LLMs. Current jailbreak attacks primarily utilize scenario camouflage techniques. However their explicitly mention of malicious intent will be easily recognized and defended by LLMs. In this paper, we propose an indirect jailbreak attack approach, Puzzler, which can bypass the LLM’s defensive strategies and obtain malicious response by implicitly providing LLMs with some clues about the original malicious query. In addition, inspired by the wisdom of “When unable to attack, defend” from Sun Tzu’s Art of War, we adopt a defensive stance to gather clues about the original malicious query through LLMs. The experimental results indicate that the Query Success Rate of the Puzzler is 14.0%-82.7% higher than baselines on the most prominent LLMs. Furthermore, when tested against the state-of-the-art jailbreak detection approaches, Puzzler proves to be more effective at evading detection compared to baselines.