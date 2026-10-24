# Bartitsu Rogue — 2024 Mechanical Balance Audit

**Rules/source cutoff: 5 October 2026.** Quantitative audit of the provisional locked version in Section 6 of *Bartitsu Rogue Subclass Design Report*. Companion: *Bartitsu_Balance_Workbook.xlsx*. Reproducibility bundle includes the models, source-derived monster data, results, workbook builder, and validation records.

## Executive Verdict

**Overall: Slightly Overtuned, with moderate confidence.** The low-level reaction concept is sound. The on-turn weapon damage is ordinary. The concern is the cumulative high-level package: unusually accessible, advantaged off-turn Sneak Attack; an accuracy-enhanced weapon; damage-free control; and, at level 17, three effects on each of potentially two Sneak Attacks between the starts of the Rogue's turns.

This is not a finding that every encounter is excessive. Against ranged attackers, saving-throw attacks, or enemies choosing other targets, much of the reaction engine disappears. Against adjacent attackers at level 13+, its **opportunity** is automatic on either hit or miss, subject to sight on the hit branch and reaction availability. Melee exposure is a substantial price, but Sap, Uncanny Dodge and attack-dependent control pay back some of that price.

| Subclass level | Classification | Confidence | Decisive observation |
|---|---|---|---|
| 3 | Strong but Acceptable | Moderate–high | One-attack on-turn damage below competent two-attack Rogues; conditional extra Sneak Attack compensates for melee/BA exposure |
| 9 | Strong but Acceptable | Moderate | One free effect is defensible; +1 Cane and reaction control add meaningful value; level 11 deserves separate testing |
| 13 | Slightly Overtuned | Moderate | Qualifying melee attack guarantees a counter opportunity; illustrative mixed DPR exceeds Nick/Aim by 37%, before control |
| 17 | Overtuned in favorable play; Slightly Overtuned overall | Moderate | Three effects, including free Joint Lock/Suppress/Daze, can be delivered twice without daily expenditure |

The classification is a design judgment, not a statistically measured population estimate. There is no official subclass DPR ceiling. The calculations establish magnitudes and breakpoints; actual target selection and control uptime remain playtest questions.

**Before formal testing:** prevent Cane bonus stacking, resolve mastery/unarmed/grapple wording, and test Perfect Leverage with a **1d6 discount while retaining three different effects**. Preserve Exploit an Opening, Create an Opening, the Cane progression and level 9's 1d6 discount. Counterstroke deserves focused high-attention testing; do not remove off-turn Sneak Attack as a principle.

## Project Material and Authority

I read the Design Report first, including its history, rejected approaches, Section 6 subclass text, rationale and unresolved questions. Its mechanical text matches the fingerprint supplied in this request. Intentional decisions include at-will reactions, no Extra Attack, no scaling martial-arts die, no additional defense chassis, no point pool, separate discounts for each effect, Joint Lock at 2d6, and Redirect at 5 feet. These decisions are preserved in the recommendations.

I also reviewed *Executive Verdict* and the mechanical portions of *Bartitsu: Historical Overview and Design Foundations*. The latter explains why close-range counters, improvised implements and leverage are core. No historical research was repeated. The originality report is useful for leads, not balance evidence. Its descriptions of Steady Aim as a feat, Soulknife weapon-die progression and an official Disarm Cunning Strike are incorrect for the final 2024 rules. The historical document's grapple discussion sometimes uses earlier opposed-check assumptions. None governs this audit.

A writing-block item identified as the earlier research prompt was found, but its authoritative readable content was unavailable; snippets and the available reports identify the relevant hazards. No separate design-chat transcript was available. The full current prompt and Design Report supply the operative constraints. No unseen chat decision is treated as authority.

## Methodology

### Frameworks and why they remain separate

| Framework | Published context | Assumptions used here | Why included / limitation |
|---|---|---|---|
| RPGBOT Fundamental Math [4] | 2014 edition,2021 | Primary modifier+3, then+4 at 4, +5 at 8; proficiency; original DMG-derived AC schedule | Transparent accuracy convention; arithmetic transferable, AC schedule is **not** a 2024 empirical law |
| Tabletop Builds quantitative evaluation [5] | 2014 edition,2021 | Exact expected value, conditional hit probabilities, crit dice, multiple attacks and resource/defense context | Transferable mathematics; obsolete 2014 power-attack feats and encounter assumptions not imported |
| Official 2024/SRD 5.2.1 empirical model [1] | Current revision | Equal weighting of actual statblocks in explicit CR bands; per-monster hit/save calculations | Reality check; sample is incomplete and not encounter-frequency weighted |
| Fixed60% and65% sensitivity | Analyst conventions, not official rules | Mundane attack accuracy fixed; Cane adds 5 percentage points per+1 before Advantage/caps | Separates conclusions from a preferred AC convention; fixed accuracy does not mean Cane accuracy is frozen |
| Exact encounter probability tree | This audit | Qualifying attention, incoming attacks, Sap, reaction policy, finite four-round Vex/poison states | Tests trigger/action-economy assumptions; attention probabilities are scenarios, not measured frequencies |

Treantmonk's current 2024 baseline video [6] and d4's 2024 sustained-baseline episode and linked models [7] were investigated. The full numerical assumptions/transcript or linked spreadsheets were inaccessible in the available retrieval system. I therefore **do not label any reproduced number “Treantmonk's 2024 benchmark”**. A 60% case is explicitly independent sensitivity, not a fabricated replication. This limitation is preferable to treating community summaries as authoritative. RPGBOT and Tabletop Builds publish enough mathematics to use transparently; official 2024 data supplies a third independent calibration.

No results from different systems are averaged. A benchmark tells us what happens under its own assumptions. The relevant question is whether the relative conclusion survives changing them.

### Character, combat and equipment defaults

Dexterity 16 at 3,18 at 5,20 by 9; normal proficiency; Constitution 14 for durability illustrations; studded leather AC 15/16/17; one-handed 1d6 Cane so a hand can be available for locks. No external buffs, multiclassing, origin-feat damage, magic items, optional legacy spells or shared Epic Boon in the main tables. Ordinary Sneak Attack qualification is assumed for ordinary comparators; Bartitsu's granted Advantage supplies it unless cancelled. Magic and optimized cases are separate.

On-turn Bartitsu uses Create an Opening. The strongest repeatable mundane Rogue comparison uses shortsword Vex plus scimitar Nick and Steady Aim. This comparator cannot move after aiming and must aim before moving; Bartitsu can move. A mobile Nick comparison and single-attack rapier comparisons are also shown. The extra Nick attack lacks positive ability damage without Two-Weapon Fighting. It benefits from first-hit Vex when applicable.

Four rounds per encounter is an illustration, varied to 2/4/6/8 for opening-round abilities. A six-encounter, four-round day illustrates 24 rounds, not an official mandatory day. No party composition or enemy-attention distribution is assumed universal.

At level 20 the main sustained table isolates repeatable attacks and excludes shared, episodic Stroke of Luck and the level 19 Epic Boon choice for every Rogue. Their effects are separately analyzed below; they are not absent from the chassis audit. Other classes' intrinsic level 20 improvements are included in their context models.

### Exact formulas

Let `h` be hit probability **including critical hits**, `c` the critical probability, `w` mean weapon dice, `m` flat damage, and `S` mean Sneak Attack dice after paid costs.

`h = max(.05,min(.95,(21 + attack bonus − AC)/20))` for ordinary attacks.

`h_adv = 1 − (1−h)^2`; `h_dis = h^2`.

Normal critical probability=.05; Advantage=.0975; Disadvantage=.0025. Cancelling Advantage and Disadvantage returns the ordinary distribution, regardless of the number of sources.

`Attack EV = h(w+m+S) + c(w+S)`.

The extra term doubles **dice only**, not flat Dexterity, Cane bonuses or Assassin's flat first-round bonus. A paid Sneak Attack die costs `3.5(h+c)` expected damage per attempted attack. Costs are paid on a landed Sneak Attack whether the target saves or not.

Saving throws: `failure = max(0,min(1,(DC−save bonus−1)/20))`. A natural 1 or 20 does not generally auto-fail/succeed an ordinary saving throw. Legendary Resistance, condition immunity, applicability and size restrictions are separate gates.

For Nick, first attack hit=`h 1`; second attack has Vex Advantage if the first hits. Sneak Attack landing=`h 1+(1−h 1)h`; Sneak Attack critical probability=`c 1+(1−h 1)c`. Weapon damage on the second attack uses the weighted Vex distribution even when Sneak Attack was spent already. This avoids multiplying the entire Sneak Attack by two attacks.

For an enemy with ordinary hit probability `e`, `n` qualifying melee attacks, and probability `s` the first attack has Sap:

`P(at least one miss) = 1 − [(1−s)e^n + s e^(n+1)]`.

Only the first incoming attack is initially disadvantaged. This formula assumes the Rogue reserves its reaction until a miss; an early Uncanny Dodge changes that policy. At 13+, Counterstroke changes the hit-or-miss opportunity to 1 for at least one eligible attack, not the counter's hit probability to 1.

`Reaction DPR = q × melee/reach gate × reaction-available gate × trigger probability × reaction-attack EV`.

The mixed illustration uses q=.60, melee/reach=.80, reaction availability=.90, giving effective attention `.432`. Low uses `.10` and one attack; favorable uses 1 and three attacks. Sight, continued reach and external reaction competition can further lower these rates. “Best case” here does not add external buffs.

### Computational verification

Wolfram Language supplied exact d20/Advantage/crit arithmetic, symbolic Sap trigger probabilities, Cunning Strike damage costs, independent-save distributions and AC sensitivities. Python independently enumerated d20 outcomes and damage distributions, modeled finite Vex/poison states and reaction policies, and produced the monster statistics. A seeded200,000-trial level 13 simulation produced 35.5134 versus the analytic 35.5425; the 0.0291 difference is sampling noise, not a model disagreement. Exact d20 enumerations matched formulas to numerical precision.

The companion workbook uses live Excel formulas, separate editable inputs and a linked chart. Its results were compared against Python, an AC input was changed and restored to test recalculation, exported formula caches were inspected, and opening views were rendered. Excel itself was not available for application-level QA. The scripts and JSON provide an independently rerunnable calculation path.

## Rules Audit

The SRD 5.2.1 [1], official current Basic Rules and Sage Advice [2–3], published PHB errata [8], and licensed final 2024 subclass entries [9–11] govern the rules. The official errata list checked has an April 2025 PHB update; no later Rogue/Sap rules change was located. The SRD portal still identifies 5.2.1 as its current English version and was updated March 2026. No 2014 text silently overrides it.

| Rule or interaction | Verified2024 result | Consequence |
|---|---|---|
| Rogue progression | SA 2/3/5/6/7/7/9/10d6 at audited levels; CS 5, Improved 11, Devious 14 | Level 5/11/14 are material interaction points |
| Sneak Attack | Once per **turn**, Finesse/Ranged weapon requirement, normal qualification | Off-turn SA legitimate; own-turn reaction does not permit a second SA that same turn |
| Cunning Strike | Used when dealing SA; no “your turn” restriction | Valid on reaction SA; package costs deducted before damage |
| Reaction reset | Regained at start of own turn | Model cycle is between own-turn starts; calendar rounds can straddle resets |
| Weapon Mastery | Rogue selects two kinds of proficient weapons | Sap property alone does not unlock it; Cane can occupy a normal selection |
| Sap | Hit imposes Disadvantage on target's next attack roll before start of your next turn | Not an entire Multiattack; reaction Cane can reapply |
| Steady Aim | BA, must not have moved; speed 0 rest of turn | Repeatable Advantage with movement cost; Assassin 9 removes speed 0 but not “not moved” prerequisite |
| Cunning Action | BA Dash, Disengage or Hide | Competes with Create/Aim; Hide has terrain/check/visibility constraints |
| Uncanny Dodge | Seen attacker hits with attack roll, reaction halves that attack's damage | No defense against save-only damage; one attack, not Multiattack |
| Unarmed Strike | Damage attack, or Grapple/Shove saving-throw options | Ordinary unarmed attacks aren't Finesse weapons; subclass must explicitly override |
| Grapple/Shove | Target chooses STR/DEX save; size no more than one larger; hand/reach for grapple | No opposed Athletics initiation; Expertise does not improve initial DC |
| Grappled | Speed 0; attacks against others disadvantaged; action escape Athletics/Acrobatics vs escape DC | Does not inherently grant attacker Advantage; Grappler feat can |
| Prone | Disadvantage on own attacks; attacks within 5 have Advantage, other distances Disadvantage; standing costs half speed | Speed 0 prevents standing; ranged allies may be penalized |
| Poisoned | Disadvantage on attacks and ability checks | Does not reduce saving throws; repeats/immunity matter |
| Blinded | Attack-roll effects, vision failure | Special senses/being able to perceive target can mitigate practical impact |
| Unconscious | Incapacitated, speed 0, drops held objects, prone, automatic STR/DEX-save failure; attacks advantaged; within 5 hit critical | Knock Out wakes on damage; do not credit unlimited party crit chains |
| Opportunity Attack | Reaction before creature leaves reach; can use unarmed options | Forced movement without target's movement/action/BA/reaction does not provoke |
| Daze | Next turn chooses one of movement/action/BA | Not stun; can choose stationary Multiattack; reactions/legendary actions not generally removed |
| Advantage cancellation | Any Advantage and Disadvantage cancel | Disadvantaged counters lose guaranteed SA unless another normal qualifier exists |

