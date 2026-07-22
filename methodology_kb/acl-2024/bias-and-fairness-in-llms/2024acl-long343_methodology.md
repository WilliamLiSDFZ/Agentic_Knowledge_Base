# Unlearning Traces the Influential Training Data of Language Models

**Source**: https://aclanthology.org/2024.acl-long.343/

## [POSITIVE] UnTrac (Gradient Ascent Unlearning for Influence Estimation)
Estimates the influence of a training dataset by unlearning it from a trained model via gradient ascent, then measuring the change in test loss after unlearning.

**Delta**: outperforms baseline
**Condition**: Tracing influential pretraining corpora for toxic, biased, and untruthful content generation; both equal and different training dataset size settings

**Evidence**: "Across all datasets and settings, the estimated influence by UnTrac and UnTrac-Inv correlates well with the ground truth. GradCos, GradDot, and HIF (Arnoldi) perform well on Winobias. However, they show lower performance on Toxigen and TruthfulQA specifically when the dataset sizes are unbalanced."

## [POSITIVE] UnTrac-Inv (Inverse Unlearning for Scalable Influence Estimation)
Unlearns the test dataset instead of training datasets and evaluates the unlearned model on training datasets, requiring only a single run of unlearning regardless of the number of training datasets.

**Delta**: outperforms baseline
**Condition**: Scalable influence estimation when many training datasets are used; most effective with large batch sizes and small number of unlearning steps

**Evidence**: "Across all datasets and settings, the estimated influence by UnTrac and UnTrac-Inv correlates well with the ground truth."

## [POSITIVE] Preconditioned Gradient Optimizers (RMSProp, Adam, Adafactor) for Unlearning
Using optimizers with preconditioning (RMSProp, Adam, Adafactor) rather than plain SGD or SGD with momentum during the unlearning phase.

**Delta**: Adam: 0.419±0.063 vs SGD: -0.147±0.014 (Pearson r on ToxiGen)
**Condition**: UnTrac unlearning optimizer selection; ToxiGen evaluation with equal training dataset sizes

**Evidence**: "UnTrac performs well when RMSProp, Adam, and Adafactor are used, indicating that a preconditioner plays an important role in unlearning."

## [NEGATIVE] SGD for Unlearning
Using plain stochastic gradient descent (without momentum or preconditioning) for the gradient ascent unlearning step.

**Delta**: -0.147±0.014 Pearson r (UnTrac) vs 0.419±0.063 with Adam
**Condition**: UnTrac and UnTrac-Inv unlearning; ToxiGen evaluation

**Evidence**: "UnTrac performs well when RMSProp, Adam, and Adafactor are used, indicating that a preconditioner plays an important role in unlearning."

## [NEGATIVE] SGD with Momentum for Unlearning
Using SGD with momentum (momentum=dampening=0.9) for the gradient ascent unlearning step.

**Delta**: -0.239±0.011 Pearson r (UnTrac) vs 0.419±0.063 with Adam
**Condition**: UnTrac and UnTrac-Inv unlearning optimizer selection; ToxiGen evaluation

**Evidence**: "Table 4 (top) shows the performance with various optimizers... SGD with momentum: UnTrac -0.239±0.011, UnTrac-Inv -0.099±0.070"

## [POSITIVE] Large Batch Size for UnTrac-Inv
Using a large batch size (e.g., 256, containing all test examples in a single batch) when running UnTrac-Inv unlearning.

**Delta**: batch size 256 achieves positive correlation vs batch size 1 performing poorly over entire run
**Condition**: UnTrac-Inv hyperparameter tuning; ToxiGen evaluation with equal training dataset sizes

**Evidence**: "When the batch size is one, UnTrac-Inv performs poorly over the entire run of unlearning. When the batch size is 256, the performance of UnTrac-Inv rises for the first several epochs."

## [NEGATIVE] Small Batch Size for UnTrac-Inv
Using a batch size of 1 when running UnTrac-Inv unlearning.

**Delta**: performs poorly over entire run of unlearning
**Condition**: UnTrac-Inv; ToxiGen evaluation

**Evidence**: "When the batch size is one, UnTrac-Inv performs poorly over the entire run of unlearning."

## [POSITIVE] Higher Learning Rate for UnTrac
Using a higher learning rate (e.g., 5e-5 or 1e-4) during gradient ascent unlearning in UnTrac.

**Delta**: 5e-05: 0.419±0.063, 1e-04: 0.377±0.040 vs 5e-06: -0.127±0.302 (Pearson r)
**Condition**: UnTrac learning rate selection; ToxiGen evaluation with equal training dataset sizes

**Evidence**: "UnTrac performs well across various learning rates when using higher learning rates. With lower learning rates, UnTrac does not converge and performs unstably."

## [NEGATIVE] Higher Learning Rate for UnTrac-Inv
Using a higher learning rate during unlearning in UnTrac-Inv.

**Delta**: 5e-05: 0.376±0.008, 1e-04: 0.137±0.019, 5e-04: 0.027±0.015
**Condition**: UnTrac-Inv learning rate selection; ToxiGen evaluation

**Evidence**: "UnTrac-Inv is somewhat sensitive to the choice of learning rate... As a higher learning rate boosts the divergence, increasing the learning rate does not necessarily lead to higher performance."

## [POSITIVE] Sufficient Number of Unlearning Epochs for UnTrac
Running UnTrac unlearning for multiple epochs (e.g., 1 full epoch) rather than a single step.

**Delta**: performance rises and stabilizes over epochs vs underperforming at single step
**Condition**: UnTrac unlearning; ToxiGen evaluation

