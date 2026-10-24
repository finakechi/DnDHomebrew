# Veteran Fighter: Design, Balance, Optimization, and Thematic Investigation

**Ruleset:** D&D 2024 / 5.5e  
**Date:** 2026-09-30  
**Status:** Research recommendation, not a newly accepted project canon  

---

## 1. Executive Summary

The Veteran remains a strong subclass concept, and most of the project’s hard-earned architecture is worth retaining. The present version is not yet coherent enough for a polished next draft, however.

The strongest mechanical thesis is:

> **The Veteran prepares a personal toolkit of practical procedures, uses those procedures to improve actions other Fighters normally leave generic, and enters combat with an immediate plan—while retaining a bounded fallback when that plan fails.**

This is more distinct than “experienced Fighter,” and it occupies territory the 2024 Fighter does not already own. The base Fighter already changes weapon techniques through Weapon Mastery and Tactical Master, converts failed checks through Tactical Mind, repositions through Tactical Shift, and learns from missed attacks through Studied Attacks. A subclass centered on weapon flexibility, numerical skill rescue, post-miss Advantage, or Push/Sap/Slow therefore duplicates the chassis rather than completing it.

The current design contains four partly competing centers:

1. **Hard-Won Lessons:** enhanced universal actions and practical procedures.
2. **Battlefield Readiness:** beginning combat already positioned, searching, or assessing.
3. **Been Here Before / No Lesson Wasted:** changing the toolkit to meet the situation.
4. **Change the Plan:** melee weapon ↔ Unarmed Strike fail-forward attack generation.

The first three can form one coherent identity: **prepared procedures plus bounded adaptation**. The fourth currently behaves like a separate melee-combo subclass.

### Main findings

- **Hard-Won Lessons should remain the primary system**, but the roster needs rebalancing and clearer categories. It is the most distinctive part of the subclass.
- **Practical Experience should stay simple.** Proficiency plus Expertise is enough level-3 noncombat foundation when Lessons carry the specialized fieldcraft.
- **Current Change the Plan should be replaced, not merely numerically nerfed.** Its damage is not extreme, but its strongest play pattern is repeatedly using Grapple/Shove against a target likely to resist so the Veteran recovers a weapon attack. It also leaves ranged Veterans without the subclass’s supposed signature combat loop.
- **The best replacement is a Bonus Action fallback using a different weapon or an Unarmed Strike.** It preserves “the proper method failed, use the backup method,” supports ranged and melee Veterans, creates real equipment/loadout decisions, prevents Action Surge from doubling the trigger, and imposes healthy competition with Polearm Master, Dual Wielder, Second Wind, and Great Weapon Master’s Hew.
- **Battlefield Readiness should remain**, but Assess should not be preserved in its present form merely to service Find the Weak Point. Add a genuine counter-ambush/preparation option and make every choice independently useful.
- **Instant access to any unknown Lesson weakens permanent choice.** Replace the universal Recalled Lesson with a small prepared reserve chosen after a rest. This preserves adaptability while making preparation and specialization matter.
- **Level 15 should deepen contingency play, not add attacks.** The cleanest direction is a delayed third Battlefield Readiness option usable later in the fight, plus broad rest-based Lesson reconfiguration.
- **Veteran of a Hundred Fights is powerful enough for level 18 and thematically sound**, but it is highly binary. It is excellent against one attack-heavy boss, still very good against save-heavy bosses, much weaker against hordes, and partly redundant with Advantage sources. Keep it for testing, but restrict its offensive Advantage to the Veteran’s turn if off-turn optimization becomes excessive.
- **A complete polished next draft is premature.** Two mechanics—the revised Change the Plan and the Lesson-reserve structure—need table testing before exact final wording is locked.

### Recommended architecture

| Fighter level | Recommended role |
|---:|---|
| 3 | Hard-Won Lessons; Practical Experience; revised Change the Plan as a Bonus Action different-method fallback |
| 7 | Battlefield Readiness with four real choices; 5th Lesson |
| 10 | Been Here Before becomes a small prepared Lesson reserve; 6th Lesson |
| 15 | No Lesson Wasted allows broad retraining and a delayed third Readiness option; 7th Lesson |
| 18 | Veteran of a Hundred Fights; 8th Lesson |

---

## 2. Source Retrieval and Current-State Reconstruction

### Library sources retrieved

The following project sources were found and reviewed:

- `Veteran_Current_State_Addendum_2026-09-30.md`, using the preferred `/DnD Homebrew/` copy.
- `VETERAN FIGHTER SUBCLASS — MASTER PROJECT HANDOFF(1).md`.
- `PROJECT EVOLUTION TIMELINE(1).md`.
- `deep-research-report(1).md`, identified by its content as **Veteran Fighter Subclass: Design, Balance, and Optimization Research Report**.
- `Veteran.md`, Iteration D.4.1.
- `Veteran_Fighter_chat_transcript(1).txt`.
- `Veteran_Fighter_Subclass_D4_2.pdf`.
- `Veteran_Work_Context_Pack.md` and `Veteran_Work_Source_Guide.md`, both prepared on 2026-09-30.

Duplicate handoff, timeline, Veteran, transcript, and addendum copies were not counted as independent evidence. The paired handoff and timeline files have identical byte sizes and appear to be duplicate uploads. No post-September-30 Veteran canonical-state file newer than the addendum/context pack was present in `/DnD Homebrew/`.

One detail remains genuinely unavailable: the later chat’s exact eligible-skill list for **Practical Experience**. The accepted concept is preserved, but the exact list is not reproduced in the retrieved sources. That omission does not prevent the architecture or balance analysis.

### Current-state reconstruction

#### Accepted mechanics

- **Hard-Won Lessons** remains the selectable subsystem.
- Lessons known progress at **4 / 5 / 6 / 7 / 8** at Fighter 3 / 7 / 10 / 15 / 18.
- The current roster contains fourteen Lessons.
- **Practical Experience** replaces Veteran’s Eye: one suitable skill proficiency and Expertise in a suitable skill.
- **Battlefield Readiness** grants two different opening options at Fighter 7.
- **Vigilant Response** is removed.
- **Been Here Before** remains in concept.
- **No Lesson Wasted** retains broad rest-based rearrangement, a temporary combat Lesson, and Brace; its obsolete Finish the Wounded clause is gone.
- **Veteran of a Hundred Fights** uses the simplified one-visible-threat Advantage/Disadvantage concept.

#### Provisional mechanics

- **Change the Plan** in its current weapon ↔ Unarmed Strike form.
- Full Weapon Mastery on its generated weapon attack.
- Exact final wording and eligible skills for Practical Experience.
- Exact final wording of Veteran of a Hundred Fights.

#### Unresolved mechanics

- Whether Change the Plan deserves to remain the combat identity.
- How ranged Veterans participate in that identity.
- Whether Recalled Lesson undermines permanent Lesson choices.
- Whether Assess remains useful without Veteran’s Eye / Size Up.
- What level 15 adds beyond flexibility and Brace.
- Whether level-18 offensive Advantage should work on off-turn attacks.
- Lesson pick-rate balance, including evergreen versus niche Lessons.

#### Rejected or superseded mechanics

- Finish the Wounded.
- Veteran’s Eye as a multi-part proficiency/assessment package.
- Tactical Blow.
- Applied Mastery.
- The attack-replacement Veteran Actions engine.
- Vigilant Response.
- Broad additional-Reaction engines.
- Field-Expedient Fighting as a core direction.
- Press the Advantage.
- The old Read the Threat / Punish the Mistake capstone.

#### Historical material usable only as inspiration

- Improvised fighting, equipment expedience, drag-to-cover, threat reading, and dirty-trick concepts from older drafts.
- Older Drill and Veteran Action structures.
- The prior report’s proposed reaction capstone and generic-action compression ideas.

Nothing in the recommendations below reinstates these merely because they once appeared in a complete draft.

---

## 3. Veteran Design Goals

The Veteran is a working combatant rather than a decorated archetype. Its fantasy is built from repeated exposure to danger, not rank, charisma, destiny, or supernatural transformation.

The subclass should be good at:

- recognizing danger and useful terrain;
- carrying and accessing the right mundane tool;
- improving procedures such as Search, Study, Help, Hide, Dodge, Dash, Ready, Utilize, and Opportunity Attacks;
- beginning a fight with an immediate practical response;
- switching to a backup method;
- remaining useful when the campaign changes environment;
- becoming a credible secondary scout, infiltrator, investigator, saboteur, or practical negotiator through selected Lessons.