### Genuine wording issues, independent of balance

1. **Unarmed Finesse override:** “count as weapons with Finesse for you” reasonably permits Dexterity attack/damage and SA, but ordinary Unarmed Strike damage is explicitly 1+Strength and “weapon” features may have narrower requirements. Add an explicit Dexterity attack-and-damage sentence and clarify that damaging unarmed attacks count as Finesse weapons for your Rogue features. Preserve the intended broader feature compatibility only if deliberately desired. They do not acquire Light, Nick, Heavy, Thrown or a mastery.
2. **Mastery access:** choose either “you can select your Cane as one of your Weapon Mastery choices” or explicit automatic access. Current conservative reading consumes one selection. Automatically granting Sap is a small versatility increase, not extra damage to the already-selected Cane. No universal mastery for random improvised weapons follows.
3. **Magic bonuses:** a practitioner skill bonus and an item's magic bonus can be read as separate stacking benefits. State: **“If an object designated as your Cane already grants a bonus to its attack and damage rolls, use the higher of that bonus and Practiced Cane's bonus; do not add them together.”** State separately how unrelated riders are treated; this sentence does not erase fire damage or special item functions.
4. **Joint Lock:** unlike an ordinary Unarmed Strike, the custom effect doesn't explicitly require the target within grapple reach or specify escape DC. Add **“The target must be within your reach, and the grapple's escape DC equals your Cunning Strike save DC.”** A ranged Sneak Attack cannot maintain a remote grapple beyond reach. A free hand is required when the effect resolves and remains occupied while holding the grapple.
5. **Redirect:** identify movement along a legal path to an unoccupied space, rather than teleportation. Forced movement does not provoke ordinary OAs. Hazard movement may be legal and valuable; don't silently forbid its intended repositioning.
6. **Custom effects:** identify the common Cunning Strike DC and pay each cost separately. Effects occur immediately after attack damage, not before it. Use the core Simultaneous Effects rule unless the subclass intentionally overrides it: the player/GM whose turn it is determines ordering; duplicate identical effects are disallowed by the level 17 wording. Existing official save/type/size restrictions remain in force.
7. **Cane conversion:** clarify whether designating a magic quarterstaff retains its original weapon properties or uses the Cane profile. Cosmetic umbrellas don't gain every printed magic-staff spellcasting permission. A replacement after a rest creates/designates a Cane, not a duplicate magic item.

The discounts and custom effects are **not restricted to Cane/melee hits** in the current text. Poison, Trip, Withdraw, Disarm, Redirect, Suppress and Devious effects can accompany otherwise legal ranged SA. Joint Lock requires close reach. Therefore melee danger cannot justify the entirety of Scientific/Perfect Leverage.

## Benchmark Tables

### Same assumptions, baseline damage at every required level

65% mundane accuracy, actual Cane bonuses applied, crits included. No CS costs in this damage-only table. Bartitsu mixed reaction attention=.432, two incoming attacks, initially Sap if the on-turn Cane hit the relevant attacker. All values are expected damage per modeled cycle. “No reaction” comparators can still obtain ordinary OAs in play; those are not presumed every round.

| Level | Build | On-turn DPR | Reaction DPR | Total DPR | Control | Defense | Resources |
|---|---|---|---|---|---|---|---|
| 3 | Baseline rapier | 10.00 | 0 | 10.00 | Base CS at 5 | UD 5/Evasion 7 | At will |
| 3 | Rapier Steady Aim | 13.85 | 0 | 13.85 | Base CS | Speed 0; UD | At will |
| 3 | Nick + Steady Aim | 16.76 | 0 | 16.76 | Base CS | Speed 0; UD | At will |
| 3 | Mobile Vex/Nick | 14.09 | 0 | 14.09 | Base CS | BA free; UD | At will |
| 3 | Assassin | 17.48 | 0 | 17.48 | Poison 13 separate | Aim mobile 9 | First-round bonus |
| 3 | Thief | 16.76 | 0 | 16.76 | Fast Hands; CS | Mobility/stealth | Extra turn first round 17 |
| 3 | Soulknife no Homing | 17.32 | 0 | 17.32 | Rend Mind 17 separate | Teleport/invisibility | Blades at will |
| 3 | Soulknife Homing available | 17.32 | 0 | 17.32 | As above | As above | Finite psi dice |
| 3 | Arcane Trickster | 16.76 | 0 | 16.76 | Spells; extra Trip 13 | Shield options | Nick at will / Help vulnerable |
| 3 | Bartitsu | 12.87 | 4.54 | 17.41 | Discounted CS 9 | Sap + UD; melee | At will |
| 5 | Baseline rapier | 13.10 | 0 | 13.10 | Base CS at 5 | UD 5/Evasion 7 | At will |
| 5 | Rapier Steady Aim | 18.13 | 0 | 18.13 | Base CS | Speed 0; UD | At will |
| 5 | Nick + Steady Aim | 21.35 | 0 | 21.35 | Base CS | Speed 0; UD | At will |
| 5 | Mobile Vex/Nick | 18.05 | 0 | 18.05 | Base CS | BA free; UD | At will |
| 5 | Assassin | 22.55 | 0 | 22.55 | Poison 13 separate | Aim mobile 9 | First-round bonus |
| 5 | Thief | 21.35 | 0 | 21.35 | Fast Hands; CS | Mobility/stealth | Extra turn first round 17 |
| 5 | Soulknife no Homing | 22.50 | 0 | 22.50 | Rend Mind 17 separate | Teleport/invisibility | Blades at will |
| 5 | Soulknife Homing available | 22.50 | 0 | 22.50 | As above | As above | Finite psi dice |
| 5 | Arcane Trickster | 21.35 | 0 | 21.35 | Spells; extra Trip 13 | Shield options | Nick at will / Help vulnerable |
| 5 | Bartitsu | 17.16 | 5.68 | 22.84 | Discounted CS 9 | Sap + UD; melee | At will |
| 9 | Baseline rapier | 18.65 | 0 | 18.65 | Base CS at 5 | UD 5/Evasion 7 | At will |
| 9 | Rapier Steady Aim | 25.84 | 0 | 25.84 | Base CS | Speed 0; UD | At will |
| 9 | Nick + Steady Aim | 29.66 | 0 | 29.66 | Base CS | Speed 0; UD | At will |
| 9 | Mobile Vex/Nick | 25.31 | 0 | 25.31 | Base CS | BA free; UD | At will |
| 9 | Assassin | 31.81 | 0 | 31.81 | Poison 13 separate | Aim mobile 9 | First-round bonus |
| 9 | Thief | 29.66 | 0 | 29.66 | Fast Hands; CS | Mobility/stealth | Extra turn first round 17 |
| 9 | Soulknife no Homing | 31.24 | 0 | 31.24 | Rend Mind 17 separate | Teleport/invisibility | Blades at will |
| 9 | Soulknife Homing available | 34.62 | 0 | 34.62 | As above | As above | Finite psi dice |
| 9 | Arcane Trickster | 29.66 | 0 | 29.66 | Spells; extra Trip 13 | Shield options | Nick at will / Help vulnerable |
| 9 | Bartitsu | 26.62 | 9.44 | 36.06 | Discounted CS 9 | Sap + UD; melee | At will |
| 11 | Baseline rapier | 21.10 | 0 | 21.10 | Base CS at 5 | UD 5/Evasion 7 | At will |
| 11 | Rapier Steady Aim | 29.25 | 0 | 29.25 | Base CS | Speed 0; UD | At will |
| 11 | Nick + Steady Aim | 33.37 | 0 | 33.37 | Base CS | Speed 0; UD | At will |
| 11 | Mobile Vex/Nick | 28.62 | 0 | 28.62 | Base CS | BA free; UD | At will |
| 11 | Assassin | 36.00 | 0 | 36.00 | Poison 13 separate | Aim mobile 9 | First-round bonus |
| 11 | Thief | 33.37 | 0 | 33.37 | Fast Hands; CS | Mobility/stealth | Extra turn first round 17 |
| 11 | Soulknife no Homing | 34.80 | 0 | 34.80 | Rend Mind 17 separate | Teleport/invisibility | Blades at will |
| 11 | Soulknife Homing available | 38.58 | 0 | 38.58 | As above | As above | Finite psi dice |
| 11 | Arcane Trickster | 33.37 | 0 | 33.37 | Spells; extra Trip 13 | Shield options | Nick at will / Help vulnerable |
| 11 | Bartitsu | 30.14 | 7.36 | 37.51 | Discounted CS 9 | Sap + UD; melee | At will |
| 13 | Baseline rapier | 23.55 | 0 | 23.55 | Base CS at 5 | UD 5/Evasion 7 | At will |
| 13 | Rapier Steady Aim | 32.66 | 0 | 32.66 | Base CS | Speed 0; UD | At will |
| 13 | Nick + Steady Aim | 37.08 | 0 | 37.08 | Base CS | Speed 0; UD | At will |
| 13 | Mobile Vex/Nick | 31.93 | 0 | 31.93 | Base CS | BA free; UD | At will |
| 13 | Assassin | 40.19 | 0 | 40.19 | Poison 13 separate | Aim mobile 9 | First-round bonus |
| 13 | Thief | 37.08 | 0 | 37.08 | Fast Hands; CS | Mobility/stealth | Extra turn first round 17 |
| 13 | Soulknife no Homing | 38.35 | 0 | 38.35 | Rend Mind 17 separate | Teleport/invisibility | Blades at will |
| 13 | Soulknife Homing available | 42.36 | 0 | 42.36 | As above | As above | Finite psi dice |
| 13 | Arcane Trickster | 37.08 | 0 | 37.08 | Spells; extra Trip 13 | Shield options | Nick at will / Help vulnerable |
| 13 | Bartitsu | 35.54 | 15.35 | 50.90 | Discounted CS 9 | Sap + UD; melee | At will |
| 14 | Baseline rapier | 23.55 | 0 | 23.55 | Base CS at 5 | UD 5/Evasion 7 | At will |
| 14 | Rapier Steady Aim | 32.66 | 0 | 32.66 | Base CS | Speed 0; UD | At will |
| 14 | Nick + Steady Aim | 37.08 | 0 | 37.08 | Base CS | Speed 0; UD | At will |
| 14 | Mobile Vex/Nick | 31.93 | 0 | 31.93 | Base CS | BA free; UD | At will |
| 14 | Assassin | 40.43 | 0 | 40.43 | Poison 13 separate | Aim mobile 9 | First-round bonus |
| 14 | Thief | 37.08 | 0 | 37.08 | Fast Hands; CS | Mobility/stealth | Extra turn first round 17 |
| 14 | Soulknife no Homing | 38.35 | 0 | 38.35 | Rend Mind 17 separate | Teleport/invisibility | Blades at will |
| 14 | Soulknife Homing available | 42.36 | 0 | 42.36 | As above | As above | Finite psi dice |
| 14 | Arcane Trickster | 37.08 | 0 | 37.08 | Spells; extra Trip 13 | Shield options | Nick at will / Help vulnerable |
| 14 | Bartitsu | 35.54 | 15.35 | 50.90 | Discounted CS 9 | Sap + UD; melee | At will |
| 17 | Baseline rapier | 28.45 | 0 | 28.45 | Base CS at 5 | UD 5/Evasion 7 | At will |
| 17 | Rapier Steady Aim | 39.49 | 0 | 39.49 | Base CS | Speed 0; UD | At will |
| 17 | Nick + Steady Aim | 44.51 | 0 | 44.51 | Base CS | Speed 0; UD | At will |
| 17 | Mobile Vex/Nick | 38.54 | 0 | 38.54 | Base CS | BA free; UD | At will |
| 17 | Assassin | 55.23 | 0 | 55.23 | Poison 13 separate | Aim mobile 9 | First-round bonus |
| 17 | Thief | 55.64 | 0 | 55.64 | Fast Hands; CS | Mobility/stealth | Extra turn first round 17 |
| 17 | Soulknife no Homing | 45.47 | 0 | 45.47 | Rend Mind 17 separate | Teleport/invisibility | Blades at will |
| 17 | Soulknife Homing available | 50.05 | 0 | 50.05 | As above | As above | Finite psi dice |
| 17 | Arcane Trickster | 44.51 | 0 | 44.51 | Spells; extra Trip 13 | Shield options | Nick at will / Help vulnerable |
| 17 | Bartitsu | 44.69 | 19.31 | 64.00 | Discounted CS 9 | Sap + UD; melee | At will |
| 20 | Baseline rapier | 30.90 | 0 | 30.90 | Base CS at 5 | UD 5/Evasion 7 | At will |
| 20 | Rapier Steady Aim | 42.90 | 0 | 42.90 | Base CS | Speed 0; UD | At will |
| 20 | Nick + Steady Aim | 48.22 | 0 | 48.22 | Base CS | Speed 0; UD | At will |
| 20 | Mobile Vex/Nick | 41.85 | 0 | 41.85 | Base CS | BA free; UD | At will |
| 20 | Assassin | 60.42 | 0 | 60.42 | Poison 13 separate | Aim mobile 9 | First-round bonus |
| 20 | Thief | 60.28 | 0 | 60.28 | Fast Hands; CS | Mobility/stealth | Extra turn first round 17 |
| 20 | Soulknife no Homing | 49.03 | 0 | 49.03 | Rend Mind 17 separate | Teleport/invisibility | Blades at will |
| 20 | Soulknife Homing available | 53.84 | 0 | 53.84 | As above | As above | Finite psi dice |
| 20 | Arcane Trickster | 48.22 | 0 | 48.22 | Spells; extra Trip 13 | Shield options | Nick at will / Help vulnerable |
| 20 | Bartitsu | 48.39 | 20.91 | 69.30 | Discounted CS 9 | Sap + UD; melee | At will |

