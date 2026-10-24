# Veteran Fighter Subclass — Comprehensive Current-State and Design-History Report

**Project:** DnD Homebrew — Veteran Fighter  
**Rules target:** D&D 2024 / 5.5e Fighter  
**Purpose:** Authoritative handoff for a Work-mode polishing audit before releasing a public testing build  
**Current status:** Mechanically mature but not yet publication-ready. Most major subclass features are provisionally solved; remaining work is wording, integration, roster consolidation, exploit review, and structured playtest preparation.

---

## 1. How to Use This Report

This report consolidates the Veteran Fighter work completed across the main development thread, the branched research work, the September 30 research reports, and the later **Attack-Action Utility Experiment**.

For the polishing audit, use this authority order:

1. **Newest explicit decisions in this report and the conversation that produced it.**
2. **The current provisional mechanics recorded below.**
3. **Veteran_Attack_Action_Utility_Experiment_Report.md** for the newly added Attack-action utility Lessons.
4. **Veteran_Level_3_Combat_Identity_2026-09-30.md** for the Practical Fighting investigation.
5. **Veteran_Fighter_Design_Investigation_2026-09-30.md** and the focused Change the Plan follow-up as research/advisory material.
6. **Veteran_Work_Context_Pack.md** and **Veteran_Current_State_Addendum_2026-09-30.md** for earlier accepted structure and wording.
7. **VETERAN FIGHTER SUBCLASS — MASTER PROJECT HANDOFF.md**, D.4.2, D.4.1, and older chat history only where newer work has not superseded them.

Older research recommendations are **not canon merely because they appear in a report**. The current conversation deliberately departed from several of them.

Status vocabulary used here:

- **Provisionally locked / current:** use this as the testing-build direction unless the polishing audit finds a concrete rules, clarity, or balance defect.
- **Awaiting playtest:** theory work is considered sufficient; do not keep redesigning without evidence.
- **Wording open:** concept is accepted, but exact publishable text still needs work.
- **Experimental:** retained for consideration but not part of the current roster.
- **Rejected / superseded:** do not silently restore.

---

## 2. Core Fantasy and Design Thesis

The Veteran is an experienced, older, mundane front-line soldier and campaigner. The subclass is not an officer, commander, noble champion, magical warrior, or famous hero. Its power comes from:

- hard-earned experience;
- practical fieldcraft;
- preparedness;
- observation;
- tactical adaptability;
- familiarity with danger;
- improvised solutions;
- efficient use of equipment;
- knowing when a conventional technique is the wrong answer;
- surviving enough fights to recognise recurring patterns.

The strongest thematic formulation reached during development is:

> **A new fighter learns the proper way to fight. A Veteran has learned when the proper way is the wrong way.**

Related design principle:

> **The Veteran is not defined by mastery of one perfect technique, but by knowing when to stop using the obvious one.**

The subclass should feel like someone who has been through sieges, marches, ambushes, boarding actions, bad terrain, cramped fights, equipment failures, wounded retreats, and opponents who refuse to cooperate with textbook technique.

### Boundaries

The Veteran should not become:

- a Battle Master with another maneuver list;
- a Warlord/Banneret-style commander;
- a Rogue replacement;
- a Ranger with military flavour;
- a Bard-like general support class;
- a Cavalier/Sentinel lockdown specialist;
- an Eldritch Knight without spells;
- a generic “dirty tricks” subclass that depends on open-ended DM negotiation.

The Veteran may temporarily help fill secondary party roles, but should not match a specialist’s repeatable core engine.

---

## 3. Current High-Level Architecture

| Fighter Level | Current Veteran Features |
|---|---|
| **3** | **Hard-Won Lessons**, **Practical Experience**, **Practical Fighting** |
| **7** | **Battlefield Readiness**, fifth Lesson |
| **10** | **Been Here Before**, sixth Lesson |
| **15** | **No Lesson Wasted** *(name now provisional)*: Reserve Readiness, Dig Deep, Brace improvement; seventh Lesson |
| **18** | **Veteran of a Hundred Fights**, eighth Lesson |

### Lessons Known

The progression remains:

- Fighter 3: **4 Lessons**
- Fighter 7: **5 Lessons**
- Fighter 10: **6 Lessons**
- Fighter 15: **7 Lessons**
- Fighter 18: **8 Lessons**

The roster is intentionally larger than the number known. Different Veterans should feel materially different.

### Hard-Won Lesson governing principle

Unless a Lesson says otherwise, it modifies only the action or Reaction named by the Lesson and does not transform that action into another action.

The newly added **Attack-action utility Lessons** are a deliberate, bounded exception: each one explicitly replaces **one attack** with one specific procedure. This is **not** a return to the rejected universal “replace attacks with arbitrary actions” engine.

---

# 4. Level 3 Features

## 4.1 Hard-Won Lessons

Hard-Won Lessons are the subclass’s main customization spine. They represent techniques, habits, tricks, remembered procedures, practical knowledge, and hard-earned experience.

The current provisionally accepted roster is detailed in Section 9.

The original 14-Lesson roster has expanded through later development. The current working roster contains **22 provisionally accepted/current Lesson concepts**, with several additional Attack-action ideas remaining experimental.

---

## 4.2 Practical Experience

**Status: provisionally solved.**

You gain proficiency in one of the following skills of your choice:

- Animal Handling
- Athletics
- Insight
- Intimidation
- Investigation
- Medicine
- Perception
- Stealth
- Survival

Then choose one skill from that list in which you are proficient. You gain Expertise in that skill.

### Design purpose

This replaces the older, bloated Veteran’s Eye package. It gives the Veteran credible noncombat competence without rebuilding Rogue Expertise or attaching a large assessment subsystem to a ribbon feature.

