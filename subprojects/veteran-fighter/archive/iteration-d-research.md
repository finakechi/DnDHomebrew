# Veteran Fighter Subclass: Iteration D

## Executive Design Verdict and Research Basis

**Recommendation: continue the subclass, but commit decisively to Iteration C’s architecture.** The Veteran has a viable identity space in the 2024 Fighter ecosystem, but only if it stops trying to make every mundane action economically equivalent to attacking. The strongest version is a Fighter who is **better at taking otherwise-normal actions when circumstances actually call for them**, plus a small independent damage feature, a bounded reaction feature, and increasingly powerful preparedness at high levels.

The prior report itself is **not retrievable in this session**: the uploaded-file search returned no available source. I therefore treated the conclusions reproduced in your prompt as the primary design brief rather than pretending to have read text I cannot currently access. I then checked that brief against the current 2024 rules, official Fighter design, current feat/mastery structure, and optimization discussion.

That validation strongly supports the prior report's direction. The 2024 Fighter already has a crowded and competent Attack-action chassis: Weapon Mastery at level 1, Extra Attack at 5/11/20, Tactical Master at 9, and Studied Attacks at 13. It also already has Second Wind/Tactical Mind/Tactical Shift for healing, checks, and movement, while Action Surge expressly cannot grant another Magic action. citeturn17view0turn17view1 Adding another general “replace attacks with utility actions” engine would be fighting the class rather than complementing it.

The optimizer landscape reinforces that point. Older 2014 optimization material often centered Fighter damage around Crossbow Expert/Sharpshooter or Polearm Master/Great Weapon Master packages, while the 2024 feat and mastery ecosystem is materially different; the current feat listings, for example, show Sharpshooter as Bypass Cover/Firing in Melee/Long Shots and Polearm Master as Pole Strike/Reactive Strike rather than simply reproducing their 2014 packages. citeturn18search1turn18search13turn16view0 Current 2024 optimization discussion commonly places Battle Master and Eldritch Knight among the stronger Fighter choices, but exact rankings vary significantly with weapon mastery, magic-item assumptions, permitted cantrips, and build methodology. That variability is a reason **not** to tune Veteran against one supposedly canonical DPR build. citeturn18search0turn18search4turn18search6turn18search29

My design verdict on the main decisions is:

| Question | Iteration D decision |
|---|---|
| Attack replacement engine | **Abandon permanently.** |
| Battle Master-style maneuver resource | **Do not use.** Drills have no shared superiority-die analogue. |
| Enhanced generic actions | **Core architecture.** |
| Damage tied to utility actions | **Reject.** Damage has an independent trigger. |
| Number of printed drills | **13.** Enough choice without becoming a second spell list. |
| Drills known | **4 / 5 / 6 / 7 / 8** at Fighter 3 / 7 / 10 / 15 / 18. |
| Attack drills | **Intentionally omitted.** The Fighter chassis already heavily enhances Attack. |
| Hide drills | **Intentionally omitted from this pass.** High Rogue/Skulker intrusion risk. |
| Magic-action drills | **Intentionally omitted.** Too item-dependent and too easy to create action-economy problems. |
| Reaction multiplication | **No.** One normal Reaction remains the ceiling. |
| Sentinel package | **No.** No broad Disengage punishment plus Speed 0. |
| Applied Mastery | **Cut.** Tactical Master already owns flexible Push/Sap/Slow. |
| Level 18 philosophy | **Adaptation, counterplay, and inevitability**, not merely another damage die. |

The resulting subclass is somewhat unusual: many of its drills are **not expected to be used every round**. That is intentional. Search, Study, Dodge, Help, Ready, and Utilize should become *good answers to the right problem*, not disguised attacks that the Veteran presses every turn to keep pace with DPR.

## Iteration D Complete Subclass Draft

**Veteran**

*Survive Long Enough to Learn Every Bad Lesson*

Veterans are campaigners who have learned that victory rarely looks clean from the ground. They know which wall will hold, which road will turn into a killing ground, when an enemy is overcommitted, and which piece of ordinary gear can solve an extraordinary problem. Their skill comes neither from magic nor command. It comes from scars, repetition, preparation, and the ugly practical knowledge required to come home alive.

A Veteran might be an aging infantryman, caravan guard, retired marine, former mercenary, siege survivor, or simply an adventurer who has spent too many years discovering what gets people killed.

### Subclass progression

| Fighter Level | Feature | Drills Known |
|---:|---|---:|
| 3 | Veteran Drills, Finish the Job, Veteran's Eye | 4 |
| 7 | Battlefield Readiness, Vigilant Response | 5 |
| 10 | Field-Expedient Fighting | 6 |
| 15 | Prepared for the Worst | 7 |
| 18 | Veteran of a Hundred Fights | 8 |

**Level 3: Veteran Drills**

You have accumulated practical techniques called **Veteran Drills**.

You know four Veteran Drills of your choice from the Veteran Drill list. You learn one additional drill when you reach Fighter levels 7, 10, 15, and 18, as shown in the table.

A drill enhances an action you actually take; knowing a drill does not let you take that action with a different action type unless the drill specifically says otherwise. For example, a Dodge drill improves the Dodge action but does not let you Dodge as a Bonus Action or replace an attack with Dodge.

Whenever you gain a Fighter level, you can replace one Veteran Drill you know with another Veteran Drill for which you qualify.

If a drill has a Fighter-level prerequisite, your Fighter level must meet that prerequisite.

**Level 3: Finish the Job**

You know when an opponent has begun to come apart.

Once on each of your turns when you hit a **Bloodied** creature with a weapon attack or with the Damage option of an Unarmed Strike, the attack deals an extra **1d6** damage of the attack's damage type.

The extra damage becomes **1d8** when you reach Fighter level 10 and **1d10** when you reach Fighter level 18.

This feature is deliberately once per turn rather than once per Attack action. Action Surge therefore improves the chance that you land the damage but does not multiply the damage package itself. That is important because the Fighter eventually makes three attacks at level 11 and four at 20 and can gain a second Action Surge use at 17. citeturn17view0turn17view1

**Level 3: Veteran's Eye**

Years of watching people make costly mistakes have taught you what details matter.

You gain proficiency in one of the following skills of your choice: **History, Investigation, Perception, or Survival**. Alternatively, you gain proficiency with one type of Artisan's Tools.

In addition, after you spend at least 1 minute examining a battlefield, campsite, fortification, road, vehicle, weapon, suit of armor, tool, damaged structure, or other comparable physical site or object, you can ask the DM one of the following questions:

