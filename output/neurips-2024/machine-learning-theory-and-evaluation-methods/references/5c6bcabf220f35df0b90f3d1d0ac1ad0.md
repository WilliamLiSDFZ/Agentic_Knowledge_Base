---
title: "Active Classification with Few Queries under Misspecification"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/5c6bcabf220f35df0b90f3d1d0ac1ad0-Abstract-Conference.html"
categories: ['query-efficient-algorithms-with-imperfect-oracles', 'machine-learning-theory-and-evaluation-methods']
tags: ['active-learning', 'pool-based', 'misspecification']
venue: "NeurIPS 2024"
tldr: "Studies pool-based active classification with few queries under model misspecification to competitively label examples from a given hypothesis class."
---

# Active Classification with Few Queries under Misspecification

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/5c6bcabf220f35df0b90f3d1d0ac1ad0-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/5c6bcabf220f35df0b90f3d1d0ac1ad0-Abstract-Conference.html)

**TLDR**: Studies pool-based active classification with few queries under model misspecification to competitively label examples from a given hypothesis class.

## Abstract

We study pool-based active learning, where a learner has a large pool $S$ of unlabeled examples and can adaptively ask a labeler questions to learn these labels. The goal of the learner is to output a labeling for $S$ that can compete with the best hypothesis from a given hypothesis class $\mathcal{H}$. We focus on halfspace learning, one of the most important problems in active learning.It is well known that in the standard active learning model, learning the labels of an arbitrary pool of examples labeled by some halfspace up to error $\epsilon$ requires at least $\Omega(1/\epsilon)$ queries. To overcome this difficulty, previous work designs simple but powerful query languages to achieve $O(\log(1/\epsilon))$ query complexity, but only focuses on the realizable setting where data are perfectly labeled by some halfspace.However, when labels are noisy, such queries are too fragile and lead to high query complexity even under the simple random classification noise model.  In this work, we propose a new query language called threshold statistical queries and study their power for learning under various noise models. Our main algorithmic result is the first query-efficient algorithm for learning halfspaces under the popular Massart noise model. With an arbitrary dataset corrupted with Massart noise at noise rate $\eta$, our algorithm uses only $\mathrm{polylog(1/\epsilon)}$ threshold statistical queries and computes an $(\eta + \epsilon)$-accurate labeling in polynomial time. For the harder case of agnostic noise, we show that it is impossible to beat $O(1/\epsilon)$ query complexity even for the much simpler problem of learning singleton functions (and thus for learning halfspaces) using a reduction from agnostic distributed learning.