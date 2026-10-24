# Veteran Fighter — mechanical balance audit

**7 October 2026 · revised 2024 / 5.5e rules · Public Test 1, proposed testing build**

> “A new fighter learns the proper way to fight. A Veteran has learned when the proper way is the wrong way.”

This is an independent quantitative and rules-interaction audit. The accompanying workbook has twelve requested areas, live formulas, explicitly marked external policy tables, and a refresh script. The calculation bundle contains exact expected-value models, a full-dice simulation, intermediate outputs, source notes, and independent checks. Mathematical precision applies to specified scenarios; it does not turn encounter availability or DM judgments into measured facts.

## A. Executive verdict

**Overall: Strong but Acceptable, moderate confidence, suitable for instrumented playtesting without an evidence-supported numerical nerf.** This means defensibly inside the broad revised Fighter envelope under the disclosed comparisons. It does not mean equal performance across subclasses, immunity to optimization, or a demonstrated ceiling under every legal item/party combination.

The ordinary contact engine is notably front-loaded. At level 3 it increases the controlled greatsword chassis from 7.90 to 12.30 repeatable damage, with no Bonus Action. In a fresh four-round encounter including Surge, Veteran averages 15.38 versus optimized Precision/Trip Battle Master 14.96 and first-hit Psi 14.47; a plausible Battle Master reaction opportunity changes the ordering. Veteran gains an attrition advantage when dice run out. That is a meaningful strength, rather than evidence by itself of an excessive subclass.

Three interacting packages deserve the greatest attention: **own-turn Hair Trigger**, **Readiness/Study/Weak Point**, and **the full-duration level-18 mark**. Weak Point can become too generous under a routinely permissive interpretation of “exploits the weakness”; its evidence gate is a substantive condition, not permission to assume that every attack always qualifies. Hair Trigger is a legal Reaction-for-damage trade with high pick pressure. The capstone is strongest against one exposed boss and much weaker when the marked enemy is irrelevant or Advantage is already supplied.

No empirical playtest pick rates or representative monster distributions are available. Accordingly, no universal mandatory-pick claim, global numerical balance threshold, or precisely weighted utility score is asserted.

| Breakpoint | Classification | Confidence | Principal qualification |
| --- | --- | --- | --- |
| 3 | Strong but Acceptable | Moderate | Reliable contact plus four choices; adjacency and control requirements matter; clear low-rest advantage |
| 7 | Strong but Acceptable | Moderate–low | Own-turn Hair adds about 5.20 damage but spends Reaction; Readiness resolves on first turn |
| 10 | Strong but Acceptable | Moderate–low | Study/Weak Point can exceed this verdict with broad, routine qualification and valuable allied packets |
| 15 | Within Expected Range | Moderate | New package is useful conditional attrition support; BM Relentless is a stronger repeatable offense jump |
| 18 | Strong but Acceptable | Moderate–low | Upper-envelope combined boss offense/defense; existing Advantage, multiple threats and initial exposure reduce it |

The level-15 classification describes the complete character at that breakpoint, with a comparatively modest new subclass feature. In a no-adjacency/no-secondary-target environment, individual Veteran builds may be Slightly Underpowered. In a permissive optimized support environment, the level-10+ package may be Slightly Overtuned. These are scenario classifications, not an average of incompatible assumptions.

## B. Authority, sources, rules and methods

### B1. Project authority

All four requested named sources were located and read before rules research and new calculations. Public Test 1’s opening explicitly calls it a recommended, proposed player-facing release. No newer explicitly adopted testing build was identified in the retrieved project record. The audit therefore uses **the proposed Public Test 1 build**, rather than declaring all prior recommendations project canon.

| Source | Status / identity | Use in this audit |
| --- | --- | --- |
| Veteran_Public_Test_1.md | Complete, 228 lines, 19,302 bytes; libfile_6d63ed048030819185c8c36d14ececcd; dated 2026-10-05 | Mechanical subject; complete wording governs |
| Veteran_Fighter_Comprehensive_Current_State_Report_2026-10-05.md | Complete; libfile_4522958325388191811d56e563a5b756 | Historical hierarchy, accepted intent and rejected experiments |
| Veteran_Fighter_Pre_Playtest_Audit_2026-10-05.md | Complete; libfile_652c28d762888191b9d7ab4b22d1dd09 | Hypotheses and results independently checked |
| Veteran_Audit_Calculations_2026-10-05.zip | Complete; libfile_e614593c67bc81918a0f30e7da528714 | Both scripts executed; numeric JSON outputs reproduced identically |
| Older chats/reports | Not all retrieved; not asserted read | Comprehensive report’s hierarchy suffices for this mechanical subject |
| Newer adopted build | Not identified | Would supersede this subject if explicitly supplied |

The verified fingerprint matches the user’s summary: 4/5/6/7/8 known Lessons; thirteen base selections, two at 7, five at 10; Deliver/Misdirect and Distract/Takedown are merged selections. Open the Lane, Spoil the Reaction and Suppressing Fire are absent. The level-15 feature is Still in the Fight. No historical 22-concept roster or older No Lesson Wasted package is combined with this text.

Material differences from older analysis are costs and boundaries already present in Public Test 1: closed physical replacement procedures, ordinary attack slots, shared PF use per eligible action, no inherited implement benefits, reserved access limited to a declared use, explicit Fighter-only Ready attack count, genuine sabotage, and actual barricade materials. The mark’s duration includes enemy turns. The file requires visibility when selecting; it does **not** say later loss of visibility terminates the mark. Ordinary unseen-target attack restrictions still apply and can cancel its Advantage.

### B2. Rules verification and boundaries

The live official PHB errata and official April 2025 PDF were checked alongside current basic rules. The live page governs over a stale PDF. The March 2026 edition-label change to “5.5e” is not treated as a mechanical rewrite. No later applicable PHB balance change was located in this research; this is a dated verification, not a claim to have inspected every inaccessible publication. [R1–R5]

The chassis audit uses revised Second Wind (2/3/4 uses at 1/4/10, one back per Short Rest, all per Long Rest), Tactical Mind, Shift, Master, Studied Attacks and Indomitable. Surge adds an action excluding Magic; at 17 its two uses must occur on different turns. Ordinary attacks are 1/2/3/4 at Fighter 3/5/11/20. Revised ASIs and Mastery progression are used. [R1, R6]

Attack/critical probabilities include natural20 hits and natural1 misses. Advantage and Disadvantage cancel regardless of counts. Saves/checks do not automatically fail on natural1. Unarmed Grapple/Shove use the target’s choice of Strength/Dexterity save; practical Dexterity damage does not replace their Strength DC. Grapple needs a free hand; Shove does not. Ordinary size limits and immunities remain. Forced movement alone does not provoke an OA. Ready’s trigger must be perceptible and resolves after it finishes. [R2]

Equipment checks preserve the important distinctions: equip/unequip permission accompanies an actual attack; Loading limits the same crossbow without its feat; ammunition and free hands matter; Nick is once per turn; Reach does not extend Contact; Graze has only its specified ability damage; Vex and Studied entitlements stay with their target. Cleave is once per turn with target geometry; Push/Sap/Slow/Topple retain their size, timing or save restrictions. [R3]

Haste’s extra Attack action is expressly one attack: no PF, replacement procedure, or extra Nick through that action. Its Disengage or Utilize choices can still receive compatible Lessons, including Parting Blow or eligible physical Sabotage. That is a different named action, not bypassing the Attack limitation. One spell slot may be spent to cast a spell per turn; Surge does not authorize a second Magic action. [R11–R12]

Relevant revised feats/styles were checked individually, including GWM’s Strength prerequisite and +1 Strength, Grappler, Tavern Brawler, PAM, Sentinel, Shield Master, Dual Wielder, Charger, Crossbow Expert, Archery, Defense, Dueling, TWF, Thrown, GWF and Unarmed Fighting. Sharpshooter is considered for range/cover/close-pressure relief, without importing legacy −5/+10. Protection now covers the triggering and subsequent attacks against its protected ally while adjacency persists; Interception competes for the same Reaction. [F1–F15]

Legacy supplement options such as Booming Blade, Green-Flame Blade and Shadow Blade are optional revised-compatible supplements, not assumed in the default PHB model. Their edition eligibility, weapon requirements, concentration, actual trigger or movement damage and ability allocation must be declared before comparing them. No 2014 grapple checks, surprise turns, PAM opportunity-attack wording, smite freedom or Action Surge spellcasting are imported.

### B3. Separate unresolved readings

| Reading | Audit treatment | Consequence |
|---|---|---|
| Own-turn Ready | Legal when a perceptible trigger finishes on that turn; own movement is a concrete example | Hair preserves on-turn PF/Nick/GWM if requirements hold; this is a power interaction, not an invented exploit |
| Hair’s “one of these attacks” and generated PF | Conservative numbered weapon/US volley only for bonus die | Allowing generated Contact as the eligible die hit can increase hit assurance; test separately |
| TWF and Dual Wielder additional attack | Adopt the applicable “as a result of Light” reading used by current builds | A narrow table ruling reduces dual-wield totals; it does not remove PF’s ability-modifier prohibition |
| Weak Point qualification | Evidence and exploitation adjudicated, one shared benefit each turn | Model successful narrow qualification separately from broad near-universal qualification |
| Physical one-action feasibility | Real materials/tools/geometry and task duration govern | FET/Barricade/Sabotage are not arbitrary-action substitutes |
| Misdirect and passive hearing | Do not invent an active check or universally apply to passive detection | Record how the table treats its first hearing-based check; exact tactical frequency unresolved |
| Simultaneous immediate after-hit triggers | Apply compatible features in a legal declared order; no extra attacks inferred | Grappler/Shield Master/PF sequencing should be logged when the table disputes timing |

### B4. Analytical frameworks

| Framework | Established method and adopted assumptions | Limit |
| --- | --- | --- |
| Fixed accuracy | Expected-value branches: p=.50/.60/.65/.70/.80; ordinary crit .05; Advantage 1−(1−p)^2, crit .0975; same resources/policies. [M1–M3] | Normalized p is the before-Archery benchmark; +2 Archery still adds actual accuracy. Not identical final accuracy across styles |
| Legal bonus / AC sweep | Actual PB + legal primary modifier + item/style bonus; AC10–26 for GS, bow and Vex melee at all eleven levels | Independent AC sensitivity; convenience monster ACs are scenario anchors, not a population fit |
| Finite sequential expectation | Exact d20 enumeration with target-specific entitlements, crits, Contact insertion, miss correction and expiration across four turns | Exact for declared policy, not an exhaustive search over every weapon switch, kill or movement path |
| Resource horizon | 3/4/5-round fresh encounter; 3 encounters with 0/1/2 scheduled Short Rests; surge early; BM finite-horizon Precision/Trip/no-spend choices | Known AC is a favorable BM information assumption; later spending/defensive reserves change outputs |
| Day-normalized comparison | 12-round/3-encounter/1-SR schedule is a transparent current calculator convention, also varied here. [M4] | Not asserted to be the universal adventuring day |
| Scenario/geometry accounting | Exposure, cover, extraction, objective completion, actual healing, enemy clearance and party packets | No fabricated DPR or utility score assigned to movement/surrender/fieldcraft |
| Full-dice simulation | 200,000 trials, seed20261007, full d6 damage for a Studied attack sequence; separate HP/overkill cases 100,000 each | Monte Carlo uncertainty reported; mean-damage exact models are not damage distributions |

RPGBOT’s older fundamental-math argument remains usable as a hit-probability convention after replacing its rules/builds; it is not independent 2024 empirical validation. Its historical AC progression and the chosen early Fighter ASIs do not always yield 65% here. Tabletop Builds’ branch/resource reasoning is retained, not its legacy character packages. The current calculator’s day convention is adopted with our own sequential formulas rather than opaque site outputs. Treantmonk benchmarks whose exact current inputs were not established are not used as numerical authorities.

**Independent computation:** Wolfram Language was available and used for rational probability and break-even checks. Python direct d20 enumeration and separate closed-form checks agree: Contact 57/10, Hair two-attack bonus 2079/400, three-attack Distract gain for a 2d6+5 packet 8918049/2560000, and three dragon Rends prevented 4761/400. The full-dice Monte Carlo mean is 47.65560 ±0.03755 (approximate 95% mean interval), versus exact 47.65822; standard error .01916 and z=−.137. This sequence is a fresh, no-GWM, no-capstone level-20 GS–Contact–GS–GS–GS turn with Studied. Earlier simulation used mean damage dice; this one rolls them.

### B5. Accessible revised-monster scenarios

Four intentionally selected accessible revised stat blocks test reach, size, saves, immunities and boss damage. This is a convenience sample, **not representative Monster Manual data**. It is not enough to infer “typical” targets or save distributions. CR is not identified with Fighter level. [N1–N4]

| Monster / source edition | CR / AC | Attack bonus / profile | STR / DEX saves | Consequential limits |
| --- | --- | --- | --- | --- |
| Air Elemental, revised | 5 / 15 | +8; 10-ft reach; Thunder 2d8+5 | +2 / +5 | Grappled/Prone immune; BPS resistance; flight/Whirlwind |
| Hill Giant, revised | 5 / 13 | +8; two attacks; club 3d8+5 | +5 / −1 | Huge: Medium ordinary US cannot grapple/shove; club hit causes Prone without a save |
| Frost Giant, revised | 8 / 15 | +9; axe 2d12+6+2d8 cold | +6 / −1 | Huge; cold immune; War Cry supplies temporary attack Advantage |
| Adult Red Dragon, revised | 17 / 19 | +14; three Rends, 18.5 mean; breath DC21, 17d6 | +8 / +6 | Huge; natural attacks cannot be disarmed; flight; legendary resources |

For these four only: AC mean15.5, median15, range13–19; selected attack-bonus mean9.75, median8.5, range8–14; better STR/DEX save mean6, median5.5, range5–8. Attack counts, natural attacks, defenses and flight are at least as important as those averages. No protected full stat blocks are redistributed.

## C. Quantitative benchmarks

### C1. Declared legal builds

