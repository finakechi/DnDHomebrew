# Veteran Fighter Subclass: Design, Balance, and Optimization Research Report

## Executive Summary

The **Veteran is worth continuing**, but the strongest design is substantially narrower and cleaner than Iteration A. The core fantasy is distinct enough to justify a subclass: a mundane front-line survivor whose advantage comes from practiced fieldcraft, battlefield awareness, practical equipment use, timing, and experience rather than command authority, supernatural power, or formal dueling technique. The 2024 Fighter is also a substantially better chassis for that concept than the 2014 Fighter because Weapon Mastery, Tactical Mind, Tactical Shift, Tactical Master, and Studied Attacks already establish “experienced weapon user who adapts tactically” as part of the base class. citeturn15view0turn17search12turn22search12

That is simultaneously the Veteran's opportunity and its main design problem. **A Veteran subclass cannot merely add Push/Sap/Slow, skill bonuses, mobility after Second Wind, or advantage after misses and feel distinctive, because the 2024 Fighter already does those things.** Tactical Master explicitly lets a level 9 Fighter substitute Push, Sap, or Slow for a weapon's normal mastery, while Studied Attacks gives advantage on the next attack against a creature after missing it. citeturn4view2turn4view3turn19view0

My overall verdict is:

| Question | Finding |
|---|---|
| Best architecture | **Iteration C: enhanced generic actions / Veteran Drills**, with major pruning |
| Iteration A | **Abandon the engine; salvage individual ideas** |
| Iteration B | Better presentation, but it does not solve A's underlying action-economy problems |
| Tactical Blow | Keep the *idea* of a modest damage floor, but **not the existing “use utility → gain escalating damage” implementation** |
| Free generic actions | Avoid. Especially **Ready, Dodge, and Magic** |
| Reactions | One additional **restricted** reaction per round at very high level is defensible; “one Reaction on every turn” is too dangerous in this particular subclass |
| Applied Mastery | Cut. It conflicts directly with Tactical Master and permits excessive mastery stacking |
| Sentinel-like package | Do not give both “ignore Disengage” and “Speed 0” cheaply; those are premium control mechanics |
| Magic Action | Prefer **no Magic drill at all**, or one tightly written magic-item-only drill at level 10+ |
| Drill count | About **4 / 5 / 6 / 7 / 8 known**, not 4 / 6 / 8 / 10 / all |
| Best utility niche | Military analysis, fieldcraft, battlefield Search/Study, practical Help, gear/sabotage, preparedness |
| Biggest identity threat | Becoming “Battle Master, but with forty maneuvers” or “Rogue actions on a Fighter” |
| Biggest mathematical threat | Reaction multiplication and free full actions |
| Biggest usability threat | Trying to make every one of twelve generic actions equally important in combat |

The central design lesson is that **you do not need to make every generic action DPR-neutral with the Attack action**. At level 11, a Fighter gives up three attacks to Dodge, Search, Study, Help, or Utilize; at level 20 it gives up four. Trying to compensate fully for that opportunity cost is exactly what pushed Iteration A toward attack replacement, Bonus Actions, escalating Tactical Blow dice, multiple Veteran Actions, and finally free actions. The cure created a more complicated disease.

Instead, Iteration C should accept three classes of drills:

**Combat-frequency drills** should attach to things Fighters already do—Attack, Dash, reactions, Opportunity Attacks, occasionally Ready.

**Situational combat drills** should make Dodge, Help, Search, Study, Hide, and Utilize *excellent when their circumstance arises*, without pretending they should replace an Attack action every round.

**Exploration/social drills** should deliver genuinely valuable information and fieldcraft outside combat. They do not need a damage rebate.

This is also more consistent with the optimizer evidence. Under 2014 rules, optimization sources such as Tabletop Builds treated Battle Master Crossbow Expert/Sharpshooter and Polearm Master/Great Weapon Master as benchmark Fighter damage packages; their melee guide explicitly notes the positional and defensive costs of melee optimization. citeturn6search0turn6search5turn6search7 In 2024, those exact baselines cannot simply be ported forward: Weapon Mastery fundamentally alters weapon selection, Sharpshooter no longer contains the old -5/+10 damage trade, and the Fighter chassis itself supplies considerably more tactical functionality. citeturn18view0turn19view0turn21search12turn22search12

Current optimizer discussion is less unanimous about a single “best Fighter” than 2014-era discussions were. Eldritch Knight is often identified as having the highest optimization ceiling because spellcasting and revised War Magic scale into the Fighter's attack routine, while Battle Master remains the most obvious benchmark for tactical flexibility. That should be treated as community sentiment rather than an official balance ranking. citeturn5search3turn8search0turn8search11

The Veteran therefore **does not need to win a white-room DPR race against Eldritch Knight**. A better target is:

> **roughly Champion-to-Battle-Master sustained personal damage, below the nastiest Eldritch Knight nova/optimization ceilings, with unusually good mundane tactical and exploration utility.**

That is a healthy and defensible subclass niche.

## Source Review and Rules Context

The most important distinction in the research is between **2014 optimization evidence**, which is useful for understanding martial incentives, and **2024 rules evidence**, which must govern the actual Veteran.

The official 2024 Fighter obtains Fighting Style, Second Wind, and three Weapon Masteries at level 1; Action Surge and Tactical Mind at 2; Extra Attack and Tactical Shift at 5; Tactical Master at 9; the third Attack-action attack at 11; Studied Attacks at 13; and the fourth Attack-action attack at 20. Fighter subclass features occur at 3, 7, 10, 15, and 18. citeturn15view0turn4view0turn4view1turn4view2turn4view3turn4view6

Several of those details are directly relevant to your drafts.

**Action Surge is deliberately constrained.** It gives another action on the Fighter's turn, but that action cannot be the Magic action; at level 17 the Fighter has two uses but can still use Action Surge only once on a turn. citeturn4view0 That makes any Veteran mechanic that turns “one attack” into a Magic action, or provides a Magic action “for free” when Action Surge is used, especially suspicious. It can indirectly defeat a restriction the base Fighter explicitly carries.

**Tactical Mind already makes Fighters much better at ability checks.** After failing an ability check, the Fighter can expend Second Wind to add 1d10, with the use preserved if the check still fails. citeturn4view0 Consequently, Veteran's Eye should mostly supply *access to specialized conclusions and military knowledge*, not another large generic numerical skill engine.

**Tactical Shift already occupies the “experienced Fighter disengages and repositions” niche.** Activating Second Wind as a Bonus Action lets the Fighter move up to half its Speed without provoking Opportunity Attacks. citeturn4view1 A Veteran Dash drill such as Break Contact should complement that feature rather than simply making Tactical Shift irrelevant.

**Tactical Master is particularly important.** At Fighter 9, when the Fighter attacks with a mastered weapon, they can replace that weapon's mastery for that attack with Push, Sap, or Slow. citeturn4view2 Iteration A's Applied Mastery instead allowed Push, Sap, or Slow *in addition to* whatever mastery had already been used. That is not a small subclass rider; it upgrades the base Fighter's central level 9 tactical feature from substitution to stacking.

**Studied Attacks also matters to drill design.** From Fighter 13, a missed attack gives advantage on the Fighter's next attack against that creature before the end of the next turn. citeturn4view3 Consequently, “Study the opponent to gain advantage on your next attack” is largely obsolete precisely when high-level Veteran drills should be getting more interesting.

The generic actions are now unusually well formalized in the 2024 Rules Glossary, which makes your core concept much more viable than it would have been in earlier 5e.

Help has two distinct uses. Ability-check Help requires the helper to possess the relevant skill or tool proficiency and be close enough to assist verbally or physically; attack Help requires distracting an enemy within 5 feet and gives the next allied attack advantage. citeturn12view0 Thus the old “Help an ability check from 30 feet” is not automatically meaningful—2024 already permits verbal assistance where reasonable—but extending **attack Help's enemy range** is a concrete rules benefit.

Hide is now quite constrained: normally DC 15 Dexterity (Stealth), while Heavily Obscured or behind Three-Quarters or Total Cover and outside enemies' lines of sight. Successful hiding gives the Invisible condition until one of the listed ending conditions occurs. citeturn12view1 A Veteran drill that allows hiding in substantially lighter concealment is therefore not a ribbon. It is a meaningful exception that can manufacture advantage and should be priced accordingly.

Influence is deliberately GM-mediated. The player urges a monster to do something; the GM decides whether it is willing, unwilling, or hesitant before a check is made. citeturn20view0 “Thousand-Yard Stare: hostile creature hesitates” should therefore not piggyback on Influence as a disguised combat condition unless you define a separate saving throw and explicit effect. Otherwise the drill blurs social adjudication and combat control.

The Magic action includes both casting suitable spells and activating features or magic items that require that action. citeturn12view3 This is why “Magic Item” is safer than “Magic,” but even magic-item activation varies wildly in value from item to item.

