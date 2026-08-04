---
title: "Harmonic Self-Conditioned Flow Matching for joint Multi-Ligand Docking and Binding Site Design"
source: "https://proceedings.mlr.press/v235/stark24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/stark24a/stark24a.pdf"
categories: ['generative-models-for-molecular-protein-design', 'generative-models-and-variational-inference']
tags: ['molecular-docking', 'binding-site-design', 'flow-matching', 'multi-ligand']
venue: "ICML 2024"
tldr: "HarmonicFlow is proposed for joint multi-ligand docking and binding site design using harmonic self-conditioned flow matching over protein-ligand structures."
---

# Harmonic Self-Conditioned Flow Matching for joint Multi-Ligand Docking and Binding Site Design

**Source**: [https://proceedings.mlr.press/v235/stark24a.html](https://proceedings.mlr.press/v235/stark24a.html)

**TLDR**: HarmonicFlow is proposed for joint multi-ligand docking and binding site design using harmonic self-conditioned flow matching over protein-ligand structures.

## Abstract

A significant amount of protein function requires binding small molecules, including enzymatic catalysis. As such, designing binding pockets for small molecules has several impactful applications ranging from drug synthesis to energy storage. Towards this goal, we first develop HarmonicFlow, an improved generative process over 3D protein-ligand binding structures based on our self-conditioned flow matching objective. FlowSite extends this flow model to jointly generate a protein pocket’s discrete residue types and the molecule’s binding 3D structure. We show that HarmonicFlow improves upon state-of-the-art generative processes for docking in simplicity, generality, and average sample quality in pocket-level docking. Enabled by this structure modeling, FlowSite designs binding sites substantially better than baseline approaches.