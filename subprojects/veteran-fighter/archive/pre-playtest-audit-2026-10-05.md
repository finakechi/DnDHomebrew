# Veteran Fighter — Final Pre-Playtest Polishing Audit

**Rules:** D&D 2024 / revised fifth edition • **Audit date:** October 5, 2026  
**Authority:** Veteran_Fighter_Comprehensive_Current_State_Report_2026-10-05.md, read completely: all 1,350 lines.  
**Deliverable:** Recommendations, quantitative analysis, and a complete proposed public testing build. Recommendations here do not retroactively change project canon.

## A. Executive verdict

**The architecture is ready for public playtesting after a bounded integration and wording pass. The source report itself is not yet a table-ready release.** Preserve Practical Fighting, Battlefield Readiness, Been Here Before, the level-15 chassis integration, and the level-18 capstone. Their total contribution is defensible enough to test against official Fighters; the analysis does not establish exact parity or final balance.

The Veteran is a strong subclass. Its early melee engine outperforms a resource-empty Champion in ordinary damage, but resource-normalized Battle Master and Psi Warrior comparisons substantially narrow that gap. At level 11, the controlled four-round encounter model gives Veteran **44.25**, Battle Master **44.52**, and Psi Warrior **45.35** average personal damage per round. These figures include Action Surge, use matching weapons and accuracy, and are not optimized ceilings. The capstone pushes the Veteran toward the upper end of the single-enemy envelope while providing significant defense. That is the most important high-level watchpoint, not a demonstrated exploit.

Highest-priority changes:

1. Explicitly allow Strength or Dexterity for **both** Practical Contact attack rolls and damage. The source changes damage only, leaving a Dexterity Veteran's unarmed attack accuracy dependent on Strength.
2. Give Practical Fighting **one shared use per Attack action**; identify generated attacks as part of that action; exclude restricted one-attack actions from producing additional attacks.
3. Close Field-Expedient Tool's scope: weapon-assisted physical procedures, not every action involving a nonmagical item. Preserve physically feasible Sabotage/Barricade synergy without ranged lockpicking, crafting acceleration, consumable delivery damage, or magic activation.
4. Define Reserve Lesson duration, declarations, conditional benefits, and temporary tool proficiency. Prevent rest-swapping from permanently accumulating tool proficiencies.
5. Clarify Hair Trigger's attack count as the Fighter's Extra Attack count; it does not copy Practical Fighting or Light-property attacks onto somebody else's turn.
6. Resolve the four utility procedures with explicit ranges, target boundaries, and attack-slot restrictions.
7. Merge Two-Man Takedown into Fire-Team Assist as an alternative Help mode; merge Deliver an Object and Misdirect with Sound into **Battlefield Improvisation**. This reduces 22 selections to **20** while preserving every accepted procedure.
8. Bound Find the Weak Point's shared once-per-turn benefit, evidence requirement, and concurrent subjects. Do not allow multiple studies to create an uncapped bank of independent Advantage effects.
9. Rename the level-15 package **Still in the Fight**. Preserve its mechanics.
10. Publish with controlled comparisons and explicit monitoring of Grappler, off-turn attacks, ranged riders, initiative preparation, and dominant Lesson selections.

**No experimental Lesson is promoted. No damage nerf, resource pool, extra Reaction, or redesign of a stable feature is recommended.** Some integration fixes below are mechanical; they are identified in the change log rather than disguised as editorial changes.

### Evidence labels

- **Project decision:** directly recorded in the authoritative report.
- **Rules fact:** supported by official text or a licensed reproduction of that text.
- **Research finding:** external design or optimization methodology, not rules authority.
- **Model assumption:** a declared input or policy in this audit's calculations.
- **Recommendation:** this audit's proposed wording or mechanical choice.
- **Playtest hypothesis:** plausible table behavior not established by these models.

## B. Source and rules verification

### Primary rules sources and access limits

The official D&D Beyond Basic Rules provided the Fighter chassis, Champion, equipment, and glossary. The direct PHB class URL redirected to a marketplace page; it was not usable as full paid-book access. For Battle Master, Eldritch Knight, Psi Warrior, and several feats, this audit used **Roll20's licensed Player's Handbook (2024) compendium text**, not fan-wiki transcriptions. Some pages display a purchase banner while exposing rules text; the retrieved text was inspected. [R1–R9]

The official April 2025 PHB errata corrects Grappler's movement language, explicitly identifies Shield donning/doffing as Utilize, adds voluntary grapple release, and clarifies Invisible while hidden. These corrections matter directly to this subclass. The current official changelog and targeted searches were checked; no later relevant correction was found in that check. This is not a claim that every possible rules update was exhaustively excluded. [R10–R11]

### Verified Fighter chassis

Action Surge grants another action except Magic; at Fighter 17 there are two uses between rests, still only one per turn. Second Wind heals 1d10 plus Fighter level; a Short Rest restores one use. Tactical Mind modifies a failed check and preserves the resource if it still fails. Tactical Shift normally follows Bonus Action Second Wind. Extra Attack supplies 2/3/4 attacks at Fighter 5/11/20. Tactical Master substitutes Push, Sap, or Slow; Studied Attacks grants the next attack against a missed target Advantage within its duration. Indomitable rerolls a failed save with a Fighter-level bonus. [R1–R2]

### Rules boundaries that determine this rewrite

| Topic | Verified rule / consequence | Veteran treatment |
|---|---|---|
| Unarmed Strike | Damage uses an attack roll; Grapple/Shove use the target's chosen Strength or Dexterity save | Dexterity attack-and-damage exception only; normal grapple DC and anatomy remain |
| Attack replacements | A feature can expressly replace an attack; that does not confer unrestricted action substitution | Each procedure defines its own target and effect |
| Weapon handling | The Attack action's equip/unequip permission accompanies an actual attack | A replaced procedure does not automatically provide that weapon permission |
| Help | Check assistance requires the helper's relevant skill/tool proficiency | Veteran's Correction must begin with legal Help |
| Ready | A perceivable trigger precedes the Reaction; normal Extra Attack is on-turn | Hair Trigger expressly extends the Fighter attack count |
| Haste | The extra Attack action is restricted to one attack | No second Practical Fighting attack; movement is not a separate third attack |
| Influence | Willingness and attitude are different determinations | Bloodied demands can permit a check; Hostile Disadvantage remains |
| Reach | Reach extends attacks with that weapon, not all procedures performed nearby | Break Their Hold explicitly borrows a held melee weapon's reach |
| Magic items | Activation requirements and action types remain binding | Neither Field-Expedient Tool nor Action Surge enables unauthorized Magic actions |

Sources: Unarmed Strike/Help/Ready and glossary [R3, R12]; equipment [R4]; Haste [R13]; licensed feats and subclass text [R5–R9, R14–R22].

**Important interpretation:** the final build's explicit Haste and utility-slot restrictions are homebrew boundary choices, not an official ruling that all attack-replacement features interact identically with Haste. The source report leaves these questions open; this build settles them conservatively and visibly.

### Research methodology sources

Tabletop Builds explains outcome-weighted expected value and probability handling. RPGBOT's familiar 65% / level-AC progression derives from older DMG monster-creation expectations; it is useful as a comparative baseline, not verified average AC for the 2025 Monster Manual or an official universal success target. LudicSavant/AureusFulgens's calculator tradition sweeps AC rather than treating one AC as definitive. The Proving Grounds separates ordinary, opening, nova, and adventuring-day damage under a three-combat/four-round convention. [M1–M4]

The latter calculator uses simplifying assumptions, including fractional Vex uptime and prescribed Reaction frequency. This audit **does not copy those shortcuts into exact sequencing**. Its published assumptions are evidence for a distinct day-normalization approach. Community sources disagree because of accuracy, builds, kill frequency, target multiplicity, setup, and rests—not because one DPR formula alone defines balance.

Crawford's design discussion supports comparing a subclass as a whole and writing toward common table questions without burying the main procedure under corner cases. It is design guidance, not a mathematical power budget. [M5]

## C. Current architecture assessment

| Feature | Assessment | Decision |
|---|---|---|
| Hard-Won Lessons | Strong modular spine; choice count is manageable, catalogue requires organization | Keep 4/5/6/7/8; trim two selection slots by mergers |
| Practical Experience | One proficiency and one Expertise supply reliable mundane utility | Keep |
| Practical Contact | Implement narration is distinctive; missing Dexterity accuracy is a concrete defect | Explicit matched attack/damage modifier |
| Close Work | Guaranteed extra attempt; damage is often the default, control creates situational choices | Keep; test Grappler and melee positioning |
| Hit or Correct | Accuracy-dependent focus damage plus generous split-fire/movement | Keep; preserve the hit/miss target distinction |
| Battlefield Readiness | Preparation arrives without consuming an entire turn | Keep two choices and existing resolution timing |
| Been Here Before | Three preparation timescales; much cleaner than universal recall | Keep; define reserved-use scope |
| Level 15 | Additional preparation, healing compression, and better Brace make a coherent endurance payoff | Keep; name Still in the Fight |
| Veteran of a Hundred Fights | Powerful single-threat culmination; defense matters at least as much as DPR | Keep full duration and off-turn benefits; priority playtest |

### Official feature envelope by level and function

| Fighter level | Champion | Battle Master | Eldritch Knight | Psi Warrior | Veteran comparison |
|---|---|---|---|---|---|
| 3 | Expanded criticals; athletic/initiative benefits | Dice, maneuvers, skill/tool | Spellcasting; War Bond | Strike, protection, movement powers | Stronger repeatable contact; mundane fieldcraft |
| 7 | Additional style | More maneuvers/dice; Know Your Enemy | War Magic | Leap; Thrust | Opening preparation; mobility/reaction Lessons |
| 10 | Heroic Warrior | d10 dice | Eldritch Strike | Guarded Mind | Adaptability and reserves, little direct damage growth |
| 15 | Wider critical range | Relentless | Arcane Charge | Bulwark of Force | Healing/BA compression and later preparation |
| 18 | Survivor | d12 dice | Improved War Magic | Telekinetic Master | Repeatable single-threat offense and defense |

Official feature progression: [R5–R8]. The following are **comparative judgments**, not official ratings.

| Function | Veteran's position in the official envelope |
|---|---|
| Sustained offense | Above an empty-resource baseline early; Champion's Inspiration narrows the later gap. The capstone is a material increase rather than cosmetic scaling. |
| Burst offense | Surge multiplies its repeatable engine. BM/Psi resource spending competes in short encounters; EK's area effects require a target-count model. |
| Defense | Before18, many Lesson defenses cost an Action. That is a larger cost than applying protection through a Reaction or spell while retaining an attack turn. At18, marking changes the comparison substantially. |
| Control | Contact competes with damage; utility replaces attacks. BM often retains hit damage while adding control. Veteran's repeatability is its compensation. |
| Movement | Mundane geometry and ordinary Speed govern Veteran movement. It cannot replace flight or teleportation when a barrier makes walking impossible. |
| Action compression | Readiness, utility slots, and Dig Deep are the defining advantage. EK shows that bounded attack substitution itself is inside official design practice. |
| Exploration/social | Expertise and selected Lessons support repeated practical tasks. Spell-based solutions remain broader; Veteran need not reproduce them. |
| Adaptability | Rest swaps/reserves supply contingency rather than simultaneous access to every Lesson. More preparation flexibility does not imply more actions. |
| Resource dependence | PF is repeatable; Second Wind, Surge, group concealment, and reserves still require budgeting. Scarce rests favor it over predominantly spent-dice damage policies. |
| Build flexibility | No Intelligence requirement helps ordinary weapon builds; melee contact still requires proximity, ranged correction requires appropriate targets, and grapples require hands. |

The architecture clears a defensible **testing** threshold because its advantages have identifiable costs and official comparators have substantial omitted defense/control. This is not proof that all of those contributions cancel numerically. The capstone and dip routines still require live evidence.

### Level-by-level play experience

| Fighter level | Actual decisions and experience | Main risk |
|---|---|---|
| 3 | Four Lessons; choose contact damage/control or ranged correction; full-action utility competes with the entire weapon attack | Early melee output and sheer catalogue onboarding |
| 5 | Two ordinary attacks let a physical procedure coexist with a triggering weapon attack; Tactical Shift helps withdrawal | Efficient attack-replacement combinations |
| 7 | Choose opening preparation; fifth Lesson unlocks Ready/OA specializations | Hair Trigger assumed to include every generated attack |
| 10 | Sixth Lesson, two contingencies, one rest swap; meaningful siege/social/item roles | Most administrative onboarding occurs here |
| 11 | Third weapon attack improves ordinary offense and makes one-attack procedures relatively cheaper | Full-action utility now costs much more damage |
| 13 | Studied Attacks turns misses into sequencing information | Extra roll bookkeeping; redundant Advantage |
| 15 | Use later unused Readiness; heal/shift with Surge; preserve Bonus Action | Feature feels quiet in easy fights with no attrition |
| 17 | Two Surge/Dig Deep moments across different turns | Mistaken double-Surge turn; Second Wind budgeting |
| 18 | Choose dangerous visible opponent each turn; off-turn threat coverage matters | Boss suppression and high defensive uptime |
| 20 | Four normal attacks, one Practical Fighting use per action | Fast-turn procedures worth much more relative to full actions |