Ready is the most structurally dangerous generic action for an attack-replacement engine. A character taking Ready chooses a perceivable trigger and an action or movement to perform with their Reaction before the start of their next turn; a readied spell is actually cast when readied and requires Concentration while held. citeturn12view4 Meanwhile Fighter Extra Attack is tied to taking the Attack action on the Fighter's turn. citeturn4view1 Allowing “replace one attack with the Ready action” therefore nests an entire future action inside an Attack action. Even when ordinary off-turn Extra Attack does not apply, same-turn trigger edge cases and features that care about attacks “once per turn” become a rules minefield. It is a particularly poor primitive on which to build a subclass.

Search and Study are more promising. Search uses Wisdom and identifies things such as concealed creatures or objects, tracks, ailments, or states of mind depending on the skill; Study uses Intelligence for knowledge and deductions involving Arcana, History, Investigation, Nature, and Religion. citeturn12view5turn12view6 Those are excellent hooks for a battlefield veteran because they can produce valuable information without inventing a new minigame.

Utilize is also promising. The 2024 equipment rules now explicitly give many pieces of gear and tools Utilize functions; even donning or doffing a shield is a Utilize action. citeturn12view7turn19view1 A “Veteran knows how to use ordinary stuff better than most people” mechanic consequently has actual rules infrastructure behind it.

Opportunity Attacks remain Reactions made when a visible creature leaves reach using specified forms of movement. citeturn20view3 Reach weapons explicitly add 5 feet when determining the wielder's Opportunity Attack reach. citeturn19view0 Reactions normally refresh at the start of the character's turn, so a character ordinarily cannot simply react once on every creature's turn. citeturn12view4

The 2014 Cavalier's level 18 Vigilant Defender is important precedent because it *does* provide a special reaction on every creature's turn, but it is narrowly constrained: the special reaction is only for an Opportunity Attack, excludes the Cavalier's own turn, and cannot be used on the same turn as the Cavalier's normal reaction. citeturn22search2turn22search8 Your Iteration A capstone is materially broader because it grants ordinary Reactions every turn, supplies additional triggers for attacks, and then adds a 3d8 Tactical Blow to those off-turn hits. The existence of Cavalier therefore does not make the Veteran version safe; it demonstrates how carefully such a mechanic normally has to be fenced.

The weapon system further increases the importance of action-economy analysis. Greatsword and glaive both have Graze; longsword has Sap; pike has Push; longbow has Slow; shortsword has Vex; and scimitar has Nick. citeturn18view0turn18view2turn18view3 Graze deals the attack ability modifier on a miss, Nick moves the Light property's extra attack into the Attack action once per turn, Vex gives advantage on the next attack against a damaged target, Push moves a Large-or-smaller target up to 10 feet, Sap imposes disadvantage on its next attack, and Slow reduces Speed by 10 feet. citeturn19view0

That creates an important Veteran-specific balance issue: **Bonus Action Veteran Actions disproportionately favor Nick users**. The Light property normally spends the Bonus Action on its extra attack, but Nick moves that extra attack into the Attack action once per turn. citeturn18view7turn18view5 A shortsword/scimitar Fighter can therefore receive most of dual wielding's basic extra-attack benefit *and still have the Bonus Action free for a Veteran Action*, while Polearm Master, Dual Wielder, and Second Wind/Tactical Shift users face real Bonus Action competition.

The modern optimization literature reinforces several broader conclusions.

Tabletop Builds' 2014 “Basic Fighter” used a Battle Master with Crossbow Expert and Sharpshooter and explicitly treated it as a strong, consistent martial damage baseline; its melee counterpart used Polearm Master/Great Weapon Master and emphasized Precision Attack, Trip Attack, and the costs inherent to melee positioning. citeturn6search0turn6search7 The site's higher-optimization Flagship series did not select Fighter as one of its premier overall high-optimization classes, which is useful context: even an optimized 2014 Fighter's strength was primarily reliable weapon damage rather than being the game's universal optimization ceiling. citeturn6search14

Those 2014 numeric benchmarks are no longer directly portable. Current Sharpshooter's listed benefits are Bypass Cover, Firing in Melee, and Long Shots rather than the old power-attack damage mechanic, while current Great Weapon Master is built around Heavy Weapon Mastery and Hew. citeturn21search12 Polearm Master remains an action-economy feat with Pole Strike and Reactive Strike. citeturn21search5

For 2024 analysis, Treantmonk's Fighter damage series is one of the more useful public optimizer references because it explicitly separates baselines, sword-and-board, and great-weapon variants, while his newer baseline work attempts to standardize sustained-damage comparisons. citeturn9search2turn9search8 Community summaries of that methodology commonly describe four combats of four rounds with one Short Rest in the middle, and debates around his Fighter results demonstrate how materially Polearm Master, Great Weapon Master, encounter count, and resource assumptions change the ranking. citeturn8search4turn9search0turn9search12

That methodological disagreement is useful rather than inconvenient. Giant in the Playground discussions around similar DPR analyses have also cautioned that damage-in-a-vacuum misses control, positioning, survivability, and encounter structure. citeturn9search14 That is particularly important for the Veteran because its intended value proposition is explicitly **damage plus tactical utility**, not raw DPR alone.

Battle Master remains the closest subclass benchmark. The official 2024 Fighter update notes that Battle Master's level 15 Relentless now allows a free d8 in place of expending a normal Superiority Die for a maneuver once per turn. citeturn22search0 That means a high-level Veteran that obtains a broadly useful, no-resource tactical rider each turn is not inherently inappropriate—but it should be compared against roughly “a maneuver with a d8,” not “a free full Dodge plus 3d8 plus several reactions.”

Champion supplies the other useful extreme. Its Improved Critical makes attacks critical on a 19 or 20 from level 3. citeturn22search4 As the calculations below show, expanded critical range alone is a surprisingly modest DPR feature unless the build supplies additional on-crit or bonus-action synergies. Champion should consequently be treated as a **low-complexity floor**, not the maximum acceptable Veteran power.

Eldritch Knight is the upper tactical/damage ceiling. The 2024 revision loosened spell-school restrictions and revised War Magic/Improved War Magic. citeturn11search16turn22search12 Its design is especially relevant because even a spellcasting Fighter does not receive “replace one attack with any action”: War Magic is tightly scoped around inserting specific spellcasting into the Attack action. The narrower precedent is a strong argument against Iteration A's generic full-action replacement mechanic.

Psi Warrior provides a resource-based damage/defense/control comparison, while Rune Knight remains a useful **legacy 2014** comparison for a Fighter receiving broad nonmagical-looking battlefield control, defensive tools, and substantial Bonus Action/Reaction pressure. Rune Knight is not one of the four 2024 PHB Fighter subclasses and should not be treated as a 2024-native balance benchmark. citeturn22search12turn17search11

The broad optimizer takeaway is therefore not “Fighter must do X DPR.” It is:

> **2024 Fighter damage is extremely sensitive to weapon, mastery, feat, reaction, and resource assumptions; therefore the safest Veteran design is one whose utility mechanics do not themselves create additional scalable attack actions.**

## Benchmark Methodology

The following numbers are **my calculations**, not copied from an optimizer spreadsheet. Optimizer publications were used to choose meaningful archetypes and assumptions; official 2024 rules were used for the mechanics. This separation matters because published white-room DPR tables frequently disagree because of assumptions rather than arithmetic. citeturn9search0turn9search2turn9search12

**Target AC.** Rather than assign arbitrary monsters to each character level, I use a synthetic AC curve that preserves a 65% hit chance for an ordinary melee Fighter whose primary ability progresses from 16 to 18 at Fighter 4 and 20 at Fighter 6. This is a common style of optimization benchmark because it holds accuracy approximately constant while character bonuses increase.

| Fighter level | Attack ability | PB | Baseline attack bonus | Benchmark AC | Base hit chance |
|---:|---:|---:|---:|---:|---:|
| 3 | +3 | +2 | +5 | 13 | 65% |
| 5 | +4 | +3 | +7 | 15 | 65% |
| 7 | +5 | +3 | +8 | 16 | 65% |
| 10 | +5 | +4 | +9 | 17 | 65% |
| 11 | +5 | +4 | +9 | 17 | 65% |
| 15 | +5 | +5 | +10 | 18 | 65% before Studied Attacks |
| 18 | +5 | +6 | +11 | 19 | 65% before Studied Attacks |
| 20 | +5 | +6 | +11 | 19 | 65% before Studied Attacks |

Natural 1s and 20s are handled normally. Base critical chance is 5%. Advantage converts a 65% hit chance to 87.75% and a 5% critical chance to 9.75%.

For levels 13+, I model Studied Attacks instead of simply leaving accuracy at 65%. The feature says that after missing a creature, the Fighter has advantage on the next attack against it before the end of the next turn. citeturn4view3 Against the same durable target, this can be represented as a two-state sequence: normal attack or advantaged attack after a miss. At a 65% ordinary hit rate, the steady-state model produces approximately a **71.5% effective hit rate and 6.35% critical rate**. Actual combats will deviate because targets die, switch, become unreachable, or otherwise break the sequence.

The basic expected-damage equation is:

\[
D = p_h(W + M + B) + p_cW + p_mG
\]