It should pay opportunity costs. A Veteran who Dodges to hold a passage or Studies a gate’s weak point should be making a situational choice, not converting every non-Attack action into full Fighter DPR.

It should not acquire all of these identities at once:

- Battle Master’s attack-rider tactics;
- Rogue’s efficient action conversion;
- Ranger’s broad wilderness chassis;
- Cavalier’s lockdown;
- Banneret/Warlord command;
- Eldritch Knight’s action-compressed magic.

---

## 4. Unique Mechanical Thesis

### What no other Fighter subclass does

The Veteran can uniquely be the Fighter who:

1. **selects enhanced versions of normally universal procedures;**
2. **executes two prepared procedures immediately when combat begins;**
3. **keeps a small reserve of situational procedures; and**
4. **uses a different physical method when the first method fails.**

This is not the Battle Master loop. A Battle Master normally spends a limited die to attach a maneuver and extra damage to an attack or check. The Veteran’s Lessons are mostly persistent permissions attached to full actions or circumstances, and its tactical advantage is *preparation and procedure*, not a per-hit maneuver budget.

### Primary, supporting, and removable theses

| Role | Thesis | Verdict |
|---|---|---|
| Primary | Enhanced universal actions and practical procedures | Keep and clarify |
| Primary support | Opening-combat readiness | Keep and broaden |
| Primary support | Prepared, bounded adaptation | Keep but revise |
| Secondary support | Different-method fallback after failure | Keep the idea; replace implementation |
| Remove as center | Weapon ↔ Grapple/Shove attack multiplication | Too narrow and build-skewed |
| Remove | Generic “experienced = Advantage” packages | Already supplied elsewhere and mechanically bland |

The current architecture is therefore salvageable, but its center of gravity should move away from Unarmed Strike and toward **procedural preparedness**.

---

## 5. 2024 Fighter Design-Space Analysis