| Question |
|---|
| Which position I can see appears easiest to defend against attack from the most likely direction? |
| Which route I can see appears fastest or least exposed for a group traveling on foot? |
| Where does the available evidence suggest an ambush, sentry, alarm, or concealed approach would most plausibly be placed? |
| What part of the subject shows the clearest evidence of damage, tampering, poor maintenance, instability, or recent use? |
| What practical component, supply, or piece of equipment appears missing, misplaced, unusually important, or out of place? |

The DM answers truthfully according to evidence your character could reasonably discern from the examination. The answer doesn't reveal supernatural secrets, exact game statistics, or facts for which no physical or contextual evidence exists. If there is no meaningful evidence relevant to the question, you learn that no reliable conclusion can be drawn.

You can use this question-and-answer benefit a number of times equal to your Proficiency Bonus, regaining all expended uses when you finish a Long Rest.

This is intentionally **not** Expertise and not a Tactical Mind duplicate. Tactical Mind already lets a Fighter spend Second Wind to add 1d10 to a failed ability check; Veteran's Eye instead changes the kind of actionable information the Fighter can obtain. citeturn17view0

**Level 7: Battlefield Readiness**

You rarely need the opening moments of a fight to understand that a fight has begun.

At the start of your first turn of each combat, choose one of the following options. You can't choose the same option more than once when a later Veteran feature allows you to choose multiple options.

**Take Position.** You can immediately move up to half your Speed.

**Sweep.** You immediately take the Search action.

**Assess.** You immediately take the Study action.

An action taken through this feature can benefit from a Veteran Drill you know that enhances that action.

This is the one deliberate, tightly bounded piece of action compression in Iteration D. It occurs only on the Veteran's first turn, it cannot produce Attack, Dodge, Ready, Utilize, Help, or Magic, and it cannot be repeated through Action Surge.

**Level 7: Vigilant Response**

You have learned to recognize the instant an enemy's attack leaves it exposed.

Immediately after a creature you can see misses you with an attack while it is within the reach of a melee weapon you are wielding or your Unarmed Strike, you can take a Reaction to make one melee attack against that creature with that weapon or with an Unarmed Strike.

The attack made by this feature **isn't an Opportunity Attack**.

You can use this feature a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest.

That final sentence distinguishing it from an Opportunity Attack is essential. Under the 2024 rules an Opportunity Attack is specifically a Reaction triggered by a visible creature leaving your reach using its movement, action, Bonus Action, Reaction, or one of its speeds. citeturn19view7 Keeping Vigilant Response outside that category prevents the entire ecosystem of Opportunity Attack riders from automatically attaching to it.

**Level 10: Field-Expedient Fighting**

A weapon is whatever is still in your hand when the proper weapon is gone.

You gain the following benefits.

**Improvised Weapons.** You are proficient with improvised weapons. When you hit with an improvised weapon that isn't being treated as a Simple or Martial weapon, its damage die is a d6 instead of a d4. When you make a melee attack with such an object while wielding it in two hands, you can use a d8 instead if the object can reasonably be wielded that way.

This feature doesn't give an improvised weapon a mastery property. If the DM determines that an improvised weapon is sufficiently similar to a Simple or Martial weapon to use that weapon's rules, use the normal weapon's rules instead.

The qualification matters because the default 2024 improvised-weapon rules deny proficiency, use a d4 damage die, and already allow the DM to treat a sufficiently similar object as an ordinary weapon. citeturn19view9

**Hard-Knuckle Fighting.** When you use the Damage option of an Unarmed Strike, its damage die is a d6. The die is a d8 while you are holding neither a weapon nor a Shield. This feature doesn't change the ability score used for the attack or its damage. If another feature gives your Unarmed Strike a larger damage die, use the larger die rather than combining the dice.

The baseline 2024 Unarmed Strike can deal damage, Grapple, or Shove; its ordinary Damage option deals 1 plus Strength modifier, while Grapple and Shove use their own saving-throw rules. citeturn19view8 Field-Expedient Fighting improves only the Damage option and therefore does not directly improve grapple or shove DCs.

**Experienced Eye.** When you use Veteran's Eye, you can ask **two different questions** instead of one.

**Level 15: Prepared for the Worst**

Experience has taught you that a plan need not survive contact with the enemy if you already prepared for its failure.

Whenever you finish a Short or Long Rest, you can replace one Veteran Drill you know with another Veteran Drill for which you qualify.

In addition, your Battlefield Readiness improves in two ways:

First, add the following option to Battlefield Readiness.

**Brace.** You gain Temporary Hit Points equal to your Fighter level. These Temporary Hit Points disappear when the combat ends.

Second, whenever you use Battlefield Readiness, you choose **two different options** instead of one.

**Level 18: Veteran of a Hundred Fights**

There are few mistakes left that someone hasn't already made in front of you.

Your Battlefield Readiness improves again: you now choose **three different options** when you use it.

In addition, you gain the following benefits.

**Read the Threat.** Once per round, immediately after a creature you can see hits you with an attack or you fail a saving throw caused by that creature, you can read its methods. That creature becomes your **Read Threat** until the start of your next turn. You can have only one Read Threat at a time; choosing another ends the previous designation.

When you designate your Read Threat, you can immediately move up to 10 feet. This movement doesn't provoke Opportunity Attacks from the Read Threat.

While a creature is your Read Threat, its attack rolls against you have Disadvantage, and you have Advantage on saving throws it forces you to make.

**Punish the Mistake.** If your Read Threat misses you with an attack while it is within the reach required by Vigilant Response, you can use Vigilant Response against it without expending one of that feature's uses. You must still expend your Reaction normally.

Nothing in this feature gives you an additional Reaction.

This is intentionally a large capstone. It allows the Veteran to learn from the *first* successful hit or failed save and become much harder for the same enemy to defeat by repetition. It does not prevent the initial failure, doesn't protect against every enemy simultaneously, doesn't grant offensive Advantage, doesn't create another turn, and doesn't multiply Reactions.

### Veteran Drill list

The following thirteen drills are the recommended Iteration D menu.

**Field Advance — Dash.** When you take the Dash action, you gain 10 feet of additional movement for the current turn, and Difficult Terrain costs you no extra movement for the rest of that turn.

The extra movement is deliberately modest. Dash already grants additional movement, and the 2024 Speedy feat itself includes improved movement and a Dash-over-Difficult-Terrain benefit, so this drill should not attempt to become a second mobility feat. citeturn16view0

