# Contamination-Resilient Anomaly Detection via Adversarial Learning on Partially-Observed Normal and Anomalous Data

**Source**: https://proceedings.mlr.press/v235/lv24b.html

## [POSITIVE] Adversarial Learning with Three Datasets (CR-GAN)
A GAN framework that jointly leverages a contaminated dataset, a small clean normal dataset, and a small clean anomaly dataset to learn the normal-data distribution by minimizing f-divergence between specially constructed mixture distributions P(x) and Q(x).

**Delta**: outperforms baseline
**Condition**: Anomaly detection under contaminated training datasets with access to small auxiliary normal and anomaly datasets

**Evidence**: "Extensive experimental results on both toy and real-world datasets demonstrate the proposed method can effectively exploit the collected normal and anomalous samples even if their number is small and achieve better performance than comparable baselines under the contamination scenarios."

## [POSITIVE] Auxiliary Normal Dataset Exploitation
Incorporating a small clean normal dataset X+ in addition to the contaminated dataset and anomaly dataset, which existing methods do not use.

**Delta**: +4.2 AUROC on MNIST (88.2 vs 84.0 without auxiliary datasets)
**Condition**: Ablation study on MNIST and FMNIST datasets

**Evidence**: "From the Table 6, we can clearly observe that by using the additionally collected normal and anomaly datasets, the performance can be improved substantially."

## [POSITIVE] Label Flipping Mechanism
A mechanism that randomly flips samples between normal and anomaly datasets with probability gamma to prevent the discriminator from memorizing the small auxiliary datasets, thereby alleviating overfitting.

**Delta**: +2.4 AUROC on MNIST (90.6 vs 88.2 without flipping)
**Condition**: When auxiliary datasets are small (tens to hundreds of samples)

**Evidence**: "Furthermore, by using the theoretically supported flipping mechanism, a further improvement can be observed due to the mechanism's ability to alleviate the overfitting problem caused by the small size of the additional collected datasets."

## [POSITIVE] Adaptive Flipping Probability Adjustment
Dynamically adjusting the flipping probability gamma based on the estimated overfitting degree of the discriminator, measured as the difference between averaged discriminator outputs on X+ and X-.

**Delta**: +0.7 AUROC on MNIST (90.6 adaptive vs 89.9 fixed gamma=0.1)
**Condition**: Compared to fixed flipping probability values across MNIST, FMNIST, 20NEWS, HAR, UNSW-NB15

**Evidence**: "We can also see that by using the proposed adaptive probability adjusting scheme, the best performance can be achieved. This indicates that slightly flipping the labels of auxiliary datasets is helpful when collected clean datasets are small. However, the fixed gamma should be set carefully to avoid the negative impacts."

## [NEGATIVE] Fixed High Flipping Probability
Setting the flipping probability gamma to a fixed high value (e.g., 0.1) without adaptive adjustment.

**Delta**: -0.9 AUROC on 20NEWS (70.8 at gamma=0.1 vs 72.4 at gamma=0)
**Condition**: On 20NEWS dataset, gamma=0.1 performs worse than gamma=0 (72.4)

**Evidence**: "the fixed gamma should be set carefully to avoid the negative impacts."

## [POSITIVE] Bidirectional GAN (BiGAN) for Detection
Extending the proposed GAN to the bidirectional paradigm by adding an encoder E that maps samples to latent space, enabling use of both reconstruction error and latent norm for anomaly scoring.

**Delta**: outperforms baseline
**Condition**: Anomaly detection inference stage

**Evidence**: "To detect anomalies efficiently, we extend the proposed GANs to the bidirectional paradigm and then use the combination of the reconstruction error and the norm of latent representations to serve as the final detection criteria."

## [POSITIVE] Combined Anomaly Score (Reconstruction + Latent Norm)
Computing anomaly score as a weighted combination of reconstruction error ||x - G(E(x))||^2 and latent representation norm ||E(x)||^2, normalized by validation set min/max values.

**Delta**: robust across rho in [1,8]
**Condition**: Anomaly scoring at test time; weight rho=4 used by default

**Evidence**: "From the Table 8, we can see that the performance of our method is quite robust to the choice of the value of rho. As long as it is chosen within the range [1, 8], the performance does not have too much difference on the considered datasets."

## [POSITIVE] Least-Squares GAN (LSGAN) Objective
Using least-squared loss (Pearson chi-squared divergence) instead of cross-entropy loss to train the discriminator and generator, corresponding to f(u)=(u-1)^2.

**Delta**: theoretically guaranteed convergence to p+(x)
**Condition**: Training the GAN discriminator and generator under the proposed framework

**Evidence**: "As revealed in (Mao et al., 2017), minimizing the Pearson chi^2 divergence between two distributions can be achieved via the least-squared GAN, which employs the least-squared loss, instead of the commonly-used cross-entropy loss, to train the discriminator and generator."

## [NEGATIVE] Diverse Normal Data Setting (Multiple Normal Categories)
Evaluating with normal data comprised of multiple categories (K=1,3,5) rather than the single-category assumption common in prior work.

