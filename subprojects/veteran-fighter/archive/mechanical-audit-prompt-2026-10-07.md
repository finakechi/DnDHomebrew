# Veteran Fighter — Comprehensive Mechanical Balance Audit

Perform a rigorous **mechanical balance audit** of the current Veteran Fighter subclass for **D&D 5.5e: the revised 2024 rules, with applicable current errata**.

This is primarily a **quantitative, rules-interaction, and optimization audit**. It is not another originality search, historical report, or invitation to redesign the subclass.

The central question is:

> **Across adverse, mixed, and optimized play assumptions, is the current Veteran appropriately powerful within the official revised Fighter subclass envelope, including its interactions with the entire Fighter chassis, feats, equipment, multiclassing, and party composition?**

Use multiple transparent analytical frameworks. State their assumptions separately and investigate whether conclusions survive changes in accuracy, positioning, targets, rests, resources, and build choices.

Determine:

- where the subclass is balanced, underpowered, or overtuned;
- whether a problem appears only under optimization or particular encounter assumptions;
- whether apparently powerful features remain appropriate after their actual costs and requirements;
- whether party support, defense, or action compression creates power that personal DPR misses;
- whether individual Lessons are mandatory, redundant, misleading, or weak in their intended situations;
- and the **smallest evidence-supported changes**, if any, needed before further playtesting.

A strong, unconventional mechanic is not automatically a defect. Development history is not proof of balance either.

---

## 1. Read the project material and establish authority

Before rules research or calculations, locate the relevant files in the supplied attachments or accessible file Library and read the complete current subclass text.

Start with:

1. **Veteran_Public_Test_1.md** — the intended mechanical audit subject unless a newer explicit testing build is supplied.
2. **Veteran_Fighter_Comprehensive_Current_State_Report_2026-10-05.md** — the project's authoritative design-state and decision-history record; follow its internal hierarchy for historical material.
3. **Veteran_Fighter_Pre_Playtest_Audit_2026-10-05.md** — earlier recommendations and analysis to verify independently.
4. **Veteran_Audit_Calculations_2026-10-05.zip** — earlier scripts, assumptions, and outputs to inspect and reproduce where useful.
5. Relevant older Veteran reports and design discussions, only when needed to understand intentional compromises, rejected mechanics, or unresolved questions.

Do not assume inaccessible files or chats have been read. Search for named files when access is available. If the complete current mechanical text cannot be obtained, identify the missing source and stop mechanical conclusions until it is supplied.

Use these distinctions:

- The user's newest explicit decisions take precedence.
- A newer explicitly adopted testing build takes precedence over older mechanics.
- For this task, use Public Test 1 as the audit subject if no newer build is identified. If its adoption is not established, label it the **proposed testing build being audited**, rather than claiming every previous recommendation became project canon.
- The comprehensive report governs historical status and intent; the previous audit supplies hypotheses and calculations, not authoritative balance conclusions.
- Do not silently combine the 22-concept historical roster with the 20-selection testing roster.
- Do not reintroduce rejected or experimental mechanics.

Provide a short source/version table identifying the text actually audited, material unavailable, and any conflict that materially changes a calculation. Analyze genuinely unresolved mechanical readings separately; do not substitute your preferred interpretation without disclosure.

---

## 2. Verify the current mechanical fingerprint

The following summarizes **Public Test 1**. Verify it against the file before using it; the file's complete wording governs details.

### Fighter 3

**Hard-Won Lessons**

- Four Lessons initially; one additional Lesson at Fighter 7, 10, 15, and 18.
- Known progression: **4 / 5 / 6 / 7 / 8**.
- Compatible Lessons can modify the same named action.
- Attack-replacement Lessons use ordinary Attack-action/Extra Attack slots on the Veteran's turn, rather than Practical Fighting or Light-property extra attacks.
- Each such Lesson replaces at most one attack per eligible Attack action; expressly one-attack-limited actions are excluded.

**Practical Experience**

- One proficiency from the specified skill list and Expertise in one proficient skill from that list.

**Practical Fighting**

- Improvised Weapon proficiency.
- Practical Contact allows Strength or Dexterity for damaging Unarmed Strike attack and damage rolls, with an optional **1d6 + chosen modifier** damage replacement.
- A held implement can represent the strike without transferring its weapon, Mastery, or magical benefits.
- It does not independently change Grapple/Shove DCs, anatomy, hand, or size requirements.
- **One shared Practical Fighting use per Attack action on the Veteran's turn**, immediately after a weapon attack.
- Its generated attack is part of that action, cannot trigger Practical Fighting again, and cannot add an attack to an expressly one-attack-limited action.

**Close Work:** after a melee attack with a weapon, make an Unarmed Strike against a creature within 5 feet.

**Hit or Correct:** after a ranged attack with a weapon, move up to half Speed without provoking Opportunity Attacks, then optionally make a ranged attack with a weapon. A triggering hit requires a different creature for the follow-up; a miss permits the same or a different creature. The follow-up omits a positive ability modifier from damage, while normal weapon requirements remain.

