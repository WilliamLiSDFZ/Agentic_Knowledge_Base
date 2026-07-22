# InstructProtein: Aligning Human and Protein Language via Knowledge Instruction

**Source**: https://aclanthology.org/2024.acl-long.62/

## [POSITIVE] Multilingual Pre-Training on Protein and Natural Language Corpora
Incrementally pre-training an LLM (OPT-1.3B) on both protein sequences (UniRef100) and natural language text (PubMed abstracts) before instruction tuning

**Delta**: outperforms baseline
**Condition**: Protein sequence understanding tasks (GO-BP, GO-MF, GO-CC, Location, MIB)

**Evidence**: "InstructProtein clearly outperforms the LLMs (i.e., ChatGPT, LLaMA, Alpaca) which are stemmed from natural language training corpora. These results demonstrate that training with the corpus where proteins and natural language coexist is beneficial to LLMs, enhancing their proficiency in protein language understanding."

## [POSITIVE] Knowledge Graph-Based Instruction Generation
Constructing a protein knowledge graph from UniProtKB and using KG triples (converted to instructions via ChatGPT) for supervised instruction tuning, rather than directly using raw documents or seed tasks

**Delta**: outperforms state-of-the-art LLMs by a large margin
**Condition**: All protein-text generation tasks (Held-In and Held-Out)

**Evidence**: "Extensive experiments have demonstrated that the introduced protein knowledge instructions significantly improve the performance of LLMs on protein understanding and design tasks."

## [POSITIVE] Knowledge Causal Modeling (KCM)
Augmenting KG triples with causal relationships between protein annotations (e.g., domain → molecular function → biological process) organized as a directed acyclic graph, inspired by chain-of-thought reasoning

**Delta**: +0.84 ACC on Location (Sub) (69.95 → 70.79); neutral/slight on GO-MF (85.92 → 85.83)
**Condition**: Protein subcellular localization prediction (Location Sub); marginal effect on GO-MF

**Evidence**: "We also observe that the causal relationship between annotations introduced by KCM improves the performance."

## [POSITIVE] Debiased Sampling Strategy (Sequence + Property Clustering via KGE)
Clustering proteins by both sequence similarity (MMseqs2 edit distance) and property similarity (KGE-based distance) and uniformly sampling triples per cluster to address annotation imbalance

**Delta**: +8.22 ACC on Location (Sub) vs. unclustering (58.12 → 69.95 with Seq. & Prop. KGE, No KCM)
**Condition**: Tasks with significant annotation imbalance (e.g., subcellular localization prediction)

**Evidence**: "clustering similar proteins in annotation imbalance-related tasks (Location) can effectively improve model performance... KGE has a stronger ability to model property similarity."

## [NEGATIVE] Sequence-Only Clustering for Debiased Sampling
Clustering proteins based only on sequence similarity (edit distance) without considering property similarity for debiased triple sampling

**Delta**: -1.88 AUPR on GO-MF vs. unclustering (83.70 vs. 85.58)
**Condition**: Tasks where annotation imbalance is not significant (e.g., GO molecular function prediction)

**Evidence**: "for tasks where annotation imbalance is not significant (GO), the clustering method based on sequence alone degrade model performance, which is reasonable because this method reduces the frequency of hard samples (proteins with similar sequences but different functions)."

## [POSITIVE] KGE-Based Property Similarity vs. Edit Distance for Property Clustering
Using knowledge graph embedding (KGE) distance instead of edit distance to measure property similarity when clustering proteins for debiased sampling

**Delta**: +3.38 ACC on Location (Sub) (66.57 → 69.95); +1.58 AUPR on GO-MF (84.34 → 85.92)
**Condition**: Both annotation-imbalanced (Location) and balanced (GO) tasks

**Evidence**: "We compare property clustering methods based on KGE distance and edit distance, and the results prove that KGE has a stronger ability to model property similarity."

## [NEGATIVE] Annotation Imbalance in Training Corpus
Training LLMs directly on imbalanced protein-text corpora where well-studied proteins dominate annotations, causing model bias toward frequent categories