A melee Veteran remains an attacking Fighter with occasional rescue/control procedures. A ranged Veteran gets less reliable focus damage but stronger safe repositioning and split-fire. Strength has the better default Grapple/Shove DC. Dexterity has viable contact damage after the attack-roll fix, stealth, and ranged accuracy. Expertise and selected fieldcraft remain useful outside combat.

Level 10 is the administrative peak. Use a player sheet with **known Lessons**, **two reserves**, and **one reserve-use checkbox**; the player needs their selected entries, not all 20 entries, at the table.

## D. Mathematical balance report

### D1. Common assumptions and limits

Numbers are this audit's calculations, not quoted optimization rankings. Unless a table says otherwise: one durable target; no damage resistance; sufficient positioning and ammunition; no party buffs; 5% natural critical chance; no kill-trigger credit; no magic items; primary modifier +3 at 3, +4 at 5, +5 at 7 onward. The latter assumes the Fighter's level-6 ability improvement, not a universal progression. Archery adds 10 percentage points where specified. No attack is credited to an unavailable Bonus Action or Reaction.

The clean official-subclass isolation uses **Defense style, greatsword, Graze, no damage feats**. This is deliberately separate from the feat-enabled build table. It reveals subclass contribution without hiding assumptions inside optimized weapon switching.

The models do not simulate a complete tactical map, target HP/overkill, initiative distributions, conditions on the Veteran, monster choices, or every magic item. Full encounter simulations would need those inputs. This report uses controlled scenarios for those effects and does not claim to establish total encounter win rate.

### D2. Fixed-hit-rate expected value

Let p include critical hits, c be critical probability, d be the mean of damage dice, m flat damage, and g miss damage:

**E = p(d + m) + c·d + (1 − p)g.**

Advantage: pA = 1 − (1 − p)²; cA = 1 − (1 − c)². Disadvantage: pD = p²; cD = c². If both apply, use ordinary p and c. Dice alone double on ordinary critical hits; flat modifiers do not.

Example: at p=.65, an unarmed 1d6+5 averages **.65×8.5 + .05×3.5 = 5.70**. Three greatsword/Graze attacks average **3×[.65×12 + .05×7 + .35×5] = 29.70**; adding contact damage yields **35.40**. This is a level-11 clean damage turn, not a nova.

| Ordinary hit chance | Chassis GS | Veteran GS | Champion crit only | Veteran bow, focus | Veteran bow, two targets |
| --- | --- | --- | --- | --- | --- |
| 50% | 26.55 | 30.98 | 27.60 | 17.09 | 17.40 |
| 60% | 28.65 | 33.93 | 29.70 | 20.07 | 20.70 |
| 65% | 29.70 | 35.40 | 30.75 | 21.48 | 22.35 |
| 70% | 30.75 | 36.88 | 31.80 | 22.84 | 24.00 |
| 80% | 32.85 | 39.83 | 33.90 | 25.34 | 27.30 |

Champion's column here isolates expanded critical range; it **excludes Heroic Warrior**, so it must not be treated as the complete level-11 Champion. D5 includes the reroll. The bow columns use equal stated p without Archery/GWM. Multi-target damage includes a valid secondary target and is total damage, not focused boss damage.

Single-target Hit or Correct triggers its damage follow-up on a miss. With n ordinary attacks and no stateful Advantage, its expected added damage is:

**[1 − pⁿ] × [p·d + c·d]**, assuming it is used on the first miss. At level 11/p=.65 with a longbow, that is **2.28**, compared with **3.15** against two suitable targets. Its safe movement remains available following a hit even if no different valid target exists; the testing text makes the follow-up optional.

This model understates powerful on-hit riders and misses the defensive importance of movement. It also demonstrates why lower accuracy increases the frequency of single-target correction without making lower accuracy desirable overall.

### D3. Representative AC and attack-bonus model

Two scenario sets are useful: the older CR-derived progression (13/15/17/18/19 at representative levels), and an AC sweep around it. These are declared scenarios, not measured contemporary monster averages. [M2–M3]

| Level | Scenario AC | Melee attack | Melee p | Archery p | Chassis GS | Veteran GS |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | 13 | +5 | 65% | 75% | 7.90 | 12.30 |
| 5 | 15 | +7 | 65% | 75% | 17.80 | 22.85 |
| 7 | 16 | +8 | 65% | 75% | 19.80 | 25.50 |
| 10 | 17 | +9 | 65% | 75% | 19.80 | 25.50 |
| 11 | 17 | +9 | 65% | 75% | 29.70 | 35.40 |
| 13 | 18 | +10 | 65% | 75% | 30.89 | 37.21 |
| 15 | 18 | +10 | 65% | 75% | 30.89 | 37.21 |
| 17 | 19 | +11 | 65% | 75% | 30.89 | 37.21 |
| 18 | 19 | +11 | 65% | 75% | 30.89 | 43.28 |
| 20 | 19 | +11 | 65% | 75% | 41.35 | 55.10 |

At level 11, a +9 melee attack faces AC 14/17/20/23 at 80%/65%/50%/35%. A +11 Archery attack faces the same ACs at 90%/75%/60%/45%. Equal-hit-rate tables deliberately remove this build advantage; real-build comparisons restore it.

| AC at11 | Melee p | Chassis GS | Veteran GS | Veteran GWM/Archery bow focus |
| --- | --- | --- | --- | --- |
| 14 | 80% | 32.85 | 39.83 | 39.26 |
| 17 | 65% | 29.70 | 35.40 | 34.87 |
| 20 | 50% | 26.55 | 30.98 | 29.15 |
| 23 | 35% | 23.40 | 26.55 | 22.58 |

**Conclusion:** the contact attack is a relatively stable incremental contribution; Graze prevents the greatsword baseline from collapsing at high AC. The ranged correction bonus is contingent rather than a full additional focus attack every round. Weapon bonuses alter both accuracy and damage and must be included separately.

### D4. Exact probabilities and stateful sequences

The scripts propagate the probability of the next-attack Advantage entitlement after every attack. Studied Attacks and Vex are not assigned arbitrary uptime.

For repeated same-target attacks with Studied Attacks alone, if q is the probability that an attack begins with Advantage:

**q(next) = (1−q)(1−p) + q(1−pA).** Its stationary value is **q=(1−p)/(1+p−p²)**. At p=.65, q=.285132 and stationary hit probability=.714868. A short sequence starting without Advantage is different from this stationary limit.

Vex alone sets the next entitlement after a hit; Studied Attacks sets it after a miss. When every roll uses a Vex weapon at Fighter 13+, either result sets up the next attack against the same creature. **The first attack still needs a prior entitlement**; an unarmed attack lacks Vex and can interrupt the chain on a hit. The Veteran's bonus contact damage therefore need not add its full isolated EV to a Vex build's total.

At level 11, repeated rapier/Vex + Dueling attacks average **30.24** for the chassis and **34.64** with immediate Close Work. Inserting unarmed contact into the chain adds about **4.40**, less than its isolated 5.70. Delaying contact until the last weapon attack can improve some sequences; these numbers evaluate the stated immediate-contact policy, not an optimizer's global maximum.

**Topple:** chance of obtaining Prone on one ordinary attack is p×save-failure probability. With p=.65 and a .50 Constitution-save failure assumption, it is .325. For a d8+5 weapon, no other Advantage, and Prone persisting for the rest of the turn, exact expected damage for 2/3/4 attacks is **13.57 / 21.26 / 29.31**; probability of at least one successful Topple is **54.44% / 69.25% / 79.24%**. Damage becomes less favorable to distant ranged allies when Prone imposes Disadvantage. A monster that stands before the next Fighter turn resets this scenario.

**Push/Sap/Slow:** Push's positional outcome, Sap's next-attack penalty, and Slow's movement denial are evaluated conditionally on a hit. They are not assigned invented flat DPR. Slow from multiple Slow hits does not multiply its reduction. Parting Blow's separate 10-foot penalty can coexist with Slow; repeated copies of Parting Blow do not stack themselves. Cleave and Nick retain their once-per-turn limits. [R4]

### D5. Official subclass comparisons under matching assumptions

| Level | Chassis | Veteran | Champion incl HI | EK matched INT |
| --- | --- | --- | --- | --- |
| 3 | 7.90 | 12.30 | 8.25 | 7.90 |
| 5 | 17.80 | 22.85 | 18.50 | 17.80 |
| 7 | 19.80 | 25.50 | 20.50 | 22.25 |
| 10 | 19.80 | 25.50 | 23.53 | 22.25 |
| 11 | 29.70 | 35.40 | 34.56 | 34.60 |
| 13 | 30.89 | 37.21 | 35.22 | 36.47 |
| 15 | 30.89 | 37.21 | 36.60 | 36.47 |
| 17 | 30.89 | 37.21 | 36.60 | 39.25 |
| 18 | 30.89 | 43.28 | 36.60 | 39.25 |
| 20 | 41.35 | 55.10 | 48.27 | 49.71 |

This table starts each sampled turn without carried Advantage, except the Veteran's active level-18 capstone. It includes within-turn Studied Attacks. Champion uses expanded criticals and, from 10 onward, spends Heroic Inspiration on its **first miss**, rerolling one die, not two; it is a simple policy, not guaranteed optimal expenditure. The second Fighting Style can add defense or modest offense depending on build; that value is not smuggled into damage. [R5]

EK uses War Magic/True Strike from 7, with **Intelligence equal to the weapon ability** for the replaced attack. That is a declared favorable ability allocation, not something a normal STR/INT Fighter automatically achieves. It excludes spell slots, concentration offense, Shield, and encounter control. At 18, Improved War Magic can produce a qualitatively different spell-and-attack turn. [R7, R23]

**Ability sensitivity:** at level11, keeping Intelligence +3 while Strength is +5 lowers the True Strike attack to p=.55 in this fixed-AC comparison. Its 4d6+3 with Graze averages 11.40, replacing a 9.90 ordinary weapon attack: the full turn becomes **31.20**, rather than 34.60 with matched Intelligence. At7, the same allocation makes the True Strike attack average 9.30, so ordinary attacks are the better damage choice in this scenario. This is why the favorable matched-ability column is a sensitivity bound, not a normal point-buy prescription. Spell defense/utility can still justify the subclass without maximum Intelligence.

Battle Master and Psi Warrior require a resource environment, so they are not represented by a resource-empty line masquerading as full subclass strength:

| Level | Veteran | Champion incl HI | Battle Master | EK matched INT | Psi Warrior INT+3 |
| --- | --- | --- | --- | --- | --- |
| 3 | 15.38 | 10.31 | 13.67 | 9.88 | 14.47 |
| 5 | 28.56 | 23.13 | 27.06 | 22.25 | 29.03 |
| 7 | 31.88 | 25.63 | 30.65 | 27.81 | 31.53 |
| 10 | 31.88 | 28.98 | 31.97 | 27.81 | 31.53 |
| 11 | 44.25 | 42.51 | 44.52 | 43.25 | 45.35 |
| 13 | 46.95 | 43.81 | 46.56 | 45.91 | 47.54 |
| 15 | 46.95 | 45.55 | 52.54 | 45.91 | 47.54 |
| 17 | 56.36 | 54.26 | 60.76 | 59.21 | 56.39 |
| 18 | 64.91 | 54.26 | 62.39 | 59.21 | 56.39 |
| 20 | 82.65 | 71.53 | 78.11 | 74.89 | 72.08 |

Champion applies one first-miss Inspiration reroll per turn from10, not one per Attack action; EK uses one matched-INT True Strike per eligible Attack action. Both carry Studied entitlement across turns and exclude other spell/defensive benefits.

This is exact branch enumeration for a **four-round fresh encounter with resources available**, Defense/greatsword/Graze, no feats, and Action Surge early (two separate Surge turns from Fighter 17). Veteran carries Studied Attacks between turns. BM spends damage-adding dice on early hits, with doubled attack dice on criticals; from 15 it uses the free d8 on the first hit each turn, then paid dice on other hits. Psi uses one Psionic Strike on its first weapon hit each turn, Intelligence +3, target within 30 feet, and does not double that separate post-hit damage on a critical. [R6, R8]

These policies **exclude** BM Precision Attack, Riposte, Trip's later-attack Advantage, free off-turn Relentless, and allied attack generation. They exclude Psi's protective reductions, thrust, flight, and Telekinesis. BM can outperform the listed policy by spending dice on control or near misses; Psi can choose defense instead of damage. The Veteran also has utility/control outside this damage policy. None of those exclusions makes the compared total feature envelopes identical.

**Precision Attack sensitivity:** spending a d8 after missing by k succeeds with probability (9−k)/8 for k=1…8, subject to the natural-1 rule. A near miss by 1, followed by successful Precision, restores the full attack's hit damage; a miss by 8 has only a 1/8 rescue chance. That makes “one die equals 4.5 damage” an inadequate general BM valuation. This is especially important with GWM and magic riders. [R6]

### D6. Sustained, nova, and multi-encounter normalization

| Level | No Surge, four-turn avg | One Surge-turn nova | 3-round avg | 4-round avg | 5-round avg |
| --- | --- | --- | --- | --- | --- |
| 3 | 12.30 | 24.60 | 16.40 | 15.38 | 14.76 |
| 5 | 22.85 | 45.70 | 30.47 | 28.56 | 27.42 |
| 11 | 35.40 | 70.80 | 47.20 | 44.25 | 42.48 |
| 15 | 37.54 | 74.86 | 50.05 | 46.95 | 45.09 |
| 18 | 43.28 | 86.55 | 72.13 | 64.91 | 60.59 |
| 20 | 55.10 | 110.20 | 91.83 | 82.65 | 77.14 |