**Hold Ground — Dodge.** When you take the Dodge action, you gain Temporary Hit Points equal to your Fighter level. These Temporary Hit Points disappear at the start of your next turn. Until the start of your next turn, you also have Advantage on Strength, Dexterity, and Constitution saving throws made to avoid the Grappled or Prone condition or to resist being moved against your will.

This is intentionally strong because Dodge consumes an entire action. The ordinary Dodge action already imposes Disadvantage on visible attackers and gives you Advantage on Dexterity saves until your next turn, so the drill focuses its added value on bracing and survivability rather than adding still more attack-roll penalties. citeturn19view0

**Shield the Line — Dodge.** When you take the Dodge action while wielding a Shield, choose one other creature within 5 feet of yourself. Until the start of your next turn, that creature has Half Cover while it remains within 5 feet of you and you aren't Incapacitated.

This is support through physically interposing yourself, not a command aura. It costs your whole action and therefore should not be confused with free protective reactions.

**Fire-Team Assist — Help.** When you take the Help action to Assist an Ability Check, you can assist an ally within 30 feet of yourself if that ally can see or hear you and the assistance can reasonably be communicated verbally or by gesture. When you use Help to Assist an Attack Roll, the enemy you distract can be within 15 feet of you instead of 5 feet.

All other requirements of the Help action apply. In particular, the DM still determines whether assistance on an ability check is actually possible. The base 2024 Help rule expressly gives the DM that authority and normally requires the enemy used for attack assistance to be within 5 feet. citeturn19view1

**Common Soldier's Tongue — Influence.** *Prerequisite: Fighter level 10.* When you take the Influence action to urge a guard, soldier, mercenary, sailor, caravan worker, laborer, craftsperson, or similarly practical working person to do something, you have Advantage on an ability check required by that action if your request concerns immediate safety, passage, shelter, work, equipment, supplies, local dangers, or another practical matter related to that creature's experience.

This drill cannot cause an unwilling creature to become hesitant or willing, alter a creature's attitude, or make a creature comply without a check when the normal Influence rules would require one.

That restriction is important because under the 2024 Influence action the DM first decides whether the creature is willing, unwilling, or hesitant; a check occurs for the hesitant case rather than social ability checks functioning as mind control. citeturn19view3

**Hair Trigger — Ready.** *Prerequisite: Fighter level 7.* When you take the Ready action and choose the Attack action as the action you will take with your Reaction, the first weapon attack you make as part of that readied action has Advantage, provided you haven't made an attack since taking the Ready action. If that attack hits, the target can't take Reactions until the start of its next turn.

If you make an attack before the readied attack occurs, you lose this drill's benefits for that use of Ready.

This restriction is specifically there to prevent the obvious Action Surge sequence of making a full offensive Attack action and then obtaining subclass-granted Advantage on an off-turn readied attack. Ready normally consumes your action and later your Reaction, while Fighter Extra Attack grants its additional attacks when you take the Attack action **on your turn**. citeturn16view4turn17view1 The intended use is genuine overwatch, not an Action Surge nova extender.

**Spot the Shooter — Reaction/Search.** *Prerequisite: Fighter level 7.* Immediately after an attack made by a creature you can't see resolves against you, you can take a Reaction to take the Search action, but only to make a Wisdom (Perception) check to locate that attacker.

This is intentionally narrow. It neither reveals magical invisibility automatically nor grants an attack; it converts your Reaction into an immediate attempt to locate a threat that has just exposed itself.

**Sweep the Ground — Search.** When you take the Search action and make a Wisdom (Perception) check, you can choose a 30-foot Cone originating from yourself. The same check searches that area for concealed creatures, concealed objects, and perceptible signs of traps or hazards. Compare the result against each applicable DC in the area. You learn only information your senses could actually perceive.

The ordinary Search action covers Perception for concealed creatures and objects and Survival for tracks, but it doesn't prescribe a standardized tactical search area; this drill gives the Veteran a clean battlefield sweep rather than a numerical bonus. citeturn19view4

**Size Up — Study.** When you take the Study action, you can use a creature you can see within 60 feet as the source of knowledge you are studying. If the Intelligence check succeeds, choose one of the following subjects: **defenses, movement, attacks, or apparent condition**. The DM tells you one useful qualitative fact about the chosen subject that could reasonably be inferred from the creature's appearance, equipment, behavior, or known lore.

This drill never reveals exact Armor Class, Hit Points, ability scores, saving-throw modifiers, attack bonuses, spell slots, legendary-resource counts, or a hidden trait that cannot reasonably be inferred.

Once you use this drill successfully on a creature, you can't use it on that creature again until you finish a Long Rest.

The 2024 Study action is explicitly an Intelligence check drawing on memory, clues, books, or other sources of knowledge; its skill table associates History with wars and Humanoids, Investigation with mechanisms, Nature with several creature types and terrain, and so forth. citeturn19view5 The Veteran expands what can count as a practical source, but not into unrestricted stat-block extraction.

**Veteran Appraisal — Study.** When you take the Study action to examine a nonmagical weapon, suit of armor, vehicle, fortification, tool, mechanism, barricade, or other manufactured object and the Intelligence check succeeds, choose one of the following questions:

**Weak Point:** What part appears most susceptible to physical failure or interference?

**Condition:** What is the most significant visible damage, wear, tampering, or poor maintenance?

**Function:** What does this object's construction suggest about how it is operated or intended to function?

**Missing Part:** What component appears absent, incorrect, or most important to restoring normal operation?

The DM answers according to what can reasonably be learned from inspection and relevant knowledge. This drill doesn't reveal magical properties.

**Sabotage — Utilize.** When you take the Utilize action to jam, wedge, sever, obstruct, or disable a nonmagical object or mechanism that isn't worn or carried by another creature, you have Advantage on any ability check required to do so. On a success, restoring the sabotaged object to immediate use requires a Utilize action even if clearing the obstruction could otherwise have been accomplished with an ordinary object interaction.

This drill doesn't allow an object to be damaged or disabled when doing so would otherwise be physically impossible.

That closed effect is preferable to an open-ended “Dirty Trick” drill. The 2024 Utilize action is specifically the action used when an object requires an action for its use, and mundane adventuring gear already provides examples of objects whose combat operation uses Utilize. citeturn19view6turn17view7

**Quick Barricade — Utilize.** *Prerequisite: Fighter level 10.* When you take the Utilize action to move or brace an unattended, nonmagical object within your reach that you are capable of lifting or dragging, you can move that object up to 5 feet as part of the action. If the object is large and solid enough to block at least half of a Medium creature's body, it can provide Half Cover to a Medium or smaller creature positioned directly behind it relative to an attacker until the object is moved.