The controlled featless progression uses primary16 at3,18 at5,20 from7. The optimized paths begin at17 and spend legal ASIs: GS GWM4 then primary20 at6; polearm PAM4/GWM6 then20 at8; dual wield DW4 then20 at6; Dexterity rapier primary20 at6; bow STR13 before GWM4 (+1 STR), DEX17→19 at6→20 at8; heavy crossbow XBE4/GWM6/DEX20 at8; thrown DW4, Thrown style, primary20 at6. Sword/shield uses Dueling and legal primary increases; mixed warhammer keeps a free hand. No build receives both a primary half-feat and an unrelated free +1 primary. Monk-compatible sequences require their own restrictions.

Only one initial style is granted. Champion receives its additional style at7 (GWF while retaining Defense in GS comparisons). Primary20 remains a controlled high-level assumption: matched Epic Boons can be added, but these tables do not claim the maximum possible level-19/20 build or grant a free22 stat.

Build-family tables are no-item scenarios. Weapon +1/+2/+3 and qualifying dice riders are separately swept against actual AC. Held-implement Contact never inherits them. No target deaths, Cleave second targets, kill-Hew, Charger geometry or assumed reaction attacks are credited automatically.

### C2. Fresh four-round GS comparison, same accuracy/resource environment

All columns include one Surge before17, two on different turns from17. GWM applies from level4. BM’s modeled Trip failure=.50, target eligible and recoverable at its turn; Precision sees AC and the missed d20. Psi uses INT3, first-hit Strike within30, separate damage not doubled on crit. EK INT3 uses legal True Strike when better than its ordinary attack; this is an **offensive floor**, not its complete spell/defense value. Champion uses first-miss Inspiration from10 and GWF from7. No Hew in this first table, for any column.

| Level | Veteran | Champion | BM opt | BM no Trip | Psi INT3 | EK INT3 floor | EK INT5 bound |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 15.38 | 10.31 | 14.96 | 14.78 | 14.47 | 9.88 | 9.88 |
| 5 | 33.44 | 28.00 | 34.80 | 33.84 | 33.91 | 27.13 | 27.13 |
| 7 | 36.75 | 32.38 | 38.77 | 37.53 | 36.41 | 29.63 | 32.69 |
| 9 | 38.37 | 34.00 | 40.85 | 39.61 | 38.03 | 31.25 | 34.31 |
| 10 | 38.37 | 39.49 | 42.01 | 40.70 | 38.03 | 31.25 | 34.31 |
| 11 | 54.00 | 57.67 | 59.66 | 57.43 | 55.10 | 48.25 | 53.00 |
| 13 | 60.27 | 62.75 | 64.41 | 62.12 | 60.88 | 54.84 | 59.25 |
| 15 | 60.27 | 64.75 | 72.01 | 68.41 | 60.88 | 54.84 | 59.25 |
| 17 | 75.56 | 80.62 | 88.39 | 83.46 | 75.61 | 72.53 | 78.44 |
| 18 | 88.61 | 80.62 | 90.01 | 84.92 | 75.61 | 72.53 | 78.44 |
| 20 | 114.24 | 105.95 | 115.90 | 108.42 | 97.73 | 94.60 | 100.54 |

INT5 is an explicitly favorable allocation bound, not free Intelligence20 alongside the same Strength progression and feats. INT16 at level3 alongside STR17 is possible under point buy/background allocation with low other scores; it carries defensive and skill trade-offs. EK’s realistic damage floor is lower than Veteran’s in several rows, but Shield, control, mobility and slot spells materially change the package comparison. Do not infer EK subclass inferiority from this column.

**Crit-triggered Hew cross-check:** correlated criticals, one BA, no kills, no Contact-triggered Hew. Champion’s wider critical range receives its actual advantage. Other comparator columns above exclude Hew and are therefore not upper offensive bounds.

| Level | Veteran + Hew | Champion + Hew | Interpretation |
| --- | --- | --- | --- |
| 3 | 15.38 | 10.31 | Same four-round fresh environment; no other BA competition |
| 5 | 34.50 | 30.11 | Same four-round fresh environment; no other BA competition |
| 7 | 37.93 | 34.89 | Same four-round fresh environment; no other BA competition |
| 9 | 39.56 | 36.51 | Same four-round fresh environment; no other BA competition |
| 10 | 39.56 | 42.81 | Same four-round fresh environment; no other BA competition |
| 11 | 55.71 | 61.99 | Same four-round fresh environment; no other BA competition |
| 13 | 62.53 | 67.79 | Same four-round fresh environment; no other BA competition |
| 15 | 62.53 | 71.85 | Same four-round fresh environment; no other BA competition |
| 17 | 78.21 | 88.41 | Same four-round fresh environment; no other BA competition |
| 18 | 92.89 | 88.41 | Same four-round fresh environment; no other BA competition |
| 20 | 119.54 | 114.83 | Same four-round fresh environment; no other BA competition |

### C3. Required benchmark format and complete packages

The following selected level-11 cases keep costs visible. Off-turn quantities are conditional scenarios; ordinary on-turn DPR does not already contain them. “Encounter” includes Surge and the stated fresh resources. “Nova” is a one-turn weapon output where calculated, not an item/party total.

| Build / model | On-turn DPR | Expected off-turn DPR | Encounter average | Nova | Control | Defense | Resources / costs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Veteran GS | 43.20 | 0.00 | 54.00 | 86.40 | Optional Contact save; Tactical Master | Readiness; full chassis | Adjacency; no BA/Reaction assumed |
| Veteran own-turn Hair | 48.87 | 0.00 | ≈base encounter +5.67 | Ready+Surge Attack; only one Reaction | Contact remains legal | Reaction defense foregone | One Lesson, perceptible own-turn trigger; no Hew credited |
| Champion GS | Policy-dependent | 0.00 | 57.67 | Resource/Hew timing dependent | Masteries | Extra style, crit movement, initiative; later Survivor | Inspiration every turn; no dice depletion |
| BM GS Precision/Trip | Policy-dependent | 0 in base | 59.66 | Exact finite-horizon policy | Trip=.50 fail; ally/control alternatives | Parry/Bait/Evasive alternatives | 5d10 fresh; all dice SR/LR; defense competes |
| BM with .50 Riposte event | Policy-dependent | Policy-dependent included in average | 61.37 | Not added again | Same target/control limits | Reaction cannot also Parry/OA | Dice consumed even on Riposte miss |
| Psi GS INT3 | First-hit policy | 0.00 | 55.10 | One Strike per turn, not per action | Thrust save; not included as free DPR | Protective Field/Guarded Mind | 8d10; one die SR; protection spends same pool |
| EK GS INT3 floor | Cantrip policy | 0.00 | 48.25 | Additional spells not priced in floor | Eldritch Strike and real spells | Shield/other spells, slots, hands | INT and slots; no arbitrary spell nova |
| Veteran longbow focused | 34.87 | 0.00 | 43.58 | 69.73 | Slow/Tactical Master; movement | Safe movement if path useful | One durable target; first-miss policy |
| Veteran longbow split | 37.65 | 0.00 | 47.06 | 75.30 | Secondary target entitlement separate | Movement not assigned DPR | Distributed total; different creature after hit |

**Complete official feature context:** Champion adds athletic/initiative Advantage, critical movement, a second style, Inspiration, 18–20 criticals and Survivor’s death-save benefits/5+CON Bloodied healing. BM has skills/tools, tactical knowledge, ally attacks, control, damage/accuracy and reaction/defensive alternatives; at15 Relentless is once per **turn**, including an eligible off-turn maneuver. Dice sizes/counts are 4d8 at3,5d8 at7,5d10 at10,6d10 at15,6d12 at18. [R1, R7]

EK has bonded weapons, realistic INT/slots, War Magic, Eldritch Strike, Surge teleport and level18 replacement of two attacks with a level1/2 action spell. Shield’s +5AC can protect against multiple enemies for a round; it costs a Reaction/slot and usable components. Slot limitation prevents two slot-spell casts on one turn even when spell replacement is legal. [R8, R11, R13]

Psi’s pool/size progresses 4d6/6d8/8d8/8d10/10d10/12d12 at3/5/9/11/13/17. It restores one die/SR, all/LR. Strike is once on its own turn within30. The same pool funds Reaction protection. It also has transport, a limited/replenishable BA flight burst, Thrust, psychic defense/condition removal, multi-ally cover at15, and Telekinesis with BA weapon attacks at18. Those powers are not exhausted away to favor Veteran. [R9]

### C4. Repeatable build-family offense

Four-turn average with carried Vex/Studied, no Surge or subclass resources, no reaction attacks. Ability rows and target mode are explicit in CSV/workbook. Contact timing is best among the enumerated fixed ordinary-weapon insertion positions; it is not a global adaptive weapon-switch policy. Nick once per turn and DW/PAM BA are included where legal. Archery adds +2 over normalized ordinary accuracy. Polearm assumes adjacency here; its contact disappears at10ft without another adjacent creature.

| Level | GS | Shield | Pole | Dual | DEX Vex | Bow focus | Bow split | Xbow focus | Thrown split | Free hand |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 12.30 | 10.80 | 11.25 | 14.27 | 11.87 | 6.75 | 9.45 | 6.65 | 13.83 | 9.50 |
| 5 | 26.75 | 19.15 | 26.50 | 29.13 | 22.34 | 18.76 | 22.05 | 16.73 | 27.92 | 16.55 |
| 7 | 29.40 | 21.10 | 30.40 | 32.85 | 24.62 | 20.26 | 23.55 | 22.21 | 29.54 | 18.50 |
| 9 | 30.70 | 21.10 | 35.35 | 32.85 | 24.62 | 23.59 | 27.30 | 25.54 | 29.54 | 18.50 |
| 10 | 30.70 | 21.10 | 35.35 | 32.85 | 24.62 | 23.59 | 27.30 | 25.54 | 29.54 | 18.50 |
| 11 | 43.20 | 28.80 | 46.80 | 40.31 | 34.64 | 34.87 | 37.65 | 37.73 | 38.80 | 24.90 |
| 13 | 48.19 | 31.66 | 51.66 | 43.01 | 36.82 | 39.10 | 42.32 | 42.12 | 40.86 | 27.39 |
| 15 | 48.19 | 31.66 | 51.66 | 43.01 | 36.82 | 39.10 | 42.32 | 42.12 | 40.86 | 27.39 |
| 17 | 50.33 | 31.66 | 53.79 | 43.01 | 36.82 | 41.91 | 45.46 | 44.94 | 40.86 | 27.39 |
| 18 | 59.07 | 39.39 | 62.12 | 46.80 | 39.39 | 46.72 | 53.65 | 50.01 | 42.72 | 34.13 |
| 20 | 76.16 | 49.92 | 77.75 | 54.60 | 49.92 | 62.22 | 68.70 | 66.60 | 52.28 | 42.90 |

These are competent legal paths, not a ranking of maximum subclass builds. The strong pole/dual values include feats and BA attacks that the sword/shield or mixed profile spends on other benefits. The melee contact EV does not scale with weapon dice or its magic. Thrown sequencing is now stateful and includes Nick/DW; it is not the prior approximate extra-shot overlay. The policy can always decline a bad optional follow-up.

### C5. Encounters, rests and attrition

The full CSV contains every required level, 3/4/5 rounds and 0/1/2 SR. Below are three four-round encounters; one SR occurs after encounter1, two after encounters1 and2. New enemies reset target entitlements. Surge is used as early as available. BM optimizes finite resources; Psi spends first-hit dice, with only one die restored per SR. No Long Rest occurs until after all three encounters. Healing, protection and utility reserve spending are excluded from these offensive allocations and examined separately.

| Level | SR | Veteran | Champion | BM opt | BM + .50 Riposte | Psi INT3 |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | 0 | 13.32 | 8.94 | 10.55 | 12.18 | 10.72 |
| 3 | 1 | 14.35 | 9.63 | 12.77 | 15.13 | 11.92 |
| 3 | 2 | 15.38 | 10.31 | 14.96 | 17.58 | 13.10 |
| 11 | 0 | 46.80 | 50.58 | 45.35 | 46.30 | 46.29 |
| 11 | 1 | 50.40 | 54.12 | 52.56 | 54.00 | 50.12 |
| 11 | 2 | 54.00 | 57.67 | 59.66 | 61.37 | 53.95 |
| 18 | 0 | 68.92 | 63.57 | 65.02 | 71.96 | 60.86 |
| 18 | 1 | 78.76 | 72.10 | 77.57 | 84.53 | 68.23 |
| 18 | 2 | 88.60 | 80.62 | 90.01 | 96.98 | 75.61 |
| 20 | 0 | 88.85 | 83.54 | 84.10 | 91.05 | 78.08 |
| 20 | 1 | 101.55 | 94.74 | 100.07 | 107.03 | 87.91 |
| 20 | 2 | 114.24 | 105.95 | 115.90 | 122.87 | 97.73 |

Longer encounters dilute fresh BM/Psi dice and Surge; Veteran’s ordinary PF and capstone continue. Short Rests restore BM’s whole dice pool but only one Psi die. Veteran’s reserve use and one Second Wind restore separately. Champion Inspiration continues every turn. BM Relentless prevents a high-level “resource-empty BM” from becoming a plain chassis. Thus Veteran’s low-rest lead at3 and18 is real under these assumptions but not universal.

## D. Features, Lessons and opportunity costs

### D1. Core feature findings

| Feature | Rating | Finding |
|---|---|---|
| Hard-Won Lessons | Strong | Four selections initially are generous, but most are conditional action modifiers; selection pressure is real and all twenty are never simultaneously known |
| Practical Experience | Appropriate | One proficiency plus Expertise supports the intended fieldcraft; increases an unclamped ordinary success chance by PB/20 over proficiency |
| Practical Contact | Strong | Reliable STR/DEX damaging strike; no weapon item/mastery inheritance; weak STR still produces a weak ordinary grapple/shove DC |
| Close Work | Strong | Repeatable added damage or save-based control without a BA; requires5ft and respects hand/size/immunity constraints |
| Hit or Correct | Strong | Focused catch-up is conditional; split total and retained legal flat/dice riders can be substantial; movement has separate geometry value |
| Battlefield Readiness | Appropriate | Two opening options, but three resolve on first turn rather than before enemies; small THP and contingent information/movement |
| Change of Approach | Appropriate | One rest swap, not instantaneous catalogue access; hour-long Short Rest is a genuine information/time boundary |
| Reserve Lessons | Strong | Two preselected unknown contingencies, one shared use/SR; persistent resulting effects are allowed without permanent knowledge |
| Reserve Readiness | Appropriate | Later unused option offers flexibility, not all four opening choices; can recover a missed opportunity when combat changes |
| Dig Deep | Appropriate | Preserves one BA on a Surge turn while spending Second Wind; actual missing HP and a real alternative BA govern value |
| Improved Brace | Appropriate | 10/12THP in tiers3/4 is useful attrition support; one useful grant, no adding successive THP pools |
| Veteran of a Hundred Fights | Strong | Whole-cycle combined offense/defense/saves against one visible-at-selection creature; upper-envelope boss package, not merely DPR |

