---
name: large-language-model-alignment-and-capabilities
description: >-
  This skill covers the theoretical foundations and practical mechanisms of LLM behavior, spanning architectural analysis (token prediction dynamics, embedding tying assumptions, knowledge storage), inference-time control methods (constrained generation, prompt sketching, context scaling without retraining), and systematic evaluation across diverse domains including code correctness, negotiation, climate information, and time series. It also addresses safety-critical concerns
---

# Large Language Model Alignment And Capabilities

This skill covers the theoretical foundations and practical mechanisms of LLM behavior, spanning architectural analysis (token prediction dynamics, embedding tying assumptions, knowledge storage), inference-time control methods (constrained generation, prompt sketching, context scaling without retraining), and systematic evaluation across diverse domains including code correctness, negotiation, climate information, and time series. It also addresses safety-critical concerns

## Entry Index

| # | Title | Tags | File |
|---|-------|------|------|
| 1 | In-Context Language Learning: Architectures and Algorithms | in-context-learning, language-models, sequence-models | akyurek24a.md |
| 2 | Unsupervised Evaluation of Code LLMs with Round-Trip Correct | code-LLMs, evaluation, round-trip-correctness | allamanis24a.md |
| 3 | Physics of Language Models: Part 3.1, Knowledge Storage and  | LLM-knowledge, knowledge-extraction, question-answering | allen-zhu24a.md |
| 4 | Training-Free Long-Context Scaling of Large Language Models | long-context-LLM, training-free, context-window-extension | an24b.md |
| 5 | The Pitfalls of Next-Token Prediction | next-token-prediction, autoregression, language-model-limitations | bachmann24a.md |
| 6 | Image Hijacks: Adversarial Images can Control Generative Mod | adversarial-images, vision-language-models, behavior-matching | bailey24a.md |
| 7 | Linguistic Calibration of Long-Form Generations | linguistic-calibration, long-form-generation, hallucination | band24a.md |
| 8 | To Each (Textual Sequence) Its Own: Improving Memorized-Data | unlearning, memorization, privacy | barbulescu24a.md |
| 9 | By Tying Embeddings You Are Assuming the Distributional Hypo | tied-embeddings, distributional-hypothesis, language-models | bertolotti24a.md |
| 10 | Guiding LLMs The Right Way: Fast, Non-Invasive Constrained G | constrained-decoding, LLMs, formal-languages | beurer-kellner24a.md |
| 11 | Prompt Sketching for Large Language Models | prompt-engineering, LLMs, constrained-generation | beurer-kellner24b.md |
| 12 | Multi-Patch Prediction: Adapting Language Models for Time Se | LLM, time-series, representation-learning | bian24a.md |
| 13 | How Well Can LLMs Negotiate? NegotiationArena Platform and A | LLM-agents, negotiation, multi-agent | bianchi24a.md |
| 14 | Scalable AI Safety via Doubly-Efficient Debate | ai-safety, debate, scalable-oversight | brown-cohen24a.md |
| 15 | Assessing Large Language Models on Climate Information | LLM-evaluation, climate-change, science-communication | bulian24a.md |
| 16 | Weak-to-Strong Generalization: Eliciting Strong Capabilities | weak-to-strong, alignment, RLHF | burns24b.md |
| 17 | CodeIt: Self-Improving Language Models with Prioritized Hind | self-improvement, hindsight-replay, ARC-benchmark | butt24a.md |
| 18 | Bridging Environments and Language with Rendering Functions  | vision-language-models, reinforcement-learning, language-conditioned-agents | cachet24a.md |
| 19 | Human Alignment of Large Language Models through Online Pref | RLHF, preference-optimization, online-learning | calandriello24a.md |
| 20 | Successor Features for Efficient Multi-Subject Controlled Te | controlled-text-generation, successor-features, multi-subject | cao24a.md |
| 21 | Envisioning Outlier Exposure by Large Language Models for Ou | out-of-distribution-detection, LLM, outlier-exposure | cao24d.md |
| 22 | AI Alignment with Changing and Influenceable Reward Function | AI-alignment, dynamic-rewards, influenceable-preferences | carroll24a.md |
| 23 | Using Left and Right Brains Together: Towards Vision and Lan | vision-language-planning, spatial-reasoning, LLM | cen24a.md |
| 24 | MaxMin-RLHF: Alignment with Diverse Human Preferences | RLHF, diverse-preferences, MaxMin-optimization | chakraborty24b.md |
| 25 | Dense Reward for Free in Reinforcement Learning from Human F | RLHF, dense-reward, token-level-reward | chan24a.md |
| 26 | InstructZero: Efficient Instruction Optimization for Black-B | instruction-optimization, black-box-LLMs, Bayesian-optimization | chen24e.md |
| 27 | MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vi | multimodal-LLMs, LLM-as-judge, vision-language-benchmark | chen24h.md |
| 28 | Premise Order Matters in Reasoning with Large Language Model | LLM-reasoning, premise-ordering, robustness | chen24i.md |
| 29 | Self-Play Fine-Tuning Converts Weak Language Models to Stron | self-play, fine-tuning, LLM-alignment | chen24j.md |
| 30 | From Yes-Men to Truth-Tellers: Addressing Sycophancy in Larg | sycophancy, LLM-alignment, pinpoint-tuning | chen24u.md |
| 31 | Toward Adaptive Reasoning in Large Language Models with Thou | llm-reasoning, thought-rollback, adaptive-reasoning | chen24y.md |
| 32 | DiJiang: Efficient Large Language Models through Compact Ker | linear-attention, efficient-transformers, compact-kernelization | chen24ab.md |
| 33 | GRATH: Gradual Self-Truthifying for Large Language Models | LLM-truthfulness, self-training, TruthfulQA | chen24aj.md |
| 34 | SelfIE: Self-Interpretation of Large Language Model Embeddin | LLM-interpretability, embedding-interpretation, self-explanation | chen24ao.md |
| 35 | In-Context Sharpness as Alerts: An Inner Representation Pers | hallucination, inner-representations, LLM | chen24av.md |
| 36 | $\textttMoE-RBench$: Towards Building Reliable Language Mode | mixture-of-experts, LLM-reliability, model-robustness | chen24bg.md |
| 37 | LLaGA: Large Language and Graph Assistant | graph-LLM, node-classification, LLM-graph-integration | chen24bh.md |
| 38 | HALC: Object Hallucination Reduction via Adaptive Focal-Cont | hallucination-reduction, vision-language-models, focal-contrast-decoding | chen24bi.md |
| 39 | Do Models Explain Themselves? Counterfactual Simulatability  | counterfactual-simulatability, LLM-explanations, human-mental-models | chen24bl.md |
| 40 | ODIN: Disentangled Reward Mitigates Hacking in RLHF | RLHF, reward-hacking, length-bias | chen24bn.md |
| 41 | Can AI Assistants Know What They Don’t Know? | LLM-uncertainty, knowledge-awareness, open-domain-QA | cheng24i.md |
| 42 | Language Models as Science Tutors | science-tutoring, language-models, educational-NLP | chevalier24a.md |
| 43 | Chatbot Arena: An Open Platform for Evaluating LLMs by Human | llm-evaluation, human-preference, benchmark | chiang24b.md |
| 44 | Listwise Reward Estimation for Offline Preference-based Rein | preference-based-rl, reward-learning, offline-rl | choi24b.md |
| 45 | Embodied CoT Distillation From LLM To Off-the-shelf Agents | embodied-ai, chain-of-thought, knowledge-distillation | choi24d.md |
| 46 | PICLe: Eliciting Diverse Behaviors from Large Language Model | persona, in-context-learning, llm-behavior | choi24e.md |
| 47 | MusicRL: Aligning Music Generation to Human Preferences | music-generation, reinforcement-learning-from-human-feedback, text-to-music | cideron24a.md |
| 48 | CogBench: a large language model walks into a psychology lab | llm-evaluation, cognitive-benchmarks, psychology | coda-forno24a.md |
| 49 | Agent Instructs Large Language Models to be General Zero-Sho | llm-reasoning, zero-shot, autonomous-agent | crispino24a.md |
| 50 | ULTRAFEEDBACK: Boosting Language Models with Scaled AI Feedb | llm-alignment, ai-feedback, preference-learning | cui24f.md |
| 51 | Getting the most out of your tokenizer for pre-training and  | tokenization, llm-pretraining, domain-adaptation | dagan24a.md |
| 52 | Larimar: Large Language Models with Episodic Memory Control | large-language-models, episodic-memory, knowledge-editing | das24a.md |
| 53 | Learning Cognitive Maps from Transformer Representations for | transformers, cognitive-maps, planning | dedieu24a.md |
| 54 | Multicalibration for Confidence Scoring in LLMs | multicalibration, confidence-scoring, LLM-uncertainty | detommaso24a.md |
| 55 | Fewer Truncations Improve Language Modeling | language-model-training, document-truncation, data-integrity | ding24f.md |
| 56 | Quality Diversity through Human Feedback: Towards Open-Ended | quality-diversity, RLHF, human-feedback | ding24h.md |
| 57 | LongRoPE: Extending LLM Context Window Beyond 2 Million Toke | LLM, context-window, RoPE | ding24i.md |
| 58 | Pruner-Zero: Evolving Symbolic Pruning Metric From Scratch f | LLM-pruning, symbolic-regression, evolutionary-search | dong24b.md |
| 59 | WorkArena: How Capable are Web Agents at Solving Common Know | web-agents, LLM-agents, enterprise-software | drouin24a.md |
| 60 | Principled Gradient-Based MCMC for Conditional Sampling of T | MCMC, energy-based-models, text-sampling | du24a.md |
| 61 | Improving Factuality and Reasoning in Language Models throug | multiagent-debate, LLM-reasoning, factuality | du24e.md |
| 62 | AnyTool: Self-Reflective, Hierarchical Agents for Large-Scal | LLM-agents, API-calls, tool-use | du24h.md |
| 63 | Exploration-Driven Policy Optimization in RLHF: Theoretical  | RLHF, policy-optimization, exploration | du24i.md |
| 64 | Efficient Exploration for LLMs | exploration, reinforcement-learning-from-human-feedback, active-learning | dwaracherla24a.md |
| 65 | Model Alignment as Prospect Theoretic Optimization | rlhf, prospect-theory, human-feedback | ethayarajh24a.md |
| 66 | Is In-Context Learning in Large Language Models Bayesian? A  | in-context-learning, large-language-models, bayesian-inference | falck24a.md |
| 67 | Promptbreeder: Self-Referential Self-Improvement via Prompt  | prompt-optimization, evolutionary-algorithms, llm-self-improvement | fernando24a.md |
| 68 | Data Engineering for Scaling Language Models to 128K Context | long-context, continual-pretraining, data-engineering | fu24d.md |
| 69 | Language-guided Skill Learning with Temporal Variational Inf | skill-discovery, temporal-segmentation, hierarchical-inference | fu24e.md |
| 70 | PinNet: Pinpoint Instructive Information for Retrieval Augme | retrieval-augmented-generation, code-summarization, information-pinpointing | fu24f.md |
| 71 | FuRL: Visual-Language Models as Fuzzy Rewards for Reinforcem | visual-language-models, reward-shaping, sparse-rewards | fu24j.md |
| 72 | Linear Alignment: A Closed-form Solution for Aligning Human  | LLM-alignment, RLHF, closed-form-solution | gao24f.md |
| 73 | Fast-Slow Test-Time Adaptation for Online Vision-and-Languag | test-time-adaptation, vision-and-language-navigation, online-learning | gao24p.md |
| 74 | LLark: A Multimodal Instruction-Following Language Model for | music-understanding, multimodal-model, instruction-tuning | gardner24a.md |
| 75 | Variance-reduced Zeroth-Order Methods for Fine-Tuning Langua | zeroth-order-optimization, fine-tuning, language-models | gautam24a.md |
| 76 | Patchscopes: A Unifying Framework for Inspecting Hidden Repr | LLM-interpretability, hidden-representations, patchscopes | ghandeharioun24a.md |
| 77 | Understanding Finetuning for Factual Knowledge Extraction | finetuning, factual-knowledge, language-models | ghosal24a.md |
| 78 | A Closer Look at the Limitations of Instruction Tuning | instruction-tuning, LLM-limitations, fine-tuning | ghosh24a.md |
| 79 | Better & Faster Large Language Models via Multi-token Predic | multi-token-prediction, language-model-training, sample-efficiency | gloeckle24a.md |
| 80 | AST-T5: Structure-Aware Pretraining for Code Generation and  | code-generation, abstract-syntax-tree, pretraining | gong24c.md |
| 81 | A Nearly Optimal Single Loop Algorithm for Stochastic Bileve | bilevel-optimization, unbounded-smoothness, meta-learning | gong24d.md |
| 82 | Evaluation of LLMs on Syntax-Aware Code Fill-in-the-Middle T | code-completion, fill-in-the-middle, llm-benchmark | gong24f.md |
| 83 | Learning Universal Predictors | meta-learning, universal-prediction, amortized-inference | grau-moya24a.md |
| 84 | CRUXEval: A Benchmark for Code Reasoning, Understanding and  | code-reasoning, benchmark, llm-evaluation | gu24c.md |
| 85 | Automated Evaluation of Retrieval-Augmented Language Models  | retrieval-augmented-generation, evaluation, synthetic-exam | guinet24a.md |
| 86 | DS-Agent: Automated Data Science by Empowering Large Languag | LLM-agents, data-science-automation, case-based-reasoning | guo24b.md |
| 87 | COLD-Attack: Jailbreaking LLMs with Stealthiness and Control | jailbreak, LLM-safety, controllable-generation | guo24i.md |
| 88 | GistScore: Learning Better Representations for In-Context Ex | in-context-learning, example-selection, gist-bottleneck | gupta24c.md |
| 89 | Covert Malicious Finetuning: Challenges in Safeguarding LLM  | LLM-safety, finetuning, covert-attack | halawi24a.md |
| 90 | Large Language Models Can Automatically Engineer Features fo | llm, feature-engineering, tabular-learning | han24f.md |
| 91 | Spotting LLMs With Binoculars: Zero-Shot Detection of Machin | llm-detection, machine-generated-text, zero-shot | hans24a.md |
| 92 | GLoRe: When, Where, and How to Improve LLM Reasoning via Glo | llm-reasoning, refinement, outcome-reward-model | havrilla24a.md |
| 93 | From Words to Actions: Unveiling the Theoretical Underpinnin | llm-agents, hierarchical-rl, theoretical-foundations | he24a.md |
| 94 | Two Stones Hit One Bird: Bilevel Positional Encoding for Bet | positional-encoding, length-extrapolation, transformers | he24c.md |
| 95 | Instruction Tuning for Secure Code Generation | instruction-tuning, code-generation, security | he24k.md |
| 96 | Decoding Compressed Trust: Scrutinizing the Trustworthiness  | LLM-compression, trustworthiness, safety | hong24a.md |
| 97 | Do Large Code Models Understand Programming Concepts? Counte | llm, code-generation, counterfactual-analysis | hooda24a.md |
| 98 | Decomposing Uncertainty for Large Language Models through In | uncertainty-decomposition, llm, aleatoric | hou24b.md |
| 99 | PrE-Text: Training Language Models on Private Federated Data | federated-learning, privacy, llm | hou24c.md |
| 100 | Accelerated Speculative Sampling Based on Tree Monte Carlo | speculative-sampling, llm-inference, tree-monte-carlo | hu24f.md |
| 101 | SceneCraft: An LLM Agent for Synthesizing 3D Scenes as Blend | llm-agent, 3d-scene-generation, blender | hu24g.md |
| 102 | Case-Based or Rule-Based: How Do Transformers Do the Math? | large-language-models, arithmetic-reasoning, in-context-learning | hu24n.md |
| 103 | InfiAgent-DABench: Evaluating Agents on Data Analysis Tasks | llm-agents, data-analysis, benchmark-evaluation | hu24s.md |
| 104 | In-Context Decision Transformer: Reinforcement Learning via  | in-context-reinforcement-learning, decision-transformer, chain-of-thought | huang24j.md |
| 105 | InstructSpeech: Following Speech Editing Instructions via La | speech-editing, instruction-following, large-language-models | huang24k.md |
| 106 | BiLLM: Pushing the Limit of Post-Training Quantization for L | post-training-quantization, binarization, large-language-models | huang24q.md |
| 107 | Position: TrustLLM: Trustworthiness in Large Language Models | trustworthiness, large-language-models, safety | huang24x.md |
| 108 | MLAgentBench: Evaluating Language Agents on Machine Learning | language-agents, ml-experimentation, benchmark | huang24y.md |
| 109 | Token-Specific Watermarking with Enhanced Detectability and  | watermarking, large-language-models, AI-generated-text | huo24a.md |
| 110 | Understanding the Learning Dynamics of Alignment with Human  | RLHF, alignment, learning-dynamics | im24a.md |
| 111 | Human-like Category Learning by Injecting Ecological Priors  | category-learning, ecological-rationality, LLM-priors | jagadish24a.md |
| 112 | R2E: Turning any Github Repository into a Programming Agent  | LLM-agents, coding, evaluation-benchmark | jain24c.md |
| 113 | Degeneration-free Policy Optimization: RL Fine-Tuning for La | RL-fine-tuning, language-models, degeneration | jang24b.md |
| 114 | An Information-Theoretic Analysis of In-Context Learning | in-context-learning, information-theory, meta-learning | jeon24a.md |
| 115 | Towards Efficient Exact Optimization of Language Model Align | LLM-alignment, policy-optimization, KL-divergence | ji24c.md |
| 116 | LLM Maybe LongLM: SelfExtend LLM Context Window Without Tuni | long-context, llm, context-window-extension | jin24b.md |
| 117 | What Will My Model Forget? Forecasting Forgotten Examples in | catastrophic-forgetting, language-model-refinement, forecasting-forgetting | jin24d.md |
| 118 | Video-LaVIT: Unified Video-Language Pre-training with Decoup | video-language-pretraining, multimodal-llm, visual-motional-tokenization | jin24f.md |
| 119 | Language Models as Semantic Indexers | semantic-indexing, information-retrieval, language-models | jin24h.md |
| 120 | Model-Based Minimum Bayes Risk Decoding for Text Generation | minimum-bayes-risk, text-generation, decoding | jinnai24a.md |
| 121 | Watermark Stealing in Large Language Models | watermarking, LLM, AI-generated-content | jovanovic24a.md |
| 122 | Leveraging VLM-Based Pipelines to Annotate 3D Objects | vision-language-models, 3D-objects, annotation | kabra24a.md |
| 123 | Position: LLMs Can’t Plan, But Can Help Planning in LLM-Modu | LLM, planning, reasoning | kambhampati24a.md |
| 124 | C-RAG: Certified Generation Risks for Retrieval-Augmented La | RAG, certified-generation, hallucination | kang24a.md |
| 125 | Prismatic VLMs: Investigating the Design Space of Visually-C | vision-language-models, design-space, visual-conditioning | karamcheti24a.md |
| 126 | Debating with More Persuasive LLMs Leads to More Truthful An | LLM-debate, truthfulness, scalable-oversight | khan24a.md |
| 127 | An LLM Compiler for Parallel Function Calling | LLM, function-calling, parallel-execution | kim24y.md |
| 128 | Transformers Learn Nonlinear Features In Context: Nonconvex  | transformers, in-context-learning, mean-field-dynamics | kim24af.md |
| 129 | DistiLLM: Towards Streamlined Distillation for Large Languag | knowledge-distillation, large-language-models, autoregressive | ko24c.md |
| 130 | VideoPoet: A Large Language Model for Zero-Shot Video Genera | video-generation, large-language-models, multimodal | kondratyuk24a.md |
| 131 | Audio Flamingo: A Novel Audio Language Model with Few-Shot L | audio-language-model, few-shot-learning, dialogue | kong24a.md |
| 132 | CLLMs: Consistency Large Language Models | LLM-inference, Jacobi-decoding, consistency-distillation | kou24a.md |
| 133 | Implicit meta-learning may lead language models to trust mor | meta-learning, fine-tuning, source-reliability | krasheninnikov24a.md |
| 134 | Understanding the Effects of Iterative Prompting on Truthful | iterative-prompting, truthfulness, LLM-reliability | krishna24a.md |
| 135 | A Mechanistic Understanding of Alignment Algorithms: A Case  | DPO, alignment, toxicity | lee24a.md |
| 136 | A Human-Inspired Reading Agent with Gist Memory of Very Long | long-context, LLM-agent, gist-memory | lee24c.md |
| 137 | RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Fe | RLAIF, RLHF, AI-feedback | lee24t.md |
| 138 | Improving Instruction Following in Language Models through P | instruction-following, uncertainty-estimation, proxy-model | lee24z.md |
| 139 | Cell2Sentence: Teaching Large Language Models the Language o | single-cell-transcriptomics, large-language-models, gene-expression | levine24a.md |
| 140 | Improving Context Understanding in Multimodal Large Language | multimodal-LLM, compositional-learning, visual-understanding | li24s.md |
| 141 | Mastering Robot Manipulation with Multimodal Prompts through | robot-manipulation, multimodal-prompts, pretraining | li24x.md |
| 142 | VisionGraph: Leveraging Large Multimodal Models for Graph Th | large-multimodal-models, graph-theory, visual-reasoning | li24ab.md |
| 143 | Q-Probe: A Lightweight Approach to Reward Maximization for L | language-model, reward-maximization, Q-learning | li24ae.md |
| 144 | Promises and Pitfalls of Generative Masked Language Modeling | masked-language-modeling, text-generation, autoregressive | li24af.md |
| 145 | Visual-Text Cross Alignment: Refining the Similarity Score i | vision-language-models, CLIP, zero-shot | li24ag.md |
| 146 | Cascade-CLIP: Cascaded Vision-Language Embeddings Alignment  | CLIP, zero-shot, semantic-segmentation | li24aq.md |
| 147 | Chain of Code: Reasoning with a Language Model-Augmented Cod | chain-of-thought, code-emulation, reasoning | li24ar.md |
| 148 | Evaluating Quantized Large Language Models | post-training-quantization, large-language-models, evaluation | li24bb.md |
| 149 | The WMDP Benchmark: Measuring and Reducing Malicious Use wit | machine-unlearning, biosecurity, LLM-safety | li24bc.md |
| 150 | The Good, The Bad, and Why: Unveiling Emotions in Generative | emotion-understanding, large-language-models, generative-AI | li24bs.md |
| 151 | ReMax: A Simple, Effective, and Efficient Reinforcement Lear | RLHF, PPO, LLM-alignment | li24cd.md |
| 152 | DecisionNCE: Embodied Multimodal Representations via Implici | multimodal-pretraining, imitation-learning, representation-learning | li24cr.md |
| 153 | Revisiting the Role of Language Priors in Vision-Language Mo | vision-language-models, language-priors, zero-shot | lin24c.md |
| 154 | Non-confusing Generation of Customized Concepts in Diffusion | diffusion-models, concept-customization, compositional-generation | lin24d.md |
| 155 | Learning to Model the World With Language | world-models, language-grounding, agent-learning | lin24g.md |
| 156 | Selecting Large Language Model to Fine-tune via Rectified Sc | LLM-selection, scaling-law, fine-tuning | lin24j.md |
| 157 | Graph-enhanced Large Language Models in Asynchronous Plan Re | LLMs, asynchronous-planning, graph-enhanced-reasoning | lin24k.md |
| 158 | Dual Operating Modes of In-Context Learning | in-context-learning, task-retrieval, task-learning | lin24l.md |
| 159 | Use Your INSTINCT: INSTruction optimization for LLMs usIng N | instruction-optimization, neural-bandits, LLMs | lin24r.md |
| 160 | Adaptive Text Watermark for Large Language Models | watermarking, LLM, adversarial-robustness | liu24e.md |
| 161 | Decoding-time Realignment of Language Models | language-model-alignment, RLHF, decoding-time | liu24r.md |
| 162 | Reason for Future, Act for Now: A Principled Architecture fo | llm-agents, autonomous-decision-making, task-planning | liu24ab.md |
| 163 | How do Large Language Models Navigate Conflicts between Hone | llm-alignment, honesty, helpfulness | liu24bb.md |
| 164 | Entropy-Reinforced Planning with Large Language Models for D | drug-discovery, llm-planning, entropy-reinforced | liu24be.md |
| 165 | LIDAO: Towards Limited Interventions for Debiasing (Large) L | debiasing, large-language-models, fairness | liu24bm.md |
| 166 | DoRA: Weight-Decomposed Low-Rank Adaptation | parameter-efficient-fine-tuning, LoRA, weight-decomposition | liu24bn.md |
| 167 | Language-Driven Cross-Modal Classifier for Zero-Shot Multi-L | zero-shot-learning, multi-label-recognition, CLIP | liu24bq.md |
| 168 | In-context Vectors: Making In Context Learning More Effectiv | in-context-learning, latent-space, steering-vectors | liu24bx.md |
| 169 | SPHINX-X: Scaling Data and Parameters for a Family of Multi- | multimodal-LLM, visual-encoders, scaling | liu24cc.md |
| 170 | MobileLLM: Optimizing Sub-billion Parameter Language Models  | on-device-LLM, sub-billion-parameters, mobile-deployment | liu24ce.md |
| 171 | Non-Vacuous Generalization Bounds for Large Language Models | generalization-bounds, large-language-models, PAC-Bayes | lotfi24a.md |
| 172 | Discrete Diffusion Modeling by Estimating the Ratios of the  | discrete-diffusion, score-matching, language-generation | lou24a.md |
| 173 | HumanTOMATO: Text-aligned Whole-body Motion Generation | motion-generation, text-driven, whole-body | lu24b.md |
| 174 | WebLINX: Real-World Website Navigation with Multi-Turn Dialo | web-navigation, dialogue-agent, benchmark | lu24e.md |
| 175 | Open-Domain Text Evaluation via Contrastive Distribution Met | text-evaluation, open-domain-generation, contrastive-methods | lu24f.md |
| 176 | DiNADO: Norm-Disentangled Neurally-Decomposed Oracles for Co | controllable-generation, language-models, norm-disentanglement | lu24o.md |
| 177 | SPP: Sparsity-Preserved Parameter-Efficient Fine-Tuning for  | parameter-efficient-fine-tuning, sparsity, pruning | lu24p.md |
| 178 | Scaling Laws for Fine-Grained Mixture of Experts | mixture-of-experts, scaling-laws, LLM | ludziejewski24a.md |
| 179 | OMPO: A Unified Framework for RL under Policy and Dynamics S | reinforcement-learning, distribution-shift, policy-adaptation | luo24d.md |
| 180 | RoboMP$^2$: A Robotic Multimodal Perception-Planning Framewo | multimodal-LLM, robotics, perception-planning | lv24a.md |
| 181 | Coarse-to-Fine Highlighting: Reducing Knowledge Hallucinatio | hallucination, retrieval-augmented-generation, LLM | lv24c.md |
| 182 | Parameter Efficient Quasi-Orthogonal Fine-Tuning via Givens  | parameter-efficient-fine-tuning, orthogonal-fine-tuning, Givens-rotation | ma24a.md |
| 183 | Neighboring Perturbations of Knowledge Editing on Large Lang | knowledge-editing, LLM, neighboring-perturbations | ma24h.md |
| 184 | Split-and-Denoise: Protect large language model inference wi | local-differential-privacy, llm-inference, embedding-privacy | mai24a.md |
| 185 | tinyBenchmarks: evaluating LLMs with fewer examples | llm-evaluation, benchmark-efficiency, item-response-theory | maia-polo24a.md |
| 186 | Auto-Regressive Next-Token Predictors are Universal Learners | auto-regressive-models, next-token-prediction, universal-approximation | malach24a.md |
| 187 | Large Language Models are Geographically Biased | geographic-bias, large-language-models, fairness | manvi24a.md |
| 188 | Copyright Traps for Large Language Models | copyright, membership-inference, LLM-training-data | meeus24a.md |
| 189 | Provable Interactive Learning with Hindsight Instruction Fee | interactive-learning, hindsight-feedback, instruction-following | misra24a.md |
| 190 | Language Models with Conformal Factuality Guarantees | conformal-prediction, factuality, language-model-reliability | mohri24a.md |
| 191 | Controlled Decoding from Language Models | controlled-decoding, RLHF, KL-regularization | mudgal24a.md |
| 192 | Active Preference Learning for Large Language Models | active-learning, RLHF, preference-learning | muldrew24a.md |
| 193 | Nash Learning from Human Feedback | Nash-learning, RLHF, preference-learning | munos24a.md |
| 194 | Learning to Route Among Specialized Experts for Zero-Shot Ge | mixture-of-experts, zero-shot-generalization, model-routing | muqeeth24a.md |
| 195 | Autoformalizing Euclidean Geometry | autoformalization, Euclidean-geometry, neuro-symbolic | murphy24a.md |
| 196 | BAGEL: Bootstrapping Agents by Guiding Exploration with Lang | LLM-agents, exploration, language-instructions | murty24a.md |
| 197 | NExT: Teaching Large Language Models to Reason about Code Ex | code-execution, chain-of-thought, LLM-reasoning | ni24a.md |
| 198 | Compositional Text-to-Image Generation with Dense Blob Repre | text-to-image, compositional-generation, blob-representations | nie24b.md |
| 199 | Reward Model Learning vs. Direct Policy Optimization: A Comp | RLHF, DPO, human-preferences | nika24a.md |
| 200 | RoSA: Accurate Parameter-Efficient Fine-Tuning via Robust Ad | parameter-efficient-fine-tuning, robust-PCA, LoRA | nikdan24a.md |
| 201 | Risk Aware Benchmarking of Large Language Models | LLM-benchmarking, stochastic-dominance, risk-assessment | nitsure24a.md |
| 202 | Skill Set Optimization: Reinforcing Language Model Behavior  | LLM-agents, skill-learning, sequential-decision-making | nottingham24a.md |
| 203 | Do Language Models Exhibit the Same Cognitive Biases in Prob | large-language-models, cognitive-biases, problem-solving | opedal24a.md |
| 204 | Towards Modular LLMs by Building and Reusing a Library of Lo | LoRA, parameter-efficient-finetuning, adapter-reuse | ostapenko24a.md |
| 205 | Structured Chemistry Reasoning with Large Language Models | large-language-models, chemistry-reasoning, structured-reasoning | ouyang24a.md |
| 206 | Feedback Loops With Language Models Drive In-Context Reward  | language-model-feedback-loops, reward-hacking, in-context-learning | pan24d.md |
| 207 | Auto-Encoding Morph-Tokens for Multimodal LLM | multimodal-LLM, visual-generation, visual-comprehension | pan24h.md |
| 208 | BRAIn: Bayesian Reward-conditioned Amortized Inference for n | RLHF, distribution-matching, language-model-alignment | pandey24a.md |
| 209 | Self-Alignment of Large Language Models via Monopolylogue-ba | LLM-alignment, social-simulation, self-alignment | pang24a.md |
| 210 | Arrows of Time for Large Language Models | arrow-of-time, autoregressive-LLM, language-modeling | papadopoulos24a.md |
| 211 | In-Context Unlearning: Language Models as Few-Shot Unlearner | machine-unlearning, in-context-learning, language-models | pawelczyk24a.md |
| 212 | Exploiting Code Symmetries for Learning Program Semantics | code-symmetries, program-semantics, LLMs | pei24b.md |
| 213 | eCeLLM: Generalizing Large Language Models for E-commerce fr | e-commerce, large-language-models, instruction-tuning | peng24c.md |
| 214 | Pragmatic Feature Preferences: Learning Reward-Relevant Pref | reward-learning, preference-learning, pragmatic-communication | peng24d.md |
| 215 | UPOCR: Towards Unified Pixel-Level OCR Interface | OCR, unified-interface, pixel-level | peng24e.md |
| 216 | Extracting Training Data From Document-Based VQA Models | vision-language-models, memorization, training-data-extraction | pinto24a.md |
| 217 | diff History for Neural Language Agents | language-agents, embodied-control, observation-compression | piterbarg24a.md |
| 218 | Amortizing Pragmatic Program Synthesis with Rankings | program-synthesis, rational-speech-acts, amortization | pu24c.md |
| 219 | Momentor: Advancing Video Large Language Model with Fine-Gra | video-LLM, temporal-reasoning, fine-grained-understanding | qian24a.md |
| 220 | To Cool or not to Cool? Temperature Network Meets Large Foun | temperature-scaling, foundation-models, distributionally-robust-optimization | qiu24c.md |
| 221 | Transferring Knowledge From Large Foundation Models to Small | knowledge-distillation, foundation-models, transfer-learning | qiu24d.md |
| 222 | STEER: Assessing the Economic Rationality of Large Language  | LLM-agents, economic-rationality, decision-making | raman24b.md |
| 223 | WARM: On the Benefits of Weight Averaged Reward Models | reward-hacking, RLHF, reward-model | rame24a.md |
| 224 | Generalization to New Sequential Decision Making Tasks with  | in-context-learning, sequential-decision-making, transformers | raparthy24a.md |
| 225 | Provably Robust DPO: Aligning Language Models with Noisy Fee | DPO, preference-learning, noisy-feedback | ray-chowdhury24a.md |
| 226 | Position: Key Claims in LLM Research Have a Long Tail of Foo | LLM-research, claims-analysis, position-paper | rogers24a.md |
| 227 | Fast Adversarial Attacks on Language Models In One GPU Minut | adversarial-attacks, beam-search, language-models | sadasivan24a.md |
| 228 | Failures Are Fated, But Can Be Faded: Characterizing and Mit | failure-characterization, bias-mitigation, vision-language-models | sagar24a.md |
| 229 | Stay on Topic with Classifier-Free Guidance | classifier-free-guidance, language-modeling, prompt-adherence | sanchez24a.md |
| 230 | Robust CLIP: Unsupervised Adversarial Fine-Tuning of Vision  | adversarial-robustness, CLIP, vision-language-models | schlarmann24a.md |
| 231 | In-Context Learning Agents Are Asymmetric Belief Updaters | in-context-learning, belief-updating, asymmetric-learning | schubert24a.md |
| 232 | Algorithm of Thoughts: Enhancing Exploration of Ideas in Lar | chain-of-thought, reasoning, LLMs | sel24a.md |
| 233 | Improved Generalization of Weight Space Networks via Augment | weight-space-networks, data-augmentation, neural-fields | shamsian24a.md |
| 234 | Language Generation with Strictly Proper Scoring Rules | language-generation, scoring-rules, maximum-likelihood-estimation | shao24c.md |
| 235 | Thermometer: Towards Universal Calibration for Large Languag | LLM-calibration, uncertainty-quantification, instruction-tuning | shen24c.md |
| 236 | Position: Do pretrained Transformers Learn In-Context by Gra | in-context-learning, gradient-descent, transformer-mechanics | shen24d.md |
| 237 | Tag-LLM: Repurposing General-Purpose LLMs for Specialized Do | domain-adaptation, LLM-specialization, tag-based-fine-tuning | shen24f.md |
| 238 | Why Larger Language Models Do In-context Learning Differentl | in-context-learning, large-language-models, model-size-scaling | shi24f.md |
| 239 | Representation Surgery: Theory and Practice of Affine Steeri | representation-steering, bias-mitigation, affine-transformations | singh24d.md |
| 240 | In-Context Reinforcement Learning for Variable Action Spaces | in-context-learning, transformers, variable-action-spaces | sinii24a.md |
| 241 | Should we be going MAD? A Look at Multi-Agent Debate Strateg | multi-agent-debate, LLMs, factual-accuracy | smit24a.md |
| 242 | Latent Logic Tree Extraction for Event Sequence Explanation  | LLMs, event-sequences, logic-trees | song24j.md |
| 243 | ReGAL: Refactoring Programs to Discover Generalizable Abstra | program-synthesis, LLM, code-abstraction | stengel-eskin24a.md |
| 244 | RLVF: Learning from Verbal Feedback without Overgeneralizati | RLHF, verbal-feedback, LLM-alignment | stephan24a.md |
| 245 | ED-Copilot: Reduce Emergency Department Wait Time with Langu | emergency-department, LLM, diagnostic-assistance | sun24a.md |
| 246 | DFA-RAG: Conversational Semantic Router for Large Language M | RAG, finite-automaton, LLM | sun24e.md |
| 247 | FedBPT: Efficient Federated Black-box Prompt Tuning for Larg | federated-learning, black-box-prompt-tuning, LLM | sun24j.md |
| 248 | video-SALMONN: Speech-Enhanced Audio-Visual Large Language M | audio-visual, speech-understanding, multimodal-llm | sun24l.md |
| 249 | BBox-Adapter: Lightweight Adapting for Black-Box Large Langu | black-box-llm, adapter, fine-tuning | sun24p.md |
| 250 | A Minimaximalist Approach to Reinforcement Learning from Hum | RLHF, self-play, preference-optimization | swamy24a.md |
| 251 | Preference Fine-Tuning of LLMs Should Leverage Suboptimal, O | RLHF, preference-learning, on-policy-data | tajwar24a.md |
| 252 | Generalized Preference Optimization: A Unified Approach to O | preference-optimization, offline-alignment, unified-framework | tang24b.md |
| 253 | StrokeNUWA—Tokenizing Strokes for Vector Graphic Synthesis | vector-graphics, LLM-tokenization, stroke-representation | tang24h.md |
| 254 | MathScale: Scaling Instruction Tuning for Mathematical Reaso | mathematical-reasoning, instruction-tuning, data-synthesis | tang24k.md |
| 255 | Coactive Learning for Large Language Models using Implicit U | coactive-learning, LLM-finetuning, implicit-feedback | tucker24a.md |
| 256 | Do Large Language Models Perform the Way People Expect? Meas | LLM-evaluation, human-generalization, deployment-decisions | vafa24a.md |
| 257 | Code as Reward: Empowering Reinforcement Learning with VLMs | reinforcement-learning, vision-language-models, reward-generation | venuto24a.md |
| 258 | Position: Will we run out of data? Limits of LLM scaling bas | LLM-scaling, data-limits, human-generated-text | villalobos24a.md |
| 259 | A Language Model’s Guide Through Latent Space | concept-guidance, language-models, latent-space | von-rutte24a.md |
| 260 | ConTextual: Evaluating Context-Sensitive Text-Rich Visual Re | multimodal-reasoning, text-rich-visual-reasoning, benchmark | wadhawan24a.md |
| 261 | AlphaZero-Like Tree-Search can Guide Large Language Model De | AlphaZero, tree-search, LLM-decoding | wan24c.md |
| 262 | Towards Unified Multi-granularity Text Detection with Intera | text-detection, multi-granularity, interactive-attention | wan24i.md |
| 263 | Understanding Reasoning Ability of Language Models From the  | language-model-reasoning, pre-training, reasoning-paths | wang24a.md |
| 264 | One Prompt is not Enough: Automated Construction of a Mixtur | prompt-optimization, mixture-of-experts, LLM | wang24b.md |
| 265 | Executable Code Actions Elicit Better LLM Agents | LLM-agents, code-generation, executable-actions | wang24h.md |
| 266 | Diagnosing the Compositional Knowledge of Vision Language Mo | vision-language-models, compositional-reasoning, game-theory | wang24n.md |
| 267 | MEMORYLLM: Towards Self-Updatable Large Language Models | LLM, self-updatable, continual-learning | wang24s.md |
| 268 | SciBench: Evaluating College-Level Scientific Problem-Solvin | LLM-benchmarking, scientific-reasoning, college-level-problems | wang24z.md |
| 269 | Transforming and Combining Rewards for Aligning Large Langua | reward-modeling, LLM-alignment, preference-learning | wang24ay.md |
| 270 | TroVE: Inducing Verifiable and Efficient Toolboxes for Solvi | language-models, tool-use, program-synthesis | wang24az.md |
| 271 | InstructRetro: Instruction Tuning post Retrieval-Augmented P | retrieval-augmented-generation, instruction-tuning, large-language-models | wang24bd.md |
| 272 | LLM-Empowered State Representation for Reinforcement Learnin | reinforcement-learning, state-representation, large-language-models | wang24bh.md |
| 273 | RL-VLM-F: Reinforcement Learning from Vision Language Founda | reinforcement-learning, vision-language-models, reward-generation | wang24bn.md |
| 274 | Rethinking Generative Large Language Model Evaluation for Se | llm-evaluation, multiple-choice-qa, semantic-comprehension | wei24c.md |
| 275 | Magicoder: Empowering Code Generation with OSS-Instruct | code-generation, llm, synthetic-data | wei24h.md |
| 276 | QuRating: Selecting High-Quality Data for Training Language  | data-selection, pre-training, language-models | wettig24a.md |
| 277 | Fundamental Limitations of Alignment in Large Language Model | LLM-alignment, safety, fundamental-limitations | wolf24a.md |
| 278 | Optimizing Watermarks for Large Language Models | LLM-watermarking, text-quality, identifiability | wouters24a.md |
| 279 | NExT-GPT: Any-to-Any Multimodal LLM | multimodal-LLM, any-to-any-generation, multi-modal-output | wu24e.md |
| 280 | A Resilient and Accessible Distribution-Preserving Watermark | LLM-watermarking, distribution-preservation, resilience | wu24h.md |
| 281 | Evaluating and Analyzing Relationship Hallucinations in Larg | hallucination, vision-language-models, relationship-detection | wu24l.md |
| 282 | VoroNav: Voronoi-based Zero-shot Object Navigation with Larg | object-navigation, zero-shot, voronoi | wu24u.md |
| 283 | Detecting Any instruction-to-answer interaction relationship | medical-VQA, visual-question-answering, instruction-following | wu24ac.md |
| 284 | Q-Align: Teaching LMMs for Visual Scoring via Discrete Text- | image-quality-assessment, large-multimodal-models, visual-scoring | wu24ah.md |
| 285 | Training Large Language Models for Reasoning through Reverse | large-language-models, reasoning, reinforcement-learning | xi24a.md |
| 286 | LESS: Selecting Influential Data for Targeted Instruction Tu | instruction-tuning, data-selection, influence-functions | xia24c.md |
| 287 | TravelPlanner: A Benchmark for Real-World Planning with Lang | LLM-planning, benchmark, language-agents | xie24j.md |
| 288 | Iterative Preference Learning from Human Feedback: Bridging  | RLHF, KL-regularization, iterative-preference-learning | xiong24a.md |
| 289 | Reprompting: Automated Chain-of-Thought Prompt Inference Thr | chain-of-thought, prompt-optimization, Gibbs-sampling | xu24b.md |
| 290 | Is DPO Superior to PPO for LLM Alignment? A Comprehensive St | RLHF, DPO, PPO | xu24h.md |
| 291 | Contrastive Preference Optimization: Pushing the Boundaries  | machine-translation, contrastive-preference-optimization, LLM | xu24t.md |
| 292 | Libra: Building Decoupled Vision System on Large Language Mo | vision-language-model, decoupled-vision, cross-modal-interaction | xu24ab.md |
| 293 | Language Agents with Reinforcement Learning for Strategic Pl | language-agents, reinforcement-learning, social-deduction-games | xu24ad.md |
| 294 | OpenMoE: An Early Effort on Open Mixture-of-Experts Language | mixture-of-experts, open-source-LLM, scaling | xue24c.md |
| 295 | Exploring the LLM Journey from Cognition to Expression with  | LLM-interpretability, linear-representations, cognition-expression | yan24c.md |
| 296 | DoraemonGPT: Toward Understanding Dynamic Scenes with Large  | video-understanding, LLM-agent, dynamic-scene-analysis | yang24d.md |
| 297 | A Dense Reward View on Aligning Text-to-Image Diffusion with | text-to-image-diffusion, preference-alignment, dense-reward | yang24e.md |
| 298 | Rewards-in-Context: Multi-objective Alignment of Foundation  | multi-objective-alignment, reinforcement-learning, dynamic-preferences | yang24q.md |
| 299 | UniAudio: Towards Universal Audio Generation with Large Lang | audio-generation, large-language-models, universal-model | yang24x.md |
| 300 | Position: Video as the New Language for Real-World Decision  | video-generation, decision-making, world-models | yang24z.md |
| 301 | Mastering Text-to-Image Diffusion: Recaptioning, Planning, a | text-to-image, diffusion-models, multimodal-LLM | yang24ai.md |
| 302 | Junk DNA Hypothesis: Pruning Small Pre-Trained Weights $\tex | LLM-pruning, pre-trained-weights, downstream-tasks | yin24b.md |
| 303 | Outlier Weighed Layerwise Sparsity (OWL): A Missing Secret S | LLM-pruning, sparsity, outlier-weights | yin24e.md |
| 304 | MMT-Bench: A Comprehensive Multimodal Benchmark for Evaluati | multimodal-benchmark, vision-language-models, multitask-evaluation | ying24a.md |
| 305 | Privacy-Preserving Instructions for Aligning Large Language  | differential-privacy, llm-alignment, instruction-tuning | yu24e.md |
| 306 | Few-Shot Character Understanding in Movies as an Assessment  | theory-of-mind, few-shot-learning, meta-learning | yu24n.md |
| 307 | MM-Vet: Evaluating Large Multimodal Models for Integrated Ca | multimodal-models, evaluation-benchmark, integrated-capabilities | yu24o.md |
| 308 | Language Models are Super Mario: Absorbing Abilities from Ho | model-merging, delta-parameters, language-model-capabilities | yu24p.md |
| 309 | Self-Rewarding Language Models | self-rewarding, llm-alignment, iterative-training | yuan24d.md |
| 310 | RigorLLM: Resilient Guardrails for Large Language Models aga | llm-safety, guardrails, harmful-content | yuan24f.md |
| 311 | tnGPS: Discovering Unknown Tensor Network Structure Search A | tensor-networks, structure-search, LLM-driven-optimization | zeng24b.md |
| 312 | Token-level Direct Preference Optimization | RLHF, direct-preference-optimization, token-level | zeng24c.md |
| 313 | Learning Reward for Robot Skills Using Large Language Models | reward-learning, LLM, robot-skills | zeng24d.md |
| 314 | LQER: Low-Rank Quantization Error Reconstruction for LLMs | LLM-quantization, low-rank-approximation, post-training | zhang24j.md |
| 315 | Look Ahead or Look Around? A Theoretical Comparison Between  | self-supervised-learning, autoregressive, masked-pretraining | zhang24m.md |
| 316 | Watermarks in the Sand: Impossibility of Strong Watermarking | watermarking, language-models, impossibility | zhang24o.md |
| 317 | Generating Chain-of-Thoughts with a Pairwise-Comparison Appr | chain-of-thought, pairwise-comparison, LLM-reasoning | zhang24t.md |
| 318 | Advancing DRL Agents in Commercial Fighting Games: Training, | deep-RL, fighting-games, human-alignment | zhang24v.md |
| 319 | Towards Causal Foundation Model: on Duality between Optimal  | causal-inference, foundation-models, attention-mechanism | zhang24x.md |
| 320 | Parameter-Efficient Fine-Tuning with Controls | LoRA, parameter-efficient-fine-tuning, control-theory | zhang24y.md |
| 321 | Revisiting Zeroth-Order Optimization for Memory-Efficient LL | zeroth-order-optimization, LLM-fine-tuning, memory-efficiency | zhang24ad.md |
| 322 | DPZero: Private Fine-Tuning of Language Models without Backp | differential-privacy, LLM-fine-tuning, zeroth-order-optimization | zhang24af.md |
| 323 | Conditional Language Learning with Context | language-modeling, conditional-learning, context-awareness | zhang24ag.md |
| 324 | Multi-Factor Adaptive Vision Selection for Egocentric Video  | egocentric-video, visual-question-answering, multi-factor-attention | zhang24aj.md |
| 325 | In-Context Principle Learning from Mistakes | in-context-learning, principle-learning, mistake-correction | zhang24at.md |
| 326 | How Language Model Hallucinations Can Snowball | hallucination, language-models, snowballing-errors | zhang24ay.md |
| 327 | Trustworthy Alignment of Retrieval-Augmented Large Language  | retrieval-augmented-generation, LLM-alignment, trustworthiness | zhang24bg.md |
| 328 | Switchable Decision: Dynamic Neural Generation Networks | auto-regressive-generation, early-exit, dynamic-inference | zhang24bj.md |
| 329 | Interpreting and Improving Large Language Models in Arithmet | LLM-interpretability, arithmetic, mechanistic-analysis | zhang24bk.md |
| 330 | NExT-Chat: An LMM for Chat, Detection and Segmentation | large-multimodal-models, visual-grounding, segmentation | zhang24bu.md |
| 331 | PARDEN, Can You Repeat That? Defending against Jailbreaks vi | jailbreak-defense, LLM-safety, repetition-based-detection | zhang24ca.md |
| 332 | Offline Training of Language Model Agents with Functions as  | LLM-agents, offline-training, function-optimization | zhang24cd.md |
| 333 | Confronting Reward Overoptimization for Diffusion Models: A  | diffusion-models, reward-overoptimization, alignment | zhang24ch.md |
| 334 | Long Is More for Alignment: A Simple but Tough-to-Beat Basel | instruction-fine-tuning, data-selection, LLM-alignment | zhao24b.md |
| 335 | Probabilistic Inference in Language Models via Twisted Seque | LLM-alignment, sequential-Monte-Carlo, probabilistic-inference | zhao24c.md |
| 336 | Learning and Forgetting Unsafe Examples in Large Language Mo | LLM-safety, fine-tuning, unsafe-content | zhao24e.md |
| 337 | Subgoal-based Demonstration Learning for Formal Theorem Prov | theorem-proving, LLM, in-context-learning | zhao24h.md |
| 338 | LangCell: Language-Cell Pre-training for Cell Identity Under | cell-identity, pre-training, language-model | zhao24u.md |
| 339 | PRISE: LLM-Style Sequence Compression for Learning Temporal  | temporal-action-abstractions, sequence-compression, LLM | zheng24b.md |
| 340 | GPT-4V(ision) is a Generalist Web Agent, if Grounded | multimodal-LLM, web-agent, GPT-4V | zheng24e.md |
| 341 | Self-Infilling Code Generation | code-generation, infilling, auto-regressive-decoding | zheng24o.md |
| 342 | Language Agent Tree Search Unifies Reasoning, Acting, and Pl | language-agents, tree-search, reasoning-and-planning | zhou24r.md |
| 343 | ArCHer: Training Language Model Agents via Hierarchical Mult | language-model-agents, hierarchical-RL, multi-turn-dialogue | zhou24t.md |
| 344 | Improving Open-Ended Text Generation via Adaptive Decoding | decoding, text-generation, language-models | zhu24d.md |
| 345 | Iterative Data Smoothing: Mitigating Reward Overfitting and  | RLHF, reward-model, overfitting | zhu24e.md |
| 346 | Dynamic Evaluation of Large Language Models by Meta Probing  | LLM-evaluation, data-contamination, dynamic-evaluation | zhu24m.md |
| 347 | Language Models Represent Beliefs of Self and Others | theory-of-mind, language-models, belief-representation | zhu24o.md |
| 348 | Reinformer: Max-Return Sequence Modeling for Offline RL | offline-RL, sequence-modeling, transformers | zhuang24b.md |
| 349 | GPTSwarm: Language Agents as Optimizable Graphs | LLM-agents, graph-optimization, prompt-engineering | zhuge24a.md |
| 350 | Emergence of In-Context Reinforcement Learning from Noise Di | in-context-reinforcement-learning, transformers, noise-distillation | zisman24a.md |
| 351 | Safety Fine-Tuning at (Almost) No Cost: A Baseline for Visio | safety-fine-tuning, vision-language-models, jailbreak | zong24a.md |
| 352 | Fool Your (Vision and) Language Model with Embarrassingly Si | adversarial-robustness, permutations, vision-language-models | zong24b.md |