**Delta**: biased predictions (e.g., all 1806–1808 out of 1808 predictions mapped to single category)
**Condition**: Subcellular localization prediction with OPT, LLaMA, Alpaca, Galactica

**Evidence**: "The outcomes of LLMs are presented in Table 1, from which one can observe that these LLMs are biased in a certain category, due to the annotation imbalance in the training corpus of LLMs."

## [NEGATIVE] Absence of Instructional Signals in Protein Corpus
Protein-related textual content consisting primarily of descriptive narratives without instructional signals, hindering zero-shot task generalization

**Delta**: subpar zero-shot performance
**Condition**: Zero-shot protein understanding tasks for models trained without instruction tuning

**Evidence**: "The absence of instructional signals: Protein-related textual content is primarily comprised of descriptive narratives, often devoid of instructional signals specifically designed for training LLMs. This inherent disparity obstructs a holistic understanding of a wide range of tasks, ultimately resulting in subpar zero-shot performance."

## [NEGATIVE] Template-Based Instruction Dataset (Mol-Instructions approach)
Using fixed instruction templates without diversity for protein instruction tuning

**Delta**: all negative predictions on GO and MIB benchmarks
**Condition**: Held-In (GO) and Held-Out (MIB) protein understanding tasks

**Evidence**: "The instruction templates of Mol-Instructions are not adequately diverse, thus unable to understand the tasks in the GO and MIB benchmarks, leading to all negative predictions."

## [POSITIVE] Scaling Model Parameter Size
Increasing the number of parameters in InstructProtein (125M → 350M → 1.3B) for protein de novo design

**Delta**: pLDDT increases with model scale
**Condition**: Protein de novo design (structure-based sequence generation)

**Evidence**: "pLDDT increases with model scale, suggesting that scaling up the parameter size results in the generation of sequences with fewer intrinsically disordered regions."

## [POSITIVE] KG Completion Task Framing for Instruction Generation
Simulating KG completion tasks (head prediction, tail prediction, triple classification) as templates for generating diverse protein instructions via ChatGPT

**Delta**: factual, logical, and diverse instructions
**Condition**: Instruction dataset construction for supervised fine-tuning

**Evidence**: "the KG completion tasks offer a comprehensive template for proposing domain-specific tasks based on triples. Therefore, we simulate KG completion, and employ general LLMs (e.g., ChatGPT) to transform KG triples with retrieved KCM into instructions."

## [NEGATIVE] Unidirectional Protein-to-Text Training (prior work limitation)
Training models only to convert protein sequences to text descriptions without the ability to generate protein sequences from text instructions

**Delta**: BioMedGPT focuses solely on converting proteins to texts and lacks protein design capabilities
**Condition**: Protein sequence design / instruction-protein pairing tasks

**Evidence**: "these architectures predominantly exhibit a unidirectional cross-modal capability, focusing solely on converting protein language to textual description."

## [POSITIVE] Pre-training on Protein Corpus Before Instruction Tuning
Including protein sequence pre-training before instruction tuning; Mol-Instructions lacks this step

**Delta**: InstructProtein: 55.57/65.07/79.24 vs. Mol-Instructions: 12.81/12.57/12.44 on Fold/SuperFamily/Family pairing
**Condition**: Instruction-protein pairing task (fold, superfamily, family levels)

**Evidence**: "Mol-Instructions lacks pre-training on protein corpora, which makes it difficult for the model to distinguish the nuances of proteins, resulting in poor results."

## [NEUTRAL] Data Contamination Prevention via Sequence Identity Clustering
Using MMseqs2 to cluster proteins at 70% identity threshold and removing clusters containing test set proteins from training data

**Delta**: 19,455 sequences removed
**Condition**: Training data preprocessing to prevent evaluation leakage

**Evidence**: "we use mmseqs2 to cluster proteins with an identity surpassing the 70% threshold, then remove the clusters containing the proteins in the test set, for a total of 19,455 sequences."