The DM determines whether an object is sufficiently large and solid to function as cover.

This is one of the few places where DM physical adjudication is unavoidable and desirable: a table, overturned cart, heavy door, or crate is different from a blanket or chair leg. The rule nevertheless has a closed mechanical payoff—Half Cover—rather than inviting improvised conditions.

**Hook and Turn — Opportunity Attack.** *Prerequisite: Fighter level 7.* When you hit a creature with an Opportunity Attack using a melee weapon or an Unarmed Strike, and the target is no more than one size larger than you, you can force it to make a Strength saving throw. The DC equals 8 plus your Proficiency Bonus plus the ability modifier you used for the attack. On a failed save, you move the target up to 5 feet to an unoccupied space you can see within your reach.

This drill doesn't make Disengage provoke an Opportunity Attack and doesn't reduce the target's Speed to 0.

That is a deliberate boundary. The current 2024 Sentinel feat is explicitly built around features named Guardian and Halt, while Polearm Master contains its own Reactive Strike; the Veteran should not reproduce their control package for free. citeturn16view0

## Rules Compatibility and Design Rationale

Iteration D is designed around a simple principle: **the 2024 action names are interfaces, not currencies.** A drill says “when you take the Search action” because Search is a defined Wisdom-check action; “when you take Study” because Study is a defined Intelligence-check action; “when you take Utilize” because Utilize governs objects requiring an action; and so on. citeturn19view4turn19view5turn19view6 It does not create a parallel category called a Veteran Action that then needs rules for what counts as one, how it interacts with Extra Attack, whether it is an action for other features, and whether Action Surge changes it.

That is the principal improvement over Iterations A and B.

**What was salvaged from Iteration A:** Veteran's Eye; longer-range practical Help; the “enemy misses the veteran” half of Vigilant Response; improvised fighting; improved unarmed damage; readiness; sabotage; battlefield-position analysis; and a limited Opportunity Attack control concept.

**What was salvaged from Iteration B:** the closed-menu idea and prerequisite levels. The menu itself survived, but the maneuvers-with-another-name presentation did not.

**What was rejected:** attack replacement; Bonus Action Veteran Actions; Tactical Blow after utility actions; Applied Mastery; Influence as attack economy; Magic-item action compression; free Dodge while attacking; multiple Veteran Actions per turn; broad Disengage punishment; Speed 0 on every Opportunity Attack; and reaction multiplication.

There is especially good historical reason not to simply reskin Battle Master. When Wizards discussed earlier Cavalier development, it specifically described feedback that players regarded superiority-die maneuvers as Battle Master's territory and disliked propagating the same subsystem into another Fighter archetype. citeturn15search7 The 2024 Battle Master also retains the established number and scaling of its Superiority Dice and maneuvers, and its revised Know Your Enemy now uses a Bonus Action to reveal concrete Immunities, Resistances, and Vulnerabilities. citeturn16view1 Veteran therefore should **not** get another pool of dice plus a list of attack riders, and Size Up deliberately provides qualitative observation rather than Battle Master's exact combat intelligence.

The omissions in the drill list are equally intentional.

| Omitted action | Why |
|---|---|
| **Attack** | Weapon Mastery, Tactical Master, Extra Attack, and Studied Attacks already heavily enrich Fighter attacks. Another menu of attack riders is where Veteran most quickly turns into Battle Master. citeturn17view0turn17view1turn17view5turn17view6 |
| **Hide** | The 2024 Hide action has explicit cover/obscurement and line-of-sight requirements and grants Invisible while hidden. Relaxing those requirements is disproportionately Rogue/Skulker-shaped, while many Strength Veterans will also wear armor that already imposes Stealth Disadvantage. citeturn19view2turn17view6 |
| **Magic** | The Magic action encompasses spells, features, and magic-item activation. Action Surge expressly excludes the Magic action. A subclass drill that compresses “magic item use” risks either campaign-dependent dead text or accidental circumvention of that restriction. citeturn16view3turn17view0 |
| **Disengage** | Tactical Shift already gives the Fighter half-Speed movement without provoking Opportunity Attacks when Second Wind is activated. A Veteran-specific Disengage package would be unusually redundant. citeturn17view0 |

This draft also avoids stepping heavily onto Rogue identity. Nothing grants a recurring Bonus Action Dash, Hide, Search, Study, or Utilize. Most drills still cost the full normal action, so using them during ordinary combat has a genuine opportunity cost. Battlefield Readiness is the exception, but it is locked to the start of the first turn and only permits movement, Search, Study, and eventually temporary HP. It cannot be used to perform the usual high-value combat actions for free.

It similarly avoids Bard intrusion. Common Soldier's Tongue gives conditional Advantage on a narrow category of Influence checks rather than Expertise, automatic success, altered attitudes, or broadly superior Charisma. The underlying Influence rules expressly let the DM decide whether an NPC is willing, unwilling, or hesitant before a check occurs. citeturn19view3

The Ranger boundary is less clean but still defensible. Veteran's Eye and Search/Study drills can address routes, tracks, camps, and threats, but they are **local, evidence-based, and procedural** rather than granting broad wilderness supremacy, magical tracking, animal abilities, or exploration spells. The flavor should stay focused on *campaigning through dangerous places*, not being nature's preeminent scout.

Finally, the subclass respects the Weapon Mastery layer rather than competing with it. Push, Sap, Slow, Topple, Vex, Graze, Nick, and Cleave already produce substantial weapon differentiation; Tactical Master later lets Fighters substitute Push, Sap, or Slow for their weapon's normal mastery. citeturn17view1turn17view5turn17view6 Hook and Turn is therefore a 5-foot Opportunity Attack reposition, not “also add Push,” and no drill adds a second mastery property to an ordinary hit.

## Power-Level and Optimization Analysis

### Damage contribution

The Veteran's predictable subclass DPR comes primarily from **Finish the Job**. That is intentional. The drills should create tactical value; they should not be hiding an additional DPR engine.

For a transparent baseline, I modeled:

- 65% ordinary hit probability per attack;
- 87.75% hit probability with Advantage;
- one, two, three, or four Fighter attacks according to Extra Attack progression;
- the target already being Bloodied on 50% of the Veteran's offensive turns as a middle-of-the-road assumption;
- no magic weapon;
- no critical-hit contribution to the bonus die;
- no Cleave or Nick extra attack;
- no Action Surge;
- no off-turn attacks.

