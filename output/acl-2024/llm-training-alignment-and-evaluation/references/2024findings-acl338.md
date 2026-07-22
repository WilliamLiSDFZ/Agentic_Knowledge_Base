---
title: "Improving Large Language Models via Fine-grained Reinforcement Learning with Minimum Editing Constraint"
source: "https://aclanthology.org/2024.findings-acl.338/"
categories: ['llm-training-alignment-and-evaluation', 'speech-and-language-multimodal-generation-systems']
tags: ['reinforcement-learning', 'fine-grained-reward', 'minimum-editing']
venue: "ACL 2024"
tldr: "Introduces token-level RL with minimum editing constraints to provide fine-grained supervision for improving LLM reasoning and reducing harmful outputs."
---

# Improving Large Language Models via Fine-grained Reinforcement Learning with Minimum Editing Constraint

**Source**: [https://aclanthology.org/2024.findings-acl.338/](https://aclanthology.org/2024.findings-acl.338/)

**TLDR**: Introduces token-level RL with minimum editing constraints to provide fine-grained supervision for improving LLM reasoning and reducing harmful outputs.

## Abstract

AbstractReinforcement learning (RL) has been widely used in training large language models (LLMs) for preventing unexpected outputs, e.g., reducing harmfulness and errors. However, existing RL methods mainly adopt instance-level reward, which cannot provide fine-grained supervision for complex reasoning tasks. As a result, the RL training cannot be fully aware of the specific part or step that actually leads to the incorrectness in model response. To address it, we propose a new RL method named RLMEC that incorporates a generative model as the reward model, which is trained by the erroneous solution rewriting task under the minimum editing constraint, which can produce token-level supervision for RL training. Based 0on the generative reward model, we design the token-level RL objective for training and an imitation-based regularization for stabilizing RL process. And these two objectives focus on the revision of the key tokens for the erroneous solution, reducing the effect of other unimportant tokens. Experiment results on 8 tasks have demonstrated the effectiveness of our approach. Our code and data will be publicly released.