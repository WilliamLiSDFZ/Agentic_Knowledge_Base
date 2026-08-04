# Fast White-Box Adversarial Streaming Without a Random Oracle

**Source**: https://proceedings.mlr.press/v235/feng24c.html

## [POSITIVE] Fully Homomorphic Encryption (FHE)-based streaming hash
Uses a pseudorandom FHE scheme (specifically GSW) to construct a collision-resistant hash function for white-box adversarially robust sparse recovery, replacing the random oracle/large random matrix used in prior work.

**Delta**: Eliminates random oracle requirement; achieves O~(k) space and O~(1) update time under subexponential LWE
**Condition**: White-box adversarial streaming model for k-sparse recovery under subexponential LWE hardness assumption

**Evidence**: "Our main result is informally stated as follows: Theorem 1.1 (Informal). Assuming the sub-exponential hardness of the Learning with Errors (LWE) problem, there is a WAR streaming algorithm for k-sparse recovery, which: takes O~(k) bits of space, has O~(1) update time, and has O~(k^{1+c}) report time for an arbitrarily small constant c > 0."

## [POSITIVE] Removal of random oracle assumption
Prior work (Feng & Woodruff, 2023) relied on a random oracle to heuristically compress a large random SIS matrix; this work eliminates that requirement by using pseudorandom FHE ciphertexts instead.

**Delta**: Removes random oracle dependency; reduces space overhead from storing large random seed
**Condition**: White-box adversarial streaming; applies to all proposed constructions

**Evidence**: "The main drawback of previous work is that it requires a random oracle, which is especially problematic in the streaming model since the amount of randomness is counted in the space complexity of a streaming algorithm... our solution does not require a random oracle and has a polylogarithmic per item processing time."

## [POSITIVE] Polynomial-time reduction (replacing brute-force)
Instead of brute-forcing over all k-sparse vectors in the security reduction (as in prior work), the adversary is allowed to run the same poly-time weak recovery scheme, enabling a polytime reduction and removing the dependency of the security parameter on k.

**Delta**: Removes k log n factor from security parameter; enables polynomial hardness assumption instead of requiring subexponential hardness for prior construction
**Condition**: Security reduction for WAR sparse recovery; affects space and time complexity under polynomial LWE

**Evidence**: "Our first idea is to construct a polytime reduction in order to remove such a dependency on k. This allows us to achieve better space and time efficiency, in addition to basing the construction on a polynomial hardness assumption."

## [POSITIVE] Pseudorandom FHE (PFHE) with pseudorandom public keys and ciphertexts
Requires the FHE scheme to have computationally indistinguishable public keys and ciphertexts from truly random distributions, allowing the algorithm to sample truly random digests while the proof uses structured encryptions.

**Delta**: Enables truly random-looking state (no structured randomness exposed to adversary) while maintaining provable security
**Condition**: Required for white-box security; satisfied by GSW and most LWE/Ring-LWE based FHE schemes

**Evidence**: "We solve both issues above by considering a pseudorandom property of the FHE scheme and show that a random guess of the index m actually suffices. We assume that the distributions of public keys and ciphertexts of the FHE scheme are indistinguishable, respectively, from some truly random distributions from the perspective of the adversary."

## [POSITIVE] Compact FHE key (O(log n) ciphertexts as hash key)
The hash key consists of only L = O(log n) ciphertexts, from which n evaluated ciphertexts are derived on the fly using simple circuits, achieving a polylogarithmic-sized state.

**Delta**: Hash key size reduced to O(log n) ciphertexts (polylogarithmic in n) vs. a full n-column random matrix in prior work
**Condition**: Streaming model; subexponential LWE enables polylogarithmic security parameter

**Evidence**: "In our hash function, the hash key consists of L = O(log n) ciphertexts ct1, . . . , ctL... from these L ciphertexts, we will derive n evaluated ciphertexts ct'_j for j in [n] by evaluating L ciphertexts on simple functions C1, . . . , Cn."

## [POSITIVE] On-the-fly FHE circuit evaluation for stream updates
For each stream update at index i, the algorithm evaluates a simple circuit C_i on L = O(log n) stored ciphertexts to derive the i-th column ciphertext, enabling O~(1) update time.

**Delta**: Update time reduced to O~(1) vs. O~(k) in prior work
**Condition**: Streaming model under subexponential LWE; uses GSW FHE scheme

**Evidence**: "These circuits are polynomial in L = O(log n) sized and therefore can be evaluated on ct1, . . . , ctL in polynomial in (λ, log n) time guaranteeing fast updates... StreamAlg.Update runs in time O~(1)."