This table uses the same clean greatsword/Defense build; finite turns carry Studied Attacks. Nova means **one Surge turn**, not both level-17 charges on the same turn. Encounter averages include one Surge below 17 and up to two above it. Second Wind/Dig Deep healing is excluded from damage, but described in E.

| Level | Short Rests | Veteran | Battle Master | Psi Warrior |
| --- | --- | --- | --- | --- |
| 3 | 0 | 13.33 | 10.17 | 10.72 |
| 3 | 1 | 14.35 | 12.07 | 11.92 |
| 3 | 2 | 15.38 | 13.67 | 13.10 |
| 5 | 0 | 24.75 | 20.90 | 23.03 |
| 5 | 1 | 26.66 | 23.98 | 25.14 |
| 5 | 2 | 28.56 | 27.06 | 27.25 |
| 11 | 0 | 38.35 | 34.64 | 37.84 |
| 11 | 1 | 41.30 | 39.58 | 41.02 |
| 11 | 2 | 44.25 | 44.52 | 44.20 |
| 15 | 0 | 40.67 | 41.73 | 40.93 |
| 15 | 1 | 43.81 | 47.20 | 44.25 |
| 15 | 2 | 46.95 | 52.54 | 47.54 |
| 18 | 0 | 50.49 | 44.90 | 45.92 |
| 18 | 1 | 57.70 | 53.65 | 51.16 |
| 18 | 2 | 64.91 | 62.39 | 56.39 |
| 20 | 0 | 64.28 | 57.10 | 58.15 |
| 20 | 1 | 73.47 | 67.61 | 65.11 |
| 20 | 2 | 82.65 | 78.11 | 72.08 |

Three encounters use new targets, with carried attack entitlement reset at encounter start. One Short Rest occurs after encounter one; two occur after encounters one and two. Surges are spent as early as available on different turns. This is a deliberately explicit schedule, not a universal adventuring day. More rests support BM much more than they support a repeatable Veteran engine; Psi restores only one expended die per Short Rest. [R6, R8]

The Veteran's advantage over a resource-empty comparison grows when rests are scarce. It narrows in short, well-rested encounters. Its level-18 always-available package remains important across environments.

### D7. Feat- and build-sensitive models

| Level | Build | Chassis | Veteran total | Veteran focus | Method |
| --- | --- | --- | --- | --- | --- |
| 11 | Great weapon | 37.50 | 43.20 | 43.20 | exact stated policy |
| 11 | Sword shield | 23.10 | 28.80 | 28.80 | exact stated policy |
| 11 | Polearm | 41.10 | 46.80 | 46.80 | exact stated policy |
| 11 | Dual wield | 35.05 | 40.28 | 40.28 | exact stated policy |
| 11 | Dex melee | 30.24 | 34.64 | 34.64 | exact stated policy |
| 11 | Longbow | 31.05 | 37.65 | 34.87 | exact stated policy |
| 11 | Heavy crossbow | 33.45 | 40.85 | 37.73 | exact stated policy |
| 11 | Thrown | 34.58 | 38.33 | not modelled | approx. |
| 11 | Mixed unarmed | 19.20 | 24.90 | 24.90 | exact stated policy |
| 20 | Great weapon | 58.95 | 76.16 | 76.16 | exact stated policy |
| 20 | Sword shield | 34.03 | 49.92 | 49.92 | exact stated policy |
| 20 | Polearm | 61.23 | 77.75 | 77.75 | exact stated policy |
| 20 | Dual wield | 44.96 | 54.60 | 54.60 | exact stated policy |
| 20 | Dex melee | 42.12 | 49.92 | 49.92 | exact stated policy |
| 20 | Longbow | 50.03 | 68.48 | 62.22 | exact stated policy |
| 20 | Heavy crossbow | 53.43 | 73.47 | 66.60 | exact stated policy |
| 20 | Thrown | 46.34 | 51.33 | not modelled | approx. |
| 20 | Mixed unarmed | 28.31 | 42.90 | 42.90 | exact stated policy |

Build definitions:

| Build | Weapon / style / feat assumptions | Boundary |
|---|---|---|
| Great weapon | Greatsword Graze, Defense, GWM at 4; primary 20 at 6 | No kills, Hew not in base table |
| Sword/shield | Longsword Sap, Dueling; Shield Master as a control scenario | Free contact Shove and Shield Bash can be redundant |
| Polearm | Glaive Graze, Defense, PAM4/GWM6; Strength20 at8 | Contact needs 5 feet despite glaive reach; table assumes it |
| Dual wield | Shortsword Vex + scimitar Nick, TWF, Dual Wielder4 | Nick once per turn; BA cannot also heal/smite/etc. |
| Dex melee | Rapier Vex, Dueling, primary Dexterity | Uses recommended Dex contact accuracy; no Dex grapple DC |
| Longbow | Slow, Archery, GWM4 with Strength 13; Dexterity20 at8 | Stat investment is real; no +10 legacy Sharpshooter |
| Heavy crossbow | Push, Archery, XBE4/GWM6, Dex20 at 8 | Before XBE, Loading prevents the extra shot |
| Thrown | Handaxe Vex, dagger Nick, Thrown style, Dual Wielder4 | Extra Light attacks lack ability without TWF; no Archery for thrown melee weapons |
| Mixed/unarmed | Warhammer Push + free hand, Defense | Damage table excludes Grappler's control/Advantage; scenario below adds it |

Sources for feat/style interaction: GWM [R14], Dual Wielder [R15], PAM [R16], XBE [R17], TWF [R24], Archery/Thrown [R25–R26].

Melee columns use an exact repeated-turn boundary. Longbow/crossbow use exact **fresh-turn** correction-or-split sequencing and do not carry previous-turn Studied Advantage into the opening attack. Thrown uses an isolated follow-up against an unmarked secondary target at ordinary accuracy as an approximation because Vex target switching and the Light attack schedule interact; it is explicitly not an exact optimized total. At level 20, a split follow-up against an unmarked enemy does not inherit capstone Advantage. These distinctions are retained in the calculation output.

**Hew:** not assumed always available. At level 11, three ordinary weapon rolls have a 14.26% chance of at least one critical (before other Advantage). A free BA greatsword/Graze attack without Attack-action GWM averages 9.90, so the rough critical-only contribution is **1.41 DPR**. The corresponding Champion critical-only frequency is 27.10%, roughly **2.78 DPR** with its expanded-crit attack EV. These estimates omit correlations from rerolls and Studied Attacks and are supplementary, not exact additions to all table rows. Kill-based Hew frequency requires actual target HP and turn order.

**Great Weapon Fighting:** the principal heavy builds take Defense, a reasonable defensive trade. The 2024 style raises each d6 mean from 3.5 to 4 and each d10 from 5.5 to 5.8. A 2d6 weapon therefore gains .70 expected damage per ordinary p=.65 attack including criticals; it does not improve an unarmed contact attack. Extra rider dice may require checking their applicable wording; do not give the unarmed strike the held weapon's style benefits. [R27]

**Grappler scenario:** p=.65 unarmed hit and .50 target save failure yield **32.5%** first-attempt Damage+Grapple success. After a triggering weapon attack, immediate Close Work can establish Advantage for subsequent weapon attacks. Two remaining d8+5 attacks would each gain 2.375 EV when the grapple succeeds, a **1.54** unconditional incremental damage benefit that turn, before escapes and other Advantage. A pure Grapple attempt instead succeeds .50 but sacrifices the 5.70 damage option. Holding a heavy two-handed weapon and maintaining a grapple prevents attacks requiring both hands; shield+weapon leaves no grappling hand. The feat is strong, not free universal Advantage. [R18]

**Tavern Brawler:** rerolling a 1 once raises a d6 mean by 2.5/6=.4167; the isolated contact gain at p=.65 is **.2917**, plus its once-per-turn push. Its d4 damage option and improvised proficiency overlap Practical Contact, so it is less efficient here than on a subclass that lacks them. [R19]

**Unarmed Fighting style:** its held-weapon d6 largely overlaps Practical Contact. Its d8 requires no held weapons or Shield at the attack roll, and its grappled-target start-of-turn damage averages 2.5 while a qualifying grapple persists. Choosing another unarmed damage option replaces the die rather than adding dice together. Test weapon stowing/drawing explicitly if a player pursues the d8; do not assume shield builds qualify. [R34]

### D8. Opportunity cost and party contribution

| Level | One GS/GWM attack | One sword/Dueling attack | One bow/GWM/Archery attack | Whole Veteran GS action | Relative slot cost |
| --- | --- | --- | --- | --- | --- |
| 5 | 10.85 | 7.05 | 8.10 | 26.75 | 1/2 ordinary attacks |
| 11 | 12.50 | 7.70 | 10.35 | 43.20 | 1/3 ordinary attacks |
| 20 | 17.09 | 10.53 | 14.97 | 76.16 | 1/4 ordinary attacks |

The attack-cost scenarios use ordinary p=.65, Archery p=.75, and marked-target Advantage at20. Level5 bow damage uses Dexterity +3 after its Strength-increasing GWM choice. These are standardized accuracy costs, not a second claim about the bow’s actual level5 AC matchup.

One replacement loses one **eligible normal attack**, not automatically the whole Attack action. Relative ordinary-attack fractions are 1/2, 1/3, and 1/4 at 5/11/20. Absolute lost attack EV can grow with GWM, accuracy, and magic. If the Veteran replaces its last remaining triggering weapon attack, it can also lose Practical Fighting: at level 3 that is a significant hidden cost. On-turn utility followed by a retained weapon attack preserves it from level 5.

Full-action Help, Search, Study, Dodge, Dash, Hide, Influence, or Utilize generally forgoes the entire normal attack sequence and Practical Fighting. Battlefield Readiness can remove that cost for Search/Study; Action Surge pays a limited resource instead. Sabotage and Battlefield Activation return a BA attack if the BA is available.

| Lesson / situation | Quantitative or scenario evaluation |
|---|---|
| Fire-Team Assist: one ordinary allied d8+5 attack | Advantage gain = .2275×9.5 + .0475×4.5 = **2.38**; poor pure-DPR substitute for a high-level Fighter turn |
| Fire-Team Assist: up to three identical allied attempts, benefit ends on hit | Chance at least one hit improves .957125→.998162; expected total damage gain about **2.70**, not three times 2.38 |
| Assist a Rogue with otherwise unavailable Sneak Attack | Can enable a much larger packet; evaluate whether Help truly changes eligibility and existing Advantage, rather than crediting Sneak Attack twice |
| Two-Man Takedown mode | If ordinary save failure probability is f, Disadvantage raises failure to 1−(1−f)². At f=.50: **50%→75%**; at f=.40: **40%→64%** |
| Veteran's Correction | Check shortfall k=1…10 is rescued with probability (11−k)/10; still-failed attempts spend no Second Wind. Cost is lost healing/shift opportunity on successes |
| Threat Scan | At p=.65, one enemy d8+5 attack loses about **2.38** EV from Disadvantage; the allied first-attack gain is also 2.38 if neither already has modifiers. Discovering an ambusher matters beyond this sum |
| Find the Weak Point | Shared one qualifying roll per turn can improve several different party turns. Four suitable attacks can gain about **9.5** per round in the simple d8+5 example, conditional on successful Study and usable weakness |
| Common Soldier's Tongue | A surrender can end several remaining enemy turns; no defensible universal damage equivalent. At DC15/+5, ordinary success=.55; Hostile Disadvantage=.3025 |
| Quick Barricade / Shield the Line | +2 AC reduces ordinary attack hit chance by .10 away from boundaries: about 1.5 damage avoided per incoming 15-damage attack. Coverage, duration, angles, and Dexterity saves determine value |
| Break Their Hold | .50 release chance can save an ally's Action or concentration situation; disarming only matters if pickup, backup weapons, and monster attacks are tracked |
| Casualty Extraction | Carry a wounded ally 30 feet instead of 15 in the stated movement-cost scenario; may save healing actions or prevent finishing attacks |
| Battlefield Improvisation | Deliver the needed key/potion before an ally's turn; or disrupt an enemy Search. Recipient Reaction and attack sacrificed are real costs |

The Fire-Team multi-attempt figure includes critical dice and assumes identical attacks, no external Advantage, and no other movement value. Recompute with heterogeneous allies instead of treating it as a fixed Lesson valuation.

### D9. Defense, movement, and magic sensitivity

At p=.65, capstone Disadvantage reduces enemy hit chance to .4225; ordinary critical chance falls from .05 to .0025. A d8+5 enemy attack drops **6.40→4.03** expected damage. Three such attacks save about **7.13 HP per round** while the marked creature remains the attacker. Against four different enemies, marking one does not suppress all four. Against pre-existing Disadvantage, the incremental benefit is zero. Saving-throw Advantage raises success p=.40→.64, p=.60→.84, conditional on identifying the forcing creature.

**Official defensive context:** with Constitution +3, Champion Survivor can restore 8 HP at the start of a turn when its Bloodied and minimum-HP conditions apply. A level11 Psi Protective Field with Intelligence +3 averages 8.5 damage reduction per die/Reaction before the actual damage cap. Veteran’s marked-enemy reduction is repeatable but opponent-dependent; those official defenses have different activation and resource boundaries. [R5, R8]

For EK, Shield’s +5 AC can reduce hit chance by .25 away from natural-roll boundaries. Against three attacks with a 15-point ordinary hit packet, that represents about **11.25** damage avoided across a protected turn, before conditional-trigger selection and attack correlations. It spends a Reaction and spell slot; magic defenses are excluded from the offense tables. [R33]

