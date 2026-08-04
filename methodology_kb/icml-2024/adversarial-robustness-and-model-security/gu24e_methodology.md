# Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast

**Source**: https://proceedings.mlr.press/v235/gu24e.html

## [POSITIVE] Infectious Jailbreak via Adversarial Image
Crafting a single adversarial image that, when injected into one agent's memory, propagates through multi-agent interactions to infect all agents exponentially fast without further adversary intervention

**Delta**: ~100% infection ratio after 27-31 chat rounds in 1 million agents
**Condition**: Multi-agent environments with shared memory banks and pairwise chat interactions

**Evidence**: "feeding an (infectious) adversarial image into the memory of any randomly chosen agent is sufficient to achieve infectious jailbreak"

## [POSITIVE] Border Attack Perturbation
Perturbing only the thin border region of an image without pixel constraints, using border width h as the perturbation budget

**Delta**: p16 cumulative ~93.75% at h=6, ~93.12% at h=8 (low diversity)
**Condition**: Low and high textual chat diversity scenarios

**Evidence**: "Border attack: Inspired by Zajac et al. (2019), we only perturb the thin border region of V without pixel constraints."

## [POSITIVE] Pixel Attack Perturbation
Optimizing all pixels of an image under l-infinity norm perturbation constraints with budget epsilon

**Delta**: p16 cumulative ~93.75% at epsilon=8/255 and ~93.52% at epsilon=16/255 (low diversity)
**Condition**: Low and high textual chat diversity scenarios

**Evidence**: "Pixel attack: All the pixels of V are optimized under l∞-norm perturbation constraints to ensure ||V_adv − V||∞ ≤ ε, where ε is the perturbation budget."

## [POSITIVE] Ensemble of Chat Records for Adversarial Optimization
Using M=512 sampled chat records from a multi-agent system to craft the adversarial image by optimizing over an ensemble of prompts

**Delta**: Both current and cumulative infection ratios at round 16 generally increase with larger M
**Condition**: Adversarial image crafting phase; applies to both border and pixel attacks

**Evidence**: "both the current and cumulative infection ratios at the 16-th chat round generally increase with larger M, regardless of the type of attack implemented"

## [NEGATIVE] Small Ensemble Sample Size (low M)
Crafting adversarial images with a limited number of chat records (small M)

**Delta**: Lower infection ratios at round 16 compared to large M
**Condition**: Scenarios where attacker has limited access to chat records

**Evidence**: "both the current and cumulative infection ratios at the 16-th chat round generally increase with larger M"

## [NEGATIVE] High Textual Chat Diversity
Using system prompts that encourage agents to play roles and generate more diverse, longer interactions

**Delta**: Generally lower infection ratios at specific chat rounds and longer rounds required to reach 90% threshold compared to low diversity
**Condition**: Ablation comparing low vs high diversity system prompts

**Evidence**: "the high diversity scenario poses a greater challenge, evidenced by generally lower infection ratios at specific chat rounds and longer chat rounds required to reach particular infection thresholds"

## [POSITIVE] Low Textual Chat Diversity
Using brief system prompts that result in short, low-diversity agent interactions

**Delta**: Higher infection ratios and fewer rounds to reach 90% threshold vs high diversity
**Condition**: Default scenario with simple system prompts

**Evidence**: "This scenario is characterized by brevity in agent interactions and low textual chat diversity"

## [POSITIVE] Large Image Album Memory Bank (|B|=10)
Setting the image album FIFO queue to a large maximum length, reducing recovery probability

**Delta**: Higher infection ratios compared to |B|=2; slight decrease vs |B|=6 due to retrieval dilution
**Condition**: Ablation on image album size

**Evidence**: "when |B| = 10, there is a slight decrease in the infected ratio by the 16-th chat round. This phenomenon can be attributed to a diminished retrieval success rate, owing to the prevalence of benign images in the album."

## [NEGATIVE] Small Image Album Memory Bank (|B|=2)
Setting the image album FIFO queue to a small maximum length, increasing recovery probability

**Delta**: Noticeably restrained spread, requiring greater number of chat rounds to reach 90% infection rate
**Condition**: Ablation on image album size; potential defense mechanism

**Evidence**: "with |B| = 2, the spread of infectious jailbreak is noticeably restrained, necessitating a greater number of chat rounds to reach an infection rate of 90%"

## [NEUTRAL] Larger Text History Memory Bank (|H|)
Increasing the text histories FIFO queue length from |H|=3 to larger values

**Delta**: No significant change in infectious dynamics
**Condition**: Ablation on text history memory bank size

**Evidence**: "the increase of the text histories memory bank does not significantly alter the infectious dynamics. This observation underscores the robustness and universality of our adversarial examples"

## [POSITIVE] Image Augmentation During Adversarial Crafting (Resize, Flip, JPEG)
Applying random resize, random horizontal flip, and random JPEG compression during adversarial image optimization to improve robustness against corruptions

**Delta**: Infection curves approach ~90% despite corruptions, though with noticeable fluctuations
**Condition**: Scenarios where images may be corrupted during storage/transmission in memory

**Evidence**: "various image corruptions may challenge but not stop the infectious jailbreak"

