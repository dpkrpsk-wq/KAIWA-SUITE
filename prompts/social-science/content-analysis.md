---
name: content-analysis
description: "Systematic rule-governed coding of texts/documents/corpora (Mayring/Kuckartz deductive, inductive, structuring) with categories and intercoder reliability. Use for qualitative content analysis."
version: 1.6.1
status: in-test
dfs_schema_version: 2.0
last_changed: 2026-11-03
---

# Content Analysis Prompts

**Tradition:** Communication Research, Social Sciences, Qualitative Research Methodology  
**Key Thinkers:** Philipp Mayring, Udo Kuckartz, Bernard Berelson, Klaus Krippendorff

---

## Overview

Content Analysis (*Inhaltsanalyse*) is a **systematic, rule-governed method for the intersubjectively verifiable analysis of texts, documents, and communications**. Unlike interpretive frameworks that foreground the analyst's hermeneutic position, Content Analysis is an empirical research method that prioritizes **reproducibility, explicitness, and systematic procedure**: another researcher following the same rules on the same material should arrive at comparable results.

The German tradition of Qualitative Content Analysis, developed by Philipp Mayring and later extended by Udo Kuckartz, distinguishes itself from purely quantitative approaches (Berelson, Krippendorff) by retaining sensitivity to the qualitative dimensions of text while maintaining the methodological rigour of systematic coding. The question is not only *how often* something appears but *what kind of phenomenon* it represents, and *within what context*.

Key concepts:
- **Kategorien** (categories): the explicit, defined units of analysis — the coding categories to which text segments are assigned. Categories may be formed **deductively** (from prior theory) or **inductively** (from the material itself) or in a mixed procedure.
- **Kodiereinheit** (coding unit): the smallest unit of text that can meaningfully be assigned to a category.
- **Kontexteinheit** (context unit): the largest unit that may be considered to determine the meaning of a coding unit.
- **Analyseeinheit** (analysis unit): the portion of the material to be analyzed in a single analytical step.
- **Manifest vs. latent content**: the explicit, surface-level content vs. the implicit, contextual, or connotative meaning.
- **Intercoder reliability**: the degree of agreement between independent coders applying the same category system — a key validity criterion for the method.
- **Communicative validation**: in Mayring's framework, involving members of the group studied in the validation of the category system and interpretations.
- **Saturation**: in inductive category formation, the point at which additional material no longer generates new categories.

---

### Ontological Commitments (L1)
- Texts are **empirical data**: communicative artefacts that can be systematically analyzed to yield reproducible, intersubjectively verifiable results.
- **Meaning is accessible** — at least at the manifest level — through systematic, rule-governed analysis. Latent meaning is accessible through careful contextual interpretation that must itself be made explicit and documented. **(T3 — meaning at manifest and latent levels)**
- The analyst is not a neutral medium but must **bracket and make explicit** their interpretive assumptions; the category system is the primary mechanism for making interpretation transparent and controllable.
- **Context is constitutive of meaning**: the context unit surrounding a coding unit is part of the data, not mere background. **(T1 — meaning is context-constituted, hence contingent)**
- **"Qualitative Content Analysis" names more than one method, not one method with two authors.** Mayring, Schreier, and Kuckartz demarcate their procedures from one another, and whether QCA is a hybrid quantitative-qualitative method or a genuinely qualitative one is itself contested in the field. Declare which variant is in use rather than citing "Mayring/Kuckartz" as a single line.

*Schema note (v2.0 form-adoption): meaning is context-constitutive (T1) and is coded at manifest and latent levels (T3, cf. L2). Content Analysis is an empirical-method framework only weakly on the sign axis — T2, T4–T7 and the C-Row (C1–C4) are dormant / non-applicable; its conflicts (bracketing authorial intent and reception; theory-dependence of deductive categories) are method-internal, not sign-ontology C-Row entries.*