Indomitable remains valuable: Advantage reduces failures, whereas its large reroll bonus can rescue the failure that remains. They do not stack extra dice onto one roll without limit.

Hit or Correct and Tactical Shift can each grant additional movement; neither teleports through occupied spaces, walls, or impassable terrain. Opportunity-Attack immunity does not prevent readied attacks, Reactive Strike, or other separately triggered reactions. Half Speed movement is not extra Speed and does not turn a 0-Speed creature mobile.

Magic sensitivity: a +1 weapon grants its actual accuracy/damage benefits to Hit or Correct but not an implement-flavored unarmed strike. Bracers of Archery's +2 damage survives removal of the ability modifier. A hypothetical extra 2d6 on-hit ranged rider adds **4.90 EV** to a guaranteed ordinary p=.65 follow-up; single-target correction scales by the correction availability probability. Do not assume every melee magic weapon permits thrown/ranged use of its rider. [R28–R30]

### D10. Calculation verification

Python performs exact finite branching, state propagation, and finite encounters. Wolfram Language independently returned pA=351/400=.8775, ordinary Advantage critical probability=39/400=.0975, Studied stationary entitlement=140/491=.285132, and contact EV=5.70. It also independently confirmed the correction and save-failure examples.

A seeded independent Monte Carlo check used **300,000 trials** for four greatsword attacks plus an inserted contact attack with Studied Attacks. Exact EV **47.658224**; simulated mean **47.670195**; standard error **.013349**. The difference is .90 standard errors. Dice damage was replaced by its mean in that cross-check to isolate attack-sequencing correctness; it therefore does not estimate the full damage distribution. No Monte Carlo result is presented as an exact probability.

The calculation archive includes the scripts and underlying tables. Not every tactical interaction has been simulated. In particular, the optional kill-trigger, battlefield geography, enemy willingness, and tool feasibility scenarios remain declared scenarios.

## E. Action-economy and nova audit

### Attack replacement and utility compression

The testing build permits each Attack-action Lesson **once during each Attack action on your turn**. It replaces an ordinary attack slot, not an extra Practical Fighting or Light-property attack. Different utility Lessons can replace different ordinary attacks in the same action. This preserves the “experienced physical tasks faster” thesis without letting a free unarmed strike become a free object procedure.

At Fighter 5, replacing one attack and making the other weapon attack still permits Practical Fighting. Replacing both ordinary attacks yields the procedures but no weapon-triggered Practical Fighting. At Fighter 11/20, the relative cost falls while absolute attack value may rise. Action Surge supplies another action and therefore another use of each eligible Lesson; it does not refresh once-per-turn or rest limits.

Field-Expedient Tool still performs a **specific qualifying Utilize procedure**. A known Sabotage or Quick Barricade Lesson can modify that procedure if the weapon-assisted task actually meets its requirements. It is not “all Utilize”: fine lockwork still needs the actual tools, ranged shots can only cause impact/cutting/pressure effects, and prolonged repair/crafting takes its normal time. Nonmagical status alone does not make poisoning, medical treatment, armor donning, operating vehicles for a minute, or every device button legal within one attack.

The Sabotage BA attack follows a **valid attempt**, not only success. This is a disclosed recommendation: it preserves momentum and avoids making the payoff depend on an already uncertain check. The task must be a genuine attempt to affect a mechanism's function. Deliberate Sabotage does not grant a combat BA attack after one minute. Repeated hasty attempts cannot produce more than the one Bonus Action available in a turn.

### Action Surge and Practical Fighting

Two ordinary Attack actions create two Practical Fighting applications. At Fighter 20, that is **eight normal attacks plus two contact attempts**, before an available BA/Reaction. Nick remains one Light extra attack per turn, not one per Surge action. GWM's Attack-action Heavy rider applies to each eligible weapon hit, including Hit or Correct; the no-positive-ability clause does not remove other flat bonuses. [R14, R15, R24]

For the feat-enabled greatsword build at Fighter 20/p=.65, marked-target Surge is approximately **152.32** expected damage before Hew, items, or a Reaction. This is a two-action nova, not its 76.16 ordinary-turn figure. The contact portion itself accounts for 15.60 of that nova. Remove adjacency and the unarmed attempts cease to contribute damage.

### Dig Deep and Second Wind

Dig Deep spends an actual Second Wind use and heals **20.5 at Fighter 15 / 25.5 at Fighter 20** on average, subject to missing HP. It also allows Tactical Shift and preserves the BA for PAM, Dual Wielder, Battlefield Activation, a consumable, or another feature. Its damage contribution is therefore **the available BA option recovered**, not an automatic extra attack. At level 17, two Surges on different turns can each use Dig Deep if Second Wind uses remain. No double Action Surge on one turn. [R1–R2]

Tactical Mind/Veteran's Correction compete with healing for the same Second Wind stock. A failed correction does not drain a use; a successful one does. Tactical Mind does not itself trigger Tactical Shift, because it is not Bonus Action healing, and Dig Deep is explicitly written to grant the movement.

### Ready and Hair Trigger

Hair Trigger lets the readied Attack action use **2/3/4 attacks at Fighter 7/11/20**, plus 1d10 on one hit. On another creature's turn, it normally loses on-turn Practical Fighting, on-turn GWM damage, and on-turn Light/Nick benefits. It also spends the Reaction that could defend, stop movement, or make an OA.

At level 11 with greatsword/Defense and no feats, three readied attacks, using the optional damage die on the first hit as a stated policy, average **35.37** versus **35.40** for an immediate Veteran Attack action. This readied calculation includes critical doubling of the extra die when its first successful hit is critical; it assumes the trigger occurs. It is very close offensively but pays timing/Reaction risk. With GWM, moving the action off-turn loses its Heavy rider and makes ordinary attack turns more attractive. At 18+, capstone Advantage applies to the readied attacks for its full duration. [R6, R12, R14]

A trigger can occur on the Veteran's own turn—for example after another immediate action—so the on-turn limitations are about **whose turn it is**, not whether the attack spends a Reaction. Practical Fighting can apply in that unusual on-turn readied Attack action. It remains one use for that action and does not create a third Action Surge.

Do not trigger Ready “before” a spell or movement that has not finished when the actual chosen trigger requires completion. A new Ready use does not bank extra Reactions, and it cannot pay for a Reaction already spent. This is timing sensitivity, not an infinite loop.

### Battlefield Activation and magic-item nova

Ordinary action: eligible item Magic activation. Surge action: Attack. BA: Battlefield Activation attack. Dig Deep: heal/shift while preserving that BA. At Fighter 20 that sequence contains **four normal attacks + contact + one BA attack**, not two Magic actions or a free spell.

At p=.65 with the marked-target greatsword/Defense, the attack portion is **67.00** EV: five-attack Veteran action 55.10 plus one non-GWM BA greatsword/Graze attack 11.90. The item effect is added separately. A hypothetical DC15 Fireball against three creatures with +2 Dexterity saves deals **67.2** expected total damage (28×.8×3), giving 134.2 damage across the whole sequence before healing. That is a scarce item/Surge nova and is distributed damage, not focused boss damage.

**Item legality matters:** the current Wand of Fireballs requires spellcaster attunement and cannot simply be assumed available to a pure non-spellcasting Veteran. A qualifying multiclass or other eligible character must meet the actual requirement. Its charge/upcast limit also matters. [R29] Potions often use their own action wording; do not treat every drink as Magic activation or every item as usable with this Lesson.

### Cost by action type

| Cost | What is given up | Examples |
|---|---|---|
| Action | Entire attack sequence, often PF and BA attack prerequisites | Help, Search, Study, Dodge, full Utilize |
| One ordinary attack | That attack's dice, flat bonuses, Mastery, and sometimes a triggering opportunity | Tool, Break Their Hold, Improvisation |
| Bonus Action | Second Wind, PAM/Dual Wielder attack, marks/smites, consumables or other BA feature | Activation/Sabotage returned attack still costs BA |
| Reaction | OA, Sentinel, Shield Master defense, readied action, defensive spell | Hair Trigger, Hook and Turn, recipient catching |
| No extra action | Benefit is attached to the specified procedure, not universal free permission | Readiness, Correction trigger, Practical Fighting |

## F. Hard-Won Lessons matrix

The two linked tables below form the full matrix. Every one of the **22 source concepts** is represented; merging an entry removes a selection slot, not its accepted procedure. Pick forecasts are hypotheses: **H** high in appropriate builds, **M** moderate, **N** niche/campaign-specific. Complexity is procedural complexity at use, not word count alone.

### F1. Purpose, cost, frequency, and complexity

| Source Lesson | Level | Action modified / cost | Combat purpose | Noncombat purpose | Frequency / optimization | Complexity |
|---|---:|---|---|---|---|---|
| Forced March | 3 | Dash; full action or another feature's Dash cost | Reach objectives through terrain | March/escape rough routes | Situational; movement-focused M | Low |
| Break Through | 3 | Dash; full action; saves per new enemy space | Breach occupied lane, push blockers | Emergency crowd escape | Formation fights M/H | Medium/high in crowds |
| Field Concealment | 3 | Hide; action; team benefit 1/rest | Ambush/infiltration preparation | Armored party concealment | Infiltration H, open fights N | Medium |
| Shield the Line | 3 | Dodge; action | Guard an adjacent ally | Escort in hazards | Defense niche M | Low |
| Hold Ground | 3 | Dodge; action | Resist displacement/grapple/prone | Brace at dangerous crossings | Forced-movement fights M | Medium |
| Fire-Team Assist | 3 | Help; action | Persistent-until-hit attack aid + 10-foot movement | None beyond ordinary Help | High-value allied packet M | Medium |
| Two-Man Takedown | 3 | Help; action | Impose disadvantage on one grapple/shove save | Restraining prisoners | Grapple party H, others N | Low |
| Veteran's Correction | 3 | Legal check Help; action + SW on success | Rescue crucial environmental checks | Broad assisted skill/tool reliability | Utility teams H | Medium |
| Threat Scan | 3 | Search; action, or Readiness free | Reveal threats and first-roll modifiers | Traps/tracks/violence evidence | Scouting H | Medium |
| Casualty Extraction | 3 | Disengage; action | Move wounded ally without carrying surcharge | Rescue/evacuation | Attrition/rescue H, other N | Low |
| Parting Blow | 3 | Disengage; action; attack during movement | Withdrawal attack + slow | Minimal | Mixed/ranged withdrawal M | Low |
| Field-Expedient Tool | 3 proposed | Replace one ordinary attack; once/action | Manipulate practical mechanism while fighting | Rough equipment procedures | Siege/urban H; otherwise M/N | High adjudication |
| Break Their Hold | 3 proposed | Replace one ordinary attack; once/action | Release ally or disarm | Capture/arrest | Armed foes/grapplers H | Medium |
| Misdirect with Sound | 3 proposed | Replace one ordinary attack; once/action | Penalize bounded hearing-based locating check | Concealed allies/infiltration | Prepared distraction N/M | Medium |
| Deliver an Object | 3 proposed | Replace one ordinary attack; recipient Reaction | Supply needed object at distance | Equipment handoff | Task-specific N | Low |
| Hair Trigger | 7 | Ready action + Reaction | Full Fighter volley after a trigger + d10 | Guarding an opening | Readied tactics H | Medium |
| Hook and Turn | 7 | Hit with OA; Reaction already paid | d10 + reposition provoking enemy | Minimal | Sentinel/true-OA builds H | Low |
| Common Soldier's Tongue | 10 | Influence action | Attempt bloodied enemy compliance | Practical workers/logistics talk | Social/surrender games H | High adjudication |
| Battlefield Activation | 10 | Item Magic action + optional BA attack | Preserve offense on item turns | Equipment handling | Item-rich H, item-poor trap | Low |
| Sabotage | 10 | Utilize action or eligible Tool replacement; optional BA attack | Disable/rig mundane function | Infiltration/repair knowledge/tools | Siege/urban H | High adjudication |
| Quick Barricade | 10 | Utilize action or eligible Tool replacement | Half Cover/edge movement obstacle | Fortify camps/chokepoints | Material-rich defense H | Medium |
| Find the Weak Point | 10 | Study action, or Readiness free | Shared once/turn exploitation Advantage | Structural/repair assessment | Evidence-rich fights H | High adjudication |

### F2. Overlap, pick forecast, risks, and disposition

