# Privacy Attacks in Decentralized Learning

**Source**: https://proceedings.mlr.press/v235/mrini24a.html

## [POSITIVE] Knowledge Matrix Construction via RREF
Building a system of linear equations (knowledge matrix KT) from messages received during gossip averaging, then solving via Reduced Row Echelon Form (RREF) factorization to reconstruct private values of nodes

**Delta**: reconstructs data of nodes up to 28 hops away in a 31-node line graph
**Condition**: gossip averaging protocol with known gossip matrix

**Evidence**: "we see in Figure 4(a) that the results are far better than one would intuitively expect: even though the gradients of distant nodes are mixed many times before reaching the attacker, our attack allows to disentangle the contributions of the different nodes to enable informative reconstruction up to distance 28"

## [POSITIVE] Attacker Collusion (Multiple Attackers)
Multiple attacker nodes share all their observations, effectively expanding the combined view and increasing the number of reconstructible nodes

**Delta**: fraction of reconstructed nodes increases with number of attackers (1 to 3 attackers tested)
**Condition**: gossip averaging on Erdos-Renyi graphs

**Evidence**: "The collusion of several attacking nodes further strengthens the attack... The fraction of reconstructed nodes increases with the connectivity of the graph and the number of attackers."

## [POSITIVE] High Graph Connectivity
Higher edge probability in the network graph, leading to more connections between nodes

**Delta**: fraction of reconstructed nodes increases with connectivity
**Condition**: Erdos-Renyi synthetic graphs with varying edge probability p

**Evidence**: "The fraction of reconstructed nodes increases with the connectivity of the graph and the number of attackers."

## [POSITIVE] High Attacker Degree Centrality
Attacker node positioned at a high-degree (well-connected) location in the graph

**Delta**: Spearman correlation of 0.94 for both Erdos-Renyi and Ego graphs
**Condition**: single attacker on Erdos-Renyi and Facebook Ego graphs

**Evidence**: "We observe in Table 1 that for both types of graphs, degree centrality is the most correlated with the proportion of reconstructed nodes."

## [POSITIVE] Gradient Similarity Assumption (Noise-Signal Decomposition)
Assuming each node's gradient can be decomposed into a fixed component (constant across iterations) and a centered random noise component, enabling gradient reconstruction via Generalized Least Squares

**Delta**: attack works well when gradients change sufficiently slowly across iterations
**Condition**: D-GD attack; assumption approximately satisfied near convergence or with small learning rate

**Evidence**: "We note that this assumption is typically not satisfied in real use cases, but we will see in Section 6 that the algorithm is robust in practice to small violations of this assumption (in particular, it works well when gradients change sufficiently slowly across iterations)."

## [POSITIVE] Generalized Least Squares (GLS) for Gradient Reconstruction
Using GLS with the computed covariance matrix to reconstruct gradients from attacker observations in D-GD, accounting for correlated noise structure

**Delta**: similar reconstruction quality to OLS in practice
**Condition**: D-GD gradient reconstruction step

**Evidence**: "Although this gives a bit more weight to the most noisy points compared to the optimal estimator under Assumption 5.1, we found experimentally that the reconstruction quality is quite similar between the two methods."

## [NEUTRAL] Ordinary Least Squares (OLS) vs GLS
Using OLS instead of the exact GLS estimator, ignoring the non-diagonal covariance structure of the noise

**Delta**: reconstruction quality quite similar between OLS and GLS
**Condition**: D-GD gradient reconstruction; noise structure assumption not fully satisfied

**Evidence**: "we found experimentally that the reconstruction quality is quite similar between the two methods. This can be explained by the fact that the assumption of the noise structure is not fully satisfied, and OLS tends to be quite robust in practice."

## [POSITIVE] Attackers' Contribution Removal
Preprocessing the received updates to subtract the attacker nodes' own contributions before solving the reconstruction problem, reducing noise in the approximated reconstruction

**Delta**: described as reducing overall noise in approximated reconstruction
**Condition**: D-GD attack preprocessing step

**Evidence**: "(iii) Removing the attackers' own contributions to reduce overall noise in the approximated reconstruction"

## [POSITIVE] Small Learning Rate
Using a small learning rate in D-GD so that gradients do not vary wildly across iterations, satisfying the gradient similarity assumption more closely

**Delta**: PSNR degrades significantly as log learning rate increases from -6.0 toward -2.5 (Figure 12)
**Condition**: D-GD attack; learning rates tested on line graph

**Evidence**: "the learning rate plays an important role: it should be small enough to ensure that gradients do not vary wildly across iterations. We illustrate this behavior in Appendix H."

## [NEGATIVE] Large Learning Rate
Using a large learning rate in D-GD causing gradients to change significantly across iterations

**Delta**: PSNR drops toward 0 at higher learning rates (Figure 12)
**Condition**: D-GD attack on line graph

**Evidence**: "When the learning rate becomes too large, gradients vary too much across iterations and it becomes impossible to make accurate reconstructions."