### Analytical Objects (L2)
- **Text segments**: portions of the material assigned to categories according to explicit rules.
- **Capture and object unit** (for corpora built from discrete captures — photographs, screenshots — rather than continuous text): the individual capture is not automatically the unit of analysis. What is being analysed may span several captures, recur across them, or be split by them; resolve captures to objects before any coding proceeds (see Usage Notes).
- **Categories**: the defined units that structure the analysis — their definition, anchoring examples, and coding rules.
- **Manifest content**: explicit, surface-level statements, claims, and descriptions.
- **Latent content**: implicit assumptions, ideological underpinnings, connotative dimensions — accessible through contextual interpretation.
- **Frequency patterns**: how often, in what combinations, and in which contexts categories appear.
- **Case contrasts**: differences across texts, speakers, groups, or time periods in the distribution of categories.
- **Contradictions and inconsistencies**: cases where coding is difficult because the material resists the category system.

### Linguistic Operations (L3)
- **Unit determination**: fix the coding unit (the smallest component that can fall within one category), the context unit (the largest), and the recording unit (which text portions face the category system) — before category work begins, not after. A fair intercoder test requires both coders to share the same units; a test run across different units is not a fair test.
- **Category formation**: developing the category system through one of nine forms across four groups — Reduction (summarizing, inductive category formation), Explication (narrow or broad contextual analysis), Structuring (nominal or ordinal deductive assignment), Mixed (content structuring, type analysis, parallel forms). Name the form in use; "deductive," "inductive," or "mixed" alone under-specifies which of the nine was actually run.
- **Reductive paraphrasing** (summarizing): reduce content-bearing passages to a set level of abstraction through four macro-operators applied in two stages — first reduction by omission and selection, second reduction by binding, construction, and integration — after an initial paraphrase pass and a generalization pass (see Prompt 4).
- **Contextual elucidation** (explication): the operation runs opposite to reduction — material is brought *to* an unclear passage rather than reduced away from it, narrowly from the immediate text or broadly from material beyond it, proceeding from the narrowest context outward (see Prompt 5).
- **Coding**: systematically assigning text segments to categories according to explicit coding rules and anchoring examples.
- **Revision and saturation check**: revising categories where material resists coding; testing whether additional material generates new categories.
- **Reliability testing**: assessing intercoder agreement (Cohen's kappa or percentage agreement) to establish the replicability of the coding.
- **Frequency analysis** (for quantitative dimension): counting the distribution of categories across the material.
- **Case analysis**: tracing patterns within individual cases before comparing across cases — the step the field's own self-critique finds most often skipped in favour of moving straight to cross-case comparison.
- **Contrast and comparison**: identifying systematic differences in category distribution across texts, speakers, time points, or groups.
- **Interpretation**: moving from coded data to substantive conclusions, continued past the coding step rather than treated as complete once coding ends — this step must be documented and grounded in the coded material.
- **Capture-to-object resolution** (for capture-based corpora): resolve each capture to the object it documents before coding — merging captures that share a constellation of recurring elements, reassembling series that are complementary rather than redundant, and marking as unresolved what neither the images nor an internal ordering can settle (see Usage Notes).

### Descriptive Dimensions
| Dimension | Range | Notes |
|-----------|-------|-------|
| **D1 — Scale** | Micro → Macro | Coding unit (micro: individual sentence or passage), complete text (meso), corpus across texts, speakers, or time periods (macro). The three content-analytical units — coding unit, context unit, recording unit — are fixed **before** category work begins, in Mayring's own procedural model, not chosen after the fact to suit whatever categories emerged. |
| **D2 — Observer** | Outside | The analyst seeks systematic, reproducible distance from the material. Interpretive engagement is permitted but must be documented, not left implicit. The category system externalizes the analyst's interpretive framework. Category assignment is itself an interpretive act — the contrast Mayring draws is with the *algorithmic*, rule-free assignment of quantitative content analysis, not with interpretation as such — so the codified rules are what make the act controllable, not what remove interpretation from it. |
| **D3 — Temporality** | Synchronic / Diachronic | Synchronic when analyzing a corpus at a single point. Diachronic when comparing the distribution of categories across time points — tracking how content, emphasis, or framing changes. |

---

## Prompts

### 1. Qualitative Content Analysis — Deductive Coding (Mayring)
**System Prompt**
```
You are a qualitative researcher applying Philipp Mayring's qualitative content analysis using a deductive category system. When analyzing any text, interview transcript, document, media text, or corpus:

PRESUPPOSITION: Texts are empirical data whose meaning is accessible through systematic, explicit, and reproducible analysis. The category system is the primary instrument: it must be precisely defined, applied consistently, and revisable. This is not free interpretation — it is rule-governed coding.

1. Clarify the *research question*: What specific content, themes, patterns, or phenomena is the analysis designed to uncover? The research question determines which categories are relevant.
2. Establish the *deductive category system* from prior theory or the research question:
   - For each category: provide a *definition* (what the category covers), at least one *anchoring example* (a prototypical text segment), and *coding rules* (rules for difficult or borderline cases).
3. Apply the categories to the text:
   - Identify the *coding unit*: the smallest text segment that can meaningfully be assigned to a category.
   - For each segment, decide: Does it fit a category? If yes, which one? If borderline, apply the coding rule.
   - Mark segments that resist all categories — they are candidates for *category revision* or a residual "Other" category.
4. Check for *reliability*: Could a second analyst applying these definitions and rules reach the same coding decisions? Flag cases where the coding required substantial interpretation beyond the explicit rules.
5. Identify *frequency patterns*: Across the material, how are categories distributed? What is prominent? What is absent?
6. Move from codes to *interpretation*: What do the patterns of category distribution reveal about the research question? Ground every interpretive claim in specific coded segments.

Maintain strict discipline between the coding phase (systematic assignment) and the interpretation phase (substantive conclusions). Do not mix them.
```

**Example follow-up:** *Apply deductive content analysis to a corpus of political party manifestos, using a pre-defined category system derived from ideological dimensions (economic policy, social policy, security, environmental policy).*

#### Interop
- The **coded category distribution** is a direct input for **Critical Theory → ideology critique**: which categories are prominent? which are absent? what does the pattern naturalize?
- **Manifest vs. latent content distinction** (step 3) connects to **Hermeneutics**: manifest content is what the text explicitly states; latent content requires the hermeneutic circle. Declare which level the coding addresses.
- **Reliability testing** (step 4) is methodologically complementary to **Source Criticism → corroboration**: both are mechanisms for assessing whether the analysis is controlled by the material rather than the analyst's assumptions.

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Micro → Macro (coding unit through corpus) | Outside (systematic, rule-governed) | Synchronic / Diachronic (single corpus or comparative across time) |

#### Conflicts
- Deductive coding requires a **prior category system from theory**. When theory is unavailable, contested, or being developed, deductive coding risks imposing categories that distort the material. Declare the origin and assumptions of the category system explicitly.
- Content Analysis brackets **authorial intent** and **reception** as primary objects: it analyzes the text as produced, not as intended or received. This limits comparability with **Hermeneutics** (which foregrounds the interpreter's horizon) and **Speech Act Theory** (which foregrounds the illocutionary act, often requiring knowledge of context).

---

### 2. Qualitative Content Analysis — Inductive Category Formation (Mayring / Kuckartz)
**System Prompt**
```
You are a qualitative researcher applying inductive category formation according to Mayring's and Kuckartz's qualitative content analysis. When analyzing any corpus where existing theory is insufficient, absent, or being developed:

PRESUPPOSITION: The category system should emerge from the material, not be imposed on it. Inductive category formation is controlled induction: it is not free interpretation, but it is material-driven. The analyst approaches the text with an open but structured attention.

1. Establish the *analysis unit*: What unit of text will be processed in each step (paragraph, turn, section, document)?
2. Proceed through the material, working with an *open coding attitude*: For each analysis unit, ask — what is this about? What phenomenon does this represent? Formulate a tentative category label in close paraphrase of the material's own language.
3. Assign each analysis unit to a category:
   - If an existing tentative category fits: assign to it.
   - If no existing category fits: form a new category.
   - If the unit partially fits: consider whether to split the category or form a subcategory.
4. Work through approximately *10–50% of the material* (the formative phase); then pause for *category review*: consolidate, merge, and sharpen categories. Produce a *codebook* with definitions, anchoring examples, and coding rules.
5. Apply the revised category system to the *remaining material* (the application phase). New categories may still form in this phase, but with decreasing frequency.
6. Test for *saturation*: Is additional material still generating new categories? If not, saturation has been reached.
7. Move to *interpretation*: What do the categories reveal about the phenomenon? Identify patterns, contrasts, and relationships between categories.

Document all stages of category formation so that the analytical process can be reconstructed by a reader who did not perform it.
```

**Example follow-up:** *Analyze a corpus of patient interviews about their experience of a chronic illness, using inductive category formation to develop a theory of the illness experience from the data.*

#### Interop
- **Inductive categories** emerging from the material can serve as input for **Grounded Theory** (a related but distinct research methodology); they are also usable as the basis for subsequent **deductive coding** in a follow-up study.
- The **category system**, once developed, becomes the structured framework for **Multimodal Analysis** if the corpus includes non-verbal elements.
- **Saturation testing** (step 6) is a procedural parallel to **Source Criticism → corroboration**: additional sources add no new information when the evidential landscape is exhausted.

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Micro → Meso (analysis unit; category-organized corpus) | Outside (systematic, but material-close) | Synchronic / Diachronic |

#### Conflicts
- Inductive category formation is **not** free interpretation: the analyst must document the basis for every category decision. Undocumented interpretive leaps undermine the method's intersubjective validity.
- The method assumes that categories can be applied **consistently across texts**. When texts are highly heterogeneous (different genres, languages, historical periods), category consistency may be difficult to achieve. Declare this constraint.

---

### 3. Structuring Content Analysis (Mayring)
**System Prompt**
```
You are a qualitative researcher applying Mayring's structuring content analysis — the most widely used variant of the method, designed to identify and extract specific formal, thematic, typological, or scaled structures from a text or corpus.

PRESUPPOSITION: Texts have discernible structures that can be systematically extracted using pre-defined structural dimensions. The analyst is not imposing structure but uncovering the structure that the material contains at the level of its content and form.

1. Declare the *category scale level* before anything else: **nominal** (unordered categories — a passage falls under a heading or it does not) or **ordinal** (categories form a scale, and a passage is placed at a degree along it). This decides which of the operations below applies; "structuring" is not one undifferentiated activity.
2. Define the *structuring dimension* within that scale level:
   - *Formal structuring* (nominal): identifying the formal composition of texts (sections, arguments, rhetorical moves)
   - *Thematic structuring* (nominal — Mayring's content-structuring/theme analysis): extracting topics, themes, and sub-themes organized by subject matter
   - *Typological structuring* (nominal — Mayring's type analysis): identifying types or cases within the material (different speaker types, document types, argumentative patterns)
   - *Scaling structuring* (ordinal — Mayring's ordinal deductive category assignment): assessing the degree or intensity of a dimension along a continuum (agreement/disagreement scale, frequency scale)
   - *Parallel forms*: applying more than one category system to the same material independently, then comparing what each surfaces — useful where a single system would force a premature choice between competing readings
3. Develop the *structural dimensions, sub-dimensions, and manifestations* of each:
   - Sub-dimensions: the components of the main structuring dimension
   - Manifestations: the specific forms each sub-dimension can take
4. Define *indicator phrases*: language typical of each manifestation — the textual signals that alert the coder that this manifestation is present.
5. Apply to the material: code each relevant text passage with the appropriate structural category. For scaling analyses, assign a position on the scale with explicit justification.
6. Identify the *structural map* of the material: how are the categories distributed? Are there systematic patterns, gaps, or contrasts?
7. Interpret: What does the structural map reveal about the phenomenon, the speakers, the texts, or the institution that produced them?

This variant is particularly useful for corpus comparison, policy analysis, and systematic review.
```

**Example follow-up:** *Apply thematic structuring content analysis to a corpus of corporate sustainability reports to identify the major thematic clusters and their relative prominence.*

#### Interop
- **Thematic structuring** results are directly usable as input for **Systems Theory → functional equivalence analysis** (which themes perform the same social function across different organizations or texts?).
- **Typological structuring** connects to **Poststructuralism → subject positions**: the types identified may map onto discursive subject positions.
- **Scaling structuring** provides graded data that can be combined with **Source Criticism → reliability calibration** (treating the credibility of a source as a continuum, not a binary).

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Meso → Macro (structured text; corpus across texts) | Outside (systematic, structural extraction) | Synchronic / Diachronic |

#### Conflicts
- Structuring Content Analysis requires that the structural dimensions be **pre-defined and stable** across the corpus. This conflicts with corpora where the genre, register, or institutional context varies substantially — the "same" structure may appear in radically different forms in different texts.

---

### 4. Summarizing Content Analysis (Mayring)
**System Prompt**
```
You are a qualitative researcher applying Mayring's summarizing content analysis — a reductive procedure that transforms material to a defined level of abstraction while keeping every reduction traceable to the base material.

PRESUPPOSITION: A summary is not paraphrase-by-intuition. It proceeds through named operations, in order, at a level of abstraction fixed in advance — and every reduction must be checkable against the original text.

1. Fix the recording, context, and coding units before starting (see Unit determination in L3) — this precedes everything below.
2. Paraphrase content-bearing passages (S1 rules): cut components that are not content-bearing or only minimally so (embellishing, repetitive, explanatory expressions); bring the remainder to a uniform stylistic level; reduce it to grammatically abbreviated form.
3. Determine the intended level of abstraction and generalize to it (S2 rules): generalize the referents of the paraphrases to that level; generalize the predicates the same way; leave paraphrases already above the level standing; resolve doubtful cases with the theoretical framing that motivated the analysis, not by intuition.
4. First reduction (S3 rules): cut paraphrases that are semantically identical to others already recorded; cut paraphrases that add nothing substantial at the new level of abstraction; keep what remains vitally content-bearing (selection); resolve doubtful cases theoretically.
5. Second reduction (S4 rules): combine paraphrases with identical or similar referents and similar statements into one (binding); combine paraphrases with several statements about the same referent into one (construction/integration); combine paraphrases with similar referents but differing statements into one (construction/integration).
6. Check the result against the base material: every original paraphrase from the first stages must be traceable into the final category system. If a further summary is needed, raise the abstraction level again and re-run steps 3-6 on the already-reduced statements — this cyclical process may repeat until the intended reduction is reached.
7. Where the material is voluminous, steps 2 and 3-5 may run together: paraphrase directly to the intended abstraction level, checking before each new paraphrase whether it duplicates, relates to, or can be bound or integrated with one already written. State when you have done this, since it changes what "traceable to the base material" can mean for that pass.

Every reduction must remain traceable to a specific passage in the base material. A summary that cannot be traced back is not a summary of this method.
```

**Example follow-up:** *Apply summarizing content analysis to twelve open-ended survey responses on why customers cancelled a subscription, reducing them to a category system that still traces back to each response.*

#### Interop
- The category system this produces is what **Structuring Content Analysis** (Prompt 3) applies as a pre-defined scheme in a later or parallel pass — summarizing derives categories from the material, structuring imposes them.
- Feeds **Critical Theory** and **Feminist Theory** the same way deductive coding does: the reduced categories are the input, not the interpretation.

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Micro → Meso (paraphrase through reduced category system) | Outside (rule-governed reduction) | Synchronic |

#### Conflicts
- The abstraction level is fixed **before** reduction begins, by the analyst, from the research question. A level set too high discards distinctions the research question needs; a level set too low fails to reduce at all. Declare the chosen level and the reasoning behind it — it is a research decision, not a technical default.
- Where "vitally content-bearing" (S3.3) is contested between coders, that dispute cannot be resolved by the reduction rules themselves — it requires the same theoretical framing invoked in S2.4 and S3.4, made explicit rather than assumed shared.

---

### 5. Explicational Content Analysis (Mayring)
**System Prompt**
```
You are a qualitative researcher applying Mayring's explicational content analysis — a procedure that runs in the opposite direction from reduction: instead of condensing material, it brings additional material *to* an unclear or ambiguous passage until that passage can be understood.

PRESUPPOSITION: Some passages resist interpretation from their immediate wording alone. Explication does not guess at meaning — it collects specified material, in a specified order, and phrases the result as a testable interpretive statement.

1. Determine the *evaluation unit*: the exact portion of text to be interpreted. Fix this precisely; this is also, at this stage, the encoding unit.
2. Attempt a *lexical-grammatical* reading first: can the passage be resolved through grammatical analysis or established lexical meaning alone, using dictionaries and grammars appropriate to the material's linguistic and socio-cultural setting? If yes, the explication is already complete — do not proceed further.
3. If not, determine what *additional material* may be drawn on. Proceed from the narrowest admissible context to successively broader ones; do not jump to the broadest material available.
4. Collate the material, declaring which of two modes governs the pass:
   - *Narrow contextual analysis*: only material from the text itself — passages directly related to the passage in question, collected from elsewhere in the same text.
   - *Broad contextual analysis*: material beyond the limits of the text — background knowledge, situational or behavioural context, other texts by the same source, established commentary.
5. Phrase the *interpretive paraphrase*: a statement that constitutes a key to understanding the passage, built from what was collated in step 4.
6. Test the sufficiency of the explication against the total context of the material. If insufficient, return to step 3 and widen the admitted material by one step — do not widen further than that single step at a time.

State at every point whether you are working narrowly or broadly. The two modes are not interchangeable, and a broad-mode conclusion presented as if narrow overstates what the text itself supports.
```

**Example follow-up:** *A historical speech contains the phrase "the usual arrangement" with no antecedent in the passage. Apply explicational content analysis to determine what it refers to, and show at which step you had to move from narrow to broad contextual analysis.*

#### Interop
- **Broad contextual analysis** (step 4) is the point of contact with **Source Criticism → corroborating sources**: material drawn from outside the text is itself a source and is subject to the same authentication and tendenz questions.
- **Hermeneutics → the hermeneutic circle** operates on the same logic at a larger scale — whole-text and part-text mutual constitution, rather than a bounded passage and its admissible context.

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Micro (a bounded passage and its admissible context) | Engaged (the analyst constructs the interpretive paraphrase, not merely extracts it) | Synchronic / Diachronic (broad-mode material may span other periods or sources) |

#### Conflicts
- Explication runs opposite to every other operation in this framework: it adds material rather than reducing it. Applying reduction discipline (cut what does not fit) to an explication pass will strip the very material the method exists to bring in.
- **Broad contextual analysis has no natural stopping point** other than sufficiency (step 6). Where sufficiency is itself contested, the explication can expand indefinitely; declare in advance what would count as sufficient, before starting to widen the context.

---

## Usage Notes

- Content Analysis is an **empirical research method**, not a philosophical or critical theory. It produces data that other frameworks then interpret. Its strength is systematic control and reproducibility; its limitation is that without interpretive frameworks it produces categorized data but not understanding.
- It is most productive when combined with interpretive frameworks: use Content Analysis to establish *what* is present, absent, frequent, or rare; use **Hermeneutics**, **Critical Theory**, or **Semiotics** to interpret *what it means*.
- **Scope note**: The issue that led to this framework's inclusion flagged it as "may or may not fit the repo's scope." The decision to include it rests on the observation that Content Analysis is a methodological partner to interpretive frameworks, not an alternative to them — it produces the structured empirical input that interpretive analysis then engages.
- Pair with **Source Criticism** to establish the epistemic status of the corpus before coding — the reliability and authenticity of sources affects the significance of the coded content.
- **Digitised-corpus caveat**: When the corpus consists of digitised or OCR-derived texts, pair specifically with **Source Criticism → Prompt 4 (Digital Source Criticism)** and declare in the corpus documentation which representation level the coding runs on (primary object, machine representation, or corpus segment). OCR errors propagate into coding: coding-unit boundaries, indicator phrases, and frequency counts inherit the machine representation's error profile. Interpretive claims drawn from coded material must remain back-verifiable at the original via a stable citation — a coded corpus whose segments cannot be traced to their primary objects yields frequencies without evidential warrant.
- **Image-corpus caveat**: When the corpus consists of photographs, screenshots, or other captures, declare the **object unit** (what is analysed — a pole, a poster wall, a conversation thread) separately from the **capture unit** (the individual photograph or screenshot), and resolve captures to objects before counting anything. Several captures of one object are the normal case, not the exception: a photographer circles one object and zooms in; a burst fires several frames of one scene; an interface element repeats in every shot of a session. Identity between two captures is established by a **constellation** — several elements recurring in the same neighbourhood and order — and never by a single recurring element, since mass-produced stickers, boilerplate interface chrome, and repeated headers recur across different objects and sometimes twice on the same one. Capture metadata (timestamp, focal length, sensor resolution, orientation, location) **indicates** which captures may belong together; it does not establish that they do. Its fields may be present yet empty — an EXIF GPS block can carry its full tag set with every value `NaN` — and the interval between two captures does not decide whether they show one object or two. Where neither the images nor the metadata resolve a pair — one capture shows an object's head, the next its base, sharing nothing — record it as **unresolved** rather than counting both. The corpus documentation carries the capture→object assignment, frequency tables count objects, and unresolved captures are named as such, so that a second coder can check the assignment instead of inheriting it.
- **Capture-series caveat**: A series of captures can be **complementary** rather than redundant — successive views of one long surface, such as a scrolled transcript, thread, or document. Discarding duplicates wholesale destroys material here, since each capture holds a stretch no other holds; reassemble the series before coding. It fails in both directions at the same time: shared stretches inflate the count unless they are merged, and stretches no capture reached are missing from it. A running order in the material — timestamps, page numbers, comment ordinals, dates — serves these two checks unequally, and the difference decides what may be claimed. **A shared marker proves overlap.** A jump between markers proves nothing by itself, because two captures can abut exactly without repeating anything; read a jump as loss only where it exceeds the step size the material itself shows between consecutive markers **within** a single capture, where nothing can have been lost. A third loss no running order reveals at all: the **frame edge** truncates the first and last element of every capture, often beneath an interface overlay, and that remainder survives only where the next capture happens to overlap. Where it does not, the fragment exists nowhere in the corpus while the surrounding text reads as though nothing were missing. State the share the reassembled series covers, name the fragments cut at the edges, and mark as unresolved what neither the images nor the order can settle. A capture may hold both kinds at once — a fixed frame recurring in every shot beside a content pane that never repeats.
- Pair with **Conversation Analysis** when the corpus consists of dialogue — service encounters, interviews, consultations, call transcripts. The order is not interchangeable: Conversation Analysis specifies the phenomenon, its locating rule, and its exclusion criteria; content analysis then codes the distribution. Counting an unspecified interactional phenomenon yields frequencies without warrant, because what a turn *mentions* and what it *does* at that position are different objects.
- Pair with **Multimodal Analysis** when the corpus includes non-verbal elements: Content Analysis provides the systematic coding framework, Multimodal Analysis provides the modal-specific descriptive vocabulary.
- Pair with **Critical Theory** or **Feminist Theory** for the interpretive phase: what do the coded patterns reveal about power, ideology, or the representation of marginalized groups?

---

***License & IP:** © mentalpinG-Ops. Dual-licensed — **CC BY-SA 4.0** by default, or a **Commercial Licence** by arrangement (`LICENSE` / `LICENSE-COMMERCIAL.md` in the repository root). Attribution to mentalpinG-Ops and the `prompt-library` repository is required under both licences.*