### D2. Contact, control and sequencing

For one damaging d6 Contact, EV is p×(3.5+modifier)+crit×3.5. With modifier5 the accuracy sweep is:

| Ordinary p | Contact EV | Advantage hit p | Advantage Contact EV |
| --- | --- | --- | --- |
| 0.50 | 4.42 | 0.75 | 6.72 |
| 0.60 | 5.28 | 0.84 | 7.48 |
| 0.65 | 5.70 | 0.88 | 7.80 |
| 0.70 | 6.12 | 0.91 | 8.08 |
| 0.80 | 6.97 | 0.96 | 8.50 |

At level3/modifier3 the corresponding .65 EV is4.40. Contact is not “weapon DPR times an extra attack”: Dueling, GWM, +3 weapons and weapon fire dice do not attach to it. Global qualifying riders, such as Rage using Strength or Hunter’s Mark’s attack-roll rider, may apply under their own rules. The held haft/shield/pommel is narration, not a weapon-property loophole.

A normal grapple/shove requires only the save, not an attack-roll hit. With DC17 and the enemy’s better save+5, success=.55. With better save+11, success=.25. A Dexterity20 Veteran with Strength8 has ordinary DC11 at PB4: against+5 success=.25 despite .65 contact accuracy. Grappler’s Damage+Grapple first requires a hit and then a failed save: .65×.55=.3575 in the STR case, .1625 in that low-STR case. It is once per turn on an eligible own-turn Attack action, not every contact or BA strike. Grappler’s ensuing Advantage improves later attacks, rather than retroactively improving the triggering hit.

Example at level5: weapon → Grappler Contact → remaining weapon. Against .55 failed-save probability, later-weapon Advantage is gained with probability .3575; at base p=.65, a 2d6+7 own-turn weapon packet with Graze4 gains roughly .3575×[(.2275×14)+(.0475×7)−(.2275×4)]≈.93 damage. The grapple also restricts movement and other-target attacks; it is not just that .93. A target may escape, teleport, be immune, or be too large. A held grapple generally prevents two-handed heavy-weapon attacks until a hand becomes available; do not retain both heavy attacks and an unavailable grappling hand.

Shield/one-hand weapon can still kick for damage or Shove; it lacks the free hand for Grapple unless equipment is released. Reach10 without an adjacent creature yields zero Close Work attempts, even though the weapon attack is legal. Unarmed Fighting can replace the damage with d8 when no weapon/shield is held at the roll: attack and legally stow the weapon, then Contact, then draw a weapon with a later actual attack. It never stacks d8+d6, and an equipped Shield prevents that d8 clause. Monk die replacements similarly replace, not add. Tavern Brawler rerolls a Contact damage die1 once into a kept new result: d6 mean rises by5/12, about .292 EV at .65 including crits; its push is limited by its own once-turn requirements. It overlaps proficiency and default damage, but its no-save push remains real.

Topple/Shield Master can make another Shove/prone source redundant. Topple uses Constitution and the weapon ability DC; Shield Master’s own Strength save is not the target-chosen US save. Neither is assumed always successful. Prone helps attacks within5ft and hinders farther attacks, so it can harm the ranged party. Tactical Master can exchange a weapon’s mastery for Push/Sap/Slow from9 without adding two masteries to one attack.

**Timing is not additive:** Vex can be consumed by the inserted Contact, whose hit does not renew Vex. An early unarmed attack can improve control for later attacks but lower pure damage on a high-value Vex weapon or consume an Advantage entitlement better used by that weapon. The script enumerates fixed insertion positions, while the workbook shows the recurrence explicitly. Studied starts at13 and follows misses against the actual target, including a Contact miss. Capstone Advantage makes many timing-based accuracy differences redundant. A competent policy may decline Contact or select save-based control instead of consuming a valuable roll entitlement.

### D3. Action economy at every audited level

One ordinary Action and one BA/Reaction are available; generated PF attacks belong to an eligible Attack action. Nick and optional feat BAs are separate from ordinary slots. The table lists capacity, not permission to use every option simultaneously.

| Fighter | PB | Ordinary slots | PF / eligible action | BA | Reaction | Movement | Surge / SW / Indomitable |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 2 | 1 | 1 shared Contact or HoC | 1: SW/PAM/DW/item/other | 1: OA/Ready/defense | Speed; HoC/Shift conditions | 1 Surge/SR; 2 SW, +1/SR; 0 Indom/LR |
| 5 | 3 | 2 | 1 shared Contact or HoC | 1: SW/PAM/DW/item/other | 1: OA/Ready/defense | Speed; HoC/Shift conditions | 1 Surge/SR; 3 SW, +1/SR; 0 Indom/LR |
| 7 | 3 | 2 | 1 shared Contact or HoC | 1: SW/PAM/DW/item/other | 1: OA/Ready/defense | Speed; HoC/Shift conditions | 1 Surge/SR; 3 SW, +1/SR; 0 Indom/LR |
| 9 | 4 | 2 | 1 shared Contact or HoC | 1: SW/PAM/DW/item/other | 1: OA/Ready/defense | Speed; HoC/Shift conditions | 1 Surge/SR; 3 SW, +1/SR; 1 Indom/LR |
| 10 | 4 | 2 | 1 shared Contact or HoC | 1: SW/PAM/DW/item/other | 1: OA/Ready/defense | Speed; HoC/Shift conditions | 1 Surge/SR; 4 SW, +1/SR; 1 Indom/LR |
| 11 | 4 | 3 | 1 shared Contact or HoC | 1: SW/PAM/DW/item/other | 1: OA/Ready/defense | Speed; HoC/Shift conditions | 1 Surge/SR; 4 SW, +1/SR; 1 Indom/LR |
| 13 | 5 | 3 | 1 shared Contact or HoC | 1: SW/PAM/DW/item/other | 1: OA/Ready/defense | Speed; HoC/Shift conditions | 1 Surge/SR; 4 SW, +1/SR; 2 Indom/LR |
| 15 | 5 | 3 | 1 shared Contact or HoC | 1: SW/PAM/DW/item/other | 1: OA/Ready/defense | Speed; HoC/Shift conditions | 1 Surge/SR; 4 SW, +1/SR; 2 Indom/LR |
| 17 | 6 | 3 | 1 shared Contact or HoC | 1: SW/PAM/DW/item/other | 1: OA/Ready/defense | Speed; HoC/Shift conditions | 2 Surge/SR; 4 SW, +1/SR; 3 Indom/LR |
| 18 | 6 | 3 | 1 shared Contact or HoC | 1: SW/PAM/DW/item/other | 1: OA/Ready/defense | Speed; HoC/Shift conditions | 2 Surge/SR; 4 SW, +1/SR; 3 Indom/LR |
| 20 | 6 | 4 | 1 shared Contact or HoC | 1: SW/PAM/DW/item/other | 1: OA/Ready/defense | Speed; HoC/Shift conditions | 2 Surge/SR; 4 SW, +1/SR; 3 Indom/LR |

Legal sequences matter more than maxima:

- **GS Surge:** weapon(s), PF once; second Attack action weapon(s), PF once. At17 a second Surge is available on a later turn, not now.
- **Dual/Nick Surge:** first Attack ordinary Light weapon(s), one Nick extra, one PF; second Attack ordinary attacks and one PF; one DW BA for the turn. Nick does not occur again in the second action. PF cannot be generated by the BA or by its own strike.
- **Own-turn Hair:** Ready an Attack for a perceptible completed event; move to complete that event; Reaction takes the readied Attack on this same turn, with legal PF and own-turn Light/Nick/GWM; optional Surge Attack. The one Reaction is then unavailable until next own turn. Hair does not duplicate Extra Attack’s count.
- **Off-turn Hair:** Ready now, trigger later, Reaction takes its2/3/4 numbered attacks and optional die; no PF, own-turn Nick or GWM. Valid Vex/Studied/capstone benefits can remain. Failure to trigger before next own turn loses the readied action.
- **Replacement with engine retained:** at5, weapon → PF → replace one remaining ordinary attack with an eligible procedure. At11/20 other ordinary slots remain. Procedures cannot replace PF or Nick.
- **Fighter3 replacement:** replace its sole ordinary attack; no weapon attack remains to trigger PF. Replacement cost is the attack plus the lost engine.
- **Haste:** ordinary Attack can trigger PF; extra one-attack-limited Attack cannot. Alternatively extra Disengage+Parting Blow produces its one outside-Attack attack, with its own costs/rider limits.
- **Magic item nova:** ordinary Magic activation → Surge Attack → eligible PF; one BA chosen from Activation attack, PAM/DW, healing or another feature. Dig Deep can heal without taking that BA. No second Magic action is granted by Surge.

Drawing/stowing is attached to actual attacks, including their normal weapon rules, not presumed free with every replaced procedure. An object already held for Deliver may require real inventory preparation. Thrown draws as part of the actual thrown attack; a ranged physical procedure does not acquire unrelated magic/mastery effects.

### D4. Replacement costs

At .65, default legal GS/GWM primary progression, one sacrificed weapon attack costs7.90/10.85/12.50/13.80 at Fighter3/5/11/20 before later Advantage, items, control and kill effects. Contact EV is4.40/5.05/5.70/5.70. At3 replacing the only weapon slot costs12.30 including engine loss. At5/11/20 the relative ordinary slots surrendered are1/2,1/3,1/4, but the absolute attack remains valuable. With capstone at20 the matched GS weapon is17.09 and Contact7.80; losing one ordinary attack is still substantial. Full-action Dodge/Help/Dash/Disengage generally forgo the entire attack sequence, including PF. No relative fraction makes the absolute loss free.

FET+eligible Hasty Sabotage is genuine action compression: one lost ordinary attack can produce a BA attack after the attempt, even if its check fails. For the level11 GS build, replacing a12.50 Attack-action GWM attack and recovering a9.90 outside-Attack BA weapon attack costs2.60 damage, plus a normally valuable BA, while gaining real sabotage. At20 with mark, the GWM flat6 alone creates5.265 expected damage difference between the own-action and BA attack, before other complications. Surge does not create another BA. If a PAM/DW BA was already available, the recovery is substitution rather than a free extra attack.

Compatible replacements can share an Attack action: at11 weapon/PF, FET, Break Their Hold, each replacing at most one ordinary slot. At5, replacing both ordinary slots with two different procedures removes PF. FET modifies a specific physical Utilize; it cannot replace an attack with arbitrary Help, Dodge, Magic, donning equipment, drinking a potion or multi-minute work.

### D5. Complete 20-selection Lesson matrix

Frequency letters are **scenario forecasts**, not measured rates: H=often in an intentionally suitable encounter/campaign; M=conditional recurring; L=uncommon/niche. Pick pressure means relative to other known selections under that scenario. “Exploit” is reserved for actual rule bypass; strong finite synergy is recorded separately. Every selection and both merged modes are covered.

