# Trained Random Forests Completely Reveal your Dataset

**Source**: https://proceedings.mlr.press/v235/ferry24a.html

## [POSITIVE] Constraint Programming (CP) Formulation
Formulating the dataset reconstruction problem as a CP model solved using OR-Tools CP-SAT solver, leveraging constraint propagation, backtracking, and solution domain reduction

**Delta**: reconstruction error reaches 0 for deepest forests without bagging
**Condition**: Random forests trained without bootstrap aggregation, across all three datasets

**Evidence**: "When bagging is not used to train the RFs, the reconstruction error reaches 0 in all cases for the deepest forests"

## [POSITIVE] CP vs MILP Solver Choice
Using Constraint Programming instead of Mixed-Integer Linear Programming for solving the reconstruction problem

**Delta**: outperforms baseline
**Condition**: Especially effective when bagging is used; MILP extension for bagging is prohibitively large

**Evidence**: "having conducted experiments with both techniques, and as demonstrated in Appendix B, CP generally achieved better performance and permitted to handle bagging much more effectively"

## [POSITIVE] Bootstrap Aggregation (Bagging)
Training each tree on a bootstrap sample (random sampling with replacement) of the original training set, so not all examples are used in each tree and some appear multiple times

**Delta**: reconstruction error reaches a threshold and stops improving even for larger forests
**Condition**: Applied as a privacy protection mechanism against reconstruction attacks; reduces attack effectiveness compared to no-bagging setting

**Evidence**: "bagging intrinsically provides a form of protection regarding the training data. This is consistent with theoretical results stating that bagging provides (weak) differential privacy guarantees"

## [NEGATIVE] No Bootstrap Aggregation (No Bagging)
Training random forests without bootstrap aggregation, using all examples in each tree but with feature randomization

**Delta**: reconstruction error reaches 0
**Condition**: Makes the dataset completely reconstructable; worst-case privacy scenario

**Evidence**: "random forests trained without bootstrap aggregation but with feature randomization are susceptible to a complete reconstruction. This holds true even with a small number of trees."

## [POSITIVE] Maximum Log-Likelihood Objective
Orienting the CP search towards solutions that maximize the log-likelihood of the bootstrap sampling process, using the probability that each sample appears a given number of times in each tree

**Delta**: descriptive - guides search toward most likely reconstructions
**Condition**: Applied when bagging is used; when bagging is not used the objective becomes constant and the problem reduces to feasibility search

**Evidence**: "we orient the search towards the solutions (datasets) that are the most likely... Maximizing this probability is equivalent to maximizing its logarithm"

## [POSITIVE] Increasing Tree Depth (dmax)
Allowing trees to grow deeper by increasing or removing the maximum depth constraint

**Delta**: decreases reconstruction error toward 0 for no-bagging case
**Condition**: Applies across all three datasets; deeper trees provide more constraints for reconstruction

**Evidence**: "increasing the trees' depth or the number of trees in the forest decreases the reconstruction error as it provides more information regarding the training data"

## [POSITIVE] Increasing Number of Trees
Using more trees in the random forest ensemble

**Delta**: decreases reconstruction error
**Condition**: Applies across all three datasets; more trees provide more constraints for reconstruction

**Evidence**: "increasing the trees' depth or the number of trees in the forest decreases the reconstruction error as it provides more information regarding the training data"

## [NEUTRAL] Bootstrap Occurrence Bound (B = {0,...,7})
Limiting the maximum number of times a sample can appear in a bootstrap-sampled tree to 7, based on probabilistic analysis that higher values are extremely unlikely

**Delta**: probability of appearing more than 7 times is roughly 10^-5
**Condition**: Used for N=100 training examples; remains similar for larger N values

**Evidence**: "we will assume that a training example appears at most 7 times in any tree, since higher values are very unlikely... the probability of an example appearing more than 7 times in a bootstrap sampled training set is roughly 10^-5"

## [POSITIVE] Model Simplification Without Bagging
Simplifying the CP model when bagging is not used: fixing class variables in advance, making leaf assignment variables binary, and eliminating the objective function

**Delta**: solution times scale approximately linearly with number of trees
**Condition**: Only applicable when random forests are trained without bootstrap aggregation

**Evidence**: "the CP model can be significantly simplified... the objective function becomes constant, and the problem reduces to the search for a feasible solution"

## [POSITIVE] Symmetry Breaking Constraints (MILP)
Adding constraints to break symmetry within each class in the MILP formulation

**Delta**: descriptive - reduces search space
**Condition**: Applied in the MILP formulation without bagging

**Evidence**: "Note that we additionally use the following constraints for symmetry breaking in each class"

## [NEUTRAL] Feature Randomization
During RF training, only a random subset of features is considered at each split node to encourage diversity between trees

**Delta**: descriptive - does not prevent reconstruction
**Condition**: Used in all experiments; does not provide meaningful protection against the proposed reconstruction attack

**Evidence**: "only a random subset of the M features is considered to determine the best split at each node. Note that this mechanism is used in all our experiments, although we do not explicitly leverage it."

## [POSITIVE] Per-Node Class Count Exploitation
Using the per-class example counts stored in every internal and leaf node (as provided by scikit-learn) as constraints in the reconstruction model

**Delta**: outperforms random baseline
**Condition**: Requires white-box access to the trained random forest; information available by default in scikit-learn

**Evidence**: "we leverage both the structure of the trees within the forest and the counts provided within each node to conduct a dataset reconstruction attack"

## [POSITIVE] Partial Reconstruction with Known Attributes
Leveraging partial knowledge of some dataset attributes to improve reconstruction of the remaining unknown attributes

**Delta**: lower error rates for unknown attributes
**Condition**: Applied in complementary experiments (Appendix G) where some attributes are assumed publicly known

**Evidence**: "our approach successfully leverages knowledge of part of the dataset attributes, which results in lower error rates for the other ones"

## [POSITIVE] Multi-threaded CP Solving
Running the CP-SAT solver with 16 parallel threads with up to 6 GB RAM per thread

**Delta**: descriptive - enables practical solving within time limits
**Condition**: Applied to all experiments; bagging models often reach the time limit but usually find feasible solutions much earlier

**Evidence**: "Each model resolution is limited to a maximum of five hours of CPU time using 16 threads with up to 6 GB of RAM for each thread"

## [NEUTRAL] One-Hot Encoding of Categorical/Numerical Features
Binarizing numerical and categorical attributes via one-hot encoding before reconstruction, with group constraints ensuring exactly one binary feature per original attribute is active

**Delta**: descriptive - enables handling of non-binary attributes
**Condition**: Required preprocessing step for non-binary datasets; handled natively in the CP formulation

**Evidence**: "categorical attributes are typically one-hot encoded for tree ensembles and directly handled by our formulation"
