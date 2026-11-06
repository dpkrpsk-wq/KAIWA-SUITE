---
name: structuralism
description: "Analyzes deep structures and systems of difference via Levi-Strauss myth, Propp narrative morphology, binary-opposition mapping, and Althusser ISA prompts. Use for myths, narratives, discourse, institutions."
version: 1.1.2
status: in-test
dfs_schema_version: 2.0
last_changed: 2026-11-03
---

# Structuralism Prompts

**Tradition:** Linguistics, Anthropology, Literary Theory  
**Key Thinkers:** Ferdinand de Saussure, Claude Lévi-Strauss, Vladimir Propp, Roland Barthes (early), Louis Althusser, Roman Jakobson

---

## Overview

Structuralism holds that cultural phenomena are best understood not in isolation but as elements within **systems of differences**. Following Saussure's linguistics — where signs have no intrinsic meaning but only meaning through their differences from other signs — structuralists sought the underlying systems (*structures*) that generate the surface variety of myths, kinship systems, narratives, and ideologies.

Key concepts:
- **Langue / parole**: the underlying language system (langue) vs. individual speech acts (parole).
- **Signifier / signified**: the sound-image vs. the concept it denotes; their relation is *arbitrary*.
- **Binary oppositions**: structures operate through pairs of opposites (raw/cooked, nature/culture, sacred/profane).
- **Deep structure**: the invariant pattern beneath surface variation (Lévi-Strauss's mythemes, Propp's narrative functions).
- **Myth** (Lévi-Strauss): myths resolve — or rather mask the irresolvability of — fundamental cultural contradictions.

### Ontological Commitments (L1)
- **Meaning arises from relations within a system**, not from individual terms: a sign's meaning is purely differential — it is what other signs are not. **(T1; communicative phenomena treated methodologically as signs, T2)**
- **Deep structures underlie surface phenomena**: beneath the diversity of myths, narratives, and cultural practices lie invariant structural patterns that generate surface variation. **(T5a / T5b — the structural-determination pole)**
- The **system** (*langue*) has priority over individual use (*parole*): structure is not built up from instances; instances are expressions of an underlying system. **(T5b — operates under structural-closure governance)**

*Schema note (v2.0 form-adoption): Structuralism occupies the **structural-closure pole of T5**; in cross-framework composition it governs as the structurally-determined-meaning side of **C2**. Saussurean-derivative lineage → **T4b dormant** (only one sign-ontology active; activation trigger = introducing a Peircean component, per T4-IN-1). Single-framework readings do **not** trigger the **T6-IN-1** Retained/Transformed/Lost audit row (required only for multi-framework compositions under one governance).*

### Analytical Objects (L2)
- **Binary oppositions**: the fundamental pairs through which structural meaning is organised (raw/cooked, nature/culture, sacred/profane, self/other).
- **Paradigmatic and syntagmatic relations**: the axis of substitution (what could replace this element?) and the axis of combination (how do elements follow each other in sequence?).
- **Mythemes** (Lévi-Strauss): the minimal relational units of myth — brief statements that gain meaning only through their relations with other mythemes.
- **Narrative functions** (Propp): the 31 invariant functions that structure the morphology of the folktale, independent of the specific characters or settings.
- **Deep structure**: the invariant underlying pattern — the code that generates surface variation.

### Linguistic Operations (L3)
- **Segmentation**: breaking a text, practice, or myth into its minimal constituent units.
- **Commutation test**: substituting one element for another to determine whether the substitution changes the meaning — identifying which distinctions are structurally relevant.
- **Opposition mapping**: identifying the fundamental binary pairs that organise the material and tracing the values clustered around each pole.
- **Reconstructing the underlying code**: moving from surface elements to the deep structural pattern — from *parole* to *langue*.
- **Narrative function analysis**: mapping the sequence of narrative functions against Propp's morphological template.

### Descriptive Dimensions
| Dimension | Range | Notes |
|-----------|-------|-------|
| **D1 — Scale** | Micro → Meso | Minimal unit (micro), system of relations within a text or corpus (meso). The macro is the system (*langue*) that generates all instances. |
| **D2 — Observer** | Outside | Detached, structural, third-person. The analyst maps the system from a position outside the participant's perspective. |
| **D3 — Temporality** | Synchronic | The system at a single moment — the cross-section of relations. Diachronic change (*langue* evolving over time) exists but is not the primary focus of structuralist analysis. |

---

## Prompts

### 1. Structural Analysis of Myth (Lévi-Strauss)
**System Prompt**
```
You are a structural anthropologist working in the tradition of Claude Lévi-Strauss. When analyzing any myth, folktale, cultural narrative, religious story, or founding legend:

1. Identify the *mythemes*: the constituent units of the myth — brief relational statements (e.g., "Oedipus kills his father," "Antigone buries her brother") that gain meaning not individually but through their relations with other mythemes.
2. Arrange the mythemes in two axes:
   - *Horizontal* (syntagmatic): the sequence of the narrative as told.
   - *Vertical* (paradigmatic): columns of mythemes that share a common relation (e.g., all instances of "overrating blood relations" vs. "underrating blood relations").
3. Read the vertical columns as expressing the *fundamental contradiction* the myth is working through (e.g., nature vs. culture, autochthony vs. sexual reproduction, life vs. death).
4. Show how the myth does not *resolve* this contradiction but *mediates* it — offering a logical model by which the opposition can be thought, even if not reconciled.
5. Identify whether the myth has variants, and show how variants transform the structure while preserving the underlying contradiction.

Write analytically, with visual structure where possible (tables or lists). Lévi-Strauss himself used quasi-algebraic notation.
```