**Evidence**: "On both batch sizes, UnTrac achieves high and stable performance as the number of unlearning epochs increases... UnTrac and UnTrac-Inv underperform when the number of unlearning steps is one."

## [NEGATIVE] Excessive Unlearning Steps for UnTrac-Inv
Running UnTrac-Inv for too many unlearning epochs beyond the initial few.

**Delta**: performance degrades gradually after initial rise
**Condition**: UnTrac-Inv with large batch size; ToxiGen evaluation

**Evidence**: "When the batch size is 256, the performance of UnTrac-Inv rises for the first several epochs, while it degrades gradually after a while."

## [POSITIVE] Fixed Training Steps Leave-Dataset-Out (Modified Ground Truth)
Training each counterfactual model for the same number of steps T (sampling from D\Z) rather than training on all examples in D\Z, to avoid overestimating the influence of large datasets.

**Delta**: avoids overestimation of large dataset influence
**Condition**: Ground-truth influence computation when training datasets have different sizes

**Evidence**: "This setup is practical for evaluating the influence of datasets of different sizes... The influence of large datasets is higher because the size of D\Z becomes smaller, and the performance of model θ−Z largely depends on the dataset sizes [in the conventional setup]."

## [NEGATIVE] GradDot (Single Checkpoint Gradient Dot Product)
Approximates influence using the dot product of training and test gradients at the last model checkpoint only.

**Delta**: -0.123±0.008 (ToxiGen equal), -0.250±0.007 (ToxiGen different) Pearson r
**Condition**: Pretraining corpus influence estimation on ToxiGen and TruthfulQA, especially with unbalanced dataset sizes

**Evidence**: "GradCos, GradDot, and HIF (Arnoldi) perform well on Winobias. However, they show lower performance on Toxigen and TruthfulQA specifically when the dataset sizes are unbalanced."

## [NEUTRAL] GradCos (Cosine Similarity of Gradients)
Normalizes training and test gradients and uses cosine similarity to estimate influence, mitigating outlier gradient effects.

**Delta**: 0.418±0.018 (ToxiGen equal) but -0.337±0.007 (ToxiGen different) Pearson r
**Condition**: Works on WinoBias but fails on ToxiGen and TruthfulQA with unbalanced dataset sizes

**Evidence**: "GradCos, GradDot, and HIF (Arnoldi) perform well on Winobias. However, they show lower performance on Toxigen and TruthfulQA specifically when the dataset sizes are unbalanced."

## [NEUTRAL] HIF with Arnoldi Iteration
Hessian-based influence functions approximated using Arnoldi iteration with low-rank eigenvector projection (n=200, p=100).

**Delta**: 0.559±0.010 (WinoBias equal) but -0.343±0.005 (ToxiGen different) Pearson r
**Condition**: Works on WinoBias but fails on ToxiGen with unbalanced dataset sizes

**Evidence**: "GradCos, GradDot, and HIF (Arnoldi) perform well on Winobias. However, they show lower performance on Toxigen and TruthfulQA specifically when the dataset sizes are unbalanced."

## [NEGATIVE] HIF with LISSA
Hessian-based influence functions with inverse Hessian approximated by LISSA (linear time stochastic second-order algorithm).

**Delta**: high variance: 0.389±0.117 (WinoBias equal), -0.092±0.042 (WinoBias different)
**Condition**: Pretraining corpus influence estimation across all test datasets

**Evidence**: "The performance of HIF (LISSA) is unstable, as indicated by the high variance in its score."

## [NEGATIVE] TracIn (Multiple Checkpoint Gradient Tracing)
Traces influence by summing gradient dot products at multiple model checkpoints saved during training.

**Delta**: 0.591±0.014 (TruthfulQA equal) but -0.187±0.005 (TruthfulQA different) Pearson r
**Condition**: Performs reasonably with equal dataset sizes but degrades with unbalanced dataset sizes

**Evidence**: "While TracIn achieves a relatively higher correlation with equally sized training datasets, its performance declines when the sizes are different."

## [POSITIVE] Adam with Decaying Gradient Average for UnTrac-Inv
Using Adam optimizer (which maintains decaying average of gradients) for UnTrac-Inv unlearning, making training less stochastic.

**Delta**: 0.376±0.008 Pearson r vs -0.231±0.012 with RMSProp for UnTrac-Inv
**Condition**: UnTrac-Inv optimizer selection; ToxiGen evaluation

**Evidence**: "We suspect this is because both Adam and Adafactor use a decaying average of gradients, rather than just the gradient for the current batch as RMSProp and SGD do. This makes training less stochastic and has a somewhat similar effect to using larger batches, which is beneficial for UnTrac-Inv."

## [POSITIVE] Gradient Clipping Disabled During Unlearning
Turning off gradient clipping during the unlearning phase of UnTrac and UnTrac-Inv.

**Delta**: part of best configuration achieving highest correlations
**Condition**: UnTrac and UnTrac-Inv unlearning hyperparameter configuration

**Evidence**: "Gradient clipping is turned off during unlearning."

## [NEUTRAL] Sampling Training Examples for Influence Estimation
Randomly sampling 10,000 examples from each training dataset (rather than using all examples) to estimate its influence, for computational efficiency.

**Delta**: results reported as invariant to choice of examples across four runs
**Condition**: Pretraining corpus influence estimation with OPT-125M

**Evidence**: "In practice, computing influences using the whole pretraining dataset is quite expensive. Thus, we randomly sample 10,000 examples from each dataset to estimate its influence. To ensure that the reported results are invariant to the choice of examples, we report the average and standard deviation across four runs using different examples."