The core formula is:

`Expected Finish the Job DPR = P(target Bloodied) × P(at least one hit) × average bonus die`

with

`P(at least one hit) = 1 − (1 − p)^number of attacks`.

The resulting **subclass-only** contribution is:

| Fighter Level | Attacks | Bonus Die | Expected DPR, 65% hit and Bloodied half the time | With Advantage | Expected if target is Bloodied every turn |
|---:|---:|---:|---:|---:|---:|
| 3 | 1 | d6 | **1.14** | **1.54** | **2.28** |
| 5 | 2 | d6 | **1.54** | **1.72** | **3.07** |
| 7 | 2 | d6 | **1.54** | **1.72** | **3.07** |
| 10 | 2 | d8 | **1.97** | **2.22** | **3.95** |
| 11 | 3 | d8 | **2.15** | **2.25** | **4.31** |
| 15 | 3 | d8 | **2.15** | **2.25** | **4.31** |
| 18 | 3 | d10 | **2.63** | **2.74** | **5.26** |
| 20 | 4 | d10 | **2.71** | **2.75** | **5.42** |

That is a healthy shape. **It scales, but it does not explode with Fighter attack count.** With three or four attacks, the Veteran is mostly improving the reliability of landing its once-per-turn die rather than multiplying it.

It is also weapon-neutral. Sword-and-board, great weapon, reach weapon, ranged, Nick/TWF, and unarmed builds all receive approximately the same subclass increment once their hit probabilities are similar. That is preferable to a subclass whose power changes by 50–100% depending on whether the player discovered one particular attack-count package.

Action Surge does not double the rider because Finish the Job is once per turn. It merely makes a miss-out increasingly unlikely. Likewise, Vex and Studied Attacks can make the rider more reliable, but they cannot multiply its die; Studied Attacks already grants Advantage on the next attack against a creature after the Fighter misses it. citeturn17view1 Graze is also well behaved: Graze deals ability-modifier damage on a miss, but Finish the Job explicitly requires a **hit**, so a Graze miss does not trigger it. citeturn17view5

This is substantially safer than Tactical Blow. Tactical Blow had the wrong incentive structure: the subclass ostensibly encouraged Search, Study, Help, and Utilize, but optimal players were incentivized to ask, “What is the cheapest Veteran Action I can press to turn on my damage?” Finish the Job instead says, “When the enemy is hurt, the Veteran becomes slightly better at closing.”

### Vigilant Response and nova

Vigilant Response is the larger optimization variable.

A single ordinary reaction attack is roughly worth the expected value of one weapon attack. As a rough illustration, a one-handed d8 weapon with +5 damage produces 9.5 damage on a hit, or about 6.2 expected damage at 65% hit before criticals and other riders. A 2d6 weapon with +5 produces 12 on a hit, or 7.8 expected before mastery; Graze can raise the miss floor because it deals the attack ability modifier even when the attack roll misses. citeturn17view5

That sounds large relative to the Finish the Job numbers, but Vigilant Response is constrained in four ways:

**It needs the enemy to miss. It needs that enemy to be in your melee reach. It consumes your only Reaction. It has Proficiency Bonus uses per Long Rest until the capstone.**

Consequently, I would expect the level 7–17 Veteran's overall damage to sit **above Champion in favorable melee encounters but below an aggressively expended Battle Master or spell-enabled Eldritch Knight nova ceiling**. That is a design target, not a proven empirical ranking.

At level 18, the Read Threat feedback loop becomes a real subclass engine: once a foe has hurt the Veteran, subsequent attacks from that foe suffer Disadvantage, making a miss more likely; a miss can then produce a free-use Vigilant Response, still constrained by the Veteran's single Reaction. This could contribute another single attack—often roughly 6–10 expected damage—on a favorable boss round. It therefore requires serious playtesting, but it is appropriately high-level rather than an accidental level-3 damage exploit.

### Action economy

The architecture is unusually clean here.

The subclass uses **no routine Bonus Action at all**. That is a major compatibility advantage. Second Wind already occupies a Bonus Action, and Tactical Shift attaches movement to that use; current feat and weapon packages can also create Bonus Action competition. citeturn17view0turn16view0 Veteran leaves that lane alone.

Its **Reaction economy is intentionally crowded**. A Veteran can use an ordinary Opportunity Attack, Vigilant Response, Spot the Shooter, a readied action through Hair Trigger, or feat-based reactions—but only one until the start of the Veteran's next turn because that is the normal 2024 Reaction rule. citeturn17view8 That is good tension. The old “one Reaction on every turn” feature would have removed the tension entirely and turned every new reaction-based option, feat, subclass feature, and magic item into future balance debt.

Its **action economy remains costly**. Dodge, Dash, Help, Ready, Search, Study, and Utilize normally compete with Attack, exactly as they should. At level 11, passing up three attacks to Dodge is expensive. Hold Ground therefore needs to be materially better than ordinary Dodge without pretending that every defensive turn should equal three attacks in damage.

Hair Trigger deserves particular attention. Ready normally costs an action and later a Reaction, and the readied response occurs after its trigger; Extra Attack specifies taking the Attack action **on your turn**, which is why a readied off-turn Attack normally does not carry the Fighter's multiattack progression. citeturn16view4turn17view1 Hair Trigger makes that one delayed attack accurate and tactically disruptive. The “no intervening attack” clause deliberately shuts off the Veteran-specific benefit in an Attack → Action Surge → Ready double-dipping line.

### Comparison with published Fighter baselines

| Baseline | Veteran position |
|---|---|
| **Champion** | Veteran is markedly more complex and has far more exploration/control utility. Champion receives expanded crit range at 3 and 15, another Fighting Style at 7, recurring Heroic Inspiration in combat at 10, and strong Bloodied regeneration at 18. citeturn17view3turn17view4 Veteran should exceed Champion's tactical agency but should not be allowed to turn that into effortless permanent DPR superiority. |
| **Battle Master** | Veteran should lose the nova comparison. Battle Master retains its established Superiority Dice/maneuver scaling and concrete maneuver effects. citeturn16view1 Veteran instead has at-will situational action enhancements, physical problem-solving, and no superiority-die resource loop. |
| **Eldritch Knight** | Veteran should have the lower theoretical ceiling. Current 2024 optimizer guides emphasize Eldritch Knight's ability to combine Fighter weapon competence with spellcasting and spell/attack integration, and community optimization discussion frequently points to it as a high sustained-damage/defense option under permissive spell assumptions. citeturn18search4turn18search16turn18search3 Veteran's compensation is reliable nonmagical utility with no spell-slot dependence. |
| **Psi Warrior** | Veteran is less burst/resource driven and less overtly defender-oriented; Psi Warrior remains part of the 2024 PHB lineup after being imported from Tasha's with revisions. citeturn15search13 Veteran should occupy “practical generalist” rather than psionic protector space. |
| **Rune Knight, legacy** | Rune Knight's identity prominently uses magical runes, many activated through Bonus Actions or Reactions. citeturn15search16 Veteran avoids magic and has substantially less per-rest supernatural control, while occupying some of the same broad “more things to do than attack” appeal. |
| **Cavalier/Sentinel territory** | Veteran deliberately has only Hook and Turn plus a self-defense riposte. It does not automatically punish attacks against allies, make Disengage fail, or universally stop movement. |

