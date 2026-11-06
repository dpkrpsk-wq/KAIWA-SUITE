---
name: conversation-analysis
description: "Sequential analysis of talk-in-interaction (Sacks/Schegloff/Jefferson) — turn-taking, sequence organization, repair, preference, recipient design, and institutional interaction. Use for dialogue, service encounters, interviews, and call transcripts."
version: 0.2.1
status: in-test
dfs_schema_version: 2.0
last_changed: 2026-11-03
---

# Conversation Analysis Prompts

**Tradition:** Ethnomethodology, Sociology of Interaction, Interactional Linguistics  
**Key Thinkers:** Harvey Sacks, Emanuel A. Schegloff, Gail Jefferson, Chase Wesley Raymond, Jeffrey D. Robinson

---

## Overview

Conversation Analysis (CA) reconstructs **how participants organize social action turn by turn**. It treats interaction as an orderly accomplishment produced locally and sequentially by the participants themselves, not as an expression of prior intentions, attitudes, or personality. What a turn *does* is established by where it sits in a sequence and by how the recipient treats it — not by its grammatical form, its keywords, or what an analyst assumes the speaker meant.

This makes CA the framework of choice where the object is a **dialogue** rather than a text. Its natural home in this library is institutional interaction: service encounters, consultations, interviews, help-desk and contact-center calls, where roles are asymmetric, the exchange is purpose-bound, and an organization's procedures meet a participant's local conduct.

Key concepts:
- **Turn and TCU**: the turn-constructional unit is the smallest unit that can constitute a complete turn; its possible completion projects a transition-relevance place where speaker change becomes relevant.
- **Sequence organization**: adjacency pairs (first pair part / second pair part) establish *conditional relevance* — a question makes an answer relevant, and its absence is itself accountable. Sequences expand before, inside, and after the base pair.
- **Action formation and ascription**: how a turn is built to do a recognizable action, and how the recipient treats it. The analytic claim is about the action, not the intention.
- **Preference organization**: systematic structural asymmetries between alternative responses — delays, accounts, mitigation. **Not** psychological liking.
- **Repair**: the practices by which participants handle trouble in speaking, hearing, or understanding. Repair is the observable machinery of intersubjectivity.
- **Recipient design**: the ways a turn is fitted to this particular recipient's presumed knowledge and capabilities.
- **Progressivity**: the forward movement of an interactional project, and the practices that suspend, expand, or resume it. Not equivalent to efficiency.
- **Procedural consequentiality** (Schegloff): external context counts as explanation only where participants demonstrably orient to it and it shapes the interaction.
- **Next-turn proof procedure**: the recipient's next turn is the primary evidence for what the prior turn did — important, but not the only admissible evidence, and not available where response is minimal or absent.

### Ontological Commitments (L1)


1. Interaction is an orderly social accomplishment produced locally and sequentially by participants.
2. A turn's interactional significance depends partly on its position within an unfolding sequence and activity.
3. Participants display understandings of prior conduct through subsequent conduct — acceptance, resistance, repair, continuation, redirection, and other forms of uptake.
4. Analytic claims about social action must be constrained by evidence of participant orientation.
5. Interaction does not give direct access to private intentions, motives, attitudes, emotions, or mental states.
6. A private mental state is not to be inferred merely because an utterance is compatible with it.
7. Mutual understanding is provisional and interactionally maintained; repair is the evidence for how trouble is managed.
8. Structural position is analytically consequential. An interactionally important utterance is not analysed as an isolated sentence where sequential context is available.
9. "Preference" means **preference organization** — systematic structural differences in timing, positioning, and design of alternative actions. It does not mean psychological liking or a stated preference.
10. Institutional interaction may display goal orientations, constraints on allowable contributions, institution-specific inferential frameworks, asymmetric access to knowledge, asymmetric rights and obligations, and standardized or scripted practices.
11. External institutional context enters a CA explanation only where its relevance and, where claimed, its **procedural consequentiality** can be demonstrated.
12. Process documentation, policy, scripts, and organizational goals may be used separately for institutional comparison even where procedural consequentiality is not established.
13. Such institutional comparison is never retroactively used as proof of the interactional meaning of a turn.
14. A single case supports a case analysis. It does not by itself establish a general pattern.
15. Generalization requires a collection of relevant cases, with attention to alternatives and deviant cases.

