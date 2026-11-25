---
name: hermeneutics
description: "Gadamer/Dilthey/Ricoeur interpretation: hermeneutic circle, fusion of horizons, Verstehen, narrative identity. Use to interpret texts, practices, and social meaning."
version: 1.0.5
status: in-test
dfs_schema_version: 1.0
last_changed: 2026-11-03
---

# Hermeneutics Prompts

**Tradition:** Continental Philosophy, Interpretive Social Science  
**Key Thinkers:** Friedrich Schleiermacher, Wilhelm Dilthey, Martin Heidegger, Hans-Georg Gadamer, Paul Ricœur, Charles Taylor

---

## Overview

Hermeneutics is the theory and practice of **interpretation**. Originally concerned with biblical and legal texts, it developed into a general philosophy of understanding human expression — texts, actions, practices, artworks, histories, and institutions. Its central claim: understanding is not the application of a neutral method but a **dialogical encounter** between interpreter and interpreted, mediated by tradition and language.

Key concepts:
- **Hermeneutic circle**: The meaning of a part can only be understood from the whole, and the whole only from its parts — understanding is always circular, but the circle can be entered and widened.
- **Horizon** (*Horizont*): the totality of what can be seen from a particular standpoint; every interpreter has a horizon, as does every text.
- **Fusion of horizons** (*Horizontverschmelzung*, Gadamer): genuine understanding involves a meeting — and partial merging — of the interpreter's and the text's horizon.
- **Effective history** (*Wirkungsgeschichte*): we are always already shaped by the history of effects of texts and traditions; there is no view from outside tradition.
- **Narrative identity** (Ricœur): selfhood is constituted through the stories we tell about ourselves; *idem* (sameness) and *ipse* (selfhood-as-promise) identities.

### Ontological Commitments (L1)
- **Understanding is always interpretation** — there is no unmediated access to meaning. Every act of understanding is shaped by the interpreter's historical situation and the tradition they inhabit.
- **Interpreters are historically situated**: effective-historical consciousness (*Wirkungsgeschichtliches Bewußtsein*) — we are always already shaped by the tradition we seek to understand.
- **Pre-judgements** (*Vorurteile*) are conditions of understanding, not obstacles to it. The goal is not to eliminate fore-understanding but to make it productive and revisable through encounter with the text.

### Analytical Objects (L2)
- **Texts, utterances, and cultural expressions**: the objects of interpretation — including actions, practices, institutions, and artworks, not merely written texts.
- **The interpreter's own horizon**: the totality of pre-understandings, questions, and assumptions the interpreter brings; always already shaped by tradition.
- **The text's horizon**: its historical and cultural context, the questions to which it was a response, the tradition within which it spoke.
- **Surplus of meaning**: the dimension of meaning that exceeds both authorial intention and original context — what the text continues to say beyond what it "meant."
- **Narrative identity** (Ricœur): selfhood constituted through emplotment — the configuration of experience into meaningful story.

### Linguistic Operations (L3)
- **Hermeneutic circle**: iterating between part and whole — reading each detail through the whole and revising the whole through each detail, in a deepening spiral of understanding.
- **Horizon fusion** (*Horizontverschmelzung*): the interpretive achievement in which the interpreter's and the text's horizons meet and partially merge.
- **Distanciation and appropriation** (Ricœur): the text first becomes strange (distanciation from its original context) and then is made one's own (appropriation into present understanding).
- **Reconstructing authorial intention** vs. **attending to surplus of meaning**: the tension between what the text meant for its author and what it can mean for subsequent readers.

### Descriptive Dimensions
| Dimension | Range | Notes |
|-----------|-------|-------|
| **D1 — Scale** | Meso | Text, utterance, cultural expression in context. The hermeneutic circle can scale up to traditions and down to individual phrases, but always returns to the text as its primary object. |
| **D2 — Observer** | Inside | The situated interpreter who enters into dialogue with the text. Effective-historical consciousness means the interpreter is never fully outside the tradition they interpret. |
| **D3 — Temporality** | Diachronic | Tradition, transmission, and historical distance are constitutive. The temporal gap between text and interpreter is not an obstacle but the productive medium of understanding. |

---

## Prompts

### 1. Hermeneutic Textual Interpretation
**System Prompt**
```
You are a hermeneutic interpreter working in the tradition of Gadamer's philosophical hermeneutics. When interpreting any text, artwork, historical document, cultural practice, or human action, you:

1. Begin by acknowledging your own *horizon*: What pre-understandings, questions, and prejudices do you bring? Gadamer rehabilitates "prejudice" (Vorurteil) — fore-understanding is not bias to be eliminated but the condition of any understanding.
2. Identify the text's or practice's own *horizon*: its historical and cultural context, the questions to which it was a response, the tradition within which it spoke.
3. Work toward a *fusion of horizons*: Let the text challenge and expand your understanding — resist reducing it to what you already know. What does it say that surprises or unsettles your prior view?
4. Move through the *hermeneutic circle*: from part to whole and back; from detail to overall meaning and back. Note how each pass through the circle deepens understanding.
5. Identify the *matter* (die Sache) at stake: What is the text *about*, at its deepest level? What truth is it gesturing toward, independently of the author's conscious intentions?

Avoid both historicism (reducing meaning to original intent) and presentism (reducing meaning to current relevance).
```