| Selection / mode | Access | Action cost | Role | Forecast frequency | Numerical / procedure contribution | Overlap / pressure / complexity / risk | Recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Battlefield Improvisation — Deliver | Base | Replace1 attack; catch may use ally Reaction | Object logistics / supply | M in distributed-object missions; L in plain fights | Useful if it saves a recipient movement/Action; no use/equip/drink. Lost attack; at3 also PF. | Low combat pressure, useful merged flexibility; no attack riders; actual path/free hand | KEEP |
| Battlefield Improvisation — Misdirect | Base | Replace1 attack; expend object/ammo | Hearing-based concealment of another creature | L; needs unheard method visibility and an actual hearing check before expiry | DISADV first qualifying Perception check only; no automatic Hide. Short duration makes many intended distractions too late. | Weak niche, high DM/timing burden; Deliver prevents entire selection being a trap; passive reading unresolved | PLAYTEST |
| Break Their Hold | Base | Replace1 attack; within5 or actual held melee reach | Grapple release / unsecured disarm | M with grapplers/armed enemies; zero disarm value against natural attacks | Save only, target’s better STR/DEX. DC17 vs+5=.55; dropped weapon can be retrieved, not destroyed. | Medium niche pressure; overlaps Shove but differs reach/no explicit size limit; no magic disarm protections bypass | KEEP |
| Break Through | Base | Full Dash or legal BA Dash | Enemy-space traversal / push | M in blocked lanes; L on open maps | Ignore OAs only from entered enemies; failed chosen save pushes5; failure does not revoke traversal. | Combines with Forced March; ordinary larger-enemy traversal can make it redundant; BA multiclass synergy strong finite | KEEP |
| Casualty Extraction | Base | Disengage; physical carry capacity | Rescue / evacuation | M in casualty/objective fights | Removes movement surcharge for willing/unconscious payload, not anatomy/weight; no universal OA immunity for payload inferred. | Strong with Parting/Monk/Rogue Disengage; carrying a grappled unwilling foe still costs normally | KEEP |
| Field Concealment | Base | Hide; group grant1/SR | Infiltration / ambush | H in stealth campaign; L mid-brawl without hiding conditions | Own armor penalty ignored; after success group PB+you10min Advantage, armor relief. Not automatic invisibility. | High stealth-package pressure; skill/Expertise useful; group duration expires through an hour rest | KEEP |
| Field-Expedient Tool | Base | Replace1 attack with closed physical Utilize | Mechanisms / field repair / hazards | M–H in object-rich objectives | Weapon ability/proficiency substitutes a check; actual tools/time required; ranged impact cannot pick locks remotely. | High fieldcraft pressure; pairs Barricade/Sabotage; competent physical adjudication required, no arbitrary actions | KEEP |
| Fire-Team Assist — Distract | Base | Full Help action; ally mover need not use Reaction | Attack support / ally reposition | M when attacking is bad or packet eligibility matters; L pure DPR trade | At .65 packet7+5, first3 attempts gain3.48 total; one hitter moves10 without OA from that enemy. | Usually loses to full Fighter volley for damage alone; party SA eligibility can change value; no unconditional party-round ADV | KEEP |
| Fire-Team Assist — Two-Man Takedown | Base | Full Help; within5; next ally Grapple/Shove | Save-based setup | M for dedicated grapple parties | If normal fail q=.55, disadvantaged fail=.7975; marginal .2475; no advantage on damage/hit supplied. | Prerequisite position/action meaningful; better enemy save and immunity remain; overlaps existing DISADV | KEEP |
| Forced March | Base | Full Dash or legal BA Dash | Terrain travel / speed | M–H rough terrain; L clear stationary arena | Speed30 Dash normally total60; Lesson70, difficult terrain ignored for turn. | Overlaps Charger speed modestly; complementary not redundant with Break Through; campaign travel does not erase rest/exhaustion | KEEP |
| Hold Ground | Base | Dodge; same full-action cost | Personal control resistance | M vs save-based prone/grapples/push; weak against no-save prone | Adv relevant saves/checks; automatic push reduced10; Grappled-Speed0 alone preserves Dodge. | No auto protection from Hill Giant on-hit Prone; combines Shield Line; high lost-DPR cost | KEEP |
| Parting Blow | Base | Disengage; one attack during real movement | Retreat / attack+slow / BA multiclass | M pure Fighter retreat; H optimized Rogue/Monk routine | Outside Attack: no PF or GWM PB. Slow−10 through next own turn, no same-feature stacking. | High Rogue dip pressure; Ready/Sneak routine legal, finite; Reaction, feat and progression comparisons required | PLAYTEST |
| Shield the Line | Base | Dodge; willing ally5, remain5 | Ally cover / formation | M defensively appropriate turns; L routine offense | Half Cover +2AC/DEX saves; at unclamped accuracy often .10 fewer hits per allied incoming attack. | Not a shield equipment requirement in text; overlaps existing cover; combines Hold Ground on same Dodge | KEEP |
| Threat Scan | Base | Search; Readiness can compress | Ambush / tracking / concealed threats | M with concealed danger; low direct combat value vs visible foes | Adv Wisdom; detail must be evidenced. Only finding concealed location grants first allied attackADV and first enemy attackDISADV. | Strong scout package; not universal combat Advantage; expiring first-turn support can miss allies already acted | KEEP |
| Veteran’s Correction | Base | Eligible helped ally failed check; SW via Tactical Mind | Skill reliability / resource preservation | M important cooperative checks | Gap m1–10 rescue=(11−m)/10; cost only on success; no heal/Shift or free new Help. | Competes healing/Dig Deep; lawful Help proficiency needed; no combat saving-throw correction | KEEP |
| Hair Trigger | F7 | Ready Action + Reaction | Off-turn volley / own-turn Reaction trade | H own-turn optimization; M held-lane triggers | Own-turn extra die≈5.20 at7,5.67 at11; off-turn loses PF/Nick/GWM; trigger uncertainty can erase volley. | High combat pick pressure; no recursion; critical-wait policy differs at larger volley; clarified interpretation before testing | PLAYTEST |
| Hook and Turn | F7 | Modify a true OA; no second Reaction | Off-turn damage / displacement | M–H Sentinel or real movement; zero if never triggered | At .65 extra d10 EV3.85 per available OA; mark makes5.3625. Full OA damage separate. | PAM Reactive Strike not OA; Sentinel Guardian is OA; forced5ft move does not chain OAs | KEEP |
| Battlefield Activation | F10 | Item Magic action + optional BA attack | Item turn compression | M with legal action items; zero without them | Recovers one outside-Attack weapon/US attack; not sustained item DPR; requirements/charges remain. | PAM with Surge may already offer BA; pure Veteran cannot attune spellcaster-only wand; no second Magic Surge | KEEP |
| Common Soldier’s Tongue | F10 | Influence full action | Surrender / practical negotiation | M negotiated campaigns; L suicidal/magically compelled foes | Bloodied plausible survival demand changes willingness, not attitude; hostile DISADV can cancel topic ADV; DC max15/INT. | Can save whole combats; not compulsory surrender or secret extraction; full combat action/evidence costs | KEEP |
| Find the Weak Point | F10 | Study; possibly free Readiness; INT/evidence gate | One-subject party accuracy / physical checks | H on qualified bosses, L absent feasible evidence/exploitation | One SHARED benefit per TURN,1min; packet7+5 gain3.0625 on a fresh eligible roll; four distinct turns12.25/round. | Highest party pick pressure if broadly permitted; existingADV redundant; no save DC/vulnerability creation | PLAYTEST |
| Quick Barricade | F10 | Utilize or eligible FET replacement | Cover / lane delay / fortification | M with real sturdy materials; zero on empty unsuitable map | Two connected5ft edges; Half Cover; crossing+5ft; actual AC/HP. Ten minutes only small practical assessment/arrangement. | Shared cover geometry can matter to several allies; destroyed/bypassed materials reduce it; no material creation | KEEP |
| Sabotage | F10 | Physical Utilize; Hasty optional BA; Deliberate1min | Function denial / tool proficiency | M–H mechanisms; L natural enemies without objects | CheckADV; genuine attempt can yield BA even on fail; target function must be feasible; enemy clearing action/check can matter. | FET combo strong finite compression; while-known tool proficiency ends when swapped; reserve grants only for use | KEEP |

The merged rows above are22 **procedures**, representing20 selections. They are not a22-selection testing roster. No Lesson is supported for CUT or MERGE by this audit. Misdirect is the weakest standalone procedure: even its intended situation needs a check to occur before a short expiry, while the Veteran’s own noise remains revealing. It warrants actual stealth-objective trials, not an automatic buff based on combat DPR zero.

### D6. Selection packages rather than catalogue ownership

These are illustrative legal portfolios; forecast pressure is a hypothesis.

| Known count / level | Combat/response portfolio | Fieldcraft/mission alternative | Reserve considerations |
|---|---|---|---|
|4 /3|Break Their Hold, Parting Blow, Fire-Team Assist, Threat Scan|FET, Improvisation, Field Concealment, Casualty Extraction|None; choosing stealth options gives up combat contingencies |
|5 /7|Prior response4 +Hair; or replace one with Hook for Sentinel|Fieldcraft4 +Forced March or Break Through|Cannot fit every movement, support and reaction choice |
|6 /10|Hair, Hook, Weak Point, Threat Scan, FET, Sabotage|Concealment, FET, Improvisation, Tongue, Barricade, Extraction|Pick two unknown before day; one shared use/SR; often reserve an item/mission niche |
|7 /15|Combat6 +Parting or Correction|Mission6 +Hair/Hook/Correction as relevant|Rest swap adapts one known selection; no immediate reserve refill |
|8 /18|Prior7 +one terrain/rescue/party contingency|Fieldcraft7 +Weak Point or defense|Self accuracy benefit may be redundant with mark; choose party utility deliberately |

Hair is the likeliest high-pressure combat selection at7. Weak Point becomes similarly attractive at10 when qualification is reliable. FET/Sabotage exert object-mission pressure; Concealment exerts stealth pressure. Forced March/Break Through, Hold Ground/Shield Line and Extraction/Parting are complementary pairs with distinct costs, not necessarily duplicate selections. The design does not require every Lesson to be equally attractive in an empty arena.

## E. Interacting packages, defense and party value

### E1. Focused correction, split fire and retained riders

Before Studied/Vex, with n ordinary attacks all aimed at one durable creature, the first-miss focused follow-up occurs with probability1−p^n. Its expected damage omits only the positive ability modifier. At level11 bow p=.75 with Archery, follow-up d8+GWM4 EV=6.60: focused gain3.815625. Base primary damage31.05 becomes34.865625. With a second legal creature available after the final all-hit attack, additional distributed damage is2.784375, making total37.65. The primary is still34.865625; the difference is not focused boss DPR.

Without GWM, at exactly .65 the d8 follow-up EV3.15 and three-attempt first-miss probability .725375 produce2.28493125. With only one ordinary attack the probability is simply the miss chance. Increasing accuracy can reduce correction availability even as the follow-up itself becomes more reliable. At level13 the triggering miss gives that creature a Studied entitlement, so the independent formula no longer applies; the exact state model handles it. Vex/Studied created on a secondary creature never migrate to the primary. Valid primary entitlements remain until used/expired.

Policy choices are distinguishable: immediate split after the first hit guarantees early distributed damage when a secondary target may die or disappear; waiting for the first miss focuses the extra shot; saving a split shot for the final hit preserves focus when targets remain durable. The script implements first-miss/final-hit and an immediate branch; it does not pretend that one fixed policy globally optimizes unknown HP, changing sightlines, damage riders or future target availability. An optional unfavorable shot may be declined. Declaring full extra damage on every one-target all-hit turn is incorrect.

**Loading stress test:** the default level3 heavy-crossbow row assumes one crossbow and cannot shoot it again within that action. This does not ban another legal weapon. A post-shot stow of crossbowA, followed by drawing/firing crossbowB on the generated attack, uses one equip/unequip permission per actual attack; the next turn can alternate the weapons. With p=.75/DEX3/Archery, two otherwise legal crossbows produce11.05 distributed total versus6.65 ordinary, or7.75 focused first-miss total. A dagger follow-up from the available hand is another smaller legal alternative (the dagger has no Archery bonus): at .65 it adds1.75 when made, giving8.40 distributed or7.0875 focused total. Costs include actual weapons/ammunition/handling. Those are finite equipment sequences, not a recursion or an assumption that Loading ceased to exist. Crossbow Expert from4 removes the same-weapon limit and its listed hand restriction under its current text.

GWM applies to qualifying Heavy attacks made as part of an Attack action on the Veteran’s own turn, including a heavy ranged HoC follow-up if the feat’s STR prerequisite was legally paid. Bracers/weapon bonuses and qualifying riders are not the omitted positive ability modifier. A hypothetical extra d6 rider gives an ordinary .65 attack another2.45 EV, more with Advantage; legal HoC can retain it, while implement-narrated Contact cannot inherit a weapon rider. One rider is not automatically reusable if its feature says once per turn or requires another target. Weapon +1/+2/+3 improve the weapon’s actual accuracy/damage, not Contact. The matched-item sweep is separate from no-item results.

Movement remains valuable even if no follow-up is legal. With Speed30 it is up to15ft along a traversable path. It can leave melee safely, reach cover or a firing lane, or close an objective gap. It is not a teleport, ignores neither difficult terrain nor barriers, and suppresses OAs rather than all reactions: PAM Reactive Strike, a readied attack or Sentinel’s separately triggered event must be checked individually. A longbow attack made while pressured within5 may suffer Disadvantage before the movement; the follow-up after moving can have different accuracy. XBE/Sharpshooter can remove relevant close-range restrictions when legally taken. An optimized bow can take GWM4, DEX+2 at6 and Sharpshooter+1DEX at8 rather than inventing an extra ASI.

### E2. Full-dice HP/target availability scenario

These are one-turn, level11, three longbow attacks, p=.75, no Studied, GWM4; normal d8+9, PF d8+4. Focus first surviving target; first miss or final hit follow-up; actual target HP clips damage. Each Veteran and baseline case uses100,000 trials and separate recorded seeds; increment SE combines their mean uncertainties. This policy is not optimized target-by-target overkill avoidance.

| Targets | HP each | Actual Vet damage | Baseline actual damage | Increment | Increment SE | Enemies removed | PF shots |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 8 | 7.96 | 7.87 | 0.09 | 0.00 | 0.99 | 0.25 |
| 1 | 18 | 17.65 | 17.11 | 0.54 | 0.01 | 0.94 | 0.43 |
| 1 | 35 | 31.28 | 28.28 | 3.00 | 0.03 | 0.61 | 0.58 |
| 2 | 8 | 15.33 | 14.63 | 0.71 | 0.01 | 1.90 | 0.44 |
| 2 | 18 | 27.21 | 23.20 | 4.01 | 0.03 | 0.99 | 0.58 |
| 2 | 35 | 34.22 | 28.39 | 5.83 | 0.04 | 0.61 | 0.99 |
| 4 | 8 | 22.89 | 18.02 | 4.87 | 0.03 | 2.74 | 1.00 |
| 4 | 18 | 30.01 | 23.14 | 6.87 | 0.04 | 0.99 | 1.00 |
| 4 | 35 | 34.33 | 28.45 | 5.88 | 0.04 | 0.61 | 1.00 |

Low-HP outcomes cannot be inferred from white-room37.65: enemies may be removed before later ordinary/PF opportunities occur, and a weaker follow-up may fail to kill a target a normal shot would kill. Movement/objective value after a kill is not counted as damage. The sample is a disclosed HP scenario, not an empirical monster HP distribution.

### E3. Readiness, adaptation and noncombat contribution

Counter-Ambush removes only surprise’s Initiative Disadvantage, not an old-edition lost surprise turn. Against one equally modified enemy d20, assigning ties half to each, acting first rises from.33375 under Disadvantage to.50: +.16625. Actual enemy bonuses and tie rules change it. Champion’s existing Initiative Advantage is broader; surprise cancels that Advantage if no other rule removes the Disadvantage. Readiness’s other options resolve only at the Veteran’s first turn, so they cannot retroactively prevent earlier damage or identify a threat before it already acted.

Take Position grants15ft at Speed30 but uses normal movement/OA rules. Read the Field can compress Threat Scan or Weak Point, declared reserves included, but the search/study still needs its evidence/check. Brace gives3/4/5/6THP before15, then10/12. Useful absorption is min(grant, actual eligible incoming damage before replacement); successive THP are chosen, never added. If a superior pool already exists or the Veteran takes no damage, Brace can add zero. Study+Brace is attractive when no opening movement is needed; Position+Study suits an objective; Counter+Brace or Counter+Position suits an ambush. No combination guarantees pre-enemy safety.