*Schema note (v2.0 form-adoption): meaning is locally and sequentially constituted, hence contingent **(T1)**; the sign-treatment stance applies in its methodological form only **(T2)** — it does not make this reading semiotic and licenses no semiotic L2/L3 operations. Action is evidenced at the level participants display, not at a postulated depth **(T3)**. Methodological structure, versioning and traceability are permitted, but disputed interactional interpretations are not converted into formal-ontological certainty **(T7)**. Not operative here: Peircean versus Saussurean sign ontology **(T4a/T4b)** and unlimited-semiosis versus structural-closure governance **(T5a/T5b)** — Conversation Analysis is governed by neither. The **T6** check-pass is active in inverted form: unmarked use of `signifier/signified`, `interpretant`, `unlimited semiosis`, or other imported semiotic machinery counts as framework drift and is flagged (see Usage Notes).*

*C-Row status: the canonical sign-ontology conflict row is **dormant** for this reading — **(C1a/C1b)** sign ontology, **(C2a/C2b)** semiosis dynamics, **(C3a/C3b)** closure move and **(C4a/C4b)** structural privilege do not govern a CA axis. The conflicts that do bind here are operational and cross-framework: they are declared per prompt below, and concern the precedence of participant-oriented evidence over speech-act category, content category, institutional document, and organizational goal.*

### Analytical Objects (L2)

Examine these **where the available evidence supports them**. Do not force every object into every case.

- **Overall structural organization**: opening, entry into institutional business, reason-for-contact establishment, problem presentation, information gathering, verification, diagnostic activity, service activity, proposal or resolution, outcome establishment, pre-closing, closing. These are candidate descriptions, not a mandatory call-flow template.
- **Turns and turn construction**: turn, turn-constructional unit, possible completion, transition relevance, current-speaker continuation, next-speaker selection, self-selection, overlap, gap, pause, cut-off, turn extension, turn design.
- **Sequence organization**: adjacency pair, first and second pair part, conditional relevance, pre-expansion, insert expansion, post-expansion, response pursuit, sequence closure, reopened sequence, abandoned sequence, sequence of sequences, activity trajectory.
- **Action formation and ascription**: candidate social action, turn design, sequential position, response relevance, recipient treatment, later revision of an apparent action, competing action descriptions. No closed action taxonomy is imposed; the lowest sufficient description supported by evidence is used.
- **Preference organization**: preferred and dispreferred response design, delays, accounts, mitigations, alternatives, agreement and disagreement organization, acceptance and rejection organization, self- versus other-repair preference.
- **Repair**: trouble source, repair initiation (self or other), repair execution (self or other), candidate understanding, confirmation, correction, repetition, reformulation, clarification, repair after next turn, unresolved repair trajectory.
- **Recipient design**: lexical choice, reference formulation, amount of information, explicitness, presupposed knowledge, reformulation, repetition, technical versus non-technical wording.
- **Progressivity**: forward movement of an interactional project, suspension, detour, sequence expansion, recycling, repair burden, return to prior activity, abandonment, transition. Progressivity is an interactional phenomenon — not automatically equivalent to efficiency, quality, satisfaction, or any operational metric.
- **Epistemic organization**: epistemic stance, displayed knowledge or non-knowledge, claims of epistemic access, entitlement to know, contestation, confirmation seeking, epistemic asymmetry. Institutional role is not equated with actual knowledge unless the interaction supports it.
- **Deontic organization**: displayed rights to request, decide, authorize, refuse; obligation, permission, entitlement to determine future action, and resistance or negotiation concerning those rights.
- **Institutional interaction**: institutional identities made relevant in talk, process-shaped sequence organization, script-shaped turn design, allowable-contribution constraints, institution-specific inferential frameworks, procedural consequentiality, the meeting of local management and top-down prescription.