Assassin table uses Nick/Aim plus flat first-round damage and, at 17, first-round CON-save doubling of the SA-bearing attack. It does not assume every enemy is surprised or double both weapon attacks. Envenom adds a separate save-dependent poison stream discussed below. Thief 17 includes one extra own turn in a four-round encounter, not permanent double turns. Soulknife Homing is a **pool-available envelope**, not unlimited daily dice. Arcane Trickster chooses the better of mundane Nick/Aim or Intelligence 16 True Strike with familiar Help; it does not silently get Intelligence 20 as well as Dexterity 20.

### Environment sensitivity

Low qualifying attention=.10, one attack; mixed=.432, two; favorable=1, three. All include own-turn Create. Zero eligible melee attacks means reaction DPR 0 and total equals on-turn DPR. Ranged-only and save-only encounters belong to that zero-trigger case.

| Level | On-turn | Low total | Mixed total | Favorable total | Mixed reaction | Mixed / Nick Aim |
|---|---|---|---|---|---|---|
| 3 | 12.87 | 13.73 | 17.41 | 24.44 | 4.54 | 1.04 |
| 5 | 17.16 | 18.21 | 22.84 | 31.91 | 5.68 | 1.07 |
| 9 | 26.62 | 28.41 | 36.06 | 50.62 | 9.44 | 1.22 |
| 11 | 30.14 | 31.41 | 37.51 | 50.46 | 7.36 | 1.12 |
| 13 | 35.54 | 39.10 | 50.90 | 71.08 | 15.35 | 1.37 |
| 14 | 35.54 | 39.10 | 50.90 | 71.08 | 15.35 | 1.37 |
| 17 | 44.69 | 49.16 | 64.00 | 89.39 | 19.31 | 1.44 |
| 20 | 48.39 | 53.23 | 69.30 | 96.79 | 20.91 | 1.44 |

At 13 the mixed four-round totals are 203.59 Bartitsu versus 148.33 Nick/Aim. At 17 they are 256.00 versus 178.03. In a 24-round illustration they become 1535.99 versus 1068.18 at 17 **if the same opportunity assumptions persist**. These are expected output totals, not a claim that a melee Rogue survives uninterrupted 24-round exposure.

## Feature-by-Feature Findings

### Bartitsu Training — Appropriate

Proficiency and Finesse mostly expand options. A 1d4 improvised object is weaker than a rapier; damaging unarmed strikes using Dexterity deal 1+Dex, with no ordinary weapon die to double on a crit. At 3, advantaged unarmed SA averages 10.34 against the 65% mundane-accuracy target, versus 12.87 with a 1d6 Cane or 13.85 with a rapier. Training doesn't create Extra Attack or Light/Nick.

Dex grapple DC is 13/15/17/17/18/18/19/19. A Strength 8 Rogue's ordinary grapple DC is 9/10/11/11/12/12/13/13, a four-to-six-point improvement, equivalent to 20–30 percentage points against an unsaturated save. A comparable Dex Monk already enjoys this consolidation. A Strength-based competent grappler reaches the same DC with its primary stat. This makes Rogue grappling viable; it does not improve a specialist's DC beyond the normal formula. Sacrificing the Rogue's single damaging action attack for a save-based grapple is expensive until Grappler or Joint Lock integrates it with damage.

### Create an Opening — Appropriate

At baseline 65%, Advantage raises hit probability 65%→87.75% and crit 5%→9.75%. At 3 it raises Cane attack EV 9.30→12.87, a 3.57 gain. At 13, after+2 Cane, it raises hit 75%→93.75% and damage 27.65→35.54, a 7.89 gain. Advantage also supplies ordinary SA qualification.

Steady Aim offers the same mathematical improvement with wider weapon/range eligibility but forfeits movement. Create exchanges that movement restriction for 5-foot range, a narrow weapon list and melee risk. Hide requires suitable concealment, a check and the hidden condition; Vex relies on prior hits; Nick offers an extra chance and frees the BA for mobility or Aim. Create is superior to Aim for a mobile Cane attack, inferior in safety/range, and not superior to the complete ordinary Rogue setup toolkit. It competes with Dash, Disengage, Hide and feat/other-class BA attacks.

### Exploit an Opening — Strong, acceptable at 3–12

One valid reaction attack has the same EV as the advantaged on-turn Cane attack:12.87 at 3,26.62 at 9,30.14 at 11. That is large conditional damage but depends on an enemy missing an adjacent melee attack, plus reaction availability. It is neither inherently illegitimate nor safely assumed rare.

Against incoming hit probability 60%, no Sap gives 40/64/78.4% miss opportunities for 1/2/3 attacks. Certain Sap gives 64/78.4/87.04%. Against 90%, those become 10/19/27.1% versus 19/27.1/34.39%. High-accuracy enemies suppress the engine before Counterstroke. The on-turn Cane must hit and Sap must affect the same attacker; the model uses that probability rather than automatic Sap.

The mixed totals at 3/5 are 17.41/22.84, close to competent official/two-attack Rogues. At 9 the 36.06 mixed result is stronger than 29.66 Nick/Aim but within the broader resource-bearing martial range. At 11, a higher-accuracy enemy band drops reaction contribution enough that damage alone isn't excessive. This illustrates why “two Sneak Attacks means double DPR” is wrong before 13.

### Cane — Appropriate; wording fixes needed

1d6 one-handed is below rapier 1d8, while versatile 1d8 trades hand availability for one mean damage. That adds `h+c`:0.975 at 3,1.035 at 13,1.0575 at 17 per attempted advantaged attack. Over two attacks it is still only about 2 damage. Using a lock occupies a hand and usually returns later Cane attacks to 1d6. Releasing/regripping a two-handed weapon does not permanently supply an extra grapple hand.

Sap is a strong defensive mastery but comparable to the defense/control built into ordinary masteries. A signature replacement after a rest does not generate money, magic bonuses or duplicate items. Automatic Sap versus a normal mastery selection changes versatility rather than the signature attack's modeled DPR. Recommend ordinary selection with explicit wording.

### Practiced Cane — Strong, acceptable without stacking

Against the 65% mundane-accuracy benchmark, Cane's ordinary accuracy becomes 70/75/80% at 9/13/17, Advantage 91/93.75/96%. Relative to the same 1d6 weapon with no bonus, the single-attack damage gain is 1.76/3.86/6.18 respectively. The SA landing gain with Advantage is 3.25/6/8.25 percentage points. Accuracy and damage gains are applied again on a reaction, so favorable two-attack gains double.

This is meaningful bounded-accuracy improvement but resembles access to+1/+2/+3 equipment; it is not an automatic extra attack. Soulknife's miss correction can be stronger while its pool lasts, and Devotion Paladin has a class-owned attack bonus with a different chassis/resource budget. If ordinary comparators also have equivalent magic weapons, the Cane's relative equipment advantage largely disappears. Do not simultaneously give Bartitsu its skill bonus and assume other Rogues never find weapons in an actual magic-rich campaign.

**Magic-item stress test:** at 17, greater-of+3 remains 44.69 per advantaged attack. Stacking a+3 item with+3 skill produces 49.30, +4.61 per attack/+9.22 in the guaranteed two-attack case. Ordinary hit 80%→95%, Advantage 96%→99.75%. At 13, +3 item alone 37.29 versus stacking+5 at 40.35. Stacking is an avoidable progression advantage, not infinite accuracy: natural 1 still matters. Nonstacking language is the narrow fix; no change to+1/+2/+3 itself is supported.

### Scientific Leverage — Strong; retain 1d6 at 9

The expected one-die refund at 9 is 3.526 per attempted advantaged attack, or 3.875 conditional on a hit including its crit chance. At 11 it remains 3.526; at 13 it is 3.623. Improved Cunning Strike at 11 doubles the refund when two eligible effects would each cost at least one die. An off-turn hit can receive another refund. Refund is not the same as successful control: saves and applicability are separate.

Free Poison/Trip/Withdraw/Disarm/Redirect are powerful specialization. Poison immunity, strong CON saves, Trip size, target choice on Redirect and real positional utility keep their expected value below the superficially alarming “free condition every turn” description. Level 9 official subclass features are often utility-heavy; Bartitsu is distinctly combat-heavy, but one free rider plus a modest Cane bonus is not sufficient evidence for a mandatory nerf.

The level 11 combination is a stronger inflection than 9: free Trip+free Poison can force two saves with full damage; Trip+Joint Lock costs 1 die. This warrants testing, especially because both packages can recur on reaction SA. Do not restrict all 9 mechanics to melee merely to rationalize balance: ranged use is currently legal and is part of the text being audited.

### Disarm — Appropriate at 1d6 base

Free after 9. A failed STR save can remove a weapon/focus, but many monsters have no relevant held object, and natural attacks remain available. Picking up an object can be inexpensive if the item remains accessible; the meaningful version involves retrieval denial, an ally taking it, terrain or follow-up control. Dropping a focus does not universally shut down spells: verbal/somatic/no-cost-material alternatives, component pouches, innate monster actions and multiple weapons matter. The rule does not destroy held objects or disarm embedded natural weapons. No cost increase is supported without evidence of pervasive item-denial encounters.

### Redirect — Appropriate at 1d6 base

Free after 9, but target chooses its better STR/DEX save; size gate applies. Five feet frequently changes little; at ledges, hazards, auras or grapple-separation thresholds it can be worth much more than 3.5 damage. Such terrain/party dependence is normal forced-movement utility. It does not itself generate an OA. Clarify path/reach interactions; retain 5 feet and base 1 die.

### Joint Lock — Strong at 2d6; problematic mainly when free at 17

At 9–16 it costs 1 die after discount, demands a free hand and proximity, and lets the target choose its better save. By itself it does not impose disadvantage against the grappler or grant Advantage. Combined with Trip, speed 0 prevents standing. The target can use an action to escape, attack the grappler with disadvantage from Prone, teleport, incapacitate the grappler or create forced separation. Enemy allies can break the geometry. This is a real action/movement lock but not stun.

Base 2d6 is defensible through 16. At 17 the current 2 die discount removes its remaining price, permitting Trip+Lock+Daze with full SA damage; that cumulative package is the concern. Keep Joint Lock's base cost and tune the high-level discount instead of punishing it at 9.

### Suppress — Appropriate at 2d6

One die paid at 9–16. Prevents reactions until start of your next turn on failed DEX save. Useful for allied movement, shields/counterspell-like reactions where available, or escaping without OAs. Withdraw already gives the Rogue safe immediate movement without a save, so Suppress earns its cost mainly through party utility or denying a relevant non-OA reaction. It does not cancel the attack already triggering a counter or remove legendary actions. Free at 17 is a meaningful party support rider; not independently a critical issue.

### Counterstroke — Strong; over budget under sustained high attention

At 13, a seen adjacent melee attack either misses (Exploit) or hits (UD+Counterstroke). Conditional opportunity=100%, whether the attack's ordinary hit probability is 30% or 95%. Conditional damage=35.54 at default target accuracy; hit probability 93.75%; critical 9.75%. Enemy accuracy determines how much UD/Sap helps and the defensive branch, rather than whether any counter is available.

Mixed contribution 15.35 gives 50.90 total. Guaranteed attention gives 71.09, versus 37.08 Nick/Aim,42.36 pool-available Soulknife, and roughly 40–42 Assassin in this illustrative four-round environment. That ceiling is too high to dismiss as “Rogues sometimes get an OA anyway.” It is much more reliable when the Rogue is attacked, doesn't require ally resources, and adds control as well.

But the qualifying-attention rate is decisive: a 10% environment adds only 3.55. Counterstroke does not create another reaction and does not protect against save-only attacks. It deserves a high-attention playtest gate rather than an automatic removal of reaction SA. Optional numerical tuning is recalculated in Recommendations.

### Perfect Leverage — Overtuned as a complete at-will package

Current 17 costs are Poison 0, Trip 0, Withdraw 0, Disarm 0, Redirect 0, Joint Lock 0, Suppress 0, Daze 0, Obscure 1, Knock Out 4 dice. Three distinct effects can accompany each SA. Thus full damage can coexist with three control attempts; a reaction can do it again. Daze is substantially weaker than stun, and Huge targets/immunities remove some options, but minion/weapon-user encounters still expose a broad free-control ceiling.

The smallest supported first test is **keep three effects, retain the 1 die discount**. That keeps the specialist identity and free basic tactics while retaining prices for Lock, Suppress, Daze, Obscure and Knock Out. Do not simultaneously remove the third effect and reduce the discount without testing the narrower change.

## Synergy Findings

### Cane + Sap + Exploit