where \(p_h\) is probability of a hit including criticals, \(p_c\) is critical probability, \(W\) is average weapon dice, \(M\) is ability/style flat damage, \(B\) is other on-hit damage, and \(G\) is miss damage such as Graze. Criticals add another set of weapon damage dice. Graze is modeled exactly as the mastery describes: ability-modifier damage after a miss, with that damage not further increased by other modifiers. citeturn19view0

The loadouts are:

| Archetype | Benchmark setup |
|---|---|
| Sword and shield | Longsword, Dueling, Sap |
| Two-handed | Greatsword, Great Weapon Fighting, Graze |
| Polearm | Glaive, Great Weapon Fighting, Graze |
| Ranged | Longbow, Archery, Slow |
| Two weapons | Shortsword/scimitar, Two-Weapon Fighting, Nick; baseline table deliberately does **not** monetize all possible Vex chains |
| Veteran unarmed | Iteration A's proposed 1d8 + Strength when holding neither weapon nor shield, from level 10 |

The official greatsword is 2d6/Graze, glaive 1d10/Graze, longsword 1d8/Sap, longbow 1d8/Slow, shortsword 1d6/Vex, and scimitar 1d6/Nick. citeturn18view0turn18view2turn18view3 Great Weapon Fighting treats a 1 or 2 on applicable melee weapon damage dice as 3; that gives a 2d6 greatsword an 8.0 expected weapon-dice result rather than 7.0. citeturn16search4

**Resource assumptions.** The main DPR tables are at-will and use no Action Surge, spell slot, Superiority Die, magic item, or external buff. A separate nova column uses one Action Surge. This is intentionally more informative for homebrew design than averaging every resource over a hypothetical adventuring day.

For contextualizing resource subclasses, the report uses the common optimizer sensitivity model of roughly four rounds per encounter, four encounters, and one Short Rest as a reference point—but not as a statement that real campaigns universally work that way. That convention is documented in discussion around Treantmonk's 2024 calculations and is itself a source of optimizer debate. citeturn8search4turn9search12

**Action Surge.** It adds another Attack action in the nova table. It does not grant another Bonus Action, and Nick can supply its extra Light attack only once per turn. citeturn4view0turn18view5

**Optimized feat assumptions.** For the deliberately aggressive builds:

- Greatsword takes Great Weapon Master at 4.
- Polearm takes Polearm Master at 4 and Great Weapon Master at 6, reaching Strength 20 at 8.
- Dual-wield takes Dual Wielder at 4 and reaches Dexterity 20 at 6; the model conservatively does not optimize every Vex/equip sequence.
- Ranged takes Sharpshooter at 4, Great Weapon Master at 6 where legal for the Heavy longbow, and reaches Dexterity 20 at 8. Current Sharpshooter is primarily a range/cover feat rather than the old 2014 damage feat, while longbows have the Heavy property. citeturn21search12turn18view2

For Great Weapon Master calculations I assume its Heavy Weapon Mastery damage applies to qualifying hits made as part of the Attack action. I **exclude Hew's bonus attack** from the main table, making the values conservative when a crit or kill would trigger it. The current D&D Beyond entry identifies Heavy Weapon Mastery and Hew as GWM's current benefits. citeturn21search12

**Magic items and buffs.** No magic weapon is assumed in the principal tables. To show sensitivity, I separately model a +1 weapon, permanent Advantage, and a Bless-like +1d4 attack bonus. Since Veteran magic-item drills would interact with the *properties and activation economy of particular items*, not simply a +1 weapon, those have to be stress-tested item-by-item rather than folded into a universal DPR number. Magic item activation can use the Magic action where an item says so. citeturn12view3turn16search13

The largest uncertainty is not the arithmetic. It is **encounter access**: whether the Fighter can remain in melee, whether a Polearm Master reaction triggers, whether a target is already Bloodied, whether a readied trigger occurs, whether cover exists, whether a second enemy is available for Cleave, and how often external Advantage is supplied. Any homebrew whose DPR depends heavily on those conditions should be evaluated as a range, not a single number.

## Comparison to Fighter Baselines

The first table is subclass-neutral Fighter chassis damage. These values already include the relevant Fighting Style and damage-producing mastery but no subclass damage, feats, magic items, or Action Surge.

| Level | AC | Sword + shield | Greatsword | Glaive | Longbow | Two weapons + Nick* | Veteran d8 unarmed |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 13 | 6.4 | 8.6 | 7.1 | 5.9 | 8.8 | — |
| 5 | 15 | 14.1 | 19.2 | 16.1 | 13.2 | 15.2 | — |
| 7 | 16 | 15.4 | 21.2 | 18.1 | 14.7 | 17.1 | — |
| 10 | 17 | 15.4 | 21.2 | 18.1 | 14.7 | 17.1 | 12.8 |
| 11 | 17 | 23.1 | 31.8 | 27.2 | 22.1 | 22.8 | 19.2 |
| 15 | 18 | 25.5 | 33.7 | 28.5 | 23.3 | 25.2 | 21.2 |
| 18 | 19 | 25.5 | 33.7 | 28.5 | 23.3 | 25.2 | 21.2 |
| 20 | 19 | 34.0 | 44.9 | 38.1 | 31.1 | 31.5 | 28.3 |

\*The two-weapon line is intentionally conservative because it counts Nick's additional attack but not the full optimization value of Vex advantage chains.

The first important finding is how severe the Attack-action opportunity cost becomes. At level 5 the greatsword Fighter's whole at-will Attack action is worth about **19.2 DPR** in this model. At level 11 it is **31.8**, and at level 20 it is **44.9**. A full-action Veteran Study therefore cannot be made broadly competitive simply by adding a d8. If you try, the necessary compensating damage becomes increasingly absurd.

Weapon Mastery also makes raw attack replacement more expensive than “weapon die + ability” suggests. Greatsword and glaive still deal their Strength modifier through Graze when they miss. citeturn19view0 Replacing a greatsword attack therefore sacrifices an unusually reliable packet of damage.

The optimized comparison makes the scaling pressure clearer:

| Level | GWM greatsword | With Surge | PAM/GWM reach | With Surge | Dual Wielder* | With Surge | Ranged heavy build | With Surge |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 8.6 | 17.2 | 7.1 | 14.1 | 8.8 | 13.2 | 5.9 | 11.7 |
| 5 | 23.1 | 46.2 | 22.4 | 38.5 | 20.2 | 30.3 | 13.2 | 26.4 |
| 7 | 25.1 | 50.2 | 25.3 | 44.4 | 22.8 | 34.2 | 16.5 | 33.1 |
| 10 | 26.4 | 52.8 | 30.6 | 53.9 | 22.8 | 34.2 | 20.7 | 41.4 |
| 11 | 39.6 | 79.2 | 42.3 | 77.2 | 28.5 | 45.6 | 31.0 | 62.1 |
| 15 | 44.4 | 88.8 | 46.8 | 86.1 | 31.5 | 50.4 | 35.2 | 70.3 |
| 18 | 46.5 | 93.1 | 48.9 | 90.4 | 31.5 | 50.4 | 37.5 | 75.0 |
| 20 | 62.1 | 124.1 | 62.7 | 118.0 | 37.8 | 63.0 | 50.0 | 100.1 |

\*Again conservative on Vex sequencing. Hew's conditional bonus attack is omitted from the GWM numbers.

These should not be read as “the correct 2024 Fighter DPR.” They illustrate the range the Veteran has to survive. Current optimizer discussions reach substantially different Fighter results depending on whether PAM is included, how GWM is used, how many encounters occur, and what accuracy assumptions are chosen. One 2024 Reddit recalculation of a Treantmonk build, for example, found substantially greater output after introducing PAM/GWM under the poster's otherwise matching assumptions. citeturn9search0

The fact that the optimized level 11 greatsword line rises from a 31.8 chassis baseline to about 39.6 also explains why a Veteran feature that adds “only” 1d8 every round should not be dismissed as small. Permanent, resource-free damage stacks on top of already-efficient feat packages.

Accuracy buffs demonstrate similar sensitivity:

| Greatsword level | Baseline | Permanent Advantage | Bless-like +1d4 to hit | +1 weapon |
|---:|---:|---:|---:|---:|
| 5 | 19.2 | 23.6 | 21.2 | 21.4 |
| 11 | 31.8 | 38.4 | 34.8 | 35.1 |
| 15 | 33.7 | 38.4 | 35.8 | 36.8 |
| 18 | 33.7 | 38.4 | 35.8 | 36.8 |
| 20 | 44.9 | 51.2 | 47.7 | 49.1 |

The smaller high-level advantage increase reflects Studied Attacks already supplying some advantage after misses. citeturn4view3 This is another argument against a Veteran Study drill whose primary payoff is advantage on the Veteran's next attack: the chassis increasingly self-supplies it.

**Champion comparison.** Expanded critical range sounds larger than it is. In this model, with a no-feat greatsword, changing only the crit range from 20 to 19–20 increases DPR by approximately 0.4 at level 3, 0.8 at level 5, 1.2 at level 11, and about 2.0 at level 20. Champion's broader package matters, and GWM/Hew gives additional crits more economic value, but Improved Critical by itself is not an appropriate “maximum acceptable damage subclass” benchmark. The official feature does indeed move the critical range to 19–20 at Fighter 3. citeturn22search4

