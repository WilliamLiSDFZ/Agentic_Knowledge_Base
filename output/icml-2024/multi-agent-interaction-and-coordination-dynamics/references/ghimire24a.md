---
title: "State-Constrained Zero-Sum Differential Games with One-Sided Information"
source: "https://proceedings.mlr.press/v235/ghimire24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ghimire24a/ghimire24a.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics', 'multi-agent-mdp-structure-and-dependencies']
tags: ['differential-games', 'state-constraints', 'one-sided-information']
venue: "ICML 2024"
tldr: "Studies zero-sum differential games with state constraints and one-sided information, characterizing equilibrium strategies for the informed player."
---

# State-Constrained Zero-Sum Differential Games with One-Sided Information

**Source**: [https://proceedings.mlr.press/v235/ghimire24a.html](https://proceedings.mlr.press/v235/ghimire24a.html)

**TLDR**: Studies zero-sum differential games with state constraints and one-sided information, characterizing equilibrium strategies for the informed player.

## Abstract

We study zero-sum differential games with state constraints and one-sided information, where the informed player (Player 1) has a categorical payoff type unknown to the uninformed player (Player 2). The goal of Player 1 is to minimize his payoff without violating the constraints, while that of Player 2 is to violate the state constraints if possible, or to maximize the payoff otherwise. One example of the game is a man-to-man matchup in football. Without state constraints, Cardaliaguet (2007) showed that the value of such a game exists and is convex to the common belief of players. Our theoretical contribution is an extension of this result to games with state constraints and the derivation of the primal and dual subdynamic principles necessary for computing behavioral strategies. Different from existing works that are concerned about the scalability of no-regret learning in games with discrete dynamics, our study reveals the underlying structure of strategies for belief manipulation resulting from information asymmetry and state constraints. This structure will be necessary for scalable learning on games with continuous actions and long time windows. We use a simplified football game to demonstrate the utility of this work, where we reveal player positions and belief states in which the attacker should (or should not) play specific random deceptive moves to take advantage of information asymmetry, and compute how the defender should respond.