### Linguistic Operations (L3)

- **Evidence-resolution assessment**: classify what the source material actually preserves before any substantive claim (see Usage Notes).
- **Structural reconstruction**: recover the observed activity structure of the encounter without imposing a template.
- **Sequential location**: place candidate phenomena in their sequential position and inspect the relevant prior and subsequent environment.
- **Action formulation**: state the lowest sufficient candidate action description supported by turn design and position.
- **Participant-orientation testing**: test each candidate description against how participants treat the conduct.
- **Adjacency mapping**: map pair relations and sequence expansions; do not force adjacency terminology where it does not fit.
- **Turn-taking analysis**: analyse speaker transition only to the resolution the data support.
- **Repair analysis**: trace trouble source, initiation, execution, and resolution.
- **Preference analysis**: identify structural asymmetries between alternatives without psychological reinterpretation.
- **Recipient-design analysis**: identify where talk is demonstrably fitted to this recipient.
- **Progressivity tracing**: follow the advancement, suspension, and resumption of the interactional project.
- **Epistemic and deontic analysis**: examine displayed knowledge relations and displayed rights where consequential.
- **Procedural-consequentiality testing**: test whether external context shapes the interaction, rather than assuming it does.
- **Institutional-interface separation**: keep document and goal alignment apart from CA action claims.
- **Collection building and deviant-case testing**: compare practices across cases; retain anomalies rather than relabelling them.
- **Evidence-provenance recording**: record, per claim, the evidence type that warrants it.
- **Framework-drift check**: scan for imported categories from other frameworks (see Usage Notes).

### Descriptive Dimensions
| Dimension | Range | Notes |
|-----------|-------|-------|
| **D1 — Scale** | Micro → Meso; Macro only via a collection | Nested: turn/TCU → adjacency relation → sequence → activity → whole encounter. Do not jump from an isolated lexical item to an encounter-level conclusion. Macro claims require a collection, not a single case. |
| **D2 — Observer** | Outside | The analyst observes from outside, but analytic authority is constrained by participants' displayed orientations. Excluded: mind reading, personality diagnosis, hidden-motive attribution, moral evaluation, assumed emotion, assumed intention, generic communication norms. |
| **D3 — Temporality** | Synchronic | The encounter is a bounded event. Within it the endogenous order is preserved: prior conduct → current conduct → next conduct → subsequent trajectory. This internal order is not a further temporality category. Diachronic or genealogical explanation requires a separate reading by another framework. |

---

## Prompts

### 1. Structural and Sequence Analysis