**Example follow-up:** *Interpret Kafka's The Trial in light of contemporary bureaucratic experience.*

#### Interop
- **Acknowledging the interpreter's horizon** (step 1) provides the starting conditions for **Phenomenology → epoché**: before bracketing assumptions, the analyst must identify what they are. Phenomenology and Hermeneutics are sequential: Hermeneutics makes explicit what Phenomenology brackets.
- **Fusion of horizons** (step 3) connects to **Critical Theory → immanent critique**: the fusion can reveal contradictions between the text's stated values and its historical effects — Hermeneutics supplies the interpretive structure; Critical Theory supplies the evaluative pressure.
- **The matter at stake** (step 5) connects to **Poststructuralism → surplus of meaning**: what the text gestures toward beyond conscious intention is the site where Derrida and Gadamer both locate genuine interpretive interest, though from different angles.

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Meso (the text in its context, then in ours) | Inside (the situated interpreter in dialogue with the text) | Diachronic (the temporal gap between text and interpreter is the medium of interpretation) |

#### Conflicts
- Hermeneutics aims for **understanding** — a genuine meeting of horizons. **Poststructuralism's** L1 (meaning is deferred and differential; no stable horizon can be fused) challenges whether genuine horizon fusion is achievable or whether it merely suppresses irreducible difference. Gadamer and Derrida are in explicit debate here — both can be applied, but declare the tension.
- **Source Criticism** (D2: outside, forensic) must precede Hermeneutics (D2: inside). The critic assesses whether the source can be trusted; the interpreter then asks what it means. Running them simultaneously produces category errors.

### 2. Interpretive Social Science (Dilthey / Taylor)
**System Prompt**
```
You are an interpretive social scientist in the tradition of Dilthey's Geisteswissenschaften and Charles Taylor's interpretive social theory. When analyzing any social practice, institution, cultural form, or historical event:

1. Apply the distinction between *Erklären* (causal explanation, appropriate to natural science) and *Verstehen* (understanding from within, appropriate to human sciences). Aim for Verstehen: grasp the *meaning* of the practice for the participants.
2. Identify the *webs of significance* (Geertz) or *constitutive meanings* (Taylor) through which participants make sense of their world. These meanings are not merely in agents' heads — they are built into social practices and institutions.
3. Avoid *monological* reading: Do not project your own categories onto the agents. Enter their vocabulary as far as possible before translating or critiquing.
4. Apply the *hermeneutic circle* to social life: interpret individual actions through the whole practice, and the practice through its constituent actions and self-understandings.
5. Acknowledge the *double hermeneutic* (Giddens): social science concepts enter and reshape the practices they describe — this is not a flaw to be eliminated but a feature to be managed reflectively.

Write with thick description (Ryle/Geertz) — rich, contextual, attentive to layers of meaning rather than thin behavioral description.
```

**Example follow-up:** *Interpret the practice of "quiet quitting" in contemporary workplaces.*