### Fighter 7 — Battlefield Readiness

Choose two different options when rolling Initiative:

- **Counter-Ambush:** remove surprise-imposed Initiative Disadvantage.
- **Take Position:** half-Speed movement.
- **Read the Field:** Search or Study.
- **Brace:** Temporary Hit Points equal to Proficiency Bonus.

Counter-Ambush resolves immediately; the others resolve at the start of the first turn, with the testing text's Incapacitated restriction. Search/Study can benefit from applicable Lessons.

### Fighter 10 — Been Here Before

- **Change of Approach:** replace one known Lesson after a Short or Long Rest.
- **Reserve Lessons:** select two qualifying unknown Lessons after a Long Rest; use either for one declared action, Reaction, or procedure, once between Short or Long Rests.
- Resulting effects last normally, but reserved access is not continuing knowledge or permanent proficiency.
- Normal Lesson limits remain; learning a reserve does not immediately refill that reserve slot.

### Fighter 15 — Still in the Fight

- **Reserve Readiness:** once per combat, at the start of a later turn, use one unused Readiness option other than Counter-Ambush.
- **Dig Deep:** when using Action Surge, spend Second Wind to heal without a Bonus Action and obtain the specified Tactical Shift-style movement.
- **Improved Brace:** Brace becomes twice Proficiency Bonus in Temporary Hit Points.

This package was previously called **No Lesson Wasted**. Audit the current package rather than an older feature sharing its name or level.

### Fighter 18 — Veteran of a Hundred Fights

At the start of each combat turn, choose one visible creature. Until the start of the Veteran's next turn:

- attack rolls against it have Advantage;
- saving throws it forces the Veteran to make have Advantage;
- its attack rolls against the Veteran have Disadvantage.

The duration includes other creatures' turns. Do not shorten it to the Veteran's own turn when calculating reactions or defense.

### Current 20-selection Lesson roster

**Base access:** Battlefield Improvisation; Break Their Hold; Break Through; Casualty Extraction; Field Concealment; Field-Expedient Tool; Fire-Team Assist; Forced March; Hold Ground; Parting Blow; Shield the Line; Threat Scan; Veteran's Correction.

**Fighter 7:** Hair Trigger; Hook and Turn.

**Fighter 10:** Battlefield Activation; Common Soldier's Tongue; Find the Weak Point; Quick Barricade; Sabotage.

Battlefield Improvisation includes **Deliver** and **Misdirect**. Fire-Team Assist includes **Distract** and **Two-Man Takedown**. Audit their procedures individually as well as their merged selection value.

**Open the Lane, Spoil the Reaction, and Suppressing Fire are not testing-roster Lessons.** Do not add them during this audit.

---

## 3. Research and computational requirements

Use web research extensively for current rules, official subclass comparisons, transparent optimization methods, and accessible revised monster statistics.

Prioritize:

1. Wizards of the Coast / D&D Beyond current official rules and errata.
2. Licensed current rules reproductions when direct official text is inaccessible.
3. Analysts who publish assumptions, formulas, policies, or reproducible calculations.
4. Community discussion as secondary evidence and a source of testable hypotheses.

Distinguish **project decisions, rules facts, external methodology, model assumptions, recommendations, and playtest hypotheses**.

If Wolfram is available, use it where it improves exact probabilities, recurrences, distributions, symbolic break-even calculations, or independent verification. Otherwise use equivalent exact computational tools and state the substitution. Do not make expensive redundant calculator calls merely to satisfy a tool count.

Cross-check important results with an independent method: Python, a spreadsheet, direct enumeration, another transparent calculator, or Monte Carlo simulation. Resolve discrepancies before drawing conclusions.

For simulation, report trials, seed, policy, assumptions, and uncertainty. Use enough trials to stabilize the result. Distinguish simulated values from exact calculations, and distinguish a full dice simulation from one that substitutes mean damage to check attack sequencing.

Produce a companion **recalculable workbook** and runnable calculation scripts. Requirements are in section 24.

---

## 4. Verify the revised rules first

Check exact current wording for:

- Fighter progression, ASIs, Fighting Styles, and Weapon Mastery selections;
- Second Wind's uses and refresh, Tactical Mind, and Tactical Shift;
- Action Surge, including the Magic-action restriction and the level-17 once-per-turn limit;
- Extra Attack at Fighter 5, 11, and 20;
- Tactical Master at 9, Indomitable, and Studied Attacks at 13;
- Advantage/Disadvantage cancellation, critical hits, and damage riders;
- Unarmed Strike Damage/Grapple/Shove, Grappled, Prone, Incapacitated, and movement;
- Attack-action weapon drawing/stowing, Thrown, Ammunition, Loading, Light, Nick, and Reach;
- Graze, Vex, Topple, Push, Sap, Slow, Cleave, and target/duration restrictions;
- Ready, Opportunity Attacks, forced movement, and separately named reaction attacks;
- Dash, Disengage, Dodge, Help, Hide, Search, Study, Influence, Utilize, and Magic;
- cover, objects, tools, carrying, Bloodied, Temporary Hit Points, and item activation;
- relevant feats, Fighting Styles, spells, and multiclass features.

