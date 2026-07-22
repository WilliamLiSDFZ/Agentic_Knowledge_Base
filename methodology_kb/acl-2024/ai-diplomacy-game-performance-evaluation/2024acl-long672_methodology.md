# More Victories, Less Cooperation: Assessing Cicero’s Diplomacy Play

**Source**: https://aclanthology.org/2024.acl-long.672/

## [POSITIVE] Domain-specific AMR Fine-tuning
Fine-tuning a sequence-to-sequence AMR parser on a Diplomacy-specific AMR corpus instead of using the general AMR 3.0 dataset

**Delta**: +39.1 SMATCH (from 22.8 to 61.9)
**Condition**: AMR parsing of Diplomacy game communications

**Evidence**: "Our domain-tuned model using Diplomacy-AMR improves SMATCH by 39.1, to 61.9."

## [POSITIVE] Data Augmentation with Contextual Information
Adding contextual information to dialogues (e.g., knowing the sender is England and the recipient is Germany) to aid the model's understanding of pronouns and strategic details

**Delta**: +2.7 SMATCH (from 61.9 to 64.6)
**Condition**: AMR parsing of Diplomacy game communications

**Evidence**: "Adding data augmentation into the model (e.g., knowing the sender of a message is England and the recipient is Germany) improves SMATCH to 64.6."

## [POSITIVE] Separate Encodings for Sender/Recipient Identity
Incorporating specific tokens for sender and recipient identities as separate encodings in the model

**Delta**: +0.8 SMATCH (from 64.6 to 65.4)
**Condition**: AMR parsing of Diplomacy game communications

**Evidence**: "Adding separate encodings for this information further improves SMATCH by 0.8 (65.4)."

## [POSITIVE] Pronoun and Abbreviation Replacement
Data processing to replace (1) pronouns with country names and (2) province abbreviations with full names

**Delta**: +1.2 SMATCH (from 65.4 to 66.6)
**Condition**: AMR parsing of Diplomacy game communications

**Evidence**: "Additionally, we apply data processing to replace (1) pronouns with country names and (2) provinces in abbreviations with full names, which increases SMATCH to 66.6."

## [NEUTRAL] Natural Language Communication in Cicero vs. Cicero Games
Allowing Cicero agents to use full natural language communication when playing against other Cicero agents

**Delta**: Expected +0.2 additional supply centers (-0.5 to 0.9 95% interval) vs. best communication strategy
**Condition**: Cicero vs. Cicero games measuring supply center gains

**Evidence**: "the best language condition AMR only yielded an expected 0.2 additional supply centers (-0.5–0.9 95% interval). In other words, the effect of choosing the best power over the median power is 14 times larger than the best communication strategy."

## [NEUTRAL] AMR-only Communication Level
Restricting Cicero agents to only pass through messages about game actions parsed by AMR, allowing coordination of game actions without full natural language

**Delta**: Best communication condition; only +0.2 supply centers vs. random messages baseline
**Condition**: Cicero vs. Cicero games; communication level comparison

**Evidence**: "the best language condition AMR only yielded an expected 0.2 additional supply centers (-0.5–0.9 95% interval)."

## [NEUTRAL] Random Message Communication
Sending random messages from a corpus of previous Diplomacy games, mimicking form without content

**Delta**: Used as baseline; negligible difference from AMR or Natural Language conditions
**Condition**: Cicero vs. Cicero games; communication level comparison

**Evidence**: "the effect of choosing the best power over the median power is 14 times larger than the best communication strategy. This is consistent with prior findings... that Cicero's communicative ability plays no clear role in its win rate."

## [POSITIVE] Power Assignment in Diplomacy
The specific nation/power a Cicero agent is assigned to play (e.g., France vs. Russia)

**Delta**: +2.8 supply centers for France vs. median power Russia (2.0–3.6 95% interval); 14x larger effect than best communication strategy
**Condition**: Cicero vs. Cicero games measuring supply center gains

**Evidence**: "Playing as France (FRA) yields an expected 2.8 additional supply centers (2.0–3.6 95% interval) compared to the median power Russia (RUS)... the effect of choosing the best power over the median power is 14 times larger than the best communication strategy."

## [POSITIVE] Cicero's Strategic AI vs. Human Players
Cicero's underlying strategic model playing against human players in full Human-Cicero games

**Delta**: Cicero won 20 out of 24 games (84%); more supply centers than humans across most power assignments
**Condition**: Human-Cicero games across 24 games

