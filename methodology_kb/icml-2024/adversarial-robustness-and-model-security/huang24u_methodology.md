# Self-Driven Entropy Aggregation for Byzantine-Robust Heterogeneous Federated Learning

**Source**: https://proceedings.mlr.press/v235/huang24u.html

## [POSITIVE] Instance Sharpness (IS)
Minimizes per-instance prediction entropy of the global model on random public data to encourage over-confident (sharp) predictions, thereby suppressing malicious client contributions

**Delta**: IS alone: ~39.45 PairF, ~35.87 SymF, ~33.86 RanN (row ❶ in ablation)
**Condition**: Byzantine-robust aggregation in heterogeneous federated learning using random public data; effective against both data-based and parameter-based attacks

**Evidence**: "we propose Instance Sharpness (IS) to encourage the global model prediction sharpness on public data via minimizing the entropy of the distribution for each instance. The rationale behind this is that learnable aggregation parameters would disregard those 'troublemakers'"

## [POSITIVE] Class Diversity (CD)
Maximizes batch-prediction entropy of the mean prediction over a batch of public samples to encourage diverse class predictions, preventing the global model from collapsing to a biased subset of benign clients

**Delta**: CD alone: ~65.90 PairF, ~58.84 SymF but collapses on parameter-based attacks (12.65 RanN, 10.00 MiMa)
**Condition**: Heterogeneous federated learning; CD alone is insufficient for parameter-based attacks but essential when combined with IS and CC

**Evidence**: "we propose Class Diversity (CD) to make the batch-wise predictions diversely distributed to avoid prescriptive prediction preference... LCD encourages the entropy maximization of the mean prediction for a batch of public samples to achieve fruitful batch prediction"

## [POSITIVE] Cooperative Cluster (CC)
Uses parameter-free clustering (FINCH) to divide learnable aggregation weights into two groups, identifies benign group as the one with larger center value, and equally redistributes weight among benign clients to prevent Matthew Effect bias

**Delta**: IS+CC: ~58.75 PairF, ~62.90 SymF, ~55.60 RanN; full IS+CD+CC: 67.68 PairF, 65.82 SymF, 69.21 RanN, 68.32 LIE, 67.47 MiMa, 67.80 MiSu
**Condition**: Heterogeneous federated learning with data heterogeneity causing heterogeneous sharpness; alleviates Matthew Effect in weight allocation

**Evidence**: "we introduce the Cooperative Cluster (CC) to achieve benign balance... we leverage unsupervised clustering to divide the aggregation weights into two groups... we take inspiration from the cooperative equilibrium, which achieves satisfying benefits when sharing fair benefits"

## [POSITIVE] Learnable Aggregation Weight
Replaces fixed aggregation weights (data-scale or participant-scale) with a learnable parameter vector M optimized via gradient descent on random public data to dynamically assign client importance

**Delta**: outperforms baseline fixed-weight aggregation; SDEA achieves best results across all attack types in Tab. 4
**Condition**: Byzantine-robust federated learning; optimized using Adam with lr=0.005 for E=20 rounds per communication epoch

**Evidence**: "We introduce a learnable aggregation weight M ∈ R^K, which assigns a dynamic weight for each client... we regard the aggregation weight as a learnable parameter to minimize the prediction entropy on random public data to detach malicious effects, which is free of hyper-parameter and stable"

## [POSITIVE] FINCH Clustering for CC
Parameter-free clustering algorithm using first-neighbor relations and Euclidean distance to group aggregation weights, avoiding hyperparameter sensitivity of K-Means

**Delta**: FINCH: 67.68/65.82/69.21/68.32/69.29/69.49 vs K-Means: 61.58/59.04/66.03/66.15/66.26/66.35 on PairF/SymF/RanN/LIE/MiMa/MiSu
**Condition**: Cooperative Cluster step in SDEA; Cifar-10 with β=0.5, Φ=0.2, K=10

**Evidence**: "we shift the gaze towards FINCH (Sarfraz et al., 2019), which is parameter-free and thus suitable for heterogeneous federated learning with diverse attacks and agnostic client scale"

## [NEGATIVE] K-Means Clustering for CC
Standard K-Means clustering used as alternative to FINCH for grouping aggregation weights in Cooperative Cluster

**Delta**: K-Means: 61.58/59.04/66.03/66.15/66.26/66.35 vs FINCH: 67.68/65.82/69.21/68.32/69.29/69.49
**Condition**: Cooperative Cluster in SDEA; Cifar-10 with β=0.5, Φ=0.2, K=10

**Evidence**: "K-Means (MacQueen et al., 1967; Arthur & Vassilvitskii, 2006) iteratively assigns points to a fixed group number. However, it is sensitive to hyperparameter selection under different scenarios"

## [NEGATIVE] DBSCAN Clustering for CC
Density-based clustering used as alternative to FINCH for grouping aggregation weights in Cooperative Cluster