No additional tool proficiency is currently included here because tool/equipment identity is better handled through Lessons.

---

## 4.3 Practical Fighting

**Status: provisionally solved / awaiting playtest.**

Practical Fighting replaced the former Change the Plan combat identity. It intentionally treats melee and ranged fighting asymmetrically.

### Practical Contact

You gain proficiency with improvised weapons.

The Damage option of your Unarmed Strike deals **1d6 + your Strength or Dexterity modifier** bludgeoning damage.

A held weapon, worn Shield, or similar implement can represent the **Damage or Shove** option of an Unarmed Strike against a creature within 5 feet.

When an implement is used this way:

- the attack is still an Unarmed Strike;
- it does not inherit the implement’s weapon properties;
- it does not inherit Weapon Mastery;
- it does not inherit the implement’s magical attack bonuses, damage, or other magical benefits.

Normal Unarmed Strike rules remain in force. Practical Contact does not automatically make Dexterity the ability used for Grapple or Shove, does not remove free-hand requirements, and does not change size restrictions.

### Close Work

**Once during each Attack action you take on your turn**, after you make a melee weapon attack, you can make a **full 2024 Unarmed Strike** against a creature within 5 feet.

That Unarmed Strike can use:

- Damage;
- Grapple;
- Shove.

If Damage is chosen, Practical Contact’s d6 Strength-or-Dexterity damage applies.

### Hit or Correct

**Once during each Attack action you take on your turn**, after you make a ranged weapon attack, you can move up to **half your Speed without provoking Opportunity Attacks**, then make one additional ranged weapon attack.

- If the triggering attack **hit**, the additional attack must target a **different creature**.
- If the triggering attack **missed**, the additional attack can target the **same creature or a different creature**.
- You do not add a **positive ability modifier** to the additional attack’s damage.
- Normal range, ammunition, Loading, and other weapon requirements still apply.
- The generated attack cannot recursively trigger Practical Fighting.

### Shared-use intent

The polishing audit should make explicit that Practical Fighting has **one application per Attack action**, not one Close Work plus one Hit or Correct in the same Attack action unless a later explicit decision changes that.

### Current playtest watchpoints

Do not redesign these pre-emptively; test them:

- whether Close Work becomes an automatic damage routine instead of an interesting choice;
- Grappler interaction;
- sequencing with Topple, Push, Vex, Graze, and Tactical Master;
- interaction with Studied Attacks at Fighter 13;
- magic/rider value on the ranged follow-up;
- Action Surge creating a second application because it creates another Attack action;
- whether Hit or Correct remains satisfying against single and multiple targets;
- whether the no-ability-modifier restriction is enough at high levels.

The September 30 combat-identity report explicitly concluded that the missing evidence is table data, not more theorycrafting. Treat Practical Fighting as **awaiting playtest**, not as a current redesign target.

---

# 5. Level 7 — Battlefield Readiness

**Status: provisionally solved.**

Battlefield Readiness expresses that an experienced Veteran starts a fight already doing the practical thing.

### Current structure

When combat starts, before you roll Initiative, choose **two different** Battlefield Readiness options.

**Counter-Ambush** resolves immediately. The other chosen options resolve at the start of your first turn in the combat, in either order.

An action taken through Battlefield Readiness can benefit from a Hard-Won Lesson you know that modifies that action.

### Counter-Ambush

If you are Surprised, you do not have Disadvantage on your Initiative roll from being Surprised.

### Take Position

Move up to **half your Speed**.

This is ordinary movement. The current version does **not** add blanket Opportunity-Attack immunity.

### Read the Field

Take the **Search or Study action**.

This replaces the old separate Sweep and Assess options. It keeps both information modes while avoiding the old problem where Study/Assess was a weak or trap choice before Find the Weak Point became available.

### Brace

Gain Temporary Hit Points equal to your **Proficiency Bonus**.

At Fighter level 15, this becomes **twice your Proficiency Bonus**.

### Design notes

Battlefield Readiness is deliberately outside the Lesson menu. It is a core Veteran competency, not another selectable technique.

The two-choice structure is accepted. The current option roster is considered healthy enough for a testing build.

---

# 6. Level 10 — Been Here Before

**Status: provisionally solved.**

Been Here Before represents bounded adaptability without giving the Veteran unrestricted access to the entire Lesson list on demand.

The previous “recall any unknown Lesson” design was rejected because it encouraged the player to learn only evergreen Lessons permanently and use universal recall for niche situations.

## Change of Approach

Whenever you finish a **Short or Long Rest**, you can replace **one** Veteran Lesson you know with another Lesson for which you qualify.

## Reserve Lessons

Whenever you finish a **Long Rest**, choose **two** Veteran Lessons for which you qualify and that you do not know. These are your Reserve Lessons until you choose again.

When you take an action or Reaction that could benefit from one of your Reserve Lessons, you can use that Lesson as though you knew it.

You must decide to do so before making any roll required by the action or Reaction.

Once you use a Reserve Lesson this way, you cannot do so again until you finish a **Short or Long Rest**.

Using Been Here Before does not bypass, restore, or alter a Lesson’s own usage limits.

### Design intent

This produces three different time scales of adaptation:

- **Known Lessons:** the Veteran’s regular repertoire.
- **Reserve Lessons:** the two contingencies anticipated for the current adventuring day.
- **Change of Approach:** a single known-Lesson adjustment after a rest when new information changes the mission.

This is preparation, not martial spellbook access.

---

# 7. Level 15 — Current Feature Package

## Working feature name: No Lesson Wasted

**Status: mechanics provisionally locked; feature name is now open.**

