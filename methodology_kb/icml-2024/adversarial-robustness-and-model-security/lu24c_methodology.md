# Position: Exploring the Robustness of Pipeline-Parallelism-Based Decentralized Training

**Source**: https://proceedings.mlr.press/v235/lu24c.html

## [NEGATIVE] Forward Attack (Sign Flipping)
A poisoning attack where a malicious stage flips the sign of activation values during forward propagation, sending a'_out = -a_out to the next stage instead of the true activation.

**Delta**: perplexity degrades to at least 10x original model at attack rate 0.7, exceeding 200x in some cases
**Condition**: Pipeline-parallelism-based decentralized training with attack rate 0.7; effect weaker at attack rate 0.3

**Evidence**: "Without applying any defense measures and after sufficient training iterations, the perplexity of the attacked model usually degrades to at least 10 times or more of the original model and exceeds 200 times at an attack rate of 0.7."

## [NEGATIVE] Backward Attack (Noise Injection)
A poisoning attack where a malicious stage replaces gradient values during backward propagation with Gaussian random noise sampled from N(0,1), sending g'_out = noise instead of the true gradient.

**Delta**: perplexity degrades to at least 10x original model at attack rate 0.7, exceeding 200x in some cases
**Condition**: Pipeline-parallelism-based decentralized training with attack rate 0.7; effect weaker at attack rate 0.3

**Evidence**: "Without applying any defense measures and after sufficient training iterations, the perplexity of the attacked model usually degrades to at least 10 times or more of the original model and exceeds 200 times at an attack rate of 0.7."

## [NEUTRAL] Low Attack Rate (0.3)
Applying forward or backward attacks with a low probability (0.3) of injecting malicious values per transmission.

**Delta**: model may still converge; in some cases attacked model perplexity is lower than clean model due to overfitting regularization effect
**Condition**: Attack rate 0.3 in pipeline-parallelism-based decentralized training

**Evidence**: "the attack's effectiveness is not always as good when the attack rate is set to 0.3. We analyze that this may be due to the small probability of malicious values being flipped or added noise, which is offset by the high probability of normal values, allowing the model to converge with sufficient training time."

## [POSITIVE] Duplicated Block Detection Strategy
Each stage contains a redundant copy of the previous stage's sub-layers (M'_i-1) alongside its own layers (M_i). The current stage verifies received activation values by recomputing through the duplicated block, enabling 100% detection of malicious tampering.

**Delta**: 100% detection probability of malicious poisoning attackers within the current training iteration
**Condition**: Applied to pipeline-parallelism-based decentralized training as part of the robust training framework

**Evidence**: "The detection strategy can identify the presence of a malicious poisoning attacker with a 100% probability within the current training iteration, notwithstanding the assumption that the attacker possesses sufficient capability."

## [POSITIVE] Jumping Connection
Each stage additionally transmits its output to the (i+2)-th stage and receives output from the (i-2)-th stage, enabling cross-verification to detect more knowledgeable attackers who craft arbitrary consistent input-output pairs.

**Delta**: invalidates more experienced attackers who leverage arbitrary inputs and send corresponding outputs
**Condition**: Used within the detection strategy to handle knowledgeable attackers in decentralized pipeline training

**Evidence**: "This verification invalidates a more experienced attacker who leverages an arbitrary input a'_in and sends the corresponding a'_out to the next stage."

## [POSITIVE] Central Server for Transmission
Instead of direct stage-to-stage data transmission, each stage forwards its output to a trusted central server, which then sends data pairs to the next stage, narrowing down the scope of suspected malicious stages.

**Delta**: narrows malicious stage identification to either the i-th or (i+1)-th stage when an alert is raised
**Condition**: Applied in the efficient training framework component of the robust training system

**Evidence**: "Consequently, if the (i+1)-th stage raises an alert, the malicious stage is either the i-th or the (i+1)-th stage."

