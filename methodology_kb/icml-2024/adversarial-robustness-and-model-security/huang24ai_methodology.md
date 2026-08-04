# Adversarially Robust Deep Multi-View Clustering: A Novel Attack and Defense Framework

**Source**: https://proceedings.mlr.press/v235/huang24ai.html

## [POSITIVE] GAN-based adversarial attack on DMVC
Uses a Generator-Discriminator architecture to generate adversarial perturbations targeting both complementarity and consistency of multi-view data, formulated as a saddle-point minimax problem

**Delta**: EAMC ACC drops from 0.74 to 0.25 on NoisyMNIST; AECoDDC ACC drops from 0.99 to 0.24 on NoisyMNIST
**Condition**: When attacking existing DMVC models (EAMC, SiMVC, CoMVC, Multi-VAE, AECoDDC, InfoDDC, SEM)

**Evidence**: "The table reveals that the model's results have experienced varying degrees of decrease after the attack, indicating that our suggested attack architecture has effectively targeted the deep multi-view clustering approaches."

## [POSITIVE] Joint complementarity and consistency attack
Simultaneously attacks view-specific complementary representations (L_a-com) and cross-view consensus consistency (L_a-con) rather than targeting only one aspect

**Delta**: outperforms attacking only complementarity or only consistency alone
**Condition**: When designing adversarial attacks against DMVC models with multiple views

**Evidence**: "If we solely attack the complementarity of multiple views (i.e., optimizing only Eq. 2), we may fail to disrupt the final learned consensus representation, potentially yielding identical results before and after the attack. Similarly, if we exclusively target the consistency of multiple views (i.e., optimizing only Eq. 3), we cannot ensure that each view has been adequately attacked, potentially affecting only a subset of views."

## [POSITIVE] Adversarial training with consistent cross-view attack embeddings
Applies PGD-based adversarial training in multi-view setting while enforcing consistency of adversarial embeddings across views using contrastive loss on adversarial data

**Delta**: AR-DMVC post-attack ACC 0.90 on NoisyMNIST vs. best baseline post-attack ACC 0.31
**Condition**: When defending DMVC models against adversarial attacks in multi-view setting

**Evidence**: "Note that maintaining a consistent attack embedding in adversarial training is crucial for effective defense against attacks. Our empirical findings highlight that a weaker consistency attacks regularization in adversarial training typically leads to a more vulnerable model."

## [NEGATIVE] Weaker consistency regularization in adversarial training
Reducing the strength of cross-view consistency constraint during adversarial training

**Delta**: leads to more vulnerable model (quantitative not specified)
**Condition**: During adversarial training of DMVC defense models

**Evidence**: "Our empirical findings highlight that a weaker consistency attacks regularization in adversarial training typically leads to a more vulnerable model. These results further indicate that the DMVC model is challenging to defend the adversarial perturbation."

## [POSITIVE] Attack Mitigator (AM) regularization
Minimizes an upper bound on the conditional mutual information between adversarial inputs and clustering assignments (KL divergence between clean and adversarial cluster assignment distributions), derived via information-theoretic analysis in Theorem 4.2

**Delta**: AR-DMVC-AM post-attack ACC 0.93 vs AR-DMVC post-attack ACC 0.90 on NoisyMNIST; AR-DMVC-AM post-attack ACC 0.67 vs AR-DMVC post-attack ACC 0.54 on NoisyFashion
**Condition**: When added on top of AR-DMVC adversarial training framework

**Evidence**: "AR-DMVC-AM significantly enhances AR-DMVC's robustness against adversarial attacks and demonstrates improved generalization to other datasets. This underscores the efficacy of AM regularization in augmenting robustness transferability against incremental data."

## [POSITIVE] Higher adversarial training strength (large lambda)
Increasing the trade-off coefficient lambda that controls the strength of adversarial training in the AR-DMVC-AM objective

**Delta**: optimal at lambda=100 for NoisyFashion
**Condition**: Hyperparameter tuning of AR-DMVC-AM on NoisyFashion dataset

**Evidence**: "We can conclude that a stronger intensity of adversarial training, indicated by relatively large parameters (optimal at λ = 100), results in better defense against attacks."

## [NEUTRAL] AM regularization weight gamma stability
The gamma parameter controlling AM regularization contribution exhibits relative stability across a wide range of values

**Delta**: stable across tested range; set to 1 in all experiments
**Condition**: Hyperparameter tuning of AR-DMVC-AM across all datasets

**Evidence**: "The parameter γ exhibits relative stability, and thus, we consistently set it to 1 in all experiments."

## [NEGATIVE] Increasing adversarial noise budget epsilon
Increasing the perturbation budget epsilon allowed for adversarial examples during attack

**Delta**: EAMC NoisyMNIST ACC drops from 0.72 (eps=0.1) to 0.44 (eps=0.2) to 0.23 (eps=0.3)
**Condition**: When varying epsilon from 0.1 to 0.3 on NoisyMNIST and PatchedMNIST datasets

**Evidence**: "It is evident that as the ε threshold increases, the efficacy of the attack escalates while the performance of the models diminishes. Meanwhile, our proposed adversarial defense method consistently preserves better clustering results."

## [POSITIVE] Contrastive learning-based multi-view clustering (CL-MVC) base model
Uses contrastive loss between view pairs with cosine similarity and temperature parameter tau=0.1, combined with DDC clustering module on weighted-sum consensus representation

**Delta**: AR-DMVC-AM pre-attack ACC 0.99 on NoisyMNIST, competitive with SOTA
**Condition**: As the base clustering architecture for the proposed AR-DMVC defense framework

**Evidence**: "Although many CL-based MVC models have been designed to improve clustering accuracy, as mentioned in our related works analysis, our focus in this article is to explore attacks and defenses against multi-view models. Hence, we opt not to incorporate intricate regularization model frameworks as the fundamental structure."

## [POSITIVE] Robustness transferability via AM regularization
Training AR-DMVC-AM on one dataset/class split and testing on a different dataset/class split to evaluate generalization of adversarial robustness

**Delta**: NoisyFashion(0-4)->NoisyFashion(5-9): AR-DMVC-AM ACC 0.52 vs AR-DMVC ACC 0.40; NoisyMNIST(0-4)->NoisyMNIST(5-9): AR-DMVC-AM ACC 0.41 vs AR-DMVC ACC 0.40
**Condition**: Cross-dataset and cross-class-split transfer evaluation on NoisyFashion and NoisyMNIST

**Evidence**: "AR-DMVC-AM significantly enhances AR-DMVC's robustness against adversarial attacks and demonstrates improved generalization to other datasets. This underscores the efficacy of AM regularization in augmenting robustness transferability against incremental data."

## [POSITIVE] AR-DMVC-AM with large epsilon attack (eps=0.3)
Performance of the full AR-DMVC-AM defense under high perturbation budget attacks

**Delta**: AR-DMVC-AM ACC 0.94 vs AR-DMVC ACC 0.54 and all baselines below 0.47 at eps=0.3 on NoisyMNIST
**Condition**: Under high adversarial perturbation budget (epsilon=0.3) on NoisyMNIST dataset

**Evidence**: "AR-DMVC-AM: 0.99, 0.99, 0.94 vs AR-DMVC: 0.99, 0.99, 0.54 on NoisyMNIST at epsilon 0.1, 0.2, 0.3"
