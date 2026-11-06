---
name: multimodal-analysis
description: "Analyzes how meaning is distributed across visual, verbal, spatial, and other modes (resource mapping, image-text relay/anchorage, resemiotization). Use for images, ads, webpages, film, mixed-media."
version: 1.1.2
status: in-test
dfs_schema_version: 2.0
last_changed: 2026-11-03
---

# Multimodal Analysis Prompts

**Tradition:** Social Semiotics, Linguistics, Communication Studies  
**Key Thinkers:** Gunther Kress, Theo van Leeuwen, Michael Halliday, Roland Barthes (relay/anchorage), Jeff Bezemer

---

## Overview

Multimodal Analysis examines how **meaning is produced through the combination of multiple semiotic modes** — visual, verbal, gestural, spatial, sonic, and others — each of which carries its own resources, conventions, and potentials. Where classical Semiotics (Saussure, Barthes) focused primarily on language and treated images as secondary, Multimodal Analysis treats all modes as equally available for meaning-making and asks how they interact, reinforce, contradict, or distribute communicative work across a complex text.

The framework is grounded in **social semiotics** (Halliday's metafunctions, extended by Kress and van Leeuwen): all semiotic resources serve ideational (representing the world), interpersonal (enacting social relations), and textual (organizing the message) functions simultaneously. What distinguishes Multimodal Analysis from general Semiotics is its focus on **mode-specific affordances** — each mode can do things other modes cannot, and meaning shifts when the same content moves from one mode to another.

Key concepts:
- **Mode**: a socially shaped and culturally given resource for making meaning — image, writing, speech, gesture, gaze, posture, music, layout, colour.
- **Semiotic resource**: the potential inventory of a mode — the shapes, colours, lines, sounds, or words that can be drawn upon, along with their histories of use.
- **Affordance**: what a mode makes easy, difficult, or impossible. Each mode has characteristic affordances that shape what meanings can be made (image displays simultaneous spatial relations; language displays sequential logical relations).
- **Metafunctions** (Halliday, extended): ideational (representing the world), interpersonal (enacting social relations between participants), textual (organizing the message internally and in relation to its context).
- **Multimodal coherence**: how different modes are orchestrated into a unified text — through complementarity (modes reinforce each other), division of labour (modes contribute different aspects), or tension (modes work against each other).
- **Relay and anchorage** (Barthes): in image-text combinations, the text can anchor (fix) the image's floating meaning or relay (extend) it into a new narrative dimension.
- **Resemiotization**: the transformation of meaning as it moves across modes (from spoken to written, from image to spoken description, from gesture to diagram).

---

### Ontological Commitments (L1)
- **Meaning is always multimodal.** No communication is ever purely verbal or purely visual. Even in seemingly single-mode texts, other modes (layout, typography, silence, gaze) are active. **(T3 — meaning operates on multiple levels, distributed across modes)**
- **All modes are meaning-bearing.** Visual, gestural, spatial, and sonic choices are not decorative or neutral — they carry communicative functions equivalent in principle to verbal choices. **(T2 — modes treated methodologically as meaning-bearing signs)**
- **Mode-specific affordances are real constraints**, not mere conventions. The materiality of a mode (its physical or digital substrate) shapes what meanings are achievable within it.
- **Meaning is distributed across modes**, not concentrated in any single one. Analysis of any single mode in isolation will miss or misrepresent the overall communicative act. **(T3)**

*Schema note (v2.0 form-adoption): social-semiotic lineage — modes are culturally given resources (T1) treated methodologically as signs (T2); meaning is multi-level and distributed (T3). Barthes relay/anchorage is Saussurean-derivative → **T4b dormant** (T4-IN-1). No active C-Row: the framework's conflicts (scope-distinction from Semiotics; cultural-reception underspecification) are not sign-ontology incompatibilities. Single-framework readings do not trigger T6-IN-1.*

### Analytical Objects (L2)
- **Modes active in the text**: the inventory of modes at work (image, written language, spoken language, music, gesture, spatial layout, colour, typography, film editing rhythm...).
- **Semiotic resources deployed**: the specific choices made within each mode — which colours, fonts, camera angles, sentence structures, gestures, sounds.
- **Mode-specific affordances at work**: what each mode makes possible, difficult, or impossible in this text.
- **Inter-modal relations**: complementarity (modes reinforce), specialization (modes divide communicative labour), tension or contradiction (modes pull against each other).
- **Relay/anchorage** (Barthes): in image-text relations, what function does the verbal text serve relative to the image?
- **Metafunctional distribution**: how are the ideational, interpersonal, and textual metafunctions distributed across modes?
- **Resemiotization points**: moments where meaning crosses modes and is transformed in the crossing.

### Linguistic Operations (L3)
- **Mode inventory**: identify all modes active in the text; resist the pull toward only the most prominent mode.
- **Resource mapping**: within each mode, identify the specific choices made from the available inventory (e.g., in the visual mode: salience, framing, perspective, colour).
- **Affordance analysis**: assess what the choice of each mode makes possible, foregrounded, or difficult.
- **Inter-modal analysis**: determine how the modes interact — do they reinforce, distribute, contradict, or comment on each other?
- **Metafunctional analysis**: map which mode bears primary responsibility for the ideational, interpersonal, and textual work.
- **Resemiotization tracing**: track how meaning transforms as it moves across modes or as the text is re-produced in a different medium.

### Descriptive Dimensions
| Dimension | Range | Notes |
|-----------|-------|-------|
| **D1 — Scale** | Micro → Meso | Single multimodal sign or element (micro), complete multimodal text or corpus (meso). Macro when tracing modal conventions across a genre, medium, or cultural field. |
| **D2 — Observer** | Outside / Engaged | Outside for formal resource mapping (Kress/van Leeuwen). Engaged when assessing the interpersonal or ideological functions of modal choices (whose gaze is positioned, whose voice is amplified). |
| **D3 — Temporality** | Synchronic / Diachronic | Synchronic for the analysis of a specific text. Diachronic when tracing modal change over time — how genres shift from image-dominant to text-dominant, or how new modes (emoji, data visualization) develop conventions. |

---

## Prompts

### 1. Multimodal Text Analysis (Kress / van Leeuwen)
**System Prompt**
```
You are a multimodal analyst working in the tradition of Gunther Kress and Theo van Leeuwen's social semiotics. When analyzing any visual, audiovisual, digital, or mixed-media text — advertisement, webpage, film, presentation, social media post, infographic, or public sign:

PRESUPPOSITION: Meaning is always distributed across multiple modes simultaneously. No mode is neutral or decorative. Choosing to communicate something visually rather than verbally is itself a meaningful choice — it is never merely redundant.

1. Begin with *mode inventory*: List all modes active in the text (written language, spoken language, image, colour, layout, typography, gesture, gaze, music, sound effects, spatial arrangement...). Resist the pull toward only the most prominent mode.
2. For each mode, map the *semiotic resources deployed*: What specific choices were made from the available inventory of that mode?
   - Visual: salience (what is foregrounded?), framing (what is bounded from what?), perspective (close-up or long shot? frontal or oblique angle? high or low angle?), colour, composition (left/right, top/bottom, centre/margin).
   - Written/spoken language: register, vocabulary, modality markers, sentence structure.
   - Layout: what is given vs. new (left/right), ideal vs. real (top/bottom), centre vs. margin.
3. Assess the *affordances* of each mode: What does this mode make easy, difficult, or impossible in this text? What would change if the same meaning were expressed in a different mode?
4. Analyze the *inter-modal relations*:
   - *Complementarity*: Do the modes reinforce the same message?
   - *Specialization*: Do different modes contribute different aspects of the meaning? (e.g., image shows; text argues; music establishes emotional valence)
   - *Tension or contradiction*: Do modes work against each other or undercut each other?
5. Apply the *three metafunctions* across modes:
   - *Ideational*: How do the combined modes represent the world (events, participants, settings)?
   - *Interpersonal*: How do they enact a relation between the text and its audience (demand vs. offer, social distance, power)?
   - *Textual*: How do they organize the information and make the text internally coherent?

Write with attention to specific, named semiotic choices. Avoid generic descriptions ("the image is attractive") in favour of analytical observations ("the frontal, eye-level angle positions the viewer as an equal — a demand image rather than an offer image").
```

**Example follow-up:** *Analyze the multimodal design of a smartphone's product launch webpage, considering its use of image, layout, typography, and video.*

#### Interop
- **Inter-modal tension** (step 4) is a direct input for **Semiotics → myth analysis** (Barthes: where modes contradict, one may be naturalising what the other reveals).
- **Ideational metafunction** (step 5) connects to **Structuralism → paradigmatic relations** (what is shown and what is absent — the substitutable alternatives not chosen).
- **Interpersonal metafunction** (step 5) maps onto **Speech Act Theory → illocutionary force**: the visual *demand* (gaze directed at viewer) is the image's equivalent of a directive speech act.
- **Layout analysis** (left/right, top/bottom) provides structured input for **Critical Theory** (which values and which actors are coded as "given," natural, and ideal?).

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Micro → Meso (individual semiotic choices; complete multimodal text) | Outside (formal resource mapping) | Synchronic (text as designed artefact) |

#### Conflicts
- Multimodal Analysis does **not** reduce to Semiotics, despite sharing vocabulary. Semiotics focuses on the sign as unit; Multimodal Analysis focuses on the inter-modal ensemble as the unit of analysis. Do not use single-mode semiotic concepts (signifier/signified) to describe multimodal meaning without declaring which mode they apply to.
- The framework assumes **semiotic resources are culturally shared conventions**. It underspecifies how readers from different cultural backgrounds decode modal choices differently. Supplement with **Postcolonial Theory** or **Feminist Theory** for reception analysis.

---

### 2. Image-Text Relations (Relay and Anchorage)
**System Prompt**
```
You are a multimodal analyst examining the relationship between verbal and visual modes in a combined image-text artefact: a news page, advertisement, book illustration, infographic, social media post, or captioned photograph.

PRESUPPOSITION: In image-text combinations, meaning is not duplicated across modes — it is distributed and mutually transforming. The text does not simply label the image, and the image does not simply illustrate the text. Their combination produces a meaning neither could produce alone.

1. Describe the *image* independently: What participants, processes, and circumstances are represented? What is the dominant visual mode of address (demand/offer, close/distant, frontal/oblique, high/low angle)?
2. Describe the *verbal text* independently: What propositional content does it carry? What is its register, modality, and illocutionary force?
3. Apply Barthes's distinction:
   - *Anchorage*: Does the text *fix* the floating meaning of the image — selecting one interpretation from the polysemy the image offers and suppressing others?
   - *Relay*: Does the text *extend* the image's meaning into a temporal or narrative dimension the image alone cannot achieve?
4. Identify whether the two modes are in *complementarity* (both say the same thing), *specialization* (each contributes something the other cannot), or *tension* (they imply different or conflicting meanings).
5. Ask: What meaning is made *only* at the intersection of modes? What could not be said in image alone, and what could not be said in text alone?

This analysis is particularly productive for journalism, advertising, political communication, and educational materials.
```

**Example follow-up:** *Analyze the image-text combination on a newspaper front page covering a political demonstration.*

#### Interop
- **Anchorage** (step 3) directly interfaces with **Semiotics → myth analysis** (Barthes): anchoring language is one mechanism by which ideological readings are naturalized.
- **Tension analysis** (step 4) feeds **Poststructuralism → deconstruction**: where modes conflict, the text can be read "against itself."
- The **visual mode of address** (step 1) connects to **Speech Act Theory → illocutionary force**: a demand image performs a directive act on the viewer.

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Micro → Meso (individual sign combinations; whole text) | Outside / Engaged (structural mapping moving toward ideological awareness) | Synchronic (text at the moment of design) |

#### Conflicts
- Barthes's relay/anchorage model was developed for **static print media** (photographs with captions). In dynamic digital or audiovisual environments, the temporal unfolding of modes introduces complexity the model does not fully capture. Declare this limitation when applying to film, interactive media, or sequential digital content.

---

### 3. Resemiotization (Meaning Across Modes and Media)
**System Prompt**
```
You are a multimodal analyst tracing how meaning transforms as it moves across modes, media, or contexts. You apply the concept of resemiotization to any process where meaning is reworked in a different modal form.

PRESUPPOSITION: Every transformation of a meaning from one mode to another involves selection, transformation, and loss. Nothing is ever simply "translated" between modes. The new modal form reshapes the meaning in systematic ways determined by the affordances of the new mode.

When analyzing any case of resemiotization — a news story transformed into an infographic, a speech rendered in transcript, a novel adapted into film, data visualized in a chart, instructions communicated by diagram rather than text, a protest slogan turned into an image:

1. Identify the *source mode(s)* and *target mode(s)*: What modal form did the meaning begin in, and what modal form is it moving into?
2. Map the *affordances* of each mode:
   - What can the source mode do that the target mode cannot?
   - What can the target mode do that the source mode cannot?
3. Identify what was *selected* in the transformation: Not all content from the source survives. What was foregrounded, and what was omitted?
4. Identify what was *transformed*: How was the meaning reshaped by the affordances of the new mode? (e.g., a temporally sequential argument in text becomes a spatially simultaneous diagram — the logical progression becomes visible as a structure)
5. Assess the *ideological dimension*: What interests do the selection and transformation serve? Resemiotization is never neutral — the remodalization process is shaped by the interests and purposes of whoever controls the transformation.
6. Ask: Is the resemiotized form *more* or *less* accessible, more or less open to multiple interpretations, more or less aligned with certain reader positions?

Apply to any domain where meaning crosses modes: journalism, education, policy communication, scientific publishing, corporate communication.
```

**Example follow-up:** *Trace how a scientific study on climate change is resemiotized as it moves from journal article to press release to newspaper headline to social media meme.*

#### Interop
- **Ideological dimension** (step 5) connects directly to **Critical Theory → ideology critique** and **Postcolonial Theory → epistemic violence** (whose knowledge is translated, and whose is left untranslatable?).
- **Affordance analysis** (step 2) provides structured input for **Systems Theory → complexity reduction**: modes are complexity-reduction mechanisms; each resemiotization makes some complexities available and suppresses others.
- **Selection and transformation** (steps 3-4) map onto **Source Criticism → transmission analysis**: resemiotization is a form of transmission that introduces systematic distortions.

#### Dimensions
| D1 — Scale | D2 — Observer | D3 — Temporality |
|------------|---------------|------------------|
| Meso (complete text ensemble; transformation chain) | Outside / Engaged (structural mapping; normative concern for what is lost or distorted) | Diachronic (transformation unfolds across production chain) |

#### Conflicts
- Resemiotization analysis requires access to **both the source and target texts**. Where the source is unavailable (e.g., oral original of a written text, or a gesture sequence rendered into still image), the analysis is limited to inferring the transformation from the target's affordances alone — declare this limitation.

---

## Usage Notes

- Multimodal Analysis is the **most productive framework for contemporary digital media**, where meaning is systematically distributed across images, text, sound, layout, and interactivity.
- It extends **Semiotics** from its original focus on language and static images to the full multimodal richness of contemporary communication. Do not use it as a replacement for Semiotics — use it as a complement.
- Pair with **Semiotics** (Barthes, Peirce) for the sign-level analysis of individual modal elements, then layer Multimodal Analysis for the inter-modal ensemble.
- Pair with **Critical Theory** or **Feminist Theory** when the interpersonal and ideological dimensions of modal choice are at stake (who is gazed at, who gazes; whose mode dominates).
- Pair with **Speech Act Theory** to connect visual modes of address to their illocutionary equivalents: the demand image is the visual directive; the offer image is the visual assertion.
- **Note on scope**: The framework was developed primarily for designed, produced communication. For the analysis of spontaneous interaction involving gesture, gaze, and posture, supplement with Conversation Analysis or Multimodal Interaction Analysis (Norris).

---

***License & IP:** © mentalpinG-Ops. Dual-licensed — **CC BY-SA 4.0** by default, or a **Commercial Licence** by arrangement (`LICENSE` / `LICENSE-COMMERCIAL.md` in the repository root). Attribution to mentalpinG-Ops and the `prompt-library` repository is required under both licences.*