The current official Fighter progression gives the class more tactical and adaptive territory than the 2014 chassis. The official Basic Rules list Weapon Mastery at 1, Tactical Mind at 2, Tactical Shift at 5, Tactical Master at 9, a third Attack-action attack at 11, Studied Attacks at 13, and a fourth Attack-action attack at 20. Action Surge expressly cannot supply a Magic action. [Official Basic Rules: Fighter](https://www.dndbeyond.com/sources/dnd/br-2024/character-classes) [Official 2024 Fighter overview](https://www.dndbeyond.com/posts/1746-2024-fighter-vs-2014-fighter-whats-new)

### Territory already occupied by the base Fighter

| Base feature | Territory it occupies | Veteran consequence |
|---|---|---|
| Weapon Mastery | Weapon-specific riders and loadout choice | Do not build the Veteran around merely knowing more weapon tricks |
| Tactical Mind | Turning failed ability checks toward success | Practical Experience should grant access/identity, not another generic rescue die |
| Tactical Shift | Healing plus safe half-Speed movement | Break Contact and readiness movement must remain distinguishable |
| Tactical Master | On-demand Push, Sap, or Slow substitution | Do not restore Applied Mastery or stack extra mastery properties |
| Studied Attacks | A miss creates Advantage on the next attack | A post-miss feature must do something other than merely grant Advantage |
| Indomitable | Extremely reliable personal saving-throw recovery | High-level defense can be strong, but should not just be another reroll |
| Extra Attack scaling | Three attacks at 11; four at 20 | Full-action Lessons become increasingly expensive and must be situationally excellent |

### Territory still open

- Persistent enhancement of universal actions.
- First-round non-Attack preparation that does not consume the entire turn.
- Mundane equipment, cover, fieldworks, sentry practice, and route discipline.
- A prepared reserve rather than a spell-like resource pool.
- Different-method fallback with real loadout and Bonus Action costs.
- Strong qualitative battlefield information that does not expose stat blocks.
- Adaptation between encounters without duplicating weapon mastery flexibility.

The official rules also make ordinary equipment more mechanically relevant than in 2014. Nets, acid, alchemist’s fire, holy water, oil, hunting traps, manacles, maps, and other gear now have explicit Attack or Utilize procedures. [Official Basic Rules: Equipment](https://www.dndbeyond.com/sources/dnd/br-2024/equipment) This supports equipment-focused Lessons, but not a blanket permission to use every item as a Bonus Action.

---

## 6. Benchmark Methodology

The numerical analysis below is a design benchmark rather than a claim about every table.

### Assumptions

- Ordinary melee accuracy: **65%**.
- Archery accuracy: **75%** after the Fighting Style.
- Advantage converts 65% to **87.75%** and 75% to **93.75%**.
- Ability modifier: +3 at level 3, +4 through level 7, +5 from level 8 onward.
- No magic weapons or external spells.
- Target remains available for all attacks.
- Critical chance is included where shown, but kill-triggered attacks and highly encounter-dependent control value are not monetized.
- Great Weapon Master’s once-per-turn Proficiency Bonus damage is included from level 5 in the simple baseline.
- Polearm assumes Glaive + Polearm Master from level 5.
- Dual-wielding assumes Nick plus the common reading that Dual Wielder can supply its distinct Bonus Action attack. If a table rules otherwise, subtract one off-hand attack.
- Mastery control, ally advantage, forced movement, and defensive riders are discussed separately rather than falsely converted to universal DPR.

### Approximate subclassless sustained DPR reference

These figures are deliberately simple. Their function is to show the size of a Veteran rider relative to the Fighter chassis.

| Level | Sword & board | Greatsword | Polearm | Dual wield | Longbow | Unarmed |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 6.4 | 7.6 | 6.0 | 8.8 | 5.8 | 5.1 |
| 5 | 14.1 | 19.0 | 20.8 | 20.2 | 13.2 | 11.5 |
| 7 | 14.1 | 19.0 | 20.8 | 20.2 | 13.2 | 11.5 |
| 10 | 15.4 | 21.2 | 23.7 | 22.8 | 14.7 | 12.8 |
| 11 | 23.1 | 30.4 | 31.3 | 28.5 | 22.0 | 19.2 |
| 13–15 | 23.1 | 31.3 | 32.2 | 28.5 | 22.0 | 19.2 |
| 18 | 23.1 | 32.3 | 33.2 | 28.5 | 22.0 | 19.2 |
| 20 | 30.8 | 41.3 | 40.7 | 34.2 | 29.4 | 25.6 |

The table omits several benefits favorable to each archetype. Sword-and-board has defense and Shield Master; great weapons have Graze and kill/crit Hew; polearms have reach and Reactive Strike; dual wielders have Vex/Nick sequencing; ranged weapons have range and Slow; grapplers have control. It should not be read as a ranking of complete builds.

---

## 7. Quantitative Balance Analysis

### Current Change the Plan: weapon miss → Unarmed Strike

If a Veteran waits for any miss during the Attack action, the probability that the feature becomes available rises with Extra Attack:

\[
P(\text{at least one miss}) = 1 - P(\text{hit})^n
\]

At 65% accuracy this is 35.0% with one attack, 57.8% with two, 72.5% with three, and 82.1% with four.

Assuming the follow-up damaging Unarmed Strike deals only `1 + Strength modifier`, current Change the Plan adds approximately:

| Fighter level | Attacks in action | Trigger probability | Added DPR, ordinary melee | Added DPR, Nick action |
|---:|---:|---:|---:|---:|
| 3 | 1 | 35.0% | 0.91 | 0.91 |
| 5 | 2 | 57.8% | 1.88 | 2.36 |
| 7 | 2 | 57.8% | 1.88 | 2.36 |
| 10 | 2 | 57.8% | 2.25 | 2.83 |
| 11 | 3 | 72.5% | 2.83 | 3.20 |
| 13 | 3 | 72.5% | 3.82 | 4.33 |
| 15 | 3 | 72.5% | 3.82 | 4.33 |
| 18* | 3 | 32.5% | 1.71 | — |
| 20* | 4 | 40.7% | 2.14 | — |

`*` Level 18/20 figures assume attacks against the target of Veteran of a Hundred Fights and therefore Advantage. Against another target, the level-13/15 rate remains the better estimate.

Studied Attacks is responsible for the jump at level 13: the immediate follow-up attack is normally the Veteran’s next attack against that creature and therefore gains Advantage. This is legal synergy, but it means the subclass’s level-3 feature changes behavior sharply when the base class reaches 13.

With the Unarmed Fighting style, the follow-up damage is materially higher—roughly 5.4 DPR at level 13 with a d8 + 5 Unarmed Strike—but choosing that style has a real opportunity cost.

### Current Change the Plan: resisted Grapple/Shove → weapon attack

This branch is more structurally important than the raw miss branch.

Suppose a target has a 65% chance to succeed on its chosen Strength or Dexterity save and the Veteran’s weapon attack has a 65% hit chance. Replacing one normal attack with Grapple or Shove produces:

- 35% chance to impose the control effect; or
- 65% chance to generate a weapon attack, which then hits 65% of the time.

The result is **35% control plus 42.25% of a weapon hit’s expected damage**. A normal weapon attack produces 65% of a weapon hit’s expected damage. The Veteran therefore buys a 35% control chance by surrendering only 22.75 percentage points of expected weapon-hit probability.

Against a boss with an 80% save-success rate, the control attempt succeeds only 20% of the time, but the fallback recovers 52% of a weapon hit’s expected damage—close to the 65% normal attack. This creates the wrong optimizer incentive:

> The harder the target is to Grapple or Shove, the cheaper it becomes to attempt Grapple or Shove.

That is not an infinite loop and not automatically broken. It is nevertheless the rational default use of the feature, which makes Unarmed Strike control the subclass’s central routine whether or not the player imagined the Veteran as a grappler.

### Action Surge

The current “once during each Attack action” wording allows a second Change the Plan sequence during an Action Surge Attack action. The raw weapon-miss damage remains within a plausible Fighter subclass budget, but the extra control attempts, Weapon Mastery riders, and level-13 Advantage interactions stack into a busier and more reliable nova turn.

A revised “once on each of your turns” trigger avoids Action Surge multiplication without banning useful synergy.

### Graze

Graze already makes a miss productive by dealing the attack ability modifier. Current Change the Plan then adds an Unarmed Strike. This is strong synergy, not automatically an exploit.

Using deliberately poor accuracy is usually still inferior because a greatsword hit is worth more than Graze plus the expected ordinary Unarmed Strike. A deliberately low-accuracy Graze opener becomes theoretically attractive only in contrived combinations where the fallback attack is nearly as valuable as the main hit. Because 2024 Great Weapon Master no longer offers a voluntary −5 accuracy mode, the exploit is mostly theoretical and impractical.

### Mastery and control

- A generated weapon attack retaining its ordinary Mastery is **strong but acceptable in isolation**.
- The branch can apply Push, Sap, Slow through Tactical Master at Fighter 9.
- A weapon miss can deal Graze damage, trigger a Studied Attack at 13, and generate an advantaged Unarmed Strike.
- With Grappler, a damaging Unarmed Strike made as part of the Attack action can also attempt the Grapple option. The official feat requires the Unarmed Strike to be part of the Attack action on the Veteran’s turn. [Official Basic Rules: Grappler](https://www.dndbeyond.com/sources/dnd/br-2024/feats)

The project’s assumption that the generated attack remains part of the triggering Attack action is therefore balance-relevant and should be explicit if retained.

### Veteran of a Hundred Fights

At ordinary 65% accuracy, Advantage raises expected hit probability to 87.75%, a 35% relative increase in landed hits. At Fighter 18 with three attacks, simplified DPR examples against the designated threat become:

| Build | Normal | With capstone Advantage | Increase |
|---|---:|---:|---:|
| Sword & board | 23.1 | 31.6 | +8.5 |
| Greatsword | 32.3 | 42.6 | +10.3 |
| Longbow with Archery | 22.0 | 28.0 | +6.0 |

Defensively, turning an enemy’s 65% hit chance into 42.25% through Disadvantage reduces its landed attack damage by about 35%. If the Veteran normally succeeds on a saving throw 55% of the time, Advantage raises success to 79.75%, reducing failure from 45% to 20.25%.

Those are capstone-scale benefits. They are also highly matchup-dependent:

- excellent against one attack-heavy boss;
- strong against one save-heavy boss;
- less useful when saves still deal half damage;
- weak against many enemies;
- unavailable before the Veteran’s first turn;
- partially redundant with Vex, Prone, Help, and Studied Attacks;
- offensively stronger when Hair Trigger or an Opportunity Attack occurs off turn.

The current capstone is bold but defensible at Fighter 18. It needs playtesting, not immediate replacement.

---

## 8. Feature-by-Feature Critical Audit

### Practical Experience — Keep but clarify

One proficiency plus Expertise gives the Veteran a grounded noncombat identity without rebuilding Rogue’s full skill chassis. Tactical Mind already makes a Fighter unusually good at salvaging failed checks, so another general numerical engine is unnecessary.

Recommended eligible skills: choose proficiency from **Animal Handling, Athletics, Insight, Intimidation, Investigation, Medicine, Perception, Stealth, or Survival**, then choose Expertise in one skill in which the Veteran is proficient from that list. This is a design proposal because the accepted exact list was not recoverable.

### Hard-Won Lessons — Keep but revise roster

The system produces different characters when permanent choices matter. It becomes less differentiating when universal recall and full rest-based replacement allow one character to access nearly the whole list on demand.

Four Lessons at level 3 is appropriate because many are situational rather than competing combat buttons. The 4/5/6/7/8 progression remains reasonable if recall is bounded.

### Change the Plan — Replace current implementation

The concept is excellent. The current mechanics overidentify “adaptation” with melee weapon/unarmed cycling and make the resisted-control branch more attractive than the missed-weapon branch.

The replacement should:

- work for melee and ranged weapons;
- require a genuinely different method;
- use the Bonus Action;
- trigger once per turn, not once per Attack action;
- prevent recursion;
- permit an Unarmed Strike without making Grapple mandatory;
- retain ordinary weapon Mastery on the fallback weapon.

Concrete wording appears in Section 19.

### Battlefield Readiness — Keep but revise options

The two-choice structure is a good level-7 feature. It creates the experience of entering combat already doing the practical thing.

Current option quality is uneven:

- **Take Position** is broadly useful and likely selected almost every combat.
- **Sweep** is situational but can be excellent with Threat Scan or hidden enemies.
- **Assess** is weak at levels 7–9 and often lacks an actionable result.
- **Brace** is useful but unavailable until 15.

Assess should either be rewritten to produce a clear, bounded battlefield conclusion or removed. Add a pre-initiative **Counter-Ambush** option so the menu has a second broadly useful choice without manufacturing attacks.

### Been Here Before — Keep concept; replace universal recall

The current once-per-rest ability to invoke any unknown Lesson makes the rational permanent loadout “evergreen Lessons first; recall the niche answer.” This is not a balance crisis, but it weakens character differentiation and turns the Lesson table into a spellbook.

Recommended solution: after a Short or Long Rest, prepare **two reserve Lessons** not currently known. Once per rest, invoke one reserve Lesson. The Veteran remains adaptable, but the player must anticipate likely trouble.

### No Lesson Wasted — Keep but give it a combat culmination

Broad rest-based reconfiguration is appropriate at 15. The temporary initiative Lesson and Brace are useful, but the feature currently feels like administrative flexibility rather than a high-tier combat feature.

Recommended addition: once per combat, at the start of a turn after the first, use one Battlefield Readiness option not already used in that combat. This produces the fantasy of keeping a reserve plan without adding damage, Reactions, or another attack.

### Veteran of a Hundred Fights — Needs playtesting

Keep the one-threat structure. It is far clearer than the superseded capstone and communicates “I have survived this kind of danger before.”

Primary watchpoint: off-turn attack Advantage. If Hair Trigger, Sentinel, or ordinary Opportunity Attacks make the package too efficient, change offensive Advantage to attack rolls made **on the Veteran’s turn**, while leaving defensive benefits round-long.

---

## 9. Hard-Won Lessons Audit

### Roster classification

| Lesson | Current value | Finding | Recommendation |
|---|---|---|---|
| Forced March | Campaign niche | Excellent in pursuit, retreat, difficult terrain | Keep; consider exhaustion/forced-march exploration rider |
| Break Contact | Broad movement | Strong limited Disengage plus Dash | Keep |
| Field Concealment | Strong team niche | Powerful when stealth matters; meaningful armor exception | Keep; clarify that it affects Hide-action checks, not all travel stealth |
| Shield the Line | Strong defensive choice | Makes Dodge protect two bodies | Keep |
| Hold Ground | Narrow defensive choice | Good when forced movement/prone matter; often inferior to Shield the Line | Keep but strengthen or merge partially |
| Fire-Team Assist | Broad concept, costly action | Ranged Help is useful; full action becomes expensive after level 5 | Revise; tighten ability-check Help and improve tactical payoff |
| Threat Scan | Narrow combat information | Excellent against hidden movers; nearly blank otherwise | Keep as deliberately niche, or broaden to ambush/hazard detection |
| Hair Trigger | Timing tool | Good at 7–10 and 15–19; loses an attack at 11–14 and 20 | Revise scaling to match Fighter attack count or grant a non-damage benefit |
| Hook and Turn | Strong reaction Lesson | Excellent with real Opportunity Attacks | Keep; clarify that Polearm Master’s Reactive Strike is not automatically an Opportunity Attack |
| Common Soldier’s Tongue | Strong social niche | Distinct, mundane, campaign-relevant | Keep |
| Battlefield Activation | Item-dependent high ceiling | Can create Magic action + Bonus Action attack + Action Surge Attack turn | Keep but mark advanced/high-variance; item activation only |
| Sabotage | Good concept, DM burden | Advantage alone is bland; reversal DC useful | Revise toward concrete outcomes and time requirements |
| Quick Barricade | Strong fantasy, environment-dependent | Open questions about materials, dimensions, durability | Keep but write objective material/space limits |
| Find the Weak Point | Useful exploration, weak combat exchange | Full Study for one Advantage is poor; object-only scope is clean | Revise or move earlier to support Assess |

### Mandatory choices

No current Lesson is mandatory across every build, which is good. The closest are:

- Break Contact for melee mobility;
- Hook and Turn for Sentinel/Opportunity Attack builds;
- Hair Trigger for ranged characters who want meaningful subclass combat interaction;
- Field Concealment in stealth-heavy campaigns.

The roster’s larger problem is not one universally mandatory Lesson. It is that several level-3 Lessons enhance full actions that become increasingly expensive, while level-7 reaction/Ready Lessons interact directly with Fighter damage. Players who optimize for frequent combat will naturally select the latter.

### Trap risks

- **Assess without a Study Lesson** is a feature-level trap, not a Lesson trap.
- **Hair Trigger at Fighter 11–14 and 20** can lose more attacks than its d10 recovers.
- **Threat Scan** is a trap if the campaign rarely uses hiding or unseen attackers.
- **Hold Ground** is a trap if forced movement is uncommon and Shield the Line is available.
- **Find the Weak Point** is a trap if the GM rarely presents destructible objects or meaningful structures.

Niche is acceptable when the effect is excellent in its niche and can be prepared. Niche is not acceptable when the player permanently spends a known slot on an effect the campaign never presents.

### Missing Lesson space

The strongest missing areas are:

- **cover discipline** rather than more movement;
- **casualty extraction / field aid**;
- **sentry and counter-ambush routines**;
- **mundane equipment access** without blanket Bonus Action Utilize;
- **route and hazard reading**;
- **confined-space fighting**;
- **prisoner handling / manacles**;
- **weather and fatigue management**;
- **silent hand signals / coordinated stealth**.

Only a few should become Lessons. The roster should not grow merely to check thematic boxes.

---

## 10. Change the Plan Deep Dive

### What works

- The name and fantasy are excellent.
- It rewards failure without erasing failure.
- It produces visible, physical adaptation rather than abstract superiority dice.
- The recursion prohibition is correct.
- Keeping ordinary Mastery on a generated weapon attack is not independently excessive.

### What does not work

- It makes Unarmed Strike the center of a subclass whose fantasy is broader than brawling.
- The ranged Veteran has no equivalent loop.
- It makes repeated Grapple/Shove attempts economically correct even for Veterans who are not grapplers.
- It scales nonlinearly with Extra Attack, Action Surge, Studied Attacks, and Nick.
- It reads like an additional-attack feature more than a procedure learned through experience.

### Recommended conceptual replacement

The Veteran should carry a backup plan—a different weapon, a thrown weapon, a sidearm, a shield edge, a boot, a headbutt, or a grab. The fallback should cost the Bonus Action. This creates a real decision:

- use the fallback now;
- preserve the Bonus Action for Second Wind/Tactical Shift;
- preserve it for Polearm Master, Dual Wielder, or Hew;
- accept the failure and keep resources free.

That decision is more Veteran-like than receiving a free body attack every time an approach fails.

### Expected balance of the replacement

With a similar-damage backup weapon, a one-attack Fighter at 65% accuracy gains roughly `0.35 × 0.65 = 22.75%` of one hit’s damage when the Bonus Action is otherwise free. At higher levels, the probability of at least one miss rises, but the feature remains once per turn and still spends the Bonus Action.

This is generally stronger than the current ordinary Unarmed Strike branch at level 3, but it has three important costs the current feature lacks:

1. Bonus Action competition.
2. A different-weapon/loadout requirement.
3. No second activation from Action Surge.

The feature becomes an equipment and contingency mechanic rather than a free-attack engine.

---

## 11. Feat, Multiclass, and Exploit Audit

### Classification table

| Interaction | Classification | Reason |
|---|---|---|
| Grappler + current weapon-miss branch | Situationally strong | Follow-up damaging Unarmed Strike may also attempt Grapple if it remains part of Attack action |
| Grapple/Shove-first current branch | Likely design problem | Makes resisted control attempts unusually cheap and central |
| Action Surge + current wording | Strong but acceptable numerically; structural concern | One trigger per separate Attack action; doubles control/fallback sequences |
| Studied Attacks | Strong but acceptable | Current immediate follow-up usually has Advantage; sharply improves feature at 13 |
| Graze | Strong but acceptable | Miss deals ability modifier and still enables fallback |
| Nick | Strong but acceptable | More Attack-action rolls increase chance of at least one miss; Bonus Action remains free |
| Sentinel + Hook and Turn | Strong but acceptable | Sentinel explicitly creates Opportunity Attacks; normal Reaction limit contains it |
| Polearm Master Reactive Strike + Hook and Turn | Primarily wording/rules issue | Reactive Strike is a Reaction attack, not automatically an Opportunity Attack |
| Polearm Master/Dual Wielder + revised Bonus Action fallback | Healthy action conflict | Prevents free stacking and makes build choice matter |
| Great Weapon Master | Strong but acceptable | Generated hit can carry once-per-turn PB damage if not already used; Hew competes for Bonus Action in revision |
| Charger | Situationally strong | Fallback weapon hit may qualify if movement and once-per-turn limits are met |
| Shield Master | No problematic trigger | Shield Bash is not the Grapple/Shove option of an Unarmed Strike |
| Mage Slayer + Graze | Strong but official synergy | Graze damage can disrupt Concentration; Veteran adds no loop |
| Battlefield Activation + Action Surge | Situationally strong | Magic-item action + Bonus Action attack + Action Surge Attack is legal but resource/item dependent |
| Ready + Hair Trigger + Action Surge | Strong but acceptable | Can attack normally and Ready via Action Surge; total attacks are bounded and Reaction-dependent |
| Level-18 off-turn Advantage | Needs playtesting | Improves Hair Trigger, Sentinel, and Opportunity Attacks against designated threat |
| Three-level Veteran dip | Strong opportunity cost | Delays primary class progression; most attractive for Monk/Barbarian/Paladin martial builds |
| Monk + current Change the Plan | Situationally strong | Better Unarmed die and Dexterity support; three Fighter levels are costly |
| Rogue + reaction attacks | Theoretical concern | Sneak Attack once per turn values off-turn attacks, but current Veteran has no extra Reaction engine |
| Magic-action loophole | Closed by present Lesson wording | Battlefield Activation is limited to magic-item activation and does not let Action Surge take Magic action |

The relevant 2024 feat wording differs materially from 2014. Great Weapon Master no longer offers −5/+10; Sentinel’s Guardian trigger creates an Opportunity Attack; Polearm Master’s Reactive Strike is worded as its own Reaction attack; Shield Master supplies a once-turn bash after a melee weapon hit; and Mage Slayer focuses on Concentration and one mental-save success. [2024 feat index](https://www.aidedd.org/feat/) [Official Basic Rules: Grappler and Fighting Styles](https://www.dndbeyond.com/sources/dnd/br-2024/feats)

### No recursive loop found

The current explicit rule that a generated attack cannot trigger Change the Plan again closes the obvious recursion. No practical forced-movement, Opportunity Attack, Mastery, or Ready loop was found that creates unlimited attacks.

The main exploit concern is therefore **dominant routine**, not infinity: attempt control against strong saves, recover a weapon attack when the target resists, and use the feature again on the next Attack action.

---

## 12. Official Fighter Subclass Comparison

The 2024 Player’s Handbook’s official Fighter subclasses establish a wide balance envelope. Battle Master receives four d8 Superiority Dice at 3, five at 7, six at 15, and at 15 can use a free d8 maneuver once per turn instead of spending a die. Champion combines expanded criticals, Initiative/Athletics Advantage, another Fighting Style, renewable Heroic Inspiration in combat, and regeneration while Bloodied at 18. Eldritch Knight gains Wizard spellcasting and eventually replaces attacks with cantrips or low-level spells. Psi Warrior has a long-rest pool covering damage, defense, movement, and control. [Official subclass update summary](https://www.dndbeyond.com/posts/1810-updates-in-the-players-handbook-2024) [2024 Fighter subclass reference](https://www.aidedd.org/en/fighter-2024/) [RPGBOT 2024 subclass analysis](https://rpgbot.net/2024-dnd/classes/fighter/fighter-subclasses/)

| Category | Battle Master | Champion | Eldritch Knight | Psi Warrior | Recommended Veteran |
|---|---|---|---|---|---|
| Sustained damage | Moderate–high, resource sensitive; free maneuver at 15 | Low–moderate passive | High ceiling through spell/attack integration | Moderate, die-limited | Low–moderate conditional fallback |
| Nova | Strong die expenditure | Fighter baseline | Highest ceiling | Moderate | Fighter baseline; no attack multiplication |
| Defense | Maneuver choices | Excellent at 18 | Excellent through spells | Strong protective dice | Situational Lessons; strong single-threat capstone |
| Control | Excellent maneuvers | Mastery only | Spells + mastery | Telekinetic control | Equipment, universal actions, selected Lessons |
| Mobility | Maneuvers | Crit movement | Spells/teleport | Telekinetic movement/flight | Readiness, Dash Lessons, fallback positioning |
| Exploration | Limited maneuvers/tools | Athletics | Spells | Telekinesis | Primary mundane strength |
| Social | A few maneuvers | Minimal | Spells | Minimal | Common Soldier’s Tongue / Expertise |
| Resource dependence | Short-rest dice | Very low | Long-rest slots | Mostly long-rest dice | Mostly at-will; one reserve use/rest |
| Build flexibility | High | Medium | High but Int/spells constrain | Medium, Int helpful | High through Lessons and reserve |
| Complexity | High | Low | High | Medium | Medium-high |

### Older compatible comparisons

- **Cavalier:** a warning against drifting into Sentinel-style lockdown and reaction multiplication.
- **Samurai:** a benchmark for burst Advantage and social utility; its identity is more resolve/honor than working survival.
- **Rune Knight:** a benchmark for broad utility plus strong combat states, but its runes and Giant’s Might are supernatural and highly resource/action-economy driven.

The Veteran should not beat Battle Master at attack riders, Eldritch Knight at action-compressed versatility, Champion at effortless durability, and Psi Warrior at ranged protection simultaneously. Its comparative advantage should be **mundane preparedness and non-Attack procedures**.

---

## 13. Historical and Practical Veteran Research

Modern doctrine is not a direct model for fantasy combat, but it is useful evidence for what working soldiers actually practice. The U.S. Army’s ATP 3-21.8 organizes infantry work around movement techniques, actions on contact, route selection, danger areas, patrol bases, rally points, rehearsals, equipment checks, security, camouflage/noise/light discipline, sustainment, maintenance, casualty roles, observation posts, detainees, field fortifications, breaching, and deliberate contingencies. [U.S. Army ATP 3-21.8 doctrine supplement](https://www.benning.army.mil/infantry/DoctrineSupplement/ATP3-21.8/) [Army publication notice](https://www.army.mil/article/167323/atp_3_218_infantry_platoon_and_squad_now_available_for_download)

That list matters because it shows that “veteran experience” is not mostly a collection of special strikes. It is a collection of procedures that reduce surprise, friction, exposure, fatigue, wasted supplies, and confusion.

Historical armies reinforce the same themes:

- marching camps and field fortification;
- sentries, passwords, alarms, and watches;
- ration, water, baggage, and ammunition discipline;
- weapon and equipment maintenance;
- disease prevention and camp hygiene;
- knowing when terrain is defensible or dangerous;
- drill that converts panic into rehearsed action;
- practical solidarity among people who share dangerous work.

### Table-useful abstractions

| Practical experience | Bad abstraction | Better game decision |
|---|---|---|
| Sentry routine | Permanent Perception Advantage | Choose counter-ambush readiness instead of movement or temp HP |
| Route selection | Generic Survival bonus | Identify one travel hazard and choose speed, stealth, or fatigue mitigation |
| Immediate-action drill | Free attack | Spend opening readiness on movement, Search, cover, or draw/equip |
| Equipment checks | “Your gear never breaks” | Keep a prepared reserve item or access one carried item efficiently |
| Field fortification | Flat AC bonus | Spend action/materials to create an edge of Half Cover |
| Casualty evacuation | Healing magic substitute | Drag a willing/unconscious ally without the usual movement penalty |
| Fire discipline | Damage bonus | Delay/readied attacks more reliably or avoid wasting reaction on invalid trigger |
| Rally point | Aura/command | Choose a personal fallback space and gain movement when isolated |
| Pattern recognition | Stat-block extraction | After observing an attack/save, choose one bounded defensive preparation |
| Maintenance/logistics | Advantage on tools forever | During a rest, prepare one equipment-related contingency |

The most promising overlooked fantasy is **contingency discipline**: the Veteran is not omniscient; the Veteran has rehearsed what to do when contact, terrain, equipment, or the plan goes bad.

---

## 14. Overlooked Design Space

### High-value spaces

1. **Counter-ambush choice.** A readiness option chosen before Initiative that removes Surprise’s Initiative Disadvantage or provides a bounded reroll.
2. **Casualty movement.** Carry or drag a willing, Grappled, or unconscious creature without the ordinary extra movement cost for a short distance.
3. **Cover discipline.** Improve the benefit or accessibility of existing cover without conjuring cover.
4. **Prepared reserve gear.** Designate a small number of carried mundane items after a rest and access them without hand-juggling friction.
5. **Confined-space technique.** Avoid penalties or gain positioning benefits when fighting in a doorway, corridor, ship passage, or cramped space.
6. **Known route / rally point.** Mark a space or route as a fallback, then move toward it when threatened.
7. **Sentry communication.** Silent warnings or Help/Search coordination that does not become Warlord command.
8. **Post-contact assessment.** After a creature reveals a tactic, gain a bounded defense against repetition—not immunity or full stat knowledge.

### Spaces to reject or treat cautiously

- **Supply creation:** risks conjuring equipment or trivializing campaign logistics.
- **Consumable conservation:** creates economy abuse and magic-item problems.
- **Universal weather/fatigue immunity:** passive and campaign-erasing.
- **Formation auras:** drifts toward officer/Warlord identity.
- **Exact AC/HP/save extraction:** gamey and contrary to the project’s preference for qualitative information.
- **Open-ended dirty tricks:** creates negotiation burden rather than clear decisions.
- **Blanket Bonus Action Utilize:** too broad under 2024 equipment rules.

---

## 15. Filtered Mechanical Idea Bank

### Excellent candidates

#### A. Backup Method

- **Fantasy:** the first weapon or technique fails; use the sidearm, thrown weapon, shield edge, boot, or grab.
- **Concept:** once per turn after a miss or resisted Grapple/Shove, spend Bonus Action to attack the same creature with a different weapon or Unarmed Strike.
- **Cost:** Bonus Action; loadout constraint.
- **Level:** 3.
- **Overlap:** less than Battle Master because it does not add a maneuver rider or die.
- **Risk:** weapon-draw timing and “different weapon” definition.
- **Verdict:** develop now.

#### B. Prepared Lesson Reserve

- **Fantasy:** anticipated contingencies recorded or rehearsed during rest.
- **Concept:** prepare two unknown Lessons; once per rest invoke one.
- **Cost:** preparation slot and one/rest use.
- **Level:** 10.
- **Overlap:** superficially spell-like preparation, but entirely mundane and much smaller.
- **Risk:** still favors evergreen permanent picks, though reserve scarcity makes the choice real.
- **Verdict:** develop now.

#### C. Reserve Readiness

- **Fantasy:** the first plan was not the only plan.
- **Concept:** once per combat after round one begins, use a Readiness option not already used.
- **Cost:** delayed timing; option cannot repeat.
- **Level:** 15.
- **Overlap:** none significant.
- **Risk:** option roster must be healthy.
- **Verdict:** develop now.

#### D. Counter-Ambush

- **Fantasy:** sentry habits and immediate-action drills.
- **Concept:** choose as a Readiness option before Initiative; remove Disadvantage caused by Surprise and possibly gain a small initiative benefit.
- **Cost:** occupies one of two Readiness choices.
- **Level:** 7.
- **Overlap:** Champion has permanent Initiative Advantage; Veteran chooses this situationally.
- **Risk:** selection timing must occur before the Initiative roll.
- **Verdict:** develop now.

#### E. Casualty Extraction Lesson

- **Fantasy:** get the wounded out of the killing ground.
- **Concept:** when moving a willing, Grappled, or unconscious ally no larger than you, ignore the ordinary extra movement cost for a limited distance; perhaps stabilize at the destination if using a Healer’s Kit.
- **Cost:** movement and possibly Utilize action/item.
- **Level:** 3 or 10.
- **Overlap:** not magical healing and not command.
- **Risk:** Grapple rules and carrying capacity need precise wording.
- **Verdict:** promising Lesson.

### Interesting but flawed

#### Pattern Defense

After a creature hits or forces a failed save, gain a defense against the next similar effect. The fantasy is excellent, but defining “similar” creates rules disputes; defining it as the same attack or named action requires monster stat-block terminology players may not know. Keep as capstone inspiration, not current wording.

#### Improve Cover

Treat Half Cover as Three-Quarters Cover while stationary. This is mechanically clean but can create passive “stand here forever” play and is highly map-dependent. Better as a Lesson attached to Dodge or a first-round readiness option.

#### Prepared Consumable

Produce or preserve an oil, acid, antitoxin, or similar item. This creates gold/economy questions and setting dependence. Prefer access/action benefits for items actually carried.

#### Confined-Space Fighting

Useful fantasy, but 2024 rules seldom impose a universal cramped-space penalty. A feature would need to invent its own trigger and risks becoming a disguised always-on bonus in dungeon corridors.

### Reject

- Extra Reaction every round.
- Free generic Utilize each turn.
- Apply two Mastery properties.
- Convert failed attack directly into automatic damage.
- Give the whole party formation bonuses.
- Any “Veteran always has the needed item” rule without cost and limits.

---

## 16. Competing Design Directions

### Direction A — Procedural Veteran (recommended)

**Primary thesis:** Select practical procedures, execute two at contact, and keep one backup method.

**Core loop:** Build a Lesson identity; choose opening Readiness; attack normally; spend Bonus Action on a different-method fallback when failure creates the need; use prepared reserve Lessons for predicted situations.

| Level | Structure |
|---:|---|
| 3 | Hard-Won Lessons, Practical Experience, Backup Method Change the Plan |
| 7 | Battlefield Readiness, four viable options |
| 10 | Prepared reserve Lessons |
| 15 | Broad retraining plus Reserve Readiness |
| 18 | Veteran of a Hundred Fights |

**Survives:** almost the entire architecture, most Lessons, capstone concept.  
**Changes:** Change the Plan, recall, readiness roster, level-15 combat value.  
**Removed:** current free weapon/unarmed attack chain; universal unknown-Lesson recall.

**Strengths:** strongest continuity; clear equipment fantasy; supports ranged; distinct from Battle Master; moderate complexity.  
**Weaknesses:** many Lessons remain situational; Bonus Action pressure can make the signature fallback unavailable to some builds.  
**Optimization risk:** medium-low.  
**Thematic strength:** very high.

### Direction B — Contingency Veteran

**Primary thesis:** Prepare trigger-response contingencies and reveal them when the predicted failure occurs.

**Core loop:** After each rest, choose several contingencies such as Ambush, Failed Attack, Ally Down, Forced Movement, Hidden Threat, or Broken Position. Trigger one to gain a bounded response.

| Level | Structure |
|---:|---|
| 3 | Three prepared contingencies; Practical Experience |
| 7 | Additional contingency and first-round response |
| 10 | Reprepare one contingency after Short Rest |
| 15 | Trigger a second contingency per combat or retain an expended one |
| 18 | One-threat pattern mastery |

**Role of Lessons:** Lessons are rewritten as contingencies or reduced to a smaller utility list.  
**Role of Change the Plan:** absorbed into Failed Attack contingency.

**Strengths:** clearest “knows what goes wrong” identity; excellent thematic unity.  
**Weaknesses:** major rewrite; trigger tracking; risks feeling like Battle Master maneuvers with different timing; dead choices when triggers never occur.  
**Complexity:** high.  
**Optimization risk:** medium-high because trigger frequency varies greatly.  
**Verdict:** excellent fallback direction if Direction A playtests incoherently, not the next pass.

### Direction C — Fieldcraft and Equipment Specialist

**Primary thesis:** Turn terrain, cover, tools, and mundane equipment into the Fighter’s second weapon system.

**Core loop:** Prepare gear, create cover/obstacles, use equipment efficiently, breach or sabotage, and switch between weapon combat and environmental control.

| Level | Structure |
|---:|---|
| 3 | Field kit and equipment Lessons; Practical Experience |
| 7 | Opening deployment/cover selection |
| 10 | Advanced sabotage, barricades, magic-item activation |
| 15 | Reuse or reposition one preparation |
| 18 | Treat the battlefield as familiar terrain |

**Role of Lessons:** heavily equipment/environment focused.  
**Role of Change the Plan:** replaced by efficient access or use of carried gear.

**Strengths:** extremely mundane and distinctive; strong exploration identity.  
**Weaknesses:** dependent on maps, materials, GM rulings, gold, and item availability; risks Rogue/Thief overlap; hard to balance across campaigns.  
**Complexity:** medium at character sheet, high at table.  
**Optimization risk:** high with future equipment and magic items.  
**Verdict:** mine for Lessons, not recommended as the whole subclass.

---

## 17. Recommended Direction

Choose **Direction A: Procedural Veteran**.

It preserves the work that is genuinely distinctive, solves ranged exclusion, and avoids rebuilding the subclass around another resource pool. It also creates a coherent sequence:

```text
Rest: choose procedures and reserves
        ↓
Initiative: choose immediate readiness
        ↓
Turn: execute normal Fighter plan
        ↓
Failure: spend Bonus Action on a different method
        ↓
Later setback: use reserve readiness / reserve Lesson
```

### Major mechanic classification

| Mechanic | Classification | Explanation |
|---|---|---|
| Practical Experience | Keep but revise | Accepted concept is sound; recover/choose exact skill list |
| Hard-Won Lessons | Keep but revise | Best identity system; rebalance roster and recall access |
| 4/5/6/7/8 progression | Keep | Appropriate for fourteen mostly situational choices |
| Current Lesson roster | Keep but revise | Several are strong; several need clearer niches or scaling |
| Current Change the Plan | Replace | Melee/grapple dominant, ranged exclusion, wrong optimizer routine |
| Battlefield Readiness | Keep but revise | Two-choice opener is strong; option quality and timing need repair |
| Been Here Before | Replace implementation | Use prepared reserve rather than universal recall |
| No Lesson Wasted | Keep but revise | Add delayed third Readiness option; remove obsolete clauses |
| Veteran of a Hundred Fights | Needs playtesting | Capstone-scale and clear, but binary and Advantage-saturated |
| Hair Trigger | Keep but revise | Scale attack count cleanly at 11 and 20 or change its compensation |
| Hook and Turn | Keep | Strong, bounded, distinct; clarify OA terminology |
| Battlefield Activation | Needs playtesting | High item variance and Action Surge nova; wording is appropriately narrow |
| Assess | Replace or gate | Weak without a Study Lesson; do not preserve dependency |
| Brace | Keep but revise | 2 × PB THP is serviceable; test against other opening choices |

---

## 18. Recommended Level Architecture

### Fighter 3

**Hard-Won Lessons.** Four known.  
**Practical Experience.** One suitable proficiency plus one suitable Expertise.  
**Change the Plan.** Bonus Action different-method fallback, once per turn.

Level 3 should establish all three pillars: learned procedures, real-world competence, and fallback method. No additional damage die is necessary until testing shows the fallback is too weak.

### Fighter 7

**Battlefield Readiness.** When combat begins, choose two different options from a healthy list. The choice timing moves to Initiative so Counter-Ambush can function.

Suggested options:

- **Counter-Ambush:** remove Initiative Disadvantage caused by Surprise; if not Surprised, add a smaller bounded benefit such as +PB to Initiative only if this option was chosen before rolling.
- **Take Position:** at the start of the first turn, move up to half Speed.
- **Sweep:** at the start of the first turn, take Search.
- **Dig In:** gain PB Temporary Hit Points; improves to 2 × PB at 15.

Assess is removed from the default list unless rewritten to produce a reliable bounded conclusion.

### Fighter 10

**Been Here Before.** Prepare two reserve Lessons after a Short or Long Rest. Once per Short or Long Rest, use one reserve Lesson as though known for its named action or Reaction.

This is preparation, not instant access to the whole table.

### Fighter 15

**No Lesson Wasted.** After a Short or Long Rest, replace any number of known Lessons. Increase or refresh the reserve as appropriate. Once per combat, at the start of a turn after the first, use one Battlefield Readiness option not already used during that combat.

This is enough combat power to test before adding damage. A free half-move, Search, or 10 THP at the right later moment is meaningful without creating another attack.

### Fighter 18

**Veteran of a Hundred Fights.** Keep the one-visible-creature focus for testing. If offensive off-turn Advantage proves excessive, restrict only the attack-roll Advantage to the Veteran’s turn.

---

## 19. Candidate and Revised Mechanics

These are testable prototypes, not final polished rules.

### Practical Experience

**Concept:** credible work experience without rebuilding Veteran’s Eye.

> **Practical Experience**  
> You gain proficiency in one of the following skills of your choice: Animal Handling, Athletics, Insight, Intimidation, Investigation, Medicine, Perception, Stealth, or Survival. You also gain Expertise in one skill of your choice from that list with which you have proficiency.

**Balance role:** noncombat identity; combines well with Tactical Mind but does not duplicate its failure-recovery mechanic.

### Change the Plan — Backup Method prototype

> **Change the Plan**  
> When the proper method fails, you immediately try something else. Once on each of your turns, immediately after you miss a creature with a weapon attack, or after a creature succeeds on its saving throw against the Grapple or Shove option of your Unarmed Strike, you can use a Bonus Action to make one attack against that creature with a different weapon or with an Unarmed Strike.  
>  
> If the triggering attack used a weapon, the follow-up attack must use a different weapon or an Unarmed Strike. If the triggering Unarmed Strike attempted to Grapple or Shove, the follow-up attack must use a weapon.  
>  
> An attack made with this feature can’t trigger this feature.

**Open wording question:** whether drawing the fallback weapon is included. Recommended addition for usability:

> You can draw or stow one weapon as part of the follow-up attack.

**Expected role:** modest conditional DPR, visible loadout switching, meaningful Bonus Action conflict, ranged compatibility.

**Important interactions:**

- The fallback attack is not automatically part of the Attack action; therefore Grappler’s Punch and Grab does not attach to a Bonus Action damaging Unarmed Strike.
- Ordinary weapon Mastery applies if the Veteran has mastery for the fallback weapon.
- Action Surge does not create a second use because the feature is once per turn.
- Polearm Master, Dual Wielder, Hew, and Second Wind compete for the Bonus Action.

### Been Here Before — prepared reserve prototype

> **Been Here Before**  
> When you finish a Short or Long Rest, choose two Veteran Lessons for which you qualify and that you don’t know. These are your Reserve Lessons until you choose again.  
>  
> When you take an action or Reaction that could benefit from one of your Reserve Lessons, you can use that Lesson as though you knew it. You must decide before making any roll required by the action or Reaction. Once you use this feature, you can’t use it again until you finish a Short or Long Rest.

**Balance role:** bounded flexibility and preparation.

### Battlefield Readiness — structural prototype

> **Battlefield Readiness**  
> When you roll Initiative, choose two different options below. Resolve Counter-Ambush immediately. Resolve each other chosen option at the start of your first turn in the combat, in either order. You can’t choose an option more than once in the same combat.

Candidate options:

- **Counter-Ambush.** If you have Disadvantage on the Initiative roll because you are Surprised, ignore that Disadvantage.
- **Take Position.** Move up to half your Speed without provoking Opportunity Attacks.
- **Sweep.** Take the Search action.
- **Dig In.** Gain Temporary Hit Points equal to your Proficiency Bonus. At Fighter 15, the Temporary Hit Points equal twice your Proficiency Bonus.

**Design caution:** Counter-Ambush may be too weak when the Veteran is not Surprised. Do not add permanent Initiative Advantage casually; that would closely duplicate Champion. A playtest alternative is a reroll of Initiative that must be used.

### No Lesson Wasted — reserve readiness prototype

> **No Lesson Wasted**  
> Whenever you finish a Short or Long Rest, you can replace any number of Veteran Lessons you know with other Lessons for which you qualify.  
>  
> In addition, once per combat at the start of one of your turns after your first turn, you can use one Battlefield Readiness option you have not already used in that combat.

This wording intentionally does not add an attack, Reaction, or damage die.

### Veteran of a Hundred Fights — test wording

> **Veteran of a Hundred Fights**  
> At the start of each of your turns in combat, choose one creature you can see. Until the start of your next turn, you have Advantage on attack rolls against that creature and on saving throws it forces you to make, and its attack rolls against you have Disadvantage.

**First pullback if needed:** “You have Advantage on attack rolls you make **on your turn** against that creature.”

### Hair Trigger — scaling repair options

Current Hair Trigger becomes awkward at Fighter 11–14 and loses an attack at 20.

Two viable repairs:

1. **Match Extra Attack:** the readied Attack action makes the same number of attacks the Fighter could make with the Attack action on its turn, and one hit gains +1d10. This is clean but gives a powerful off-turn full attack.
2. **Fixed attacks plus stronger timing payoff:** keep two attacks (three at 15), but add a non-damage benefit such as movement before the readied action. This preserves the cost at 11/20 but may remain a trap.

Recommendation: test option 1 while retaining the normal Reaction and trigger risks. Hair Trigger does not create an extra action; it improves an action the Fighter already spent its turn Readying.

### Two promising new Lessons

#### Get Them Clear — Dash

> When you take the Dash action, you can move through the space of one willing or unconscious creature of your size or smaller and move that creature with you for up to half your Speed. This movement doesn’t provoke Opportunity Attacks from one creature of your choice that you can see. You must end in a space that can hold both creatures or place the moved creature in an unoccupied space within 5 feet of you.

This needs grid testing and a carrying-capacity safeguard.

#### Field of Fire — Dodge

> When you take the Dodge action while benefiting from Half Cover, you gain the benefits of Three-Quarters Cover until the start of your next turn or until you leave that cover.

This is simple and map-dependent. It is intentionally a niche Lesson rather than a passive AC bonus.

---

## 20. Optional Full Next Draft

A full polished next draft is **not yet justified**.

The recommended architecture is stronger than the current one, but two foundational questions require actual play:

1. Does Bonus Action Change the Plan occur often enough to feel like a signature rather than an occasional consolation?
2. Does a prepared two-Lesson reserve preserve meaningful permanent choices, or do players still choose the same evergreen Lessons?

Writing a complete subclass now would make uncertain decisions look settled and would create unnecessary wording churn. The next artifact should be a compact playtest packet containing the existing stable Lessons plus the prototypes above.

---

## 21. Playtest Plan

### Test characters

At minimum, build these Veterans at levels 3, 7, 11, 15, and 18:

- sword-and-board;
- greatsword/Graze;
- glaive/Polearm Master;
- Nick dual wielder;
- longbow/Archery;
- Unarmed Fighting + Grappler.

At level 11+, include Strength and Dexterity Veterans. At level 18, test with and without frequent Reaction attacks.

### Encounter matrix

| Test | Setup | Watch |
|---|---|---|
| Sustained combat | 4 rounds, equal-level mixed enemies | Change the Plan activations; Bonus Action conflicts; Lesson relevance |
| Nova | Action Surge on round 1 or 2 | Attack count; mastery stacking; fallback frequency |
| Solo boss | High AC, high Str/Dex saves, legendary actions | Control-spam incentive; capstone suppression |
| Save boss | Few attacks, repeated saves | Capstone save value; whether offense dominates |
| Horde | 6–10 weaker enemies | Capstone target switching; Sweep value; wasted overkill |
| Melee cramped | Doorways, cover, forced movement | Hold Ground, Shield the Line, Hook and Turn |
| Melee open | 60–100 foot starting distance | Take Position, Dash Lessons, ranged fallback |
| Ranged | Elevation and cover | Does revised Change the Plan feel equally valid? |
| Grappling | Mixed strong/weak saves and sizes | Whether control attempts remain rational but not automatic |
| Ambush | Veteran Surprised; hidden enemies | Counter-Ambush and Sweep value |
| Search | Hidden mover and concealed object | Threat Scan resolution speed and payoff |
| Study | Monster clues plus destructible structure | Assess/Find Weak Point usefulness without stat extraction |
| Exploration | Forced march, bad weather, route hazard | Niche Lesson power and reserve preparation |
| Social | Guards, sailors, mercenaries, civilians | Common Soldier’s Tongue boundaries |
| Equipment | Nets, oil, manacles, barricade materials, magic item | Utilize/Magic wording and GM burden |
| Multiclass | Fighter 3 / Monk, Barbarian, Rogue, Paladin | Fallback attack damage and action conflicts |

### Metrics to record

For every combat, record:

- number of rounds;
- each Readiness option chosen;
- each Lesson used;
- each time a known Lesson was irrelevant;
- each reserve Lesson prepared and used;
- Change the Plan trigger opportunities;
- Change the Plan uses declined because Bonus Action was occupied;
- fallback hits and control outcomes;
- additional DPR from fallback;
- whether the player intentionally chose a lower-probability method to farm a fallback;
- capstone-designated target and percentage of enemy offense it represented;
- rules questions requiring GM adjudication.

### Decision thresholds

#### Revised Change the Plan

- **Too weak:** used in fewer than 25% of combat rounds when Bonus Action is available, or ranged players cannot maintain a plausible backup loadout.
- **Too strong:** contributes more than about one full ordinary weapon hit per round over a multi-encounter sample, or makes a low-accuracy opener rational.
- **Mandatory build distortion:** players avoid all Bonus Action feats solely to preserve it.
- **Healthy:** activates roughly once every 2–3 rounds, sometimes loses to another Bonus Action, and makes weapon/loadout choice visible.

#### Lessons

- **Mandatory:** selected by at least five of six archetypes and used in most encounters regardless of scenario.
- **Trap:** selected during character creation but unused across three deliberately varied sessions.
- **Appropriately situational:** used rarely overall but clearly encounter-changing when its advertised niche appears.
- **Too weak:** even in its designed scenario, the player would rather take the ordinary Attack action.
- **Too strong:** erases another class’s signature or makes the named full action effectively free.

#### Prepared reserve

- **Too broad:** the player always has the exact answer and permanent Lesson choices stop mattering.
- **Too narrow:** reserve choice is routinely wrong despite reasonable scouting.
- **Healthy:** at least one reserve matters per adventuring day, but the Veteran still wishes for Lessons not selected.

#### Battlefield Readiness

- **Default collapse:** the same two options are chosen in more than 75% of varied encounters.
- **Weak option:** chosen only when the test artificially forces its niche.
- **Healthy:** Take Position remains common, but at least three options regularly compete for the second choice.

#### Level 18

- **Too strong:** designated boss loses more than half its expected effective offense while Veteran DPR rises by 40%+ and off-turn attacks remain frequent.
- **Too weak:** multi-enemy encounters make the feature feel absent for most rounds.
- **Binary:** encounter outcome changes almost entirely based on whether one creature accounts for most enemy actions.
- **First adjustment:** restrict offensive Advantage to the Veteran’s turn, not reduce all three benefits at once.

---

## 22. Highest-Priority Remaining Questions

1. Does the user prefer Change the Plan to cost a Bonus Action if that makes it cleaner, ranged-compatible, and less exploitable?
2. Should “different weapon” mean a different weapon **kind**, a different physical weapon, or merely a weapon other than the one that missed?
3. Should the fallback allow drawing/stowing one weapon as part of the attack?
4. Is Counter-Ambush allowed to be useless when the Veteran is not Surprised, or should it have a small secondary initiative benefit?
5. Should Assess be cut, rewritten, or supported by moving Find the Weak Point to level 7?
6. Is a prepared reserve of two Lessons enough to feel adaptable without recreating universal recall?
7. Should Hair Trigger match the Fighter’s current number of Attack-action attacks at all levels?
8. Does the level-18 feature’s offense need to be on-turn only?
9. Which two new Lesson fantasies deserve roster space: casualty extraction, cover discipline, sentry routine, route reading, equipment access, or prisoner handling?
10. What exact skill list was accepted for Practical Experience in the later project chat?

---

## 23. Sources

### Project sources

- `Veteran_Current_State_Addendum_2026-09-30.md`
- `VETERAN FIGHTER SUBCLASS — MASTER PROJECT HANDOFF(1).md`
- `PROJECT EVOLUTION TIMELINE(1).md`
- `Veteran_Work_Context_Pack.md`
- `Veteran_Work_Source_Guide.md`
- `Veteran.md` — Iteration D.4.1
- `Veteran_Fighter_Subclass_D4_2.pdf`
- `Veteran_Fighter_chat_transcript(1).txt`
- `deep-research-report(1).md` — prior Veteran design/balance report

### Official/current D&D sources

- [D&D Beyond Basic Rules (2024/5.5e): Character Classes](https://www.dndbeyond.com/sources/dnd/br-2024/character-classes)
- [D&D Beyond Basic Rules: Rules Glossary](https://www.dndbeyond.com/sources/dnd/br-2024/rules-glossary)
- [D&D Beyond Basic Rules: Equipment and Weapon Mastery](https://www.dndbeyond.com/sources/dnd/br-2024/equipment)
- [D&D Beyond Basic Rules: Feats](https://www.dndbeyond.com/sources/dnd/br-2024/feats)
- [D&D Beyond: 2024 Fighter vs. 2014 Fighter](https://www.dndbeyond.com/posts/1746-2024-fighter-vs-2014-fighter-whats-new)
- [D&D Beyond: Updates in the Player’s Handbook (2024)](https://www.dndbeyond.com/posts/1810-updates-in-the-players-handbook-2024)

### Secondary rules and optimization references

- [AideDD 2024 Fighter and subclass reference](https://www.aidedd.org/en/fighter-2024/)
- [AideDD 2024 feat index](https://www.aidedd.org/feat/)
- [RPGBOT: 2024 Fighter subclasses](https://rpgbot.net/2024-dnd/classes/fighter/fighter-subclasses/)
- [RPGBOT: 2024 Fighter class guide](https://rpgbot.net/2024-dnd/classes/fighter/)

### Historical/practical references

- [U.S. Army ATP 3-21.8: Infantry Platoon and Squad doctrine supplement](https://www.benning.army.mil/infantry/DoctrineSupplement/ATP3-21.8/)
- [U.S. Army publication notice for ATP 3-21.8](https://www.army.mil/article/167323/atp_3_218_infantry_platoon_and_squad_now_available_for_download)
- [TC 7-21.13: Soldier’s Guide](https://media.defense.gov/2018/Apr/06/2002670644/-1/-1/1/180406-N-ZZ320-1084.pdf)

---

## Final Judgment

The strongest Veteran is not “the Fighter who has seen every weapon trick,” because the 2024 Fighter already approaches that fantasy. It is not “the Fighter who grapples after missing,” because that is too small and too melee-specific to carry the subclass.

The strongest Veteran is:

> **the Fighter who has procedures for situations other people improvise through, arrives with an immediate plan, carries a credible backup method, and keeps one reserve for when experience says the first plan will not survive contact.**

That direction preserves the project’s best work while giving it one understandable gameplay identity.