**Battle Master comparison.** This is more useful for Veteran. Maneuvers can convert limited resources into damage *plus* control or support, and 2024 Relentless eventually permits a free d8 maneuver once per turn at level 15. citeturn22search0 A level 15 Veteran receiving a useful no-resource tactical effect plus something around one d8 of damage is therefore plausible. A level 15 Veteran receiving two generic actions, potentially 2d8 or 4d8 depending on ambiguous Tactical Blow stacking, double masteries, and expanded reactions is not.

Battle Master also illustrates an identity danger. Optimizer and player discussions continue to praise it specifically for tactical versatility, while Eldritch Knight is frequently singled out for the higher optimization ceiling. citeturn5search3turn8search11 The Veteran therefore should not compete with Battle Master by creating even more “attack maneuver” riders. It needs a different center of gravity: **actions other Fighters rarely specialize in, battlefield information, gear, preparedness, and survival**.

**Eldritch Knight comparison.** The 2024 revision is a valuable control case because it intentionally integrates magic into Extra Attack while keeping the exchange tightly scoped. citeturn11search16turn22search12 If the magical Fighter's attack replacement has careful constraints, a mundane subclass should not be allowed to exchange a single attack for arbitrary Ready/Magic/Dodge actions on the theory that mundane actions are automatically weaker.

**Psi Warrior comparison.** Psi Warrior has a limited pool supporting offense, defense, and movement/control, which is a better philosophical benchmark for Veteran than Champion: a subclass can provide several tactical functions so long as its most efficient effects are gated and do not all stack into the same round. The 2024 PHB imported Psi Warrior from Tasha's with relatively limited revision. citeturn22search12

**Rune Knight comparison.** Legacy Rune Knight is especially useful for action-economy review because its runes, Giant's Might, and defensive reactions produce real Bonus Action/Reaction congestion; D&D Beyond's Rune Knight guide explicitly notes that many runes occupy those economies and discusses Sentinel as a control option. citeturn17search11turn22search15 That demonstrates a healthy principle: a versatile Fighter subclass does not need to access all of its good features simultaneously.

**Other martial ceiling.** Current optimizer discussions do not consistently place Fighter at the universal top of sustained martial damage; Berserker great-weapon builds, for example, repeatedly appear in community discussions of high 2024 martial DPR. citeturn5search23 The Veteran has no reason to out-damage those builds while also out-utilitying them.

The desired balance position should therefore be approximately:

> **At will:** Fighter chassis + modest subclass DPR, usually 2–5 DPR in tiers 1–2 and perhaps 4–8 in tiers 3–4 when its conditions are met.

> **Nova:** normal Fighter Action Surge scaling, without a subclass mechanic that multiplies the number of full Attack actions or reactions.

> **Compensation:** Veteran receives more battlefield-information, support, action diversity, and mundane utility than Champion and ideally a different kind of versatility from Battle Master.

Those ranges are design recommendations, not official thresholds.

## Iteration A Critique

Iteration A contains several excellent individual concepts wrapped in an engine that is fundamentally unstable.

Its strongest idea is the **fiction-to-mechanics connection**: the Fighter is not gaining supernatural powers or commands; experience teaches them when ordinary actions are useful. Veteran's Eye, practical Help, vigilance, improvised weapons, and battlefield observation all reinforce that identity. The core idea deserves preservation.

The attack-replacement mechanic does not.

The first problem is **level scaling**. The opportunity cost of “replace one attack” changes whenever Fighter gains another attack. Before Extra Attack, replacing the only attack means sacrificing the entire Attack action's damage. At level 5 it sacrifices half the Attack action; at 11 one third; at 20 one quarter. The exact same Veteran Action consequently changes value dramatically without its own text changing.

Tactical Blow was an understandable attempt to solve this, but its numbers expose why the architecture fights itself.

Under the benchmark assumptions above, replacing one attack with a Veteran Action and then applying Tactical Blow to the remaining attacks changes no-feat damage approximately as follows:

| Level | Tactical Blow | Sword-and-board net DPR | Greatsword net DPR |
|---:|---:|---:|---:|
| 5 | 1d8 | **−3.9** | **−6.5** |
| 11 | 1d8 | **−3.5** | **−6.4** |
| 15 | 2d8 | **+0.5** | **−2.2** |
| 18 | 3d8 | **+5.0** | **+2.3** |
| 20 | 3d8 | **+5.9** | **+3.1** |

The table assumes a viable hit remains after the replacement and does not count the utility value of the Veteran Action. It demonstrates the core structural problem: **a Tactical Blow large enough to make attack replacement feel acceptable for a greatsword Fighter becomes bonus damage for builds whose sacrificed attack was weaker.**

The Bonus Action version swings to the opposite extreme. If a Veteran Action can be used as a Bonus Action while the Fighter retains all of their attacks, the expected Tactical Blow contribution alone is approximately:

| Fighter level | Tactical Blow contribution if full Attack remains |
|---:|---:|
| 3 | +3.2 DPR |
| 5 | +4.3 |
| 11 | +4.6 |
| 15 | +9.6 |
| 18 | +14.4 |
| 20 | +14.6 |

These values already account approximately for the chance of landing the rider and for criticals. They do **not** assign any value to Dash, Help, Search, Study, Dodge, or another Veteran Action itself.

At level 15, therefore, a Bonus Action Veteran Action can be providing roughly ten expected damage per round *plus a generic action's utility*. Battle Master's level 15 at-will Relentless benchmark is a free d8 maneuver once per turn. citeturn22search0 The Veteran package is too generous unless the Veteran Action itself is extremely minor.

It is also uneven across weapon styles. Nick allows the Light extra attack to move into the Attack action once per turn. citeturn18view5 A Nick Fighter can therefore retain the core dual-wield extra attack while spending their Bonus Action on Veteran Actions. A Polearm Master or enhanced dual-wield build wants its Bonus Action for another weapon attack, while Second Wind and Tactical Shift also consume the Bonus Action. citeturn15view0turn21search5 The engine inadvertently makes **Nick one of the best Veteran synergies** even though there is no obvious fantasy reason the old soldier should disproportionately favor scimitars.

The level 3 wording has another problem: **timing ambiguity**. “When you take the Attack action, you can take a Veteran Action as a Bonus Action; after taking that Veteran Action, the next hit before the end of the turn gains Tactical Blow” invites questions about whether the Bonus Action can be inserted before the one level-3 attack, after declaring the Attack action but before resolving the attack. A core subclass feature should not require that kind of action-sequencing debate.

**Ready should never be an attack-replacement Veteran Action.** Ready is itself an action that stores another action or movement for a later trigger, using a Reaction. citeturn12view4 Putting Ready inside an Attack action creates nested action structures. Ordinary off-turn readied Attack actions do not reproduce the Fighter's on-turn Extra Attack progression, but same-turn trigger constructions create enough ambiguity that the feature invites recursive and timing exploits. Even without a literal infinite loop, trading one attack for “prepare another whole action” is an unnecessarily dangerous rules primitive.

If you want a Veteran to be good at Ready, write:

> “When you take the Ready action and choose one weapon attack as the action you will take…”

and then improve that **specific readied attack**.

Do not write:

> “Replace one attack with the Ready action.”

**Magic has the same problem, amplified by the Fighter's own design.** The Magic action covers both spellcasting and certain magic-item activations, while Action Surge expressly cannot provide the Magic action. citeturn12view3turn4view0 If Veteran can convert one attack into a Magic action—or the level 18 “free Veteran Action” can be Magic—then the subclass can indirectly bypass a restriction that Wizards of the Coast put directly into Action Surge. Restricting it to magic items reduces multiclass abuse but does not solve the action-conversion problem: some magic-item activations are considerably more valuable than one weapon attack.

**Dodge at level 18 is worse.** Dodge gives attacks against the character disadvantage while visible and gives advantage on Dexterity saves until the start of the character's next turn. citeturn20view1 A capstone saying “once per turn, take a Veteran Action for free as part of Attack,” when Dodge is a Veteran Action, is effectively:

> full Fighter Attack action **plus full Dodge every round**.

That is an enormous defense increase with no resource cost and should not survive revision.

**Applied Mastery should be removed.** At Fighter 9, Tactical Master already allows replacing a weapon's mastery with Push, Sap, or Slow for an attack. citeturn4view2 Applied Mastery instead lets the Veteran retain the original mastery and bolt another mastery onto the hit. With weapons such as shortsword/scimitar or pike this can create Vex + Push, Nick weapon interactions plus Sap/Slow, or other two-mastery packages. The subclass is not merely “using Tactical Master well”; it is upgrading Tactical Master beyond the base feature.

It becomes stranger with Unarmed Strikes. Under 2024 rules, an Unarmed Strike is a separate system that can deal damage, Grapple, or Shove; its ordinary damage is 1 + Strength modifier. citeturn20view3 Weapon Masteries, by contrast, belong to weapons. citeturn19view0 Letting the Veteran impose weapon-mastery properties on unarmed attacks opens combinations with Grappler and other unarmed features that were never built around masteries.