## [POSITIVE] Deterministic relaxed sparse recovery (StreamAlg0) as subroutine
Uses a deterministic (thus inherently WAR) streaming algorithm for relaxed k-sparse recovery as a black-box subroutine, combined with the FHE-based tester to handle the non-sparse case.

**Delta**: O~(k) space, O~(1) update time, O~(k^{1+c}) report time for the subroutine
**Condition**: Used as subroutine in Construction 3.1; determinism ensures WAR property for the recovery part

**Evidence**: "There exists a streaming algorithm StreamAlg0 for the Relaxed k-Sparse Recovery problem, such that... StreamAlg0.Setup, Update, and Report are all deterministic. StreamAlg0 takes O~(k) bits of space. StreamAlg0.Update runs in O~(1). StreamAlg0.Report runs in O~(k^{1+c}) for an arbitrarily small constant c > 0."

## [POSITIVE] Ring-LWE with SIMD packing for distributed setting
In the distributed model, uses Ring-LWE's algebraic structure to pack data as ring elements and exploit SIMD-style operations via Fast Fourier Transform, reducing per-server processing time.

**Delta**: Server processing time improved to O~(n) vs. O~(nk) in prior distributed work; coordinator time O~(max(n, k^{1+c}))
**Condition**: White-box adversarial distributed model; polynomial Ring-LWE hardness assumption

**Evidence**: "We appeal to the Ring-LWE assumption, which is an algebraic variant of LWE that works over the ring Z_p[x]/(x^N + 1). Over this ring, we can exploit the SIMD property of Ring-LWE by packing the data as ring elements... This improves the processing time of each server to be almost linear in the dimension of the data."

## [NEGATIVE] Random oracle assumption (prior work)
Previous work (Feng & Woodruff, 2023) used a random oracle to heuristically compress the large SIS matrix, which cannot be proven secure via standard reduction-style proofs.

**Delta**: Requires storing large random seed; cannot be proven secure without heuristic assumptions
**Condition**: Prior work (Feng & Woodruff, 2023) in white-box adversarial streaming

**Evidence**: "a notable drawback of all prior solutions proposed is their reliance on either a random oracle or a prohibitively long random string... This assumes that the algorithm is given read access to a long string of random bits, which is often implemented with hash-based heuristic functions such as AES or SHA256. Unfortunately, this heuristic cannot be proven secure using a standard reduction-style security proof."

## [NEGATIVE] Brute-force reduction over k-sparse vectors (prior work)
Prior work's security reduction required brute-forcing over all k-sparse vectors, forcing the security parameter (number of matrix rows) to be in omega(k log n), resulting in O~(k) update time.

**Delta**: O~(k) update time per stream element in prior work vs. O~(1) in this work
**Condition**: Prior work (Feng & Woodruff, 2023) security reduction

**Evidence**: "The number of matrix rows in the previous construction depends on the sparsity parameter k due to a brute-forcing step in the reduction. To grant enough time for iterating through all k-sparse vectors (with poly(n)-bounded entries), the security parameter has to be greater than k log n, which results in O~(k) time to process every single update."

## [NEGATIVE] Polynomial LWE hardness assumption (vs. subexponential)
Under polynomial (rather than subexponential) LWE hardness, the construction incurs a multiplicative overhead of n^epsilon on space and time complexities.

**Delta**: Multiplicative overhead of n^epsilon for arbitrary constant epsilon > 0 on space and time
**Condition**: Streaming model under polynomial (not subexponential) LWE hardness

**Evidence**: "On the other hand, assuming polynomial security of the LWE problem, there is a multiplicative overhead of n^epsilon for arbitrary constant epsilon > 0 on our space and time complexities."

## [POSITIVE] Z Linear Homomorphism property of FHE
Requires the FHE scheme to support linear combinations of ciphertexts with a unique decoding guarantee, ensuring that equal hash values imply equal underlying plaintexts for small-norm inputs.

**Delta**: Enables collision resistance proof; satisfied by GSW and most LWE/Ring-LWE schemes
**Condition**: Required for security proof of Construction 3.1; satisfied by GSW (LWE-based) and BV (Ring-LWE-based) schemes

**Evidence**: "The property is that if ct'_i encrypts bit mu_i in {0,1} and x_i are small norm then there is a decryption algorithm that uniquely binds sum_{i in [n]} ct'_i x_i to sum_{i in [n]} mu_i x_i. If this holds, then the equality sum ct'_i x_i = sum ct'_i x'_i would imply x_v = x'_v which is a contradiction."