The old version centred on broad Lesson reshuffling. That was judged too administrative and too weak for a level-15 feature. The current package instead interacts more strongly with the Fighter chassis and Battlefield Readiness.

The polishing audit should strongly consider whether **No Lesson Wasted** still fits as the published name.

## 7.1 Reserve Readiness

Once per combat, at the start of one of your turns **after your first turn**, you can immediately use one Battlefield Readiness option you have not already used in that combat:

- Take Position;
- Read the Field;
- Brace.

Counter-Ambush is excluded because Initiative has already been resolved.

This is the “the first plan was not the only plan” portion of the feature.

## 7.2 Dig Deep

When you use **Action Surge**, you can expend one use of **Second Wind** to regain Hit Points from Second Wind **without using a Bonus Action**.

When you do so, you can also use **Tactical Shift** as though you had activated Second Wind with its normal Bonus Action.

### Design intent

Dig Deep ties together three core Fighter systems:

- Action Surge;
- Second Wind;
- Tactical Shift.

It is intentionally broadly useful and gives the Veteran a powerful high-level “keep going” moment without simply adding direct bonus damage.

## 7.3 Improved Brace

At Fighter level 15, Brace grants Temporary Hit Points equal to **twice your Proficiency Bonus** instead of your Proficiency Bonus.

### Superseded level-15 ideas

Do not restore without a new explicit decision:

- Finish the Wounded damage scaling;
- broad full-roster Lesson retraining as the primary level-15 payoff;
- an Initiative-time “learn any unknown Lesson for the whole combat” clause;
- extra Reactions;
- a generic damage die;
- extra Practical Fighting uses beyond what Action Surge naturally creates.

---

# 8. Level 18 — Veteran of a Hundred Fights

**Status: provisionally solved.**

At the start of each of your turns in combat, choose one creature you can see.

Until the start of your next turn:

- you have **Advantage on attack rolls** against that creature;
- you have **Advantage on saving throws** that creature forces you to make;
- that creature has **Disadvantage on attack rolls** against you.

### Off-turn attacks

The offensive Advantage intentionally applies for the full duration, including:

- Opportunity Attacks;
- Hair Trigger attacks;
- other qualifying attacks made outside your turn.

The earlier research report flagged off-turn Advantage as a watchpoint, not a demonstrated problem. The current decision is to **keep it**.

### Design intent

The Veteran becomes exceptionally good at handling one dangerous opponent because they recognise the pattern of threat and know how to fight it.

The feature is intentionally stronger against one major enemy and weaker against hordes.

---

# 9. Current Hard-Won Lessons Roster

## 9.1 Level-3 / Base-Access Lessons

### Forced March — Dash

When you take the Dash action:

- gain **10 additional feet** of movement associated with the action;
- Difficult Terrain costs you no extra movement until the end of the turn.

**Status:** keep.

---

### Break Through — Dash

When you take the Dash action:

- you can move through the space of a hostile creature that is no more than one size larger than you;
- your movement does not provoke Opportunity Attacks from creatures whose spaces you enter this way;
- the first time you enter each such creature’s space that turn, it makes a Strength or Dexterity saving throw against your Unarmed Strike save DC;
- on a failed save, it is pushed **5 feet** to an unoccupied space adjacent to its original space.

**Status:** provisionally locked.

**Polish point:** specify who chooses Strength or Dexterity for the save.

This replaced **Break Contact**, which became too weak after Parting Blow was added.

---

### Field Concealment — Hide

When you take the Hide action:

- armor-imposed Disadvantage on the Hide check does not apply;
- on a successful Hide, choose up to your Proficiency Bonus willing creatures within 30 feet that can see or hear you;
- for 10 minutes, you and those creatures have Advantage on Dexterity (Stealth) checks made as part of the Hide action and ignore armor-imposed Disadvantage on those checks;
- this does not waive the normal requirements to Hide.

The team benefit is usable **once per Short or Long Rest**.

**Status:** keep / wording polish only.

---

### Shield the Line — Dodge

When you take the Dodge action, choose a willing creature within 5 feet.

That creature has **Half Cover** while it remains within 5 feet of you, until the start of your next turn, and while you are not Incapacitated.

**Status:** keep.

---

### Hold Ground — Dodge

When you Dodge, you brace until the start of your next turn.

While braced:

- you have Advantage on saving throws and ability checks made to avoid being knocked Prone, becoming Grappled, or being moved against your will;
- if an effect would move you against your will without allowing a saving throw or ability check, reduce that movement by **10 feet**, to a minimum of 0;
- if you become Grappled, your Speed becoming 0 does not by itself cause you to lose the benefits of Dodge.

**Status:** provisionally solved.

---

### Fire-Team Assist — Help

When you take the Help action to assist an attack roll, you can distract a creature within **30 feet** of you instead of 5 feet.

Until the start of your next turn, allied attack rolls against that creature have **Advantage until one of them hits**.

When an attack benefiting from this Lesson hits, the attacker can immediately move up to **10 feet without provoking Opportunity Attacks from that creature**.

**Status:** provisionally locked.

This intentionally covers attack coordination only. Ability-check assistance is handled by Veteran’s Correction.

---

### Two-Man Takedown — Help

When you take the Help action while within 5 feet of a creature, you can help an ally **Grapple or Shove** that creature instead of helping an attack roll.

Choose Grapple or Shove.

The next time an ally uses that option of an Unarmed Strike against the creature before the start of your next turn, the creature has **Disadvantage on its saving throw**.

**Status:** provisionally locked.

**Polish point:** verify exact 2024 terminology and timing for Grapple/Shove saving throws.

---

### Veteran’s Correction — Help

When an ally fails an ability check that had Advantage from your Help action, you can use **Tactical Mind** on that ally’s check as though you had failed the check yourself.