The proposed level 10 unarmed and improvised improvements **by themselves are not alarming**. Ordinary improvised weapons lack proficiency and deal 1d4 unless the DM treats the object as an equivalent normal weapon. citeturn20view0 Proficiency plus d6/d8 makes improvised fighting usable without making a level 10 Fighter's unarmed DPR remotely competitive with a strong greatsword routine. In the model, d8 unarmed attacks at level 11 produce roughly 19.2 DPR versus 31.8 from an unfeated greatsword. The problem is not the d8. The problem is piling free control masteries and feat interactions on top of it.

**Vigilant Response is one of A's more salvageable combat features.** A reaction attack after a creature in reach misses the Veteran or attacks somebody else gives the front-line soldier a good “you left an opening” identity. But it needs to be distinguished carefully from Sentinel-like reaction territory and probably should not itself be formally labeled an Opportunity Attack unless you intentionally want every Opportunity-Attack rider to apply. Current reaction feats are already an important martial optimization space. citeturn21search5turn22search8

“No Motion Wasted” is too close to simply absorbing Sentinel's core identity. The pair “Disengage does not protect you” plus “your Opportunity Attack sets Speed to 0” is premium lockdown functionality. Disengage normally prevents Opportunity Attacks from movement for the rest of the turn. citeturn20view2 Giving both pieces in one subclass feature saves the Veteran a high-value feat selection and makes a Sentinel-taking Veteran either redundant or awkward.

The level 18 reaction capstone is the most serious problem in the entire draft.

Using the level 18 greatsword assumptions above, a normal off-turn greatsword attack is worth roughly **11.2 expected damage**. A 3d8 Tactical Blow on that single reaction attack contributes about another **10.5 expected damage** once hit and critical probabilities are included. So each qualifying reaction is worth about **21.7 expected damage**.

That means:

| Qualifying off-turn reactions in a round | Approx. added expected damage |
|---:|---:|
| 1 | 21.7 |
| 2 | 43.5 |
| 3 | 65.2 |
| 4 | 86.9 |

That is **in addition to the Veteran's own-turn attacks**.

Those extra reactions are encounter-dependent, of course. But that is precisely the problem: the feature's ceiling scales with enemy count and turn count rather than with the Veteran's level or a fixed resource.

Legacy Cavalier's Vigilant Defender demonstrates that “special reaction every turn” can exist, but Cavalier carefully limits those special reactions to Opportunity Attacks, excludes the Cavalier's own turn, and prevents combining a special and normal reaction on the same turn. citeturn22search2turn22search8 Veteran A combines the broader reaction permission with **more attack triggers and a 3d8 once-each-turn damage rider**. That package is dramatically more combustible.

It is also a multiclass problem. Features whose damage limits say “once on each turn” rather than “once on each of your turns” are famously valuable on reaction attacks. A Rogue/Fighter combination, for example, is inherently interested in getting attacks on another creature's turn because Sneak Attack is organized by turn rather than round; the 2024 Rogue remains built around Sneak Attack as its central damage feature. citeturn15view0 Ready and reaction engines should therefore be evaluated in **party DPR and multiclass DPR**, not merely Veteran DPR.

**Veteran's Eye is the opposite case: keep it.** Its military-history advantage is narrow enough to be flavorful, while the one-minute observation feature gives the subclass an actual exploration identity. The only required change is to reduce the GM's interpretive burden.

I would rewrite its second half into a question structure such as:

> After examining a battlefield, fortification, campsite, road, vehicle, weapon, suit of armor, or similar military subject for at least 1 minute, you can ask the GM one of the following questions about it:
>
> **Where is the strongest defensible position?**
>
> **What is the most likely route of approach, escape, or ambush?**
>
> **What appears damaged, poorly constructed, tampered with, or incomplete?**
>
> **What detail reveals how this was used or what happened here?**

Then specify that the character normally cannot gain another answer from the same subject until circumstances materially change.

That is easier to adjudicate than “the GM gives a useful detail” and strongly expresses veteran expertise without making the character a magical diviner.

**Verdict on Iteration A: abandon the action engine, not the subclass.** Salvage Veteran's Eye, improvised fighting, practical Help, vigilance, some Ready/OA concepts, and possibly the *notion* of a tactical damage rider. Remove the attack-replacement framework, free full actions, double mastery, escalating per-turn reaction damage, and generic “Magic action as a Fighter attack” language.

## Iteration B Critique

Iteration B fixes a genuine presentation problem but not the underlying mechanical one.

Turning the features into selectable Veteran Tactics has three clear advantages.

First, it stops the level 3 feature from becoming an enormous paragraph defining six actions plus several exceptions.

Second, it creates build differentiation. A field scout can learn Search/Hide/Ready options while a trench-fighter learns Help/OA/Dodge options.

Third, prerequisites let the strongest generic actions remain inaccessible until later levels. That is good design. Ready, magic-item activation, and Dodge are not equivalent to Search or basic Help and should not automatically enter the subclass at the same level.

This is very similar to why Battle Master maneuvers remain readable despite having a large option pool. The player learns a subset, and the individual maneuver contains its own trigger. Battle Master remains a major 2024 tactical benchmark, with four new maneuvers and several revised maneuvers in the 2024 PHB. citeturn22search12

But **Iteration B still uses the A engine**, so the most serious problems remain:

the action is still being inserted into/replaced inside Attack;

Ready still nests an action;

Bonus Action competition is still build-dependent;

Tactical Blow still turns utility use into escalating DPR;

Magic Item still potentially converts an attack into an activation that the base Fighter cannot obtain through Action Surge;

and high-level multi-action/multi-reaction scaling remains difficult to price.

In other words, B improves **content organization**, not **rules architecture**.

The proposed 4 / 6 / 8 / 10 / all progression is also too generous if the final menu resembles your current list.

At four tactics, a player has a manageable identity. At eight to ten, especially when each action category has multiple choices, the Fighter starts carrying a small spellbook of situational exceptions. At “all tactics” the level 18 character loses much of the differentiation the menu was supposed to create and gains a substantial scanning burden every turn.

That is not merely a complexity concern. **Breadth is power.** A character that always has the perfect niche answer does not need each individual tactic to be numerically exceptional.

I would use approximately:

| Fighter level | Drills known |
|---:|---:|
| 3 | 4 |
| 7 | 5 |
| 10 | 6 |
| 15 | 7 |
| 18 | 8 |

If the final menu contains only 10–12 total, 4 / 5 / 6 / 7 / 8 is generous. If the menu contains 20+, it is even more important not to reach “all.”

I would also allow **one known drill to be replaced whenever a Fighter level is gained**. At level 15, a Veteran-flavored adaptability feature could perhaps allow one drill to be changed after a Long Rest, representing the old soldier preparing for the next job. That is a better expression of “hundred fights of experience” than simply knowing every printed button.

Calling them **Drills** is preferable to Tactics. “Tactics” places the subclass linguistically next to Battle Master and officer/commander fantasies. “Drill” communicates repeated, practiced procedure: how to advance under fire, clear a room, inspect a wall, cover a retreat, brace a doorway, or use whatever object is at hand.

For D&D Beyond presentation, B and C are both preferable to A. D&D Beyond supports homebrew character content and character-sheet presentation, but the more a feature depends on manually rewriting how Extra Attack is subdivided into other full actions, the more of its operation necessarily becomes player-managed rather than a simple selectable feature entry. D&D Beyond's own homebrew guidance emphasizes building homebrew from recognizable rules language and existing design pieces. citeturn17search14 The exact automation available for a custom subclass can change, so I would not make platform automation a hard design requirement; nevertheless, discrete “When you take the X action…” entries are inherently easier for a character sheet to communicate than a global nested-action engine.

**Verdict on Iteration B: keep the menu concept; discard the Veteran Action engine underneath it.**

That leads directly to Iteration C.

## Iteration C Critique

Iteration C is the best direction because the rules become **local rather than global**.

Instead of teaching the player:

> “Here is a special subsystem for converting an Attack action into six other actions under three different timing rules depending on Fighter level…”

you can teach:

> **Forced March. When you take the Dash action…**

> **Threat Scan. When you take the Search action…**

> **Braced Shot. When you take the Ready action and ready one weapon attack…**

That is easier to read, easier to adjudicate, much easier to balance individually, and much less likely to produce unforeseen action nesting.

The major criticism of C is that **the current menu is still much too large**. You have roughly five candidates under eleven action/reaction categories. If even half survive, the subclass will contain more individual rules elements than it needs.

The right next pass is therefore not “write all fifty drills.” It is **identify approximately twelve excellent drills that collectively touch every desired part of the action system**.

The actions do not need equal representation.

| Category | Assessment | Best direction |
|---|---|---|
| Attack | Useful but dangerous identity overlap | Keep only 1–2 options; avoid generic Battle Master riders |
| Dash | **Excellent** | Mobility, terrain, escorting allies, advancing under fire |
| Dodge | Good high-level option | Holding ground, protecting adjacent ally, counterguard |
| Help | **Excellent** | Practical assistance, repositioning, extended attack Help |
| Hide | Conditional | Do not casually bypass 2024 Hide prerequisites |
| Influence | Good OOC | Soldier-to-soldier credibility, not mind control |
| Magic Action | **Weakest category** | Cut or reduce to one magic-item-only advanced drill |
| Ready | **Excellent if tightly scoped** | Enhance readied weapon attack/Help, never replace attack with Ready |
| Search | **Excellent** | Hidden attackers, threats, battlefield sweep |
| Study | **Excellent** | Qualitative enemy/fortification appraisal |
| Utilize | **Excellent** | Sabotage, barricades, mundane gear |
| Opportunity Attack | Good but feat-sensitive | Unique repositioning rather than duplicating Sentinel |