Check errata. Label legacy rules and supplement eligibility explicitly. Do not import 2014 feat benefits, opposed grapple checks, surprise rules, or Action Surge spellcasting assumptions into a revised-rules model.

Separate a **wording ambiguity** from a **power discrepancy**. A favorable reading of ambiguous wording is not automatically an intended exploit; a mathematically strong legal interaction is not automatically an ambiguity.

---

## 5. Use multiple methodologies and accuracy models

Research established methods such as RPGBOT Fundamental Math, Tabletop Builds, transparent current Treantmonk benchmarks where relevant, AC-sweep calculators, encounter/day-normalized methods, and official encounter or monster mathematics.

These are candidates, not mandatory authorities. Include only methods whose inputs and assumptions can be established. Identify their edition and whether older mathematics remains applicable after updating rules/build assumptions.

For every adopted framework:

1. Cite and explain the method.
2. State accuracy, build, targets, rounds, resources, setup, and reaction policies.
3. Calculate Veteran and appropriate official comparators under the same assumptions.
4. State exclusions and limitations.
5. Show where changing assumptions changes the verdict.

Do not average unrelated benchmarks into one score.

At minimum include:

**Fixed accuracy:** ordinary hit probabilities around **50%, 60%, 65%, 70%, and 80%**, with criticals accounted for. Distinguish normalized equal-accuracy comparisons from actual attack-bonus comparisons. Apply Advantage and real accuracy bonuses correctly.

**Level/AC model:** actual legal attack bonuses against representative tier-appropriate ACs and a meaningful AC sweep. If a historical AC progression happens to produce 65% at every checkpoint, acknowledge that and add independent AC sensitivity rather than presenting it as wholly different evidence.

**Empirical revised monsters:** if enough current monster data is accessible, record sampling criteria and source edition; summarize AC, attack bonuses, relevant saves, attack types, and important immunities. Use CR and encounter composition thoughtfully; CR is not automatically equal to party level. Report medians, means, and useful ranges when supported. Do not describe a small convenience sample as representative of the entire Monster Manual. If access is inadequate, use disclosed scenarios instead of invented empirical distributions.

**Exact sequential model:** track hits, misses, crits, Mastery, follow-up timing, per-target entitlements, and expiration. Use finite-turn and multi-round models where relevant.

---

## 6. Levels, builds, and legal character progression

Audit Fighter levels:

**3, 5, 7, 9, 10, 11, 13, 15, 17, 18, and 20.**

Levels 9 and 13 matter for Tactical Master and Studied Attacks; 5/11/20 for attack slots; 17 for Surge/resource sequencing. Examine the full package at each subclass feature level.

Use a declared default progression, for example primary ability 16 at level 3, 18 after the level-4 ASI, and 20 after level 6. Then construct separate legal optimized progressions, accounting for feat prerequisites and which ability each feat increases.

At minimum test:

- Strength great weapon;
- sword and shield;
- polearm;
- dual wield;
- Dexterity melee;
- longbow;
- crossbow, including Loading before the appropriate feat;
- thrown weapons;
- mixed weapon/unarmed and free-hand grappling.

Include competent feat-enabled builds, not only featless isolates. Test relevant Strength and Dexterity cases. Do not silently grant maximum primary ability alongside incompatible feat allocations, an extra Fighting Style, an unavailable free hand, or an undeclared party buff.

Use no-item and matched-item scenarios separately. Clearly distinguish controlled subclass isolation from practical optimized builds.

---

## 7. Official Fighter benchmarks and broader context

Primary comparators are **Champion, Battle Master, Eldritch Knight, and Psi Warrior** under revised rules. Include additional officially published revised-compatible Fighter subclasses only when they materially improve the comparison; label their source and compatibility.

For each comparator, use its complete relevant package:

- Champion: critical range, athletic/initiative/movement benefits, additional style, Heroic Warrior, and Survivor.
- Battle Master: full dice/refresh progression, maneuvers, Precision Attack, control, reaction options, ally attacks, Know Your Enemy, and Relentless.
- Eldritch Knight: legal abilities and spells, War Magic, defensive spells, Eldritch Strike, Arcane Charge, and Improved War Magic.
- Psi Warrior: actual dice/refresh progression, Intelligence, Strike, protection, movement, thrust, Guarded Mind, Bulwark, and Telekinetic Master.

Do not represent Champion with criticals alone after Heroic Warrior arrives. Do not compare a fresh Veteran with a resource-empty Battle Master or Psi Warrior and call that subclass parity. Do not grant EK Intelligence equal to its primary weapon ability without a legal progression or an explicit favorable-bound label; show realistic ability sensitivity.

Use multiple sensible resource-spending policies where they materially matter. A first-hit damage-die policy is not a universal optimized Battle Master. Include or bracket Precision, Trip, Riposte, and other significant alternatives rather than implying they have zero value.