At15, later Reserve Readiness chooses an **unused** non-Counter option. If Brace was already chosen, it is not another Brace. Opening Position+Study can hold Brace for later injury risk. In a changing map, later Position/Study may be more useful than an opening one. Incapacitation at the relevant resolution denies it. Ten THP per useful combat is meaningful in attrition but small beside tier3 multiattacks.

Practical Experience, lawful Help and Tactical Mind make investigation and perception dependable without becoming spellcasting. Example INT−1/Expertise Investigation atPB4 gives+7: ordinary DC15 success .65; Tactical Mind can rescue another.245 of attempts, total.895 if its resource is available, spending SW only on rescued outcomes. This does not remove Weak Point’s evidence gate. Threat Scan uses Wisdom, not FET’s weapon-ability substitution. Applicable skill/tool overlap or another helper can already grant Advantage, which does not stack.

Change of Approach is one swap after an actual Short/Long Rest. The identities of the two reserves were selected after the Long Rest, rather than chosen from the catalogue after an unanticipated need. Reactive use timing is considered separately in section I. Declare before **any** rolls of the modified action/reaction/procedure. Only one reserve use is shared between Short/Long Rests, not one each; learning a reserve removes it until the next Long Rest. Sabotage proficiency applies during the reserved use, not perpetually. While-known tool proficiency ends when the Lesson is no longer known. Repeated swaps do not accumulate tool proficiencies.

Durations do matter: reserved Ready/Help lasts normally; concealment10min and weakness1min expire during an hour Short Rest. Barricades are actual constructed objects and Sabotage’s Rig can persist until triggered; those lasting results can accumulate with real preparation time and materials, just as a known Lesson can repeatedly create them. This is not passive proficiency stacking. Multiple Weak Points are barred by one active subject. An indefinite accumulated catalogue of known/reserved Lessons is not permitted.

Concrete utility scenarios: concealed heavy-armored evacuation can preserve a party’s exposure/slots; Deliver can move a healer’s needed kit without drinking it; FET can cut a rope or lever a blocked release while retaining attacks at higher levels; Sabotage can deny a gate’s normal function and force an enemy clearance action; Barricade can give several ranged allies geometrically valid cover; Tongue can secure a guard’s plausible retreat without fighting to zero HP. These are material campaign contributions. They need physical and social constraints, not a made-up common DPR conversion.

### E4. Party amplification

Distract ends on the first **allied hit**, not the first allied attempt. For k equal attacks, its marginal damage is Δ×Σ(1−pAdv)^j, j=0..k−1, where Δ includes the crit increase. At p=.65, a2d6+5 packet gains3.0625 on one attack; three opportunities yield3.48361 total, already near its eventual first-hit limit. A25.5 dice+5 packet gains8.15 on one eligible fresh attack, about9.27 across three opportunities. It does not grant an entire volley unconditional Advantage. The successful hitter’s10ft movement can avoid an OA from the distracted enemy; not all surrounding threats.

Two-Man Takedown modifies the next **ally’s US Grapple/Shove save** within the duration, not a Break Their Hold procedure or spell save. With baseline failureq, disadvantaged failure=2q−q². At q=.25/.50/.55/.75 this is.4375/.75/.7975/.9375. It raises control reliability while costing Help, adjacency and a later ally attempt. Damage+Grapple still needs a real Grappler feature/hit. Prone can disadvantage distant attacks; a successful grapple does not inherently remove all enemy Actions.

Weak Point gives one shared qualifying benefit **each turn** for1min, not once per round or every attack. Four allies on different turns can each receive one; two allies attacking on the same Reaction turn share that turn’s one benefit. With four eligible2d6+5 packets and no existing Advantage, the incremental12.25 per round becomes7.9625 expected after a .65 successful-study probability, before duration/initiative/exploitation losses. A successful free opening Readiness Study over four complete party rounds can add49 party damage in this modest packet scenario. That is stronger than personal DPR reveals. High Sneak packets are more valuable, while already-advantaged allies add zero. It may also enable a Rogue’s Sneak Attack where none would otherwise qualify: an isolated d8+5 attack has6.40 EV, versus an advantaged d8+5+6d6 packet29.25125. The22.85125 difference includes **eligibility**, not merely accuracy, and is a distinct party scenario.

The costs are one Lesson/reserve use, evidence, INT/check reliability, a genuinely exploit-able subject, instructions perceived and a relevant roll. Readiness can remove the Attack-action cost; it does not remove those requirements. If the table routinely accepts any visible enemy’s generic “weak spot” as qualifying for almost every attack, the condition becomes ineffective and this combined package can move into Slightly Overtuned territory. A study success probability is not an empirical permission rate. Define the observation and permitted exploit before assigning its benefit.

Threat Scan’s first-attack/first-enemy-attack modifiers apply only after revealing a concealed location. Visible enemies or vague danger information do not qualify. Correction affects checks helped by the Veteran, not saves, with Tactical Mind’s real SW trade. Tongue changes a plausible Bloodied target’s willingness to Hesitant, not its Hostile attitude; topic Advantage can cancel Hostile Disadvantage. The Influence DC is at least15 or the target’s INT score. A willingness change is valuable even when a check remains difficult; no impossible/suicidal surrender or forced secret disclosure follows.

Cover/rescue/clearance are scenario outcomes: Half Cover normally reduces an unclamped enemy hit probability by.10 and adds2 to DEX saves; three18.5-damage attacks against one covered ally prevent5.55 expected hit damage, crit rate unchanged. Existing cover can make that zero. A barricade that an enemy destroys with one otherwise damaging attack may save that attack; a route bypass or enough movement can avoid any action cost. Extraction can double effective payload movement in the right ordinary carry scenario, but weight, accessible paths and enemy positioning govern it.

### E5. Hair Trigger, Hook and off-turn costs

Own-turn Ready is the major optimization finding. A completed movement trigger can make its success reliable without copying on-turn benefits onto a different turn. The following is an exact four-turn GS/GWM, Contact-after-last-weapon policy, no Surge/Hew, first-hit die assigned only to numbered weapon attacks. At13 the model carries real Studied entitlements; at18 it uses the full mark.

| Level | Ordinary | Own-turn Hair | Increment | OA+Hook opportunity q at damage equality |
| --- | --- | --- | --- | --- |
| 7 | 29.40 | 34.60 | 5.20 | 0.38 |
| 9 | 30.70 | 35.90 | 5.20 | 0.38 |
| 10 | 30.70 | 35.90 | 5.20 | 0.38 |
| 11 | 43.20 | 48.87 | 5.67 | 0.41 |
| 13 | 48.19 | 54.18 | 5.99 | 0.44 |
| 15 | 48.19 | 54.18 | 5.99 | 0.44 |
| 17 | 50.32 | 56.31 | 5.99 | 0.44 |
| 18 | 59.07 | 65.17 | 6.10 | 0.35 |
| 20 | 76.16 | 82.27 | 6.11 | 0.36 |

The q column is a **model-specific** comparison against a fresh GS true OA plus Hook at matching accuracy, no GWM outside Attack, no defensive/movement value and no carried off-turn entitlement. It is not a universal balance threshold. At7, a .378 probability of that particular valuable alternative OA equals the5.1975 damage gain; with fewer relevant reactions, Hair is an attractive routine. With Interception, Protection, Sentinel stopping an approach, Shield Master Interpose or later spell reactions, the lost Reaction can be substantially more valuable than this damage comparison. Capstone redundancy and party Advantage alter the equality.

Off-turn Hair makes its legal2/3/4 attacks, not an ordinary own-turn count plus PF/Nick. It loses on-turn GWM; it cannot reposition using movement from the Ready action as though taking its own normal turn later. Saving a chosen d10 for a critical is not simply “always wait”: first-hit is best in short volleys, while an exact remaining-attacks decision can slightly improve a longer volley. Crits double the attack’s extra die. The script compares first-hit and optimal observed-hit allocation, including Studied inside the volley. Trigger probabilities .25/.50/.75/1 are scenarios, not measured norms. At11, the earlier no-feat first-hit35.37 versus direct35.40 result is confirmed under its fresh .65 assumptions; with GWM off-turn it loses the PB rider on each hit and is less attractive as routine pure damage.

Hook adds d10 on a hit of a **true Opportunity Attack**; at p=.65 its extra EV3.85, with mark5.3625. The ordinary reaction attack remains additional and costs the one Reaction. Sentinel Guardian supplies a true OA after an enemy within5 takes Disengage or hits another target. PAM’s Reactive Strike is separately named and does not receive Hook by default. Hook moves Large-or-smaller targets up to5 to an empty space within the used reach, rather than granting arbitrary forced transport. Sentinel’s Halt can set Speed0 for the current turn when that OA hits; the forced reposition still happens if otherwise legal. That displacement can deny a route or move an enemy out of a threatened position. It does not provoke OAs itself or recursively grant another Reaction. A third-party trigger still needs its own actual rule; none of these features replenish Reactions mid-turn.

### E6. Dig Deep and item nova

At15 the uncapped heal is20.5; at17/18/20 it is22.5/23.5/25.5. Actual healing is E[min(missingHP, level+d10)], not min(missingHP, the mean) near the cap. With5 missing HP at15 the heal is exactly5. With20 missing, healing is19.0, not20.0: rolls1–4 yield16–19, rolls5–10 clip at20. With30 missing it is20.5. The live workbook evaluates every d10 outcome.

Second Wind is shared with ordinary healing, Tactical Mind and Correction. After a Short Rest only one expended use returns. A reserve use is a separate resource. Dig Deep preserves a BA only when Surge and healing/movement need coincide; spending Surge at full HP can leave no Dig Deep opportunity later. Delaying Surge to line up healing can sacrifice early enemy removal. A PAM/DW BA, Activation attack or legal BA consumable can give the preserved BA tangible value. Without such a competing feature it contributes no free BA damage. At17 use Surge and Dig Deep on separate turns if both charges are available, spending SW each time.

A pure Veteran legally can use a **Necklace of Fireballs**, no spellcaster attunement required: one Magic activation, a level3 Fireball (DC15), finite beads,60ft delivery. For three valid targets with DEX+2, expected28×.8=22.4 each,67.2 distributed. This is not67.2 focused weapon DPR. Activation adds a legal BA attack; matched GS p=.65, ability5, Graze5 gives9.90, so item+BA=77.10 before other Actions. A normal class with matched item access also receives the67.2 item effect. Magic→Surge Attack is legal; Magic→Surge Magic is not. On a PAM build, the Surge Attack may already unlock its BA, making Activation redundant that turn. At15 Dig Deep can preserve that BA while spending healing. The workbook’s default live Magic+Surge+Activation case adds a legal Attack/PF sequence and includes the foregone normal Attack-action opportunity in the report comparison.

Wand of Fireballs’s spellcaster attunement requirement excludes an otherwise pure Veteran; an eligible multiclass or EK must pay its own progression costs. Spell Scroll eligibility is not universal. Healing potions using their listed BA activation do not automatically become eligible Magic-action items for Activation. FET expressly cannot activate an item or apply a consumable. Charges, target saves/immunities, range, attunement, hands and components where required remain. Matched +weapons and hypothetical on-hit rider tables examine scaling, not a promise of campaign item availability. No sustained subclass DPR is inferred from a consumable bead nova.

### E7. Capstone — offense, defense, saves and targeting

The mark lasts to the next Veteran turn, including every enemy/ally turn in between. It improves a legal off-turn Hair volley or OA against that creature, and protects attack rolls/saves against that creature’s effects throughout. It gives no protection before the Veteran’s first turn, no benefit against other enemies, and no compelled aggro. Selection requires visibility at the start of the turn; subsequent retreat/death/out-of-range can waste offense, while unseen attacking applies ordinary restrictions. The mark itself does not say it ends when sight is lost.

For ordinary probability p, Advantage success gain is p(1−p); at .50/.60/.65/.70/.80 gains are.25/.24/.2275/.21/.16. Attack crit probability becomes.0975; Disadvantage enemy crit probability becomes.0025. Against a marked ordinary attack with meanD and additional crit diceK, prevented damage=(p−p²)D+(.05−.0025)K. Existing defensive Disadvantage gives no extra reduction; existing offensive Advantage gives no marginal accuracy/crit gain. An enemy’s existing attack Advantage cancels the mark’s Disadvantage, producing ordinary rolls rather than Disadvantage.

The revised adult red’s+14 attacks versus AC20 have p=.75. Three18.5 Rends with10.5 extra crit dice yield11.9025 expected prevented damage when they target this marked Veteran. If the dragon targets allies or two other dangerous enemies attack instead, that protection can be zero or cover only a portion of the incoming packet. The .75 DEX-save success example under a mark would gain .1875; for DC21 breath with a genuinely weak+0 DEX save, ordinary success is0, so Advantage alone remains0. Advantage does not manufacture a possible save. If ordinary success=.30, the breath’s mean59.5 half-save model improves expected damage by.21×29.75=6.2475; with Evasion or condition effects use their actual outcomes instead.

Indomitable’s Fighter-level bonus can change the reroll dramatically. With a DC24 INT save and−1 modifier at18, ordinary success0; an Indomitable reroll with+18 succeeds .70, marked Advantage .91. There is no natural1 auto-failure on saves. In easier saves a charged Indomitable may already guarantee the reroll: capstone then often preserves charges by reducing initial failures rather than adding another independently counted avoided failure. It does not refresh those three Long-Rest uses.

At18 GS mark repeatable damage59.07 versus an otherwise matched pre-mark Studied routine about50.30 is a meaningful offensive jump. At20 the marked routine76.16 plus valuable real reactions is large. Complete comparators remain relevant: Champion Survivor heals5+CON each eligible Bloodied turn (e.g.8 withCON3), helps death saves and keeps its Reaction; BM Relentless supplies own- and off-turn maneuver value plus control; EK Shield can defend against several enemies and its spells can support/control; Psi protection can help allies and Telekinesis can restrain a suitable threat at a substantial action/concentration cost. They are neither identical defenses nor zero-value add-ons.