## [POSITIVE] Skip Layer (Efficient Training)
Inspired by stochastic depth, when an attack is detected at stage i+1, the central server bypasses the i-th and (i+1)-th stages and transmits data directly between the (i-1)-th and (i+2)-th stages, avoiding full training restart.

**Delta**: robust training framework perplexity up to 74.6x better than attacked model; models using framework exhibit lower perplexity than clean models in some cases
**Condition**: Applied when a malicious stage is detected during pipeline-parallelism-based decentralized training

**Evidence**: "when using the robust training framework, the perplexity of the model can be at most 74.6 times better than that of the perplexity of the attacked model. What's more, models using this framework even exhibit lower perplexity than the original clean models without attacks."

## [POSITIVE] Skip Layer as Regularization
The skip-layer mechanism, used during attack recovery, acts as an implicit regularization technique similar to stochastic depth, reducing overfitting in the trained model.

**Delta**: Bloom-560M on arxiv dataset achieves perplexity of only one-third that of the original clean model
**Condition**: Bloom-560M on arxiv dataset; general effect observed across models when skip layer is triggered

**Evidence**: "Compared with the regular training process, the skip-layer mechanism serves as an effective regularization technique and successfully alleviates model overfitting. Even when testing the perplexity of Bloom-560M on dataset arxiv21, we find that the models using this robust framework have a perplexity of only one-third that of the original model."

## [POSITIVE] Robust Training Framework vs. Restart Method
The proposed robust training framework (skip layer + detection) is compared against a traditional restart method that discards the current iteration and restarts upon detecting an attack.

**Delta**: consistently lower training loss than restart method at most iterations, indicating faster convergence
**Condition**: Evaluated on GPT2-1.5B and OPT-350M on WikiText2 and arXiv datasets

**Evidence**: "our robust training framework consistently exhibits lower loss than the traditional restart method at most iterations, indicating that our approach facilitates faster model convergence."

## [NEGATIVE] Traditional Restart Defense
Upon detecting an attack, the system restarts the current training iteration from scratch, discarding all computation done in that iteration.

**Delta**: higher training loss than robust framework at most iterations; causes prolonged idle time and underutilized computing resources
**Condition**: Used as a baseline comparison against the proposed robust training framework

**Evidence**: "the restart method wastes the results obtained in the current training iteration and leads to prolonged idle time. Consequently, the subsequent computing resources have to remain underutilized for an extended period."

## [NEGATIVE] Encryption-Based Privacy Preservation (Homomorphic Encryption, Secret Sharing)
Methods that encrypt data during transmission between stages to prevent privacy inference attacks, requiring encryption and decryption at each data exchange.

**Delta**: reduces decentralized training efficiency greatly due to frequent encryption/decryption operations
**Condition**: Applied to decentralized pipeline-parallelism-based training for privacy preservation

**Evidence**: "the frequent encryption and decryption operations reduce the decentralized training efficiency greatly."

## [NEGATIVE] Perturbation-Based Privacy Preservation (Differential Privacy, Additive Perturbation)
Methods that add noise to gradient values or training datasets to prevent privacy inference, requiring minimal additional training time.

**Delta**: weak noise easily mitigated by noise reduction algorithms; strong noise significantly reduces training efficiency
**Condition**: Applied to decentralized training for privacy preservation

**Evidence**: "weak noise can be easily mitigated by noise reduction algorithms, while strong noise significantly reduces the training efficiency of the global model."

## [NEGATIVE] FL Outlier Detection (Voting/Bucketing Mechanisms)
Byzantine-resilient aggregation methods from federated learning that use outlier detection to filter malicious gradient updates, relying on comparable values from multiple workers.

**Delta**: not directly applicable; cannot be used due to lack of comparable values in single-pipeline decentralized training
**Condition**: When attempted to be applied to pipeline-parallelism-based decentralized training (single pipeline scenario)

**Evidence**: "Due to the lack of comparable values, directly applying outlier detection algorithms or other privacy-preserving methods is not feasible."
