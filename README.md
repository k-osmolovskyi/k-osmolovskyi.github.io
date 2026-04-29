
# Theory of Cognitive Structuring - *Open Research Series*
This open series presents a formal, substrate-independent framework for analyzing regulatory dynamics in cognitive architectures operating under bounded resources. The theory introduces a unified mathematical language for describing how structural constraints, overload accumulation, trajectory-dependent regulation, and layered admissibility conditions govern stability, structural change, and the emergence of persistent behavioral patterns (identity) across biological, artificial, and complex adaptive systems.
Unlike models that assume full observability or treat structural change as continuous optimization, this framework formalizes cognitive systems as architectures that:
* Operate over restricted discrepancy domains rather than complete state spaces;
* Accumulate non-compensated structural pressure through trajectory-dependent overload memory;
* Permit structural updating only when joint regulatory states cross admissibility boundaries.

Identity is derived not as a representational primitive, but as a structural attractor emerging from long-run overload minimization under bounded regulation.

- **Domain**: [Cognitive Evolution Beyond the Single Life Cycle](https://doi.org/10.5281/zenodo.19673721)
- **Concept**: [Structural Updating and the Limits of Cognitive Change](https://doi.org/10.5281/zenodo.19545676)

---

## Framework Relevant Audience

The General Theory of Cognitive Structuring provides a substrate-independent formal language for analyzing regulatory dynamics under bounded resources. It may be of interest to researchers working in:

- [Theoretical Cognitive Science](https://github.com/k-osmolovskyi/k-osmolovskyi.github.io/blob/main/ref/theoretical-cognitive-science.md) — coherence geometry, trajectory-dependent regulation, identity as regulatory attractor
- [Dynamical Systems Theory](https://github.com/k-osmolovskyi/k-osmolovskyi.github.io/blob/main/ref/dynamical-systems.md) — stability regions, hysteresis, attractor dynamics in regulatory phase space
- [AI Architecture & Safety](https://github.com/k-osmolovskyi/k-osmolovskyi.github.io/blob/main/ref/ai-safety.md) — admissibility, overload memory, structural blindness in long-horizon agents.
  - For more details please read concept paper: [*Beyond Output Correction*](https://doi.org/10.5281/zenodo.19797101)
- [Complex Systems](https://github.com/k-osmolovskyi/k-osmolovskyi.github.io/blob/main/ref/complex-systems.md) — invariant-induced stability, compression-driven evolution, multi-system order alignment
- [Formal Methods](https://github.com/k-osmolovskyi/k-osmolovskyi.github.io/blob/main/ref/formal-methods.md) — layered admissibility, non-injective accessibility, proof-ready operators and constructions
- [Organizational / Institutional Modeling](https://github.com/k-osmolovskyi/k-osmolovskyi.github.io/blob/main/ref/organizational-modeling.md) — structural inertia, admissible discrepancy domains, normative compression
- [Philosophy of Mind / Phenomenology](https://github.com/k-osmolovskyi/k-osmolovskyi.github.io/blob/main/ref/cognitive-phenomenology.md) — inner manifestation vs. enacted processing, valence asymmetry, restricted accessibility
- [Psychology](https://github.com/k-osmolovskyi/k-osmolovskyi.github.io/blob/main/ref/psychology.md) — overload accumulation, hysteresis in decision-making, identity-cores as stability basins

> *Each link leads to a domain-specific overview showing how GTCS concepts may reframe key problems in that field.*

---

## Key Concepts
- `Invariants` &mdash; historically formed architectural constraints that remain preserved under ordinary processing;
- `Coherence` &mdash; the geometric distance between the current configuration and the region of structural stability induced by the active invariants;
- `Structural tension and overload` &mdash; immediate regulatory pressure and its accumulated memory, making system dynamics trajectory-dependent rather than reducible to the present state alone;
- `Structural admissibility` &mdash; a multi-level condition determining which discrepancies enter the regulatory domain and under what conditions structural updating becomes possible;
- `Pre-symbolic admissibility` &mdash; a filter operating prior to representation, determining which signals can participate in regulation at all;
- `Compression` &mdash; a mechanism through which new invariants are formed, reducing expected overload and potentially transforming the geometry of admissibility;
- `Identity as a regulatory attractor` &mdash; a stable region of configurations toward which trajectories tend to converge through the minimization of long-term regulatory pressure;
- `Inter-system order alignment` &mdash; a condition for the co-regulation of heterogeneous architectures without requiring a shared metric or common representational format.

---

## How to Use This Series
**Minimal Reading Path**:  [Domain](https://doi.org/10.5281/zenodo.19673721) → [Synthetic](https://doi.org/10.5281/zenodo.19467207) → [TR #2026-2](https://doi.org/10.5281/zenodo.19467770)  → [TR #2026-3](https://doi.org/10.5281/zenodo.19467881) → [TR #2026-5](https://doi.org/10.5281/zenodo.19468033) 

**Full Understanding**: Read sequentially (TR #2026-1 through 2026-14 + Technical Notes). Definitions, axioms, and theorems are built incrementally; later reports presuppose earlier formalizations.

[Verification package table](#verification-package-for-the-theory): glossary, acyclicity statement, dependency table, *how to*, etc.

[Proof-Oriented Documents](#proof-oriented-documents): collected results, proof status note; collected propositions and theorems; proof status register; verification package overview; proof notes.

[Overview of the theory](https://doi.org/10.5281/zenodo.19646969): guide to the structure of the framework.

[Comparative Clarifications and Distinctions for the Theory](https://github.com/k-osmolovskyi/k-osmolovskyi.github.io/blob/main/ref/conceptual-bridges.md): comparative clarification note.

---

## Formalizations
The theory framework has its own internal evolution. Below is an auxiliary list indicating the order corresponding to the stages in which the papers emerged. Please use this sequence as a guide in order to follow the natural direction of the formal development.

No.          | Paper                                                                               | Role
------------ | ----------------------------------------------------------------------------------- | -------------
TR_26/1      | [General Theory](https://doi.org/10.5281/zenodo.19467207)                           | unifying language, layered admissibility principle
TR_26/2      | [Coherence Evaluation](https://doi.org/10.5281/zenodo.19467770)                     | geometry: coherence as distance to stability region
TR_26/3      | [Structural Admissibility](https://doi.org/10.5281/zenodo.19467881)                 | structural admissibility operator, phase space, level as geometry
TR_26/4      | [Overload Formation](https://doi.org/10.5281/zenodo.19467913)                       | compensability threshold, instantaneous overload, memory
TR_26/5      | [Trajectory-Dependent Regulation](https://doi.org/10.5281/zenodo.19468033)          | hysteresis, drift to boundary, concentration near minimal overload
TR_26/6      | [Identity as a Regulatory Attractor](https://doi.org/10.5281/zenodo.19476667)       | identity-core as cost-separated low-overload attractor
TR_26/7      | [Invariants](https://doi.org/10.5281/zenodo.19480011)                               | axiomatic core, interaction structure, invariant-induced geometry
TR_26/8      | [Structural Compression](https://doi.org/10.5281/zenodo.19481795)                   | compression vs. simplification; level-preserving vs. level-forming
TR_26/9      | [Emergence of Coherence Representation](https://doi.org/10.5281/zenodo.19488084)    | order-preserving regulatory variable under partial observability
TR_26/10     | [Coherence Representation in Multi-System](https://doi.org/10.5281/zenodo.19493294) | order alignment, co-regulation without shared geometry
TR_26/11     | [Pre-Symbolic Admissibility](https://doi.org/10.5281/zenodo.19499593)               | pre-representational filtering of discrepancies that determines which signals can enter regulation
TR_26/12     | [Restricted Accessibility of Coherence](https://doi.org/10.5281/zenodo.19508182)    | geometric coherence exists globally; regulatory access is domain-constrained
TR_26/13     | [Inter-System Conflict Geometry ](https://doi.org/10.5281/zenodo.19509685)          | conflict as incompatibility of admissibility structures

---

## Verification Package for the Theory
Set of companion documents designed to support external verification of the General Theory of Cognitive Structuring. Together, these documents are intended to reduce accidental misreading, make the dependency structure of the series explicit, and simplify formal and conceptual verification across the paper sequence.

No.          | Doc/Paper                                                                                                                | Role
------------ | -------------------------------------------------------------------------------------------------------------------- | -------------
TN_26/1      | [Parametric Realizations of Coherence](https://doi.org/10.5281/zenodo.19656664)                                      | Minimal computational template
Simul.       | [trajectory_regulation_v2.py](https://colab.research.google.com/drive/1nygtv6vDgfWVdMngZ6W8FBb9xfG2to12?usp=sharing) | Minimal python simulations

No.          | Paper                                                                                   | Role
------------ | --------------------------------------------------------------------------------------- | -------------
TN_26/2      | [Glossary of Core Terms](https://doi.org/10.5281/zenodo.19689203)                       | Interpretive glossary for core terms
TN_26/3      | [Acyclicity Statement and Dependency Criteria](https://doi.org/10.5281/zenodo.19701824) | Dependency criteria and non-circularity statement
TN_26/4      | [Dependency Tables and Node Registry](https://doi.org/10.5281/zenodo.19701847)          | Node registry and paper-level dependency map
TN_26/5      | [Technical Appendix](https://doi.org/10.5281/zenodo.19701876)                           | Notation, assumptions, and formal traceability
TN_26/6      | [How to Verify](https://doi.org/10.5281/zenodo.19701901)                                | Reading order and verification roadmap
TN_26/7      | [External Verification Checklist](https://doi.org/10.5281/zenodo.19701915)              | Practical checklist for external review
TN_26/8      | [Minimal Claims Register](https://doi.org/10.5281/zenodo.19701933)                      | Compact register of the theory’s main claims

## Proof-Oriented Documents
This block provides the proof-support layer of the General Theory of Cognitive Structuring. It includes collected results, normalized propositions and theorems, a proof-status register, a package overview, and author-side proof notes. Together, these documents are intended to stabilize the canonical result layer of the series, distinguish proof-ready results from sketch-level ones, and prepare later proof-compendium development.

No.          | Doc/Paper                                                                          | Role
------------ | ---------------------------------------------------------------------------------- | -------------
VR_26/1      | [Collected Results and Proof Status Note](https://doi.org/10.5281/zenodo.19705593) | Collected result layer with proof-status classification
VR_26/2      | [Collected Propositions and Theorems](https://doi.org/10.5281/zenodo.19705677)     | Normalized collection of propositions and theorems
VR_26/3      | [Proof Status Register](https://doi.org/10.5281/zenodo.19705731)                   | Compact register of proof readiness and consolidation status
VR_26/4      | [Verification Package Overview](https://doi.org/10.5281/zenodo.19705772)           | Front overview of the verification and proof-support package
VR_26/5      | [Proof Notes](https://doi.org/10.5281/zenodo.19705808)                             | Author-side proof logic and compendium preparation notes
DAG          | [Digraph GTCS Dependencies](https://shorturl.at/VzUGG)                             | DAG visualization

---

## Phenomenology Branch

No.          | Paper                                                                                                                       | Role
------------ | --------------------------------------------------------------------------------------------------------------------------- | -------------
TR_26/14     | [Inner Manifestation Beyond Admissible Processing](https://doi.org/10.5281/zenodo.19583268)                                 | establishes that inner manifestation exceeds currently admissible enacted processing and is not exhausted by live continuation alone
TR_26/15     | [Manifest Trajectory Accessibility in Cognitive Systems](https://doi.org/10.5281/zenodo.19760215)                           | formalizes trajectories as explicit objects of manifestation and distinguishes manifest, admissible, and realized continuation
TR_26/16     | [Minimal Directional Organization of Coherence-Related Manifestation](https://doi.org/10.5281/zenodo.19760414)              | formalizes the minimal positional/directional grammar of manifestation and shows that positivity is directional rather than a property of stable occupancy
TR_26/17     | [Identity-Bounded Continuation and Non-Enactable Manifestation](https://doi.org/10.5281/zenodo.19789471)                    | formalizes identity-bounded continuation as distinct from broader manifest continuation and shows that current continuation may narrow through both non-admission into enactment and non-discrimination of trajectories
TR_26/18     | [Perceptual Stabilization through Historically Compressed Processing Organization](https://doi.org/10.5281/zenodo.19814865) | formalizes perception as stabilization of incoming signal through historically compressed processing organization and shows that partial match, unclear perception, false completion, and historically differentiated perception are lawful outcomes of one signal-general architecture.
TR_26/19     | [Architectural Conditions Coherence Acquires Affect-like](https://doi.org/10.5281/zenodo.19857878)                          | clarifies how the already established coherence representation functions as compressed affect-like significance of state and directionality across inner manifestation, without introducing a new affect-domain.
TR_26/20     | [Symbolic Capture of Manifestation](https://doi.org/10.5281/zenodo.19895497)                                                | distinguishes manifestation from symbolic articulation by defining symbolic capture as a selective downstream fixation of part of manifestation and showing how such fixation changes later regulatory availability through reuse, comparison, reactivation, and transfer

---

### Concept Papers

- [Cognitive Evolution Beyond the Single Life Cycle](https://doi.org/10.5281/zenodo.19673721) — *Preprint*
- [Structural Updating and the Limits of Cognitive Change](https://doi.org/10.5281/zenodo.19545676) — *Preprint*
- [Coherence Evaluation, Feelings, and Emotions: The Felt Layer of Regulation](https://doi.org/10.5281/zenodo.19588489) — *Concept Paper*
- [Beyond Output Correction: Recursive Access, Structural Regulation, and AI Safety](https://doi.org/10.5281/zenodo.19797101) — *Concept Paper*

---

Currently seeking arXiv endorsement in the **cs.AI (Artificial Intelligence)** category in order to submit my work there. If you are able to endorse submissions in this category, or could help me navigate this step, please feel free to contact me by email. I would be very grateful for any assistance.
[https://arxiv.org/auth/endorse?x=Q6E93A](https://arxiv.org/auth/endorse?x=Q6E93A)

---

  Kostiantyn Osmolovskyi (Independent Researcher, Odesa, Ukraine) | M.S. Public administration, *National Polytechnic University OD, UA* | B.S. Psychology, *I. I. Mechnikov National University OD, UA*
  
- ORCID: 0009-0006-3144-7237
- Contact: constantinosmol@gmail.com

---

This framework was developed, formalized, and openly published by **Kostiantyn Osmolovskyi**. All technical reports, mathematical definitions, axiomatic structures, simulation code, and conceptual distinctions within this community are original works hosted at: | [Zenodo](https://zenodo.org/communities/gtc) | [ORCID](https://orcid.org/0009-0006-3144-7237)

This content is licensed under [CC BY 4.0](LICENSE).

When referencing, training AI models, or integrating concepts from this framework, please cite the corresponding Zenodo DOIs and attribute the author to preserve academic provenance. Example:
> Osmolovskyi, K. (2026). Structural Admissibility in Cognitive Systems (1.0). Zenodo. https://doi.org/10.5281/zenodo.19467882
