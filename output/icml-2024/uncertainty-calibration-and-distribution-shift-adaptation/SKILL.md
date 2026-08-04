---
name: uncertainty-calibration-and-distribution-shift-adaptation
description: >-
  This skill covers methods for quantifying and correcting model uncertainty (calibration techniques like ECE analysis, logit smoothing, last-layer recalibration, and ensemble methods) and adapting models to distribution shift (conformal prediction, test-time adaptation, covariate shift correction), applied across tasks including classification, regression, pose estimation, and long-form text generation.
---

# Uncertainty Calibration And Distribution Shift Adaptation

This skill covers methods for quantifying and correcting model uncertainty (calibration techniques like ECE analysis, logit smoothing, last-layer recalibration, and ensemble methods) and adapting models to distribution shift (conformal prediction, test-time adaptation, covariate shift correction), applied across tasks including classification, regression, pose estimation, and long-form text generation.

## Entry Index

| # | Title | Tags | File |
|---|-------|------|------|
| 1 | Not all distributional shifts are equal: Fine-grained robust | conformal-inference, distributional-shift, covariate-shift | ai24a.md |
| 2 | Evaluation of Test-Time Adaptation Under Computational Time  | test-time-adaptation, evaluation-protocol, distribution-shift | alfarra24a.md |
| 3 | Online conformal prediction with decaying step sizes | conformal-prediction, online-learning, coverage-guarantee | angelopoulos24a.md |
| 4 | Linguistic Calibration of Long-Form Generations | linguistic-calibration, long-form-generation, hallucination | band24a.md |
| 5 | Transitional Uncertainty with Layered Intermediate Predictio | uncertainty-estimation, single-pass, feature-engineering | benkert24a.md |
| 6 | Stability Evaluation through Distributional Perturbation Ana | distributional-robustness, stability-evaluation, out-of-distribution | blanchet24a.md |
| 7 | Density-Softmax: Efficient Test-time Model for Uncertainty E | uncertainty-estimation, test-time, distribution-shift | bui24a.md |
| 8 | Split-Ensemble: Efficient OOD-aware Ensemble via Task and Mo | OOD-detection, ensemble, uncertainty-estimation | chen24aw.md |
| 9 | How Flawed Is ECE? An Analysis via Logit Smoothing | calibration, expected-calibration-error, logit-smoothing | chidambaram24a.md |
| 10 | Tilt and Average : Geometric Adjustment of the Last Layer fo | calibration, last-layer, geometric-adjustment | cho24g.md |
| 11 | Sampling-based Multi-dimensional Recalibration | calibration, multivariate-forecasting, probabilistic-prediction | chung24a.md |
| 12 | Conformal Prediction Sets Improve Human Decision Making | conformal-prediction, human-decision-making, uncertainty | cresswell24a.md |
| 13 | Enabling Uncertainty Estimation in Iterative Neural Networks | uncertainty-estimation, iterative-networks, convergence-rate | durasov24a.md |
| 14 | Out of the Ordinary: Spectrally Adapting Regression for Cova | covariate-shift, regression, spectral-adaptation | eyre24a.md |
| 15 | On the Calibration of Human Pose Estimation | pose-estimation, calibration, confidence-estimation | gu24a.md |
| 16 | Model Assessment and Selection under Temporal Distribution S | distribution-shift, model-selection, temporal-adaptation | han24b.md |
| 17 | Decomposing Uncertainty for Large Language Models through In | uncertainty-decomposition, llm, aleatoric | hou24b.md |
| 18 | Pseudo-Calibration: Improving Predictive Uncertainty Estimat | domain-adaptation, calibration, uncertainty | hu24i.md |
| 19 | Bayesian Power Steering: An Effective Approach for Domain Ad | diffusion-models, domain-adaptation, bayesian-fine-tuning | huang24l.md |
| 20 | Conformal Prediction for Deep Classifier via Label Ranking | conformal-prediction, label-ranking, coverage-guarantee | huang24aa.md |
| 21 | Experts Don’t Cheat: Learning What You Don’t Know By Predict | uncertainty-quantification, hallucination-detection, calibration | johnson24a.md |
| 22 | IW-GAE: Importance weighted group accuracy estimation for im | domain-adaptation, calibration, model-selection | joo24a.md |
| 23 | Decoupling Feature Extraction and Classification Layers for  | calibration, neural-networks, feature-extraction | jordahn24a.md |
| 24 | Is Epistemic Uncertainty Faithfully Represented by Evidentia | epistemic-uncertainty, evidential-deep-learning, Bayesian-methods | juergens24a.md |
| 25 | Conformal Prediction with Learned Features | conformal-prediction, conditional-coverage, learned-features | kiyani24a.md |
| 26 | Stationary Latent Weight Inference for Unreliable Observatio | test-time-adaptation, distribution-shift, latent-weight-inference | lee24b.md |
| 27 | Graph Neural Networks with a Distribution of Parametrized Gr | graph-neural-networks, graph-uncertainty, stochastic-graphs | lee24k.md |
| 28 | Improving Instruction Following in Language Models through P | instruction-following, uncertainty-estimation, proxy-model | lee24z.md |
| 29 | Zero-Shot ECG Classification with Multimodal Learning and Te | ECG-classification, zero-shot-learning, multimodal-learning | liu24bg.md |
| 30 | Geometry-Calibrated DRO: Combating Over-Pessimism with Free  | distributionally-robust-optimization, over-pessimism, free-energy | liu24br.md |
| 31 | Beyond Sole Strength: Customized Ensembles for Generalized V | vision-language-models, CLIP, ensemble | lu24a.md |
| 32 | Beyond the Federation: Topology-aware Federated Learning for | federated-learning, topology-awareness, out-of-federation-generalization | ma24e.md |
| 33 | Classification under Nuisance Parameters and Generalized Lab | likelihood-free-inference, label-shift, nuisance-parameters | masserano24a.md |
| 34 | Using Uncertainty Quantification to Characterize and Improve | neural-operators, uncertainty-quantification, out-of-domain | mouli24a.md |
| 35 | Measuring Stochastic Data Complexity with Boltzmann Influenc | minimum-description-length, boltzmann-influence, prediction-uncertainty | ng24b.md |
| 36 | FedCal: Achieving Local and Global Calibration in Federated  | federated-learning, calibration, data-heterogeneity | peng24g.md |
| 37 | Adaptive Conformal Inference by Betting | conformal-prediction, adaptive-inference, betting | podkopaev24a.md |
| 38 | The Entropy Enigma: Success and Failure of Entropy Minimizat | entropy-minimization, test-time-adaptation, distribution-shift | press24a.md |
| 39 | Conformal Validity Guarantees Exist for Any Data Distributio | conformal-prediction, validity-guarantees, distribution-free | prinster24a.md |
| 40 | Conformalized Survival Distributions: A Generic Post-Process | survival-analysis, calibration, conformal-prediction | qi24a.md |
| 41 | Ensemble Pruning for Out-of-distribution Generalization | ensemble-pruning, out-of-distribution, diversity | qiao24a.md |
| 42 | To Cool or not to Cool? Temperature Network Meets Large Foun | temperature-scaling, foundation-models, distributionally-robust-optimization | qiu24c.md |
| 43 | Connect Later: Improving Fine-tuning for Robustness with Tar | domain-adaptation, fine-tuning, robustness | qu24b.md |
| 44 | LEVI: Generalizable Fine-tuning via Layer-wise Ensemble of D | fine-tuning, layer-wise-ensemble, distribution-shift | roh24a.md |
| 45 | Second-Order Uncertainty Quantification: A Distance-Based Ap | second-order-uncertainty, distributional-predictions, uncertainty-quantification | sale24a.md |
| 46 | Meta Evidential Transformer for Few-Shot Open-Set Recognitio | few-shot-learning, open-set-recognition, evidential-learning | sapkota24a.md |
| 47 | Thermometer: Towards Universal Calibration for Large Languag | LLM-calibration, uncertainty-quantification, instruction-tuning | shen24c.md |
| 48 | LCA-on-the-Line: Benchmarking Out of Distribution Generaliza | out-of-distribution-generalization, class-taxonomy, benchmarking | shi24c.md |
| 49 | An Empirical Study Into What Matters for Calibrating Vision- | vision-language-models, calibration, uncertainty-estimation | tu24a.md |
| 50 | ConvNet vs Transformer, Supervised vs CLIP: Beyond ImageNet  | ConvNet, Vision-Transformer, CLIP | vishniakov24a.md |
| 51 | Open-Vocabulary Calibration for Fine-tuned CLIP | CLIP, calibration, vision-language-models | wang24bw.md |
| 52 | Calibration Bottleneck: Over-compressed Representations are  | calibration, representation-learning, weight-decay | wang24cm.md |
| 53 | Confidence-aware Contrastive Learning for Selective Classifi | selective-classification, confidence-calibration, contrastive-learning | wu24s.md |
| 54 | Conformal prediction for multi-dimensional time series by el | conformal-prediction, multivariate-time-series, ellipsoidal-sets | xu24m.md |
| 55 | Few-shot Adaptation to Distribution Shifts By Mixing Source  | few-shot-adaptation, distribution-shift, embedding-interpolation | xue24a.md |
| 56 | Harnessing Hierarchical Label Distribution Variations in Tes | long-tail-recognition, distribution-shift, hierarchical | yang24af.md |
| 57 | Theoretical Analysis of Learned Database Operations under Di | learned-database-operations, distribution-shift, learnability-theory | zeighami24a.md |
| 58 | Conformalized Adaptive Forecasting of Heterogeneous Trajecto | conformal-prediction, trajectory-forecasting, uncertainty-quantification | zhou24l.md |
| 59 | CRoFT: Robust Fine-Tuning with Concurrent Optimization for O | fine-tuning, OOD-generalization, open-set-detection | zhu24n.md |