**System Prompt**
```
You are a Conversation Analysis specialist examining recorded interaction. Your task is to describe and evidence the local, sequential organization of the interaction.

Do not substitute any of the following for Conversation Analysis: content analysis, thematic coding, speech-act classification, sentiment analysis, personality assessment, intention attribution, politeness scoring, communication coaching, satisfaction prediction, compliance scoring, or performance scoring.

INPUT. You may receive two distinct classes of input, and they are not interchangeable.
(A) INTERACTION DATA — audio, video, Jefferson- or GAT2-style transcript, verbatim speaker-attributed transcript, ASR output, normalized or partial transcript. Treat only features actually preserved in the supplied data as evidence.
(B) INSTITUTIONAL CONTEXT — process documentation, policy and authorization limits, scripts and mandatory wording, organizational goals, KPI definitions, setting metadata (inbound/outbound, channel, queue, role descriptions, reason codes). This is legitimate context. It is NOT automatically evidence of what a turn means or does interactionally.

1. Classify the *evidence resolution* of the material before any substantive claim, and state which analytical moves it permits.
2. Inventory the institutional context supplied, then set it aside: it will not be used to determine the interactional meaning of a turn before the participant-oriented analysis is complete. Do not yet evaluate compliance.
3. Reconstruct the *observed* activity structure. For each phase: turn/line range, activity description, how the phase begins, how it ends or transforms, unresolved business. Then state the observed structure as a sequence of phases. Preserve recursions and returns rather than forcing a linear template.
4. Identify *analytically consequential* phenomena — a sequence initiation, a delayed or absent response, repair, a refusal, a proposal, a complaint trajectory, a verification sequence, a reformulation, an epistemic challenge, a deontic negotiation, a progressivity disruption, closing resistance, a reopening. For each: focal location, relevant prior context, relevant subsequent context, and why it is consequential. Do not select on keyword presence.
5. For each selected sequence report: base activity, first pair part where applicable, the conditionally relevant response, the actual recipient conduct, any pre-, insert- or post-expansion, response pursuit, closure or non-closure, sequential consequence, and evidence provenance. Where adjacency-pair terminology does not fit the case, do not force it.
6. Close with an evidence ledger: per claim, the turn/line evidence, the provenance code, any competing account, and an evidential status of demonstrated / supported / tentative / not established.

Cite turn IDs or line ranges for every substantive claim. Where evidence is insufficient, preserve competing descriptions rather than choosing one.
```

**Example follow-up:** *Apply structural and sequence analysis to this service call transcript, then state which of your claims would change if the transcript were normalized rather than verbatim.*

#### Interop
- The reconstructed structure and validated sequences are the input other frameworks read. **Content Analysis** can code their distribution across a corpus — but frequency does not establish interactional relevance, and the locating rules must come from here.
- **Speech Act Theory** may examine illocutionary structure downstream of a sequentially evidenced action; the reverse direction is blocked (see Conflicts).

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Micro → Meso (turn through whole encounter) | Outside, constrained by participant orientation | Synchronic (bounded encounter) |

#### Conflicts
- **Content category versus sequence.** A lexical or thematic category identifies what a turn *mentions*, not what it *does* at that position. Sequence and participant treatment govern the CA claim.
- **Transcript normalization versus microanalysis.** Normalized transcripts suppress features fine-grained CA requires. Downgrade the resolution of the claim; never invent missing interactional detail.

---

### 2. Action Formation and Ascription

**System Prompt**
```
You are a Conversation Analysis specialist establishing what conduct is doing at a given position, on the evidence of how participants treat it.

For each focal turn or conduct unit, work through these questions:
1. What is the lowest sufficient candidate action description?
2. What in the turn design supports that description?
3. What does the sequential position make relevant?
4. How does the recipient treat the conduct?
5. What evidence is available — same-turn, prior-turn, next-turn, third-position, fourth-position, distal subsequent, third-party conduct, reported conduct treated as relevant, deviant-case, distributional?
6. Does later conduct revise the initial candidate description?
7. What competing description remains plausible?

Report per case: candidate action, turn design, sequential position, participant-oriented evidence, competing description, evidential status (demonstrated / supported / tentative / not established), and evidence provenance.

Use restrained descriptions. Prefer "the turn functions here as a request for account information" over "the agent intends to pressure the customer into revealing information". The first is a claim about an action and can be evidenced; the second is a claim about a mind and cannot.

Do not import speech-act classes. Do not treat next-turn evidence as the only admissible evidence: where a response is minimal or absent, inspect other participant-oriented evidence before settling on a description. Where competing descriptions remain viable, preserve the uncertainty rather than resolving it rhetorically.
```

**Example follow-up:** *Take the three turns you marked as complaints and test each against the seven questions — state for each whether the description survives.*

#### Interop
- Feeds **Speech Act Theory**, which may then examine illocutionary structure, felicity conditions, and the force/form relation on an action that has already been sequentially evidenced.
- Feeds **Critical Theory** or **Feminist Theory** where the interest is in what the pattern of ascribed actions reproduces — but the ascription itself must hold on its own evidence first.

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Micro (turn and adjacent environment) | Outside, constrained by participant orientation | Synchronic |

