# AegisFL: Efficient and Flexible Privacy-Preserving Byzantine-Robust Cross-silo Federated Learning

**Source**: https://proceedings.mlr.press/v235/chen24ag.html

## [POSITIVE] Custom Packing Scheme for RLWE-based HE
A special polynomial packing method (pm1 and pm2) that encodes vectors into polynomials compatible with RLWE-based HE, enabling inner products, L2 norms, and mean values to be computed with a single polynomial multiplication instead of multiple rotations.

**Delta**: ~24x speedup for inner products and L2 norms, ~30x speedup for mean values compared to original CKKS
**Condition**: Computing similarity metrics (inner product, L2 norm, mean value) for federated learning aggregation under homomorphic encryption

**Evidence**: "compared to the original CKKS, our encoding approach achieves approximately 24 times speedup in computing inner products and L2 norms, and about 30 times speedup in calculating mean values."

## [POSITIVE] Single Ciphertext Multiplication for AGR Construction
Under the custom packing scheme, the server only needs to perform one ciphertext multiplication to compute any required aggregation rule metric, versus log2(N) rotations and additions in standard CKKS.

**Delta**: Reduces from log2(N) rotations + log2(N) additions to a single polynomial multiplication
**Condition**: Server-side computation during secure defense phase in AegisFL

**Evidence**: "with this special packing approach, computing the inner product, L2 norm and mean value requires only a single polynomial multiplication. Conversely, in the original CKKS encoding scheme, requiring one polynomial multiplication, log2 N rotations, and log2 N polynomial additions for both inner product and L2 norm"

## [POSITIVE] Flexible AGR Support
AegisFL is designed to support multiple robust aggregation algorithms (AGRs) rather than being bound to a single one, allowing switching between AGRs depending on attack type and data distribution.

**Delta**: outperforms baseline (enables defense against AGR-tailored attacks that fixed-AGR systems cannot handle)
**Condition**: Environments with varying poisoning attack types or iid/non-iid data distributions

**Evidence**: "different AGRs exhibit varying levels of effectiveness depending on the specific scenario... if malicious clients know the adopted AGR, they can launch targeted advanced poisoning attacks so that the poisoned models completely bypass the detection of the adopted AGR."

## [POSITIVE] Two-Server Non-Colluding Architecture
Uses two honest-but-curious non-colluding servers (S1 and S2) where S1 handles encrypted local models and S2 holds the secret key, preventing either server alone from accessing plaintext model data.

**Delta**: Provides privacy guarantees under three adversary cases including malicious client collusion with one server
**Condition**: Cross-silo federated learning with privacy requirements against honest-but-curious servers

**Evidence**: "we consider two honest-but-curious and non-colluding servers... even if the malicious clients collude with S1 and leak the private key skc to S1, as long as S1 and S2 are non-colluding, S1 still cannot decrypt the encrypted information."

## [POSITIVE] Secure Key Conversion
A protocol that converts ciphertext encrypted under the server public key (pks) to ciphertext encrypted under the client public key (pkc), ensuring the final global model is only accessible to honest clients.

**Delta**: Ensures final model ownership exclusively by honest clients (unlike prior schemes that expose model to server)
**Condition**: Cross-silo FL where model confidentiality from the server is required

**Evidence**: "some schemes (Lu et al., 2023; Miao et al., 2022; Rahulamathavan et al., 2023) expose the final model to the server, which does not meet the requirements of cross-silo FL... the final model should be released exclusively to honest clients"

## [POSITIVE] Consistency Check
A verification step where S1 and S2 cooperate to ensure clients have correctly packaged their local model updates using the required packing method, filtering out incorrectly formatted submissions.

**Delta**: Reduces communication cost between S1 and S2 from 2N·log2(QL) to (N+1)·log2(QL)
**Condition**: Secure defense phase when verifying client submissions in AegisFL

**Evidence**: "our approach has two advantages. Firstly, it reduces the communication cost between S1 and S1 from 2N · log2 QL to (N + 1) · log2 QL. Secondly, after decryption, only the constant terms are meaningful, that is, S2 cannot get any valuable information from other terms, further enhancing data privacy."

## [POSITIVE] Modified FLAME (M-FLAME) Clipping Formula
A transformation of FLAME's clipping formula to remove dependency on the current global model w(t) in ciphertext form, making it compatible with the HE framework by avoiding per-iteration multiplication depth consumption.

**Delta**: Maintains superior robustness while being compatible with the ciphertext framework (original FLAME would require one multiplication depth per global iteration, which is unrealistic)
**Condition**: Applying FLAME aggregation rule under homomorphic encryption in AegisFL

**Evidence**: "this clipping formula is not friendly to our system framework because w(t) is included in this clipping formula. In ciphertext form, the server cannot refresh ct(w(t)), so each global iteration requires one layer of multiplication depth, which is unrealistic... our experiments also show that modified-FLAME has very superior robustness."

