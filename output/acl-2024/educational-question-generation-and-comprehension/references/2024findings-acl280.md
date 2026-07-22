---
title: "Planning First, Question Second: An LLM-Guided Method for Controllable Question Generation"
source: "https://aclanthology.org/2024.findings-acl.280/"
pdf_url: ""
categories: ['educational-question-generation-and-comprehension', 'llm-agents-reasoning-and-planning']
tags: ['question-generation', 'controllable-generation', 'LLM', 'education', 'planning']
venue: "ACL 2024"
tldr: "An LLM-guided method that plans question structure before generation to enable controllable educational question generation beyond difficulty."
---

# Planning First, Question Second: An LLM-Guided Method for Controllable Question Generation

**Source**: [https://aclanthology.org/2024.findings-acl.280/](https://aclanthology.org/2024.findings-acl.280/)

**TLDR**: An LLM-guided method that plans question structure before generation to enable controllable educational question generation beyond difficulty.

## Abstract

AbstractIn the field of education, for better assessment of students’ abilities, generated questions often need to meet experts’ requirements, indicating the need for controllable question generation (CQG). However, current CQG methods mainly focus on difficulty control, neglecting the control of question content and assessed abilities, which are also crucial in educational QG. In this paper, we propose an LLM-guided method PFQS (for Planning First, Question Second), which utilizes Llama 2 to generate an answer plan and then generates questions based on it. The plan not only includes candidate answers but also integrates LLM’s understanding and multiple requirements, which make question generation simple and controllable. We evaluate our approach on the FairytaleQA dataset, a well-structured QA dataset derived from child-friendly storybooks. In the dataset, the attribute label represents content control, while the local_or_sum and ex_or_im labels denote difficulty control. Experimental results demonstrate that our approach outperforms previous state-of-the-art results and achieves better consistency with requirements compared to prompt-based method. Further application of our method to Llama 2 and Mistral also leads to improved requirement consistency in a zero-shot setting.