Roll the Tactical Mind die and add it to the ally’s check.

If the check still fails, the use of Second Wind is not expended, following Tactical Mind’s normal resource logic.

**Status:** provisionally locked.

This is intentionally Fighter-kit integration rather than another independent reroll resource.

---

### Threat Scan — Search

Threat Scan now has both a combat payoff and a broad fieldcraft component.

When you take the Search action, you have Advantage on the Wisdom check when looking for appropriate practical threats or signs, including:

- concealed creatures;
- concealed weapons or objects that pose an immediate threat;
- traps or other immediate physical dangers;
- tracks or signs that a creature recently passed through the area;
- signs of recent violence;
- evidence that an ambush or other immediate danger is imminent.

On a successful Search, the DM can also provide **one useful tactical detail** supported by the evidence you found.

If the Search locates one or more creatures, choose one.

Before the start of your next turn:

- the **first attack roll against that creature has Advantage**; and
- the **first attack roll that creature makes has Disadvantage**.

**Status:** current provisional direction.

**Polish points:** tighten the “tactical detail” boundary and ensure the first-attack clauses have unambiguous expiration and beneficiary wording.

---

### Casualty Extraction — Disengage

When you take the Disengage action, moving while dragging or carrying a willing or unconscious creature you can physically move **does not cost you extra movement until the end of the turn**.

Normal limits on what you can physically move still apply.

**Status:** provisionally locked.

This is intended to make the Veteran genuinely better at getting wounded allies out of the killing ground, not merely refund movement after a normal half-speed drag.

---

### Parting Blow — Disengage

When you take the Disengage action, you can make **one weapon attack or Unarmed Strike** at any point during your movement.

On a hit, the target’s Speed is reduced by **10 feet** until the start of your next turn.

An attack made with this Lesson cannot trigger Practical Fighting.

**Status:** provisionally locked.

This is a fighting withdrawal, not a Cunning Action clone.

---

## 9.2 Attack-Action Utility Lessons from the Latest Experiment

These are the newest additions and must be treated as part of the current project state.

The central experiment conclusion was:

> **Extra Attack can represent not only how quickly the Veteran attacks, but how quickly an experienced combatant can perform practical physical tasks during a fight.**

These Lessons replace **one attack** with a bounded procedure. They do not grant arbitrary action substitution.

### Field-Expedient Tool — Attack

When you take the Attack action, you can replace one of your attacks with a **Utilize action that targets a nonmagical object or mechanism**.

When you do so:

- you can use your weapon’s attack ability modifier in place of the ability modifier normally used for any required check;
- you add your Proficiency Bonus if you are proficient with that weapon;
- you can perform the interaction at your weapon’s reach;
- if you use a ranged or thrown weapon, you can perform an appropriate interaction within that weapon’s normal range.

This Lesson cannot target an object worn or carried by an unwilling creature and does not replace a required Tool proficiency.

Examples include cutting, levering, hammering, probing, manipulating mechanisms, triggering distant objects, rough repair, and similar practical physical tasks.

**Status:** provisionally locked.

**Level placement:** not yet explicitly finalized in the experiment report; no prerequisite was specified.

**Polish points:** define when an interaction is “appropriate” at range, ensure it does not bypass tool requirements, and reconcile its embedded Utilize action with any “once per action” or object-interaction rules.

---

### Break Their Hold — Attack

When you take the Attack action, you can replace one attack to interfere with a creature within reach.

The target makes a Strength or Dexterity saving throw against your Unarmed Strike save DC.

On a failed save, choose one:

- the creature ends one Grapple it is maintaining; or
- the creature drops one chosen object it is holding.

This also absorbs the earlier basic Disarm concept.

**Status:** provisionally locked.

**Level placement:** not yet explicitly finalized.

**Polish points:** specify who chooses the save ability, define “within reach” if a weapon has extended reach, and verify worn/secured objects and two-handed holdings.

---

### Misdirect with Sound — Attack

Replace one attack to deliberately create a distracting sound at another location.

Current intended asymmetry:

- a ranged or thrown weapon can create the sound somewhere within its normal range when the fiction supports it;
- a melee-focused Veteran can instead throw a small object, tentatively at a shorter range such as **30 feet**.

The intended payoff is that creatures which hear the distraction without seeing its source become worse at determining where another creature actually is, such as suffering **Disadvantage on an appropriate Perception check**.

**Status:** concept provisionally locked; exact wording remains open.

**Polish points:** range, valid sound source, duration, affected creatures, what exact check is penalised, whether it affects Search, and how it interacts with hiding/Invisible creatures.

---

### Deliver an Object — Attack

When you take the Attack action, replace one attack to throw a small carried object to a willing creature within a bounded range.

The recipient can use its **Reaction** to catch the object if it has a free hand. Otherwise the object lands nearby.

Potential uses include:

- passing a potion;
- delivering ammunition;
- throwing a key;
- sending tools;
- passing a torch;
- delivering another needed piece of equipment.

Delivering an object does **not** also activate, drink, use, equip, or otherwise operate the object.

**Status:** provisionally locked.

**Level placement:** not yet finalized.

**Polish points:** exact range, object size/weight, line of effect, whether the recipient must see the object, landing-space rules, and whether a Shield/occupied hand affects the catch.

---

## 9.3 Level-7 Lessons

### Hair Trigger — Ready

**Prerequisite: Fighter level 7**

When you take the Ready action and ready the Attack action using a weapon or Unarmed Strike, then use your Reaction to take that readied Attack action:

- you make the **same number of attacks** you could make with the Attack action on your turn;
- once during that readied Attack action, one hit deals an extra **1d10 damage** of a type dealt by the attack.