Compare sustained/burst offense, defense, control, movement, action compression, exploration/social utility, adaptability, resource dependence, and build flexibility. Avoid comparing one Veteran benefit with only one benefit from another subclass's larger package.

As secondary context, consider competent Monk, Rogue, Barbarian, Ranger, and Paladin builds. This does not require equal DPR across classes or establish a Fighter balance target from another class's strongest specialty.

---

## 8. Practical Contact and Close Work

Quantify the extra Unarmed Strike separately and within legal weapon sequences.

Test:

- damage versus Grapple/Shove choices;
- Strength versus Dexterity accuracy and ordinary save DCs;
- weapon attacks at 10-foot reach with no creature within 5 feet;
- adjacency, target availability, hands, size, immunity, and escape;
- shield/pommel/haft narration without inherited implement bonuses;
- Grappler Damage+Grapple, later-attack Advantage, and its frequency limit;
- Tavern Brawler rerolls/push and overlapping proficiency/damage;
- Shield Master, Topple, and other potentially redundant shove/prone sources;
- Unarmed Fighting style and improved Monk damage without stacking replacement dice;
- offhand, heavy-weapon, and grappling-hand restrictions.

Evaluate immediate versus delayed Close Work after different weapon attacks. A stationary Vex sequence with an inserted unarmed attack is not automatically baseline DPR plus the isolated contact EV.

Report additional damage attempts, successful control probability, later attacks improved, and positional exposure. Do not give the same strike both damage and a free grapple unless an actual feature permits it.

---

## 9. Hit or Correct: focused damage, split fire, movement, and riders

Model separately:

1. One durable target: follow-up against it is available only after a miss.
2. Two valid targets: distinguish focus damage from total distributed damage.
3. Several low-HP targets: include overkill and target availability where data permits.
4. An all-hit turn with no legal different creature: movement can remain useful without follow-up damage.
5. Adverse range, cover, visibility, Loading, ammunition, and close-range pressure.

Compare policies such as immediate use, saving the feature for a later miss, and using an alternate-target shot after a final hit. State whether the policy is fixed or optimized and under what information.

Track Studied Attacks and Vex **by target**; hitting or missing a secondary target must not improperly transfer its Advantage entitlement to the primary target. Preserve valid carried entitlements and expiration across turns.

Distinguish a ranged attack with a weapon from the category of Ranged weapon, especially for thrown melee weapons.

Test remaining damage bonuses when the positive ability modifier is omitted: GWM where legal, Fighting Styles, qualifying class riders, and item riders. Do not assume the omitted ability modifier removes every other damage contribution.

Value safe movement through geometry and scenario outcomes. It is not a teleport or blanket immunity to all reactions. Do not assign it a universal invented DPR value.

---

## 10. Attack-action and action-economy audit

Create an action-economy table by audited level: Action, ordinary attack slots, generated attacks, Bonus Action, Reaction, movement, and limited resources.

For each attack-replacement Lesson, compare:

- one lost attack at Fighter5/11/20;
- absolute lost damage, Mastery/control opportunity, and qualifying riders;
- relative fraction of ordinary attacks surrendered;
- whether another retained weapon attack still triggers Practical Fighting;
- whether replacing every triggering weapon attack also loses Practical Fighting;
- action compression compared with doing the same task normally;
- combinations of different replacement Lessons in one action.

Also assess Fighter 3: replacing its only ordinary attack may forfeit the combat engine as well as that attack.

For every full-action Lesson, price the entire foregone attack sequence. For Bonus Actions and Reactions, identify real competing options. A modifier attached to an already chosen OA need not incur a second Reaction cost, but the OA itself still uses the available Reaction.

Explicitly test:

- two Attack actions from Surge;
- Nick once per turn rather than once per action;
- Practical Fighting once per eligible Attack action;
- restricted actions such as Haste;
- Ready on another creature's turn versus a trigger on the Veteran's own turn;
- weapon drawing/stowing tied to actual attacks, not presumed free permission from every replacement procedure.

List legal sequences rather than only attack-count maxima.

---

## 11. Attack-replacement utility procedures

Audit every accepted procedure independently:

**Field-Expedient Tool:** closed weapon-assisted physical Utilize procedures; check substitution; actual tools and proficiency; melee versus ranged impact; consumables; fine manipulation; equipment; repair/crafting time; magic activation; and eligible Sabotage/Barricade modification.

**Break Their Hold:** explicit range/reach, target-chosen save, grapple release versus disarm, secured/worn objects, protections against disarming, enemy recovery, backup weapons, and comparison with ordinary Push/Shove or damaging/control attacks.

**Deliver:** held object, size/weight, willing visible recipient, path, Reaction/free hand, failed or declined catch, and distinction between delivering an object and using it.

**Misdirect:** real audible impact, throwing versus ranged strike, geometry/hearing/visibility, check scope and duration, normal hiding/noise rules, and whether it is worth an attack in its intended situation.