**Delta**: DBSCAN: 68.13/66.74/54.62/52.89/33.93/41.27 on PairF/SymF/RanN/LIE/MiMa/MiSu; collapses on parameter-based attacks
**Condition**: Cooperative Cluster in SDEA; Cifar-10 with β=0.5, Φ=0.2, K=10; particularly poor on parameter-based attacks

**Evidence**: "Table 2 shows DBSCAN achieves 33.93 on MiMa and 41.27 on MiSu compared to FINCH's 69.29 and 69.49"

## [POSITIVE] Random Public Dataset Usage
Using an unlabeled public dataset with no label space overlap with private data (e.g., Tiny-ImageNet for Cifar-10 task) instead of requiring a semantically consistent proxy dataset

**Delta**: SDEA with Tiny-ImageNet/Market1501 outperforms proxy-dataset methods FLTrust and Sageflow across most settings in Tab. 5
**Condition**: Byzantine-robust aggregation; eliminates need for labeled semantically-consistent proxy data

**Evidence**: "SDEA gets rid of the strong assumption and shows flexibility to different random public datasets... ours presents high generalizable under different degrees of domain shift with local data and consistently performs superior on two random public datasets i.e., Tiny-ImageNet and Market1501"

## [POSITIVE] Diversity Public Dataset Selection
Choosing a diverse random public dataset (e.g., Tiny-ImageNet, Market1501) rather than a less diverse one (e.g., SVHN, SYN) for the entropy-based aggregation

**Delta**: Tiny-ImageNet: 67.68/65.82/69.21/68.32/67.47/67.80; Market1501: 68.13/66.79/67.40/67.99/67.36/68.13; SVHN: 66.01/63.75/65.84/64.07/65.31/64.71; SYN: 62.01/62.22/66.99/63.36/63.03/62.94
**Condition**: SDEA on Cifar-10 with β=0.5, Φ=0.2; diversity of public dataset matters for performance

**Evidence**: "our methodology benefits from the fruitful random public dataset and we leverage different random public datasets in Tab. 2(c). It shows that utilizing the diversity datasets, e.g., Tiny-ImageNet and Market1501, shows relatively gratifying performance"

## [POSITIVE] Weak Data Augmentation on Public Data
Applying weak augmentation to public dataset samples during entropy optimization rather than strong augmentation

**Delta**: Weak augmentation outperforms strong on 4 of 6 attack types: PairF 67.68 vs 67.13, SymF 65.82 vs 65.03, RanN 69.21 vs 68.08, MiSu 67.80 vs 67.56
**Condition**: SDEA on Cifar-10 with β=0.5, Φ=0.2; weak augmentation preferred for most attack types

**Evidence**: "as shown in Tab. 2(b), a weak augmentation is better for SDEA to produce the confident output and thus distinguish malicious ones"

## [POSITIVE] Public Data Batch Size of 64
Using a moderate batch size of 64 for public data during aggregation weight optimization

**Delta**: Batch size 64 achieves balanced performance: 67.68/65.82/69.21/68.32/67.47/67.80; large batch (1024) degrades on parameter-based attacks: 62.11 RanN, 49.87 MiMa
**Condition**: SDEA on Cifar-10 with β=0.5, Φ=0.2; moderate batch size balances performance across attack types

**Evidence**: "too large or too small would bring optimization hindrance or bias (e.g., Bg=16, 1024 for Add Noise)... To be convenient and consistent, we set the |Bg| = 64 in the following experiments"

## [NEGATIVE] Large Public Data Batch Size (1024)
Using a large batch size of 1024 for public data during aggregation weight optimization

**Delta**: Batch 1024: 69.29 PairF (best) but 62.11 RanN, 60.42 LIE, 49.87 MiMa, 52.58 MiSu (significantly worse on parameter-based attacks)
**Condition**: SDEA on Cifar-10 with β=0.5, Φ=0.2; large batch hurts performance on parameter-based attacks

**Evidence**: "too large or too small would bring optimization hindrance or bias (e.g., Bg=16, 1024 for Add Noise)"

## [NEGATIVE] IS-only Aggregation (without CD and CC)
Using only Instance Sharpness loss without Class Diversity or Cooperative Cluster components

**Delta**: IS only: 39.45 PairF, 35.87 SymF, 33.86 RanN, 35.73 LIE, 33.27 MiMa, 34.08 MiSu vs full SDEA: 67.68/65.82/69.21/68.32/67.47/67.80
**Condition**: Heterogeneous federated learning (Cifar-10, β=0.5, Φ=0.2); IS alone insufficient due to heterogeneous sharpness problem

**Evidence**: "As illustrated in Fig. 3, combining IS, CD and CC acquires the best performance... purely leveraging IS brings a mismatch between expectation and reality in heterogeneous federated learning due to the question II): heterogeneous sharpness"

## [NEGATIVE] CD-only Aggregation (without IS and CC)
Using only Class Diversity loss without Instance Sharpness or Cooperative Cluster components