EK18 has a particularly useful comparison: weapon hit can impose Eldritch Strike, followed within the Attack action by a legal two-slot Hold Person replacement against a humanoid, and Surge attacks exploit any resulting paralysis. This sacrifices ordinary attacks, spends one slot, needs an eligible target/save and concentration, but can amplify an entire nearby party via automatic melee criticals. It illustrates why a True Strike-only column cannot define the official support ceiling. It is not granted against dragons or creatures immune/ineligible for that spell.

The mark is probably the strongest feature relative to its level when the fight is dominated by one creature attacking the Veteran. Its benefit is more concentrated than a broad all-enemy defense and less redundant in low-Advantage parties. The combined boss routine warrants high-level trials; the calculations do **not** establish that its full duration or off-turn protection requires shortening.

## F. Model agreement, sensitivity and environments

The frameworks agree that contact is a meaningful early repeatable benefit and that most replacement/Help/Dodge choices have real attack costs. They disagree in ordering because they ask different questions. A fresh short encounter favors dice spending and accurate high-value attacks; a long day favors PF and capstone persistence. Vex favors weapon packets and careful insertion; high item dice magnify that opportunity cost. An eligible Trip target increases BM’s later-hit advantage; a Huge or immune target removes that control contribution while Precision and damage maneuvers remain.

A key accuracy result: at3, fresh four-round Veteran beats the modeled BM from around the .60 case upward but loses at .50. At5 the ordering can change again near the .80 case. These are discrete d20/AC scenarios, not a smooth universal crossover: changing feat paths, AC information, saves or defense policy changes the comparison. At18/20 the fresh BM Trip/Precision policy is modestly above the weapon-only Veteran throughout the tested .50–.80 range; on an ineligible Trip target use its no-Trip column. Adding Hair’s actual Reaction cost, defensive mark value and party effects requires the separate scenarios above.

| Level | p | Veteran fresh | Champion fresh | BM optimal | Psi first hit | EK INT3 floor |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | 0.50 | 12.84 | 9.00 | 13.30 | 12.22 | 8.56 |
| 3 | 0.65 | 15.38 | 10.31 | 14.96 | 14.47 | 9.88 |
| 3 | 0.80 | 17.91 | 11.62 | 16.34 | 16.65 | 11.19 |
| 11 | 0.50 | 46.22 | 50.39 | 53.47 | 48.36 | 40.75 |
| 11 | 0.65 | 54.00 | 57.67 | 59.66 | 55.10 | 48.25 |
| 11 | 0.80 | 61.78 | 63.47 | 65.07 | 61.51 | 55.75 |
| 18 | 0.50 | 79.52 | 73.08 | 83.19 | 68.87 | 63.92 |
| 18 | 0.65 | 88.61 | 80.62 | 90.01 | 75.61 | 72.53 |
| 18 | 0.80 | 94.48 | 86.92 | 95.45 | 82.16 | 80.71 |

The actual-bonus sweep avoids recycling an assumed65% progression as independent evidence. Representative examples, same actual target AC, no Surge/items:

| Level | Build | AC | Actual bonus | Chassis | Veteran |
| --- | --- | --- | --- | --- | --- |
| 3 | Great weapon | 13 | 5 | 7.90 | 12.30 |
| 3 | Longbow | 13 | 7 | 5.85 | 6.75 |
| 3 | Great weapon | 19 | 5 | 5.80 | 8.25 |
| 3 | Longbow | 19 | 7 | 3.60 | 4.84 |
| 3 | Great weapon | 23 | 5 | 4.40 | 5.55 |
| 3 | Longbow | 23 | 7 | 2.10 | 3.11 |
| 18 | Great weapon | 13 | 11 | 53.23 | 64.77 |
| 18 | Longbow | 13 | 13 | 44.98 | 47.78 |
| 18 | Great weapon | 19 | 11 | 44.02 | 59.07 |
| 18 | Longbow | 19 | 13 | 37.38 | 46.72 |
| 18 | Great weapon | 23 | 11 | 37.98 | 50.52 |
| 18 | Longbow | 23 | 13 | 30.34 | 42.74 |

Actual-AC ranged rows use focus against one durable primary, actual Archery and legally delayed DEX progression. At18 the primary is marked while any different secondary would not automatically be marked. Higher p reduces correction opportunities; a marked boss may make HoC mostly movement while its ordinary shots are strong.

| Environment | Disclosed conditions | Consequence |
|---|---|---|
|Adverse|Reach/ranged foe beyond5; no valid secondary; strong chosen save; existing Advantage; empty room; Ready trigger fails; enemies target allies|Many Lessons/PF branches add little; mark defense can be irrelevant; some Veteran builds below official packages |
|Mixed scenario|Four rounds; some adjacent turns/secondary foes; real cover/objective; p=.65 reference and actual-AC sweeps; scheduled rest; selective control; some reactions|Repeatable engine competitive; actions/resources/geometry decide ordering; “typical” not asserted empirically |
|Favorable/optimized|Legal GWM/Nick/Grappler; own-turn Ready; suitable sabotage materials; qualified Study; high-value allies on distinct turns; one boss attacking Veteran; legal item access|Strong combined contribution; Hair/Weak Point selection pressure and boss defense need live evidence; no infinite loop demonstrated |

Relevant breakpoints are conditional rather than fabricated universal numbers: contact adjacency0 makes its damage/control0; existing Advantage makes another Advantage source’s marginal accuracy0; a .55 normal failed save becomes.7975 with Takedown; spell/weapon immunity can make damage/control0; one target removes every hit-triggered split shot; unavailable BA removes Sabotage/Activation’s recovered attack; an already stronger THP pool can make Brace0. The Hair q equality and Rogue trigger equality below are policy comparisons, not balance verdict thresholds.

## G. Optimization, multiclass and exploit findings

### G1. Feat/style/equipment interactions

- Grappler adds damage+save-gated grapple once per eligible own turn and can improve later attacks; it is not a free grapple on every Contact. Low STR ordinary DC remains a Dexterity build cost unless another feature, such as compliant Monk Martial Arts, changes it.
- Tavern Brawler overlaps proficiency/damage but keeps its reroll/push benefits. Shield Master/Topple overlap Shove/prone yet use different saves/timing. Charger’s die is once per turn and needs actual10ft straight movement; Surge does not multiply it. Forced March can combine with a legal Dash/Charger speed contribution without granting an otherwise missing BA Dash.
- GWM retains its heavy own-Attack PB rider on legal HoC; melee crit/kill Hew needs a real qualifying event and competes for the BA. PAM/DW BAs occur once through their rules; a second Attack action does not create another BA. Sentinel/Hook is strong finite synergy; PAM Reactive Strike is not renamed an OA.
- Archery adds actual attack bonus to Ranged weapons, not every thrown Melee weapon. Thrown style’s2 damage can remain on an eligible HoC thrown follow-up. Dueling/TWF/GWF have their actual holding/weapon/Light/two-hand requirements. No second style is granted except where Champion or another class explicitly grants it. GWF can improve qualifying weapon attack dice including eligible riders; our default Veteran keeps Defense instead of receiving both.
- +weapon accuracy/damage, archery bracers and eligible riders can strengthen ranged follow-ups. Contact remains nonmagical weapon-independent damage unless a separate legal feature changes it. The capstone’s Advantage is less unique in a party already generating it; a high-value weapon rider makes consuming Vex with Contact less attractive.

### G2. Matched total-level multiclass checks

Prerequisites are paid: Fighter STR13 or DEX13; Monk DEX13/WIS13; Rogue DEX13; Barbarian STR13; Paladin STR13/CHA13; Ranger DEX13/WIS13. PB follows total character level, while Fighter Lesson/Hair/feature prerequisites follow Fighter level. Extra Attack features do not stack; another class’s eligible two-attack action can trigger PF once. A Fighter3/other5 character is level8, not a level5 Veteran with free extra class features. [C1–C5]

**Monk:** Martial Arts requires no armor/shield and only appropriate Monk weapons; its damage die replaces Contact’s die and its Dexterous Attacks can replace the US save DC only under those restrictions. Flurry and Patient Defense compete for BA/resources. F3 gives Mastery/TWF/Surge shared with other Fighter dips; Veteran adds Contact. The table uses two Light Monk weapons, Nick, dip TWF; pure Monk legally pays Weapon Master4/ASI8. Vex and subclass riders are excluded, not silently erased from a claimed global optimum. At8 dip primary18 versus pure20 uses actual .65/.70 accuracy; at20 pure Body and Mind’sDEX24 gives .75 versus dipDEX20 .65. Thus the high-level pure stat gain is included.

| Total level | Dip | Dip repeatable | Pure Monk +Nick | Dip Flurry | Pure Flurry |
| --- | --- | --- | --- | --- | --- |
| 8 | F3/M5 TWF+Nick | 28.75 | 24.00 | 34.50 | 30.87 |
| 14 | F3/M11 TWF+Nick | 35.50 | 25.15 | 49.70 | 39.35 |
| 20 | F3/M17 TWF+Nick | 39.00 | 36.55 | 54.60 | 57.45 |

At8 F3/M5 has three fewer Focus, delayed Evasion/subclass progression and only one Monk ASI; at14 F3/M11 delays Deflect Energy and all-save proficiency; at20 F3/M17 lacks Superior Defense and Body and Mind. Pure20 beats the modeled dip Flurry turn despite the contact, and has major defenses. At14 the sustained dip gain is substantial, especially with TWF/Nick: that is a strong legal dip worth live testing, not proof that its lost defenses are irrelevant. Battle Master’s same three Fighter levels supply four SR d8 maneuvers, Precision/Trip/defense and Mastery/TWF/Surge too; a fresh-resource comparison is materially better than comparing the dip to an empty BM. Champion supplies critical/initiative/athletic benefits. F5/Monk5 does not stack to three ordinary attacks; taking those extra Fighter levels instead of Monk progression can be inefficient.

**Rogue:** F3/R9 at total12 can BA Cunning Action Disengage, make a finesse Parting attack during movement, and use its Action to Ready a separate off-turn attack. Sneak Attack remains once per turn, not once per round, so two are legal if both qualify. It forgoes Uncanny Dodge/other Reaction protection. Remaining adjacent for a rapier Ready attack is a real positional requirement; disengaging far out of reach can invalidate the follow-up. Ready can fail if the enemy does not perform the perceptible trigger.

With DEX20, p=.65, Dueling rapier, SA5d6 eligible on both turns, on-turn EV19.95; the off-turn conditional EV24.917625 includes per-target Vex from a successful on-turn rapier and its correct .0975 Advantage critical probability. A pure Rogue12 shortsword/Nick first-hit SA6d6 baseline is27.995, so this isolated comparison favors the dip once trigger q> .322864. At q=.50 the dip32.409 is+15.8%; atq=1 its44.868 is+60.3%. That headline does **not** prove dominance against a complete optimized Rogue.

A pure Rogue12 can legally spend its additional feat on Sentinel and generate an off-turn SA when its Guardian conditions occur, retaining its own Attack action. With a d6+5+6d6 packet and .65/crit.05 that OA is20.40. If the same q applies, pure27.995+20.40q stays ahead of dip19.95+24.917625q for everyq≤1. Ready can trigger on attacks at the Rogue or on misses where Sentinel cannot, so their real q values differ; for example Ready .80 versus Sentinel .40 gives39.884 versus36.155, a much smaller relative lead. All these assume SA eligibility/position, no incompatible offhand/Style benefit, no free reaction replenishment and no already-used Reaction. An isolated no-ally/no-Vex case after a missed Parting attack cannot retain the assumed Sneak eligibility. BM Riposte also offers off-turn SA at a resource/trigger cost; it is a relevant official dip comparator. Seven Fighter levels for Hair delay substantially more Sneak dice/feats; Hair grants its Fighter2 attacks, not a doubled Rogue count. Eleven Fighter levels improve ordinary slots but leave only Rogue9 at total20, losing much higher Rogue progression.

**Barbarian:** F3/B5 at total8 loses the pure B8 additional ASI, Feral Instinct progression and later Brutal Strike timing; Rage forbids Heavy armor and spell/concentration use. Strength attacks, including Contact, qualify for Rage/Reckless; Dexterity Contact does not. A legal GWM4 Berserker case with dipSTR18/p=.60 (Reckless .84) versus pureSTR20/p=.65 (Reckless .8775), Rage+2, GS Graze and first-hit2d6 Frenzy produces approximately45.63 versus40.09 repeatable damage without crit/kill Hew. Veteran’s contact adds Rage/Frenzy hit assurance without adding another once-turn Frenzy packet. The dip’s extra style, Surge and HP are Fighter chassis benefits shared by official dips. It delays Brutal Strike and later subclass features; at higher matched totals the primary/stat and feat opportunity costs must remain. Reckless includes incoming attack Advantage; a Fighter18 mark would require a drastically different level split and cannot be casually added to this F3 build.

**Paladin:** F3/P5 at total8 delays Aura of Protection, subclass7 and an ASI; those party saves can matter more than a contact. Divine Smite uses a BA after its qualifying hit and a spell slot (or its stated free use), so another contact/Surge only increases delivery assurance, not several unrestricted smites. At total14 F3/P11 legally has Radiant Strikes on US: Contact d6+d8+5 at .65 gives8.85 EV. That is a substantial repeatable rider ceiling. PureP14 has the additional ASI, level4 spells, Restoring Touch and three more Paladin levels of Lay on Hands/other progression. The repeatable dip is strong, particularly in short-rest-poor weapon fights, but spell/party-defense opportunity costs prevent an automatic harmless-or-broken conclusion. Paladin and Fighter can each explicitly grant a style; declaring those two styles is legal, unlike granting them to a pure Veteran for free. No P11 Radiant Strikes are available in an impossible F15/P11 level20 character.

**Ranger:** F3/R5 at total8 delays Roving, subclass7 and its second Ranger ASI; an optimized actual-AC comparison must reflect dipDEX18 versus pureDEX20 unless another legal allocation is stated. Hunter’s Mark applies to attack-roll hits including Contact, with concentration/BA casting and retargeting costs. A dip Contact withDEX4, ordinary p=.60, d6+d6+4 gives6.95 EV on the marked creature. A hit-triggered HoC against a different creature does not automatically carry that mark’s rider. F3/R11 at total14 delays Relentless Hunter13, Nature’s Veil14 and level4 spells; maintaining concentration after taking damage is not free. Once-turn Hunter subclass riders remain once per turn. Both classes can grant declared styles; PB comes from total level, not one class.