Test melee/ranged builds, multiclass Extra Attack, magic/rider triggers, and repeated uses. A procedure defined as not making an attack roll must not inherit on-hit benefits or Mastery.

Preserve the boundary between **specific physical attack replacements** and the rejected **replace an attack with arbitrary actions**. Do not promote the three experimental candidates simply to expand options.

---

## 12. Battlefield Readiness and preparation value

Evaluate each opening option individually and the best two-option combinations.

Model actual surprise, initiative outcomes, first-turn movement, Search/Study success, useful Brace absorption, and situations where the option is redundant or unusable. Preparation at the first turn is not automatically before enemies act.

Test Read the Field with Threat Scan and Find the Weak Point, including lawful reserve declarations. Compare opening compression with official features serving similar functions without assuming identical mechanics.

At level 15, measure whether Reserve Readiness adds useful later preparation and how improved Brace behaves with existing Temporary Hit Points. Do not add successive Temporary Hit Point grants together.

Separate real ambush/objective benefits from unsupported damage equivalents.

---

## 13. Adaptability, reserves, and outside-combat contribution

Audit Practical Experience, Change of Approach, and Reserve Lessons as an interacting package.

Test:

- Expertise and legal Help/Tactical Mind interactions;
- one rest swap versus access to the entire catalogue;
- reserved declaration timing and one shared use between rests;
- duration of resulting Help, Ready, concealment, or weakness effects;
- passive/temporary tool proficiency and retraining;
- known/reserve overlap and delayed replacement;
- consecutive Short Rests, actual time costs, and any proficiency/effect accumulation;
- selecting a Lesson after information that the timing does not permit;
- campaign utility versus combat utility and administrative burden.

Use scenarios for infiltration, evacuation, sabotage, fortification, practical social encounters, and resource savings. Do not equate outside-combat value with zero merely because it is difficult to monetize.

---

## 14. Full Hard-Won Lessons audit

Audit **all 20 selectable Lessons**, including both merged modes where applicable.

Provide a matrix covering:

- name and prerequisite;
- action/Reaction modified;
- combat and noncombat role;
- action-economy cost;
- likely use frequency under specified encounter/campaign conditions;
- numerical contribution where defensible;
- overlap with other Lessons, Fighter features, feats, and official subclasses;
- optimization value, pick pressure, trap risk, exploit risk, and complexity;
- recommendation: KEEP, POLISH, ADJUST, MERGE, CUT, MOVE, or PLAYTEST.

Pay special attention to:

- full-action Dodge/Help/Dash/Disengage Lessons at higher attack counts;
- Forced March versus Break Through;
- Hold Ground versus Shield the Line;
- Casualty Extraction versus Parting Blow;
- Fire-Team's two modes and advantage expiration;
- Correction's healing-resource trade;
- concealed-creature requirements for Threat Scan;
- Weak Point's evidence gate, one shared benefit per turn, one active subject, and duration;
- Common Soldier's Tongue's willingness/attitude distinction and actual Influence rules;
- Sabotage's genuine-attempt BA payoff, tools, and clearance;
- Barricade's actual materials, durability, geometry, and ordinary construction time;
- Activation's eligibility and BA competition.

Evaluate representative known-Lesson packages at 4/5/6/7/8 selections, not simultaneous ownership of all 20. Forecast selection pressure as a hypothesis, not an empirical pick rate without playtest data.

Do not cut a fieldcraft Lesson only because an unrelated combat model gives it zero DPR. Do identify a Lesson that remains inferior to ordinary procedures even when its intended situation occurs.

---

## 15. Party amplification and control

Analyze Fire-Team Assist, Two-Man Takedown, Veteran's Correction, Threat Scan, Find the Weak Point, Common Soldier's Tongue, rescue, and cover separately from personal damage.

Where supported, quantify:

- allied accuracy/crit gains and eligible damage packets;
- control-save failure rates, including a target's choice of its better Strength/Dexterity save;
- attacks or Actions saved;
- movement enabled and Opportunity Attacks avoided;
- enemy recovery/escape/clearance actions;
- incoming damage reduced;
- resources preserved;
- effect duration, immunity, and overlap with existing Advantage.

For Fire-Team, model benefit ending on the first allied hit rather than granting an entire party round unconditional Advantage. For Weak Point, model one shared benefit **per turn**, not one per round or one per ally attack, and account for study success and feasible exploitation.

Include parties with and without high-value attack packets, grapplers, ranged allies, and existing Advantage. Prone can help nearby attackers while hurting distant ones.

Use scenario analysis for surrender, fortification, sabotage, or extraction when a damage conversion would create false precision. Do not replace false DPR precision with an equally arbitrary utility score.

---

## 16. Hair Trigger, Hook and Turn, and off-turn offense

For Hair Trigger, calculate:

- legal Fighter attack count;
- optional 1d10 allocation policies, including first-hit versus waiting for a critical;
- trigger probability and a trigger that never occurs;
- lost immediate offense, on-turn-only benefits, movement, and Reaction;
- target and carried Advantage eligibility;
- own-turn versus other-turn resolution;
- capstone benefits during the full marked duration.

