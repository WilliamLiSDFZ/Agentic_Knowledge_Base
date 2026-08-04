# Verifying message-passing neural networks via topology-based bounds tightening

**Source**: https://proceedings.mlr.press/v235/hojny24a.html

## [POSITIVE] Static Bounds Tightening (sbt)
A topology-based bounds tightening routine that computes tighter variable bounds by considering graph structure and available budgets in a single forward pass, rather than using plain interval arithmetic over all possible neighbors.

**Delta**: ~3x faster than SCIPbasic; ENZYMES sgm-time reduced from 37.81s to 21.26s; solves 5831 vs 5579 instances (ENZYMES, s=2)
**Condition**: Graph classification tasks (ENZYMES, MUTAG); most beneficial on robust instances

**Evidence**: "SCIPsbt is around three times faster than SCIPbasic and solves more instances within the same time limit."

## [POSITIVE] Aggressive Bounds Tightening (abt)
A dynamic bounds tightening routine that operates within the branch-and-bound tree, using already-fixed edge variables (Au,v) to further tighten bounds at each node via local cutting planes.

**Delta**: SCIPabt ~10% faster than SCIPsbt on robust MUTAG instances in sgm-time (29% in arithmetic mean); 412 robust ENZYMES instances significantly faster
**Condition**: Harder graph classification instances (MUTAG robust instances); most pronounced at global budgets of 2% and 3%

**Evidence**: "For the MUTAG instances (which are harder to solve than ENZYMES), SCIPabt is roughly 10% faster than SCIPsbt in shifted geometric mean (29% in arithmetic mean)."

## [NEGATIVE] Aggressive Bounds Tightening (abt) on non-robust instances
Applying abt to non-robust instances where finding a feasible attack is sufficient; extra cutting planes may hinder heuristics from finding a feasible attack quickly.

**Delta**: SCIPabt slower than SCIPsbt on some instances; avg-time 246.02s vs 230.59s for SCIPsbt on all ENZYMES instances
**Condition**: Non-robust instances where finding a feasible attack is sufficient

**Evidence**: "SCIPabt might even be slower than SCIPsbt in some instances... the extra cutting planes added in abt may slow down finding a feasible attack."

## [NEGATIVE] Static Bounds Tightening on non-robust MUTAG instances
Applying sbt to MUTAG graph classification where most instances are non-robust; tighter bounds are unnecessary when only a feasible attack needs to be found.

**Delta**: GRBsbt avg-time 59.93s vs GRBbasic 34.58s on all MUTAG instances
**Condition**: Non-robust graph classification instances (MUTAG)

**Evidence**: "Considering all instances from MUTAG, it seems like static bounds tightening slows down the solving process. The reason is that most MUTAG instances are not robust, i.e., finding good bounds on the objective value is unnecessary, finding a feasible attack instead is sufficient."

## [NEUTRAL] Optimization-Based Bound Tightening (OBBT)
For each variable, solves an LP by changing the objective to the variable's lower or upper bound with all binary variables relaxed, yielding tighter bounds than interval arithmetic at high computational cost.

**Delta**: Average OBBT bound computation time 6045.02s; average solving time with OBBT 331.60s vs SCIPsbt 336.41s
**Condition**: Robust MUTAG instances with s=2; not recommended for general GNN verification

**Evidence**: "The improvement of OBBT w.r.t. the solving time is quite limited, despite its high time cost on computing bounds."

## [NEUTRAL] Big-M formulation for bilinear terms
Introduces auxiliary variables to replace bilinear terms Au,v * x_u in the MPNN encoding, linearizing the product of binary edge variables and continuous node features.

**Delta**: Enables MIP encoding of MPNNs with non-fixed graph structure
**Condition**: Required for any MPNN verification with topological perturbations

**Evidence**: "the Zhang et al. (2023) big-M formulation introduces auxiliary variables x^(l-1)_{u->v} to replace the bilinear terms A_{u,v} x_u^(l-1) and linearly encodes x-bar^(l)_v"

## [NEUTRAL] Big-M formulation for ReLU activation
Encodes ReLU nonlinearity using binary variables sigma and big-M constraints, controlling the on/off state of each activation unit.

**Delta**: Enables exact MIP-based verification of ReLU MPNNs
**Condition**: All MPNN verification problems with ReLU activation

**Evidence**: "Anderson et al. (2020) proposed a big-M formulation... where sigma^(l)_{v,f} in {0,1} controls the on/off of the activation"

## [POSITIVE] Topology-based bounds tightening improving SCIP vs Gurobi gap
Implementing topology-based bounds tightening in the open-source solver SCIP reduces the performance gap between SCIP and the commercial solver Gurobi.

**Delta**: Time penalty factor reduced from 10x to 3x for robust instances
**Condition**: Graph classification benchmarks (ENZYMES, MUTAG)

**Evidence**: "making the open-source solver SCIP nearly as performant as the commercial solver Gurobi, e.g., improving the time penalty of the open-source solver from a factor of 10 to a factor of 3 for robust instances."

## [NEGATIVE] Topology-based bounds tightening for node classification
Applying sbt and abt to node classification problems where only edge removal is considered (P2 perturbations).

**Delta**: SCIPbasic avg-time 0.10s vs SCIPsbt 0.17s vs SCIPabt 0.46s on Cora; all methods solve all instances instantly
**Condition**: Node classification (Cora, CiteSeer) with edge-removal-only perturbations

**Evidence**: "Only removing edges results in simple verification problems: all methods can solve all instances instantly. Adding more cutting planes is not helpful as this could hinder heuristics to find a feasible attack (in case of nonrobustness) or result in solving more (difficult) LPs due to additional cutting planes."

## [POSITIVE] Parallel execution of SCIPsbt and SCIPabt
Running static and aggressive bounds tightening in parallel to exploit complementary strengths of each strategy.

**Delta**: 412 robust ENZYMES instances faster with SCIPabt, 512 faster with SCIPsbt
**Condition**: Graph classification with mixed robust and non-robust instances

**Evidence**: "We therefore propose running SCIPsbt and SCIPabt in parallel, this idea corresponds to the common observation in MIP that parallelizing multiple strategies (here: SCIPsbt and SCIPabt) yields more benefits than parallelizing just one algorithm."

## [POSITIVE] Local cutting planes for abt in branch-and-bound
Adding inequalities as local cutting planes valid only at the current branch-and-bound node and its children, encoding tightened bounds derived from fixed edge variables.

**Delta**: Enables dynamic tightening of ReLU interval bounds; fixes binary ReLU variables when pre-activation bounds are one-sided
**Condition**: Aggressive bounds tightening within SCIP branch-and-bound tree

**Evidence**: "we add local cutting planes to implement abt bounds... abt implies a dynamic tightening on ReLU interval bounds in MPNNs."

## [POSITIVE] Solving 266 additional graph classification instances
Topology-based bounds tightening enables solving instances that were previously unsolvable within the time limit.

**Delta**: +266 graph classification instances solved
**Condition**: Graph classification benchmarks with topology-based bounds tightening vs basic

**Evidence**: "solving an extra 266 graph classification instances after implementing topology-based bounds tightening in SCIP"