## [NEUTRAL] Approximate HE (CKKS) with Scaling Factor Δ=2^40
Using CKKS approximate homomorphic encryption with a scaling factor of 2^40, which introduces small approximation errors but maintains model training accuracy comparable to plaintext.

**Delta**: Accuracy under encryption is on par with or slightly exceeds plaintext accuracy
**Condition**: Model training accuracy when using CKKS-based homomorphic encryption in AegisFL

**Evidence**: "the accuracy under encryption is on par with, or slightly exceeds, the accuracy in plaintext, indicating that at ∆= 2^40, approximate HE does not adversely affect model training."

## [POSITIVE] Full N-slot Packing (vs N/2 slots in standard CKKS)
The custom packing scheme uses all N polynomial slots for data packaging, compared to at most N/2 slots in standard CKKS, allowing more data per ciphertext.

**Delta**: Communication burden roughly equivalent to or slightly higher than baseline 2 (CKKS-based scheme) despite uploading two ciphertexts per client
**Condition**: Client-to-server communication in AegisFL compared to standard CKKS-based PBFL

**Evidence**: "In original CKKS, there are at most N/2 slots for packaging data, but in our scheme all N slots can be used for packaging data. Therefore, although the client needs to upload twice ciphertexts to S1 in our scheme, the communication burden will not increase compared to baseline 2."

## [NEGATIVE] Paillier-based Encryption for PBFL
Using Paillier homomorphic encryption for privacy-preserving Byzantine-robust federated learning, requiring element-wise quantization and encryption.

**Delta**: Significantly lower efficiency than CKKS; traffic ~49.69 MB (ShieldFL/Paillier) vs ~7.03 MB (AegisFL) on HAR
**Condition**: Baseline comparison for PBFL schemes using Paillier encryption

**Evidence**: "When using Paillier (Liu et al., 2021; Ma et al., 2022; Lu et al., 2023), each element in an intermediate result needs to be quantified and encrypted one by one, and measuring the similarity between intermediate results in Paillier ciphertext also requires a lot of additional calculation and communication, which makes their methods very inefficient."

## [NEGATIVE] CKKS with ReLU Approximation for AGR
Using iterative algorithm to approximate ReLU function under CKKS ciphertext for implementing trust-score-based AGR, requiring high multiplication depth.

**Delta**: Requires high multiplication depth, possibly requiring bootstrapping, severely degrading efficiency
**Condition**: CKKS-based PBFL schemes that use ReLU-based trust scoring in AGR

**Evidence**: "in (Miao et al., 2022), they use the ReLU function to realize their AGR. However, when evaluating in CKKS, an iteration algorithm is used to approximate the ReLU function, which requires a high multiplication depth (possibly requiring bootstrapping), severely degrading efficiency."

## [POSITIVE] Only Two Multiplication Levels Required
AegisFL's design requires only two ciphertext multiplication levels throughout the entire secure defense process, keeping the HE parameter requirements minimal.

**Delta**: Avoids bootstrapping overhead; contrasts with prior CKKS approaches requiring high multiplication depth
**Condition**: Secure defense phase in AegisFL using RLWE-based HE

**Evidence**: "It is worth noting that our system only requires two multiplication levels."

## [POSITIVE] ShieldFL AGR on non-iid data (HAR)
Using ShieldFL's cosine-similarity-based AGR on non-iid distributed data (HAR dataset) against untargeted and label flipping attacks.

**Delta**: Improved defense against untargeted and label flipping attacks on HAR (non-iid) compared to FedAvg baseline
**Condition**: Non-iid data distribution (HAR dataset) with untargeted or label flipping attacks

**Evidence**: "ShieldFL shows improved defense capabilities against untargeted attacks and label flipping attacks on the HAR (non-iid) dataset, yet it is less effective against more subtle scaling attacks."

## [NEGATIVE] ShieldFL AGR against scaling attacks
Using ShieldFL's cosine-similarity-based AGR to defend against scaling (backdoor) attacks.

**Delta**: Backdoor success rate remains high (e.g., 0.521 with 12 attackers on MNIST) compared to M-FLAME (0.168)
**Condition**: Scaling/backdoor attacks in federated learning

**Evidence**: "ShieldFL shows improved defense capabilities against untargeted attacks and label flipping attacks on the HAR (non-iid) dataset, yet it is less effective against more subtle scaling attacks."

## [POSITIVE] M-FLAME AGR on iid data (MNIST) against scaling attacks
Using the modified FLAME aggregation rule on iid distributed data (MNIST dataset) to defend against scaling/backdoor attacks.

**Delta**: Backdoor success rate ~0.12-0.17 with M-FLAME vs ~0.14-0.52 with ShieldFL on MNIST scaling attack
**Condition**: iid data distribution (MNIST dataset) with scaling/backdoor attacks

**Evidence**: "M-FLAME performs better on the MNIST (iid) dataset and effectively counters scaling attacks. This indicates that different AGRs exhibit varying levels of effectiveness depending on the specific scenario."