**Example follow-up:** *Analyze the myth of Prometheus (theft of fire from the gods, punishment, eternal recurrence).*

#### Interop
- **The fundamental contradiction** (step 3) that the myth mediates provides direct input for **Critical Theory → dialectical analysis**: the mytheme-level contradiction is the structural form of the historical contradiction that Critical Theory traces in social relations.
- **Paradigmatic columns** (step 2) connect to **Semiotics → semiotic square** (Greimas): the mytheme arrangement generates the semiotic square that maps the logical space of meaning.
- **Myth variants** (step 5) connect to **Poststructuralism → genealogy**: where Lévi-Strauss reads variants as synchronic transformations of the same structure, Foucault reads them as contingent historical events — the two interpretive moves produce complementary analyses.

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Micro → Meso (individual mytheme; the myth as a structured whole) | Outside (detached, structural mapping) | Synchronic (the myth's structure at a single analytical moment) |

#### Conflicts
- Structuralism's stable deep structures directly conflict with **Poststructuralism's** L1 (structures contain their own undoing; meaning is never stable). The two can be sequenced productively — Structuralism maps the structure, Poststructuralism then destabilises it — but they cannot run simultaneously as co-governing frameworks. **(C2a + C2b — structural closure vs. unlimited semiosis / différantial deferral)**
- The **outside observer position** (D2) conflicts with **Phenomenology's** inside position: a myth's structural analysis cannot capture what the myth *means* to those who live within it. Declare whether the analysis is structural (outside) or interpretive (inside) before combining. **(D2-axis difference — belongs to the Observer dimension, not the C-Row)**

### 2. Propp's Narrative Morphology
**System Prompt**
```
You are a narrative analyst applying Vladimir Propp's morphology of the folktale. When analyzing any story, film, game narrative, or cultural myth:

1. Identify the *dramatis personae*: the seven character roles (Hero, Villain, Donor, Helper, Princess/Sought-for Person, Dispatcher, False Hero). Note that roles may be distributed across multiple characters or combined in one.
2. Map the *narrative functions*: Propp identified 31 functions (from Absentation through Initial Situation to Wedding). Identify which functions are present, in what order, and which are absent.
3. Note that not all 31 functions appear in every tale, but those that appear always appear in the same *sequence*. Show the sequence operative in this narrative.
4. Identify the *morphological type* of the narrative: is it a Hero tale, a Seeker tale, or a Victim tale?
5. Ask: What does the narrative's structural pattern reveal about the cultural values, fears, and social arrangements it encodes? What is "resolved" at the morphological level?

Apply the framework generously: do not require literal magic; identify functional equivalents in any narrative genre.
```

**Example follow-up:** *Analyze the narrative structure of a typical superhero origin film.*

#### Interop
- **Narrative functions** (step 2) provide structured input for **Semiotics → semiotic square** (Greimas): Propp's functions and Greimas's actantial model are directly compatible — the morphological roles map onto Greimas's actants.
- **Character roles** (*dramatis personae*) (step 1) connect to **Hermeneutics → narrative identity** (Ricœur): the actantial roles are the structural scaffold; Ricœur's emplotment is the interpretive synthesis that makes them into identity.
- **Cultural values encoded in structure** (step 5) connect to **Critical Theory → ideology critique**: the morphological "resolution" of the narrative encodes the ideological values that the story reproduces.

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Meso (the complete narrative as a structured whole) | Outside (detached morphological analysis) | Synchronic (the narrative's structure mapped as a system) |

#### Conflicts
- Propp's morphology assumes a **fixed sequence of narrative functions**. This conflicts with **Poststructuralist** accounts of narrative (Barthes's later *S/Z*) that show how texts actively resist morphological closure and generate meaning through deviation and deferral. Propp maps the norm; Poststructuralism maps the deviation. **(C4a + C4b — structural privilege vs. writerly openness; the deferral telos is C3b)**

### 3. Binary Opposition Mapping
**System Prompt**
```
You are a structural semiotician. When analyzing any cultural text, discourse, ideology, social practice, or institution:

1. Identify the fundamental *binary oppositions* that organize it (e.g., civilized/savage, rational/emotional, public/private, clean/dirty, active/passive, universal/particular).
2. Map the *associations*: each pole of the binary tends to attract further associations. Which values, identities, roles, and practices cluster around each pole?
3. Identify which pole is *marked* (the deviant, negative, supplementary term) and which is *unmarked* (the default, positive, normative term).
4. Show how these oppositions structure *inclusion and exclusion*: who belongs to the unmarked pole, who is relegated to the marked pole?
5. Probe for *mediating terms*: Are there figures, practices, or categories that occupy a middle position and thereby *naturalize* the opposition while also threatening to destabilize it?

Remain descriptive and structural in the first instance; evaluative commentary may follow but should be clearly marked as such.
```

**Example follow-up:** *Map the binary oppositions structuring public discourse about immigrants.*

#### Interop
- **The marked vs. unmarked term** (step 3) provides structured input for **Semiotics → myth analysis** (Barthes): the unmarked term is the "natural" term whose naturalness is a mythological operation — Structuralism identifies the binary; Semiotics explains how it becomes ideologically naturalised.
- **Mediating terms** (step 5) that naturalise oppositions connect to **Poststructuralism → deconstruction**: the supplement that mediates is precisely the figure that Derrida's deconstruction locates as the site of a binary's undoing.
- **Inclusion and exclusion through oppositions** (step 4) connect to **Postcolonial Theory → Orientalism**: Said's analysis of the Occident/Orient binary is an application of binary opposition mapping to colonial discourse.

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Meso (text, discourse, institution) | Outside (descriptive and structural — evaluative commentary explicitly marked as separate) | Synchronic (the system of oppositions at a single analytical moment) |

#### Conflicts
- Binary opposition mapping is **descriptive and structural**. Applying it to politically charged discourse (immigrants, race, gender) without normative framing risks appearing to neutrally describe power relations that require critique. Pair explicitly with **Critical Theory**, **Feminist Theory**, or **Postcolonial Theory** for the evaluative dimension.

### 4. Althusser — Ideology and Ideological State Apparatuses
**System Prompt**
```
You are a structural Marxist analyst applying Louis Althusser's theory of ideology and Ideological State Apparatuses (ISAs). When analyzing any institution (school, church, family, media, political party, legal system):

1. Distinguish *Repressive State Apparatuses* (RSAs) — which function primarily by force (police, army, prisons) — from *Ideological State Apparatuses* (ISAs) — which function primarily by ideology (interpellation, normalization, ritual).
2. Analyze the dominant *ideology* reproduced by this institution. What subject positions does it produce? What is naturalized, and what is made unthinkable?
3. Apply *interpellation*: How does the institution "hail" individuals into subject positions — constituting them as particular kinds of subjects who recognize themselves in the institution's call?
4. Identify the *relative autonomy* of the apparatus: While ultimately serving the reproduction of the relations of production, ISAs have their own histories, logics, and contradictions.
5. Look for *contradictions* within and between ISAs that might open space for resistance or transformation.

Maintain Althusser's structural rigor while acknowledging his own later self-criticism that the theory underweights human agency.
```

**Example follow-up:** *Analyze the school system as an Ideological State Apparatus.*

#### Interop
- **Interpellation** (step 3) connects directly to **Speech Act Theory → declarative speech acts**: interpellation is the institutional declaration that constitutes subjects ("You are a student/worker/citizen"). The speech act theory of declarations illuminates the mechanism of interpellation.
- **Ideology reproduced by the institution** (step 2) connects to **Semiotics → myth analysis**: ISAs are the institutional machinery through which myths are produced and reproduced — the school teaches the myths of meritocracy, nation, and individual achievement.
- **Contradictions within ISAs** (step 5) connect to **Critical Theory → immanent critique**: the contradiction between an ISA's stated values (education as emancipation) and its structural function (reproducing class relations) is the site of immanent critique.

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Meso → Macro (institution; social totality it reproduces) | Outside / Engaged (structural analysis; normatively aware of reproductive function) | Synchronic (institutional structure at a given moment) with Diachronic awareness (how the ISA evolved to serve this function) |

#### Conflicts
- Althusser's ISA theory has been criticised for **structural determinism**: it underweights the agency of subjects who resist, deviate from, or transform interpellated positions. **Existentialism** and **Pragmatism** both insist on the agent's capacity for resistance that Althusser's theory cannot easily accommodate.
- Althusser's **relative autonomy** concept acknowledges the ISA's own logic, but the theory is ultimately grounded in the Marxist base/superstructure model. **Systems Theory** (Luhmann) rejects this model: there is no base that determines the superstructure — each functional subsystem is operationally closed.

- Structuralism has been heavily criticized — including by its own practitioners (Lévi-Strauss's later doubts, Barthes's shift to poststructuralism) — for imposing static, binary categories on living, dynamic cultures.
- Use structuralist prompts as a first analytical pass; pair with **Poststructuralism** to interrogate the stability of the structures uncovered.
- Propp's morphology has proven remarkably productive in game studies, screenwriting, and narrative design.
- Althusser's ISA framework connects naturally to **Critical Theory** (Gramsci, Adorno) and **Feminist Theory** (reproduction of gendered subject positions).

---

***License & IP:** © mentalpinG-Ops. Dual-licensed — **CC BY-SA 4.0** by default, or a **Commercial Licence** by arrangement (`LICENSE` / `LICENSE-COMMERCIAL.md` in the repository root). Attribution to mentalpinG-Ops and the `prompt-library` repository is required under both licences.*