| Lesson | Other Lesson / Fighter / official overlap | Pick | Trap / exploit risk | Status and reason |
|---|---|---|---|---|
| Forced March | Break Through; Tactical Shift; Charger Dash | M | Low; terrain frequency matters | POLISH: same effect; no merge because terrain vs bodies differs |
| Break Through | Forced March; Push; mobility feats | M/H | Multi-enemy save slowdown; self-loop through same foe | POLISH: target chooses save; first entry per creature/turn; cannot end in occupied space |
| Field Concealment | Expertise; Rogue Hide; armor stealth | H/N | Benefits must not waive Hide requirements | POLISH: voluntary team activation after legal successful Hide |
| Shield the Line | Hold Ground; Protection/Interception; Psi Bulwark | M | Full-action price; moving away removes cover | KEEP/POLISH: distinct ally protection |
| Hold Ground | Shield the Line; Indomitable; defensive feats | M | Capstone Dodge overlap against marked foe | POLISH: preserve grapple-only Speed-0 exception |
| Fire-Team Assist | Two-Man; ordinary Help; BM Distracting Strike | M | Weak pure personal-DPR use; status stacking confusion | MERGE: retain attack mode; add takedown alternative |
| Two-Man Takedown | Fire-Team; Topple; Grappler | H/N | Redundant separate slot for another combat Help mode | MERGE into Fire-Team Assist; preserve 5-foot save mode |
| Veteran's Correction | Tactical Mind; Help proficiency; skill support | H | Proficiency-free Help or healing trigger abuse | POLISH: legal Help and existing Tactical Mind cost |
| Threat Scan | Readiness; Find Weak Point; Fighter Perception | H | Searching a known visible enemy to farm modifiers | POLISH: modifier only after finding a concealed creature |
| Casualty Extraction | Parting Blow; Grappler movement benefit | H/N | Grappler overlaps; carrying capacity still applies | KEEP/POLISH: willingness/unconsciousness keeps extraction identity |
| Parting Blow | Extraction; Tactical Shift; Slow; Rogue Cunning Action | M | Rogue dip makes BA withdrawal efficient; no recursion | POLISH: one per Disengage; single nonstacking penalty |
| Field-Expedient Tool | Sabotage/Barricade; tool proficiency; Thief Utilize | H/N | Broadest action-bypass risk | ADJUST: closed physical scope; preserve eligible Lesson modifications |
| Break Their Hold | Shove/Push release; BM Disarming Attack | H | Arbitrary secured gear removal; repeated pickup denial | ADJUST/POLISH: target chooses save; held unsecured object only; explicit weapon reach |
| Misdirect with Sound | Threat Scan/Hide; illusion-like presentation | N/M | Undefined range, hearing, and duration | MERGE/POLISH into Battlefield Improvisation; real noise, bounded check penalty |
| Deliver an Object | Normal object handoff; Tool's general improvisation theme | N | Lesson-slot tax on occasional mundane task | MERGE into Battlefield Improvisation; retain precise 30-foot handoff |
| Hair Trigger | Extra Attack; Ready; capstone; BM reaction tactics | H | Copying PF/Nick off-turn; banking ready actions | POLISH: EA count only; retain one chosen-hit die |
| Hook and Turn | Sentinel; Push; PAM Reactive Strike differs | H/N | Incorrect PAM qualification | KEEP/POLISH: actual OA trigger, Large-or-smaller movement |
| Common Soldier's Tongue | Influence; Expertise; BM social maneuver | H/N | Compulsory surrender as mind control; forced free secrets | POLISH: DM evidence gate; attitude unchanged; no secret extraction |
| Battlefield Activation | Action Surge, Dig Deep; EK/item combat | H/N | Assumed illegal attunement / Magic Surge | PLAYTEST/POLISH: keep one BA attack |
| Sabotage | Tool, Barricade; Thief; practical item systems | H/N | Permanent tool harvesting; ranged complex mechanisms | ADJUST/POLISH: genuine attempt BA; proficiency while known; physical feasibility |
| Quick Barricade | Tool, Shield Line; ordinary object cover | H/N | Creating free material; indestructible cover; instant large fort | POLISH: actual material, two edges maximum, 10-minute field assessment |
| Find the Weak Point | Threat Scan; Vex/Studied; Readiness | H | Advantage saturation, many concurrent subjects, veto frequency | ADJUST/POLISH: one active subject and one shared benefit/turn; playtest usability |

### Roster verdict

**Publish 20 selectable Lessons: 13 base-access, 2 at Fighter 7, 5 at Fighter 10.** Utility procedures remain accessible at 3 because sacrificing the only ordinary attack is an adequate early cost; Extra Attack improves them naturally. Moving all to 5 would require adding an unrequested retraining feature or make them unavailable to learn until 7 under the existing learn-at-milestones progression.

The two mergers intentionally improve the value of underused procedures without expanding their individual effects. Merging combat Help modes is particularly clean because the modes already compete for the same action. Merging distraction and object delivery gives a coherent small-equipment Lesson enough breadth to justify a slot. No universal action engine is added.

Do not merge Threat Scan and Find the Weak Point: they have different ability bases, evidence, timing, and fieldcraft roles. Do not merge the two Dodge Lessons: ally shielding and personal anchoring are different builds, and using both on a Dodge is an intended investment. Likewise, Dash terrain traversal and occupied-space traversal are different.

### Illustrative known-Lesson selections

At 3, a breach fighter might choose Break Through, Hold Ground, Break Their Hold, and Field-Expedient Tool. A scout might choose Field Concealment, Threat Scan, Forced March, and Battlefield Improvisation. A protector might choose Shield the Line, Casualty Extraction, Fire-Team Assist, and Veteran's Correction. A ranged skirmisher might choose Parting Blow, Threat Scan, Battlefield Improvisation, and Break Their Hold for emergencies. These are playtest packages, not optimized mandatory prescriptions.

At 10+, siege Veterans can spend a known slot on Sabotage and Quick Barricade; item Veterans may select Activation; scouts/social Veterans can select Soldier's Tongue and Weak Point. Reserve choices should follow expected missions. A reserve that never gets used is not itself evidence that the reserved Lesson is weak.

## G. Trimming report

| Exact source area | Trim / consolidation | Why the retained length is justified |
|---|---|---|
| Practical Contact implement bullets | One sentence excludes inherited weapon/magic benefits | Prevents a +3/Flame Tongue Shield narration becoming a magic unarmed strike |
| Close Work / Hit or Correct duplicate triggers | Shared Practical Fighting introduction | Makes one use per action unmistakable |
| “Full 2024 Unarmed Strike” explanation | Use defined Unarmed Strike term | Published build targets the 2024 rules |
| Readiness design/history notes | Remove from player rules | Rules need timing and options, not discarded Sweep/Assess history |
| Brace level-15 repetition | Write base value once, improvement once | Short reminder is enough |
| Reserve philosophy paragraphs | Keep in audit, remove from rules | Rules need declaration, scope, reset, and limit clauses |
| Fire-Team/Takedown separate entries | One entry with two modes | Fewer slots and headings; same procedures |
| Deliver/Misdirect separate entries | Battlefield Improvisation with two modes | Removes low-value selection tax |
| Threat Scan long example list | Compact categories plus evidence-supported detail | Bounds DM adjudication without pretending stat extraction |
| Quick Barricade broad ribbon | 10-minute assessment under ordinary materials/checks | Gives a useful procedure without a fortification minigame |
| Find Weak Point examples and prohibited stats | Short observation gate, DM check, shared trigger | Longer shared-limit clause prevents a real stacking ambiguity |
| Source status/history/rejection lists | Keep out of player build | Essential authority context, unnecessary during play |

The recommended testing text measures approximately **3,132 words**: **989** for its core features and **2,143** for its Lesson catalogue (headings/table cells included). For planning, comparable official text is on the order of several hundred words for Champion, roughly 1,100–1,700 for Battle Master including maneuvers, and roughly 500–900 for Eldritch Knight or Psi Warrior before external spell/item descriptions. Those official ranges are editorial estimates, not exact measured counts.

Official comparisons are approximate **feature-text counts**, excluding narrative, tables/navigation, and unrelated spell descriptions. The Veteran's modular catalogue justifies being longer than Champion or Psi Warrior. Battle Master's maneuver catalogue is the relevant presentation analogue. A practical target is a core feature section under roughly 1,200 words and a player handout containing only selected Lesson text. A long catalogue is acceptable; a long mandatory turn procedure is not.

The testing build is self-contained as subclass rules, but relies on normal defined 2024 actions, conditions, and Fighter features. Reprinting the entire Fighter, feats, and glossary would make it less usable.

## H. Interaction and exploit report

### H1. Intended strong synergies

| Interaction | Finding |
|---|---|
| Action Surge + PF | Second Attack action supplies second PF use; explicit intended synergy |
| Grappler + Close Work | Damage plus one grapple attempt, then later attacks with Advantage if successful; hand and size requirements remain |
| Tavern Brawler + contact | Reroll ones and once/turn push survive; overlapping d4/proficiency benefits do not stack |
| Shield Master + contact | Shield Bash can establish Prone; Close Work may choose damage/grapple instead of redundant shove; Bash is once on own turn |
| GWM + Hit or Correct | Heavy ranged weapon follow-up retains PB damage when on-turn/part of Attack; STR13 prerequisite and weapon accuracy remain |
| Dual Wielder/Nick + PF | Different sources can add attacks; Nick is still once/turn and BA remains singular |
| Charger + readiness/shift movement | Movement can help meet charge geometry; charge rider remains once on own turn; distant ranged attacks do not qualify |
| Sentinel + Hook/capstone | Actual Sentinel OAs can receive d10, displacement, and full-duration Advantage |
| Tactical Master + Parting Blow | Slow can coexist with its separate penalty; choose other Mastery as needed |
| Weak Point/Threat Scan + Readiness | Early information is the deliberate reward; Search/Study can benefit from a known Lesson |
| Reserve Readiness + Lessons | Later Search/Study follows the same enhancement rules |
| Dig Deep + BA attack builds | Healing no longer crowds out their BA on a Surge turn; not extra BA capacity |
| Mage Slayer + extra damage attempts | More chances to force concentration saves; does not create a spellcasting-triggered reaction attack in 2024 |

Relevant verified feat text: [R14–R22, R24, R31].

### H2. Concerning dominant routines, not demonstrated exploits

- **Level-3 contact damage every round.** It is often optimal; the presence of an obvious ordinary damage turn is not automatically bad. Watch whether Grapple/Shove ever gets chosen and whether low-level utility becomes invisible.
- **Level-18 marked-boss offense and defense.** Constant Advantage plus enemy Disadvantage plus save Advantage can compress three roles into one feature. Compare boss and mixed-enemy maps; the capstone is weaker before the Veteran's first turn and when the marked target disappears.
- **GWM ranged follow-up plus damage items.** The omitted ability modifier is not a complete high-level damage cap. If it dominates actual play, first examine rider abundance and comparison builds rather than retroactively removing all rider synergy.
- **Field-Expedient Tool + Sabotage/Barricade.** Genuine physical setup plus retained attacks is desirable; if every object qualifies without materials or time, the adjudication boundary has failed.
- **Weak Point as default opening choice.** Fine when the observational fiction matters; concerning if it grants unconditional party Advantage against every creature or is denied so often it becomes a trap.

### H3. Confusing interactions resolved by the testing text

| Question | Testing-build resolution |
|---|---|
| Two Practical Fighting branches in one action? | No; shared use |
| Does a thrown melee weapon trigger Close Work? | Only a melee attack with a weapon does; a thrown ranged attack triggers Hit or Correct |
| PF from Disengage or Magic BA attacks? | No; those attacks are outside an Attack action |
| PF during own-turn Hair Trigger Reaction? | Yes if all normal conditions apply; not on another creature's turn |
| Haste PF follow-up? | No additional PF attack from one-attack-restricted action |
| Haste utility replacement? | Testing rules require a normal Attack action, excluding expressly one-attack-restricted actions |
| PAM Reactive Strike qualifies Hook/Sentinel Halt? | It is separately named, not automatically an OA |
| Break Their Hold with glaive? | Explicitly up to held melee weapon reach; no damage or Mastery rider |
| Grapple DC gets Dexterity from Practical Contact? | No; another feature such as applicable Monk Martial Arts can change it |
| Two-handed held weapon while grappling? | Can release a hand to grapple, but cannot make two-handed weapon attacks until the hand is available |
| Reserve Sabotage grants tool proficiency forever? | No; only for the selected action/procedure |
| Known Sabotage retraining harvests tools? | No; proficiency exists while the Lesson is known |
| Reserve Weak Point continues after the action? | Yes; its created effect lasts normally, but the Lesson is not generally known |
| Reserve Hair Trigger declaration? | When taking Ready, before rolls; benefit remains through that readied action |
| Fire-Team ends on independently advantaged hit? | Yes; first allied hit ends the attack-mode benefit |
| Help legal without own proficiency for Correction? | No |
| BA attack from unsuccessful Sabotage? | Yes after a genuine valid Hasty attempt; one BA total |
| Hook movement creates chained OAs? | Forced displacement does not use the displaced creature's own movement/action; no self-repeating OA chain |

### H4. Actual loopholes in loose wording; removed before testing

1. **Tool proficiency harvesting:** unqualified “gain proficiency” plus rest-swapping can create permanent proficiency accumulation. Use proficiency while known; reserved access is temporary.
2. **Ranged fine manipulation:** full Utilize-at-normal-range can look like long-distance thieves' tools. Limit remote work to a real strike/cut/impact/pressure procedure and preserve actual tool requirements.
3. **Unbounded “one attack replacement” copying:** using generated PF/Light slots for tasks can create utility without sacrificing normal offense. Define eligible slots.
4. **Attack-count copying in Hair Trigger:** “same number as on your turn” can be read to import PF/Nick/other conditional bonus attacks. Specify Fighter Extra Attack count.
5. **Unclear concurrent Weak Points:** repeated free opening studies could accumulate independent shared benefits. One active subject and one benefit per turn close this.

These are interpretation paths, not proof that the author intended them or that they were used at a table. No infinite attack, heal, or rest-resource recursion was found after the stated restrictions.

### H5. Multiclass stress tests

