---
name: stochastic-optimization-convergence-and-variance-reduction
description: >-
  This skill covers the theoretical analysis and algorithmic development of stochastic optimization methods, including adaptive optimizers (Adam, SGD variants), variance reduction techniques, and convergence guarantees under relaxed assumptions (non-convexity, heavy-tailed noise, asynchronous/distributed settings). Applications span machine learning training (diffusion models, mixture models, performative prediction) with considerations
---

# Stochastic Optimization Convergence And Variance Reduction

This skill covers the theoretical analysis and algorithmic development of stochastic optimization methods, including adaptive optimizers (Adam, SGD variants), variance reduction techniques, and convergence guarantees under relaxed assumptions (non-convexity, heavy-tailed noise, asynchronous/distributed settings). Applications span machine learning training (diffusion models, mixture models, performative prediction) with considerations

## Entry Index

| # | Title | Tags | File |
|---|-------|------|------|
| 1 | MicroAdam: Accurate Adaptive Optimization with Low Space Ove | adam-optimizer, memory-compression, convergence-guarantees | 000f947dcaff8fbffcc3f53a1314f358.md |
| 2 | AdjointDEIS: Efficient Gradients for Diffusion Models | diffusion-models, adjoint-method, gradient-optimization | 04badd3b048315c8c3a0ca17eff723d7.md |
| 3 | Shadowheart SGD: Distributed Asynchronous SGD with Optimal T | asynchronous-SGD, distributed-optimization, communication-heterogeneity | 06e2dd57e90a736a5a1fd3bb2bf95c6c.md |
| 4 | Optimizing over Multiple Distributions under Generalized Qua | multi-distribution-optimization, quasar-convexity, policy-optimization | 0885cd8bf11e9ca58302992ddcfd3652.md |
| 5 | Self-Refining Diffusion Samplers: Enabling Parallelization v | diffusion-sampling, parareal-iterations, parallel-inference | 09d320a5b92d74bbde3d0c4f52e680a9.md |
| 6 | The High Line: Exact Risk and Learning Rate Curves of Stocha | adaptive-learning-rates, stochastic-gradient-descent, high-dimensional | 0c7ca207a051228f978971447a56464a.md |
| 7 | Stability and Generalization of Asynchronous SGD: Sharper Bo | asynchronous-SGD, generalization-bounds, distributed-learning | 0e7e2af2e5ba822c9ad35a37b31b5dd4.md |
| 8 | Stochastic Optimization Schemes for Performative Prediction  | performative-prediction, stochastic-optimization, nonconvex-loss | 1055c730c7098c04579beb526c8cd4ba.md |
| 9 | Near-Optimal Streaming Heavy-Tailed Statistical Estimation w | clipped-SGD, heavy-tailed-estimation, streaming-optimization | 10bf96894abaf4c293b205709a98fc74.md |
| 10 | The Road Less Scheduled | learning-rate-schedule, schedule-free, stochastic-optimization | 136b9a13861308c8948cd308ccd02658.md |
| 11 | Fully Unconstrained Online Learning | online-learning, parameter-free, regret-bounds | 13cd22c32c1330decd69c13cf8cadc0a.md |
| 12 | Toward Global Convergence of Gradient EM for Over-Paramteriz | expectation-maximization, gaussian-mixture-models, over-parameterization | 14a1f12a530a934dc034f4c1e2d97aa8.md |
| 13 | On Convergence of Adam for Stochastic Optimization under Rel | adam-optimizer, non-convex-optimization, affine-variance-noise | 14bb27f680bee45d83bc769738e7f9b5.md |
| 14 | Differentially Private Stochastic Gradient Descent with Fixe | differential-privacy, dp-sgd, renyi-differential-privacy | 14fef58f09f2ebe69306e0a322e3be2b.md |
| 15 | A Simple and Optimal Approach for Universal Online Learning  | universal-online-learning, gradient-variation-regret, adaptive-algorithms | 150f35763dc51bfc269690d36a5a7c88.md |
| 16 | A Gradient Accumulation Method for Dense Retriever under Mem | dense-retrieval, InfoNCE-loss, gradient-accumulation | 15ba84c1e19b0eb75f96922f5da0a021.md |
| 17 | HyperPrism: An Adaptive Non-linear Aggregation Framework for | distributed-machine-learning, non-IID-data, non-linear-aggregation | 15e5fccdfeb10bb54f8e74944de1c8bf.md |
| 18 | Gaussian Approximation and Multiplier Bootstrap for Polyak-R | polyak-ruppert-averaging, berry-esseen-bound, TD-learning | 1700ad4e6252e8f2955909f96367b34d.md |
| 19 | Non-asymptotic Analysis of Biased Adaptive Stochastic Approx | biased-gradients, adaptive-sgd, non-asymptotic-analysis | 178b306c7ee66a66db2171646e17da36.md |
| 20 | Fundamental Convergence Analysis of Sharpness-Aware Minimiza | sharpness-aware-minimization, convergence-analysis, generalization | 17b08a9de93e2accf13429643e7eafdc.md |
| 21 | SCAFFLSA: Taming Heterogeneity in Federated Linear Stochasti | federated-learning, linear-stochastic-approximation, TD-learning | 19a42d5885e25e51852aca8144e5af0d.md |
| 22 | Emergence of heavy tails in homogenized stochastic gradient  | stochastic-gradient-descent, heavy-tails, homogenization | 19ba2b9448d5de25826f6eb408dab194.md |
| 23 | Directional Smoothness and Gradient Methods: Convergence and | gradient-descent, directional-smoothness, convergence | 1ac83203e88eb6cf6b30642f0239b932.md |
| 24 | ReLIZO: Sample Reusable Linear Interpolation-based Zeroth-or | zeroth-order-optimization, gradient-estimation, linear-interpolation | 1b3750390ca8b931fb9ca988647940cb.md |
| 25 | Improving Linear System Solvers for Hyperparameter Optimisat | Gaussian-processes, hyperparameter-optimization, linear-solvers | 1c1b099a19621e4bd2753ac572e1dbd5.md |
| 26 | Non-geodesically-convex optimization in the Wasserstein spac | wasserstein-space, non-convex-optimization, difference-of-convex | 1e1cf05517b959c1ce5934734efc421b.md |
| 27 | Non-asymptotic Global Convergence Analysis of BFGS with the  | BFGS, quasi-newton, global-convergence | 1e269abc604816c35f600ae14b354efd.md |
| 28 | Ordered Momentum for Asynchronous SGD | asynchronous-SGD, distributed-learning, momentum | 1e5cff01121223de917a84a242de30a5.md |
| 29 | Policy Optimization for Robust Average Reward MDPs | robust-mdps, average-reward, policy-optimization | 1f28e9341ab99d8e5a5734f0a76601c7.md |
| 30 | Communication Efficient Distributed Training with Distribute | distributed-training, Lion-optimizer, sign-operations | 20cea6c1b36ae5f69c48427a68b67fbc.md |
| 31 | FERERO: A Flexible Framework for Preference-Guided Multi-Obj | multi-objective-learning, Pareto-optimization, preference-guided | 21a33eba893ca3890e395651b38810df.md |
| 32 | Achieving Near-Optimal Convergence for Distributed Minimax O | distributed-optimization, minimax, adaptive-stepsize | 2302f4e66752149be7f63015a548a84c.md |
| 33 | DropBP: Accelerating Fine-Tuning of Large Language Models by | fine-tuning, backward-propagation, llm-efficiency | 240225294cdd2c9b692c2519d3278a08.md |
| 34 | Public-data Assisted Private Stochastic Optimization: Power  | differential-privacy, public-data, stochastic-convex-optimization | 243697ace81f57daef8737ff2c5cffd3.md |
| 35 | Gradient Methods for Online DR-Submodular Maximization with  | dr-submodular, online-learning, stochastic-constraints | 249b8d8f41970822651435629e68a6e1.md |
| 36 | Nesterov acceleration despite very noisy gradients | nesterov-acceleration, noisy-gradients, convex-optimization | 24d2dd6dc9b79116f8ebc852ddb9dc94.md |
| 37 | The Collusion of Memory and Nonlinearity in Stochastic Appro | stochastic-approximation, Markovian-data, constant-stepsize | 2676109d49d1eb26d6bc584a8f556305.md |
| 38 | Adaptive Variance Reduction for Stochastic Optimization unde | variance-reduction, adaptive-optimization, STORM | 272efd3a6091ceefcbc79f1f3a6fdba4.md |
| 39 | BAdam: A Memory Efficient Full Parameter Optimization Method | block-coordinate-descent, memory-efficient-optimization, llm-finetuning | 2c570b0f9938c7a58a612e5b00af9cc0.md |
| 40 | First-Order Minimax Bilevel Optimization | minimax-bilevel-optimization, first-order-methods, multi-task-learning | 2c8047bf3ed8ef6905351608d641f02f.md |
| 41 | Mirror and Preconditioned Gradient Descent in Wasserstein Sp | wasserstein-space-optimization, mirror-descent, preconditioned-gradient | 2cf153951b5e9b39564fc4a0ef6adc1a.md |
| 42 | Policy Mirror Descent with Lookahead | policy-mirror-descent, lookahead, reinforcement-learning | 2e8eaf43f20948ad878e6b8902797d1e.md |
| 43 | Stochastic Optimization Algorithms for Instrumental Variable | instrumental-variable-regression, stochastic-optimization, streaming-data | 2ea07a4acbf7e38913062fd69a70805f.md |
| 44 | Universality of AdaGrad Stepsizes for Stochastic Optimizatio | adagrad, stochastic-optimization, adaptive-gradient | 2f1232aa8c790447419d3aadbc9927b4.md |
| 45 | Near-Optimal Distributed Minimax Optimization under the Seco | distributed-optimization, minimax, variance-reduction | 314f72f80227e21cd95f402c73f0d360.md |
| 46 | Rethinking Memory and Communication Costs for Efficient Data | distributed-training, large-language-models, data-parallelism | 318f3ae8be3c97cb7555e1c932f472a1.md |
| 47 | A Layer-Wise Natural Gradient Optimizer for Training Deep Ne | natural-gradient, second-order-optimization, layer-wise | 31fb284a0aaaad837d2930a610cd5e50.md |
| 48 | MomentumSMoE: Integrating Momentum into Sparse Mixture of Ex | mixture-of-experts, momentum-optimization, sparse-routing | 32eb183794ef5ef9a3ab1d40a3d2b303.md |
| 49 | Constrained Sampling with Primal-Dual Langevin Monte Carlo | constrained-sampling, langevin-monte-carlo, primal-dual-optimization | 33c674cb3ce9dae35021930d8d63308f.md |
| 50 | Weight for Robustness: A Comprehensive Approach towards Opti | byzantine-robustness, asynchronous-distributed-learning, fault-tolerance | 3504a4fa45685d668ce92797fbbf1895.md |
| 51 | Computation-Aware Gaussian Processes: Model Selection And Li | gaussian-processes, model-selection, computational-uncertainty | 379ea6eb0faad176b570c2e26d58ff2b.md |
| 52 | Universal Online Convex Optimization with $1$ Projection per | universal-online-learning, convex-optimization, projection-efficiency | 37e90dcf2909b5068858b34b5239f187.md |
| 53 | Efficient Sign-Based Optimization: Accelerating Convergence  | signSGD, variance-reduction, convergence-acceleration | 3b7db05c0e383518d789b6e93131f1f0.md |
| 54 | Byzantine Robustness and Partial Participation Can Be Achiev | byzantine-fault-tolerance, distributed-learning, gradient-clipping | 3db3e1f192877e47bf48c93cae238e51.md |
| 55 | Mean-Field Langevin Dynamics for Signed Measures via a Bilev | mean-field-langevin-dynamics, signed-measures, bilevel-optimization | 3e0f495e21bdbdb4251792d0fff57928.md |
| 56 | Robust and Faster Zeroth-Order Minimax Optimization: Complex | zeroth-order-optimization, minimax-problems, nonconvex-optimization | 413885e70482b95dcbeeddc1daf39177.md |
| 57 | Inexact Augmented Lagrangian Methods for Conic Optimization: | augmented-Lagrangian, conic-optimization, linear-convergence | 480eb35745feb11c9120b666f640893e.md |
| 58 | Optimal Algorithms for Online Convex Optimization with Adver | online-convex-optimization, adversarial-constraints, regret-bounds | 486ff0b164cf92b0255fe39863bcf99e.md |
| 59 | Accelerated Regularized Learning in Finite N-Person Games | accelerated-learning, N-person-games, Nesterov-acceleration | 487667c56596138d36bbaa3bd8aac6df.md |
| 60 | DOPPLER: Differentially Private Optimizers with Low-pass Fil | differential-privacy, DP-SGD, noise-reduction | 49c466ccc038f39b08b1980a2b06673c.md |
| 61 | VeLoRA: Memory Efficient Training using Rank-1 Sub-Token Pro | memory-efficient-training, LoRA, rank-1-projections | 4a9eaf6dff3fdac9ab1aaf4c0fe2d563.md |
| 62 | Approximated Orthogonal Projection Unit: Stabilizing Regress | natural-gradient, orthogonal-projection, soft-sensor-online-learning | 4ae7d78ebbe48f772e31c5c3fcc04c43.md |
| 63 | Parameter-free Clipped Gradient Descent Meets Polyak | parameter-free-optimization, clipped-gradient-descent, polyak-stepsize | 4ebba705ffdee81e0a638c99fe066ce2.md |
| 64 | An Accelerated Gradient Method for Convex Smooth Simple Bile | bilevel-optimization, accelerated-gradient, convex-optimization | 4fc81f4cd2715d995018e0799262176b.md |
| 65 | Gradient-Free Methods for Nonconvex Nonsmooth Stochastic Com | gradient-free, nonconvex-nonsmooth, stochastic-compositional-optimization | 50be7e77b9c883144940be925b608acc.md |
| 66 | Remove that Square Root: A New Efficient Scale-Invariant Ver | AdaGrad, scale-invariant, adaptive-optimization | 54ca2c45ce17dbd9ebad7ab0f39c825a.md |
| 67 | Stepping on the Edge: Curvature Aware Learning Rate Tuners | learning-rate-tuning, sharpness, curvature | 555479a201da27c97aaeed842d16ca49.md |
| 68 | Fast TRAC: A Parameter-Free Optimizer for Lifelong Reinforce | lifelong-reinforcement-learning, plasticity-loss, parameter-free-optimizer | 5b76d77e7095c6480ed827b85f0c2878.md |
| 69 | SAMPa: Sharpness-aware Minimization Parallelized | sharpness-aware-minimization, parallelization, generalization | 5bf2b802e24106064dc547ae9283bb0c.md |
| 70 | Online Non-convex Learning in Dynamic Environments | online-learning, non-convex-optimization, dynamic-environments | 5d1233f819202ade06023346df80a6d2.md |
| 71 | Fast Iterative Hard Thresholding Methods with Pruning Gradie | iterative-hard-thresholding, sparse-learning, gradient-pruning | 5eaa54503005d9125ad6aa3044e912d8.md |
| 72 | LSH-MoE: Communication-efficient MoE Training via Locality-S | mixture-of-experts, locality-sensitive-hashing, communication-efficiency | 61674667d642ae52f6bb281bea90ee29.md |
| 73 | Freya PAGE: First Optimal Time Complexity for Large-Scale No | asynchronous-distributed-optimization, nonconvex-finite-sum, heterogeneous-workers | 618c8af8efd19b4ce90b8864a764d0fa.md |
| 74 | Shuffling Gradient-Based Methods for Nonconvex-Concave Minim | shuffling-gradient, minimax-optimization, nonconvex-concave | 649f080d8891ab4d4b262cb9cd52e69a.md |
| 75 | Single-Loop Stochastic Algorithms for Difference of Max-Stru | non-convex-optimization, weakly-convex, difference-of-max | 67e79c8e9b11f068a7cafd79505175c0.md |
| 76 | Functionally Constrained Algorithm Solves Convex Simple Bile | bilevel-optimization, convex-optimization, first-order-methods | 69f98acf161316ed896047e45da3bc0c.md |
| 77 | Leveraging partial stragglers within gradient coding | gradient-coding, stragglers, distributed-learning | 6f1cacd88ac241bf51266d9d6594ab32.md |
| 78 | S-SOS: Stochastic Sum-Of-Squares for Parametric Polynomial O | polynomial-optimization, sum-of-squares, stochastic-parameters | 710f3f8473b93394505a082f9a8f3ba2.md |
| 79 | SPARKLE: A Unified Single-Loop Primal-Dual Framework for Dec | decentralized-optimization, bilevel-optimization, primal-dual | 72f9c316440c384a95c88022fd78f066.md |
| 80 | Improving the Training of Rectified Flows | rectified-flows, diffusion-models, ode-sampling | 7343a5c976f8399880b695267f1f9e9f.md |
| 81 | The Sample Complexity of Gradient Descent in Stochastic Conv | gradient-descent, sample-complexity, stochastic-convex-optimization | 7571c9d44179c7988178593c5b62a9b6.md |
| 82 | Memory-Efficient LLM Training with Online Subspace Descent | memory-efficient-training, LLM, subspace-descent | 760d09bcc06b949f5ac4b6a918739aa8.md |
| 83 | Heterogeneity-Guided Client Sampling: Towards Fast and Effic | federated-learning, client-sampling, non-iid-data | 7886b9bafe76c52fd568db10ff9772df.md |
| 84 | The Poisson Midpoint Method for Langevin Dynamics:  Provably | Langevin-dynamics, diffusion-models, discretization | 796455f65fd2cbe049112a2d2d4488cb.md |
| 85 | OptEx: Expediting First-Order Optimization with Approximatel | first-order-optimization, parallelization, convergence | 7c06d57601163b03fbd132dbf925eff7.md |
| 86 | Sample-Efficient Constrained Reinforcement Learning with Gen | constrained-mdp, reinforcement-learning, momentum-acceleration | 7e7b768198d24d883d69704eee57efb0.md |
| 87 | Provably Faster Algorithms for Bilevel Optimization via With | bilevel-optimization, without-replacement-sampling, stochastic-gradient | 8258e815fa93aa59441ad526cc828c53.md |
| 88 | Large Stepsize Gradient Descent for Non-Homogeneous Two-Laye | large-stepsize, gradient-descent, margin-maximization | 835a0185f61867a1ea0f86155489839a.md |
| 89 | ADOPT: Modified Adam Can Converge with Any $\beta_2$ with th | adam-optimizer, convergence-theory, adaptive-gradient-methods | 84d286e32bbee8fa3a86ee9c50e00081.md |
| 90 | Tighter Convergence Bounds for Shuffled SGD via Primal-Dual  | shuffled-sgd, primal-dual-analysis, convergence-bounds | 84d395725a9b40cb4a49d84478ac24c7.md |
| 91 | Does Worst-Performing Agent Lead the Pack? Analyzing Agent D | distributed-sgd, federated-learning, asymptotic-analysis | 852f50969a9e523ec41d26f2f68bd456.md |
| 92 | Small steps no more: Global convergence of stochastic gradie | stochastic-gradient-bandits, global-convergence, policy-optimization | 8815c983a1f46b477fe4fbf7042a3ba3.md |
| 93 | Faster Accelerated First-order Methods for Convex Optimizati | accelerated-primal-dual-algorithms, convex-optimization, strongly-convex-constraints | 8d8e060d9a3312ae12f42adf0da6ec7c.md |
| 94 | An Accelerated Algorithm for Stochastic Bilevel Optimization | bilevel-optimization, unbounded-smoothness, stochastic-optimization | 8ee4dfc3bac3d53d36fb9c0c72ec2a9f.md |
| 95 | Hierarchical Federated Learning with Multi-Timescale Gradien | hierarchical-federated-learning, gradient-correction, multi-timescale-optimization | 8fb96e8d0fbf591b1fa1ad85653d8417.md |
| 96 | REDUCR: Robust Data Downsampling using Class Priority Reweig | data-downsampling, class-imbalance, online-batch-selection | 96ddbf813f042e8ff891b4d6f7149bb6.md |
| 97 | Don't Compress Gradients in Random Reshuffling: Compress Gra | gradient-compression, random-reshuffling, distributed-training | 99c80ceb10cb674110f03b2def6a5b76.md |
| 98 | A-FedPD: Aligning Dual-Drift is All Federated Primal-Dual Le | federated-learning, primal-dual-optimization, drift-alignment | 9bb4d1b3fbeed86a0e854d736ea1d293.md |
| 99 | Improving the Worst-Case Bidirectional Communication Complex | distributed-optimization, communication-compression, nonconvex | a1d20cc72a21ef971d7e49a90d8fa56f.md |
| 100 | Immiscible Diffusion: Accelerating Diffusion Training with N | diffusion-models, noise-assignment, training-acceleration | a422a2f016c14406a01ddba731c0969a.md |
| 101 | Stochastic Newton Proximal Extragradient Method | stochastic-optimization, newton-method, superlinear-convergence | a51a0d42d794c8adf416196aae9f0974.md |
| 102 | Memory-Efficient Gradient Unrolling for Large-Scale Bi-level | bi-level-optimization, gradient-unrolling, memory-efficiency | a5321f64005b0d4a94d0b18e84e19f48.md |
| 103 | Noisy Dual Mirror Descent: A Near Optimal Algorithm for Join | differential-privacy, mirror-descent, resource-allocation | a6e1f6963f65bcc4854691a15460dbd8.md |
| 104 | Spectral-Risk Safe Reinforcement Learning with Convergence G | risk-constrained-RL, spectral-risk-measures, convergence-guarantees | a7fbf054c80d26e5b4ed67588ea384f0.md |
| 105 | SLowcalSGD : Slow Query Points Improve Local-SGD for Stochas | local-SGD, distributed-learning, heterogeneous-data | a97b58c4f7551053b0512f92244b0810.md |
| 106 | Adaptive and Optimal Second-order Optimistic Methods for Min | minimax-optimization, second-order-methods, adaptive-step-size | ab41313eaa3cbedbe491c24cbfe6547d.md |
| 107 | Optimal and Approximate Adaptive Stochastic Quantization | quantization, adaptive-quantization, stochastic-optimization | ab6a2c6ee757afe43882121281f6065c.md |
| 108 | Adam with model exponential moving average is effective for  | Adam-optimizer, exponential-moving-average, nonconvex-optimization | ac8ec9b4d94c03f0af8c4fe3d5fad4fd.md |
| 109 | A Primal-Dual-Assisted Penalty Approach to Bilevel Optimizat | bilevel-optimization, primal-dual, coupled-constraints | acccb791886d5d811fe4e16e98c26633.md |
| 110 | Reverse Transition Kernel: A Flexible Framework to Accelerat | diffusion-inference, reverse-SDE, acceleration | ad62d81bb6edee5f9b33f5e0d34a7943.md |
| 111 | Achieving Linear Convergence with Parameter-Free Algorithms  | decentralized-optimization, parameter-free, linear-convergence | ae1752315811107ee07aa5ab06cead71.md |
| 112 | Lower Bounds and Optimal Algorithms for Non-Smooth Convex De | decentralized-optimization, non-smooth-convex, time-varying-networks | af10f27d0a48175e486a647c06c7a9c6.md |
| 113 | B-ary Tree Push-Pull Method is Provably Efficient for Distri | distributed-learning, push-pull, b-ary-tree | b0d4b9d3dc41b36cad1d36ddd27858ab.md |
| 114 | Stochastic Zeroth-Order Optimization under Strongly Convexit | zeroth-order-optimization, minimax-sample-complexity, strongly-convex | b444ad72520a5f5c467343be88e352ed.md |
| 115 | Stabilized Proximal-Point Methods for Federated Optimization | federated-learning, proximal-point, communication-complexity | b4b75092bb44a14815be33d052aa47f5.md |
| 116 | Adaptive Proximal Gradient Method for Convex Optimization | proximal-gradient, adaptive-methods, convex-optimization | b676cbd80be73a4a7af178f12035a801.md |
| 117 | CRONOS: Enhancing Deep Learning with Scalable GPU Accelerate | convex-neural-networks, GPU-acceleration, two-layer-networks | ba9e3d60610f3525717665966d86e0cd.md |
| 118 | A Framework for Bilevel Optimization on Riemannian Manifolds | bilevel-optimization, riemannian-manifolds, hypergradient | bc1c5e5fb8ed1ef9b9b5abced2022e40.md |
| 119 | Efficient Federated Learning against Heterogeneous and Non-s | federated-learning, client-unavailability, non-stationary | bcaebb606df0c8c714756660e4a3bd7c.md |
| 120 | How Does Black-Box Impact the Learning Guarantee of Stochast | stochastic-compositional-optimization, black-box-optimization, AUC-maximization | c3010e98dc44b6f76df7cf82b5e12c77.md |
| 121 | Learning General Parameterized Policies for Infinite Horizon | constrained-MDPs, average-reward, primal-dual | c46c759679acea07d7ea92823ea1e290.md |
| 122 | Random Function Descent | stochastic-optimization, random-function, step-size-selection | c980ad0fb46f0cfb0faabcd42b30a67a.md |
| 123 | Why Warmup the Learning Rate? Underlying Mechanisms and Impr | learning-rate-warmup, sgd, adam-optimizer | ca98452d4e9ecbc18c40da2aa0da8b98.md |
| 124 | Matching the Statistical Query Lower Bound for $k$-Sparse Pa | sparse-parity, stochastic-gradient-descent, statistical-query | cd38340309ed34d886b9cd6e35059606.md |
| 125 | Improved Particle Approximation Error for Mean Field Neural  | mean-field-Langevin-dynamics, particle-approximation, neural-network-optimization | ce5f18eba5e5e9c7c166062300c677c3.md |
| 126 | One-Step Diffusion Distillation through Score Implicit Match | diffusion-distillation, score-matching, one-step-generation | d107ca794d83c8242e357e6a43a068f4.md |
| 127 | Last-Iterate Convergence for Generalized Frank-Wolfe in Mono | Frank-Wolfe, variational-inequalities, last-iterate-convergence | d10f451f973846d20dae8674c493fa3c.md |
| 128 | Exploring Jacobian Inexactness in Second-Order Methods for V | variational-inequalities, second-order-methods, Jacobian-inexactness | d1ca7877cdaf3201ecfa95b1240f7942.md |
| 129 | Truncated Variance Reduced Value Iteration | Markov-decision-process, variance-reduction, randomized-algorithms | d529b943af3dba734f8a7d49efcb6d09.md |
| 130 | Derivatives of Stochastic Gradient Descent in parametric opt | stochastic-gradient-descent, hyperparameter-optimization, parametric-optimization | d751402fe54c65e766fc958d78930803.md |
| 131 | Scalable Bayesian Optimization via Focalized Sparse Gaussian | bayesian-optimization, sparse-gaussian-processes, scalability | da30215ee52c1daaaaddada8137cfd0b.md |
| 132 | On the Optimal Time Complexities in Decentralized Stochastic | decentralized-optimization, asynchronous-SGD, time-complexity | dd850be1e74582b68fa82078f3fc6d4d.md |
| 133 | On the Convergence of Loss and Uncertainty-based Active Lear | active-learning, convergence-analysis, SGD | ddb0a18cc21b98fffb4b69c43f9b56f5.md |
| 134 | No-regret Learning in Harmonic Games: Extrapolation in the F | no-regret-learning, harmonic-games, extrapolation | df5a8051be8bf4eaaabceb67c6d48332.md |
| 135 | Stochastic Extragradient with Flip-Flop Shuffling & Anchorin | extragradient, minimax-optimization, shuffling | df658fe5097f65485ad80b06e6cb30dd.md |
| 136 | The Power of Extrapolation in Federated Learning | federated-learning, server-extrapolation, fedprox | e0b6f389739496e363a89155c9448a8a.md |
| 137 | Convergence of $\text{log}(1/\epsilon)$ for Gradient-Based A | zero-sum-games, gradient-algorithms, smoothed-analysis | e3b1291b7529063172d927588d2b03a1.md |
| 138 | Last-Iterate Global Convergence of Policy Gradients for Cons | constrained-reinforcement-learning, policy-gradient, global-convergence | e47470631adb188a30f14c9738fe157b.md |
| 139 | 4-bit Shampoo for Memory-Efficient Network Training | second-order-optimization, 4-bit-quantization, memory-efficient-training | e5b4633454cb2174779d294ccda02318.md |
| 140 | Regularized Adaptive Momentum Dual Averaging with an Efficie | adaptive-momentum, structured-sparsity, neural-network-optimization | e83b86156555ab9692743f9f8f67adf1.md |
| 141 | Private Algorithms for Stochastic Saddle Points and Variatio | differential-privacy, saddle-point-problems, non-euclidean-geometry | e88476b0ce9d445037422fe68ca097e4.md |
| 142 | Safe and Sparse Newton Method for Entropic-Regularized Optim | optimal-transport, sinkhorn-algorithm, newton-method | ea8620683340facbd5f754dd169e0980.md |
| 143 | Bayesian Online Natural Gradient (BONG) | variational-bayes, sequential-inference, natural-gradient | ecffd829f90b0a4b6aa017b6df15904f.md |
| 144 | Surge Phenomenon in Optimal Learning Rate and Batch Size Sca | learning-rate-scaling, batch-size, adam-optimizer | ef74413c7bf1d915c3e45c72e19a5d32.md |
| 145 | Accelerating Diffusion Models with Parallel Sampling: Infere | diffusion-models, parallel-sampling, sub-linear-inference | f162fa05675e3db4a733aafc081653cf.md |
| 146 | Adam on Local Time: Addressing Nonstationarity in RL with Re | adam-optimizer, nonstationarity, reinforcement-learning | f2733d3b0dde1d74995f35a9cf442d38.md |
| 147 | Drago: Primal-Dual Coupled Variance Reduction for Faster Dis | distributionally-robust-optimization, primal-dual, variance-reduction | f2c5a0d8e445cc359eb446521f438ee3.md |
| 148 | Computing the Bias of Constant-step Stochastic Approximation | stochastic-approximation, Markovian-noise, constant-step-size | f949c1f490beb42124a267b7476cd353.md |
| 149 | Quantitative Convergences of Lie Group Momentum Optimizers | lie-groups, momentum-optimization, variational-optimization | fda447b299f186d22b2de3ec23d75dcf.md |
| 150 | Penalty-based Methods for Simple Bilevel Optimization under  | bilevel-optimization, penalty-methods, Holderian-error-bounds | fe61e76998bbe3db53a6a48fa58207e9.md |
| 151 | High-probability complexity bounds for stochastic non-convex | minimax-optimization, high-probability-bounds, stochastic-gradient | fec946957ce1af51a61e8f2d851ac98f.md |
| 152 | First-Order Methods for Linearly Constrained Bilevel Optimiz | bilevel-optimization, first-order-methods, linear-constraints | ffd86e56e6403d63dd6face033060e5a.md |
