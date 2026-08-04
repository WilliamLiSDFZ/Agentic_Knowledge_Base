# Relational DNN Verification With Cross Executional Bound Refinement

**Source**: https://proceedings.mlr.press/v235/banerjee24a.html

## [POSITIVE] Cross-Executional Bound Refinement
Jointly optimizing parametric activation bounds (alpha parameters) across multiple DNN executions simultaneously, leveraging inter-execution dependencies rather than optimizing each execution independently.

**Delta**: up to +16.5% UAP accuracy on MNIST, up to +22% UAP accuracy on CIFAR10, up to -8 hamming distance (40% reduction)
**Condition**: Relational DNN verification tasks including k-UAP and worst-case hamming distance across all tested networks and datasets

**Evidence**: "RACoon gains up to +16.5% and up to +22% improvement in the worst-case UAP accuracy (averaged over 10 runs) for MNIST and CIFAR10 DNNs respectively. Similarly, RACoon reduces the worst-case hamming distance (averaged over 10 runs) up to 8 which is up to 40% reduction for binary strings of size 20."

## [POSITIVE] LP Formulation for Relational Verification
Formulating relational verification as a linear program that jointly reasons about multiple executions using fixed linear approximations, proving exactness for fixed approximations.

**Delta**: t*(G) improved to -0.05 from -0.2 for MNIST DiffAI DNN
**Condition**: When used with fixed linear approximations; insufficient alone when approximations are not jointly optimized

**Evidence**: "For fixed linear approximations {(L1, b1), (L2, b2)} of N, the LP formulation is exact i.e. it always proves the absence of common adversarial perturbation if it can be proved with {(L1, b1), (L2, b2)}"

## [POSITIVE] Lagrangian Dual Closed-Form Derivation
Deriving a differentiable closed-form of the Lagrangian dual function G(lambda) that preserves cross-execution dependencies via Lagrange multipliers, enabling joint optimization of parameters from multiple executions.

**Delta**: t*(G) >= t*(G_bar) always (Theorem 4.2), with strict improvement in certain conditions
**Condition**: Multi-execution relational verification where cross-execution dependencies exist

**Evidence**: "Unlike G(alpha), G(lambda) relates linear approximations from two different executions using (lambda_1, lambda_2) enabling joint optimization over (alpha_1, alpha_2)... t*(G) >= t*(G_bar) (Theorem 4.2)"

## [NEGATIVE] Naive Independent Dual Optimization (G_bar)
Solving the inner minimization problem for each execution separately and combining with max, ignoring cross-execution dependencies during optimization.

**Delta**: strictly worse than joint optimization G(lambda) per Theorem 4.2
**Condition**: When used as the optimization objective for relational verification instead of the joint dual G(lambda)

**Evidence**: "G(alpha) produces a suboptimal result since it ignores cross-execution dependencies and misses out on the benefits of jointly optimizing (alpha_1, alpha_2)."

## [POSITIVE] MILP Formulation with Cross-Executional Bounds
Encoding the relational verification problem as a MILP using cross-executionally refined linear approximations, introducing only O(k * n_l) integer variables by encoding only the output specification.

**Delta**: most precise results among all components tested
**Condition**: Full RACoon pipeline; more scalable than naive MILP encoding which requires O(k * n_r) integer variables

**Evidence**: "As expected, RACoon (cross-execution refinement with MILP) yields the most precise results while cross-execution refinement without MILP achieves the second-best results with notably faster runtime."

## [POSITIVE] Cross-Executional Bound Refinement Without MILP
Using only the cross-executional bound refinement step without the subsequent MILP formulation to prove relational properties.

**Delta**: second-best precision with notably faster runtime than full RACoon
**Condition**: When runtime is prioritized over maximum precision; useful when non-relational verification fails on all executions

**Evidence**: "cross-execution refinement without MILP achieves the second-best results with notably faster runtime. Note that only cross-executional bound refinement without MILP can prove the absence of common adversarial perturbation for a set of executions even if non-relational verification fails on all of them."

## [POSITIVE] Eliminating Individually Verified Executions
Running non-relational verifiers first and removing already-verified executions from subsequent cross-executional refinement steps to reduce computational cost.

**Delta**: no loss in precision (proven in Appendix Theorem B.12)
**Condition**: k-UAP and worst-case hamming distance relational properties

**Evidence**: "RACoon eliminates the executions already verified with the non-relational verifier and does not consider them for subsequent steps... we formally prove the correctness of the elimination technique in Appendix Theorem B.12 and showcase eliminating verified executions does not lead to any loss in precision of RACoon."