Sap increases one attack's miss chance by `e−e²`, peaking at 25 percentage points when enemy hit chance 50%. At ordinary 40/60/80/95% accuracy, the increment is 24/24/16/4.75 points. Weighted by the Cane hit and same-attacker probabilities, it is smaller. For two attacks at enemy 60% hit and on-turn 87.75% Cane hit, miss-trigger probability 64%→76.636%, an increase 12.636 points; at 3 this is 1.626 conditional extra expected damage before attention weighting,0.703 under.432 attention.

A landed counter can Sap the next incoming attack. That is a legitimate, positive, bounded synergy: one additional attack roll affected, one reaction used, and no additive stacking with existing Poison/Prone Disadvantage. At 13+ Sap no longer increases total counter opportunity, because both hit and miss qualify. It remains defensive and changes which branch spends UD. Sap is not the feature pushing high-level reaction frequency beyond 100%.

### Scientific Leverage + Improved Cunning Strike; Trip + Joint Lock

At 11 free Trip+Poison preserves all six SA dice; Trip+Lock preserves five. With representative DC 17, DEX save+5 and chosen STR/DEX+6, failure rates 55% and 50% give 27.5% joint success **conditional on the hit**, about 25.0% per advantaged Cane attempt. Against weaker DEX+2/choice+4, rates 70% and60% give 42% joint success,38.2% per attack. If two independent attempts are available, probability at least one lock combo succeeds is `1−(1−p)^2` for the same target and unchanged gates, not simply double p.

The empirical whole-band level 11 effective joint success is 16.3% per hit after size/immunity gates; at 13 it is 19.3%. This low aggregate is heavily influenced by Huge creatures and is not representative of eligible humanoids. Do not conclude the combo is weak against eligible foes from the aggregate, or assume it affects dragons because it dominates a medium enemy.

Escape is an action check versus the explicit proposed escape DC. At DC 18, escape skill+8 succeeds 55%, +3 succeeds 30%; the expected action cost is not always one action. Poison also disadvantages the escape **check**, creating another synergy if simultaneously applied. Grappler's Expertise improves its own escape or related checks, not the DC forcing the enemy's initial save.

### Counterstroke + UD; reaction SA + Cunning Strike

UD and the counter use **the same reaction**. On a hit they combine offense with halving one attack, reducing the normal choice cost. On an early miss, Exploit forfeits UD against later hits. On a low-damage early hit, accepting UD+counter forfeits a potentially more valuable later UD. Opportunity attacks, Defensive Duelist and other reactions compete.

Off-turn Cunning Strike is legal. Prone or Poison on the counter can disadvantage remaining attacks; it cannot undo the triggering hit. Withdraw can immediately move the Rogue out of reach and truncate attacks only if the enemy cannot follow/retarget. Daze concerns the **next** turn and doesn't cancel current Multiattack. Obscure can affect the rest of the current turn and the next turn; duration starts when applied. Knock Out wakes on subsequent damage and should not be credited for damage that would end it.

Repeated conditions do not stack. Reapplying Trip to an already-Prone target or Grapple to an already-held target is not another full control benefit, and a boss need not spend LR on redundant effects. Packages can target different attackers/targets, refresh useful durations, or switch to different applicable effects. For a static eligible target with three independent 60% failure effects and no escape/expiration, two landed attempts increase the probability all three are eventually established from 21.6% to 59.27%; including 96% accuracy on each guaranteed-opportunity attack gives 56.28%. Those are persistence upper bounds, not six distinct useful conditions.

Two packages per cycle are possible. They are not guaranteed: at 17 with mixed attention, expected landed packages are `.96×(1+.432)=1.37472`; favorable attention gives 1.92. Applying three save-based effects means 4.124 or 5.76 expected initial saves per cycle when all three are applicable. Withdraw does not force a save; invalid effects don't create meaningful save pressure.

### Perfect Leverage combination stress tests

For independent failure probabilities a,b,c on a fixed target: at least one=`1−(1−a)(1−b)(1−c)`; at least two=`ab+ac+bc−2 abc`; all three=`abc`. Shared monster identity makes population mixtures correlated, so empirical results calculate these per creature and then average, rather than multiplying mean failure rates.

Representative fixed-target tests (eligible, no immunity or LR use):

| Failure probabilities | At least one | At least two | All three | Expected failed saves across six valid saves |
|---|---:|---:|---:|---:|
| .20,.20,.20 |48.8%|10.4%|0.8%|1.2|
| .40,.40,.40 |78.4%|35.2%|6.4%|2.4|
| .60,.60,.60 |93.6%|64.8%|21.6%|3.6|
| .80,.80,.80 |99.2%|89.6%|51.2%|4.8|
| .60,.50,.40 |88.0%|50.0%|12.0%|3.0|

The last column conditions on **both attacks landing** and six independent saves being applicable. Knock Out-first packages require the conditional calculation below rather than this independent-roll formula. Multiply by actual package/attack rates for encounter output.

Empirical CR 17–24 sample, DC 19, before voluntary LR spending. Trip/Lock/Redirect include Medium Rogue's size gate; immunity gates where applicable. Disarm assumes a relevant held object for this numerical column—an optimistic applicability bound, not proof every dragon carries a weapon:

| Combination | At least 1 | At least 2 | All 3 | Expected failures / landed package |
|---|---|---|---|---|
| Trip+Joint Lock+Daze | 0.55 | 0.10 | 0.03 | 0.68 |
| Trip+Suppress+Daze | 0.80 | 0.31 | 0.03 | 1.14 |
| Disarm+Redirect+Daze | 0.74 | 0.28 | 0.03 | 1.05 |
| Obscure+Trip+Suppress | 0.82 | 0.39 | 0.03 | 1.24 |
| Knock Out+Trip+Suppress | 0.80 | 0.31 | 0.03 | 1.14 |
| Knock Out+Trip+Suppress (KO first) | 0.80 | 0.49 | 0.09 | 1.39 |

Trip+Joint Lock+Daze is weakened against this high-CR sample because most targets are too large for Trip/Lock. Against medium minions the same package can have the far higher probabilities above. Obscure and Knock Out use their ordinary save/duration rules; the row gives **initial save outcomes**, not sustained incapacitation or unlimited party damage.

**Knock Out ordering exception:** effects happen after the attack’s damage. If KO resolves first and succeeds, Unconscious makes subsequent STR/DEX saves fail automatically. For an eligible target with KO failure probability a and Trip/Suppress ordinary failures b,c, ordered probabilities are at least one=`a+(1−a)[1−(1−b)(1−c)]`, at least two=`a+(1−a)bc`, all three=`a`, and expected failed saves=`3 a+(1−a)(b+c)`. With a=.40,b=c=.60, these are 90.4%,61.6%,40.0%,1.92, rather than the independent 90.4%,55.2%,14.4%,1.60. Trip is redundant while the target remains unconscious because it is already Prone; it is fallback if KO fails. Suppress can remain useful after the target wakes. Huge targets still cannot receive Trip. The empirical table includes an explicit KO-first row; the original KO row is the KO-last/independent-order bound. On the Rogue's own turn it can choose the favorable ordering; on an enemy turn the DM controls simultaneous ordering unless text changes that rule. LR can negate KO and thus prevent the automatic-save cascade. Auto-failed saves should not be logged as independent d20 rolls.

### Save pressure and Legendary Resistance

Three saves per landed SA can challenge LR reserves, especially when another party member threatens a decisive spell. Six valid attempts with each 40% failure average 2.4 failures, with probability of at least three failures among six=.45568, calculated from a binomial distribution. A boss does not automatically spend LR on every failed Trip, Disarm or Daze. It can accept a low-value rider, be size-ineligible or immune, or use strong secondary saves. Thus “six saves means six LR removed” is false.

The highest CR sample has 18/19 creatures with LR, and only a small eligible subset for locks. This is a limitation of using CR 17–24 as a universal enemy proxy: a level 17 party also fights lower-CR groups, where free package applicability is much higher. Analyze both.

Official high-level alternatives can also force several saves: Monk Stunning Strike plus a subclass control rider across attacks, Soulknife Rend Mind plus two base CS effects, area spells against multiple targets, or repeated low-level control from spellcasters. Their costs differ: Focus, psi dice/LR, spell slots, or SA dice. Bartitsu's breadth is unusual because the three-save package can be **at will and damage-free**. It is a budget concern, not proof it always dominates slot-based area control. This supports pricing the stronger effects at 17, not deleting every multi-save feature.

## DPR Model Comparison

| Level | Method | Bartitsu on-turn | Mixed total | Favorable total | Nick/Aim same method |
|---|---|---|---|---|---|
| 3 | Fixed60 | 12.36 | 16.70 | 23.45 | 16.21 |
| 3 | Fixed65 | 12.87 | 17.41 | 24.44 | 16.76 |
| 3 | RPGBOT | 12.87 | 17.41 | 24.44 | 16.76 |
| 3 | Empirical | 12.36 | 16.70 | 23.44 | 16.15 |
| 5 | Fixed60 | 16.48 | 21.90 | 30.61 | 20.70 |
| 5 | Fixed65 | 17.16 | 22.84 | 31.91 | 21.35 |
| 5 | RPGBOT | 17.16 | 22.84 | 31.91 | 21.35 |
| 5 | Empirical | 16.46 | 21.88 | 30.57 | 20.62 |
| 9 | Fixed60 | 25.74 | 34.82 | 48.89 | 28.83 |
| 9 | Fixed65 | 26.62 | 36.06 | 50.62 | 29.66 |
| 9 | RPGBOT | 27.36 | 37.11 | 52.09 | 30.33 |
| 9 | Empirical | 27.23 | 36.93 | 51.84 | 30.19 |
| 11 | Fixed60 | 29.15 | 36.22 | 48.70 | 32.47 |
| 11 | Fixed65 | 30.14 | 37.51 | 50.46 | 33.37 |
| 11 | RPGBOT | 30.14 | 37.51 | 50.46 | 33.37 |
| 11 | Empirical | 29.45 | 36.61 | 49.24 | 32.72 |
| 13 | Fixed60 | 34.58 | 49.52 | 69.16 | 36.12 |
| 13 | Fixed65 | 35.54 | 50.90 | 71.08 | 37.08 |
| 13 | RPGBOT | 35.54 | 50.90 | 71.08 | 37.08 |
| 13 | Empirical | 35.75 | 51.20 | 71.50 | 37.28 |
| 14 | Fixed60 | 34.58 | 49.52 | 69.16 | 36.12 |
| 14 | Fixed65 | 35.54 | 50.90 | 71.08 | 37.08 |
| 14 | RPGBOT | 35.54 | 50.90 | 71.08 | 37.08 |
| 14 | Empirical | 35.75 | 51.20 | 71.50 | 37.28 |
| 17 | Fixed60 | 43.73 | 62.61 | 87.45 | 43.41 |
| 17 | Fixed65 | 44.69 | 64.00 | 89.39 | 44.51 |
| 17 | RPGBOT | 44.69 | 64.00 | 89.39 | 44.51 |
| 17 | Empirical | 43.02 | 61.61 | 86.05 | 42.61 |
| 20 | Fixed60 | 47.35 | 67.80 | 94.69 | 47.05 |
| 20 | Fixed65 | 48.39 | 69.30 | 96.79 | 48.22 |
| 20 | RPGBOT | 48.39 | 69.30 | 96.79 | 48.22 |
| 20 | Empirical | 46.59 | 66.72 | 93.18 | 46.20 |

The conclusion is stable across accuracy models: level 3 mixed damage is ordinary; level 9 is strong; level 13/17 favorable sustained damage is much larger than competent mundane Rogue baselines. Actual high-CR AC lowers both Bartitsu and comparator results, rather than eliminating the reaction multiplier. RPGBOT's level 9 AC convention gives a normal mundane 70% hit rate rather than 65%; this was retained, not silently adjusted.

The models can disagree on **classification** when attention changes, not because one formula secretly ignores crits. A guaranteed two-attack level 13 case gives 71.09 versus a.10 attention case 39.10. Different assumed attack frequencies can outweigh the differences between 60% and65% accuracy.

### Numerical breakpoints

The table shows effective qualifying-attention probability needed for Bartitsu to exceed Nick/Aim by 25% or 50%, using two incoming attacks and the stated Sap model before 13. These are comparison markers, **not official balance caps**.

| Level | Attention for +25% DPR | Attention for +50% DPR |
|---|---|---|
| 3 | 0.77 | 1.17 |
| 5 | 0.72 | 1.13 |
| 9 | 0.48 | 0.82 |
| 11 | 0.68 | 1.17 |
| 13 | 0.30 | 0.57 |
| 14 | 0.30 | 0.57 |
| 17 | 0.24 | 0.49 |
| 20 | 0.25 | 0.49 |

Values above 1 cannot be reached under that scenario. At 13,30.4% attention produces a 25% damage lead and 56.5% produces a 50% lead. At 17, the thresholds are 24.5% and49.4%. These are substantially lower than an 85% attention assumption. Control advantages are additional, while melee survival/mobility differences are omitted from these damage ratios.