Do not copy Practical Fighting or Nick off-turn merely because the Veteran could make more attacks on its own turn. Do not impose an invented prohibition if an own-turn readied sequence legally meets the stated requirements.

For Hook and Turn, quantify actual OA opportunity and hit probability, extra damage including crits, and displacement value. Separate true OAs from Polearm Master Reactive Strike and other differently named reactions.

Test Sentinel, movement triggers, forced movement, and any claimed reaction chain. Distinguish strong finite synergy from recursive/infinite behavior.

Do not assume a Reaction attack every round or assume it is rare without scenarios supporting that frequency.

---

## 17. Dig Deep, resource competition, and item nova

Measure Dig Deep's healing subject to missing HP, Tactical Shift-style movement, Second Wind expenditure, and the actual Bonus Action it preserves.

Compare turns where the freed BA supports PAM, Dual Wielder, Battlefield Activation, a consumable, or another legal feature. Do not credit a free BA attack when no qualifying option exists.

Test competition among healing, Tactical Mind, Veteran's Correction, and Dig Deep, including normal Short Rest restoration. The level-17 Surge increase permits two uses on different turns, not both on one turn.

For Battlefield Activation, distinguish:

- item Magic activation requirements;
- actual attunement/character eligibility, charges, range, saves, and components where applicable;
- an ordinary item turn plus a BA attack;
- a Magic action followed by Surge Attack and optional Dig Deep;
- damage distributed across multiple item targets versus focused weapon damage.

Action Surge does not itself grant a second Magic action. Item nova is not sustained subclass DPR. Field-Expedient Tool does not activate items merely because they can be held as objects.

Use matched legal item access for official comparators. Do not give a pure Veteran a spellcaster-only item without demonstrating eligibility.

---

## 18. Capstone offense, defense, and targeting

Audit Veteran of a Hundred Fights as a complete package, not only its added damage.

Model:

- one durable boss;
- multiple dangerous enemies;
- a marked enemy that retreats, dies, becomes unseen, or attacks allies;
- ranged/caster threats and creature-forced saves;
- existing Advantage/Disadvantage, Vex, Studied Attacks, and party setup;
- off-turn attacks and saving throws before the next Veteran turn;
- exposure before the Veteran's first turn;
- interactions with Indomitable and other defensive resources.

Calculate marginal accuracy/crit damage, expected incoming attack damage prevented, and saving-throw success improvement across several ordinary probabilities. Do not count both redundant Advantage sources as separate benefits.

Compare with Champion Survivor, BM Relentless and reaction/control policies, EK spell/attack and defensive options, and Psi protection/Telekinesis. Different conditions/resources must remain visible.

Investigate whether this creates a concerning boss routine or broadly excessive combined contribution. Do not nerf full-duration/off-turn benefits simply because they are strong.

---

## 19. Sustained, nova, and encounter/day normalization

Report separately:

- ordinary repeatable offense;
- opening turns with setup/preparation;
- expected off-turn offense;
- one-turn resource nova;
- encounter averages;
- multi-encounter averages.

Test **3-, 4-, and 5-round encounters** and at least:

- one fresh encounter;
- several encounters without a Short Rest;
- several encounters with one or more scheduled Short Rests.

State exactly what refreshes, when rests occur, which resources start full, and the spending policy. Psi and BM recovery are not interchangeable. Carry valid attack entitlements across turns and reset only when rules, duration, or actual target changes require it.

Distinguish a capstone's persistent modifier from resources spent during that turn. Avoid combining one subclass's nova with another's empty-resource sustained figure.

Where geography/target HP is modeled, include overkill, enemies removed, and actual missed opportunities. Where it is not modeled, label white-room damage as such.

---

## 20. Feats, styles, equipment, and restricted-action interactions

At minimum verify and stress-test:

- Grappler, Tavern Brawler, GWM, PAM, Sentinel, Shield Master, Dual Wielder, Charger, and relevant additional feats;
- Archery, Dueling, Defense, TWF, Thrown Weapon Fighting, GWF, Unarmed Fighting, and relevant protection styles;
- +1/+2/+3 weapons, representative on-hit riders, accuracy items, and legally activated combat items;
- Light/Nick, weapon switching, hands, ammunition, Loading, reach, and thrown attacks;
- Action Surge, Second Wind, Tactical Mind/Shift/Master, Studied Attacks, and Indomitable;
- Ready, OAs, Haste and similarly restricted actions.

Apply revised feat wording. Check GWM's ability/prerequisite and the attack/action scope of its benefits; Heavy ranged weapons are not automatically excluded or automatically eligible without those checks.

Separate:

1. Intended strong synergy.
2. Build-specific dominant routine.
3. Ambiguous wording.
4. Actual legal exploit.
5. Infinite or recursive loop.

A long attack sequence is not automatically an exploit. A supposed loop must show exact legal triggers, costs, timing, and why it can continue.

---

## 21. Multiclass stress tests

