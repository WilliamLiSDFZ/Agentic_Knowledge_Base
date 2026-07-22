# Disentangling Dialect from Social Bias via Multitask Learning to Improve Fairness

**Source**: https://aclanthology.org/2024.findings-acl.553/

## [POSITIVE] Multitask Learning with Dialect Auxiliary Task (MULTITASK+AAE)
A weight-sharing joint learning architecture with a shared encoder and separate classification heads for five bias aspects plus an auxiliary AAE dialect detection head, trained round-robin

**Delta**: improves over best baseline and single-task learning for four out of five bias aspects; ingroup F1 .227 vs .000 for baselines
**Condition**: Social bias detection across five aspects (offensiveness, intent, lewdness, target group, ingroup) on SBIC corpus

**Evidence**: "The proposed multitask learning approach improves over the best baseline and over single-task learning for four out of five bias aspects. Moreover, the dialect auxiliary task improves fairness for texts with dialect language and also benefits non-dialect texts."

## [POSITIVE] Multitask Learning without Dialect (MULTITASK)
Weight-sharing joint learning architecture with shared encoder and five classification heads for bias aspects only, without dialect auxiliary task

**Delta**: ingroup F1 .235 vs .000 for single-task; offensiveness AAE macro F1 .816 vs .787 for SINGLETASK
**Condition**: Social bias detection, especially for ingroup and offensiveness aspects

**Evidence**: "Both multitask approaches further improve upon SINGLETASK, showing performance increases in most aspects except target group. The biggest gains are achieved for the offensiveness and ingroup aspects. For ingroup, seemingly the most challenging aspect, MULTITASK and MULTITASK+AAE are among the only three evaluated models that show a learning effect, with a significantly improved F1-score of .235 and .227 respectively."

## [POSITIVE] Single-Task Fine-tuning with AAE Modeling (SINGLETASK+AAE)
Single-task classification model that also jointly learns AAE dialect detection as an auxiliary task

**Delta**: lewdness F1 .755 vs .744; ingroup F1 .108 vs .000 for SINGLETASK
**Condition**: Single-task learning setting, especially for lewdness and ingroup aspects

**Evidence**: "Modeling dialects seems to improve results most when finetuning on a single task. This is most visible for lewdness and ingroup, where the scores of SINGLETASK+AAE increase by .011 and .108 over SINGLETASK, respectively."

## [POSITIVE] Supervised Fine-tuning (SINGLETASK) vs. Generative Baselines
Fine-tuning DeBERTa-v3-base with a classification head on individual bias aspect labels, compared to GPT-2 generative and few-shot approaches

**Delta**: +9.6 F1 points on target group (.833 vs .737 few-shot); outperforms GPT-2 and few-shot on three aspects significantly
**Condition**: Social bias detection compared to GPT-2 generative and few-shot LLM baselines

**Evidence**: "Fine-tuning on single labels seems to work notably better than using a generative approach: SINGLETASK outperforms the two baselines (GPT-2 and few-shot learning) on three bias aspects significantly. We observe a strong F1-score gain of 9.6 points over the best baseline on the target group aspect (.833 vs. .737)."

## [POSITIVE] Loss Weighting for Class Imbalance (AAEwgh)
Weighing the loss of each label relative to label distribution to handle heavy class imbalance in dialect classification, instead of subsampling

**Delta**: macro F1 .78 vs .70 for TwitterAAE baseline; positive class precision .80 vs .73 for TwitterAAE
**Condition**: AAE dialect classification on heavily imbalanced TwitterAAE corpus (only ~2% AAE)

**Evidence**: "Overall, AAEwgh not only performs better than TwitterAAE in all metrics, but also improves over AAEsmp, except for positive class recall and negative class precision... Gains of both approaches over the TwitterAAE baseline are significant (‡ for p < .01)."

## [NEUTRAL] Subsampling for Class Imbalance (AAEsmp)
Randomly sampling non-AAE texts to match the number of AAE texts and create a balanced training dataset

**Delta**: Higher AAE recall than AAEwgh but lower overall macro F1; macro F1 .77 vs .78 for AAEwgh
**Condition**: AAE dialect classification; better recall for positive class but worse overall performance than loss weighting

**Evidence**: "While AAEsmp seems better in finding dialect texts (higher recall for Pos), AAEwgh performs better overall... AAEsmp would likely introduce more noise through false predictions, as indicated by its lower recall for the negative class, which also does not improve over the baseline."

## [POSITIVE] Data Augmentation with Automated Dialect Labels
Training a dialect classifier on a separate corpus (TwitterAAE) and using it to automatically annotate the main bias corpus (SBIC) with AAE dialect labels for multitask learning