**Delta**: MNIST drops from 93.7 (K=1) to 83.5 (K=5) for proposed method
**Condition**: All methods evaluated on MNIST, FMNIST, CIFAR10, 20NEWS with increasing normal category diversity

**Evidence**: "It can be seen from Table 1 that the performance of all methods decreases as the normal data becomes more diverse. But thanks to the exploitation of a normal dataset, the results show that the performance of our method deteriorates more slowly than the baselines."

## [NEGATIVE] Incomplete Anomaly Type Coverage in X-
Using an anomaly dataset X- that only covers a subset of all anomaly types, reflecting real-world diversity constraints.

**Delta**: pg(x) cannot converge to p+(x) but converges to mixture of p+(x) and unobserved anomaly distribution
**Condition**: When collected anomaly dataset does not cover all anomaly types

**Evidence**: "From Theorem 3.3, we can see that under the scenario with incomplete collected anomalies, the generation distribution pg(x) cannot converge to normal-data distribution p+(x) anymore, but instead to a mixture of p+(x) and p_u^-(x), which represents the anomaly distribution of unobserved types."

## [POSITIVE] Increasing Number of Collected Anomaly Types
Collecting anomaly samples from more diverse anomaly types in the auxiliary dataset X-.

**Delta**: performance improves as types increase from 1 to 4 on MNIST and F-MNIST
**Condition**: MNIST and F-MNIST datasets with varying anomaly type coverage

**Evidence**: "Figure 1 shows that how the performance varies as the number of types of collected anomalies varies from 1 to 4 on MNIST and F-MNIST datasets. Obviously, as the number of collected anomalous types increases, the performance of all the methods improves, but our method remains the best over all number of types considered."

## [NEGATIVE] Increasing Contamination Ratio
Higher proportion of anomalous samples in the contaminated training dataset X.

**Delta**: MNIST AUROC drops from 94.9 (ep=0.05) to 87.8 (ep=0.3) for proposed method
**Condition**: All methods across MNIST, FMNIST, CIFAR10, 20NEWS, HAR, UNSW-NB15

**Evidence**: "From the table, it can be seen that the performance of all anomaly detection methods decreases as the level of contamination increases. But our approach drops slower than other methods in all six datasets across."

## [POSITIVE] Increasing Auxiliary Dataset Size
Using more samples in the small auxiliary normal and anomaly datasets (ranging from 10 to 50 samples).

**Delta**: HAR improves from 89.4 (size=10) to 93.3 (size=50) for proposed method
**Condition**: Auxiliary dataset size experiments across MNIST, FMNIST, CIFAR10, 20NEWS, HAR, UNSW-NB15

**Evidence**: "Table 2 shows that given a limited amount of collected data, varying from 10 to 50, our method with the proposed flipping mechanism outperforms other weakly/semi-supervised methods. Specifically, the averaged performance gains of our method over the best baseline in MNIST, FMNIST and 20NEW are 11.5%, 3.7% and 5.9% respectively."

## [POSITIVE] Weight Parameters Lambda and Beta in [0.6, 0.8]
Setting the weights lambda and beta (controlling emphasis on clean auxiliary datasets) in the range [0.6, 0.8].

**Delta**: best AUROC achieved at lambda=beta=0.8 for MNIST (90.2) and HAR (92.6)
**Condition**: Sensitivity analysis across MNIST, FMNIST, 20NEWS, HAR, UNSW-NB15

**Evidence**: "Table 7 shows that lambda and beta could be roughly set in the range [0.6, 0.8] to better resist the contamination."

## [POSITIVE] Increasing Lambda to Dampen Unobserved Anomaly Influence
Increasing the weight lambda of the normal dataset X+ to reduce the coefficient of unobserved anomaly distribution in the converged generator when anomaly coverage is incomplete.

**Delta**: reduces coefficient kappa_2/kappa_3 controlling weighting of unobserved anomaly distribution
**Condition**: Incomplete anomaly type coverage scenario; limited by small size of X+ causing overfitting risk

**Evidence**: "if we increase the weight of normal samples lambda, due to kappa_2 = (1-gamma)(1-lambda)(1-pi)(1-alpha), the coefficient controlling the weighting of p_u^-(x) will become small. Thus, although we cannot use X- to mitigate the influence of anomalies from unobserved types, we can still use the normal dataset X+ to dampen their influence in the final converged distribution pg(x)."

## [NEUTRAL] BERT Feature Extraction for Text Data
Using pre-trained BERT to extract textual features from the 20newsgroups dataset for anomaly detection.

**Delta**: not separately quantified
**Condition**: 20newsgroups textual anomaly detection dataset preprocessing

**Evidence**: "we use three image datasets (MNIST, F-MNIST and CIFAR10) and one textual dataset (20newsgroups), in which the textual features are extracted from a pre-trained BERT (Devlin et al., 2019) as proposed in ADBench (Han et al., 2022)."