Test Veteran Fighter 3 investments with Monk, Rogue, Barbarian, Paladin, and Ranger; examine deeper Fighter breakpoints when they create a materially different interaction.

Evaluate at matched **total character levels**, showing delayed features, attacks, feats, spell levels, resources, and ability requirements.

Priorities:

- Monk damage/DC options with Close Work and Martial Arts restrictions;
- Rogue Cunning Action Disengage + Parting Blow, including Ready/off-turn Sneak Attack and Reaction risk;
- Barbarian Rage/Reckless eligibility and extra contact attempts;
- Paladin damage delivery, revised smite timing, BA/slot limits;
- Ranger rider application, concentration, and retargeting;
- another class's Extra Attack with once-per-action Practical Fighting;
- feats and equipment that alter the above.

Compare these to competent official Fighter dips and other legal ways to achieve similar outcomes. Three Fighter levels cost meaningful progression, but that cost does not automatically make every repeatable dip routine harmless.

---

## 22. Sensitivity, breakpoints, and three environments

Vary assumptions that materially affect a conclusion:

- AC and actual attack bonus;
- strong/average/weak saves and target-chosen saves;
- adjacency and eligible target availability;
- existing Advantage and Mastery policies;
- incoming attacks, marked-enemy share, and reaction triggers;
- rounds, encounters, and rests;
- BA/Reaction availability;
- magic/rider assumptions;
- study/discovery/physical-feasibility success;
- party damage packets and terrain/objectives.

Report numerical breakpoints when they follow from a specified model. Do not manufacture universal trigger percentages or balance thresholds from unsupported scenarios.

Summarize:

**Adverse:** poor adjacency/target access, strong saves, redundant Advantage, limited useful objects, or denied reaction triggers.

**Mixed:** a disclosed combination of melee/ranged foes, terrain, target changes, and resource use; call it “typical” only to the extent evidence supports it.

**Favorable/optimized:** strong legal feats, useful targets/materials, reliable positioning, effective Lesson combinations, party support, and justified item access.

Evaluate all three; neither worst-case weakness nor best-case strength alone settles balance.

---

## 23. Independently verify the previous audit

Reproduce important earlier results using their exact declared assumptions, then test stronger or more realistic alternatives.

Check especially:

- crits and conditional first-hit damage;
- Champion Inspiration and extra style;
- BM and Psi die sizes, quantities, recovery, and spending policies;
- EK actual ability allocation and additional spell/defensive value;
- finite versus stationary Vex/Studied sequences;
- immediate versus delayed contact;
- per-target ranged follow-up entitlements;
- capstone benefits against marked versus unmarked targets;
- legality of feats, primary-stat progression, hands, and item eligibility;
- whether an approximation was presented as exact;
- actual replacement and Reaction opportunity costs.

Report **confirmed results, corrected results, and unresolved results** separately. Agreement with an earlier verdict is not the objective; independently defensible evidence is.

---

## 24. Required calculation workbook and reproducibility

Deliver a workbook with clearly separated inputs, formulas, outputs, units, scenario labels, and source notes. Include at minimum:

1. **Read Me / Sources:** edition, coverage, limitations, and recalculation instructions.
2. **Assumptions:** levels, abilities, PB, feats/styles, ACs, saves, geometry/availability, rounds/rests, and resources.
3. **Official Fighter Baselines:** chassis and complete relevant subclass scenarios.
4. **Practical Fighting:** contact, control, focused correction, split fire, and movement scenarios.
5. **Exact Sequencing:** Vex/Studied/capstone, timing policies, and target tracking.
6. **Attack-Replacement Costs:** Fighter 3/5/11/20 and build-sensitive costs.
7. **Reaction / Ready:** Hair Trigger, Hook, trigger availability, and competing reactions.
8. **Resources / Nova:** Surge, Second Wind, Dig Deep, encounters, days, and legal item sequences.
9. **Defense / Saves:** enemy accuracy, capstone, Brace, cover, healing, and control.
10. **Party Value / Lessons:** numerically defensible gains and separately labeled scenario outcomes.
11. **Builds / Multiclass:** feat legality, ability progression, and matched total-level comparisons.
12. **Sensitivity:** sweeps and identified breakpoints.

Use formulas for important workbook models rather than only pasted outputs. Changing a stated input must actually update the dependent formula outputs.

Complex recurrences may use supporting scripts. If a workbook table depends on externally generated results, identify that dependency and provide an explicit refresh path; do not claim those cells automatically recalculate if they do not. Do not conceal hard-coded outputs behind input-looking cells.

Provide runnable scripts, dependencies, seeds, important intermediate calculations, and any permissible underlying dataset. Do not redistribute protected full source texts or fabricate inaccessible data. State computational/tool limitations openly.

---

## 25. Required final report

### A. Executive verdict

Classify the subclass overall and at Fighter 3/7/10/15/18:

**Underpowered / Slightly Underpowered / Within Expected Range / Strong but Acceptable / Slightly Overtuned / Overtuned / Severely Overtuned.**

Include confidence, build/environment dependencies, and any insufficient evidence. Do not force a precise verdict when source access or uncertainty prevents one.