## [POSITIVE] Greedy Selection of Execution Subsets (k0, k1 hyperparameters)
Selecting top-k0 unverified executions based on output specification violation scores and limiting subset size to k1 for cross-executional refinement, avoiding exponential blowup over all 2^k subsets.

**Delta**: larger k0 and k1 improve precision but increase runtime
**Condition**: Relational properties over k executions where k0 <= 10 in practice

**Evidence**: "As expected, with larger k0 and k1 RACoon's precision improves but it also increases RACoon's runtime."

## [NEGATIVE] I/O Formulation (SOTA Baseline - Input-Only Dependency Tracking)
Computing linear approximations of the DNN independently for each execution using a non-relational verifier, then adding linear constraints only at the input layer to capture cross-execution dependencies.

**Delta**: outperformed by RACoon by up to +16.5% UAP accuracy on MNIST and +22% on CIFAR10
**Condition**: Relational DNN verification; limited because it only captures input-layer dependencies, not hidden-layer dependencies

**Evidence**: "ignoring cross-execution dependencies while computing provably correct linear approximations of the DNN for each execution leads to the loss of precision (as confirmed by our experiments in Section 6)... RACoon outperforms current SOTA baseline I/O formulation on all DNNs for both the relational properties."

## [NEGATIVE] Non-Relational Verification Baseline (Independent Executions)
Treating all k executions of the DNN as independent and solving k individual verification problems without any cross-execution dependency tracking.

**Delta**: worst performance among all methods; e.g., 38.5% vs RACoon's 54.0% UAP accuracy on MNIST ConvSmall Standard
**Condition**: Relational verification tasks; fundamentally unable to exploit cross-execution dependencies

**Evidence**: "the relational verifier in (Khedr & Shoukry, 2023) treats all k executions of the DNN as independent and loses precision as a result of this... in all 4 cases in Fig. 1 individual refinement fails to prove the absence of common adversarial perturbation while cross-executional refinement succeeds."

## [POSITIVE] Individual Bound Refinement with MILP
Applying parametric bound refinement (alpha-CROWN) independently per execution and then using MILP formulation, without cross-execution dependency tracking during refinement.

**Delta**: more precise than I/O formulation for some cases (MNIST and CIFAR10 standard DNNs), but less precise than cross-executional refinement
**Condition**: Standard (non-robustly trained) DNNs on MNIST and CIFAR10; intermediate approach between non-relational and full cross-executional refinement

**Evidence**: "for some cases (i.e. MNIST and CIFAR10 standard DNNs) I/O formulation (static linear approximation with MILP) outperforms individual refinements while both individual refinement with MILP and cross-execution refinement are always more precise."

## [POSITIVE] Parametric Activation Bounds (alpha parameters)
Using parametric linear bounds for ReLU activations where the slope parameter alpha in [0,1] is optimized via gradient descent rather than using static bounds.

**Delta**: enables optimization-based precision improvement over static bounds
**Condition**: DNN verification with ReLU activations; sub-optimal when optimized independently per execution for relational properties

**Evidence**: "Recent works such as (Xu et al., 2021), instead of static linear bounds, use parametric linear bounds and refine the parameters with scalable differential optimization techniques to facilitate verification of the property... existing works can only optimize the alpha parameters w.r.t individual executions independently making these methods sub-optimal for relational verification."

## [POSITIVE] Projected Gradient Descent for Joint Parameter Optimization
Using projected gradient descent (specifically Adam optimizer) to maximize the closed-form dual function G(lambda) over joint parameters from multiple executions while satisfying constraints.

**Delta**: t*_i(G) > t*_i(G_bar) at each iteration i across all 4 tested configurations
**Condition**: Cross-executional bound refinement optimization; may not find global maximum but correctness does not require it

**Evidence**: "For each iteration i, t*_i(G) > t*_i(G_bar) shows that cross-executional refinement is more effective in learning parametric bounds that can facilitate relation verification."

## [POSITIVE] Greedy Subproblem Selection for Conjunction of Linear Inequalities
Greedily selecting which subproblems to use for bound refinement when output specifications involve conjunctions of m linear inequalities, avoiding the exponential m^n subproblem blowup.

**Delta**: avoids exponential blowup while maintaining provable correctness
**Condition**: Output specifications with conjunction of multiple linear inequalities and large m, n

**Evidence**: "the number of subproblems in the worst case can be m^n which is practically intractable for large m and n. Hence, we greedily select which subproblems to use for bound refinement to avoid exponential blow-up in the runtime while ensuring the bound refinement remains provably correct"