The **Attack drills are presently the least conceptually necessary**. The Fighter already has Weapon Mastery and Tactical Master, and Battle Master already owns the broad “my weapon attack carries a tactical maneuver” space. citeturn15view0turn4view2turn22search0

“Suppressing Attack” is especially problematic if it gives disadvantage on attacks against allies: Sap already imposes disadvantage on a target's next attack, and Tactical Master can select Sap. citeturn19view0turn4view2

“Break Formation: move 5 feet” is simply a weaker Push, another Tactical Master option.

“Pattern Recognition: bonus/advantage on next attack” runs into Studied Attacks.

A Veteran Attack drill needs to do something **orthogonal** to Weapon Mastery. “Finish the Wounded” is the cleanest of your candidates because Bloodied is now an official 2024 term for a creature at half its Hit Points or fewer. citeturn20view3 A modest once-per-turn damage bonus against a Bloodied target is easy to remember, highly Veteran-flavored, and does not require manufacturing a new control condition.

I would be cautious even there because it can become the subclass's automatic DPR drill. That may be acceptable if the subclass needs a simple damage baseline.

**Dash drills are among the strongest design space.** Forced March and Shielded Advance make Dash a genuine “advance under pressure” action. Difficult Terrain normally costs one additional foot per foot moved. citeturn20view2 Ignoring nonmagical Difficult Terrain while Dashing is therefore concrete without being equivalent to flight or teleportation.

Break Contact is less appealing because Tactical Shift already provides no-Opportunity-Attack repositioning with Second Wind. citeturn4view1 It needs a different identity—perhaps one enemy loses the ability to react to *your passage* only after you have attacked it, rather than merely recreating Disengage.

Drag to Cover is exceptionally thematic, but do not literally use unrestricted grapple-dragging language. Grappled movement normally costs additional movement unless the target is Tiny or at least two sizes smaller. citeturn20view3 For a willing ally, a fixed effect such as “one willing creature within 5 feet can move up to 10 feet with you without provoking from one creature you choose” will be cleaner than a miniature carrying simulation.

**Dodge drills can be strong because Dodge already charges the enormous price of the Fighter's full action.** Dodge imposes disadvantage on visible attackers and gives advantage on Dexterity saves until the next turn. citeturn20view1 “Hold Ground”—advantage/resistance against being shoved, moved, or knocked Prone—is both thematic and narrow.

“Dug In” granting temporary HP is workable if the amount is modest because temporary HP do not turn Dodge into damage; however, avoid an amount that scales so aggressively that the Veteran becomes correct to Dodge every round.

“Counterguard” is more interesting but considerably stronger. Dodge manufactures misses, so “when an attacker misses you while Dodging, make an attack” converts defense directly back into offense. One reaction per round keeps this tolerable; pairing it with an eventual extra-reaction capstone requires renewed testing.

“Shield the Line” granting an adjacent ally Half Cover is one of the strongest conceptual support options. It makes the Veteran protect people through positioning rather than commands.

**Help is almost ideal Veteran territory.** Attack Help normally requires the enemy to be within 5 feet. citeturn12view0 Extending that to 10 or 15 feet is a clean front-line benefit. Allowing the helped ally a small safe step is also useful.

Avoid “Veteran's Correction” if it means Help gives advantage **and** a reroll **and/or** an additive die. Help is already a strong roll-modifier action; stacking multiple forms of reliability makes its value difficult to price.

“Hard-Earned Advice” should not grant something described as a “proficiency-style bonus.” Expertise/proficiency math is an important class-identity space, and Tactical Mind already supplies the Fighter with a powerful failed-check rescue. citeturn4view0 The Veteran's contribution should be situational expertise, not generic numerical supremacy.

**Hide needs restraint.** The 2024 Hide action deliberately requires meaningful concealment/cover and a DC 15 check. citeturn12view1 “Combat Concealment” that permits hiding in Light Obscurement substantially rewrites those conditions and can become an easy advantage engine, especially on a Fighter making three or four attacks.

“Vanish in the Chaos” is safer: **after succeeding** on a normal Hide action, move 5 or 10 feet without immediately revealing yourself, subject to the ordinary ending conditions. That improves fieldcraft without rewriting what counts as hiding.

“Quiet Hands” is also excellent: doing something mundane while remaining hidden is a flavorful infiltration ribbon and unlikely to challenge Rogue unless it begins granting Rogue-like Bonus Action Hide.

**Influence should stay human-scale.** The Influence action already depends heavily on the monster's desires and the GM's assessment. citeturn20view0 “Common Soldier's Tongue”—advantage or another modest benefit when dealing with guards, soldiers, mercenaries, caravan workers, laborers, camp followers, and similar people in practical matters—is thematically excellent.

“Barracks Authority” can work if narrowly worded, but routinely replacing Charisma with Constitution for persuasion is conceptually dubious. Constitution represents endurance, not interpersonal skill. A Strength-based Intimidation check may be situationally logical, but 5e already permits the GM to associate abilities and skills where appropriate; the subclass need not create “social Constitution.”

“Thousand-Yard Stare” should be cut unless it becomes a separate combat feature with a save. Influence is not a fear/condition delivery action.

“Command Without Rank” is thematically risky for a different reason: the user's stated fantasy explicitly is **not an officer**. Practical Help and shouted warnings fit. Repeatedly issuing mechanically rewarded commands pulls the subclass toward Warlord/Banneret territory.

**Magic Action drills are the least healthy part of C.** Field Activation—drawing or stowing an item as part of its activation—is harmless but underwhelming. “Combat Use: move while activating” is largely redundant because characters can normally split their movement around their action unless a rule says otherwise. “Jury-Rigged Timing” adds unrelated movement/temp HP to arbitrary magic-item effects, which makes the item's existing power determine the drill's value. “Emergency Trigger” is the most dangerous because changing an action-based defensive magic item into a Reaction can dramatically alter an item's intended economy.

More importantly, the Fighter's own Action Surge cannot take the Magic action. citeturn4view0 That is a strong reason not to make “I use Magic unusually quickly” a central mundane Veteran competency.

My recommendation is **remove Magic Action as a full drill family**. If the magic-item fantasy matters, make one level-10+ drill:

> **Field Activation.** When you take the Magic action to activate a magic item, you can draw that item as part of the action, and your movement before or after the activation doesn't provoke Opportunity Attacks from one creature you can see.

Even that should be playtested with actual item lists.

**Ready is excellent when it modifies Ready instead of replacing an attack with it.** “Hair Trigger” and “Braced Reaction” are particularly good.

A clean pattern would be:

> When you take the Ready action and ready one weapon attack, choose one benefit…

Then give the attack something modest such as extra damage, Slow, or the ability to stop a creature's movement under a specific trigger.

Do not let the Veteran ready the entire Attack action more efficiently than other characters.

“Contingency Veteran” has a good fantasy—experienced soldiers do not waste preparation—but “if the trigger fails, take Search or Study for free” creates another weird off-turn full-action grant. Better:

> If your readied trigger has not occurred when the Ready effect ends, you gain advantage on one Search or Study check before the end of your next turn.

That preserves the idea without awarding a phantom action.

**Search is probably the best unexplored combat-support category.** “Spot the Shooter: use your Reaction to Search for a creature that just attacked while hidden” is excellent. Search already formally covers concealed creatures through Perception. citeturn12view5

Threat Scan can be useful if it produces a bounded effect such as:

> A creature you detect with this Search cannot gain advantage against you solely from being hidden until the start of your next turn.

Do not simply say “the creature cannot hide,” which overrides too many possible concealment abilities.

Read the Ground is extremely on-theme as an exploration enhancement and helps distinguish Veteran from Battle Master.

**Study is equally promising**, but avoid exact-stat-block extraction. A “Size Up” drill that asks “What is its exact AC? Exact current HP? Which saving throw is lowest?” pushes the GM toward exposing game data and can slow every new-monster encounter.

Qualitative information is better:

> Is it Bloodied?

> Does its armor/stance suggest unusually strong physical defense?

> Has it shown a repeated fighting pattern?

> Does it appear prepared to flee, charge, defend, or use a particular weapon?

For objects and fortifications, Veteran Appraisal is outstanding. The Study action already uses Investigation and History for traps/gadgets, wars, and related knowledge. citeturn12view6 Let the Veteran learn which section looks weakest, recently repaired, load-bearing, improvised, or poorly maintained.

That may be the most distinctive noncombat ability in the whole subclass.

**Utilize should be a cornerstone.** The 2024 rules contain far more explicit tool and object uses than older 5e, including Strength-based Smith's Tools for prying open objects and numerous other defined Utilize functions. citeturn16search12