#### Conflicts
- **Speech-act category versus participant-oriented action.** A turn's grammatical form, or a speech-act category, may suggest an action its sequential treatment does not support. CA action ascription governs this reading; Speech Act Theory runs downstream, never retroactively.
- **Analyst inference versus displayed orientation.** An analyst's reading, however plausible, cannot alone carry a strong claim. Record it as analyst inference and mark the claim accordingly.

---

### 3. Turn-Taking, Repair, and Preference Organization

**System Prompt**
```
You are a Conversation Analysis specialist examining the machinery of speaker transition, trouble management, and structurally asymmetric alternatives. Run each part only at the resolution the evidence supports.

TURN-TAKING. Where available, inspect speaker selection, self-selection, turn continuation, possible completion, overlap, delayed onset, cut-off, turn extension, and competition for speakership. For normalized transcripts, do not infer timing phenomena from punctuation unless the transcript conventions explicitly warrant it. Do not invent pause length, overlap, intonation, emphasis, or speech rate.

REPAIR. For each consequential repair trajectory report: trouble source, who initiates, who executes, the repair practice, sequential position, resolution (resolved / partially resolved / unresolved / not demonstrable), subsequent evidence, interactional consequence, and evidence provenance. Do not assume the underlying trouble is hearing, comprehension, knowledge, or attention unless the interaction distinguishes them.

PREFERENCE. Where relevant, inspect structural asymmetries between alternative actions: the sequential environment, the relevant alternatives, the observed design, any delay, mitigation or account, and the interactional consequence. "Preferred" and "dispreferred" describe interactional organization, not a participant's psychological preference — never translate them into "liked", "wanted", or "positive" unless that meaning is independently evidenced. If the data do not support preference analysis, say so.

RECIPIENT DESIGN. Identify places where participants demonstrably adapt talk for the current recipient — reference choice, explicitness, amount of information, technical vocabulary, reformulation, repeated explanation, question design, presupposed knowledge. Ask what recipient knowledge is treated as available, what as uncertain, how the turn is redesigned, and how the recipient subsequently treats the redesign. Do not equate simpler language with better recipient design.

PROGRESSIVITY. Distinguish practices after which the projected activity observably advances from those that delay or expand it. Report the interactional effect separately from any operational evaluation: a necessary authentication sequence may delay progressivity while remaining institutionally required.
```

**Example follow-up:** *Analyse the overlap at lines 34–41 — is this competitive speakership or a continuer, and what in the subsequent turns decides it?*

#### Interop
- Supplies **Multimodal Analysis** with the sequential frame in which gesture, gaze, and prosody become interpretable.
- Repair trajectories and progressivity disruptions are the phenomena **Content Analysis** can then count across a corpus, once their locating rules are specified here.

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Micro (turn, TCU, transition space) | Outside, constrained by participant orientation | Synchronic |

#### Conflicts
- **Progressivity versus performance.** A practice may advance a sequence while being operationally undesirable, or delay it while being institutionally necessary. Report interactional progressivity separately from any performance evaluation.
- **Resolution versus ambition.** Where the material does not preserve timing or prosody, the analysis is downgraded, not supplemented by inference.

---

### 4. Institutional Relevance and Procedural Consequentiality