| Multiclass | Strong interaction | Cost / boundary / verdict |
|---|---|---|
| Fighter 3 / Monk X | Extra unarmed attempt can use a better Martial Arts die; Monk may improve grapple DC | Delays Monk scaling; armor/weapon restrictions for Martial Arts remain. Strong dip to test; do not add dice together |
| Fighter 3 / Rogue X | Cunning Action Disengage + Parting Blow creates a BA weapon attack; main action may Ready for off-turn Sneak Attack | Powerful two-turn Sneak Attack routine; Rogue lost levels, Ready trigger/Reaction risk, and feat alternatives matter. Must prioritize playtest |
| Fighter 3 / Barbarian X | Rage bonus and Reckless Advantage on Strength contact attacks; lessons remain mundane | Three-level investment delays Barbarian features; Rage uses, BA, heavy-armor restriction remain. Intended strong synergy |
| Fighter / Paladin | More contact/weapon attempts can deliver qualifying damage; Dig Deep may preserve BA | Smite's actual casting/BA and once-per-turn slot rules constrain nova. No free second Bonus Action |
| Fighter / Ranger | Marked-target on-hit damage may benefit extra hits; ranged safety improves positioning | Mark retargeting consumes BA; concentration and setup matter; not every follow-up may hit the marked creature |
| Fighter 7 / Rogue | Hair Trigger restores Fighter's own two attacks off-turn, not Rogue attack-count scaling | Seven-level dip is expensive; one off-turn Sneak Attack per turn, not per attack |
| Fighter 3 / caster | Real Attack actions can trigger PF; spell attacks alone cannot | Action Surge still cannot take Magic; homebrew Tool cannot activate item spells |

The Rogue withdrawal/Ready routine deserves special attention. It is not accurate to dismiss it as harmless simply because it is finite. Conversely, comparable off-turn Sneak Attack can be enabled by allies, other feats, and other subclasses; assess its **reliability and opportunity cost**, not only its maximum packet. Relevant class and Martial Arts text: [R1, R32]. The proposed testing build preserves it for evidence rather than imposing a speculative once-per-turn damage restriction.

## I. Recommended changes, ranked

### Required before testing

- Shared PF use and action membership; explicit Dexterity contact attack accuracy; explicit limited-action boundary.
- Closed Field-Expedient Tool scope; actual tools/materials/time and action-type boundaries.
- Precise utility ranges/targets, target-chosen saves, and attack-slot eligibility.
- Hair Trigger attack-count clarification; Reserve scope and rest/proficiency handling.
- Fire-Team hit expiration; Threat Scan discovery boundary; Weak Point shared effect and concurrency limit.
- Complete timing/resource language and internally consistent Lesson progression.

### Strongly recommended before testing

- Merge the two combat Help modes and the two small-object utility concepts; publish 20 selections.
- Sabotage BA after a genuine attempt; state this choice openly.
- Use Still in the Fight for level 15 and a known/reserve checkbox handout.
- Test matched official Fighters with resources, not resource-empty subclass comparisons.

### Optional polish

- Arrange Lessons alphabetically within prerequisite tiers.
- Make a one-page player reference with selected Lessons and a “normal turn / procedure turn / Surge turn” reminder.
- Use consistent “attack with a weapon,” “Unarmed Strike,” “Fighter level,” and “until the start of your next turn” wording.

### Defer until playtest

- Damage or use-limit changes to Practical Fighting.
- Changing the capstone's off-turn Advantage or defensive components.
- Adding Open the Lane, Spoil the Reaction, or Suppressing Fire.
- Cutting another fieldcraft Lesson merely because its campaign is niche.
- Moving all new utility Lessons to higher level or adding an independent resource system.

## J. Polished testing build

The following is the complete **recommended** public testing version. The audit's mechanics-setting decisions are documented in K. It includes 20 selectable Lessons and all accepted source procedures; experimental candidates are omitted.

---

# Fighter Subclass: Veteran

*Learn When the Proper Way Is the Wrong Way*

Veterans survive by recognizing danger, preparing contingencies, and using whatever the battlefield provides. Their hard-won experience makes weapons, fieldcraft, and practical improvisation parts of the same craft.

## Level 3: Hard-Won Lessons

You learn four Hard-Won Lessons of your choice from the options below. You must meet a Lesson's prerequisite to learn it. You learn one additional Lesson at Fighter levels 7, 10, 15, and 18.

| Fighter Level | Lessons Known |
|---|---:|
| 3 | 4 |
| 7 | 5 |
| 10 | 6 |
| 15 | 7 |
| 18 | 8 |

A Lesson modifies only the action or Reaction it names unless it says otherwise. If multiple Lessons can apply to the same action, you can apply them together unless their effects require different choices for that action. A Lesson doesn't grant an additional action, Bonus Action, or Reaction unless it expressly says so.

**Attack Procedures.** A Lesson that replaces an attack can be used only during an Attack action on your turn that isn't expressly limited to one attack. It replaces an attack granted by that action or your Extra Attack feature, not an extra attack granted by Practical Fighting or the Light property. Each such Lesson can replace only one attack during that action. The procedure isn't an attack roll, deals no attack damage, and doesn't apply weapon properties or magical attack benefits except as the Lesson specifies.

## Level 3: Practical Experience

You gain proficiency in one of these skills of your choice: Animal Handling, Athletics, Insight, Intimidation, Investigation, Medicine, Perception, Stealth, or Survival. Choose one skill from this list in which you are proficient; you gain Expertise in it.

## Level 3: Practical Fighting

You gain the following benefits.

**Practical Contact.** You have proficiency with Improvised Weapons. When you choose the Damage option of your Unarmed Strike, you can use Strength or Dexterity for its attack and damage rolls. You can replace its normal damage with 1d6 plus the chosen modifier.

A held weapon, equipped Shield, or similar implement can represent the Damage or Shove option of this Unarmed Strike. It remains an Unarmed Strike against a creature within 5 feet and gains none of the implement's weapon properties, mastery properties, or magical benefits. This feature doesn't change the Grapple or Shove save DC or the requirements for those options.

**Practical Fighting Options.** Once during each Attack action on your turn, immediately after you make an attack with a weapon, you can use one of the following options, as appropriate. An attack granted by either option is part of that Attack action, can't trigger this feature again, and can't be granted during an action expressly limited to one attack.

- **Close Work.** After a melee attack with a weapon, make an Unarmed Strike against a creature within 5 feet of you.
- **Hit or Correct.** After a ranged attack with a weapon, move up to half your Speed without provoking Opportunity Attacks. You can then make one ranged attack with a weapon. If the triggering attack hit, this additional attack must target a different creature. If it missed, the additional attack can target the same creature or a different creature. Don't add a positive ability modifier to the additional attack's damage. The weapon's normal requirements still apply.

## Level 7: Battlefield Readiness

When you roll Initiative, before making the roll, choose two different options below. Counter-Ambush takes effect immediately. Resolve the other chosen options at the start of your first turn in that combat, in either order. If you have the Incapacitated condition at that time, you can't resolve them.

- **Counter-Ambush.** Being surprised doesn't impose Disadvantage on this Initiative roll.
- **Take Position.** Move up to half your Speed.
- **Read the Field.** Take the Search or Study action.
- **Brace.** Gain Temporary Hit Points equal to your Proficiency Bonus.

An action taken with this feature can benefit from a Hard-Won Lesson that modifies it.

## Level 10: Been Here Before

**Change of Approach.** When you finish a Short or Long Rest, you can replace one Hard-Won Lesson you know with another for which you qualify.

**Reserve Lessons.** When you finish a Long Rest, choose two Hard-Won Lessons for which you qualify and that you don't know. They are your Reserve Lessons until you choose again. If you learn one of them, it is no longer a Reserve Lesson; you don't choose a replacement until your next Long Rest.

When you begin an action, Reaction, or procedure that a Reserve Lesson can modify, you can use that Lesson as though you knew it for that action, Reaction, or procedure. Declare this use before making any of its rolls. The Lesson's resulting effects last for their normal duration, including a readied action or assistance that resolves later, but you gain no continuing access to the Lesson. Any proficiency it grants applies only to that use.

Once you use either Reserve Lesson this way, you can't use this benefit again until you finish a Short or Long Rest. This benefit doesn't reset or bypass a Lesson's own limits.

## Level 15: Still in the Fight

**Reserve Readiness.** Once per combat, at the start of one of your turns after your first turn, you can use one Battlefield Readiness option you haven't used in that combat, other than Counter-Ambush. You can't use this benefit while Incapacitated.

**Dig Deep.** When you use Action Surge, you can expend one use of Second Wind to regain its Hit Points without taking a Bonus Action. You can also move up to half your Speed without provoking Opportunity Attacks, as with Tactical Shift.

**Improved Brace.** Your Brace option grants Temporary Hit Points equal to twice your Proficiency Bonus.

## Level 18: Veteran of a Hundred Fights

At the start of each of your turns in combat, choose one creature you can see. Until the start of your next turn, you have Advantage on attack rolls against it and saving throws it forces you to make, and it has Disadvantage on attack rolls against you.

## Hard-Won Lessons

### Base-Access Lessons

#### Battlefield Improvisation

Once during an Attack action on your turn, you can replace one attack with one of these procedures:

**Deliver.** Throw one object you are holding, weighing no more than 5 pounds and small enough to hold in one hand, to a willing creature you can see within 30 feet. The object must have an unobstructed path. The creature can take a Reaction to catch it if it can see the object and has a free hand. Otherwise, it lands in the creature's space. This doesn't activate, use, drink, or equip the object.

**Misdirect.** Create a distracting sound at a point you can see by throwing a small nonmagical object up to 30 feet, or by striking an object or surface with a ranged or thrown weapon within its normal range. The point must have an unobstructed path, and the method must be capable of producing an audible impact there. Expend the object or ammunition normally.

Until the start of your next turn, a creature within 30 feet of that point that heard the sound but couldn't see how you caused it has Disadvantage on the first Wisdom (Perception) check it makes to locate a creature other than you by hearing. This doesn't conceal you, obscure anything, or prevent a noise you make from revealing you.

#### Break Their Hold

Once during an Attack action on your turn, you can replace one attack to interfere with a creature within 5 feet of you, or within the reach of a Melee weapon you are holding and use for the procedure. The creature makes a Strength or Dexterity saving throw (its choice) against your Unarmed Strike save DC.

On a failed save, choose one grapple it is maintaining to end, or one unsecured object it is holding to drop. A dropped object lands in its space. This can't remove worn or attached equipment, and it doesn't override a feature that prevents disarming.

#### Break Through

When you take the Dash action, until the end of the turn you can move through an enemy's space if it is no more than one size larger than you. Your movement doesn't provoke Opportunity Attacks from enemies whose spaces you enter this way.

The first time you enter each such enemy's space on that turn, it makes a Strength or Dexterity saving throw (its choice) against your Unarmed Strike save DC. On a failed save, you can push it 5 feet to an unoccupied space adjacent to its original space. You can't willingly end your movement in another creature's space.

#### Casualty Extraction

When you take the Disengage action, until the end of the turn you don't spend extra movement to drag or carry a willing creature or one with the Unconscious condition. You must still be able to physically move the creature.

#### Field Concealment

When you take the Hide action, ignore Disadvantage on its Dexterity (Stealth) check imposed by your armor.

After you succeed on that check, you can choose up to your Proficiency Bonus willing creatures within 30 feet that can see or hear you. For 10 minutes, you and the chosen creatures have Advantage on Dexterity (Stealth) checks made to Hide and ignore armor-imposed Disadvantage on those checks. Normal requirements for hiding still apply.

Once you grant this group benefit, you can't do so again until you finish a Short or Long Rest.

#### Field-Expedient Tool

Once during an Attack action on your turn, you can replace one attack with a Utilize action to perform one physical procedure on a nonmagical object or mechanism using a weapon you are holding: cutting, levering, hammering, probing, applying pressure, or rough repair. The procedure must normally be possible with one Utilize action. It can't target anything worn or carried by an unwilling creature.

For a required ability check, you can use the ability modifier you would use to attack with that weapon. You add your Proficiency Bonus if you are proficient with it, without adding the bonus more than once. You must still have any tools or tool proficiency the procedure requires.

You can perform the procedure within the weapon's melee reach. With a ranged or thrown weapon, you can instead strike a point within its normal range along an unobstructed path, expending ammunition or throwing the weapon normally. A ranged procedure must be accomplished by that strike's impact, cutting, or pressure; it can't perform fine manipulation or use tools at a distance.

This Lesson doesn't deal attack damage, use or apply a consumable, don or doff equipment, craft an item, accelerate a procedure lasting longer than an action, or activate a magic item. A Hard-Won Lesson that modifies Utilize can apply if the procedure also meets that Lesson's requirements.

#### Fire-Team Assist

When you take the Help action to assist against an enemy, choose one of these options:

**Distract.** The enemy can be within 30 feet of you instead of 5 feet. Until the start of your next turn, your allies have Advantage on attack rolls against it until the first allied attack hits it. After that hit, the attacker can immediately move up to 10 feet without provoking Opportunity Attacks from that enemy.

**Two-Man Takedown.** If the enemy is within 5 feet of you, choose Grapple or Shove. Before the start of your next turn, the next time one of your allies uses that option of an Unarmed Strike against it, the enemy has Disadvantage on the saving throw. This replaces the Help action's normal attack-roll assistance.

#### Forced March

When you take the Dash action, gain 10 additional feet of movement from that action, and Difficult Terrain doesn't cost you extra movement until the end of the turn.

#### Hold Ground