Duration sensitivity: Thief 17's extra first-round turn is +50/25/16.7/12.5% of ordinary turn damage in 2/4/6/8-round combats. Assassin's flat opening bonus and Death Strike similarly dilute with duration. Bartitsu's qualifying reaction damage doesn't dilute if attention stays constant. A long adventuring day strengthens its sustainability relative to limited nova routines, but do not treat every finite pool as scarce. Over six four-round encounters with two Short Rests, high-level Monk Flurry alone fits 24 uses comfortably within three 13-point-or-larger Focus pools; Soulknife Homing consumes about 6 dice on average; Ranger can often sustain Mark through multiple encounters. Fighter Action Surge is roughly three uses in that day at 13, and AT 13 has two third-level Haste slots before other recovery/support. Bartitsu’s main comparative sustainability advantage concerns reliable counters and stronger repeated control; healing/exposure can become its binding resource.

### Enemy statistics and saves: Model C limitations

The extracted SRD sample contains 328 complete statblocks; two detected headers lacked a complete usable schema and were excluded. The audited CR bands contain 220 statblocks. Spot checks included Aboleth, Bandit Captain, Ogre, Troll, Giant Ape, adult/ancient red dragons, Mage, Assassin, Vampire and Lich; wrapped melee-roll lines were corrected before the final data run. Saving-throw bonuses come from the **SAVE column**, not the ability modifier column. First listed melee attack bonus is a proxy; some monsters instead use save-based attacks or multiple distinct attack types. No attack roll is invented for those cases. Explicit Unconscious immunity occurs in 4/110,7/65,0/26,0/19 statblocks across the bands; Stunned immunity in 5/110,1/65,0/26,0/19. This incomplete sample is not evidence those immunities are absent from every high-level published monster.

| CR band | n | AC mean / median | AC p 10–p 90 | Melee bonus mean / median | Melee n | Poisoned immunity |
|---|---|---|---|---|---|---|
| [1, 4] | 110 | 13.65 / 13.00 | 11–17 | 5.18 / 5.00 | 108 | 0.17 |
| [5, 10] | 65 | 15.75 / 16.00 | 13–18 | 7.79 / 7.00 | 62 | 0.32 |
| [11, 16] | 26 | 17.62 / 18.00 | 16–19 | 10.80 / 11.00 | 25 | 0.31 |
| [17, 24] | 19 | 20.42 / 21.00 | 18–22 | 14.78 / 14.50 | 18 | 0.26 |

CR 1–4 is used for level 3, CR 5–10 for 5/9, CR 11–16 for 11/13/14, CR 17–24 for 17/20. These are broad sensitivity bins, not the claim “enemy CR equals PC level.” Raw DPR tables are before damage resistance/immunity. Bludgeoning resistance appears in 8/110 and 7/65 lower-band statblocks, none in the two upper bands here. Applied as a simple half-damage factor before rounding, empirical on-turn Cane DPR falls 12.36→11.92 at 3 and 27.23→25.71 at 9. A skill bonus or magic weapon does not bypass an unqualified Bludgeoning resistance; use the actual 2024 statblock. Monk’s Force option, Soulknife Psychic and True Strike Radiant can change these matchups. Equal weighting overrepresents families with many printed variants; the upper band is dragon/legendary heavy. The workbook includes every parsed row so encounter-weighted or custom samples can replace this convention.

Effective failure columns below include size/immunity gates but exclude voluntary LR. STR/DEX/CON and chosen-save columns are raw saving-throw failure probabilities conditional on a landed attack:

| Rogue level | DC | STR fail | DEX fail | CON fail | Chosen STR/DEX fail | Effective Trip | Effective Lock | Effective Poison |
|---|---|---|---|---|---|---|---|---|
| 3 | 13 | 0.47 | 0.52 | 0.50 | 0.43 | 0.43 | 0.38 | 0.41 |
| 5 | 15 | 0.48 | 0.59 | 0.48 | 0.44 | 0.41 | 0.33 | 0.33 |
| 9 | 17 | 0.58 | 0.69 | 0.58 | 0.54 | 0.49 | 0.40 | 0.39 |
| 11 | 17 | 0.48 | 0.61 | 0.48 | 0.45 | 0.33 | 0.26 | 0.34 |
| 13 | 18 | 0.53 | 0.66 | 0.53 | 0.50 | 0.36 | 0.28 | 0.38 |
| 14 | 18 | 0.53 | 0.66 | 0.53 | 0.50 | 0.36 | 0.28 | 0.38 |
| 17 | 19 | 0.48 | 0.57 | 0.46 | 0.46 | 0.11 | 0.11 | 0.34 |
| 20 | 19 | 0.48 | 0.57 | 0.46 | 0.46 | 0.11 | 0.11 | 0.34 |

At 13, target choice lowers expected lock/redirect success from 65.8% using DEX alone to 49.8%; about 16 percentage points. At 17, raw DEX failure 56.6% becomes 45.5% with choice. Against save+0/+5/+10 at DC 19, failure 90/65/40%; against+15,15%. Strong and weak saves remain important despite proficiency scaling.

## Control and Defensive Value

### Control is separately budgeted

| Effect | Quantifiable value | Bound / practical limit |
|---|---|---|
| Poison | Each affected attack loses hit probability `e−e²`; attacks/checks disadvantaged | Immunity; end-turn saves; overlaps Sap/Prone; no save disadvantage |
| Trip | Advantage for attacks within 5; target spends half speed to stand | No stand cost if already prone; ranged allies can lose accuracy; size gate |
| Withdraw | Immediate half-speed escape without OA | Can sacrifice future reaction opportunities; doesn't force enemy action loss |
| Disarm | Retrieval/access denial and possible lost weapon attack | Relevant held object required; natural attacks unaffected; easy pickup can erase value |
| Redirect |5 feet can break formation, move into hazard or separate grapple | No normal OA; terrain/party dependent; target chooses save |
| Joint Lock | Denied movement, escape action(s); enables prone lock | Free hand, reach, size; attacking grappler remains possible |
| Suppress | Denies relevant reactions and enables allied repositioning | Zero value if target had no useful reaction; not legendary actions |
| Daze | Denies simultaneous move+action+BA next turn | Stationary Multiattack remains; not incapacitation |
| Obscure | Attack denial/Advantage support over current remainder and next turn | Special senses, range and overlapping conditions affect value |
| Knock Out | Potential lost turn, auto STR/DEX failure, one close critical hit | Damage wakes; end-turn saves; LR and immunity; party must choose restraint versus damage |

Example: incoming hit 75%, mean hit 15 and ordinary crit extra 9 gives Sap prevention `.1875×15+.0475×9=3.24` on one certainly affected attack. Two otherwise normal attacks poisoned before resolution can prevent up to 6.48 expected damage; multiply by landing, save failure and actual duration, and subtract overlap with Sap. Do not count the same disadvantaged roll twice.

For four allied melee attacks at baseline 65% accuracy with 12 mean hit damage, pure accuracy improvement from Advantage is `.2275×12×4=10.92` conditional on the condition applying and surviving. With a 60% Trip failure and 93.75% Rogue hit, that is 6.14 expected party damage before standing/initiative/senses adjustments. Extra critical dice can increase this; ranged allies or standing before their turns can reduce it to 0 or even impose a loss. A bounded 0–approximately 11+crit-dice conditional amplification is more defensible than assigning every Trip a universal DPR value.

Grapple+Prone can extend that assistance over several turns and can consume escape actions. The appropriate metric is **eligible creature turns locked**, not only Rogue damage. Suppress should count valuable reactions actually denied, not one arbitrary “action-equivalent” every use. Daze should count turns in which the enemy needed more than one of its three permitted categories.

### Defensive model and opportunity cost

Exact incoming damage example:2d8+6 on hit,4d8+6 on crit, seen enemy, no external Advantage. UD halves actual integer damage with rounding down. Counter Cane can reapply Sap. “Offense first” spends on first miss or qualifying hit at 13+, reserving pre 13 UD until the last attack if no miss occurred. “Defense first” pre 13 uses UD on first hit; at 13 it can decline early misses and wait for a hit to combine UD+counter.

| Level | Incoming attacks | Enemy hit | Policy | Damage taken | Counter probability | Damage prevented by UD |
|---|---|---|---|---|---|---|
| 5 | 1 | 0.60 | first | 2.86 | 0.61 | 3.06 |
| 5 | 1 | 0.60 | defense | 2.86 | 0.61 | 3.06 |
| 5 | 2 | 0.60 | first | 11.31 | 0.77 | 1.90 |
| 5 | 2 | 0.60 | defense | 9.33 | 0.24 | 6.03 |
| 5 | 3 | 0.60 | first | 20.97 | 0.86 | 1.14 |
| 5 | 3 | 0.60 | defense | 17.59 | 0.10 | 7.22 |
| 13 | 1 | 0.75 | first | 4.19 | 1.00 | 4.47 |
| 13 | 1 | 0.75 | defense | 4.19 | 1.00 | 4.47 |
| 13 | 2 | 0.75 | first | 12.85 | 1.00 | 4.47 |
| 13 | 2 | 0.75 | defense | 11.57 | 1.00 | 7.05 |
| 13 | 3 | 0.75 | first | 24.55 | 1.00 | 4.47 |
| 13 | 3 | 0.75 | defense | 21.66 | 1.00 | 7.69 |
| 17 | 1 | 0.90 | first | 5.92 | 1.00 | 6.33 |
| 17 | 1 | 0.90 | defense | 5.92 | 1.00 | 6.33 |
| 17 | 2 | 0.90 | first | 18.16 | 1.00 | 6.33 |
| 17 | 2 | 0.90 | defense | 17.14 | 1.00 | 7.67 |
| 17 | 3 | 0.90 | first | 32.11 | 1.00 | 6.33 |
| 17 | 3 | 0.90 | defense | 30.67 | 1.00 | 7.80 |
| 20 | 1 | 0.90 | first | 5.92 | 1.00 | 6.33 |
| 20 | 1 | 0.90 | defense | 5.92 | 1.00 | 6.33 |
| 20 | 2 | 0.90 | first | 18.16 | 1.00 | 6.33 |
| 20 | 2 | 0.90 | defense | 17.14 | 1.00 | 7.67 |
| 20 | 3 | 0.90 | first | 32.11 | 1.00 | 6.33 |
| 20 | 3 | 0.90 | defense | 30.67 | 1.00 | 7.80 |

At 5 against three 60%-accuracy attacks, offense-first takes 20.97 and counters 86.0%; defense-first takes 17.59 and counters 9.8%. Early offense costs 3.38 expected damage in that example. At 13 against three 75%-accuracy attacks, offense-first takes 24.55 versus 21.66 when preserving UD for a hit, while both eventually counter 100% under homogeneous, stable-reach assumptions. Late offense delays Sap/control, and if the target can leave or a more dangerous attacker follows, it changes the result.

An ordinary Rogue with no Sap, taking UD on its first hit from three such attacks, takes 27.18 expected damage. Raw no-UD damage is 35.10. Bartitsu's offense-first 24.55 is only about 10% lower than ordinary melee Rogue damage taken in this illustration, not invulnerability. A 94 HP level 13 Rogue has about 3.8 such exposed rounds before HP exhaustion versus 3.5 for the ordinary example, without healing/control/other damage. At 17,122 HP against the illustrative 90%-accuracy three attacks takes 32.11 under offense-first, again only 3.8 rounds. These are exposure illustrations, not complete effective-HP rankings.

Ranged Rogue can often avoid those melee attacks altogether; an attention reduction can outweigh Sap. Monk Deflect Attacks reduces one eligible hit by 1d10+Dex+Monk level, averaging 23.5 at 13, much more than one typical UD prevention, but consumes its reaction and has its own limitations. Fighter/Paladin can have higher armor, shields and HP; Barbarian rage can resist much of physical incoming damage but Reckless increases enemy accuracy. Bartitsu retains d8 HP/light armor and the base Rogue defense package, not a tank chassis.

Base Rogue Evasion 7 is excellent against qualifying DEX saves, Slippery Mind 15 adds WIS/CHA-save proficiency, and Elusive 18 prevents attackers gaining Advantage while the Rogue isn't incapacitated. Elusive matters against Reckless-like enemy advantage: incoming Advantage otherwise cancels Sap's Disadvantage to ordinary accuracy. It doesn't create extra counters against save-only attacks. Reliable Talent 7 supports proficient ability checks, including relevant skills, but doesn't increase the initial grapple save DC.

Counterstroke makes first-attack reaction offense attractive in a homogeneous melee duel, often a dominant local choice. It doesn't eliminate meaningful decisions when later damage is larger, another enemy is more dangerous, an OA prevents escape, Defensive Duelist covers multiple attacks, or a hit source cannot be seen. Record those situations in testing.

## Action Economy Audit

| Slot | Base Rogue competition | Bartitsu additions | Main level interactions |
|---|---|---|---|
| Action | Attack; Ready; Hide; Utilize; spellcasting for AT | Cane/unarmed damage; Dex save-based grapple/shove | Grapple-only action forfeits SA; no Extra Attack gained |
| Bonus Action | Cunning Action; Steady Aim; Light/Dual Wielder attack; Soulknife blade; subclass utility | Create an Opening | All levels: movement versus accuracy/extra attacks; free Withdraw can compensate at 9 |
| Reaction | OA; UD 5; other feat/spell reactions | Exploit 3; UD+Counterstroke 13 | One reaction between own-turn starts; first counter can forfeit later UD/OA |
| Movement | Positioning; Aim sets 0; Disengage costs BA | Create allows movement; Withdraw half-speed after hit; Redirect/lock positioning | Need remain within 5 for reaction engine; escaping can turn it off |
| Sneak Attack | Once/turn | Same rule, different eligible implements and triggers | No second own-turn SA; one enemy-turn SA per available reaction |
| Cunning Strike | Dice sacrifice; one effect 5, two 11; Devious 14 | Discount 9; custom effects 9; three 17 | Potential on-turn plus off-turn packages; effect saves/applicability separate |