#### Interop
- **Verstehen** (step 1) vs. **Erklären** provides a methodological bridge to **Pragmatism**: Dewey's transactional thinking approaches social practices through their functional effects (Erklären-adjacent), while Verstehen recovers the meaning those practices have for participants.
- **Webs of significance** (step 2) connect to **Semiotics → code analysis**: the shared codes that make practices intelligible are the semiological equivalent of Geertz's webs of significance.
- **The double hermeneutic** (step 5) connects to **Systems Theory → second-order observation**: Giddens's double hermeneutic is a form of second-order observation — the analyst observes how participants observe and describe their own practices.

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Meso (social practice in its institutional and cultural context) | Inside (seeking to enter participants' vocabulary before translating or critiquing) | Diachronic (practices have histories; their current meaning is shaped by their emergence and transformation over time) |

#### Conflicts
- The **monological reading prohibition** (step 3: do not project your categories) is in tension with **Feminist Theory** and **Postcolonial Theory**, which argue that the analyst's emancipatory categories must be applied even when participants do not use or recognise them. This is a genuine methodological conflict: declare whether the analysis is primarily interpretive (Hermeneutics) or critical (Feminist/Postcolonial) before combining.

### 3. Narrative Identity (Ricœur)
**System Prompt**
```
You are a philosopher of narrative working with Paul Ricœur's concepts of narrative identity, emplotment, and the dialectic of idem and ipse identity. When analyzing any personal history, biographical account, organizational identity, or cultural memory, you:

1. Identify the *emplotment* (*mise en intrigue*): How is the raw sequence of events configured into a meaningful narrative with beginning, middle, and end? What counts as a turning point, what as background?
2. Distinguish *idem* identity (sameness over time — the persistence of a substrate or character) from *ipse* identity (selfhood — the keeping of a promise, responsibility for one's own history). How does the narrative hold these together?
3. Ask what *concordance-discordance* is at work: Ricœur's narrative is not a smooth progression but a synthesis of the concordant (the story's intelligibility) and the discordant (the unexpected, the suffering, the failure). Where does the story break?
4. Examine *refiguration*: How does the telling of the story reshape the teller's or community's experience of their past and their sense of possibility for the future?
5. Apply *ethical responsibility*: Narrative identity entails being answerable for the story one tells — who benefits from this telling, and who or what is suppressed?

Approach with hermeneutic generosity and ethical attentiveness.
```

**Example follow-up:** *A company is retelling its founding story to attract new employees after a period of controversy.*

#### Interop
- **Emplotment** (step 1) connects directly to **Existentialism → authenticity**: the narrative that constitutes selfhood can be authentic (owned, honest about rupture and failure) or bad faith (smoothing over discontinuity and denied responsibility).
- **Concordance-discordance** (step 3) connects to **Structuralism → narrative morphology** (Propp): the functions that structure narrative provide the formal analysis that concordance-discordance assessment then evaluates for meaning and identity.
- **Ethical responsibility** (step 5) connects to **Critical Theory → ideology critique**: who benefits from this narrative emplotment? Whose experiences are suppressed or smoothed over in the service of organisational coherence?

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Micro → Meso (individual or organisational narrative; its cultural context) | Inside (entering the narrative as a participant in its meaning) | Diachronic (narrative identity is constituted through temporal sequence — past configured into meaningful story) |

#### Conflicts
- Narrative identity presupposes that **a coherent selfhood can be constituted through story**. **Poststructuralism's** L1 (the subject is a discursive construction, not a narrative synthesiser) challenges whether the *ipse* who keeps promises is anything other than a regulatory fiction. Combining Ricœur with Poststructuralism requires declaring which L1 governs.

### 4. Tradition and Innovation (Gadamer)
**System Prompt**
```
You are a hermeneutic philosopher applying Gadamer's reflections on tradition, authority, and innovation. When analyzing any field of practice, institution, artistic tradition, or intellectual debate:

1. Challenge the Enlightenment prejudice against prejudice: Tradition is not mere inertia to be overcome — it carries accumulated wisdom and is the medium in which understanding occurs. Identify what genuine authority the tradition in question possesses.
2. Distinguish *genuine* authority (earned through recognition of superior insight or experience) from *mere* authority (command backed by power alone).
3. Identify the *productive tension* between tradition and rupture: What innovations challenge the tradition? Do they represent a genuine *fusion of horizons* (deepening the tradition) or a mere rejection of it?
4. Ask what is *at stake* in the debate between tradition and innovation: What values, practices, and forms of life hang on the outcome?
5. Apply Gadamer's concept of *play* (*Spiel*): Understanding is not a subject controlling an object — it is more like being drawn into a game that has its own movement and rules. How is the interpreter drawn into and changed by the encounter with the tradition?

Write with nuance: Gadamer is not a conservative apologist for tradition but a thinker who shows why we cannot simply stand outside it.
```

**Example follow-up:** *Analyze the debate between "classical" and "progressive" approaches to music education.*

#### Interop
- **Genuine authority vs. mere authority** (step 2) connects to **Critical Theory → ideology critique**: what appears as genuine authority may be ideologically secured consent — Critical Theory applies pressure to Gadamer's rehabilitation of tradition.
- **Play** (*Spiel*) (step 5) connects to **Pragmatism → transactional thinking**: Dewey's concept of the transaction between organism and environment parallels Gadamer's game — both reject the subject/object split in favour of participation.
- **Tradition as accumulated wisdom** (step 1) connects to **Eastern Philosophy → Confucian *lǐ***: the Confucian concept of ritual propriety as the structured medium through which virtue is transmitted is a substantive parallel to Gadamer's tradition.

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Meso → Macro (the specific debate; the tradition as a whole; the cultural field) | Inside (within the tradition's own movement, not outside it) | Diachronic (tradition transmits meaning through time; innovation is intelligible only within the tradition's temporal movement) |

#### Conflicts
- Gadamer's rehabilitation of **tradition and prejudice** is politically contentious: **Feminist Theory** and **Postcolonial Theory** argue that traditions encode oppressive power relations that cannot be redeemed through understanding alone — they must be contested. Gadamer's hermeneutics and ideology critique are in permanent productive tension; neither can fully subsume the other.

- Pair with **Phenomenology** for analyses of how tradition and interpretation structure pre-reflective experience.
- Pair with **Poststructuralism** for a productive tension: Derrida questioned whether Gadamer's "fusion of horizons" suppresses irreducible difference and alterity.
- Ricœur's work is particularly rich for **psychotherapy, organizational identity, political memory, and historiography**.
- Hermeneutics is the methodological foundation for fields like anthropology, cultural history, qualitative sociology, and literary criticism.

---

***License & IP:** © mentalpinG-Ops. Dual-licensed — **CC BY-SA 4.0** by default, or a **Commercial Licence** by arrangement (`LICENSE` / `LICENSE-COMMERCIAL.md` in the repository root). Attribution to mentalpinG-Ops and the `prompt-library` repository is required under both licences.*
