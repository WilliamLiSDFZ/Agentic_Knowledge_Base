---
title: "Budget-Constrained Tool Learning with Planning"
source: "https://aclanthology.org/2024.findings-acl.536/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'llm-training-alignment-and-evaluation']
tags: ['tool-learning', 'budget-constraint', 'planning']
venue: "ACL 2024"
tldr: "A novel budget-constrained tool learning method that uses planning to resolve user queries within specified cost limits."
---

# Budget-Constrained Tool Learning with Planning

**Source**: [https://aclanthology.org/2024.findings-acl.536/](https://aclanthology.org/2024.findings-acl.536/)

**TLDR**: A novel budget-constrained tool learning method that uses planning to resolve user queries within specified cost limits.

## Abstract

AbstractDespite intensive efforts devoted to tool learning, the problem of budget-constrained tool learning, which focuses on resolving user queries within a specific budget constraint, has been widely overlooked. This paper proposes a novel method for budget-constrained tool learning. Our approach involves creating a preferable plan under the budget constraint before utilizing the tools. This plan outlines the feasible tools and the maximum number of times they can be employed, offering a comprehensive overview of the tool learning process for large language models. This allows them to allocate the budget from a broader perspective. To devise the plan without incurring significant extra costs, we suggest initially estimating the usefulness of the candidate tools based on past experience. Subsequently, we employ dynamic programming to formulate the plan. Experimental results demonstrate that our method can be integrated with various tool learning methods, significantly enhancing their effectiveness under strict budget constraints.