**Evidence**: "Of twenty-four games, Cicero won twenty (84%), which strongly suggests that Cicero has super-human strategy. On average, Cicero has more supply centers than human players by the end of the game."

## [NEGATIVE] Cicero's Natural Language Communication with Humans
Cicero using its full natural language generation capability to communicate with human players

**Delta**: Humans identify Cicero with F1=0.81 by game end; Cicero persuasion success rate only 10.9% vs. humans' 21.1%; Cicero broken commitment rate lower but perceived as lying more (14.4% vs. 7.1%)
**Condition**: Human-Cicero games evaluating communicative effectiveness

**Evidence**: "Cicero plays 'differently'; humans can reliably identify Cicero and it is less deceptive and persuasive to human players. Communication from Cicero is more transactional, relying on its optimal strategy rather than the alliance building which is the hallmark of top human players."

## [NEGATIVE] Prior Exposure to Cicero (Returning Players)
Human players who have previously played against Cicero at least once are better at identifying it as an AI

**Delta**: Returning players achieve higher F1 scores for bot identification than first-time players throughout the game
**Condition**: Human identification of Cicero in Human-Cicero games

**Evidence**: "Players who previously played against Cicero at least once are better at identifying it. This suggests that Cicero can no longer pass as human once humans are aware of the possible existence of such agents."

## [NEUTRAL] Human Lie Annotation of Incoming Messages
Asking human players to annotate each incoming message as truthful or deceptive during gameplay

**Delta**: Humans perceive 14.4% of Cicero messages as lies vs. 7.1% of human messages; but humans correctly identify only 0.2% of actual lies in Human-Human messages
**Condition**: Human-Cicero games; lie perception vs. actual lie detection

**Evidence**: "Humans perceive 14.4% of the 6,960 messages they receive from Cicero as lies... In contrast, they perceive only 7.1% of the messages from other humans as lies... humans can correctly identify five lies (0.2%), suggesting a small overlap between actual lies and perceived lies."

## [NEUTRAL] Broken Commitment Detection via AMR
Automatically detecting broken commitments by comparing AMR-parsed communicative intent to final submitted orders

**Delta**: Precision 0.51, Recall 0.71
**Condition**: Automatic deception detection in Diplomacy game messages

**Evidence**: "Broken commitment detection has a precision of 0.51 and a recall of 0.71. Our precision is lower than our expectation due to errors in parsing a complex English to AMR and a definition that only detects commitments at a move level."

## [POSITIVE] Persuasion Detection via AMR
Automatically detecting persuasion by comparing initial intents to communicative suggestions and final orders

**Delta**: Precision 0.81, Recall 0.72
**Condition**: Automatic persuasion detection in Diplomacy game messages

**Evidence**: "Accuracy for persuasion is better; precision rises to 0.81, and recall to 0.72."

## [POSITIVE] Extended AMR Vocabulary for Diplomacy
Extending the standard AMR vocabulary with Diplomacy-specific concepts (e.g., betray-01, threaten-01, demilitarize) and roles beyond DAIDE predicates

**Delta**: Enables coverage of communicative intents not expressible in DAIDE; contributes to overall SMATCH improvement
**Condition**: AMR annotation and parsing of Diplomacy game communications

**Evidence**: "we extend the AMR vocabulary to include not only abbreviations, such as 'SWE' for Sweden, but also verbs like 'threaten' and 'demilitarize'... AMR covers more Diplomacy content than DAIDE, not only due to additional concepts such as betray-01, but also because arguments are syntactically optional."

## [NEUTRAL] Partial/Empty AMR Annotation for Non-Strategic Utterances
Annotating non-game-relevant utterances as empty AMRs rather than forcing full annotation, focusing annotation effort on strategically relevant content

**Delta**: 4,412 out of 8,878 utterances annotated as empty AMRs
**Condition**: AMR annotation of Diplomacy game messages

**Evidence**: "4,412 of those utterances are annotated as empty AMRs (e.g. for 'Lemme think about your idea') indicating no in-game move intent."

## [POSITIVE] Increasing Training Epochs for AMR Parser
Increasing the number of fine-tuning epochs from 16 to 32 when training the Diplomacy AMR parser

**Delta**: Part of overall improvement pipeline; specific isolated delta not reported
**Condition**: Fine-tuning the sequence-to-sequence AMR parser on Diplomacy-AMR corpus

**Evidence**: "used similar parameters except for increasing the number of epochs from 16 to 32."