**Status:** provisionally solved / awaiting playtest.

This fixes the old scaling problem at Fighter 11 and 20.

Playtest with Action Surge, the level-18 capstone, Sentinel/Opportunity Attack builds, and high-level magic weapons.

---

### Hook and Turn — Opportunity Attack

**Prerequisite: Fighter level 7**

When you hit a creature with an **Opportunity Attack**:

- the attack deals an extra **1d10 damage** of a type dealt by the attack;
- if the target is Large or smaller, move it up to **5 feet** to an unoccupied space within your reach.

The movement does not have to be directly away from you.

**Status:** keep.

Polearm Master’s separately named Reactive Strike is not automatically an Opportunity Attack.

---

## 9.4 Level-10 Lessons

### Common Soldier’s Tongue — Influence

**Prerequisite: Fighter level 10**

This Lesson now has both a combat application and a broader social/fieldcraft application.

#### Combat application

Against a **Bloodied** creature that can understand you, a reasonable battlefield demand such as:

- surrender;
- retreat;
- drop a weapon;
- release someone;
- cease fighting;

can, when appropriate, be treated as **Hesitant rather than Unwilling** for the Influence action.

This does not make suicidal, absurd, magically compelled, or fundamentally impossible requests possible.

#### Fieldcraft ribbon

When dealing with soldiers, guards, mercenaries, dangerous labourers, caravan workers, sailors, and comparable practical workers:

- you have Advantage on appropriate Influence checks concerning practical matters such as danger, supplies, routes, pay, working conditions, security, fortifications, logistics, or survival;
- ordinary conversation can also surface useful local practical information they actually know and are not deliberately concealing.

**Status:** current provisional direction.

**Polish points:** exact Bloodied demand wording, willing/hesitant/unwilling interaction, hostility boundaries, language requirements, and how much information the ribbon grants without a roll.

---

### Battlefield Activation — Magic

**Prerequisite: Fighter level 10**

When you take the **Magic action to activate a magic item**, you can draw or stow that item as part of the action.

After the item’s activation resolves, you can make **one weapon attack or Unarmed Strike as a Bonus Action** before the end of the turn.

This Lesson:

- does not waive attunement or other item requirements;
- does not change the action required to activate the item;
- does not itself let Action Surge take the Magic action.

**Status:** provisionally solved / awaiting playtest.

The earlier concern about strong magic-item turns is mostly an Action Surge issue that already exists without this Lesson. Battlefield Activation generally adds one attack to that existing sequence rather than creating the sequence itself.

Stress-test, but do not pre-emptively nerf.

---

### Sabotage — Utilize

**Prerequisite: Fighter level 10**

You gain proficiency with **Thieves’ Tools or Tinker’s Tools**.

When you take the Utilize action to interfere with an accessible nonmagical object or mechanism, you have Advantage on any required check.

On a success, choose:

**Jam.** One normal function cannot be used until the sabotage is cleared.

**Rig.** The object appears functional. Choose one normal function. The next time that function is used, it fails; afterward the sabotage becomes obvious.

Choose one method:

**Hasty.**
- Takes one action.
- A creature can attempt to clear it with the Utilize action and a check against:
  **8 + your Proficiency Bonus + your Strength or Dexterity modifier**, chosen when you perform the sabotage.
- After a successful or attempted Hasty Sabotage as defined by the final wording, the current design direction allows you to make **one weapon attack or Unarmed Strike as a Bonus Action that turn**.

**Deliberate.**
- Takes 1 minute.
- Reversal requires appropriate tools or materials plus a check against the same DC.
- It cannot normally be undone merely by quickly removing an obstruction.

The sabotage must plausibly affect the mechanism. It cannot make an object fail in a way its construction cannot support. Normal object-damage rules still apply.

**Status:** current provisional direction.

**Polish point:** decide whether the Bonus Action attack requires a successful Hasty Sabotage or merely taking the Hasty attempt, and make the tool-proficiency choice permanent/clear.

---

### Quick Barricade — Utilize

**Prerequisite: Fighter level 10**

#### Combat application

When you take the Utilize action while adjacent to suitable sturdy material you can physically manipulate, arrange it into a temporary barricade covering **up to two connected 5-foot edges** (a maximum 10-foot line) within reach.

The material must plausibly be substantial enough to obstruct attacks.

Creatures behind the protected edge gain **Half Cover** against attacks and effects passing through it.

Crossing a protected edge costs **5 additional feet of movement**.

The barricade gains no supernatural durability. Use the normal AC, Hit Points, and properties of the materials involved.

#### Fieldcraft ribbon

Given appropriate materials and several minutes, the Veteran can efficiently assess and fortify:

- camps;
- rooms;
- doors;
- chokepoints;
- firing positions;
- similar defensible locations.

This can create more extensive practical fortifications than the one-action combat version, subject to the available materials and normal object rules.

**Status:** current provisional direction.

**Polish points:** exact preparation time for the ribbon, whether a check is required, how extensive the noncombat fortification can become, and whether the combat version always uses two connected edges or “up to” two.

---

### Find the Weak Point — Study

**Prerequisite: Fighter level 10**

This Lesson now applies to **creatures as well as objects**.

When you take the Study action to examine a creature, nonmagical object, structure, vehicle, fortification, mechanism, or piece of equipment you can observe, you can look for a practical weakness, opening, damaged component, poor support, vulnerable mechanism, behavioural tell, or similar exploitable detail.

On a successful Intelligence check, the DM identifies one plausible weakness supported by what the Veteran can actually observe or reasonably infer.

For **1 minute**, once per turn, when you or a creature that can see or hear your directions makes an attack roll or ability check specifically to exploit that identified weakness, that roll has **Advantage**.