**Delta**: CD only: 65.90 PairF, 58.84 SymF, but 12.65 RanN, 12.65 LIE, 10.00 MiMa, 10.00 MiSu
**Condition**: Heterogeneous federated learning (Cifar-10, β=0.5, Φ=0.2); CD alone fails on parameter-based attacks

**Evidence**: "Figure 3 ablation row ❷ shows CD alone collapses on parameter-based attacks (RanN: 12.65, LIE: 12.65, MiMa: 10.00, MiSu: 10.00)"

## [NEGATIVE] CD+CC without IS
Using Class Diversity and Cooperative Cluster without Instance Sharpness

**Delta**: CD+CC: 66.96 PairF, 67.21 SymF, but 33.51 RanN, 37.03 LIE, 22.52 MiMa, 20.19 MiSu
**Condition**: Heterogeneous federated learning (Cifar-10, β=0.5, Φ=0.2); IS is critical for parameter-based attack robustness

**Evidence**: "Figure 3 ablation row ❺ shows CD+CC achieves good data-based attack performance but collapses on parameter-based attacks"

## [NEGATIVE] Proxy Dataset with Large Domain Shift
Using a semantically consistent but domain-shifted proxy dataset for FLTrust/Sageflow-style aggregation

**Delta**: Sageflow accuracy drops from SVHN (96.70) to SYN (89.51) on MNIST β=0.5, Φ=0.2 with SymF attack
**Condition**: Proxy dataset methods (FLTrust, Sageflow) in MNIST scenario; performance degrades with increasing domain shift between proxy and local data

**Evidence**: "proxy dataset solutions present serious performance degradation under the difficult proxy dataset with a large domain shift. For example, Sageflow presents accuracy drop from SVHN (96.70) to SYN (89.51) in the MNIST scenario (β=0.5 and Φ=0.2) with the Symmetry Flipping attack"

## [NEUTRAL] FedProx Local Optimization Objective
Using FedProx as the local optimization objective for client training in heterogeneous federated learning

**Delta**: Used as standard baseline setup; no comparative delta reported
**Condition**: All experiments; used as the local training objective for fair comparison across methods

**Evidence**: "For local training, we leverage the FedProx (Li et al., 2020b) as the local optimization objective"

## [NEUTRAL] Dirichlet Distribution for Data Heterogeneity Simulation
Using Dir(β) Dirichlet distribution to simulate label skew with β∈{0.3, 0.5} controlling imbalance degree

**Delta**: Lower β (more heterogeneous) generally reduces performance for all methods; SDEA at β=0.3, Φ=0.4 achieves 62.39/63.38/62.40/60.19/56.63/60.12
**Condition**: Experimental setup for all heterogeneous federated learning experiments; β=0.5 and β=0.3 tested

**Evidence**: "We use Dirichlet distribution: Dir(β) to simulate label skew, Non-IID distribution as previous... The smaller β is, the more imbalanced the local distribution is"

## [POSITIVE] Equal Weight Allocation for Benign Clients (Cooperative Equilibrium)
Assigning equal aggregation weights to all clients identified as benign, inspired by cooperative game theory equilibrium

**Delta**: IS+CC: 58.75/62.90/55.60/57.16/47.80/57.42 vs IS+CD+CC: 67.68/65.82/69.21/68.32/67.47/67.80
**Condition**: Cooperative Cluster step in SDEA; effective but acknowledged as not globally optimal

**Evidence**: "we view each honest client as equal importance in federated learning and equally divide the weight for those marked as goodwill... equal weight for all amicable clients is probably not the global optimal but is effective under byzantine attacks"

## [POSITIVE] SDEA vs Distance-based Methods (Multi Krum, FoolsGold, DnC)
SDEA compared against distance-based Byzantine-robust aggregation methods that rely on parameter space similarity

**Delta**: SDEA: 67.68/65.82/69.21/68.32/67.47/67.80 vs best distance-based DnC: 65.55/64.72/64.72/64.21/64.29/64.25 on Cifar-10 β=0.5, Φ=0.2
**Condition**: Cifar-10 with β=0.5, Φ=0.2; distance-based methods fail under data heterogeneity

**Evidence**: "Take the result of Cifar-10 with Random Noise in Tab. 4, our method outperforms the best counterpart with a gap of 4.49%"

## [POSITIVE] SDEA vs Statistics Distribution Methods (RFA, Trim Median, Bulyan)
SDEA compared against statistics distribution-based Byzantine-robust aggregation methods

**Delta**: SDEA: 69.21 RanN vs RFA: 58.19 RanN on Cifar-10 β=0.5, Φ=0.2; RFA collapses at Φ=0.4: 24.40/24.26/12.21/13.49
**Condition**: Cifar-10 with varying β and Φ; statistics methods sensitive to degree of data heterogeneity

**Evidence**: "Empirical results demonstrate the effectiveness... SDEA presents faster and stabler convergence speed than others with diverse attacks"