**Delta**: enables multitask learning with dialect; no separate quantitative delta reported for augmentation alone
**Condition**: When no dialect-annotated bias detection corpus exists; prerequisite for dialect-aware multitask learning

**Evidence**: "Previous work has shown that parallel data benefits multitask learning, as correlations between multiple labels are easier to identify, positively affecting all learned tasks... It enables multitask learning approaches to transfer knowledge between the primary and auxiliary tasks more efficiently."

## [NEGATIVE] Separate Corpus for Auxiliary Task (without data augmentation)
Using a separate dialect corpus rather than augmenting the main corpus with dialect labels for multitask learning

**Delta**: not quantified; described as causing domain transfer problems and noise
**Condition**: Multitask learning setup when auxiliary task data domain differs from primary task data

**Evidence**: "relying on a separate corpus for the auxiliary task (Collobert and Weston, 2008; Talat et al., 2018) may easily cause domain transfer problems and introduce noise. Preliminary tests confirmed this assumption."

## [NEGATIVE] AdapterFusion
Non-destructive task composition approach for transfer learning using adapters

**Delta**: performed notably worse in preliminary tests
**Condition**: Compared to joint multitask learning for social bias detection with dialect modeling

**Evidence**: "adapter fusion (Pfeiffer et al., 2021) performed notably worse in preliminary tests."

## [POSITIVE] Round-Robin Training for Multitask Learning
Alternating between tasks in a round-robin manner during training, with each task's loss individually backpropagated to the shared encoder

**Delta**: contributes to overall multitask improvements; no isolated delta reported
**Condition**: Multitask learning training procedure for joint bias and dialect detection

**Evidence**: "the used labels alternate between the different dialect and bias aspect tasks in a round-robin manner... the loss for the encoder model is calculated by alternating round-robin between tasks and individually being backpropagated to the encoder."

## [POSITIVE] Modeling Multiple Bias Aspects Jointly (Implicit Label Dependencies)
Training on all five bias aspects simultaneously allows the model to learn interdependencies and avoid impossible label combinations (e.g., intentional but not offensive)

**Delta**: SINGLETASK predicts impossible label combinations 59 times; MULTITASK and MULTITASK+AAE reduce this to 0
**Condition**: Detection of logically dependent bias aspects (offensive/intentional, target group/ingroup)

**Evidence**: "While the SINGLETASK model predicts these impossible combinations for offensive and intentional only 59 times, both multitask learning variants, MULTITASK and MULTITASK+AAE, eliminate the issue and never predict such wrong combinations."

## [POSITIVE] DeBERTa-v3-base as Encoder
Using DeBERTa-v3-base as the shared encoder backbone for all classification tasks

**Delta**: achieves state-of-the-art; DeBERTa-v3-large showed no notable increase in preliminary tests
**Condition**: Both dialect classification and social bias detection tasks

**Evidence**: "We fine-tune DeBERTa-v3-base (He et al., 2023) with a classification head on the TwitterAAE corpus. While bigger models exist, BERT-based text encoders still show state-of-the-art performance in various downstream tasks (He et al., 2023) and remain competitive for text-only classification tasks."

## [POSITIVE] AAE Dialect Modeling Improving Non-Dialect Texts
Adding AAE dialect as auxiliary task also improves performance on non-AAE texts, not just AAE texts

**Delta**: lewdness non-AAE F1 increases from .861 (SINGLETASK) to .869 (SINGLETASK+AAE); target group and ingroup non-AAE also increase
**Condition**: Single-task learning with AAE auxiliary task, for lewdness, target group, and ingroup aspects on non-AAE texts

**Evidence**: "Interestingly, however, SINGLETASK+AAE shows the opposite effect for two aspects: For lewdness, the performance on AAE texts drops from .842 to .836, but increases for non-AAE texts from .861 to .869. Similarly, an increase for non-AAE texts is visible for the target group and ingroup aspects. These results indicate that awareness of dialect language helps improves results for texts written with dialect, but also for those without."

## [NEUTRAL] MULTITASK+AAE Dialect Modeling Trade-off on Non-Dialect Texts
In the multitask setting, adding AAE dialect modeling improves AAE text performance but slightly decreases non-AAE performance

**Delta**: lewdness AAE F1 .846 vs .840 (MULTITASK); lewdness non-AAE F1 .865 vs .870 (MULTITASK)
**Condition**: Multitask learning setting when adding AAE dialect auxiliary task on top of five bias aspect heads

**Evidence**: "Unlike for SINGLETASK+AAE, the gain in performance is only visible for AAE, while often slightly decreases for non-AAE. On lewdness, for example, the score increases significantly from .840 (MULTITASK) to .846 (MULTITASK+AAE) for AAE texts, but decreases from .870 (MULTITASK) to .865 (MULTITASK+AAE) for non-AAE texts."