The information remains valid until the subject materially changes or the weakness ceases to exist.

#### Fieldcraft ribbon

Outside combat, Study can provide useful practical information about:

- condition;
- structural failure points;
- likely causes of damage;
- appropriate repair methods;
- suitable ways to disable, force, or bypass the subject.

The Lesson must not provide raw stat-block extraction such as exact AC, HP, saving throw values, or unsupported vulnerabilities.

**Status:** current provisional direction.

**Polish points:** define the boundary for studying creatures, who determines the relevant Intelligence skill, and what qualifies as “specifically exploiting” the weakness.

---

# 10. Experimental Attack-Action Candidates Not Yet in the Current Roster

These came from the latest Attack-Action Utility Experiment but were **not** provisionally locked as roster entries.

## Open the Lane — Attack

Sacrifice one attack to help an ally reposition safely around an enemy.

**Status:** experimental.

## Spoil the Reaction — Attack

Sacrifice one attack to interfere with or temporarily deny an enemy’s Reaction.

Potentially strong enough to require a prerequisite or further restriction.

**Status:** experimental.

## Suppressing Fire — Attack

A ranged control option that discourages or complicates movement through a chosen area without increasing damage.

**Status:** experimental.

The polishing audit should not automatically add these. The project already has a large roster; consolidation is now more important than expansion.

---

# 11. Important Design Evolution and Research Findings

## 11.1 The old Attack-replacement engine was rejected

An earlier design allowed arbitrary or broad alternative actions to replace attacks. It was rejected because:

- it blurred the action economy;
- it was difficult to bound;
- it risked Magic-action and other abuse;
- it created excessive interaction complexity;
- it made every action a potential Fighter multiattack component.

The new Attack-action utility Lessons are different because each one is a **specific, closed procedure**.

Do not generalize Field-Expedient Tool into “replace attacks with any Utilize action” beyond its exact object/mechanism scope, and do not use the new Lessons as precedent for arbitrary action replacement.

## 11.2 Change the Plan research

The former Change the Plan feature used weapon↔Unarmed fail-forward chains.

Research found:

- raw damage was not demonstrably overpowered;
- the bigger problem was incentive structure;
- failed Grapple/Shove attempts became too cheap against targets likely to resist;
- ranged Veterans lacked a natural version of the feature;
- Action Surge made it stronger but did not demonstrate a broken loop;
- previous advice to turn it into a Bonus Action fallback was probably too conservative.

This led to the broader level-3 combat-identity investigation and eventually **Practical Fighting**.

## 11.3 Asymmetric melee/ranged design is intentional

The project explicitly rejected the idea that melee and ranged Veterans must have the exact same effect.

The current Practical Fighting package intentionally gives:

- close fighters body/contact integration;
- ranged fighters repositioning and correction/split-fire behaviour.

The shared identity is practical adaptation, not identical mechanics.

## 11.4 Full-action Lessons can be strong

A recurring research lesson is that Search, Study, Utilize, Influence, Help, Dodge, Ready, and similar actions can represent a severe opportunity cost for a Fighter with Extra Attack.

Therefore a Lesson that asks the Fighter to spend a full action can and often should have a **meaningful combat payoff**, especially at levels 7–10+.

This is why later revisions strengthened:

- Threat Scan;
- Common Soldier’s Tongue;
- Sabotage;
- Quick Barricade;
- Find the Weak Point;
- Fire-Team Assist.

## 11.5 Niche by campaign is acceptable; niche by tiny trigger geometry is not

A Lesson can be excellent in an infiltration, siege, naval, wilderness, urban, or magic-item-heavy campaign without being universally useful.

The goal is:

- **powerful in the right kind of game**, not
- “technically useful only if an extremely specific micro-condition happens.”

Been Here Before and Reserve Lessons help support this design philosophy, but permanent Lessons should still be desirable on their own.

---

# 12. Rejected or Superseded Material

Do not restore these without a new explicit decision:

- the broad attack-replacement / Veteran Actions engine;
- Tactical Blow;
- Finish the Wounded;
- Vigilant Response;
- Applied Mastery;
- the old multi-part Veteran’s Eye;
- Size Up as part of Veteran’s Eye;
- Field-Expedient Fighting as an entire subclass-level feature;
- broad extra-Reaction engines;
- Press the Advantage;
- the old Read the Threat / Punish the Mistake capstone;
- universal “recall any unknown Lesson exactly when needed”;
- broad full-roster Lesson reshuffling as the main level-15 payoff;
- the older weapon↔Unarmed Change the Plan as the current core combat identity;
- the research report’s proposed Bonus Action Backup Method;
- any assumption that Opportunity Attacks, Action Surge, feat synergy, or magic-item synergy must be weakened simply because they can be strong.

Older ideas can still inspire wording or isolated mechanics, but they are not current mechanics.

---

# 13. Current Feature Status Summary

## Provisionally solved / awaiting playtest

- Practical Experience
- Practical Fighting
- Battlefield Readiness
- Been Here Before
- Veteran of a Hundred Fights
- Battlefield Activation
- Hair Trigger
- most established Hard-Won Lessons

## Provisionally locked but needing publishable wording

- Break Through
- Fire-Team Assist
- Two-Man Takedown
- Veteran’s Correction
- Threat Scan
- Casualty Extraction
- Parting Blow
- Common Soldier’s Tongue
- Sabotage
- Quick Barricade
- Find the Weak Point
- Field-Expedient Tool
- Break Their Hold
- Deliver an Object

## Concept locked; wording materially open

- Misdirect with Sound

## Experimental / not current roster

- Open the Lane
- Spoil the Reaction
- Suppressing Fire