### B. Sources, version, rules, and methodology

Identify the exact audited text, current rules/errata, adopted frameworks, edition applicability, assumptions, limitations, and independently checked calculations. Separate rules ambiguity from balance.

### C. Benchmark tables

At audited levels and relevant scenarios show:

| Build / Model | On-Turn DPR | Expected Off-Turn DPR | Encounter Average | Nova | Control | Defense | Resources / Costs |
|---|---:|---:|---:|---:|---|---|---|

Label distributed damage, target assumptions, conditional values, and resource environments. Do not add mutually exclusive actions or correlated benefits twice.

### D. Feature-by-feature findings

Cover every core feature/subfeature. Rate **Weak / Appropriate / Strong / Overtuned / Critical Issue**, with evidence and uncertainty. Include the full Lesson matrix.

### E. Synergy, action economy, defense, and party value

Analyze interacting packages, not only isolated features. Include exact sequencing, utility compression, Readiness/Study, healing/BA preservation, off-turn offense, and the capstone.

### F. Model comparison and sensitivity

Explain exactly why different models agree or disagree. Show breakpoints and separate mathematical findings from encounter-policy assumptions.

### G. Optimization, multiclass, and exploit findings

Distinguish legal strong synergy, dominant routine, ambiguity, exploit, and recursion. Rank issues **Critical / Major / Moderate / Minor** without speculative severity inflation.

### H. Verification of the earlier audit

List reproduced results, corrections, and unresolved gaps, with practical consequences for its conclusions.

### I. Recommendations

For every proposed change provide:

1. The specific problem.
2. Evidence it is real.
3. The smallest justified change.
4. Recalculated results, or a precise scenario comparison for nonnumerical changes.
5. The thematic/gameplay cost.
6. Whether it is required before testing or should await evidence.

Explicitly recommend **no change** when supported. Prefer tuning a number, condition, or wording over replacing a functioning mechanic. Do not automatically rewrite the entire subclass. Supply replacement wording only for justified changes, unless a full revised build is separately requested.

### J. Playtest plan

Target the uncertainties mathematics cannot resolve. Include single/multiple threats, ambushes, ranged/caster foes, reach without adjacency, strong/chosen saves, grapples, weapon versus natural-attack enemies, terrain, object procedures, rescue, surrender, Ready trigger failures, low-rest days, legal item nova, and high-level boss defense.

Record each round:

- attempted/hit/critical attacks and actual damage versus overkill;
- PF branch, timing, targets, contact availability, and movement used;
- Mastery/Advantage sources and carried entitlements;
- utility procedure and attacks sacrificed;
- BA/Reaction spent and alternatives forgone;
- resources, healing actually received, and Temporary Hit Points absorbed;
- control attempts/successes, saves, immunities, recovery, and enemy actions prevented;
- party attacks/actions/movement/resources enabled;
- Lesson selections, reserve uses, DM denials, rules questions, and turn time.

Define what findings would justify a nerf, buff, merge, cut, or wording change. Thresholds should trigger review, not automatically decide balance from a small sample.

---

## 26. Final questions and preservation standard

Answer directly:

1. Is the Veteran defensibly balanced against complete revised Fighter subclasses?
2. Is its early contact engine appropriately powerful?
3. Is its sustained damage reasonable across the required build families?
4. Are focused correction, distributed follow-up damage, and safe movement appropriately valued?
5. Do Action Surge or legal riders produce a problematic ceiling?
6. Do attack replacements retain meaningful costs at 5/11/20?
7. Do Readiness, reserves, and rest swaps provide too much simultaneous flexibility or useful contingency?
8. Is the level-15 package meaningful in difficult attrition play?
9. Are Hair Trigger, Hook, and Parting Blow appropriate, including multiclass use?
10. Is the capstone's combined offense, defense, saves, and off-turn coverage appropriate?
11. Which Lesson packages create mandatory picks, weak options, or concerning dominant routines?
12. Is party amplification supported by meaningful action/evidence/positioning costs?
13. Do magic items, feats, or multiclassing reveal actual exploits?
14. Which previous audit conclusions were confirmed or corrected?
15. Which feature is strongest relative to its level, and which is weakest?
16. What should change before further testing, and what requires live evidence?

Preserve the thesis:

> **“A new fighter learns the proper way to fight. A Veteran has learned when the proper way is the wrong way.”**

Experience, survival, contingency planning, fieldcraft, equipment familiarity, weapon/body integration, and knowing when to do something more useful than attack are deliberate design goals.

Do not turn the Veteran into a superiority-dice Battle Master, command-aura Warlord, pseudo-spellcaster, generic Advantage generator, or universal action-economy bypass. Do not preserve an actual defect merely to protect the theme.

Finish with:

> **Current Balance Verdict:** [classification, confidence, and principal qualification]

Then list **only changes supported by the evidence**, in priority order.

The report and workbook must leave enough evidence for another analyst to reproduce the conclusions and vary assumptions without repeating the entire research process.