Current optimizer conversations are not unanimous enough to justify pretending there is a single 2024 Fighter DPR benchmark. For example, community comparisons disagree on Champion versus Battle Master once different masteries and magic weapons enter the model, while other current discussions put Eldritch Knight at the high end of sustained Fighter damage. citeturn18search6turn18search3 That uncertainty strengthens the case for evaluating Veteran primarily by **incremental subclass value**, rather than attaching it to one artificially precise “standard Fighter DPR” spreadsheet.

### Utility and control

Veteran's exploration/social package is much stronger than Champion's and more consistently mundane than Eldritch Knight's. It is deliberately less mathematically potent than Rogue/Bard Expertise. Veteran's Eye is the important feature here because it produces **answers**, not merely a +2 or Advantage ribbon.

The risky part is GM dependence. Size Up, Veteran Appraisal, and Veteran's Eye are only as good as the information the GM returns. The closed question/category structure is therefore not cosmetic; it is the mechanism that makes these features playtestable.

Sabotage and Quick Barricade are potentially excellent encounter features because they interact with physical spaces without inventing free conditions. This is an area in which a mundane high-level character can have real agency without pretending a chair is equivalent to *Wall of Force*. The 2024 equipment rules already treat ordinary equipment as action-bearing mechanics—for example, a hunting trap uses Utilize and can reduce Speed to 0 on a failed save—so “gear matters” is compatible with the current rules vocabulary rather than being a foreign subsystem. citeturn17view7

## High-Level Martial vs. Full Caster Context

The level 15 and 18 features should **not** be judged only against Champion's numeric improvements.

At character level 15, full casters have access to 8th-level spells. A spell such as *Maze* can use one action to banish a visible creature into a demiplane and potentially remove it from the encounter while Concentration continues. citeturn20search2 Even 7th-level *Forcecage* creates a large force prison at range and can radically redefine an encounter. citeturn20search3

At character level 17+, a full caster can have 9th-level effects. *Foresight* lasts eight hours and grants its target Advantage on D20 Tests while imposing Disadvantage on attacks against that target. citeturn20search1 *Wish* can, at its baseline, duplicate any spell of level 8 or lower without normal casting requirements and has broader reality-altering options beyond that. citeturn20search0

That does **not** mean a level 18 Fighter subclass should receive a mundane *Wish*. It does mean that “+1d8 once per turn and one extra skill proficiency” would be an indefensibly timid capstone standard.

**Prepared for the Worst at level 15 is mechanically meaningful but narratively conservative.** Fifteen Temporary Hit Points every combat plus a free Search/Study/movement option and another free setup option can materially alter the Veteran's first turn, and rest-based drill replacement makes the character adaptable. But it still operates inside a conventional encounter rather than changing what kinds of problems the party can solve.

I think that is acceptable for the base playtest, **but it is the first feature I would strengthen if high-tier testing feels flat**. The clean stronger version is not another attack or action. It is:

> **Stronger level 15 test variant:** When you roll Initiative, choose one Veteran Drill for which you qualify that you don't know. You know that drill until the combat ends.

That produces high-tier “I have seen this situation before” adaptability without creating another resource pool. I would not put it into the first Iteration D draft because it increases choice latency at Initiative—the exact place Battlefield Readiness already asks the player to make decisions.

**Veteran of a Hundred Fights at 18 is intentionally bolder.** The closest conceptual comparison is not damage; it is a sharply limited, reactive form of *Foresight*. Unlike the spell, it doesn't give general Advantage, doesn't affect every attacker, doesn't function before the enemy successfully hurts you, doesn't last eight hours, and doesn't make every D20 Test better. citeturn20search1 But once a specific enemy demonstrates a successful technique, repeatedly using that technique against the Veteran becomes substantially worse.

That is the correct kind of high-level martial power for this subclass: **the enemy still gets to do impossible things; the Veteran gets increasingly difficult to beat with the same mistake twice.**

The 10-foot reposition is important to the narrative weight. Against a melee creature that expended most of its movement reaching the Fighter, one successful attack can teach the Veteran enough to step out of the remaining sequence. Against a ranged or magical opponent, the movement instead lets the Veteran seek cover or change angles. Against multiple opponents, however, the feature cannot defend against all of them because only one Read Threat exists.

The defensive math is substantial without being absolute. If an enemy normally hits 65% of the time and makes three sequential attacks, making attacks after its first successful hit at Disadvantage reduces the expected number of hits from about 1.95 to roughly 1.60 before accounting for the Veteran's repositioning—about an 18% reduction from the attack-roll adaptation alone. Against four sequential attacks, the reduction is roughly 22%. Those are model results, not rules claims, and real values vary with AC and attack bonuses.

The level 18 feature therefore sits in the range I want for the first high-level playtest: **aggressive, memorable, and capable of frustrating a boss, but local rather than reality-altering**. It does not compete with *Wish* on breadth and should not. It competes by functioning repeatedly, without spell slots, against the immediate physical problem the Fighter is standing in front of.

If testing shows that Veteran of a Hundred Fights still feels too conservative, I would strengthen **Read the Threat's tactical control**, not its damage. The next escalation I would test is allowing the 10-foot movement to pass through Difficult Terrain without extra cost and allowing the Veteran to stand from Prone as part of that movement. I would **not** give another Reaction, a free Dodge, another Attack action, or blanket damage resistance.

## Red Flags, Multiclass and Feat Interactions

The draft is substantially safer than Iterations A–C, but several interactions deserve deliberate stress testing.