“Sabotage” is excellent: advantage on an appropriate check to wedge, jam, disable, cut, tangle, or obstruct a mundane mechanism or piece of battlefield equipment.

“Quick Barricade” is also excellent if closed-form. For example:

> Using suitable unsecured objects within reach, you create Half Cover in one 5-foot space adjacent to you. The barricade is an object whose AC and Hit Points are determined by its material.

The official rules already provide object AC and HP guidance, which makes this unusually supportable mechanically. citeturn20view3

“Dirty Trick” in its current open-ended form is dangerous. “Use debris, a cloak, sand, rope, torch, etc. to impose disadvantage/prevent reactions/reduce speed” is nearly a blank check. Players will continuously negotiate whether whatever is nearby qualifies and which status it causes.

That can work only with a **closed menu**, such as:

> **Obscure:** target has disadvantage on its next Wisdom (Perception) check before your next turn.

> **Tangle:** reduce Speed by 10 feet until your next turn.

> **Distract:** target cannot make an Opportunity Attack against you before your next turn.

Even then, include an object requirement and perhaps an attack/check/save.

**Opportunity Attack drills require feat discipline.** “Stop Them Cold” and “Punish Disengage” live directly in Sentinel's traditional design space; current martial feat options continue to place Sentinel, Polearm Master, and Shield Master among dedicated control packages. citeturn21search5turn21search12 Giving both Sentinel-style effects as drills effectively lets the Veteran spend subclass selections in place of a major feat.

That is not automatically forbidden—subclasses can replicate some feat territory—but the Veteran should not obtain the entire lockdown package while also acquiring seven other drills.

“Hook and Turn”—move a creature 5 feet to another space still within your reach—is more original and more Veteran-like. Add a size restriction, probably Large or smaller, and once per turn/round.

“Hamstring: disadvantage on the next Dexterity save” is mechanically interesting but creates considerable party optimization potential. A Fighter can use its Reaction immediately before a caster's turn and improve a powerful area/control spell. That may be a worthwhile support niche, but it is more powerful than it first appears.

**The out-of-combat package is where C can decisively justify the subclass.** Tactical Mind already gives the base Fighter unusually good failed-check recovery. citeturn4view0 Veteran should therefore provide **things the Fighter is allowed to know or ask**, not another pile of +d4/+PB/advantage bonuses.

That is why Veteran's Eye, Veteran Appraisal, Read the Ground, Common Soldier's Tongue, and Sabotage are stronger designs than “advantage on five more skills.”

It also prevents excessive class encroachment:

Rogue can retain broad Expertise, stealth, and fast-action identity.

Ranger can retain wilderness/exploration and magical hunter identity.

Bard can retain general social expertise and inspiration.

Battle Master can retain weapon-maneuver expertise.

Veteran instead becomes **the person who looks at a battlefield, wall, ambush site, broken wagon, panicked guard, or pile of ordinary gear and knows what to do with it.**

That is a strong niche.

## Recommended Roadmap, Red Flags, and Appendix

**Recommended architecture.** Build the next version entirely around **Veteran Drills**, but drastically reduce the menu and make every drill self-contained. A Drill should normally use this template:

> **Name — Action type.** When you take the **[exact 2024 action]**, [one enhancement]. [Any frequency, range, save, or duration.]

Avoid global rules such as “a Veteran Action counts as X,” “replace an attack with Y,” or “after using any Veteran Action…”

The subclass should be comprehensible even if the player puts each known drill on a separate card.

A good target is approximately **10–14 printed drills total**, of which any Veteran knows at most eight. That is enough choice to create different characters without creating a martial spellbook.

One way to hit all your desired action themes without fifty options is to let a few drills enhance paired actions:

| Drill family | Actions covered |
|---|---|
| Field Advance | Dash |
| Hard-Earned Advice | Help / Influence |
| Concealment Drill | Hide |
| Threat Assessment | Search / Study |
| Field Expedience | Utilize / narrowly magic-item use |
| Prepared Position | Dodge / Ready |
| Close-Quarters Habit | Attack |
| Vigilant Guard | Opportunity Attack / reaction |
| Veteran's Eye | noncombat observation |
| Improvised Fighting | weapons/unarmed/gear |

That gives the subclass thematic breadth without requiring five micro-choices for every generic action.

**Suggested subclass skeleton:**

| Fighter level | Direction |
|---:|---|
| 3 | Veteran Drills, 4 known; Veteran's Eye; modest damage feature |
| 7 | 5th drill; reaction/Ready drills unlock; battlefield awareness feature |
| 10 | 6th drill; Field-Expedient Fighting; Influence and limited magic-item options unlock |
| 15 | 7th drill; Dodge/advanced preparedness unlock; veteran adaptability |
| 18 | 8th drill; strong but bounded reaction/tempo capstone |

At **level 3**, I would not attach Tactical Blow to every drill.

Give the subclass a separate modest offensive feature so utility choices do not need to be “cashed in” for damage. Two promising shapes are:

> once per turn extra 1d6 under a tactical condition;

or

> a once-per-turn effect when attacking a Bloodied creature, a creature that missed you, a creature that attacked an ally, or a creature you have Studied.

The exact trigger needs testing. The important point is that **damage and generic-action enhancement should be separate balance knobs**.

That solves one of A's worst incentives: in A, the player may take a low-value Veteran Action simply because doing so unlocks Tactical Blow. The generic action becomes a button you press to qualify for damage rather than a genuine tactical decision.

A level 3 damage budget around **+2 to +4 sustained DPR when the condition is available** is a reasonable first prototype. This is a design target, not an official threshold. Champion's raw crit benefit is below that, while Battle Master can expend resources for larger damage-and-control swings. citeturn22search4turn22search0

At **level 7**, unlock Ready and reaction-oriented drills rather than globally granting two broad reaction-attack triggers. A single Vigilant Response feature is still plausible, but it should probably say something like:

> Once per round, when a creature within your weapon's reach misses you with an attack or damages another creature, you can use your Reaction to make one melee weapon attack against it.

That is deliberately **a reaction attack, not automatically an Opportunity Attack**. This distinction lets you control which OA-specific drills and feat effects apply.

“Once per round” also future-proofs the feature against a level 18 extra-reaction ability.

At **level 10**, Field-Expedient Fighting can safely carry most of the flavor from A:

proficiency with improvised weapons;

improvised damage improved from the ordinary 1d4 to perhaps 1d6, with a two-handed substantial object reaching 1d8 at GM discretion;

and 1d6 unarmed damage, perhaps 1d8 while neither weapon nor shield is held.

Ordinary improvised weapons are otherwise nonproficient and 1d4, while ordinary damaging Unarmed Strikes are 1 + Strength. citeturn20view0turn20view3 Those are meaningful improvements without threatening the Fighter's real martial weapons.

Do **not** attach Push/Sap/Slow to all of them. If you want the Veteran to use Tactical Master with improvised objects, create a carefully worded specific bridge rather than granting an additional mastery on top of an existing one.

Level 10 is also the right place for Common Soldier's Tongue / Influence and the single optional magic-item drill.

At **level 15**, the Veteran should become dramatically better at *choosing the right procedure*, not simply get two actions.

I would consider this:

> When you finish a Long Rest, you can replace one Veteran Drill you know with another for which you qualify.

That is powerful in campaigns with scouting/information but does not increase round-by-round action count.

An additional combat benefit could make expensive defensive actions more usable. One candidate worth playtesting is:

> Once on your turn after you take the Dodge, Help, Search, Study, or Utilize action and use one of your Veteran Drills, you can make one weapon attack as a Bonus Action.

At level 15 a normal Fighter has three Attack-action attacks. citeturn15view0 This version still sacrifices two attacks and the Bonus Action, so the generic action remains a meaningful cost. It does **not** turn one sacrificed attack into an entire action, and it cannot recursively nest Ready/Magic.

I would initially exclude Ready, Hide, and Magic from that list because each creates different abuse cases.

It is not mandatory. An even cleaner design is simply to let those actions remain situational.

At **level 18**, avoid “one Reaction on every turn.” A safer capstone is:

> You gain one additional Reaction each round. You can use this additional Reaction only for a Veteran Drill, a readied weapon attack enhanced by a Veteran Drill, or a reaction attack granted by this subclass. You can't use more than one Reaction on the same turn.

That gives a meaningful “always watching” capstone while limiting the character to **two reactions per round**, rather than one reaction multiplied by every combatant's turn.

Even this needs Sentinel/Polearm Master testing.

An alternative, safer still, is not to add a reaction at all. Give Veteran the ability to apply **two different drill enhancements per round**, or to use one advanced drill without its normal limited-use cost. That produces mastery through versatility rather than action multiplication.

Do not combine an extra-reaction capstone with a 3d8 “once on each turn” Tactical Blow.

**Damage scaling.** My recommended first-test envelope is roughly:

| Tier | Veteran subclass sustained damage target |
|---|---|
| Levels 3–6 | +2 to +4 DPR under normal conditions |
| Levels 7–10 | +3 to +5 |
| Levels 11–14 | +4 to +6 |
| Levels 15–17 | +4 to +8, with significant tactical benefit |
| Levels 18–20 | +6 to +12 in ordinary circumstances |