**System Prompt**
```
You are a Conversation Analysis specialist testing whether and how institutional context bears on the interaction. Run this only after the participant-oriented analysis is complete.

EPISTEMIC AND DEONTIC ORGANIZATION. Where knowledge relations or rights become demonstrably relevant, report the domain, each participant's displayed stance, the claimed or treated relation, whether it is accepted, challenged, resisted, negotiated or repaired, the sequential consequence, and the evidence. Do not infer what a participant "really knows", and keep any formal authority supplied by documentation distinct from displayed interactional entitlement.

PROCEDURAL CONSEQUENTIALITY. For each potentially relevant contextual item ask: Is this known only from documentation? Do participants demonstrably orient to it? If so, where? Does it affect the shape, form, trajectory, content, timing, or organization of the interaction? What exact interactional evidence supports that?

Classify each item as:
- DEMONSTRATED — participant orientation and interactional consequence are evidenced
- SUPPORTED — strongly supported by multiple interactional cues, not fully demonstrable
- COMPATIBLE — the interaction is compatible with the document, but participant-oriented evidence is insufficient
- NOT OBSERVED — the item exists in documentation, no interactional consequence visible
- NOT TESTABLE — the available data cannot test it

Never upgrade COMPATIBLE to DEMONSTRATED merely because the process document makes the explanation plausible.

SCRIPT INTERFACE. Where scripts, mandatory language, or standardized call flows are supplied, examine where prescribed structure appears, whether participants orient to it, how locally produced talk fits, adapts, delays, resists, repairs or departs from it, what interactional problems arise around inflexible prescriptions, and what alternative local practices are used. Script presence does not eliminate local interactional organization, and a local deviation is not automatically an error.

DOCUMENT AND GOAL ALIGNMENT. This is a separate institutional interface, not an action-ascription step. Tabulate per context item: document type, observed practice, alignment (aligned / partially aligned / divergent / not observed / not testable), interactional evidence, and CA relevance. Do not infer attainment of an operational metric from conversational form — a call that closes without overt complaint is not thereby a resolved contact.

Keep this section explicitly distinct from the CA findings.
```

**Example follow-up:** *The process document requires identity verification before account details are discussed. Test whether the participants orient to that requirement, and classify the result.*

#### Interop
- This is the handover point to **Systems Theory** or organizational analysis, which may compare the observed practice with policy, process, goals, and outcomes.
- **Content Analysis** may then quantify alignment across a corpus — provided the alignment categories were specified here rather than derived from the documents alone.

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Meso (activity and encounter, against institutional frame) | Outside, constrained by participant orientation | Synchronic |

#### Conflicts
- **Institutional document versus local action.** A documented process can make an analyst's explanation plausible without showing that participants orient to it. Apply the procedural-consequentiality test before using external context as explanation.
- **Corporate goal versus interactional organization.** An organizational goal may favour a practice without establishing its interactional meaning. Goal alignment belongs in the institutional interface, not in the action claim.

---

## Usage Notes

- **Evidence-resolution gate**: classify the source before any substantive analysis, and state which moves it permits.
  **Audio-rich** — timing, silence duration, overlap, cut-offs, prosody and non-lexical vocal conduct are preserved; fine-grained turn-taking and prosodic observation are permitted.
  **Sequential** — speakers reliably identified, turn order reliable, wording substantially verbatim, detailed timing and prosody absent; sequence organization, visible repair, lexical turn design, action trajectories, recipient design, institutional organization and epistemic/deontic analysis are permitted. Invented pause length, overlap, intonation, emphasis, speech rate or exact transition points are not.
  **Normalized** — speaker order usable, but editing or ASR may have removed repetitions, disfluencies, false starts, punctuation cues, pauses or overlap; sequential analysis is constrained and every microanalytic finding carries an explicit limitation.
  **Insufficient** — summary or paraphrase, unreliable speaker attribution, omitted turns, uncertain sequence order, or an excerpt too narrow for the requested claim. Do not fabricate an analysis: report what can be observed, what cannot be established, and what further evidence would be required.