| Interaction | Assessment |
|---|---|
| **Action Surge** | Mostly safe. Finish the Job remains once per turn. Battlefield Readiness is first-turn-only and isn't an Action Surge option. Hair Trigger loses its benefit if the Veteran attacks after readying, specifically blocking the subclass from rewarding Attack + Action Surge + Ready nova sequencing. Action Surge's existing ban on the Magic action remains untouched. citeturn17view0 |
| **Tactical Mind** | Complementary rather than redundant. Tactical Mind modifies failed checks numerically; Veteran's Eye changes what information can be obtained. citeturn17view0 |
| **Tactical Shift** | Some thematic overlap with movement exists, but Field Advance requires Dash and Battlefield Readiness's Take Position does not suppress Opportunity Attacks. Tactical Shift retains its distinctive Second-Wind-linked no-OA movement. citeturn17view0 |
| **Tactical Master** | Safe by design. Veteran never adds Push/Sap/Slow on top of a mastery. Tactical Master already lets the Fighter substitute those properties. citeturn17view1 |
| **Studied Attacks** | Safe. Size Up doesn't grant attack Advantage; Studied Attacks retains its distinct miss-to-Advantage loop. citeturn17view1 |
| **Vex** | Increases Finish the Job reliability by improving subsequent hit probability but cannot increase the once-per-turn die count. Vex itself grants Advantage on a later attack after a hit. citeturn17view6 |
| **Graze** | Safe. Graze deals damage on a miss, whereas Finish the Job requires a hit. citeturn17view5 |
| **Push/Slow/Sap** | No direct stacking feature. Hook and Turn can add distinct 5-foot repositioning only on an Opportunity Attack. Slow already has its own nonstacking 10-foot reduction. citeturn17view5turn17view6 |
| **Nick / two-weapon fighting** | Veteran doesn't create another Light attack or consume the Bonus Action, so it is highly compatible but doesn't multiply Nick. Nick already moves the Light-property extra attack into the Attack action and is once per turn. citeturn17view5 |
| **Polearm Master** | High-priority test. Reach can enlarge the practical territory for melee reactions, while Polearm Master itself has Pole Strike and Reactive Strike. Veteran still has only one Reaction, so the main interaction is competition rather than multiplication. citeturn16view0turn17view5 |
| **Sentinel** | **Highest control-risk feat pairing.** Hook and Turn should be tested specifically with Sentinel's current Guardian/Halt package. Veteran deliberately does not contain either Disengage punishment or a Speed-0 effect by itself. citeturn16view0 |
| **Great Weapon Master** | No direct multiplier on Finish the Job. The larger concern is simply that Vigilant Response can be a high-value single heavy-weapon attack. Because it remains limited and reaction-bound, this looks acceptable but needs table testing. |
| **Sharpshooter** | Low risk. Most of Veteran's reaction offense is melee. Hair Trigger is useful to ranged Fighters but adds accuracy/control to one readied attack rather than an extra ranged attack. The 2024 feat itself focuses on cover, melee firing, and long range rather than the 2014 damage tradeoff. citeturn16view0 |
| **Shield Master** | Potentially good but not abusive on paper. Shield the Line asks the Veteran to spend Dodge; Shield Master separately provides Shield Bash and Interpose Shield. citeturn16view0 |
| **Mage Slayer** | Read the Threat can overlap with defensive benefits from Guarded Mind, but multiple sources of Advantage do not compound into stronger-than-Advantage rolls. The feat remains useful for its other functions. Its current listing includes Concentration Breaker and Guarded Mind. citeturn16view0 |
| **Grappler** | Important. The 2024 Unarmed Strike already supports Damage/Grapple/Shove, and Grappler is built to combine unarmed offense with grappling. Field-Expedient Fighting raises the damage floor but does not raise grapple DC or create extra attacks. citeturn19view8 |
| **Tavern Brawler** | Important overlap test. The current feat listing already includes Enhanced Unarmed Strike, Damage Rerolls, Improvised Weaponry, and Push. Field-Expedient Fighting must not combine damage dice additively with it; the draft's “use the larger die” rule handles the most obvious problem. citeturn16view0 |
| **Rogue multiclass** | Hair Trigger was deliberately written to avoid handing an Attack → Action Surge → Ready sequence subclass-granted Advantage after an on-turn attack. A Fighter/Rogue can still use the normal Ready rules to seek an off-turn Sneak Attack when normal Sneak Attack conditions are met; that interaction exists independently of Veteran. |
| **Monk multiclass** | The unarmed die can interact with Monk features, but the explicit “use the larger die” rule prevents additive damage dice. Field-Expedient Fighting also doesn't change which ability score is used, so Monk-specific ability substitution remains Monk's own feature rather than Veteran granting Dexterity unarmed attacks. |
| **Barbarian multiclass** | No apparent engine. Advantage makes Finish the Job reliable, but it remains once per turn and scales by Fighter level rather than total level. |
| **Paladin / Ranger / Warlock multiclass** | No new spell-smite or magic-action compression. Three Fighter levels buy only the d6 Finish the Job version and four drills; they do not create additional spell actions. |
| **Wizard / Eldritch Knight-style spellcasting** | Intentionally safe. There is no Magic drill, no “activate an item in place of an attack,” and nothing rewrites Action Surge's restriction. citeturn16view3turn17view0 |

The most important exploit test is therefore **not raw DPR**. It is the triangle of **reach weapon + Polearm Master + Sentinel + Hook and Turn/Vigilant Response**.

The rule that Vigilant Response is *not* an Opportunity Attack should remain non-negotiable. Without it, every future feature that says “when you hit with an Opportunity Attack” potentially becomes part of the subclass's ordinary retaliation engine.

The second highest-risk interaction is **level 18 Dodge tanking**. A Veteran who takes Dodge, knows Hold Ground, becomes someone's Read Threat target, and retains a Reaction can be extremely difficult to attack efficiently. That is partly intended: spending a full level-18 Fighter action on Dodge means giving up three attacks. The playtest question is whether the defensive return becomes so great that “Dodge every boss round and make one counterattack” becomes the dominant tactic. If it does, reduce Hold Ground's Temporary Hit Points before weakening the capstone.

The third risk is **information throughput** rather than combat math. A level 15 Veteran can start combat by using two Battlefield Readiness options, potentially making both Search and Study checks before its ordinary action. At level 18 it can choose three options. If Size Up and Sweep the Ground require the DM to pause combat for several minutes of adjudication, the subclass has failed even if perfectly balanced numerically.

## Playtesting Roadmap and Open Questions

Iteration D is ready for playtesting, but it is **not ready for publication**. Several pieces should remain deliberately provisional.