## [NEGATIVE] Visual Prompt Injection (VP) Baseline
Embedding harmful instructions visually into an image to override textual prompts, as a noninfectious jailbreak baseline

**Delta**: Cannot jailbreak any single agent; 0% infection ratio
**Condition**: LLaVA-1.5 based multi-agent environment with N=256

**Evidence**: "both visual and textual prompt injections are ineffective in infecting any agents"

## [NEGATIVE] Textual Prompt Injection (TP) Baseline
Crafting a textual prompt to persuade agents to generate and spread harmful content, as a noninfectious jailbreak baseline

**Delta**: Cannot jailbreak any single agent; 0% infection ratio
**Condition**: LLaVA-1.5 based multi-agent environment with N=256

**Evidence**: "both visual and textual prompt injections are ineffective in infecting any agents"

## [NEGATIVE] Sequential Jailbreak Baseline
Jailbreaking one agent per chat round using noninfectious adversarial images/prompts, requiring O(N) chat rounds

**Delta**: Linear infection rate; infects ~1/8 of agents cumulatively after 32 chat rounds vs ~100% for infectious method
**Condition**: Compared against infectious jailbreak in N=256 multi-agent environment

**Evidence**: "The sequential jailbreak ideally manages to infect 1/8 of almost all agents cumulatively after 32 chat rounds, exhibiting a linear rate of infection."

## [POSITIVE] Larger Perturbation Budget
Using larger perturbation budgets (larger h for border attack or larger epsilon for pixel attack)

**Delta**: Higher jailbreaking efficiency across metrics
**Condition**: Both low and high diversity scenarios

**Evidence**: "the results from the same table reveal a correlation between larger perturbation budgets and higher jailbreaking efficiency"

## [NEGATIVE] Small Perturbation Budget
Using perturbation budgets below threshold (h<6 for border, epsilon<8/255 for pixel)

**Delta**: Failure cases observed: slow infection rate, sudden drops, or consistently low infection ratio
**Condition**: High diversity scenarios

**Evidence**: "we find several failure cases in high diversity scenarios with small perturbation budgets, such as h < 6 for border attack and l∞, ε < 8/255 for pixel attack"

## [NEGATIVE] Larger Number of Agents N
Scaling up the number of agents in the multi-agent environment

**Delta**: Delays infection spread but does not cause failure; O(log N) rounds still sufficient
**Condition**: Scaling experiments from N=256 to N=1,000,000

**Evidence**: "a larger N, corresponding to a lower initial virus-carrying ratio (c0 = 1/N), may slow down but does not render the infectious attack failure"

## [POSITIVE] RAG Module with CLIP Encoders
Using frozen CLIP text and image encoders in a bi-encoder architecture for retrieval-augmented generation to retrieve the adversarial image from the album

**Delta**: Enables reliable retrieval of adversarial image (beta=1 in ideal conditions)
**Condition**: Core component enabling infectious spread in the multi-agent pipeline

**Evidence**: "V_adv will be retrieved due to Eq. (9), and updated into B_A after the chat between G_Q and G_A"

## [POSITIVE] Heterogeneous Multi-Agent Environment
Using a mix of 50% LLaVA-1.5 7B and 50% InstructBLIP 7B agents, with adversarial image crafted against both MLLMs

**Delta**: Almost all LLaVA-based and InstructBLIP-based agents infected by end of simulation
**Condition**: Heterogeneous multi-agent environment with mixed MLLM backbones

**Evidence**: "we observe that almost all the LLaVA-based agents and InstructBLIP-based agents are infected by the end. These new experiments show that our infectious jailbreak can still be successful in such an environment with heterogeneous agents."

## [NEUTRAL] Greedy Decoding
Using greedy decoding instead of sampling for text generation during agent chats

**Delta**: Used for reproducibility; no comparative delta reported
**Condition**: All simulation experiments

**Evidence**: "For reproducibility, we employ greedy decoding to generate textual content during chats."

## [NEUTRAL] FIFO Memory Queue
Implementing memory banks as first-in-first-out queues with fixed maximum lengths, causing natural recovery as adversarial images are eventually dequeued

**Delta**: Recovery rate gamma depends on |B|; larger |B| lowers gamma
**Condition**: All agent memory management; affects recovery rate gamma

**Evidence**: "Both H and B are implemented as first-in-first-out (FIFO) queues with fixed maximum lengths. If a queue is full, we will dequeue the earliest text or image before adding new ones."

## [NEGATIVE] Exact Match Evaluation Criterion
Requiring exact string matches with Q_harm/A_harm to count as successful jailbreak

**Delta**: Likely underestimates actual jailbreak effectiveness
**Condition**: Evaluation metric for all infection ratio measurements

**Evidence**: "This discrepancy suggests that the exact match criteria used in Zou et al. (2023) might underestimate the actual effectiveness of infectious jailbreak."

## [POSITIVE] Defense Principle: beta <= 2*gamma
Ensuring infection rate beta is at most twice the recovery rate gamma as a provable defense condition to drive infection ratio to zero

**Delta**: Provably drives infection ratio to 0 as t→∞
**Condition**: Theoretical defense design principle

**Evidence**: "if a defense mechanism can more efficiently recover infected agents or lower down infection rate such that β ≤ 2γ, then this defense is provably to decrease the infection rate to zero when t→∞"
