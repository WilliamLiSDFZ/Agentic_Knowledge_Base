---
title: "Cooperation, Competition, and Maliciousness: LLM-Stakeholders Interactive Negotiation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/984dd3db213db2d1454a163b65b84d08-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-agent-communication-and-cooperation', 'llm-values-ethics-alignment-evaluation']
tags: ['llm-negotiation', 'multi-agent-systems', 'cooperation']
venue: "NeurIPS 2024"
tldr: "Studies LLM communication and decision-making in multi-stakeholder negotiation scenarios involving cooperation, competition, and malicious agents."
---

# Cooperation, Competition, and Maliciousness: LLM-Stakeholders Interactive Negotiation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/984dd3db213db2d1454a163b65b84d08-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/984dd3db213db2d1454a163b65b84d08-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Studies LLM communication and decision-making in multi-stakeholder negotiation scenarios involving cooperation, competition, and malicious agents.

## Abstract

There is a growing interest in using Large Language Models (LLMs) in multi-agent systems to tackle interactive real-world tasks that require effective collaboration and assessing complex situations. Yet, we have a limited understanding of LLMs' communication and decision-making abilities in multi-agent setups. The fundamental task of negotiation spans many key features of communication, such as cooperation, competition, and manipulation potentials. Thus, we propose using scorable negotiation to evaluate LLMs. We create a testbed of complex multi-agent, multi-issue, and semantically rich negotiation games. To reach an agreement, agents must have strong arithmetic, inference, exploration, and planning capabilities while integrating them in a dynamic and multi-turn setup. We propose metrics to rigorously quantify agents' performance and alignment with the assigned role. We provide procedures to create new games and increase games' difficulty to have an evolving benchmark. Importantly, we evaluate critical safety aspects such as the interaction dynamics between agents influenced by greedy and adversarial players. Our benchmark is highly challenging; GPT-3.5 and small models mostly fail, and GPT-4 and SoTA large models (e.g., Llama-3 70b) still underperform in reaching agreement in non-cooperative and more difficult games.