The first test should be the **core tier-2 loop at Fighter 7–10**. Use sword-and-board, great weapon, glaive/polearm, ranged, and Nick/two-weapon Fighters. Run fights in which the Veteran sometimes has a reason to Dash, Dodge, Help, Search, Study, Ready, and interact with terrain. The key question is not “did every drill get used?” It is **whether players ever willingly choose the enhanced action when the situation calls for it**. If the answer is still “I would always rather Attack,” improve that particular drill's *action-specific outcome*, not its damage.

Second, test **Finish the Job at three Bloodied frequencies**: roughly one-quarter, one-half, and three-quarters of offensive turns. The table above suggests the rider is deliberately modest at a 50% assumption. If actual play produces very low access because the DM rarely communicates Bloodied state or enemies die too quickly after becoming Bloodied, the feature could feel nearly absent. The cleaner fix would be to expand the trigger slightly—not to reconnect damage to utility drills.

Third, aggressively test **Vigilant Response**. Record not just uses, but *trigger opportunities*. A Proficiency-Bonus-per-Long-Rest feature is irrelevant if melee enemies miss within reach only once per adventuring day, and excessive if a high-AC shield Fighter can provoke the trigger almost every round. The right tuning knobs are number of uses and trigger condition. Do not solve an overperformance problem by making it an Opportunity Attack; that would create more interactions, not fewer.

Fourth, test **Polearm Master and Sentinel together**, then separately. The current feat index confirms that Polearm Master contains a reaction-oriented feature and Sentinel contains Guardian/Halt, which makes them the obvious control stress tests. citeturn16view0 Hook and Turn should remain a 5-foot reposition unless testing demonstrates that even that is excessive with reach.

Fifth, test **Hair Trigger with Rogue multiclassing and Action Surge**. The “benefit is lost if you attack before the readied attack occurs” sentence is inelegant, but it closes a real optimization concern. If testers routinely misread it, simplify the drill even at the cost of some power. A safer fallback is:

> **Hair Trigger — conservative variant.** When you take the Ready action and ready a weapon attack, a creature hit by that attack can't take Reactions until the start of its next turn.

That version is less exciting but almost impossible to exploit.

Sixth, test **Field-Expedient Fighting with Tavern Brawler, Grappler, and Monk levels**. Tavern Brawler already occupies improvised/unarmed design territory in the current feat set, while the base Unarmed Strike can Damage, Grapple, or Shove. citeturn16view0turn19view8 If the feature mostly reads as “you received an origin feat's damage package ten levels late,” cut the d8 unarmed clause and make Field-Expedient Fighting more distinct rather than adding more numbers.

Seventh, put **Veteran's Eye, Size Up, and Veteran Appraisal in the hands of multiple DMs**. Give them the feature text without explaining designer intent. The feature passes if different DMs tend to provide similarly useful *types* of information. It fails if one DM gives “the west wall is cracked and poorly braced” while another thinks the only legal answer is “you don't know.” The fixed categories should reduce that variance, but this cannot be solved by mathematics.

Eighth, test **Quick Barricade and Sabotage in prepared environments**: tavern, ship, siege tower, dungeon, city street, forest camp, workshop, bridge, warehouse. Quick Barricade is likely to range from excellent to unusable depending on map dressing. That variation is thematic, but the drill should not require the DM to conveniently spawn waist-high crates everywhere.

Ninth, test **Common Soldier's Tongue against actual Influence adjudication**. It should produce credibility with working people, not let the Fighter substitute Constitution for Charisma, issue orders to strangers, or bypass the willing/hesitant/unwilling framework. The 2024 Influence structure provides a strong safety rail if the drill continues to modify only actual checks. citeturn19view3

Tenth, monitor **bonus-action neutrality** as a feature rather than a bug. Because Veteran doesn't consume the Bonus Action, two-weapon, Polearm Master, and Second Wind builds should feel comfortable. If this causes Veteran's optimized DPR to outperform other subclasses, the answer is probably to tune Vigilant Response or Finish the Job—not to add an arbitrary subclass Bonus Action tax. Second Wind and Tactical Shift already give the Fighter meaningful reasons to care about that action lane. citeturn17view0

Eleventh, evaluate **D&D Beyond implementation separately from tabletop readability**. The drill menu is substantially easier to encode conceptually than Iteration A because every drill can exist as a self-contained selectable option rather than rewriting Attack/Extra Attack. The potentially awkward pieces are the changing known-drill count, prerequisites, and level-15 rest-based drill replacement. If the builder cannot automate those cleanly, manual drill selection is preferable to redesigning the tabletop rules around tooling limitations.

Finally, run **at least several level-18 boss encounters** before weakening Veteran of a Hundred Fights. High-level play is the wrong place to panic because a martial character finally feels oppressive to one enemy. At the same levels, casters can employ effects on the scale of *Maze*, *Foresight*, and *Wish*. citeturn20search2turn20search1turn20search0 The relevant questions are narrower:

| Level-18 test question | Failure signal |
|---|---|
| Does Read the Threat noticeably alter how a dangerous enemy engages the Veteran? | If no, the capstone is too weak. |
| Can it completely invalidate a boss before the boss has a meaningful first success? | If yes, it is too strong; the current trigger is intended to prevent this. |
| Does it make multiple enemies irrelevant? | If yes, the one-Read-Threat restriction is not doing enough work. |
| Does it create more than one Reaction per round? | Any “yes” is a rules failure. |
| Does the 10-foot movement regularly delete the remainder of melee Multiattack sequences? | If nearly always, test reducing it to 5 feet before removing it. |
| Is Dodge + Hold Ground + Read Threat the dominant action every round? | If yes, first reduce Hold Ground's Temporary Hit Points. |
| Does the feature feel narratively high-level despite being mundane? | If no, strengthen tactical adaptability before adding damage. |
| Does the Fighter have consequential things to contribute during investigation, travel, fortifications, negotiations, and equipment problems? | If no, strengthen Veteran's Eye/Appraisal/Sabotage rather than adding another combat maneuver. |

The central design principle for the next pass should remain firm: **the Veteran should not be the Fighter who receives more ways to disguise an Attack action. It should be the Fighter who has accumulated enough experience that actions other warriors dismiss as “not attacking” can sometimes be the correct move.**

Iteration D gets substantially closer to that goal than the attack-replacement or maneuver-pool versions. Its largest unresolved risks are **Vigilant Response with optimized reaction builds, the level-18 Read Threat feedback loop, GM consistency on information drills, and whether full-action drills remain attractive once Extra Attack reaches three attacks**. Those are finite, testable problems. The previous architecture's problems were structural.