## Structural issue still open

- The **name** “No Lesson Wasted” probably no longer matches the level-15 feature.
- Exact placement/prerequisites for the newly added Attack-action utility Lessons are not yet finalized.
- The total Lesson roster may now be too large or unevenly distributed; consolidation should precede further expansion.

---

# 14. Polishing Audit Priorities for Work Mode

The next Work-mode pass should be a **polishing and release-readiness audit**, not another broad redesign exercise.

## 14.1 Reconstruct the testing-build rules text

Produce one internally consistent subclass document using only the newest current mechanics in this report.

Do not silently restore older wording because it appears in an older complete draft.

## 14.2 Official 2024 rules terminology

Verify against current official 2024 rules:

- Attack action and replacing attacks;
- Extra Attack;
- Action Surge;
- Second Wind;
- Tactical Mind;
- Tactical Shift;
- Tactical Master;
- Studied Attacks;
- Unarmed Strike Damage/Grapple/Shove;
- Opportunity Attacks;
- Ready;
- Help;
- Hide;
- Search;
- Study;
- Influence;
- Utilize;
- Magic action;
- Surprise;
- Bloodied;
- Difficult Terrain;
- cover;
- Grappled;
- dragging/carrying creatures;
- object rules;
- tool proficiency;
- weapon reach/range;
- Loading/ammunition;
- Haste and “one attack only” interactions.

## 14.3 Timing and recursion audit

For every feature, state clearly:

- when it triggers;
- whether it occurs before or after a roll;
- whether it is once per turn/action/combat/rest;
- whether generated attacks count as part of the Attack action;
- whether they can trigger Practical Fighting;
- whether a Lesson can trigger itself;
- whether Action Surge creates another opportunity;
- whether off-turn attacks benefit.

## 14.4 Hard-Won Lesson matrix

Create a matrix containing:

- name;
- level/prerequisite;
- modified action/Reaction;
- combat purpose;
- exploration/social ribbon, if any;
- action-economy cost;
- expected common use;
- major interactions;
- current status;
- potential overlap with another Lesson.

Use this to identify redundancies and trap choices.

## 14.5 Attack-action utility integration

The latest Attack-action experiment must receive special scrutiny because it is the newest subsystem expansion.

Questions:

- Are four accepted Attack Lessons too many?
- Should they all be available at level 3?
- Does Field-Expedient Tool swallow too much of Utilize or tool identity?
- Is Break Their Hold too broad when it combines grapple-breaking and disarming?
- Does Deliver an Object meaningfully justify a Lesson slot?
- Can Misdirect with Sound be written as a closed rule instead of a DM-negotiation feature?
- Do any of these recreate the rejected arbitrary attack-replacement engine in practice?
- Do they make Extra Attack disproportionately valuable for out-of-combat tasks in a way that creates strange “initiative for utility” incentives?

## 14.6 Build-diversity audit

Test hypothetical Lesson selections for:

- Strength great-weapon Veteran;
- sword-and-board Veteran;
- polearm Veteran;
- Dexterity duelist;
- archer;
- crossbow user;
- thrown-weapon Veteran;
- grappler;
- stealth/infiltration Veteran;
- siege/urban utility Veteran;
- magic-item-heavy Veteran.

Ask:

- Which Lessons become automatic picks?
- Which are never selected permanently?
- Does Been Here Before make niche Lessons more attractive or merely reduce the cost of ignoring them?
- Are there enough useful choices at level 3, 7, and 10?
- Are too many desirable Lessons gated at 10?

## 14.7 Action-economy comparison

For full-action Lessons, compare their payoff to simply taking the Attack action at:

- Fighter 3;
- Fighter 5;
- Fighter 11;
- Fighter 13;
- Fighter 15;
- Fighter 18;
- Fighter 20.

Do not assume a full-action utility Lesson must be weak because it is repeatable.

## 14.8 Official-subclass comparison

Compare the test build against 2024:

- Battle Master;
- Champion;
- Eldritch Knight;
- Psi Warrior.

Focus on:

- sustained damage;
- nova;
- control;
- defence;
- mobility;
- action compression;
- out-of-combat utility;
- resource dependence;
- subclass complexity.

Do not try to force exact numerical parity feature by feature.

## 14.9 Multiclass and feat stress tests

At minimum test:

- Monk;
- Barbarian;
- Rogue;
- Paladin;
- Ranger;
- grappling builds;
- Polearm Master;
- Sentinel;
- Great Weapon Master;
- Grappler;
- Tavern Brawler;
- Dual Wielder;
- Shield Master;
- Charger;
- Mage Slayer.

Watch especially for:

- extra on-turn Sneak Attack opportunities;
- rage + Practical Contact;
- Monk + Practical Contact;
- Grappler + Close Work;
- Sentinel/OA + Veteran of a Hundred Fights;
- Hair Trigger + Action Surge;
- Heavy-weapon riders on Hit or Correct;
- magic-item activation + Battlefield Activation + Action Surge + Dig Deep.

## 14.10 Publication wording

The final testing build should:

- read like 2024 D&D rules text;
- use consistent capitalization;
- avoid unnecessary restatement of base rules;
- avoid explanatory examples inside mechanics unless needed;
- eliminate hidden assumptions;
- keep flavour concise;
- keep DM adjudication bounded;
- make every “reasonable/plausible/appropriate” clause as narrow as practical;
- clearly label prerequisites.

The target is a **clean playtest build**, not perfect final-publication balance.

---

# 15. Structured Playtest Priorities

## Tier 1: Level 3–4

Test:

- Practical Fighting’s low-level damage increase;
- Close Work vs ordinary weapon-only turns;
- Break Through;
- Fire-Team Assist;
- Two-Man Takedown;
- Veteran’s Correction;
- Threat Scan;
- Casualty Extraction;
- Parting Blow;
- all newly added Attack-action utility Lessons that are made level-3-accessible.

Key question: does the Veteran feel versatile without having too many “free extras” before Extra Attack arrives?

## Tier 2: Level 5–10

Test:

- Practical Fighting sequencing with Extra Attack;
- full-action Lessons vs two attacks;
- Battlefield Readiness;
- Hair Trigger;
- Hook and Turn;
- new Attack-replacement Lessons with Extra Attack;
- level-10 utility Lessons;
- Been Here Before.

Key question: are utility Lessons strong enough to justify their action cost without becoming dominant?

## Tier 3: Level 11–14

Test:

- Hair Trigger with three attacks;
- Practical Fighting with three attacks;
- Action Surge interactions;
- Studied Attacks at 13;
- magic weapons and feats;
- Field-Expedient Tool with multiple attacks available.

Key question: does the Veteran’s flexibility scale naturally rather than explode through action compression?

## Tier 4: Level 15–17

Test:

- Reserve Readiness;
- Dig Deep;
- improved Brace;
- Battlefield Activation + Action Surge + Dig Deep;
- high-level utility-action opportunity cost;
- whether the level-15 feature feels substantial enough.

## Tier 4 capstone: Level 18–20

Test:

- Veteran of a Hundred Fights with off-turn attacks;
- Opportunity Attacks;
- Hair Trigger;
- Sentinel;
- four-attack Fighter 20;
- Action Surge;
- Practical Fighting;
- high-end magic weapons.

Key question: is the single-threat dominance capstone-scale but still bounded?

---

# 16. Specific Rules Questions the Polishing Audit Must Resolve

1. Does Practical Fighting permit only one branch/application per Attack action?
2. Can Haste’s one-attack-only Attack action trigger Practical Fighting without violating Haste?
3. Who chooses Strength or Dexterity for Break Through and Break Their Hold saves?
4. What exactly counts as “within reach” for Break Their Hold?
5. Can a creature resist dropping an object held in two hands, secured, strapped, or otherwise attached?
6. What exact object size/weight/range does Deliver an Object permit?
7. Can Field-Expedient Tool operate mechanisms through arrows/bolts in a way that should require a tool?
8. Does Field-Expedient Tool grant a whole Utilize action or only the specific interaction? The wording should be explicit.
9. How does Misdirect with Sound interact with Search, Perception, hiding, and Invisible creatures?
10. Does Sabotage’s Bonus Action attack require successful sabotage?
11. How much noncombat fortification can Quick Barricade’s ribbon create and how long does it take?
12. What exact skill/check does Find the Weak Point use for different creatures/objects?
13. What counts as “specifically exploiting” a Find the Weak Point result?
14. How should Common Soldier’s Tongue phrase changing an Influence request from Unwilling to Hesitant without overriding DM authority?
15. Does Fire-Team Assist’s persistent Advantage end immediately on the first hit even if that hit came from an attack that already had Advantage from another source?
16. Does Veteran’s Correction require the original Help to have been legal under the helper’s own proficiency requirements?
17. Does Reserve Readiness permit a Lesson-enhanced Search/Study exactly as opening Battlefield Readiness does?
18. Does Dig Deep trigger every time Action Surge is used at Fighter 17, subject only to available Second Wind uses?
19. Is “No Lesson Wasted” still an appropriate level-15 feature name?
20. What prerequisite levels should the new Attack-action utility Lessons have?

---

# 17. Recommended Deliverable from the Work-Mode Polishing Audit

The Work-mode audit should return:

1. **Executive verdict** — whether the Veteran is ready for a public testing build.
2. **Authority reconstruction** — confirm what mechanics were treated as current.
3. **Rules compatibility audit** — 2024 RAW/RAI issues and corrections.
4. **Full feature-by-feature wording audit.**
5. **Hard-Won Lesson matrix** with Keep / Rewrite / Merge / Cut / Experimental.
6. **Attack-action utility audit** as a dedicated section.
7. **Action-economy and exploit audit** at key Fighter levels.
8. **Feat/multiclass/magic-item stress test.**
9. **Complexity and table-speed review.**
10. **Final recommended testing-build text** for the complete subclass.
11. **Change log** from the current report to the polished build.
12. **Playtest checklist** containing only questions that actual play can answer.

The audit should be willing to make **small integration fixes** and remove redundant Lessons, but it should not reopen already solved systems without identifying a concrete defect.

---

# 18. Current Project Thesis

The subclass has evolved away from a generic “old soldier gets bonuses” concept into a specific mechanical identity:

> **The Veteran knows more practical procedures than they can keep equally ready, starts combat already prepared, can shift plans as circumstances change, and uses ordinary martial actions, weapons, body mechanics, equipment, and battlefield experience in ways less experienced fighters do not.**

Hard-Won Lessons provide the repertoire.

Practical Experience provides grounded competence.

Practical Fighting makes unconventional combat application part of normal fighting.

Battlefield Readiness expresses immediate orientation.

Been Here Before expresses prepared contingency.

The level-15 package expresses stamina and a reserve plan through the Fighter’s own core mechanics.

Veteran of a Hundred Fights expresses culmination: against one immediate threat, experience makes the Veteran extraordinarily difficult to outfight.

The Attack-action utility experiment adds one final dimension:

> **For a Veteran, Extra Attack can represent not only attacking faster, but performing practical physical battlefield tasks faster.**

That idea is promising, but it is also the newest and least integrated part of the design. The immediate next step should therefore be **consolidation, official-style wording, exploit review, and preparation of a single testing build—not further feature expansion.**
