---
title: "Reinforcement Learning from Reachability Specifications: PAC Guarantees with Expected Conditional Distance"
source: "https://proceedings.mlr.press/v235/svoboda24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/svoboda24a/svoboda24a.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['reinforcement-learning', 'reachability', 'PAC-learning']
venue: "ICML 2024"
tldr: "PAC guarantees with expected conditional distance are established for RL from reachability specifications using temporal logic."
---

# Reinforcement Learning from Reachability Specifications: PAC Guarantees with Expected Conditional Distance

**Source**: [https://proceedings.mlr.press/v235/svoboda24a.html](https://proceedings.mlr.press/v235/svoboda24a.html)

**TLDR**: PAC guarantees with expected conditional distance are established for RL from reachability specifications using temporal logic.

## Abstract

Reinforcement Learning (RL) from temporal logical specifications is a fundamental problem in sequential decision making. One of the basic and core such specification is the reachability specification that requires a target set to be eventually visited. Despite strong empirical results for RL from such specifications, the theoretical guarantees are bleak, including the impossibility of Probably Approximately Correct (PAC) guarantee for reachability specifications. Given the impossibility result, in this work we consider the problem of RL from reachability specifications along with the information of expected conditional distance (ECD). We present (a) lower bound results which establish the necessity of ECD information for PAC guarantees and (b) an algorithm that establishes PAC-guarantees given the ECD information. To the best of our knowledge, this is the first RL from reachability specifications that does not make any assumptions on the underlying environment to learn policies.