These are stress tests of the priorities, not an exhaustive ranking of every subclass/spell/race multiclass. Reproducible exact Monk/Rogue policies and clear rider ceilings are included; the Barbarian/Paladin/Ranger scenarios isolate specific interactions, not a falsely complete general DPR optimum. The full official Fighter envelope is primary; these classes’ specialties do not impose one shared DPR target.

### G3. Issue classification

| Issue | Type / severity | Evidence / disposition |
|---|---|---|
|Own-turn Hair routine|Strong legal synergy; Moderate selection-pressure concern|Reliable trigger preserves on-turn engine, adds5–6 damage for Reaction; no immediate nerf supported |
|Broad Weak Point permission|Adjudication-sensitive power; Major review priority|One benefit on several turns, compressed Study, high packets; routine broad qualification can exceed envelope |
|Parting/Rogue Ready|Strong finite synergy; Moderate multiclass concern|Two SA turns legal; reaction/position/progression costs and pure Sentinel comparison materially moderate it |
|Monk TWF/Nick/contact|Strong finite synergy; Moderate dip concern|Large tier2/3 sustained gain, but delayed Focus/defenses/stat cap; must compare competent pure and BM dip |
|Single-boss mark|Strong legal package; Moderate high-level review priority|Full-cycle offense, attack defense and saves; existing ADV/multiple threats/exposure moderate it |
|Item nova/rider stacking|Finite legal synergy; Minor eligibility/recording issue|No free second Magic action; charges and eligible items; matched access required |
|Replacement arbitrary-action bypass|Not legal in current wording|Closed procedures, costs and exclusions prevent it |
|Recursive/infinite reaction or PF loop|Not found|PF cannot retrigger itself; Nick/Cleave/BA/Reaction finite; forced movement does not generate an OA chain |
|Legacy feat/stat/free-hand imports|Modeling error, not subclass defect|Correct current wording and actual progression/hands before evaluating |

No Critical exploit or proven Major mechanical defect was demonstrated. Major review priority does not mean a confirmed Major exploit. The official comparison tables are policy-specific rather than a numerical license to ignore support/defense costs.

## H. Independent verification of the earlier audit

Both supplied scripts ran successfully. The regenerated calculations.json, official_encounters.json and official_days.json compare identically with the originals in the archive. Agreement of script outputs proves reproduction, not that every policy represents optimized play. Important outcomes were independently recalculated or varied.

| Status | Result | Practical consequence |
|---|---|---|
|Confirmed|d6+5 Contact5.70 at .65/.05; early d6+3 Contact4.40|Core repeatable engine’s size was correctly estimated |
|Confirmed|No-feat level11 fresh four-round/Surge Veteran44.25; BM44.52, Psi45.35, favorable EK43.25, Champion42.51 under original policies|A valid controlled comparison, not complete optimized subclass parity |
|Confirmed|Hair no-feat first-hit level11≈35.37 vs immediate35.40 when trigger occurs|Off-turn volley close in that isolate; on-turn benefits and trigger cost must be separate |
|Confirmed|Separate Psi Strike damage, resource counts/recovery; first-hit finite policies|Do not double the separate Strike on crit or refresh all Psi dice on SR |
|Confirmed|Mark duration includes off-turn attacks/saves/defense; GWM Heavy ranged qualification|Strong legal interactions, not defects to remove by reinterpretation |
|Confirmed|Earlier mean-damage sequencing Monte Carlo seed20261005/trials300,000 was close to exact47.65822|Correct sequencing check; it was not a full-dice damage-distribution simulation |
|Corrected scope|Champion’s additional style not valued offensively in the old GS comparison; new GWF plus Inspiration/Hew materially increases it|Champion cannot be represented as criticals alone or with an unused compatible extra style |
|Corrected scope|First-hit BM damage spending was not the universal optimal BM; new exact Precision/Trip/no-spend policy plus off-turn Relentless bracket|Veteran’s advantage is smaller or disappears in several fresh-resource scenarios |
|Corrected scope|EK matched high Intelligence is a favorable allocation, not free same-stat damage; spells/defense absent from DPR isolate|Use INT3 sensitivity and real slot/control/Shield comparisons; never treat floor as whole subclass |
|Corrected method|Fresh versus finite/stationary Vex/Studied and insertion differ; level11 rapier early Contact33.98 versus delayed34.64 across four turns|Isolated Contact5.70 is not automatically added to a Vex baseline |
|Corrected method|Prior thrown follow-up overlay was an approximation; new model includes Nick/DW and target-specific states|Stateful policy tables replace the approximation, without claiming global target/weapon optimization |
|Corrected scope|Own-turn Hair legality was acknowledged but routine value/pick pressure not quantified|Adds roughly5–6 damage for Reaction; important selection-pressure trial |
|Corrected scope|Rogue Parting/Ready concern now includes Vex crits, triggers and pure Sentinel alternatives|High isolated ceiling exists; no automatic dominant-dip conclusion |
|Unresolved|Real weakness qualification, object feasibility, DM denials, reaction frequencies, target loss and useful movement|Requires instrumented encounters; no invented typical rates |
|Unresolved|Complete optimized EK spell policy and exhaustive magic/item/weapon-switch maximum|Current comparison has explicit floors/strong scenarios, not an exhaustive universal ceiling proof |

The previous conclusion “no numerical nerf needed before testing” survives the stronger modeling as a conditional recommendation, not as a demonstration of exact parity. Its proposed bounded wording is already part of Public Test 1. Reintroducing removed experiments would invalidate this audit.

## I. Smallest supported recommendations

**No numerical or structural change is required before the next instrumented playtest on this evidence.** Keep PF’s per-action frequency, Contact die, split/focus restriction, Readiness timing, rest swap/reserve count, level15 package, Hair attack counts/die, Hook and the mark’s full duration. No replacement subclass text is warranted merely because a mechanic has a strong optimized use.

The only immediate adjustments supported are to the **testing/rulings documentation**, not a silent mechanical redesign:

| Priority | Specific problem | Evidence | Smallest adjustment | Result / gameplay cost | Timing |
|---|---|---|---|---|---|
|1|Hair can be evaluated incorrectly as exclusively off-turn or as importing PF off-turn|Own-turn legal trigger adds5.20 at7/5.67 at11 while costing Reaction; off-turn loses timing-limited benefits|Add a test-sheet example of own-turn Ready and separate off-turn sequence; explicitly record available Reaction alternatives|No numerical change; preserves intentional readiness tactics; modest logging cost|Before testing |
|2|Weak Point tests can accidentally grant whole volleys or accept undefined universal weak spots|One shared per-turn benefit can add12.25/round for four modest fresh packets; evidence/exploitation govern availability|Record observation, INT/DC, successful inference, exact allowed exploitation and each turn’s single recipient|No numerical change; preserves fieldcraft; makes permissive versus narrow rulings comparable|Before testing |
|3|Reserve “procedure” timing can be read differently for reactive Correction|Lesson triggers after a failed helped check; the Tactical Mind procedure’s d10 starts later|Record whether reserve declaration is at the Tactical Mind procedure start before its d10 or was required during earlier Help; test separately rather than backdating a reserve to reroll an already resolved die|Shared1/SR and SW-on-success remain; no numerical nerf; avoids inconsistent contingency accounting|Resolve as a table ruling before testing |

For that third point, declaring a preselected Correction reserve when the failed-check-triggered Tactical Mind procedure begins is a defensible reading: it precedes that procedure’s own roll, although the triggering ally check already happened. A restrictive Help-time declaration is an alternative procedure-scope ruling with higher wasted reserve cost. The text does not define procedure boundaries sufficiently to claim both analyses have identical timing. No retrospective declaration after the Tactical Mind roll is permitted under either reading. This is a wording/timing uncertainty, distinct from a proven power discrepancy.

Possible changes **after evidence**, not current recommendations: if Hair regularly wins while comparable reactions were realistically available and its routine consistently suppresses choices, review only its bonus-die eligibility/timing before altering attack count; if Weak Point’s broad qualification regularly creates excessive cost-free party amplification, first tighten the described exploit condition rather than replace its mechanic; if Parting dominates matched competent Rogue options despite observed positioning/reaction costs, review that BA interaction specifically; if the marked-boss package persistently overwhelms matched full subclass defenses, tune the demonstrated component rather than reflexively shortening duration. These are conditional review paths, not approved changes or new numeric thresholds.

Misdirect may need a small duration/clarity buff only if its intended hearing-distraction situations repeatedly arise and it still cannot create useful opportunities. A combat model assigning it zero DPR is insufficient to cut it. Likewise no fieldcraft Lesson is cut merely because the room has no relevant objects or social objective.

## J. Playtest plan and review criteria

Use paired encounters with the same party/build/items/resources and swap Veteran for a complete official Fighter comparator. Alternate order or use different matched maps to reduce familiarity bias. Start with levels3/7/10/15/18, then stress5/9/11/13/17/20 where chassis breakpoints change sequencing. Do not test every known Lesson simultaneously; use actual4/5/6/7/8 portfolios and declared reserves.

| Test cell | Required contrasts | What uncertainty it resolves |
|---|---|---|
|Early contact|Adjacent vs10ft reach-only; damage vs Grapple/Shove; STR vs low-STR DEX; shield/heavy/free hand|Real contact/control availability and cost |
|Threat mix|One durable foe, several threats, natural attacks vs unsecured weapons, Large/Huge, immunities|Mark concentration, disarm recovery and US limits |
|Ranged pressure|Single target, secondary dies/leaves, all-hit turn, cover/range/ammo, close enemy, single/two crossbows before XBE|Correction policy, Loading/handling, safe-movement value |
|Ambush|Actual surprise and Initiative ordering; concealed search target vs visible enemy; incapacitated first turn|Readiness’s true timing/option opportunity cost |
|Study/support|Narrow and broadly qualified weakness; low/high allied packet; existing ADV; multiple allies on same/different turns|Study success and party amplification rather than personal DPR |
|Control|Strong/better chosen saves, Topple/Shield Master, grappler party, ranged party harmed by Prone, escapes/teleports|Net party control value and redundancy |
|Terrain/objects|Blocked lane, rough terrain, FET ranged impact vs tools/fine manipulation, real barricade materials/durability, genuine Hasty/Deliberate sabotage|Physical feasibility and enemy action/route savings |
|Rescue/social|Willing/unconscious payload, weight/path; Bloodied plausible surrender vs unwilling/suicidal/compelled foe|Fieldcraft and Influence usefulness without compulsion |
|Ready/reactions|Own-turn trigger; later trigger succeeds/fails; real OAs; Sentinel; PAM separately named strike; defensive Reaction opportunity|Hair/Hook/Parting routine opportunity cost |
|Resource days|Fresh 3/4/5-round; three encounters0/1/2 SR; healing at varied missing HP; Tactical Mind/Correction competing|Dig Deep and low-rest attrition value |
|Magic items|Matched legal items/attunement/charges, item+BA vs item+Surge+BA, no second Magic, actual target saves|Finite item nova, not assumed sustained DPR |
|High level|Single boss attacking Veteran; boss attacks allies; multiple ranged/caster threats; unseen/retreat/death; before first turn; Indomitable depleted/full|Whole-cycle mark offense, defense, saves and targeting |
|Multiclass|F3/M5/M11/M17; F3/R9 vs pure Sentinel and BM; F3/B5/P5/R5 and rider breakpoints|Matched-level delayed features, feats, stats and defenses |

Each round record: ordinary/generated attacks attempted, hits/criticals, raw damage, actual HP damage and overkill; PF branch/time/targets/contact eligibility and actual movement; Mastery/Advantage sources and target-specific carried entitlement/expiry; procedures and ordinary attacks sacrificed; Action/BA/Reaction and the realistic alternatives forgone; SW/Surge/dice/slots/charges, actual healing and THP absorbed; control saves/chosen modifier/immunity/success, recovery and enemy actions actually prevented; allied damage/action/movement/resource enabled; known selections/reserves/uses, DM denials and exact rules questions; turn duration. Include zero-use opportunities and reasons, not just successful highlights.

Record changes in monster targeting separately: a boss choosing an ally instead of the marked Veteran can reduce personal incoming damage but increase party harm. Report damage prevented and party resource savings without double-counting the same control/cover/mark event. Mark an estimated counterfactual as estimated; do not record hypothetical enemy actions as certainly prevented.

Review triggers should prompt another analysis, not automatically determine balance from a small sample:

- **Nerf review:** repeated matched scenarios show a legal routine clearly replacing meaningful choices and out-contributing complete official packages after attack, Reaction, resource, geometry and party costs. Replicate across more than one DM/party before changing a general feature.
- **Buff review:** an intended Lesson situation occurs repeatedly, players try it correctly, and it remains worse than ordinary available procedures even after its non-damage outcome. This is the right test for Misdirect or a costly full-action modifier.
- **Merge/cut review:** actual portfolios consistently exclude an option because another known choice duplicates its real use, or confusion/turn time exceeds delivered contribution. Non-selection in a plain damage arena is insufficient.
- **Wording review:** two reasonable readings change legal attack count, duration, target tracking, hand/equipment legality or reserve timing; settle the reading before combining results. No favorable interpretation is automatically the intended exploit.
- **Keep/no-change review:** strong effects occur with real costs and official comparators answer different problems; preserve the Veteran’s equipment/body integration, contingency and fieldcraft identity.

## Direct answers to the sixteen final questions

