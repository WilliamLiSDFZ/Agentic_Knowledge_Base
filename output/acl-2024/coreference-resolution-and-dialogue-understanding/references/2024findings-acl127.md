---
title: "Context-Aware Tracking and Dynamic Introduction for Incomplete Utterance Rewriting in Extended Multi-Turn Dialogues"
source: "https://aclanthology.org/2024.findings-acl.127/"
categories: ['coreference-resolution-and-dialogue-understanding', 'nlp-for-asian-languages']
tags: ['utterance-rewriting', 'dialogue', 'coreference']
venue: "ACL 2024"
tldr: "Proposes context-aware tracking and dynamic introduction for incomplete utterance rewriting in extended multi-turn dialogues."
---

# Context-Aware Tracking and Dynamic Introduction for Incomplete Utterance Rewriting in Extended Multi-Turn Dialogues

**Source**: [https://aclanthology.org/2024.findings-acl.127/](https://aclanthology.org/2024.findings-acl.127/)

**TLDR**: Proposes context-aware tracking and dynamic introduction for incomplete utterance rewriting in extended multi-turn dialogues.

## Abstract

AbstractIncomplete utterance rewriting (IUR) aims to reconstruct the utterance with omitted information and pronouns to be standalone and complete based on the context. The existing works predominantly focus on simple ellipsis and coreference problems in brief multi-turn dialogues. But in actual scenarios: 1) the context of the dialogues frequently comprises multiple similar candidates for ellipsis and coreference resolution, pouring to confuse. 2) the number of turns tends to be more extensive, while the content with various topics also grows more complex. This paper proposes a novel method called CaT to address these issues. In particular, we first devise a tacker model, distilled from GPT4-turbo, to adopt Context Tracking that dynamically updates a list of key phrases turn by turn, as accurate candidates for ellipsis and coreference resolution. Second, we further present the Dynamic Context Introduction mechanism to filter irrelevant preceding contexts that are not relied on by any element within the key phrase list to condense extended dialogues. Comprehensive experiments indicate that our solution provides a significant improvement over the existing baselines, and achieves state-of-the-art on three benchmarks.