The upper end assumes the subclass is receiving fewer direct defensive benefits. These are prototype balance targets, not universal 5e design laws.

A subclass with excellent control, defensive support, field utility, and a second reaction should aim toward the **lower** end.

A subclass whose drills are mostly informational should have more room for damage.

The existing Iteration A capstone can exceed this envelope by dozens of DPR as reaction opportunities multiply, which is why changing the architecture matters much more than adjusting 3d8 to 2d8.

**Highest-risk exploit matrix:**

| Interaction | Risk | Recommendation |
|---|---|---|
| Ready as attack replacement | **Critical** | Prohibit architecture entirely |
| Magic Action as attack replacement | **Critical** | Prohibit |
| Free Dodge during full Attack | **Critical** | Prohibit |
| Reaction on every turn + 3d8 each turn | **Critical** | Replace with bounded reactions |
| Rogue + off-turn attacks | High | Never make repeated off-turn attacks trivial |
| Polearm/reach + broad reaction triggers | High | Test with 10-foot reach and PAM |
| Sentinel + Veteran OA drills | High/redundant | Avoid recreating both Sentinel pillars |
| Nick + Bonus Action Veteran Action | High build skew | Another reason to drop global BA action engine |
| Dual Wielder + BA Veteran Action | Action conflict | Healthy if intentional |
| Second Wind/Tactical Shift + BA Veteran Action | Action conflict | Healthy only if subclass does not depend on BA every turn |
| Applied Mastery + Tactical Master | **High** | Cut Applied Mastery |
| Vex + added mastery | High | Avoid double mastery |
| Grappler + improved Unarmed + added mastery | High | Improved unarmed okay; added mastery not |
| Barbarian advantage + Tactical Blow | Medium | Rider becomes highly reliable; price accordingly |
| Ranger/per-hit buffs + attack replacement | Medium | Replacement becomes disproportionately punitive |
| Paladin/Warlock/Wizard + generic Magic drill | **High** | Magic-item-only or cut |
| Charger + forced movement | Medium | Check positional loops, but generally controllable |
| Shield Master + control drills | Medium | Avoid giving the same shove/control effect twice |
| Mage Slayer + reaction expansion | Medium | Second-reaction capstone needs testing |
| Sharpshooter | Low direct DPR risk in 2024 | Current feat lacks old -5/+10 damage package |
| Improvised weapons alone | Low | d6/d8 at level 10 is safe starting point |

Current Sharpshooter's D&D Beyond entry lists Bypass Cover, Firing in Melee, and Long Shots rather than an old-style damage rider, so 2014 “SS Fighter” DPR assumptions should not be reused. citeturn21search12

Polearm Master remains important because its Pole Strike and Reactive Strike expand Bonus Action/Reaction usage. citeturn21search5 The exact wording of Veteran reaction drills should distinguish **“an Opportunity Attack”** from **“a melee attack made as a Reaction.”** Do not casually make all reaction attacks count as Opportunity Attacks; OA is a defined 2024 mechanic. citeturn20view3

**Rogue.** The principal concern is not a three-level Rogue dip adding enormous personal damage. It is that any mechanism allowing a Fighter to reliably manufacture attacks on different creatures' turns gains special value alongside once-per-turn damage features. Ready and repeated reactions therefore need conservative wording. citeturn15view0

**Monk.** The d6/d8 unarmed feature itself is not a balance threat at Fighter 10. The danger would be making an Unarmed Strike simultaneously behave like a mastered weapon. Keep weapon mastery and Veteran unarmed fighting conceptually separate. Official rules likewise treat weapon masteries as weapon properties and Unarmed Strike as its own attack/grapple/shove mechanic. citeturn19view0turn20view3

**Barbarian.** Reliable Advantage makes any “next hit deals X dice” feature approach its theoretical value, while Rage also creates Bonus Action pressure on the opening turn. The best protection is simply to keep the Veteran damage rider once per Veteran's turn and modest rather than making it available on every turn.

**Ranger and other per-hit builds.** Extra per-hit riders make every sacrificed Fighter attack more expensive; this is another reason attack replacement cannot be balanced consistently across multiclasses.

**Paladin.** The main concern is action economy rather than an obvious broken direct interaction: avoid giving the multiclass another no-cost generic action while it retains Fighter attacks and its other limited resources.

**Warlock, Wizard, and Eldritch Knight.** These are the strongest reason to say **“magic item activation,” never “Magic action” generically**. The Magic action explicitly includes casting spells, and the Fighter's own Action Surge expressly excludes it. citeturn12view3turn4view0 A subclass loophole should not undo that boundary.

**Grappler and Tavern Brawler.** Stress-test the level 10 d6/d8 unarmed package against both, but do not pre-emptively weaken the damage die. The much more dangerous version is an unarmed hit that simultaneously carries a feat rider, grapple/control, and an additional Push/Sap/Slow mastery.

**Weapon Mastery combinations.** The core Fighter already has a sophisticated mastery optimization game. Greatsword/glaive Graze gives miss damage; Vex feeds advantage; Nick rearranges action economy; Push and Slow control movement; Sap suppresses attacks. citeturn19view0 Veteran drills should mostly **interact around** those properties, not add a second mastery property to the same attack.

For example:

> Good: “When your Push mastery moves a creature, you can move 5 feet without provoking from that creature.”

> Risky: “Apply Push in addition to the mastery you already used.”

The former rewards mastery choice. The latter simply raises the Fighter's mastery budget.

**Ideas to keep almost unchanged in spirit:** Veteran's Eye, Common Soldier's Tongue, Veteran Appraisal, Read the Ground, Sabotage, a tightly defined Quick Barricade, Hold Ground, Shield the Line, Spot the Shooter, a scoped Hair Trigger, proficiency with improvised weapons, and improved unarmed damage.

**Ideas to keep after substantial rewrite:** Improved Help, Vigilant Response, Forced March, Drag to Cover, Counterguard, Dirty Trick, Finish the Wounded, Hook and Turn, magic-item expertise.

**Ideas to cut:** attack replacement as the core system; generic Magic Action conversion; Applied Mastery as an additional mastery; “two Veteran Actions per turn” as a generic permission; free Dodge inside Attack; Tactical Blow once on *each* turn; unrestricted reaction-per-turn capstone; open-ended Dirty Trick; exact-stat extraction from Study; automatic combat mind-control through Influence.

**Key-source appendix.** The most useful primary sources are the official 2024 Fighter progression and features, including Action Surge, Tactical Mind, Tactical Shift, Tactical Master, and Studied Attacks. citeturn15view0turn4view0turn4view1turn4view2turn4view3 The official Rules Glossary is critical for Help, Hide, Influence, Magic, Ready, Search, Study, Utilize, Dodge, Opportunity Attacks, Unarmed Strikes, and improvised weapons. citeturn12view0turn12view1turn12view3turn12view4turn12view5turn12view6turn20view0turn20view1turn20view3 The official weapon table and mastery descriptions are essential for Nick/Vex/Graze/Push/Sap/Slow interaction testing. citeturn18view0turn18view2turn19view0

For historical optimization baselines, Tabletop Builds' Basic Fighter and melee/ranged Fighter guides are particularly useful, but their numeric conclusions are **2014-system conclusions**. citeturn6search0turn6search5turn6search7 Its Flagship methodology is useful for understanding what “high optimization” means and for remembering that optimized party strength is not equivalent to isolated martial DPR. citeturn6search14

For 2024 optimization methodology, Treantmonk's Fighter damage work, new sustained-damage baseline, Eldritch Knight analysis, and community recalculations around those videos are useful because they expose how sensitive the answer is to assumptions. citeturn9search2turn9search8turn8search0turn9search0turn9search12 D&D Deep Dive/d4 build material is useful as another source of highly optimized tactical build patterns rather than as a universal numeric truth. citeturn10search1turn10search3

Reddit discussions in r/onednd and r/3d6 were useful primarily as **community sentiment and edge-case discovery**, not authoritative rules sources. They repeatedly surface Eldritch Knight/Battle Master comparisons, PAM/GWM sensitivity, reaction Sneak Attack concepts, Weapon Mastery sequencing, and divergent DPR assumptions. citeturn5search3turn8search4turn8search11turn9search0 Giant in the Playground was useful chiefly for criticism of overly narrow DPR analysis. citeturn9search14 D&D Beyond forums were useful for identifying contentious edge cases and current player interpretations, but official D&D Beyond rules were used instead wherever the actual 2024 rules text was available. citeturn11search1turn22search20 EN World pages encountered during the survey were not reliably accessible to the crawler, and public optimization Discord material is generally not sufficiently indexable or attributable to serve as strong evidence; neither was used as a hard basis for the recommendations.

The resulting roadmap is therefore quite decisive: **keep the Veteran, keep the mundane-action fantasy, keep the menu, and stop trying to make generic actions fit inside Extra Attack.** The 2024 Fighter already has enough attack-economy machinery. The Veteran will be more distinctive—and substantially easier to balance—if its defining question becomes not *“How many extra actions can I squeeze into Attack?”* but *“Which ordinary battlefield procedure has this character learned to execute exceptionally well?”*