There is no extra action economy slot. The high-level budget issue is the amount of value packed into the existing reaction and SA slots, not a literally additional reaction.

## Official Subclass Power Budgets

This compares complete packages at each subclass level, including nondamage abilities. It does not infer “balanced because another subclass has one similar sentence.”

| Level | Assassin | Thief | Soulknife | Arcane Trickster | Bartitsu implication |
|---|---|---|---|---|---|
|3|Opening offense/initiative plus tool proficiencies|Fast Hands plus climbing/jumping|Blades/Vex plus skill support and telepathy|Spellcasting plus enhanced Mage Hand|Combat-heavy but conditional reactions; ordinary damage comparison supports acceptability|
|9|Infiltration plus mobile Aim|Preserve hiding through paid Stealth Attack|Homing accuracy plus teleport|Invisible spell ambush disadvantage on saves|Bartitsu free control+1 Cane is stronger sustained combat than many utility 9 packages|
|13|Envenom poison damage/resistance bypass|Extra attunement, charge conservation, scroll use|Long invisibility with limited refresh|Additional Trip target near Mage Hand|Bartitsu reliable counter is a large at-will damage/control jump|
|17|First-round save-based doubling|One extra first-round turn|Save-based stun with finite refresh|Once/rest spell defense/theft|Bartitsu three free-effect packages persist after opening rounds and don't spend daily resources|

Assassin 13 Poison contribution was separately modeled with a finite poison-state process: apply while unpoisoned, pay 1 SA die, extra 2d6 on initial and each repeat failed CON save, no refresh double-counting. At 13, before poison immunity and without Death Strike, this raises the illustrative four-round result to 42.38 versus 40.19 no-poison; at 14 to 42.62 versus 40.43. Poison immunity in the empirical CR 11–16 sample is 30.8%, reducing useful uptime. Ignore resistance isn't ignore immunity. At 17 Death Strike and poison can combine; the main opening-offense table deliberately doesn't pretend the poison-only number includes Death Strike.

Soulknife finite-four-round Vex output is 38.35 at 13,42.36 when Homing is available. Homing only consumes dice when it changes a miss into a hit and cannot rescue natural 1. The pool is 10d10 at 13,12d12 at 17, shared with other psi features; returns one die on a Short Rest and all on Long Rest. The model records expected dice use, so the pool-available damage envelope must be scaled down when exhausted or spent on teleport/Rend Mind. Importantly, expected Homing use over 24 comparable rounds is only about 5.4 dice at 9,5.7 at 13 and 5.9 at 17, below the 8/10/12 pools even before Short Rest recovery. Homing alone can therefore be close to day-long sustainable in this accuracy environment; calling it prohibitively resource-limited would be misleading. Other psi expenditure and the distribution of misses can still deplete it. Rend Mind forces a WIS stun save on SA, repeats at end of turns and uses limited refresh; it's a powerful comparator, not permanent free stun.

Arcane Trickster 13 can use Haste from its own third-level slots: setup action in round 1, later hasted Attack plus Ready main action enables two SA on different turns. It costs concentration, a slot, the reaction and setup; Ready must execute before the next turn. Haste grants its extra action immediately, so round 1 can include a hasted attack despite the setup Magic action. Four rounds permit up to seven attacks: one in round 1 and two in each later round. With rapier Steady Aim on own turns and normally qualified non-advantaged readied attacks, the level 13 four-round mean is 50.33 before concentration/trigger failures—close to Bartitsu’s 50.90 mixed result. An 80% independent continuation chance per round lowers that four-round Haste mean to 35.60; a 99% chance gives 49.49. Concentration loss also carries Haste’s subsequent lethargy cost, so those attrition calculations are upper bounds, not free Haste uptime. True Strike isn't simply attached to every Extra Attack or OA. A familiar can Help but can be killed or be unavailable; table Help uptime is an envelope. Legacy Shadow Blade/booming blade are optional separate content, not assumed final 2024 core.

Thief 13 scroll access and BA Magic can enable own-turn spell damage plus a readied off-turn weapon SA in item-rich play, but scroll cost, Magic action restrictions, readied concentration where relevant, SA qualification and reaction opportunity cost remain. Thief 17 first-round extra turn can also reset a reaction and alter opening nova; treating it solely as one extra damage turn understates its tactical burst. Bartitsu should not be compared against an item-starved Thief while receiving stacked magic bonuses itself.

## Broader Martial Context

These are controlled competent packages, not universal maximum builds. Fighter uses GWF greatsword Graze; GWM variant adds PB damage per hit on own Attack action. Berserker uses Rage/Reckless/Frenzy; reaction column is Retaliation conditional on taking nearby damage, not always granted. Paladin uses sword/shield Dueling and Devotion Sacred Weapon with CHA 16; Divine Favor adds a slot/BA. Hunter uses Vex/Nick, TWF, Mark and Colossus Slayer against an already-damaged target. Monk columns distinguish at-will BA attack from Flurry; no free Focus is assumed. Every character has the same primary modifier progression; optimized half-feat cases start 17, take a half feat 4 and ASI 8, matching those modifiers.

| Level | Monk at will | Monk Flurry | Fighter GWM/Graze | Berserker GWM | Berserker conditional reaction | Devotion sword/shield | Hunter Marked |
|---|---|---|---|---|---|---|---|
| 3 | 8.80 | 13.20 | 8.60 | 18.04 | 0 | 7.83 | 19.93 |
| 5 | 17.25 | 23.00 | 23.10 | 37.11 | 0 | 17.25 | 31.43 |
| 9 | 19.20 | 25.60 | 26.40 | 46.20 | 0 | 18.85 | 33.71 |
| 11 | 21.30 | 35.50 | 39.60 | 46.20 | 13.85 | 26.50 | 33.71 |
| 13 | 21.30 | 35.50 | 41.55 | 47.96 | 13.85 | 26.50 | 33.71 |
| 14 | 21.30 | 35.50 | 41.55 | 47.96 | 13.85 | 26.50 | 33.71 |
| 17 | 23.40 | 39.00 | 43.50 | 55.30 | 14.72 | 26.50 | 38.63 |
| 20 | 31.35 | 52.25 | 58.00 | 55.30 | 14.72 | 26.50 | 44.48 |

### Open Hand Monk control/accuracy cross-check

The simple martial columns omit damage gains from conditions. A stronger official comparator is an Open Hand Monk using 2 Action attacks,3 Flurry attacks, Stunning Strike on its first hit, and Topple on Flurry hits until the target is Prone. An exact state model applies Advantage after Stun/Prone and the one-attack Advantage granted when the target succeeds its Stunning save. It doesn't grant automatic crits, redundant save attempts after Prone, or unlimited extra attacks. Results below are for an eligible target without LR/immunity; the primary attack accuracy is 65% (75%at 20 from Body and Mind). Costs are 1 Focus for Flurry plus 1 for Stunning when attempted; reaction redirection is separate.

| Monk level | CON failure | DEX failure | On-turn DPR | Stun probability | Prone probability | Meaningful save attempts |
|---|---|---|---|---|---|---|
| 13 | 0.20 | 0.30 | 40.59 | 0.20 | 0.59 | 2.51 |
| 13 | 0.45 | 0.60 | 42.54 | 0.45 | 0.88 | 2.16 |
| 13 | 0.70 | 0.80 | 43.73 | 0.70 | 0.97 | 2.03 |
| 17 | 0.20 | 0.30 | 44.61 | 0.20 | 0.59 | 2.51 |
| 17 | 0.45 | 0.60 | 46.77 | 0.45 | 0.88 | 2.16 |
| 17 | 0.70 | 0.80 | 48.08 | 0.70 | 0.97 | 2.03 |
| 20 | 0.20 | 0.30 | 58.02 | 0.20 | 0.63 | 2.65 |
| 20 | 0.45 | 0.60 | 60.29 | 0.45 | 0.91 | 2.22 |
| 20 | 0.70 | 0.80 | 61.61 | 0.70 | 0.98 | 2.05 |

At 17 the middle scenario gives 46.77 damage,44.76%stun and88.07%prone, compared with 39.00 for Flurry with no condition benefits. Stun can deny an entire enemy action/reaction/movement window and automatically fail later STR/DEX saves; it is stronger than Daze. Open Hand Topple/Push lacks Trip's Large-size cap. Deflect can also force a DEX save for 2 martial dice+Dex damage if the triggering damage is reduced to 0 and 1 additional Focus is spent. Stunning Strike says once per **turn**, so an eligible OA can attempt it again on another turn, with another Focus cost. The same reaction cannot also Deflect.

This materially limits the claim that three control saves are inherently unprecedented. Bartitsu's concern is their joint at-will damage economy and reliable reaction, not the mere existence of multiple saves. High-level Focus recovery can sustain Flurry+Stunning through a 24-round day with two Short Rests at 17 if expenditures are distributed well; it isn't automatically a once-encounter nova. Monk's stronger defensive/mobility chassis and narrower useful effect list must both count. The Open Hand model is in the reproduction script, while the workbook's martial snapshot remains the deliberately simpler Flurry-only model.

Martial nova and durability aren't in those sustained columns. Fighter Action Surge adds an action with its current attack count, typically once/rest; Battle Master maneuvers add finite damage/control/accuracy, and Champion crit improvements raise the shown core numbers. Paladin smite uses BA immediately after an eligible hit and spell slots, with higher slots for nova; Divine Favor and other spells alter its sustained budget. Barbarian Brutal Strike trades Reckless Advantage for damage/control and can be preferable by situation; it wasn't silently granted while retaining full Advantage. Monk Flurry/Stunning Strike consume Focus but have restoration features and substantial defensive/mobility value. Hunter's concentration protection and later marked-target Advantage are included where relevant.

At 13, Bartitsu's 50.90 mixed result is above a competent feat-bearing Fighter sustained snapshot but near a Berserker's raging+reaction envelope. Its 71.09 high-attention result is not impossibly larger than every martial nova, but is unusually high **for a Rogue carrying repeated discounted control without an offensive resource**. Cross-class damage parity isn't the criterion: sword/shield Paladin supplies armor/aura support; Rogue supplies skills/mobility; Monk supplies defense/speed. Compare total roles rather than demanding identical DPR.

## Multiclass and Optimization Findings

### Three-Rogue-level dip tests

| Build | Useful synergy | Real opportunity cost / limit | Audit finding |
|---|---|---|---|
|Monk 5/Rogue 3 at 8|Martial die damaging unarmed now qualifies for SA; Dex grapple; reaction attack|Flurry competes with Create; Deflect competes for reaction; loses Monk 6–8 features/Focus/ASI|Useful, no unique infinite engine; reaction 1d8+Dex+2d6 at baseline Advantage 14.72 conditional|
|Fighter 5/Rogue 3 at 8|Extra Attack preserves action accuracy; Cane counters; maneuvers can help|Lose Fighter 6 ASI and 7 subclass; Action Surge doesn't permit two same-turn SA|Strong melee dip; counter 1d8+Dex+2d6≈14.72; reaction shared with Riposte|
|Hunter 5/Rogue 3 at 8|Mark on counter and Colossus once/turn can repeat off-turn|Concentration/mark BA; target already damaged; lose ranger progression|Conditional Cane 1d6+Dex+2d6+1d6 Mark+1d8 Colossus≈21.55; not net multiclass gain|
|Barbarian 5/Rogue 3 at 8|Finesse weapon can still attack using STR; Rage and Reckless support reaction|Reckless exposes character; loses Barbarian 6 defense; Dex attack doesn't qualify for STR rage rider|Reaction 1d6+STR+2d6+Rage≈15.50; normal finesse weapons already qualify for STR SA|
|Paladin 11/Rogue 3 at 14|Radiant Strikes 1d8 applies to weapon/unarmed hit; SA reaction|Lose Paladin 12 ASI/13 spells; Smite BA normally unavailable off-turn|Conditional Cane+Dex/STR+2d6+1d8≈19.01; strong but three-level cost real|

The conditional estimates use 65% mundane accuracy, Advantage and the stated flat modifiers; they are not added to unrelated main-class builds as “free” net gains. The workbook exposes all riders and hit inputs. For Ranger/Paladin especially, Constitution, casting stat, armor and multiclass prerequisites must be budgeted; a Rogue-only Dexterity build cannot silently meet every prerequisite for free.

Unarmed Finesse enables compatibility with SA and some finesse-weapon features, but doesn't turn a punch into every kind of manufactured weapon. Monk's own Martial Arts already supplies Dexterity control and damage; the new benefit is SA eligibility plus a counter route. Fighter Unarmed Fighting/Tavern Brawler may raise the weapon-die floor with an opportunity cost. No infinite attacks, stacked reactions, Extra Attack 3-dip exploit or recurring no-save grapple was found.

### Feats/equipment