## [POSITIVE] Running Attack Near Convergence
Starting the reconstruction attack after the D-GD model is close to convergence, so that gradients are more stable across iterations

**Delta**: enables accurate gradient reconstruction
**Condition**: D-GD attack on Cifar10 and MNIST

**Evidence**: "We start running our attack when the model is close to convergence so that gradients are more stable."

## [POSITIVE] Running D-GD for Diameter-Many Steps Before Attack
Running D-GD for a number of steps roughly equal to the diameter of the graph to ensure attackers gather enough information in the knowledge matrix

**Delta**: ensures sufficient equations in knowledge matrix for reconstruction
**Condition**: D-GD attack setup

**Evidence**: "To ensure that attackers gather enough information about other nodes in the knowledge matrix, we run D-GD for a number of steps roughly equal to the diameter of the graph."

## [POSITIVE] Gradient Inversion as Black-Box
Using existing gradient inversion attacks (e.g., Geiping et al. 2020) as a black-box second step after reconstructing gradients, to recover actual data points from gradients

**Delta**: accurate reconstructions up to distance 26 on 31-node line graph with CNN on MNIST
**Condition**: D-GD attack on MNIST with convolutional neural network

**Evidence**: "we see in Figure 4(b) that our approach can naturally rely on a black-box gradient inversion attack to reconstruct data from the gradients of more complex models. Here, the reconstructions are accurate up to distance 26."

## [POSITIVE] Multiple Gossip Steps Per Gradient Step
Performing multiple gossip averaging steps for each gradient descent step, a variant of D-GD

**Delta**: makes reconstruction easier by bringing D-GD closer to gossip averaging
**Condition**: D-GD variant with multiple gossip steps per gradient step

**Evidence**: "it makes reconstruction easier as it brings D-GD closer to gossip averaging by effectively making gradients constant across several iterations."

## [POSITIVE] Uniform Parameter Initialization Across Nodes
Initializing all nodes with the same model parameters at the start of D-GD

**Delta**: enables better reconstructions as observed values are primarily influenced by gradients
**Condition**: D-GD attack setup

**Evidence**: "having similar local parameters θv across nodes enables better reconstructions as the observed values are primarily influenced by the gradients rather than by variations in the parameters. This condition is easily satisfied either by initializing all the nodes with the same parameters (a standard practice in D-GD) or by waiting until the system approaches convergence."

## [NEGATIVE] Attacker at Graph Periphery (Low Centrality)
Attacker node positioned at the edge/extremity of the network with low degree or centrality

**Delta**: nodes located at the edge of the network reconstruct a smaller proportion of other nodes
**Condition**: D-GD attack on Florentine graph

**Evidence**: "We can see in Figure 5 that most nodes (except those located at the edge of the network) can reconstruct a large proportion of other nodes with very good visual accuracy."

## [POSITIVE] Short Shortest-Path Distance Between Attacker and Target
Target node being closer (fewer hops) to the attacker in the graph

**Delta**: Kendall rank correlation of -0.44 (Erdos-Renyi) and -0.51 (Facebook Ego) between path length and reconstruction probability
**Condition**: gossip averaging on Erdos-Renyi and Facebook Ego graphs

**Evidence**: "We see that in both cases, the shortest path length provides a good insight on the reconstruction probability"

## [NEUTRAL] Secure Aggregation (SecAgg) Defense
Using secure aggregation so each node computes weighted sums with neighbors without revealing individual values

**Delta**: attack still works with slight modification to knowledge matrix construction
**Condition**: gossip averaging with SecAgg defense applied

**Evidence**: "We note that our attack still works in this case, with a slight modification in the construction of the knowledge matrix. As illustrated by Figure 4(b) or Figure 3, numerous nodes can have their data leaked in the case where the attacker has a single neighbor."

## [POSITIVE] Logistic Regression Model for Closed-Form Gradient Inversion
Using a simple fully connected layer with softmax and cross-entropy loss, enabling closed-form data reconstruction from gradients without a separate gradient inversion attack

**Delta**: allows evaluation focused on core gradient reconstruction without errors from imperfect gradient inversion
**Condition**: D-GD attack evaluation on Cifar10

**Evidence**: "For this simple model, one can reconstruct a data point from its gradient in closed-form... This allows us to focus the evaluation on the core of our attack (reconstructing gradients), avoiding the inherent errors due to the imperfections of gradient inversion attacks on more complex models."

## [POSITIVE] Community Structure in Graph (Cluster-Based Topology)
Graph topology with distinct communities or clusters, such as in Facebook Ego graphs

**Delta**: reconstruction much more likely within clusters; in most cases a vast majority of nodes in the same community have data leaked
**Condition**: gossip averaging on Facebook Ego graphs

**Evidence**: "reconstruction is much more likely within clusters, but also occur across nodes belonging to distinct clusters... in most cases, a vast majority of the nodes of the same community see their data leaked."