When you take the Dodge action, until the start of your next turn you have Advantage on saving throws and ability checks to avoid becoming Prone, becoming Grappled, or being moved against your will. Forced movement that allows you no saving throw or ability check is reduced by 10 feet, to a minimum of 0.

Having your Speed reduced to 0 by the Grappled condition doesn't itself end the benefits of that Dodge action. Its other limitations still apply.

#### Parting Blow

When you take the Disengage action, you can make one attack with a weapon or an Unarmed Strike at any point during your movement on that turn. On a hit, the target's Speed is reduced by 10 feet until the start of your next turn. Multiple uses of this Lesson don't increase that reduction on the same target.

#### Shield the Line

When you take the Dodge action, choose one willing creature within 5 feet of you. Until the start of your next turn, it has Half Cover while it is within 5 feet of you and you aren't Incapacitated.

#### Threat Scan

When you take the Search action to look for concealed creatures, immediate physical dangers, tracks, or signs of recent violence or an impending ambush, you have Advantage on its Wisdom check. On a success, the DM can identify one useful tactical detail supported by what you found.

If that Search reveals a concealed creature's location, choose one creature found this way. Until the start of your next turn, the first attack roll made against it has Advantage, and the first attack roll it makes has Disadvantage.

#### Veteran's Correction

When an ally fails an ability check that received Advantage from your Help action, you can use Tactical Mind on that check as though you had failed it. The normal Second Wind cost and Tactical Mind rules apply.

### Fighter Level 7 Lessons

#### Hair Trigger

*Prerequisite: Fighter Level 7*

When you take the Ready action to ready the Attack action and use your Reaction to take that action, you can make two attacks with weapons or Unarmed Strikes instead of one. This becomes three attacks at Fighter level 11 and four at Fighter level 20.

Once during that readied action, when you hit with one of these attacks, you can cause it to deal an extra 1d10 damage of a type it deals. This Lesson extends only the number of attacks granted by your Fighter Extra Attack feature; other features keep their own requirements and limits.

#### Hook and Turn

*Prerequisite: Fighter Level 7*

When you hit a creature with an Opportunity Attack, the attack deals an extra 1d10 damage of a type it deals. If the target is Large or smaller, you can also move it up to 5 feet to an unoccupied space within the reach you used for that attack.

### Fighter Level 10 Lessons

#### Battlefield Activation

*Prerequisite: Fighter Level 10*

When you take the Magic action to activate a magic item, you can draw or stow that item as part of the action. After the activation resolves, you can make one attack with a weapon or an Unarmed Strike as a Bonus Action on that turn. The item's normal activation and eligibility requirements apply.

#### Common Soldier's Tongue

*Prerequisite: Fighter Level 10*

When you take the Influence action against a Bloodied creature that can understand you, you can urge it to surrender, retreat, drop a held weapon, release a creature, or cease fighting. If the DM determines that the demand is a plausible means of survival for it, treat its willingness as Hesitant unless it is already Willing. Its attitude doesn't change. This can't override magical compulsion or make an impossible or suicidal demand feasible.

You also have Advantage on Influence checks about danger, supplies, routes, pay, security, working conditions, or survival when dealing with soldiers, guards, mercenaries, sailors, laborers, and similar practical workers. Conversation can reveal ordinary relevant information they know and aren't trying to conceal; it doesn't compel disclosure of secrets.

#### Find the Weak Point

*Prerequisite: Fighter Level 10*

When you take the Study action to examine a creature or nonmagical object, structure, vehicle, or mechanism you can observe, you can look for a practical weakness. The DM determines whether one can be inferred from the available evidence and chooses the relevant Intelligence check and DC. On a success, the DM identifies that weakness and how an attack or physical procedure could exploit it.

For 1 minute, once on each turn, you or a creature that can see or hear your directions can have Advantage on one attack roll or ability check that exploits the weakness in the described way. This benefit is shared among all such creatures. It ends early if the weakness no longer applies or you successfully identify another weakness with this Lesson.

The information can include damage, structural condition, failure points, or possible repair and bypass methods. It doesn't reveal numerical game statistics or unsupported damage vulnerabilities. Useful information remains valid after the Advantage ends until the subject changes.

#### Quick Barricade

*Prerequisite: Fighter Level 10*

When you take the Utilize action while within reach of sturdy materials you can physically manipulate, you can arrange them into a barricade along up to two connected 5-foot edges within reach. The materials must be sufficient to obstruct attacks.

The barricade grants Half Cover against attacks and effects passing through it. Crossing one of its protected edges costs 5 extra feet of movement. Its AC, Hit Points, and other properties are those of its actual materials.

Outside combat, you can spend 10 minutes assessing a camp, room, doorway, chokepoint, or firing position and planning or arranging practical fortifications. Larger work uses the normal materials, checks, and time the DM determines; this Lesson doesn't create materials or shorten construction beyond what is physically feasible.

#### Sabotage

*Prerequisite: Fighter Level 10*

While you know this Lesson, you have proficiency with Thieves' Tools or Tinker's Tools, chosen when you learn it.

When you take the Utilize action to interfere with an accessible nonmagical object or mechanism, you have Advantage on any required check. The DM determines the appropriate check, tools, and feasibility. On a success, choose one of these effects:

- **Jam.** One normal function can't be used until the sabotage is cleared.
- **Rig.** The object appears functional, but one normal function you choose fails the next time it is used. The sabotage then becomes obvious.

Choose one method when you begin:

- **Hasty.** The attempt takes one Utilize action. After making the attempt, you can make one attack with a weapon or an Unarmed Strike as a Bonus Action on that turn. A creature can clear the sabotage with a Utilize action and an ability check using an appropriate skill or tool, against DC 8 plus your Proficiency Bonus and your Strength or Dexterity modifier, chosen when you sabotage it.
- **Deliberate.** The attempt takes 1 minute. Clearing it requires suitable tools or materials and a check against the same DC; simply removing an obstruction isn't sufficient.

The attempt must plausibly interfere with the object's construction or operation. This Lesson can't make it fail in an unsupported way, override a magic item's properties, or replace the normal rules for damaging objects.

---

**End of testing-build rules.**

## K. Change log

“Editorial” below means clarification consistent with the recorded intent. “Mechanical” means a new limit, exception, merger, or concrete choice where the source was incomplete. Neither label implies canon without the user's acceptance.

| Source wording/mechanic | Recommended wording/mechanic | Reason | Type |
|---|---|---|---|
| 22 selectable Lessons; Takedown separate | 20 selections; Takedown inside Fire-Team | Same action and mutually exclusive modes; remove slot tax | Mechanical merger |
| Deliver and Misdirect separate | Battlefield Improvisation, two procedures | Improve utility pick value without new effects | Mechanical merger/name |
| Contact d6+STR/DEX damage only | STR/DEX attack and damage | Dexterity accuracy otherwise remains Strength | Mechanical correction |
| Damage stated as 1d6 plus chosen modifier | Explicit optional damage replacement | Preserve better Unarmed Strike options granted by another feature | Editorial compatibility clarification |
| Implement benefit exclusion bullets | One compact exclusion sentence | Preserve mundane Unarmed Strike identity | Editorial |
| Each branch says once/action; shared use is intent note | One shared trigger; choose one branch | Avoid double branch use | Editorial, recorded intent |
| Generated attack membership unclear | Generated attack part of Attack action | Resolve GWM/Grappler/property timing | Editorial/integration |
| Haste question open | No additional PF attack in one-attack-limited action | Prevent overriding explicit attack restriction | Mechanical boundary |
| Move then make HoC follow-up | Move then optionally make follow-up | Permit accepted ranged repositioning when no alternate target is legal | Mechanical clarification |
| Melee/ranged weapon attack phrasing | Melee/ranged attack with a weapon | Separate attack modality from weapon category; include thrown attacks appropriately | Editorial |
| Utility replaces one attack; repetition undefined | Once per Lesson/action on own turn; ordinary slots only; no restricted action | Prevent free generated-slot conversion or off-turn ambiguity | Mechanical boundary |
| Tool = Utilize targeting nonmagical object | Closed weapon-assisted physical procedures | Exclude arbitrary action conversion, fine remote work, crafting/activation | Mechanical narrowing |
| Tool checks replace modifier/add weapon proficiency | Same choice; PB only once; required tools preserved | Prevent stacking and tool bypass | Editorial |
| Tool range merely “appropriate” | Impact/cutting/pressure, unobstructed path, normal ammunition | Make ranged boundary reviewable | Mechanical specificity |
| Break Hold within reach, target STR/DEX | 5 feet or explicit held melee weapon reach; target chooses save | Resolve reach and save owner | Editorial/open-choice resolution |
| Break Hold drop held object | Unsecured held object drops in target space; protected disarming respected | No armor/straps/War Bond bypass | Mechanical boundary |
| Misdirect range tentative; payoff open | 30-foot throw or weapon normal range; hearing radius30; first hearing-based locating check until next turn | Turn concept into bounded physical rule | Mechanical completion |
| Deliver range/weight/open geometry | Visible willing recipient30, held one-hand object≤5lb, unobstructed path; Reaction/free hand/visibility | Complete procedure without use/activation | Mechanical completion |
| Break Through saving throw owner open | Target chooses; first entry/creature/turn; no occupied endpoint | Consistent save and movement rules | Editorial |
| Field Concealment group use timing | Voluntary activation after successful legal Hide | Don't accidentally consume limited benefit | Editorial |
| Fire-Team Advantage until one hits; benefit ambiguity | First allied hit ends regardless of other Advantage; movement follows | Eliminate source-of-Advantage accounting | Editorial |
| Threat Scan “locates” creature | Reveals concealed creature's location | Prevent sham Search of already visible target | Mechanical clarification |
| Parting Blow PF prohibition | Rely on shared PF Attack-action trigger; same Speed penalty doesn't stack | Delete redundant prohibition; prevent own copies stacking | Editorial/nonstacking boundary |
| Level7 opening options lack Incapacitated clause | Cannot resolve first-turn options while Incapacitated | Prevent free movement/Brace during lost turns | Mechanical boundary |
| Reserve Lesson used as though known | One action/Reaction/procedure, normal resulting durations; proficiency temporary | Close ongoing and passive acquisition ambiguities | Mechanical completion |
| Reserve/known overlap after swapping unspecified | Learned reserve removed; no replacement before LR | Preserve two unknown contingencies without unlimited reselection | Mechanical completion |
| No Lesson Wasted name | Still in the Fight | Endurance and contingency fit new package | Editorial name |
| Reserve Readiness start later turn | Same; Incapacitated exclusion | Consistent opening/later readiness behavior | Mechanical boundary |
| Dig Deep refers to Tactical Shift as BA activation | Explicit heal and half-Speed safe movement | Preserve exception without pretending a BA occurred | Editorial |
| Hair Trigger same number as on-turn action | Fighter2/3/4 EA count; retain d10 on one chosen hit | No PF/Nick copying; preserve accepted damage choice | Editorial attack-count clarification |
| Hook position within reach | Reach used for OA | No post-hit swapping to unrelated reach | Editorial |
| Soldier demand may be Hesitant “when appropriate” | Plausible survival demand; willingness changes, attitude doesn't | No hostile penalty deletion or mind control | Mechanical completion |
| Activation requirement exclusion list | Normal item requirements apply | Same requirements, less explanatory text | Editorial |
| Sabotage gain tools | Proficient while known; choice when learned | No permanent tool collection by retraining | Mechanical narrowing |
| Sabotage BA success/attempt unresolved | Genuine Hasty attempt, success not required | Preserve action momentum on uncertain task | Mechanical choice |
| Barricade “several minutes” broad ribbon | 10-minute assessment; ordinary construction time/materials/checks | Table-ready time without automatic fortress | Mechanical completion |
| Weak Point once/turn shared unclear; many subjects possible | One shared benefit each turn; one active identified weakness | Avoid multiplying independent advantage banks | Mechanical narrowing |
| Weak Point successful INT check, DM boundaries open | DM feasibility/check/DC and described exploitation method | Keep observed mundane evidence and exclude stats | Editorial/completion |
| Capstone full-duration/off-turn Advantage | Preserved unchanged | Strong synergy is not evidence for nerf | No change |
| Lessons4/5/6/7/8; Experience; Readiness choices; rest swap | Preserved | No identified architecture defect | No change |

No rejected universal action replacement, extra-Reaction engine, Finish the Wounded, old Change the Plan, or experimental suppression procedure returns.

## L. Public playtest plan

### L1. First release protocol

Freeze the text above as **Veteran Public Test 1**. Record version and all rulings before play. Do not make mid-session balance changes unless an obvious rules failure prevents play. Use the same encounter, equipment, party composition, and rest resources for an official Fighter comparison when feasible; rotate players/subclasses across sessions to reduce player-skill bias.

Start with levels **3, 5, 7, 10, 11, 13, 15, 17, 18, 20**. They need not all be a long campaign: selected one-shots can isolate feature changes. At minimum prioritize 3/5, 10/11, and 18/20; the remaining checkpoints can be short controlled encounters.

### L2. Builds