**Grappler:** half-feat, damaging Unarmed Strike as part of own-turn Attack action can also attempt Grapple; the grapple still permits the save. It doesn't apply to Cane hits or reaction punches. Advantage versus one's grapple can free the BA for mobility and preserve counter accuracy, but requires the grapple and hand. This is the main non-damage low-level synergy to test.

**Tavern Brawler:**1d4 unarmed and reroll 1 damage die, improvised proficiency redundancy, plus a once-own-turn push after an eligible unarmed hit. It doesn't generally turn every grapple or reaction into a free shove. Small dice improvement, not a multiplicative damage engine.

**Sentinel:** broadens reaction access when an adjacent enemy Disengages or **hits** another target. Combined with 13 hit/miss counters, many melee choices trigger an attack: attack the Rogue either outcome, hit an ally, or Disengage. Miss an ally, use a save action, attack from outside 5, teleport, or use range can still avoid it. Same reaction, not extra reactions. Rogue's spare ASIs at 10/12 allow Sentinel/Grappler after Dex 20 without sacrificing the main progression. This is a meaningful optimized attention/reliability ceiling, and the breakpoints above should use the enlarged observed opportunity rate.

**Defensive Duelist:** PB AC against melee until own-turn start can prevent several attacks, but uses the reaction. It cannot force a miss and also spend that reaction on Exploit. Its defense may be better than an early counter against heavy Multiattack, preserving a meaningful choice.

**Dual Wielder:** a Light-weapon Attack-action hit/attack setup permits a BA attack with a different melee weapon lacking Two-Handed, so a Cane can be that BA weapon. No positive ability damage on that extra attack without an appropriate feature. Cane itself isn't Light or Nick; Nick and Dual Wielder aren't interchangeable. A competent optimized Bartitsu can use Light/Nick and end with a Cane ready, avoiding Create if other SA/Advantage setup exists. The main table is therefore a **signature-weapon routine, not the absolute optimized ceiling**. No new bonus action slot is created.

A same-feat Sentinel comparator narrows the damage lead. In a two-attack example with 60% self-attention,40% ally-attention,75% enemy hit chance,80%adjacency and 90%reaction availability, ordinary Sentinel opportunity on the ally branch is `.40×.80×.90×[1−.25²]=.27`. A Nick/Aim rapier Rogue then adds.27×23.55=6.36, total 43.44. Bartitsu with the same feat gets its.432 counters plus that mutually exclusive ally-hit branch:35.54+15.35+.27×27.65=58.36. The lead is 34.3%, not the 37.3% no-feat comparison or an unbounded sum of reactions. If external control grants Advantage on the Sentinel OA, both comparators improve under the same support assumption. These scenarios use actual mutually exclusive target branches; don't add two guaranteed reactions.

Heavy-weapon or shield feats don't automatically work because an object became Finesse. Retaining a printed magic object's Heavy/Reach/riders when designated as a Cane is a separate wording/design choice, hence the profile clarification. Attack bonuses stacking is the cleanest equipment exploit to close.

### Additional feat and equipment stress tests

Tavern Brawler's reroll wording can reasonably include Sneak Attack dice when they are damage dice for the damaging Unarmed Strike. That interpretation should be confirmed explicitly rather than assuming the feat affects only the punch die. A d6 rerolling one initial 1 has mean 47/12=3.9167; d4 mean 23/8=2.875. Under the broad interpretation, pure-Rogue advantaged unarmed attacks average 13.073 at 3,41.559 at 17 and45.378 at 20, compared with Cane 12.870/44.693/48.394. This makes a feat-supported punch competitive but does not overtake the enhanced Cane at high levels. The no-Sap and hand/position tradeoffs remain. A narrow reroll interpretation lowers that output. Classify this as a genuine rules-adjudication/optimization interaction, not an infinite exploit.

Great Weapon Fighting can apply to a Cane held in two hands because it has Versatile, but current official Sage Advice [3] limits its benefit to weapon damage dice, not additional riders. It therefore does not floor every SA die to 3. Its d8 floor mean is 4.875 (ordinary 4.5), only 0.375×(h+c) additional EV; gaining the fighting style has a cost. Savage Attacker is likewise limited to weapon dice by official clarification. Do not use old forum assumptions to grant amplified Sneak Attack dice from those feats.

Shield attacks can retain the shield's AC bonus per current Sage Advice [3], but shield training is still required and the shield hand isn't a free grapple hand. A shield used as an ordinary improvised Finesse weapon can deliver SA, usually at d4 and without Sap. This is a useful Fighter/Paladin-dip defense option, not an extra free hand or automatic Cane profile.

With only two ordinary Rogue mastery selections, Cane Sap+shortsword Vex+scimitar Nick cannot all be mastered. The following three-attack Vex/Nick routine therefore sacrifices Sap, unless Sap is explicitly automatic or another class supplies more masteries. At 13+ this leaves the counter opportunity unchanged but increases defensive exposure.

Explicit Dual Wielder optimization at 13: ordinary shortsword first, Cane BA immediately afterward to consume available Vex, then Nick scimitar as the additional Attack-action attack. With no outside Advantage, the three-attack signature routine is 38.739 on-turn, versus 35.543 Create/Cane and 37.358 for the same-feat mundane Rogue using a rapier BA. The Cane BA retains its skill bonus but not positive Dexterity damage. This raises the Bartitsu high-attention total to 74.282 with its normal 35.543 counter. At 17 the analogous on-turn routine is 47.274 and high-attention 91.966. If retaining Sap+Nick and omitting Vex instead, on-turn output is 37.961 at 13 and46.490 at 17; high-attention totals 73.503 and 91.182. These are feat-dependent ceilings; they strengthen rather than erase the high-attention concern, but the extra on-turn increment alone is modest. Weapon equip/unequip and BA insertion timing must be legal at the table.

### Existing off-turn Sneak Attack routes

| Route | Reliability and dependency | Resource/action/position price |
|---|---|---|
|Ordinary OA|Enemy leaves reach using its own movement; attack still must hit/qualify|Reaction; enemy movement choice; no inherent Advantage|
|Sentinel 2024|Adjacent Disengage or hit on another target|Feat and reaction; no automatic trigger on an ally being missed|
|Battle Master Riposte 2024 [14]|Melee miss, similar trigger to Exploit; no inherent Advantage|Dip 3 or allied build isn't enough to give personal Riposte; superiority die until Fighter 15's free once/turn maneuver; reaction|
|Commander's Strike 2024 [14]|Ally directs an attack on ally's turn; no enemy miss needed|Ally replaces an attack and spends die; Rogue reaction; **no 2014 BA cost** in final 2024 wording|
|Haste plus Ready|Own hasted Attack and main Ready; trigger on another turn|Spell/concentration/setup, reaction, actual ready trigger; own AT can do this from 13|
|Action Surge plus Ready|Attack now, Ready with second action|Fighter investment and Surge; no second same-turn SA|
|Legacy forced-reaction/Order support|Can enable OA or commanded attacks when exact text permits|Optional older content, ally spell/resource/setup; not treated as a 2024 core baseline|

At level 13 a normal mundane rapier off-turn SA averages 23.55, or 26.70 with a d8 superiority rider, conditional on the reaction opportunity. Bartitsu's 35.54 is higher because it includes Advantage and +2 accuracy/damage. Current Battle Master 15 can use one free d8 maneuver per turn, including Commander's Strike on its own turn or Riposte on another turn [14]. Thus an official high-level party can supply at-will off-turn Rogue attacks, but pays an ally attack opportunity and coordination. It is a useful sustainability precedent, not proof Bartitsu's self-contained extra damage/control is free of budget concerns.

### Level 20 chassis stress

Stroke of Luck turns a failed d20 Test into 20 once/rest. A failed attack converted this way becomes a critical hit. Level 20 Cane critical mean is `2×(1d6+10d6)+8=85`. Its advantaged miss chance is 4%; with guaranteed two attacks, opportunity for at least one failed attack in a cycle is 7.84%. Over eight cycles, probability of at least one such failure is 47.96%; one use can add at most 85 expected-on-conversion damage, or≈5.10 per cycle over that interval. At mixed attention the opportunities are lower, about 37% over eight cycles, adding roughly 3.9 DPR as an attack-only ceiling. Other Rogues also have Stroke, and it may instead be spent on a save/check. These estimates aren't an at-will 85-damage bonus.

The level 19 Epic Boon chosen can materially change comparisons: Combat Prowess corrects a miss once per turn, while other boons supply defense, teleportation or damage. Apply the same chosen boon/access convention to all Rogues before claiming a level 20 subclass-specific gain. Higher accuracy generally makes Bartitsu's own extra advantage sources less valuable, but makes each additional attack's SA more reliable. The repeatable high-level double-package issue remains.

## Prior-Art Balance Resource

The strongest directly inspected published comparison was Tribality's *Scoundrel* [12], posted August 2019 (the earlier report's 2020 dating may reflect a separate release). Its 17th-level miss-triggered attack/movement feature is once per Short/Long Rest, unlike Bartitsu's 3rd-level at-will engine. It is not a 2024 Cunning Strike precedent. No reliable documented playtest sample, revision log or quantitative reviewer consensus was located. Other unarmed/improvised/counter Rogue leads in the originality report weren't promoted to validated balance standards merely because they exist. Popularity is not evidence of a sound at-will budget.

## Red Flags

### Critical

None established: no proven infinite loop or automatic bounded-accuracy collapse. Natural 1 still bounds even stacked accuracy.

### Major

- Permissive Cane magic-bonus stacking creates an unjustified equipment advantage; close it before testing.
- Level 17 cumulative free strong riders plus three effects, potentially twice per cycle.
- Level 13+ high-attention reaction engine gives a large sustained Rogue damage lead with control attached; Sentinel and spare Rogue feats broaden that ceiling.

### Moderate

- Level 11 Trip+Lock/Poison packages, especially repeated off-turn; actual eligible-target lock duration unknown.
- Ranged application of free CS: risk justification does not cover all discount uses.
- Item-rich Thief/AT and magic-equipped comparator choices materially alter the relative budget; campaign calibration required.
- Dual Wielder/Light/Nick plus a ready Cane can raise the optimized routine above the headline single-Cane on-turn model.

### Minor

- Explicit mastery selection, unarmed Dexterity override, Joint Lock reach/escape DC, Cane profile and Redirect path wording.
- Disarm retrieval/component adjudication and effect-resolution order.

## Recommendations and Recalculated Effects

Only narrow changes supported by the evidence are recommended. Do not rewrite the subclass's theme or replace counters/leverage with generic Rogue features.

| Change | Evidence/problem | Smallest change | Numerical result | Gameplay cost |
|---|---|---|---|---|
|Prevent Cane stacking|Current wording may allow +6 at 17 while comparator+3|Use higher bonus, never add|Stacked49.30→44.69 conditional attack; favorable two-attacks 98.61→89.39|Magic upgrades below skill bonus don't increase accuracy; unrelated item riders retained|
|Price strong 17 effects|Free Lock/Suppress/Daze with three effects and possible second package|Perfect discount remains 1d6; retain three different effects|Trip+Lock+Daze mixed64.00→53.40; favorable 89.39→74.58, same save chances|Full control routine gives up two SA dice per attack; basic free effects remain|
|Resolve rules hygiene|Mastery, unarmed override, remote/unspecified grapple, magic profile ambiguity|Explicit selection, Dex damage, reach and escape DC; define Cane profile/path|No change to intended/default model|Closes unintended permissive readings|

At 17, revised per-effect costs are Poison 0/Trip 0/Withdraw 0/Disarm 0/Redirect 0, Lock 1/Suppress 1/Daze 1, Obscure 2, Knock Out 5. Three-effect capability is preserved. Further 17 package recalculations under mixed attention:

| Package | Current paid dice | Current total DPR | Revised paid dice | Revised total DPR |
|---|---:|---:|---:|---:|
|Trip+Joint Lock+Daze|0|64.00|2|53.40|
|Trip+Suppress+Daze|0|64.00|2|53.40|
|Disarm+Redirect+Daze|0|64.00|1|58.70|
|Obscure+Trip+Suppress|1|58.70|3|48.10|
|Knock Out+Trip+Suppress|4|42.80|6|32.20|

Costs apply to both on-turn and reaction packages in this table. Fail rates/number of attempts do not change; the revision restores an offensive price rather than hiding control frequency. Players can still select three free 1 die-base effects and retain 64.00 damage; those effects are cheaper because their applicability/value is narrower. A simple discount change doesn't purport to solve high-attention DPR by itself.

**No change recommended:** Create an Opening; Exploit an Opening; one-handed/versatile Cane dice; Sap itself; +1/+2/+3 progression absent stacking; level 9 discount; Disarm 1/Redirect 1/Joint Lock 2/Suppress 2 base costs; level 17 third distinct effect by itself. These values have credible costs/limitations, and the strongest issue is their combination with later free costs/reliable reactions.

### Counterstroke decision gate and optional tuning

Counterstroke's high-attention lead is real, but its net budget depends on actual exposure, healing costs, loss of mobility and the campaign's official-subclass equipment/resources. Preserve it for a targeted comparative test after the 17 discount revision. If a competent party repeatedly sustains effective counter attention above roughly 55% at 13 without paying meaningful survival/action costs, the resulting 50%+ DPR lead over Nick/Aim **before control** is evidence to reduce the reaction payload.