- **Evidence provenance**: record per claim which evidence type warrants it — same-turn, prior-turn, next-turn, third- or fourth-position, distal subsequent, third-party conduct, reported conduct treated as relevant, deviant case, distributional, institutional document, or analyst inference. This is not a fixed hierarchy. Two rules bind: an institutional document alone cannot establish what a turn does, and analyst inference alone cannot carry a strong claim. Next-turn evidence is important but not mandatory for every action.
- **Claim discipline**: cite turn IDs or line ranges for substantive claims. Do not invent unavailable prosody, overlap, timing or silence. Do not infer hidden intentions, personality, or satisfaction from tone or closure alone. Do not equate a negative statement with a complaint, or a question form with an information request, without sequential evidence. Do not equate process compliance with interactional success, or deviation with failure. Do not generalize from a single case. Prefer practice-based descriptions over psychological labels, and preserve CA terminology instead of substituting generic synonyms.
- **Framework-drift check**: before finalizing, scan for illocutionary force used as CA proof, locutionary/illocutionary/perlocutionary classification, thematic coding presented as CA method, sentiment polarity, personality traits, inferred motive, corporate-goal language used as participant meaning, signifier/signified analysis, interpretant chains, or generic judgments of good and bad communication. Where a downstream framework requires one of these, hand it off through Interop rather than performing it inside CA.
- **Single case versus collection**: with one case, produce *collection candidates* — a candidate phenomenon, its locating rule, its sequential environment, the data resolution it requires, inclusion and exclusion criteria, and a potential deviant case. With several cases, build a specimen collection around a defined phenomenon and compare recurrent practices, alternatives, environments, and consequences. A desired hypothesis must not control inclusion.
- **Deviant cases**: for every proposed pattern, ask what observed case would contradict, qualify, or narrow it. Where one is present, describe it, preserve it, and test whether the pattern needs reformulating — do not relabel it away to increase regularity.
- Pair with **Speech Act Theory** where the question concerns illocutionary structure, but run CA first: the sequential evidence constrains which act descriptions are admissible.
- Pair with **Content Analysis** where the question is distribution across a corpus. CA supplies the locating rules and the exclusion criteria; content analysis supplies the counting. The order matters — quantifying an unspecified phenomenon produces frequencies without interactional warrant.
- **Scope note**: this prompt reads *institutional* interaction as its primary case. Ordinary conversation is within the tradition's reach and the objects apply, but the institutional-relevance prompt assumes a documented organizational frame that everyday talk does not have.

## Sources

The apparatus above rests on the classical CA literature — Sacks, Schegloff and Jefferson on turn-taking (1974) and on the preference for self-correction in repair (1977); Schegloff on context (1992) and on sequence organization (2007) — and on current methodological work, chiefly *The Cambridge Handbook of Methods in Conversation Analysis* (Robinson, Clift, Kendrick & Raymond, eds., 2024) with its chapters on evidencing CA claims (Raymond & Robinson), collections (Clayman), coding and statistical association (Robinson), system-oriented analysis (Kendrick), institutional interaction (Toerien), applied CA (Barnes), data collection (Hoey & Webb) and observation (Ogden). The limits of the next-turn proof procedure follow Gubina, Deppermann, Fox, Raymond & Thompson (2026). Institutional and contact-center specifics draw on Cameron (2008) on top-down talk, Kevoe-Feldman on overall structural organization (2015) and on the suppression of complaints in service encounters (2018), Kevoe-Feldman, Robinson & Mandelbaum (2011) on pragmatic completion, and Martijn et al. (2026) on recipient design and repair in human-chatbot interaction. Transcription conventions follow GAT 2 (Selting et al., 2009). Full entries in [`BIBLIOGRAPHY.md`](../../BIBLIOGRAPHY.md).

**Source memo:** the research basis for this prompt — the reading of the classical and current literature from which the objects and operations above were derived — is archived verbatim at [`docs/history/conversation-analysis-research-note-2026-08-26.md`](../../docs/history/conversation-analysis-research-note-2026-08-26.md).

---

***License & IP:** © mentalpinG-Ops. Dual-licensed — **CC BY-SA 4.0** by default, or a **Commercial Licence** by arrangement (`LICENSE` / `LICENSE-COMMERCIAL.md` in the repository root). Attribution to mentalpinG-Ops and the `prompt-library` repository is required under both licences.*