| Build | Test priorities |
|---|---|
| Strength greatsword/GWM | Contact damage vs control, Graze, Surge, adjacency lost |
| Sword/shield + Shield Master | Two available shove effects, no grapple hand with weapon/shield, protected ally |
| Glaive + PAM/Sentinel | 10-foot attacks vs 5-foot contact; Reactive Strike vs true OA |
| Dual wield + Nick/Dual Wielder | One Nick across Surge; BA healing conflict; Vex consumed by contact |
| Dex rapier | Dex accuracy fix; weak STR grapple DC; stealth/Expertise |
| Longbow + Archery/GWM | Single vs multiple targets; Strength prerequisite; movement and rider value |
| Heavy/hand crossbow + XBE | Loading before feat; ammunition hands; correct Light vs PF bonus damage |
| Handaxe/dagger thrown | Actual thrown drawing, Vex target switching, lack of Archery bonus |
| Free-hand weapon + Grappler/Tavern Brawler | First contact grapple, escape, control vs damage, weapon-hand restrictions |

Also run **Fighter3/RogueX**, **Fighter3/MonkX**, and **Fighter3/BarbarianX** at representative total levels 8 and 12. Add Paladin/Ranger cases if they appear in the intended playtest group. Avoid treating multiclass maxima with magical party support as ordinary pure-Fighter results.

### L3. Encounters and specific stress tests

| Test | Setup | Data / question |
|---|---|---|
| Single durable threat | One dangerous melee enemy, then one ranged/caster enemy | HoC all-hit turns; capstone attack/save defense; can marked enemy still threaten party? |
| Mixed threats | One major foe plus several smaller enemies | Mark decision, split damage, Opportunity Attack coverage, overkill |
| Ambush | Actual surprise/disadvantage; hidden and visible threats | Choice timing, Counter-Ambush pick frequency, genuine Search success |
| Bad terrain | Rubble, occupied lane, high ground, unreachable/flying target | Forced March/Break Through distinction; contact availability; ranged movement |
| Grapple rescue | Ally restrained by a monster grapple, enemy STR/DEX variants | Break Their Hold vs Push/Shove; ally Action saved; anatomy and size |
| Armed opponent | Enemy has backup weapon; dropped weapon can be retrieved | Is repeatable disarm useful without shutting down every enemy? |
| Siege room | Actual movable furniture, lever, secured door, inaccessible mechanism | Tool feasibility; Barricade cost; ranged “impact” boundary; object durability |
| Extraction | Downed ally in threatened space; carrying limits specified | Distance recovered, OA consequences, healing/resource savings |
| Infiltration | Armored party, observer Search, real sound occlusion | Concealment requirements; Improvisation check penalty; hidden shooter not immune to noise |
| Social surrender | Bloodied self-preserving enemy vs fanatical/compelled opponent | Hostile penalty retained; credible compliance; DM veto and check frequency |
| Ready lane | Trigger certain, then trigger uncertain/cancelled | Hair Trigger damage, unused Reaction, lost ready turn, BA trade |
| Restriction challenge | Haste; Surge+Ready; Nick; Shield donning; consumable/magic activation | Can players execute legal sequence without repeated clarification? |
| Item nova | Legal attuned item; charges recorded; Surge+Activation+Dig Deep | Actual extra BA attack value vs item effect; healing and resources |
| Low-rest day | Three encounters, no SR; repeat with one and two SR | Sustain vs BM/Psi resources; actual combat length |

Test 3-, 4-, and 5-round combat targets when possible. Do not end every combat mechanically at its target duration: record actual ending, early surrender, resource exhaustion, and waves. Those deviations are useful evidence.

### L4. Record each turn and encounter

Record target AC/save modifier, attack bonus, attacks attempted/hit/critical, Advantage source, damage actually dealt versus overkill, Mastery choices, PF branch and target, utility procedure, attacks sacrificed, movement actually useful, BA/Reaction use, resources spent/restored, and damage prevented where observable.

For party utility, record attacks/Actions saved, ally movement enabled, enemy Actions spent recovering equipment/escaping/clearing sabotage, meaningful surrendered enemies, prevented attacks, healing avoided, and whether terrain or objectives made the Lesson decisive. Record DM denial of a Lesson separately from successful but low-value use.

For usability, record turn duration, rules lookups, repeated questions, mistaken triggers, forgotten features, and whether the player could state the intended procedure before rolling. Log known/reserve selections and changes, but do not equate nonselection in one campaign with universal weakness.

### L5. Decision thresholds

These are review triggers, not automatic numerical verdicts. Aim for at least **six matched encounters per tier/build question**, several DMs, and more than one map before interpreting a pattern. Small samples can identify wording failures earlier than balance failures.

| Finding | Response justified |
|---|---|
| Repeated materially higher total contribution than well-resourced official comparators, with no offsetting positional/resource cost | Investigate a targeted nerf to the producing interaction, not the entire subclass |
| Consistent >20–25% personal damage advantage across matched ordinary and resource-rich scenarios, plus equally strong defense/control | Power review; percentage alone doesn't decide it |
| Ranged Veteran unable to produce useful correction/movement across several plausible single/multi-target encounters | Consider a focused buff after verifying build/Loading/target mistakes |
| One Lesson selected by >80% of materially different builds and repeatedly crowding out others | Check mandatory-pick pressure; change cost/value only if actual outcomes support it |
| Lesson used zero times because the campaign never presents its situation | No immediate cut; test relevant scenario or put it in reserve |
| Lesson remains inferior to mundane base procedures even in its intended scenario | Merge, buff, or cut; delivery/distraction merger is designed to prevent this |
| DM must improvise a new rule on most uses, or different DMs read opposite meanings | Wording change, even without a balance problem |
| Weak Point denied frequently despite observable enemies/structures | Clarify examples/DM guidance before changing raw Advantage strength |
| Weak Point supplies essentially unconditional Advantage for every ally turn without meaningful study/evidence | Tighten exploit method or availability based on observed abuse |
| Ready/Rogue dip reliably doubles Sneak Attack with negligible lost actions/triggers | Target the off-turn delivery routine after official alternative comparison |
| Capstone makes one boss unable to threaten Veteran or allies despite appropriate encounter tools | Review one component or targeting persistence; retain thematic single-threat focus |
| Level15 repeatedly irrelevant in hard, attrition-rich encounters | Reassess its payoff after healing, BA compression, and later Readiness use are recorded |

The public test should answer whether the Veteran's options create useful decisions at reasonable table speed. Its final damage number is less important than whether the mundane procedures, preparation, and survival advantages earn their costs without erasing the rest of the party's roles.

## References

External sources were retrieved during this audit on October 5, 2026. Licensed compendium pages may require purchase/sign-in for full access. Community methodology sources are not rules authority.

- **[R1]** [D&D Beyond, 2024 Basic Rules: Character Classes](https://www.dndbeyond.com/sources/dnd/br-2024/character-classes)
- **[R2]** [Wizards/D&D Beyond, 2024 Fighter changes](https://www.dndbeyond.com/posts/1746-2024-fighter-vs-2014-fighter-whats-new)
- **[R3]** [D&D Beyond, 2024 Rules Glossary](https://www.dndbeyond.com/sources/dnd/br-2024/rules-glossary)
- **[R4]** [D&D Beyond, 2024 Equipment and Weapon Mastery](https://www.dndbeyond.com/sources/dnd/br-2024/equipment)
- **[R5]** [Licensed 2024 Champion text](https://roll20.net/compendium/dnd5e/Subclasses%3AChampion?expansion=32231)
- **[R6]** [Licensed 2024 Battle Master text](https://roll20.net/compendium/dnd5e/Subclasses%3ABattle%20Master?expansion=32231&iframe=true)
- **[R7]** [Licensed 2024 Eldritch Knight text](https://roll20.net/compendium/dnd5e/Subclasses%3AEldritch%20Knight?expansion=32231)
- **[R8]** [Licensed 2024 Psi Warrior text](https://roll20.net/compendium/dnd5e/Subclasses%3APsi%20Warrior?expansion=32231)
- **[R9]** [Official PHB 2024 access landing page](https://marketplace.dndbeyond.com/category/3709000)
- **[R10]** [Official PHB 2024 errata, April 2025](https://media.dndbeyond.com/compendium-images/errata/PHB-24/PHB-2024_v1.pdf)
- **[R11]** [Official D&D Beyond changelog](https://www.dndbeyond.com/changelog/)
- **[R12]** [Licensed 2024 Rules Definitions](https://roll20.net/compendium/dnd5e/Rules%3ARules%20Definitions?expansion=32231&iframe=true)
- **[R13]** [Licensed revised Haste](https://roll20.net/compendium/dnd5e/Spells%3AHaste?expansion=32231&iframe=true)
- **[R14]** [Licensed 2024 Great Weapon Master](https://roll20.net/compendium/dnd5e/Feats%3AGreat%20Weapon%20Master?expansion=32231)
- **[R15]** [Licensed 2024 Dual Wielder](https://roll20.net/compendium/dnd5e/Feats%3ADual%20Wielder?expansion=32231&iframe=true)
- **[R16]** [Licensed 2024 Polearm Master](https://roll20.net/compendium/dnd5e/Feats%3APolearm%20Master?expansion=32231)
- **[R17]** [Licensed 2024 Crossbow Expert](https://roll20.net/compendium/dnd5e/Feats%3ACrossbow%20Expert?expansion=32231)
- **[R18]** [Licensed 2024 Grappler](https://roll20.net/compendium/dnd5e/Feats%3AGrappler?expansion=32231)
- **[R19]** [Licensed 2024 Tavern Brawler](https://roll20.net/compendium/dnd5e/Feats%3ATavern%20Brawler?expansion=32231&iframe=true)
- **[R20]** [Licensed 2024 Shield Master](https://roll20.net/compendium/dnd5e/Feats%3AShield%20Master?expansion=32231)
- **[R21]** [Licensed 2024 Sentinel](https://roll20.net/compendium/dnd5e/Feats%3ASentinel?expansion=32231&iframe=true)
- **[R22]** [Licensed 2024 Charger](https://roll20.net/compendium/dnd5e/Feats%3ACharger?expansion=32231)
- **[R23]** [Licensed revised True Strike](https://roll20.net/compendium/dnd5e/Spells%3ATrue%20Strike?expansion=33335&iframe=true)
- **[R24]** [Licensed 2024 Two-Weapon Fighting](https://roll20.net/compendium/dnd5e/Feats%3ATwo-Weapon%20Fighting?expansion=32231&iframe=true)
- **[R25]** [Licensed 2024 Archery](https://roll20.net/compendium/dnd5e/Feats%3AArchery?expansion=32231)
- **[R26]** [Licensed 2024 Thrown Weapon Fighting](https://roll20.net/compendium/dnd5e/Feats%3AThrown%20Weapon%20Fighting?expansion=32231)
- **[R27]** [Licensed 2024 Great Weapon Fighting](https://roll20.net/compendium/dnd5e/Feats%3AGreat%20Weapon%20Fighting?expansion=32231&iframe=true)
- **[R28]** [Licensed revised Weapon +1](https://roll20.net/compendium/dnd5e/Templates%3AWeapon%20%2B1?expansion=33335)
- **[R29]** [Licensed revised Wand of Fireballs](https://roll20.net/compendium/dnd5e/Items%3AWand%20of%20Fireballs?expansion=33359)
- **[R30]** [Licensed revised Bracers of Archery](https://roll20.net/compendium/dnd5e/Items%3ABracers%20of%20Archery?expansion=33335)
- **[R31]** [Licensed 2024 Mage Slayer](https://roll20.net/compendium/dnd5e/Feats%3AMage%20Slayer?expansion=32231&iframe=true)
- **[R32]** [Licensed revised Martial Arts](https://roll20.net/compendium/dnd5e/Other%20Options%20and%20Features%3AMartial%20Arts?expansion=33335)
- **[R33]** [Licensed revised Shield spell](https://roll20.net/compendium/dnd5e/Spells%3AShield?expansion=33335)
- **[R34]** [Licensed 2024 Unarmed Fighting](https://roll20.net/compendium/dnd5e/Feats%3AUnarmed%20Fighting?expansion=32231&iframe=true)
- **[M1]** [Tabletop Builds, A Primer on Quantitative Evaluation in D&D](https://tabletopbuilds.com/a-primer-on-quantitative-evaluation-in-dd/)
- **[M2]** [RPGBOT, Fundamental Math](https://rpgbot.net/dnd5/characters/fundamental_math/)
- **[M3]** [LudicSavant/AureusFulgens, damage calculator methodology](https://forums.giantitp.com/showsinglepost.php?p=23800132&postcount=20)
- **[M4]** [D&D Proving Grounds, DPR calculator and declared day assumptions](https://dndprovinggrounds.com/dpr-calculator)
- **[M5]** [D&D Beyond/Jeremy Crawford, Designing D&D Subclasses](https://www.dndbeyond.com/posts/318-designing-d-d-subclasses-with-jeremy-crawford-part)

## Calculation appendix: coverage and reproduction

The accompanying calculation archive contains `calculate.py`, `official_comparison.py`, `calculations.json`, `official_encounters.json`, `official_days.json`, and `build_results.csv`. Run Python 3 with no third-party dependencies. The model outputs distinguish exact sequencing from the labelled thrown approximation. Tables in this report are generated from those outputs; figures are rounded only for display.

Additional source concepts tested qualitatively: initiative timing, status interactions, object geometry, tool requirements, carrying feasibility, reserved duration, item attunement, slot restrictions, and multiclass feature gates. They do not have invented numerical damage equivalents.

**Preservation statement:** the five feature levels, 4/5/6/7/8 progression, skill/Expertise package, Practical Fighting asymmetry, opening two-choice preparation, bounded reserves/rest swap, Dig Deep, improved Brace, and full-duration single-threat capstone are preserved. The recommended release is a consolidation of the mature design, with disclosed integration fixes and two roster mergers.