1. **Defensibly balanced against complete revised Fighters?** Yes, conditionally within their broad envelope; moderate confidence. The audit supports testing, not a universal ceiling proof. Support/defense and permissive Weak Point remain the largest uncertainty.
2. **Early contact appropriate?** Strong/front-loaded but defensible;4.40 repeatable EV at3 in its adjacent damage case, with real control/hand/size costs and a low-rest advantage.
3. **Sustained damage across families?** Reasonable in the disclosed builds; feats/BA/Nick increase the chassis too. Reach-only/no-contact and one-target ranged assumptions materially reduce gains. No free stat/style is granted.
4. **Correction/split/movement valued appropriately?** Yes when separated: focused first-miss gain differs from distributed total; movement may be useful with zero follow-up and has no universal DPR value.
5. **Surge/rider ceiling problematic?** Strong finite scaling, no demonstrated recursive or broadly excessive ceiling. Two actions get two PF uses; once-turn riders/Nick remain limited. Radiant Strikes/Hunter’s Mark dips deserve actual trials.
6. **Replacement costs remain meaningful at5/11/20?** Yes. Their relative slot fraction falls, but absolute weapon/mastery/rider loss remains; at3 losing the only weapon can also lose PF. Hasty BA recovery pays a real BA and often loses GWM damage.
7. **Readiness/reserves/swaps too much simultaneous flexibility?** Not under stated timing/counts: two opening choices, one later unused choice, one swap/rest, two unknown identities and one shared reserve use/SR. Lasting actual sabotage/objects can persist, not permanent proficiency.
8. **Level15 meaningful in difficult attrition?** Yes, conditional rather than spectacular: improved THP, later preparation and BA-free healing/movement when Surge lines up with injury/resources. It can be weak after early full-HP Surge or exhausted SW.
9. **Hair/Hook/Parting appropriate including multiclass?** Strong and suitable for testing. Hair own-turn pressure and Rogue Parting/Ready are the leading routines; real Reaction/position/progression and competent alternatives moderate them.
10. **Capstone’s combined package appropriate?** Strong upper-envelope against one relevant threat; no evidence requires shortening duration. Its boss protection and save-resource preservation need live tests alongside full official defenses.
11. **Mandatory/weak/dominant Lesson packages?** Hair and broadly qualified Weak Point have the highest forecast combat pressure; FET/Sabotage and Concealment dominate suitable mission portfolios. Misdirect is weakest as a standalone mode. Empirical mandatory picks are not established.
12. **Party amplification has meaningful costs?** Generally yes. Full Help is expensive; Study evidence/action or Readiness choice, qualification, instruction and per-turn sharing matter. Routinely broad Weak Point qualification can make those costs insufficient.
13. **Actual exploits from items/feats/multiclass?** No infinite/recursive exploit found. Legal attack counts, stat requirements, hand use, current features, item eligibility and finite resources prevent several supposed ones. Strong optimized synergies remain real.
14. **Prior conclusions confirmed/corrected?** Core EV and original policy outputs reproduced; scope corrected for Champion extra style/Hew, BM policy/Relentless off-turn, EK allocation/complete spells, stateful timing/throwing, full-dice simulation and self-trigger Hair/Rogue comparisons.
15. **Strongest/weakest?** Core feature: capstone in a single-boss fight; early PF is the most front-loaded engine. Strongest party Lesson: qualified Weak Point. Weakest standalone procedure: Misdirect; weakest new core package relative to its level: conditional level15, though appropriate and useful.
16. **Change now vs live evidence?** No numerical/structural changes now. Clarify test sequences/weakness/reserve procedure rulings and collect paired evidence before any targeted adjustment.

## Reproduction and limitations

Run `python3 audit_models.py`, `python3 supplemental_models.py`, then `python3 validate_models.py` in the extracted calculation directory. Standard library only, Python3.10+. Seed/trials are in source/output. CSV/JSON snapshots contain unrounded values. Run `python3 refresh_workbook.py Veteran_Balance_Workbook.xlsx` to write a refreshed snapshot copy; live Excel formulas remain intact and recalculate on opening. Their cells are not disguised hard-coded outputs. The workbook’s live recurrence is one-target/one-action/fresh-start; the Python model handles the fuller target/turn policies.

`create_workbook.mjs` is the original artifact-tool author script, requiring Node and `@oai/artifact-tool` (available in the authoring runtime). The stdlib refresh path does not require that library. Live formulas cover probabilities, contact/control/correction, finite one-target recurrence, replacement costs, healing/resources, defense/saves, party packets and AC sensitivity. External tables are explicitly labeled and mapped in workbook_snapshot_map.json. Editing an amber live input updates only its dependent formulas; it does not magically rerun Python’s external policies.

Independent checks are in validation.json and workbook_live_check.json. The workbook exported without formula-error cells; changing primary modifier5→4 changed the .50 Contact EV4.425→3.925 and its dependent sequence, then inputs were restored. All twelve sheet previews were rendered and inspected. Earlier verification is in earlier_verification.json. Dataset coverage is a four-block convenience sample; no inaccessible empirical distributions, protected complete source texts or nonexistent playtest observations are included.

Important exclusions: no globally optimized target-death/weapon-switch search, no universal reaction/adjacency probabilities, no exhaustive EK spell policy, no exhaustive every-subclass multiclass ranking, no campaign magic-item frequency model and no verified population-level Lesson pick rate. Champion/BM/Psi/EK complete non-DPR packages are reviewed and selected strong alternatives priced; the numeric tables remain declared scenarios, not a synthetic combined score. These limitations reduce confidence in universal claims and do not justify presenting incomplete bounds as exact subclass parity.

## Source register

Rules facts use the official or licensed current sources below; project decisions come from the source/version table. Method assumptions and numerical outputs are this audit’s own. All web checks dated7October2026. Pages may contain purchase banners or legacy navigation; only their explicitly revised entries were used.

| Code | Source | URL |
| --- | --- | --- |
| R1 | Official revised classes and Champion | [Official revised classes and Champion](https://www.dndbeyond.com/sources/dnd/br-2024/character-classes) |
| R2 | Official revised glossary | [Official revised glossary](https://www.dndbeyond.com/sources/dnd/br-2024/rules-glossary) |
| R3 | Official revised equipment/masteries | [Official revised equipment/masteries](https://www.dndbeyond.com/sources/dnd/br-2024/equipment) |
| R4 | Live official PHB errata | [Live official PHB errata](https://www.dndbeyond.com/sources/dnd/sae/players-handbook) |
| R5 | Official PHB2024 errata v1 April2025 | [Official PHB2024 errata v1 April2025](https://media.dndbeyond.com/compendium-images/errata/PHB-24/PHB-2024_v1.pdf) |
| R6 | Licensed revised Fighter | [Licensed revised Fighter](https://roll20.net/compendium/dnd5e/Classes%3AFighter?expansion=33335) |
| R7 | Licensed revised Battle Master | [Licensed revised Battle Master](https://roll20.net/compendium/dnd5e/Subclasses%3ABattle%20Master?expansion=32231) |
| R8 | Licensed revised Eldritch Knight | [Licensed revised Eldritch Knight](https://roll20.net/compendium/dnd5e/Subclasses%3AEldritch%20Knight?expansion=32231) |
| R9 | Licensed revised Psi Warrior | [Licensed revised Psi Warrior](https://roll20.net/compendium/dnd5e/Subclasses%3APsi%20Warrior?expansion=32231) |
| R11 | Official spellcasting/slot limit | [Official spellcasting/slot limit](https://www.dndbeyond.com/sources/dnd/br-2024/spells) |
| R12 | Licensed revised Haste | [Licensed revised Haste](https://roll20.net/compendium/dnd5e/Spells%3AHaste?expansion=33335) |
| R13 | Licensed revised Shield | [Licensed revised Shield](https://roll20.net/compendium/dnd5e/Spells%3AShield?expansion=33335) |
| I1 | Licensed revised Necklace of Fireballs | [Licensed revised Necklace of Fireballs](https://roll20.net/compendium/dnd5e/Items%3ANecklace%20of%20Fireballs?expansion=33335) |
| I2 | Licensed revised Bracers of Archery | [Licensed revised Bracers of Archery](https://roll20.net/compendium/dnd5e/Items%3ABracers%20of%20Archery?expansion=33335&iframe=true) |
| M1 | RPGBOT Fundamental Math — legacy method, updated inputs | [RPGBOT Fundamental Math — legacy method, updated inputs](https://rpgbot.net/dnd5/characters/fundamental_math/) |
| M2 | Tabletop Builds quantitative primer — method only | [Tabletop Builds quantitative primer — method only](https://tabletopbuilds.com/a-primer-on-quantitative-evaluation-in-dd/) |
| M3 | Tabletop Builds quantitative evaluation2 — method only | [Tabletop Builds quantitative evaluation2 — method only](https://tabletopbuilds.com/quantitative-evaluation-2/) |
| M4 | Current transparent calculator assumptions/day convention | [Current transparent calculator assumptions/day convention](https://dndprovinggrounds.com/dpr-calculator/) |
| N1 | Licensed revised Air Elemental | [Licensed revised Air Elemental](https://roll20.net/compendium/dnd5e/Monsters%3AAir%20Elemental?expansion=33335) |
| N2 | Licensed revised Hill Giant | [Licensed revised Hill Giant](https://roll20.net/compendium/dnd5e/Monsters%3AHill%20Giant?expansion=33335) |
| N3 | Licensed revised Frost Giant | [Licensed revised Frost Giant](https://roll20.net/compendium/dnd5e/Monsters%3AFrost%20Giant?expansion=33335) |
| N4 | Official revised monster collection / Adult Red Dragon | [Official revised monster collection / Adult Red Dragon](https://www.dndbeyond.com/sources/dnd/br-2024/monsters) |
| C1 | Licensed revised multiclass prerequisites/progression | [Licensed revised multiclass prerequisites/progression](https://roll20.net/compendium/dnd5e/Rules%3AMulticlassing?expansion=32231) |
| C2 | Licensed revised Monk | [Licensed revised Monk](https://roll20.net/compendium/dnd5e/Classes%3AMonk?expansion=32231) |
| C3 | Licensed revised Barbarian | [Licensed revised Barbarian](https://roll20.net/compendium/dnd5e/Classes%3ABarbarian?expansion=33335) |
| C4 | Licensed revised Divine Smite | [Licensed revised Divine Smite](https://roll20.net/compendium/dnd5e/Spells%3ADivine%20Smite?expansion=32231) |
| C5 | Licensed revised Hunter’s Mark | [Licensed revised Hunter’s Mark](https://roll20.net/compendium/dnd5e/Spells%3AHunter%27s%20Mark?expansion=32231) |
| F1 | Licensed revised Great Weapon Master | [Licensed revised Great Weapon Master](https://roll20.net/compendium/dnd5e/Feats%3AGreat%20Weapon%20Master?expansion=32231&iframe=true) |
| F2 | Licensed revised Grappler | [Licensed revised Grappler](https://roll20.net/compendium/dnd5e/Feats%3AGrappler?expansion=32231&iframe=true) |
| F3 | Licensed revised Tavern Brawler | [Licensed revised Tavern Brawler](https://roll20.net/compendium/dnd5e/Feats%3ATavern%20Brawler?expansion=32231&iframe=true) |
| F4 | Licensed revised Polearm Master | [Licensed revised Polearm Master](https://roll20.net/compendium/dnd5e/Feats%3APolearm%20Master?expansion=32231&iframe=true) |
| F5 | Licensed revised Sentinel | [Licensed revised Sentinel](https://roll20.net/compendium/dnd5e/Feats%3ASentinel?expansion=32231&iframe=true) |
| F6 | Licensed revised Shield Master | [Licensed revised Shield Master](https://roll20.net/compendium/dnd5e/Feats%3AShield%20Master?expansion=32231&iframe=true) |
| F7 | Licensed revised Dual Wielder | [Licensed revised Dual Wielder](https://roll20.net/compendium/dnd5e/Feats%3ADual%20Wielder?expansion=32231&iframe=true) |
| F8 | Licensed revised Charger | [Licensed revised Charger](https://roll20.net/compendium/dnd5e/Feats%3ACharger?expansion=32231&iframe=true) |
| F9 | Licensed revised Crossbow Expert | [Licensed revised Crossbow Expert](https://roll20.net/compendium/dnd5e/Feats%3ACrossbow%20Expert?expansion=32231&iframe=true) |
| F10 | Licensed revised Archery | [Licensed revised Archery](https://roll20.net/compendium/dnd5e/Feats%3AArchery?expansion=32231&iframe=true) |
| F11 | Licensed revised Dueling | [Licensed revised Dueling](https://roll20.net/compendium/dnd5e/Feats%3ADueling?expansion=32231&iframe=true) |
| F12 | Licensed revised Two-Weapon Fighting | [Licensed revised Two-Weapon Fighting](https://roll20.net/compendium/dnd5e/Feats%3ATwo-Weapon%20Fighting?expansion=32231&iframe=true) |
| F13 | Licensed revised Thrown Weapon Fighting | [Licensed revised Thrown Weapon Fighting](https://roll20.net/compendium/dnd5e/Feats%3AThrown%20Weapon%20Fighting?expansion=32231&iframe=true) |
| F14 | Licensed revised Great Weapon Fighting | [Licensed revised Great Weapon Fighting](https://roll20.net/compendium/dnd5e/Feats%3AGreat%20Weapon%20Fighting?expansion=32231&iframe=true) |
| F15 | Licensed revised Unarmed Fighting | [Licensed revised Unarmed Fighting](https://roll20.net/compendium/dnd5e/Feats%3AUnarmed%20Fighting?expansion=32231&iframe=true) |
| F16 | Licensed revised Protection | [Licensed revised Protection](https://roll20.net/compendium/dnd5e/Feats%3AProtection?expansion=32231&iframe=true) |
| F17 | Licensed revised Interception | [Licensed revised Interception](https://roll20.net/compendium/dnd5e/Feats%3AInterception?expansion=32231&iframe=true) |
| F18 | Licensed revised Sharpshooter | [Licensed revised Sharpshooter](https://roll20.net/compendium/dnd5e/Feats%3ASharpshooter?expansion=32231&iframe=true) |
| SP1 | Licensed revised True Strike | [Licensed revised True Strike](https://roll20.net/compendium/dnd5e/Spells%3ATrue%20Strike?expansion=33335&iframe=true) |

**Current Balance Verdict:** **Strong but Acceptable**, moderate confidence; strongest in adjacent attrition builds and single-threat boss fights, with adjudication-sensitive party amplification and reaction routines still requiring live evidence.

Only evidence-supported immediate changes, in priority order:

1. Add separate own-turn/off-turn Hair examples and record the Reaction alternatives in the test protocol.
2. Record Weak Point’s evidence, DC, exploitation and single shared recipient on each turn.
3. Resolve and document reserve procedure timing for Correction before combining playtest results.

**No numerical or structural subclass change is supported before that testing.**