A narrowly numerical optional test is **a 2d6 Sneak Attack reduction on Counterstroke's hit branch only**, leaving Exploit unchanged and still permitting off-turn SA/CS. It is not automatically recommended before observing the branch frequency. With default enemy 75% hit and initial Sap from 93.75% Cane hit, first-attack hit branch=.57421875. The weighted conditional reduction is `.57421875×7.245=4.1602`, mixed total 50.90→49.10; guaranteed first-attack attention 71.09→66.92. If the player waits for a hit, branch frequency changes. This modest change does **not** cure every optimized case and must not be oversold.

Removing Advantage only from Counterstroke is similarly modest: ordinary counter 27.65 versus advantaged 35.54, weighted branch difference≈4.53, mixed 50.90→48.94 before external Advantage. Grappler/Prone can erase that reduction, making it a weak optimized fix. Adding a rest resource is a larger identity cost and isn't supported as the first change. Do not implement several small nerfs simultaneously and then call the test diagnostic.

### Optional tuning table

| Feature | Conservative test | Current | Aggressive ceiling | Expected effect |
|---|---|---|---|---|
|Perfect discount|1 die, three effects|2 dice, three effects|Current plus stacked magic|Conservative restores prices on stronger conditions; stacking is rejected|
|Counterstroke|2 SA dice reduced on hit branch, only if playtest gate met|Advantaged full SA with UD|Sentinel/Grappler/party support and high attention|Frequency/branch policy dominate the numerical effect|
|Cane|Greater bonus, normal mastery selection|Ambiguous stacking/mastery|Added item+skill and automatic mastery|Clarification removes artificial equipment advantage, not signature identity|

## Playtest Plan

Run paired encounters at 3/5/9/11/13/14/17/20 with Bartitsu and the ordinary/official Rogue comparators, same players or rotated players, same party support, same equipment policy. Use at least three repetitions per encounter type and report variability rather than one successful highlight. Separate unchanged current 17 from the 1 die-discount variant; don't change multiple features mid-block.

| Encounter | Variable isolated | What would resolve the uncertainty |
|---|---|---|
|Single strong adjacent melee foe|High attention, one attack|Counter availability versus actual survival and damage lead|
|Strong Multiattack foe|Early/late reaction policy|UD opportunity cost, counter Sap, remaining attacks controlled|
|Two melee foes attacking different allies|Moderate/low Rogue attention|Actual q and Sentinel contribution|
|Archers on open terrain|No close reaction|On-turn adequacy, cost of closing distance|
|Spellcasters using saves and attack rolls|Trigger type; reaction denial|Suppress useful reactions versus absent reaction targets|
|High-STR/DEX/CON enemies|Strong/choice saves|Discount usefulness despite low success; no flat 50% assumption|
|Weak-save minion group|High rider applicability|Repeated two/three packages, party amplification and encounter pacing|
|Armed humanoids with spare weapons|Disarm plus retrieval denial|Actions genuinely lost versus easy pickup|
|Natural-weapon creatures|Disarm nonapplicability|Player finds useful alternatives without universal shutdown|
|Huge creature versus Medium Rogue|Trip/Lock gates|No accidental size bypass; retain other useful riders|
|Legendary boss with strong and weak saves|Voluntary LR decisions|Which failures are meaningful enough to consume LR|
|Crowded melee with allied ranged attackers|Prone amplification/cost|Net party damage, hand occupancy, standing/escape timing|
|Ledges/hazards/auras/choke points|Redirect and Withdraw geometry|Hazard gain, forced separation, real actions/movement denied|
|Long adventuring day versus one nova encounter|At-will sustainability|HP/healing binding resource versus offensive pool exhaustion|
|Optimized Sentinel/Grappler; Light/Nick/Cane switching|Ceiling routine|Opportunity rate after enemy target choices; on-turn ceiling above signature routine|

Record each round/cycle: level and build; target AC and save bonuses; on-turn damage; reaction damage; number of SA; CS package count; effects attempted/successful/immune/size-ineligible; actual dice sacrificed; enemies' attacks redirected/prevented; Sap rolls affected and damage prevented; UD reduction; who was attacked and how often; qualifying miss/hit opportunities; counters used/declined and why; reaction opportunities lost; movement/BA used; hand/weapon state; escape actions and success; enemy turns unable to stand/move/use needed BA; relevant reactions actually denied; party damage helped/harmed; LR spent and effect motivating it; healing and resources used.

Use a counterfactual roll log where practicable: roll both d20 s for a Sap attack so prevented damage can be calculated rather than guessed. Track control prevention separately from Sap/UD to avoid double credit. For Prone, record whether allies attacked before the target stood. For Daze, record whether the foe needed to move or use a BA; a stationary attack turn isn't denied. For Knock Out, record whether the party woke the target before its turn.

Acceptance gate: damage alone should not be the only score. A high-attention Bartitsu should pay material survival/position/reaction costs; record whether those costs actually occur. Flag repeated full-damage double-three-effect cycles against eligible foes, long prone-lock durations, and meaningful LR depletion without an offensive resource. Report low-trigger encounters alongside favorable ones. If the revised 17 discount preserves identity and removes persistent dominance, retain it; if Counterstroke still dominates after costs, test one isolated payload change.

## Direct Answers to the Final Questions

1. **Balanced against 2024 Rogue subclasses?** Levels 3/9 plausibly yes, on the strong side. Levels 13/17 are above ordinary sustained Rogue expectations in frequent adjacent-attack play; overall slightly overtuned pending comparative testing.
2. **Sustained DPR reasonable?** On-turn yes. Encounter-adjusted total ranges from ordinary to excessive depending on effective qualifying attention.
3. **Best-case DPR reasonable?** Early levels plausible;13+ approximately double a strong mundane Rogue routine is an unusually high at-will ceiling, especially with control attached.
4. **Reaction SA too reliable?** At 13+ opportunity is automatic given a qualifying attack. Damage still requires a hit and legal SA. High attention/Sentinel is the concern.
5. **Does Sap push it too far?** Sap materially helps pre 13, bounded by one roll and actual hit/application. At 13 it adds defense, not extra counter frequency. No Sap nerf supported.
6. **Cane+1/+2/+3 appropriate?** Yes as its equipment-budget progression, provided bonuses do not stack and comparator magic access is fair.
7. **Scientific 1 die discount appropriate?** Yes at 9; level 11 and off-turn combinations need testing, not automatic removal.
8. **Four custom costs appropriate?**1/1/2/2 are defensible. Joint Lock's issue is becoming free at 17 and its reach/DC wording, not an obviously wrong base 2 cost.
9. **Counterstroke appropriate at 13?** Strong and conditionally over budget; preserve for focused testing, with a quantified high-attention gate. It is the largest subclass damage jump.
10. **Perfect Leverage appropriate at 17?** Current full package is the clearest tuning target. Test 1 die discount with three effects retained.
11. **Off-turn CS a problem?** Legal and not inherently problematic. Its combination with repeated free strong packages is the issue.
12. **Optimization/multiclass problems?** No proven infinite/automatic dip exploit. Sentinel, grappler-enabled Advantage, weapon switching, stacked bonuses and double packages raise the ceiling; magic stacking should be closed.
13. **Strongest relative to level?** Counterstroke for sustained damage; Perfect Leverage for cumulative control breadth/economy.
14. **Weakest?** Finesse unarmed/improvised damage alone, or Redirect away from meaningful terrain; neither needs buffing because it supplies identity/options.
15. **Change before formal testing?** Nonstacking bonus and explicit rules wording; use a 1 die-discount 17 test version. Keep the other numerical values initially.
16. **What needs actual table testing?** Target attention, survival/healing burden, control durations, escape choices, initiative-dependent party amplification, relevant reaction denial, LR willingness, terrain frequency and optimized weapon/feat routines.

## Sources and Reproducibility Notes

Sources were accessed or checked 5 October 2026. Where rules are available in the licensed SRD, the local SRD is the substantive basis; proprietary subclass summaries are concise. Calculations and judgments are independent derivatives, not copied community DPR tables.

1. Wizards of the Coast, **System Reference Document 5.2.1**, English published 1 May 2025. [Official portal](https://www.dndbeyond.com/srd); [PDF](https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf). Core classes, equipment, conditions, glossary and monster statblocks. SRD data is licensed under[CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/). This audit contains adapted numerical data from the System Reference Document 5.2.1, ©2025 Wizards of the Coast LLC; modifications include extraction, filtering and computed probabilities. No endorsement implied.
2. [Official 2024 Basic Rules—Character Classes](https://www.dndbeyond.com/sources/dnd/br-2024/character-classes), [Rules Glossary](https://www.dndbeyond.com/sources/dnd/br-2024/rules-glossary), [Equipment](https://www.dndbeyond.com/sources/dnd/br-2024/equipment). Verification cross-check with SRD.
3. [Official Sage Advice Compendium](https://www.dndbeyond.com/sources/dnd/sae/sage-advice-compendium). Off-turn SA, UD, unarmed/grapple and OA clarification entries checked.
4. [RPGBOT—Fundamental Math](https://rpgbot.net/dnd5/characters/fundamental_math/),2021,2014-framework AC/hit convention. Updated Bartitsu calculations performed here.
5. [Tabletop Builds—A Primer on Quantitative Evaluation in D&D](https://tabletopbuilds.com/a-primer-on-quantitative-evaluation-in-dd/),2021; [Core Tenets](https://tabletopbuilds.com/core-tenets/). Probability/expected-value and whole-build framing; legacy feats not imported.
6. [Treantmonk—The New Baseline, and T 4 Damage:2024 Player's Handbook](https://www.youtube.com/watch?v=qi3RgN6XhPA),December 2024. Investigated, not numerically reproduced because full model assumptions unavailable.
7. [d4—The New 2024 Baseline](https://dndoptimized.buzzsprout.com/1193507/episodes/15687933-the-new-2024-baseline-d-d-ep-181),September 2024. Public sustained/no-setup/no-resource framing; linked mathematical spreadsheet inaccessible. Not fabricated as a quantitative source.
8. [Official 2024 PHB Errata](https://www.dndbeyond.com/sources/dnd/sae/players-handbook). Current published update list checked.
9. [Licensed2024 Assassin](https://roll20.net/compendium/dnd5e/Subclasses:Assassin?expansion=32231&iframe=true), Roll 20/WotC PHB 2024 expansion. Opening offense, Roving Aim, Envenom and Death Strike.
10. [Licensed2024 Soulknife](https://roll20.net/compendium/dnd5e/Subclasses:Soulknife?expansion=32231&iframe=true), Roll 20/WotC. Weapon dice/Vex, energy pool/Homing, teleport/invisibility/Rend Mind.
11. [Licensed2024 Arcane Trickster](https://roll20.net/compendium/dnd5e/Subclasses:Arcane%20Trickster?expansion=32231), Roll 20/WotC. Spell progression, Ambush, extra Trip, Spell Thief. Thief is included in SRD [1].
12. [Tribality—Scoundrel: A Rogue Archetype](https://www.tribality.com/2019/08/09/scoundrel-a-rogue-archetype-5e/), creator/publisher post 9 August 2019; secondary precedent, not validated balance benchmark.
13. Licensed2024 feats: [Sentinel](https://roll20.net/compendium/dnd5e/Feats:Sentinel?expansion=32231), [Defensive Duelist](https://roll20.net/compendium/dnd5e/Feats:Defensive%20Duelist?expansion=32231), [Dual Wielder](https://roll20.net/compendium/dnd5e/Feats:Dual%20Wielder?expansion=32231); Grappler in SRD [1].

14. [Licensed2024 Battle Master](https://roll20.net/compendium/dnd5e/Subclasses:Battle%20Master?expansion=32231&iframe=true) and [Tavern Brawler](https://roll20.net/compendium/dnd5e/Feats:Tavern%20Brawler?expansion=32231&iframe=true), Roll 20/WotC final 2024 PHB. Maneuver costs/Relentless and unarmed reroll wording checked.

Workbook tabs: Assumptions; Rogue Baselines; Bartitsu On Turn; Reaction DPR; Combined DPR; Sap Defense; Cunning Costs Saves; Control Effects; Level 17 Combos; Multiclass Feats; Sensitivity; Martial Context; Monster Data; Sources. Amber marks editable inputs. Some complex finite defense/empirical-mixture outputs are provided in the independent Python results as well as the report; the workbook's Sap Defense approximation is explicitly labeled rather than presented as the exact policy enumeration. The Homing selector models pool availability, not a false unlimited-rest resource.

To rerun: extract the reproduction bundle, run `python 3 audit_models.py` from its root. This uses bundled derived `monsters.json`, not proprietary project documents. The original source parser additionally requires a text extraction of the licensed SRD at `sources/srd_raw.txt`. The workbook builder requires the documented `@oai/artifact-tool` runtime; the existing workbook itself does not require Python or that runtime for editing in a compatible spreadsheet application.

**Current Balance Verdict: Slightly Overtuned.**

Prioritized supported changes:

1. Prevent stacking Practiced Cane with an object's existing attack/damage bonus.
2. Clarify unarmed Dexterity/Finesse, Cane mastery/profile, Joint Lock reach/escape DC and Redirect movement wording.
3. Test Perfect Leverage with a 1d6 discount while preserving three different effects; retain other numerical values initially.
