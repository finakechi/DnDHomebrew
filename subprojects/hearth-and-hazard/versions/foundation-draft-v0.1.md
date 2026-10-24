**SYSTEM DESIGN • FOUNDATION DRAFT**

**HEARTH &**

**HAZARD**

**Fantasy Heartbreaker System Design Draft v0.1**

*A 2024-compatible fantasy adventure engine for consequential worlds*

| **STATUS**      | Foundation draft—not a complete standalone game         |
|-----------------|---------------------------------------------------------|
| **BASELINE**    | 2024 fifth-edition d20 rules / SRD 5.2.1                |
| **PRIMARY USE** | Design review, subsystem tests, and campaign conversion |
| **DESIGN DATE** | July 2026                                               |

**WORKING TITLE • WORKING RULES**

> A first playable specification for stronger exploration, environmental interaction, morale, social consequence, and structured GM adjudication—without abandoning the familiar modern D&D chassis.

# **DOCUMENT STATUS AND LEGEND**

This document is a first working specification. Rules labeled **Core Rule** form the proposed default game. Other labels indicate scope and confidence.

| **Label**                 | **Meaning**                                                                           |
|---------------------------|---------------------------------------------------------------------------------------|
| **Core Rule**             | Proposed default. Use unless the campaign explicitly replaces it.                     |
| **Optional Rule**         | A self-contained campaign dial that can be added without redesigning the whole game.  |
| **Advanced Rule**         | Adds tactical or simulation detail and may require extra tracking or conversion work. |
| **GM Guidance**           | A procedure or adjudication standard, not a player-facing power.                      |
| **Open Decision**         | A design fork that must be resolved in a later pass.                                  |
| **Research Basis**        | A factual summary of an existing game or published design discussion.                 |
| **Design Recommendation** | The proposed direction for Hearth & Hazard, including the reason for it.              |

## **Version Scope**

Version 0.1 does four jobs:

1.  Establishes the compatibility target and design pillars.

2.  Provides executable drafts of the central D20 Test, action, combat, exploration, social, and environmental procedures.

3.  Identifies modules that should remain optional.

4.  Lists decisions that must be locked before expensive class, spell, and monster rewriting begins.

It does **not** yet provide twenty levels of classes, a rewritten spell catalog, a complete equipment list, a full bestiary, or final encounter tables. Existing 2024-compatible content is expected to fill those roles during early tests.

## **Contents at a Glance**

1.  Executive Overview

2.  Design Pillars

3.  Edition and Game Influence Map

4.  Core Rules Draft

5.  Character Framework

6.  Action Economy Options

7.  Combat Draft

8.  Environmental Interactions and Fantasy Physics

9.  Exploration and Resource Management

10. Social and Roleplay Mechanics

11. Magic System Options

12. Advancement and Rewards

13. Monster and Encounter Design

14. Rules Language and Template Standards

15. Open Decisions

16. Recommended Next Steps

Appendices: Research Sources, Glossary, Quick References, and Attribution

# **1. EXECUTIVE OVERVIEW**

## **1.1 What This Game Is**

**Hearth & Hazard** is a modular fantasy adventure game built on the recognizable chassis of the 2024 fifth-edition d20 rules. A player who knows modern D&D should recognize the six abilities, Proficiency Bonus, Armor Class, Hit Points, Damage Types, Advantage and Disadvantage, saving throws, Actions, Bonus Actions, Reactions, classes, subclasses, feats, spell slots, and twenty-level progression.

The revision concentrates on the layer between a character sheet and the imagined world. It adds procedures for time, light, searches, social posture, morale, object damage, elemental interactions, hazardous terrain, momentum, retreat, faction activity, and consequences. These rules aim to make the world respond consistently without asking the GM to simulate every physical detail.

The intended play loop is:

1.  The GM gives actionable information.

2.  Players choose an approach and accept a visible risk.

3.  The rules resolve uncertainty and cost.

4.  The world changes in a way that creates another meaningful choice.

## **1.2 What This Game Is Not**

Hearth & Hazard is not:

- a strict recreation of any historic D&D edition;

- a physics engine;

- a replacement for GM judgment;

- a universal point-buy system;

- a guarantee that all published fifth-edition player options remain equally balanced;

- a conversion to Pathfinder’s full rules density; or

- an excuse to add a check, modifier, or condition to every fictional detail.

The system adds structure where repeated rulings affect planning. One-off color remains color.

## **1.3 Campaigns It Supports**

The default supports heroic fantasy expeditions in which characters are capable but the world remains dangerous: dungeon delves, wilderness travel, faction conflict, monster hunting, urban intrigue, domain growth, and long-form campaigns from local adventurers to world-shaping heroes.

Three campaign profiles are anticipated:

| **Profile**           | **Intended feel**                                               | **Default dials**                                                                                                           |
|-----------------------|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| **Heroic Expedition** | Familiar modern D&D with stronger exploration and consequences  | 2024 rest rules; weakened rather than removed Darkvision; standard encumbrance; morale and environmental interactions on    |
| **Perilous Delve**    | Resource pressure, uncertain encounters, and meaningful retreat | Slot encumbrance; safe-haven rests; limited Darkvision; dungeon turns; reaction and morale rolls; treasure-weighted rewards |
| **Mythic Campaign**   | High magic, domains, factions, armies, and extreme hazards      | Heroic recovery; domain procedures; advanced structures and vehicles; large-scale environmental effects                     |

## **1.4 Compatibility Target**

> **DESIGN RECOMMENDATION** Treat “compatible” as **usable with light conversion**, not mathematically identical. A 2024 class, spell, monster, or adventure should run at the table without reconstruction. A short conversion note may add morale, tags, Bloodied behavior, or an environmental trait.

| **Element**            | **Compatibility goal for v0.1**                                                                                                                 |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Player characters      | Existing 2024-compatible characters work unchanged unless an optional module says otherwise.                                                    |
| Classes and subclasses | Keep Action/Bonus Action/Reaction timing and twenty levels. Audit only where a module changes rest, casting, or skill permissions.              |
| Spells                 | Keep spell slots, spell levels, saves, attacks, and Concentration. Add interaction tags only when a spell meaningfully affects the environment. |
| Monsters               | Use current stat blocks. Add a Morale Score and, when appropriate, one Bloodied or environmental trait.                                         |
| Adventures             | Preserve DCs, maps, treasure, and encounter composition. Add exploration rounds only when time pressure matters.                                |
| Encounter math         | Begin with the 2024 encounter budgets, then apply documented danger flags instead of inventing a second Challenge Rating system in v0.1.        |

## **1.5 Modular Boundaries**

The proposed Core contains D20 Tests, the 2024-style action economy, structured GM adjudication, Bloodied as a trigger term, morale for non-player creatures, lightweight environmental interactions, and an exploration-round procedure that activates only under pressure.

The following remain modular until playtesting proves otherwise:

- proficiency ranks beyond Proficient and Expertise;

- three-action combat;

- wounds and lingering injuries;

- no-Darkvision play;

- real-time torches;

- slot encumbrance;

- safe-haven Long Rests;

- roll-to-cast magic;

- treasure-for-XP;

- random advancement;

- detailed structures, vehicles, and domain play.

# **2. DESIGN PILLARS**

## **Pillar 1: A Familiar d20 Foundation**

The game keeps the mental model modern D&D players already possess. Changes must earn their conversion cost. A subsystem that forces a rewrite of every class feature, spell, and monster is presumptively optional until proven essential.

**Design test:** Can a 2024 character enter a v0.1 session in under ten minutes?

## **Pillar 2: Simulation Where It Creates Choices**

Rules model fire, water, weight, light, time, morale, and scarcity when those elements change player decisions. The game does not calculate temperature gradients, tensile strength, or exact kinetic energy.

**Design test:** Does the rule help players predict, exploit, avoid, or accept a consequence?

## **Pillar 3: Procedures Before Precision**

A short repeatable procedure is more valuable than a long table of isolated rulings. Exploration Rounds, Influence, environmental interactions, morale, and hazard design each state who acts, what information is available, when a roll occurs, and what changes afterward.

**Research Basis.** Old-school dungeon procedures make time, light, wandering encounters, and careful movement interact. Contemporary procedural design discussion likewise emphasizes a repeatable order of operations rather than exhaustive rules for every case. \[R8\] \[R11\]

## **Pillar 4: Information, Choice, Impact**

The GM telegraphs facts a competent adventurer could perceive. Players choose with enough information to understand the category of risk. Resolution produces a consequential change rather than a null result.

**Research Basis.** The “Information, Choice, Impact” formulation argues that meaningful play needs all three: usable information, a real decision, and consequences that matter. \[R10\]

## **Pillar 5: Structured Adjudication, Visible Fiat**

The GM remains the final interpreter, but recurring decisions use published defaults. When the GM departs from a default, the table should know whether the departure is a temporary ruling, a creature-specific exception, or a campaign rule.

**Design test:** Could two GMs reach results in the same severity band even if their narration differs?

## **Pillar 6: Dangerous Exploration, Chosen Grit**

Time, light, supplies, retreat, and uncertain encounters matter when the campaign wants them to matter. Grit is assembled from explicit dials rather than smuggled into unrelated rules.

**Design test:** Can a heroic campaign turn off inventory pressure without breaking combat?

## **Pillar 7: Tactical Expenditure, Not Free Extras**

Strong positioning effects—trampling, pinning, shattering terrain, mass collisions—consume an Action, attack, Reaction, Recharge, spell resource, or meaningful setup. Large creatures and clever casters gain new options, not automatic bonus damage.

## **Pillar 8: Homebrewable by Construction**

Actions, hazards, environmental interactions, monsters, and optional rules use consistent templates. New content should state its trigger, cost, target, test, outcomes, duration, limits, and tags.

**Design test:** Can a GM write a new hazard on an index card without inventing syntax?

## **Priority Order When Pillars Conflict**

1.  Preserve a clear, playable ruling.

2.  Preserve player information and agency.

3.  Preserve the campaign’s chosen tone.

4.  Preserve compatibility.

5.  Preserve mathematical elegance.

6.  Preserve simulation detail.

This order deliberately places table function above theoretical completeness.

# **3. EDITION AND GAME INFLUENCE MAP**

The entries below distinguish historical fact from recommendation. “Borrow” describes a design influence; it does not imply direct text reuse.

| **Source**                              | **Borrow**                                                                                                                                                                                          | **Avoid**                                                                                                                  | **Placement**                                                |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| **D&D 5.5 / 2024**                      | D20 Tests; six abilities; bounded bonuses; Advantage/Disadvantage; Action, Bonus Action, Reaction; Bloodied; modern action names; current classes and spell chassis; object and encounter baselines | Unstructured exploration; ambiguous edge-case inheritance; relying on attrition assumptions that many tables do not use    | **Core**                                                     |
| **OD&D / Basic / B/X / BECMI**          | Dungeon turns; encounter distance and reaction; morale; retainers; resource pressure; treasure recovery; domain trajectory                                                                          | Race-as-class as the only structure; descending AC; opaque legacy tables; universal lethality                              | **Core procedures**, **Optional rewards/domain play**        |
| **AD&D 1e / 2e**                        | Effect-based saves as inspiration; training, hirelings, morale, encounter ecology, specialist equipment, consequences                                                                               | THAC0; initiative exceptions by subsystem; weapon-vs-armor matrices; restrictive class/race gates                          | **GM Toolkit**, **Optional grit**                            |
| **D&D 3e / 3.5**                        | Explicit action types; object hardness concepts; consistent keywords; broad character customization; tactical maneuvers                                                                             | Stacking modifier ecology; system mastery traps; universal attacks of opportunity; full-round lockouts as a default        | **Advanced combat**, **Template standards**                  |
| **D&D 4e**                              | Monster roles; Bloodied triggers; clean exception-based powers; terrain and skill challenges; minions and encounter jobs                                                                            | Homogenized power cadence; long status tracking; treating every noncombat scene as a combat-shaped challenge               | **Monster design**, **GM Toolkit**                           |
| **Pathfinder 1e**                       | Rich build vocabulary; combat maneuvers; archetype thinking; robust subsystems                                                                                                                      | Bonus stacking; feat taxes; encyclopedic exception density; mandatory grid precision                                       | **Optional character modules**                               |
| **Pathfinder 2e**                       | Three-action comparison; traits; degrees of success where useful; proficiency permissions; hazard templates; encounter budgets; object Hardness and vehicle collision ideas                         | Adding level to nearly every check; four degrees on every roll; converting all content to three actions; tag proliferation | **Template standards**, **Advanced modules**, **GM Toolkit** |
| **Shadowdark**                          | Roll only under meaningful pressure; no/default-limited Darkvision; real-time torch option; gear slots; reaction and morale; roll-to-cast option; compact distance language                         | Making real-time play or low HP mandatory; removing tactical maps from the default; replacing all class content at once    | **Optional peril modules**                                   |
| **Old-School Essentials**               | Ten-minute dungeon turns; one-hour torches; encounter checks; clear 2d6 reaction and morale procedures                                                                                              | Treating cautious procedure as mandatory during safe or dramatically irrelevant travel                                     | **Exploration Core when pressure is active**                 |
| **Blades in the Dark**                  | Visible progress clocks; faction projects; downtime relationships; consequences that alter position                                                                                                 | Importing stress/resistance or flashbacks wholesale into a resource game built on HP and spell slots                       | **Social/downtime toolkit**                                  |
| **Into the Odd / Electric Bastionland** | Direct fictional information; meaningful consequences; avoiding empty perception checks                                                                                                             | Removing attacks or class architecture from the compatibility baseline                                                     | **GM Guidance**                                              |
| **13th Age**                            | Monster roles; backgrounds as broad capability inspiration; campaign icons/faction relationships                                                                                                    | Abstract range and escalation mechanics as mandatory replacements for maps and standard attack scaling                     | **Optional narrative/tactical tools**                        |

> **DESIGN RECOMMENDATION** The system should feel like “2024 D&D with an expedition engine and a world-response engine,” not a collage in which every admired mechanic is simultaneously active.

# **4. CORE RULES DRAFT**

## **4.1 The Resolution Principle**

> **CORE RULE** When an attempted action has an uncertain outcome and failure would meaningfully change the situation, the GM resolves it with a D20 Test or a more specific rule. If the outcome is certain or failure has no meaningful consequence, no roll is made.

A meaningful consequence can include harm, lost time, expended resources, exposure, a worsened position, unwanted attention, incomplete information, a social cost, or an irrevocable choice. “Nothing happens; try again” is not a meaningful consequence unless the attempt itself consumes a scarce opportunity.

### **Resolution Procedure**

1.  **Establish the intent.** The player states what the character wants to accomplish and, when relevant, how.

2.  **Establish the stakes.** The GM states the obvious danger, cost, or limit a competent character would recognize.

3.  **Choose the rule.** Use a specific Action or subsystem if one applies. Otherwise choose the appropriate D20 Test.

4.  **Set ability, proficiency, and target.** The GM names the ability and DC, or the rule names them.

5.  **Resolve once.** Roll, apply modifiers, and compare the total to the DC or AC.

6.  **Change the situation.** Apply the result. A repeated attempt requires a changed approach, new resource, new risk, or additional time.

### **Example: The Floodgate**

The party wants to lift a rusted floodgate before water fills the chamber. Lifting it is possible, uncertain, and time matters. The GM calls for a DC 15 Strength (Athletics) check. Before the roll, the GM explains that failure advances the flood Hazard and leaves the lifter in the deepest water. The fighter succeeds and opens an escape route. If the party later wedges a pry bar under the gate, that changed approach can justify a new check with Advantage.

## **4.2 D20 Tests**

> **CORE RULE** A **D20 Test** is an Ability Check, a Saving Throw, or an Attack Roll. Roll 1d20, add the relevant ability modifier, add Proficiency Bonus if a rule or proficiency applies, add any other allowed modifier, and compare the total to a target number.

**D20 Test total = d20 + ability modifier + applicable Proficiency Bonus + other modifiers**

If the total equals or exceeds the Difficulty Class or Armor Class, the test succeeds. Otherwise it fails. A specific rule can define additional outcomes.

### **Natural 1 and Natural 20**

- On an **Attack Roll**, a natural 1 misses and a natural 20 is a Critical Hit, as in the compatibility baseline.

- On an **Ability Check** or **Saving Throw**, a natural 1 or 20 has no universal automatic effect unless a rule says otherwise.

- A subsystem may use a natural 1 or 20 as a trigger for a complication or enhanced result, but must say so explicitly.

> **DESIGN RECOMMENDATION** Do not make natural 1s automatic failures on all Ability Checks. Doing so makes experts fail routine tasks at a flat 5 percent rate and creates implausible group-check behavior.

## **4.3 Ability Checks**

> **CORE RULE** An **Ability Check** tests a creature’s attempt to overcome uncertainty through talent, training, tools, or approach. The GM chooses the ability that best matches the method. A skill or tool proficiency applies when its training is materially relevant.

The skill name does not determine the approach. A character may make:

- a Strength (Intimidation) check to bend a prison bar as a threat;

- an Intelligence (Medicine) check to identify an unfamiliar disease;

- a Constitution (Athletics) check to sustain a long-distance swim; or

- a Charisma (Investigation) check to draw useful testimony from a neighborhood.

These combinations are permissions, not a mandate to find an unusual ability for every roll.

### **Assistance**

A helper must describe useful assistance and must be capable of attempting the task. If the task benefits from one helper, the primary creature has Advantage. More helpers do not stack additional Advantage unless a specific group procedure applies.

### **Group Checks**

When a group succeeds or fails together, each participating creature makes the same Ability Check. The group succeeds if at least half succeed. Use a group check for collective stealth, rowing through rapids, or crossing unstable ground—not for six characters independently searching the same drawer.

### **Passive Scores**

A **Passive Score** equals 10 + all modifiers that normally apply to the check. Advantage adds 5; Disadvantage subtracts 5. Passive Scores are best used to determine what a creature notices without actively rolling or to set a DC against another creature’s action.

A Passive Score should reveal a clue or observable sign when that creates play. It need not reveal the entire cause, solution, or consequence.

## **4.4 Saving Throws**

> **CORE RULE** A **Saving Throw** resists an effect that acts on a creature. The source of the effect chooses the saving throw ability and DC. A creature normally does not choose to make a Saving Throw; the effect calls for one.

Use abilities by the kind of resistance required:

| **Ability**  | **Typical resistance**                                                        |
|--------------|-------------------------------------------------------------------------------|
| Strength     | Being moved, crushed, pinned, restrained, or physically overpowered           |
| Dexterity    | Avoiding an area, maintaining footing, or reacting to a visible sudden threat |
| Constitution | Enduring poison, disease, exhaustion, suffocation, or bodily transformation   |
| Intelligence | Piercing false logic, hostile psychic structure, or memory alteration         |
| Wisdom       | Resisting fear, compulsion, deception of the senses, or loss of self-command  |
| Charisma     | Asserting identity, presence, soul, or planar belonging                       |

When a new effect could plausibly use two abilities, its rule should either choose one or let the target choose between the two. Do not improvise a third “better” save after the target rolls.

## **4.5 Attack Rolls**

> **CORE RULE** An **Attack Roll** tests whether an attack hits a target. Roll 1d20, add the attack’s ability modifier and applicable Proficiency Bonus, then compare the total to the target’s Armor Class.

Melee weapon attacks normally use Strength. Finesse weapons can use Dexterity. Ranged weapon attacks normally use Dexterity. Spell attacks use the spellcasting ability named by the feature.

An attack roll resolves contact, timing, defense, and luck; it does not guarantee that every hit visibly pierces armor. Hit Point loss can represent injury, fatigue, position, or spent luck until the fiction establishes a specific wound.

## **4.6 Advantage and Disadvantage**

> **CORE RULE** If a creature has Advantage on a D20 Test, roll two d20s and use the higher. With Disadvantage, roll two and use the lower. Multiple sources of the same state do not add more dice. If both apply, they cancel and the test uses one d20, regardless of how many sources grant either.

Apply Advantage or Disadvantage when circumstances substantially favor or hinder the whole attempt. Use a changed DC when the task itself is easier or harder for anyone.

**Example:** A greased wall is harder to climb, so its DC rises. A climber using a proper rope has Advantage because that character’s approach is especially favorable.

## **4.7 Heroic Inspiration**

> **CORE RULE** A player character can have one **Heroic Inspiration** at a time. After rolling any die, the player may expend it to reroll that die and must use the new result. A player may give unspent Heroic Inspiration to another player character who lacks it.

The GM awards Heroic Inspiration when a character:

- accepts a material complication because of a Drive, Bond, Oath, or Obligation;

- takes a costly action that reveals the character’s convictions;

- fulfills a session or adventure objective in a way that creates further play; or

- earns it from a specific feature.

Heroic Inspiration is not awarded merely for speaking in character or performing for table approval.

> **OPEN DECISION** The final name may remain **Heroic Inspiration** for compatibility, change to **Fortune**, or become a two-point **Luck** pool. This draft keeps one-point Heroic Inspiration.

## **4.8 Proficiency**

> **CORE RULE** A creature adds its Proficiency Bonus once to a D20 Test when it has a proficiency that materially applies. If a rule grants **Expertise**, the creature instead adds twice its Proficiency Bonus. A Proficiency Bonus cannot be multiplied more than once or added more than once unless a rule explicitly says otherwise.

Proficiency establishes both a bonus and fictional permission. A character without the appropriate training may still attempt ordinary tasks. The GM may require training for specialist tasks such as identifying an obscure magical cipher, performing surgery, forging a royal seal, or piloting an unfamiliar spelljammer under pressure.

### **Optional Capability Ranks**

> **OPTIONAL RULE** Use five ranks as permissions while preserving bounded accuracy.

| **Rank**      | **Bonus**               | **Permission**                                                                        |
|---------------|-------------------------|---------------------------------------------------------------------------------------|
| **Untrained** | No Proficiency Bonus    | Attempt ordinary tasks; specialist tasks may be impossible without assistance or time |
| **Trained**   | Proficiency Bonus       | Attempt specialist tasks in the field                                                 |
| **Expert**    | Twice Proficiency Bonus | As Expertise; recognize advanced methods and reduce routine time                      |
| **Master**    | Twice Proficiency Bonus | Automatically complete routine professional work when time and tools are sufficient   |
| **Legendary** | Twice Proficiency Bonus | Attempt explicitly superhuman or setting-defining applications                        |

Ranks above Expert do not add larger numeric bonuses. They change what can be attempted and what no longer needs a roll.

> **DESIGN RECOMMENDATION** Keep binary proficiency plus Expertise in the Core. Permission-based ranks are promising for crafting, languages, lore, and domain play but should not require auditing every published proficiency.

## **4.9 Setting Difficulty Classes**

> **CORE RULE** Set a DC from the task as it exists in the world, not from the level of the character attempting it. Start with the standard ladder, then change the circumstances or consequences instead of chasing single-point precision.

| **DC** | **Difficulty**    | **Use**                                                       |
|--------|-------------------|---------------------------------------------------------------|
| 5      | Very Easy         | Requires attention but defeats only the completely unprepared |
| 10     | Easy              | A competent adventurer usually succeeds                       |
| 15     | Moderate          | Training or a favorable plan matters                          |
| 20     | Hard              | Demands expertise, strong ability, or substantial setup       |
| 25     | Very Hard         | Exceptional even for experts                                  |
| 30     | Nearly Impossible | At the edge of mortal or mundane capability                   |

For improvised hazards and environmental interactions, use the more compact severity ladder in Section 8: DC 10, 13, 15, or 18.

### **Contested Actions**

Avoid opposed rolls when one side can supply a stable DC. Use a creature’s Passive Score or feature DC where possible. Roll both sides only when the volatility of both efforts is itself important.

### **Secret Information**

The GM may roll secretly when knowing the die result would itself reveal information, but should not hide observable consequences. A failed Search might consume time and leave uncertainty; it should not falsely assure the players that a room is safe.

## **4.10 Limited Degrees of Outcome**

> **OPTIONAL RULE** A procedure may define four outcomes: Critical Success, Success, Failure, and Critical Failure. A result 10 or more above the DC is a Critical Success; a result 10 or more below is a Critical Failure. A natural 20 improves the outcome by one step and a natural 1 worsens it by one step.

Use this rule only when all four outcomes are written in advance, such as a complex Hazard, negotiation, crafting project, or vehicle collision. Do not apply it globally during v0.1.

**Research Basis.** Pathfinder 2e applies four degrees broadly and adjusts a degree on natural 20s and 1s. That structure creates clear, authored outcome bands, but importing it globally would change many fifth-edition probabilities and spell effects. \[R3\]

## **4.11 Repeated Attempts**

> **CORE RULE** A failed check resolves the stated attempt. Another check requires at least one of the following:

- a changed method;

- a new tool, resource, or piece of information;

- a different character whose contribution is meaningfully distinct;

- acceptance of a greater consequence; or

- enough additional time for the situation or pressure procedure to advance.

If unlimited time guarantees eventual success and no consequence can intervene, the GM narrates success and states the time required.

## **4.12 GM Ruling Hierarchy**

> **GM GUIDANCE** When no rule is obvious, use the first available level in this hierarchy:

1.  **Specific exception.** A feature, spell, creature, Hazard, or scenario rule directly governs the case.

2.  **Named procedure.** Use a relevant procedure such as Influence, Exploration Rounds, environmental interactions, or object damage.

3.  **Close precedent.** Adapt the nearest rule without importing unrelated benefits.

4.  **Standard D20 Test.** Choose ability, proficiency, DC, and consequence.

5.  **Temporary ruling.** Make the simplest fair call, state that it is provisional, and continue play.

After the session, record only temporary rulings likely to recur. Do not turn every improvised decision into permanent law.

## **4.13 Specific Rules Supersede General Rules**

> **CORE RULE** A specific rule supersedes a general rule only within its stated scope. If two specific rules conflict, the narrower rule applies. If they remain equally specific, the rule for the active creature or effect resolves first, unless the GM must issue a temporary ruling.

An exception should name the general limit it changes. “This movement does not provoke Opportunity Attacks” is clearer than “move freely.”

## **4.14 Adjudication Clauses**

Every open-ended subsystem in Hearth & Hazard follows these clauses:

- **Competence Clause:** Do not roll to make an adventurer look inept at routine work.

- **Consequence Clause:** State or strongly telegraph the category of consequence before an informed commitment.

- **One-Roll Clause:** One decision normally produces one resolution roll, not a chain of gates.

- **No Double-Dip Clause:** One fictional cause should not deal the same consequence twice unless the rule clearly prices that escalation.

- **Conservation of Agency Clause:** A ruling may make an action costly without retroactively invalidating information the players relied upon.

- **Table-Speed Clause:** If the exact modifier or interaction cannot be resolved quickly, choose the nearest severity or DC and move on.

# **5. CHARACTER FRAMEWORK**

## **5.1 Default Character Creation**

> **CORE RULE** A player character is built from a **Class**, **Background**, **Ancestry**, ability scores, proficiencies, languages, starting equipment, and one or more character commitments. Existing 2024-compatible material can fill these elements during v0.1.

Create a character in this order:

1.  **Choose a campaign profile.** Note the campaign’s grit, magic, rest, Darkvision, and advancement modules.

2.  **Choose a Class.** Record first-level features, Hit Die, proficiencies, and subclass progression.

3.  **Choose a Background.** Gain its ability increases, Origin Feat, two skills, one tool, equipment, and narrative foundation, using the 2024 structure.

4.  **Choose an Ancestry.** Gain biological or supernatural traits. Culture is not assumed from ancestry.

5.  **Choose a Region and languages.** Region supplies cultural familiarity and may exchange one language for a tool, lore, or local contact.

6.  **Generate ability scores.**

7.  **Choose remaining skills and tools.**

8.  **Choose starting gear or take the class/background currency option.**

9.  **Write commitments.** Choose two Drives, one Bond, and one Oath or Obligation.

10. **Record derived statistics.** Proficiency Bonus, Armor Class, Hit Points, Speed, Passive Scores, save DCs, and carrying capacity.

## **5.2 Class and Subclass**

The default keeps twenty-level classes and subclasses. A Class defines the character’s primary adventure role and resource engine. A subclass specializes that role without replacing the chassis.

### **Class Design Constraints for Future Drafts**

- Every class must have a useful contribution in combat, exploration, and at least one social or downtime context.

- A class should not require a particular optional module to function.

- Features that compress or exchange Actions must state exactly which Actions qualify.

- A feature that adds damage should not also grant broad action compression without a shared budget.

- Exploration and social features should create permissions, information, or resource advantages—not merely add a flat bonus to a check.

- Subclasses should receive their identity-defining play pattern early enough to matter in ordinary campaigns.

### **Existing Project Precedent: Veteran Fighter**

The existing **Veteran** subclass draft treats tactical breadth as action compression: selected general Actions become Veteran Actions, later features expand which Actions qualify, and damage rewards follow the tactical Action. This design relies on the 2024 Action/Bonus Action/Reaction chassis. It is strong evidence against changing the Core to a universal three-action system before class conversion.

> **OPEN DECISION** Keep the 2024 subclass cadence exactly, or adopt a common cadence for every rewritten class? This must be answered before subclass production begins.

## **5.3 Background**

> **CORE RULE** Background represents learned culture, occupation, formative experience, and social position. It is the primary home for Origin Feats, ordinary languages, tools, contacts, and non-biological proficiencies.

A custom Background should contain:

- three ability score increases distributed according to the campaign’s chosen 2024-compatible method;

- one Origin Feat;

- two skill proficiencies;

- one tool proficiency;

- two languages, or one language and one regional familiarity;

- starting equipment or currency; and

- a short feature expressed as a contact, access permission, or downtime advantage rather than automatic narrative authority.

## **5.4 Ancestry**

> **DESIGN RECOMMENDATION** Use **Ancestry** as the rules term and allow individual settings to use Species, Kin, Lineage, Folk, or another reader-facing term.

Ancestry should contain physical and supernatural traits: size, Speed, senses, physiology, inherent magic, unusual movement, or resistance. It should not dictate alignment, profession, personality, or a universal culture.

### **Ancestry Power Budget**

Until a mathematical budget is developed, use the 2024 species packages as the compatibility band. When an ancestry grants flight, broad magic resistance, multiple resistances, or repeatable teleportation, compare the entire package rather than pricing each trait in isolation.

> **OPEN DECISION** Decide whether ancestry traits may improve by character level. Level-scaling protects signature abilities from becoming irrelevant, but adds more feature text and makes ancestry a larger part of the build.

## **5.5 Languages and Communication**

Languages have three proposed levels of capability:

| **Capability** | **Effect**                                                                        |
|----------------|-----------------------------------------------------------------------------------|
| **Familiar**   | Exchange basic spoken meaning; complex or technical conversation may require time |
| **Fluent**     | Speak, understand, read, and write ordinary forms                                 |
| **Scholarly**  | Interpret archaic, technical, coded, or ceremonial forms                          |

> **OPTIONAL RULE** A normal language proficiency grants Fluent capability. Campaigns that want language play can split each language into Familiar, Fluent, and Scholarly without changing D20 Test bonuses. Magical language effects state the capability they grant.

The GM should not use accents or imperfect real-world language performance as a proxy for character competence.

## **5.6 Ability Score Generation**

Choose one method for the entire party.

| **Method**          | **Procedure**                                                                                                      | **Campaign effect**                                       |
|---------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| **Standard Array**  | Assign 15, 14, 13, 12, 10, 8 before Background increases                                                           | Predictable and compatible; proposed Core                 |
| **Point Buy**       | Use the 2024-compatible 27-point method and normal score limits                                                    | Controlled customization                                  |
| **Heroic Roll**     | Roll 4d6, discard the lowest die, six times; arrange as desired; if total modifiers are below +5, reroll the array | Higher variance with a floor                              |
| **Shared Array**    | Each player rolls one score using Heroic Roll; combine six results into an array everyone may use                  | Random texture without party power disparity              |
| **Gritty in Order** | Roll 3d6 for each ability in order; choose Class afterward; apply normal Background increases                      | Optional dangerous campaign; can create sharp disparities |

> **DESIGN RECOMMENDATION** Standard Array should be the rules presentation default. Shared Array is the preferred random option because it preserves a common party baseline.

## **5.7 Skills and Tools**

> **CORE RULE** A skill applies when its body of training is relevant to the approach. A tool applies when practical familiarity with the implement, craft, vehicle, kit, or process matters. If both a skill and tool proficiency materially apply, the creature gains Advantage rather than adding Proficiency Bonus twice.

Tool proficiency can also:

- allow an attempt that would otherwise be impossible;

- reduce the time or consumed material;

- reveal a more precise consequence before commitment; or

- produce a better item on success.

### **Study, Search, and Practical Knowledge**

- **Search** finds something through immediate physical perception.

- **Study** draws a conclusion through memory, analysis, records, or close examination.

- **Utilize** deliberately operates an object, device, tool, or environmental feature.

The GM should identify which Action matches the declared method, not ask the player to name a skill before describing an action.

## **5.8 Feats**

The default retains Origin Feats and General Feats. Future feat design should use three tiers:

| **Tier**    | **Typical acquisition**                       | **Scope**                                           |
|-------------|-----------------------------------------------|-----------------------------------------------------|
| **Origin**  | Character creation                            | Identity, training, modest utility                  |
| **General** | Level-based Ability Score Improvement feature | Build-defining combat or broad adventure capability |
| **Epic**    | High-level threshold or campaign reward       | Mythic permission and capstone-scale effects        |

Feats should not be taxes required to make a basic combat style functional. If nearly every user of a weapon needs the same feat, that capability belongs in the weapon, mastery, or class chassis.

## **5.9 Starting Gear**

Use class and Background packages for speed. A player who chooses currency can buy equipment before play. The campaign must publish:

- whether ammunition, rations, containers, and light sources are tracked;

- the active encumbrance method;

- whether armor has Strength requirements;

- the availability of spell components and specialist tools; and

- one unusual item, rumor, or debt that ties each character to the opening situation.

## **5.10 Optional Gritty Generation**

> **OPTIONAL RULE** For a Perilous Delve campaign:

- use Gritty in Order ability scores or the Shared Array;

- begin at level 1 with maximum Hit Points as normal;

- use slot encumbrance, limited Darkvision, safe-haven rests, and dungeon turns;

- roll starting social reaction instead of assuming hostility;

- give each character one retainer contact or faction obligation; and

- use the replacement-character rule below.

**Replacement characters** enter at the party’s level or one level lower, chosen by the campaign before play. Do not compound a character death with an indefinite level penalty unless unequal levels are an explicit campaign feature.

## **5.11 Optional Simplified Class Framework**

> **OPTIONAL RULE** For one-shots, retainers, open-table play, or early subsystem tests, use four broad classes:

| **Class**   | **Core identity**                                         | **Suggested chassis** |
|-------------|-----------------------------------------------------------|-----------------------|
| **Warrior** | Weapons, armor, endurance, battlefield control            | Fighter baseline      |
| **Expert**  | Skills, tools, precision, contacts, mobility              | Rogue baseline        |
| **Adept**   | Divine, primal, or psychic support and transformation     | Cleric/Druid baseline |
| **Mage**    | Arcane spellcraft, rituals, and fragile high-impact magic | Wizard baseline       |

Each simplified class chooses a path at level 3. This framework is not recommended as a replacement for full classes unless broad compatibility is abandoned.

## **5.12 Character Framework Questions**

> **OPEN DECISION**

- Are Background ability increases fixed, freely assigned, or chosen from a short list?

- Does Ancestry replace the 2024 term Species throughout the rules?

- Is subclass progression identical across all classes?

- Are Master and Legendary proficiency permissions worth the added terminology?

- Does every character use Drives, Bonds, and Obligations, or are they an optional roleplay module?

# **6. ACTION ECONOMY OPTIONS**

## **6.1 Comparison**

| **Model**               | **Turn resources**                                                                  | **Strengths**                                                                                                  | **Costs**                                                                                                                                           |
|-------------------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **2024-style**          | Movement, one Action, up to one Bonus Action when available, one Reaction per round | Highest compatibility; fast recognition; existing classes and monsters work; supports current project material | Bonus Action congestion; movement is not fungible; some options need special action compression                                                     |
| **True three-action**   | Three interchangeable Actions plus one Reaction                                     | Flexible turns; repeated-action pricing; elegant movement and maneuvers                                        | Requires rewriting classes, spells, Extra Attack, monsters, conditions, and action denial; multiple-attack penalties or equivalent become necessary |
| **Standard/Move/Minor** | Standard, Move, Minor, Immediate/Reaction; some Full-Round actions                  | Clear tactical categories; easy to price committed actions                                                     | More action types; resembles older design without solving all Bonus Action congestion                                                               |
| **Action-point bridge** | Three points; effects cost one or two; one Reaction                                 | Can test flexibility while preserving some 2024 content                                                        | Not actually PF2; conversion exceptions proliferate; easy to create unintended action combinations                                                  |

**Research Basis.** Pathfinder 2e gives each creature three actions and one reaction, with individual activities costing one to three actions. Its classes, spells, movement, and multiple-attack rules are authored around that economy. \[R2\]

## **6.2 Proposed Core: 2024-Style Economy**

> **CORE RULE** On a creature’s turn, it can move up to its Speed and take one Action. It can take one Bonus Action only when a rule grants or permits one. It can communicate briefly and interact with the environment as the GM permits; a consequential operation uses the Utilize Action. A creature regains its Reaction at the start of its turn.

### **Action Vocabulary**

The Core uses these general Actions:

**Attack, Dash, Disengage, Dodge, Help, Hide, Influence, Magic, Ready, Search, Study,** and **Utilize**.

A rule can introduce another Action with a specific template. A feature may let a creature replace one attack made as part of the Attack Action; such a replacement is not a separate Action.

### **Incidental Interaction**

A creature can perform one brief, uncomplicated interaction during its movement or Action: draw a weapon, open an unlocked door, hand an item to an adjacent ally, or kick aside a loose stool. A second interaction, a resistant object, a complex device, or an interaction intended to produce a mechanical effect uses the Utilize Action unless a feature says otherwise.

### **Action Compression**

Features may compress a named Action into a Bonus Action or attack replacement. They must state:

- which Actions qualify;

- how often;

- whether the compressed Action can trigger follow-up benefits;

- whether Magic or magic-item activation qualifies; and

- whether the same Action can be taken again that turn.

This standard directly supports the existing Veteran Fighter design.

## **6.3 Reactions**

> **CORE RULE** A Reaction is an immediate response to a stated trigger. A creature can take only one Reaction before the start of its next turn. If two triggers occur at the same time, the reacting creature chooses which one to answer.

A rule that interrupts its trigger states whether it resolves before the triggering event. Otherwise, the trigger resolves first.

## **6.4 Ready**

> **CORE RULE** When a creature takes the Ready Action, it chooses a perceivable trigger and an Action it will take in response. Before the start of its next turn, it may use its Reaction immediately after the trigger finishes to take the readied Action. A readied spell follows the compatibility baseline for Concentration and slot expenditure.

A trigger cannot be a vague future state such as “when anything bad happens.” The creature must be able to perceive it.

## **6.5 Advanced Three-Action Prototype**

> **ADVANCED RULE—EXPERIMENTAL** This module is for a conversion playtest, not mixed use with unconverted Core characters.

Each turn grants three Actions and one Reaction.

- **Stride:** move up to Speed; one Action.

- **Strike:** make one attack; one Action. A second or third Strike in the same turn needs a multiple-attack rule that has not yet been designed.

- **Basic Action:** Dash-equivalent Stride, Disengage, Help, Search, Study, or Utilize; generally one Action.

- **Guard:** Dodge; two Actions.

- **Cast:** costs one to three Actions as specified by the spell.

- **Activities:** class features state their Action cost.

**Required conversion work:** Extra Attack, Bonus Actions, two-weapon fighting, Monk features, Cunning Action, spell components, Action Surge, legendary actions, Multiattack, and every feature that says “as part of the Attack Action.”

> **DESIGN RECOMMENDATION** Do not advance this module beyond a small prototype until the Core environmental and exploration procedures are tested. The conversion cost is too large to pay before knowing whether the campaign actually dislikes the 2024 turn structure.

## **6.6 Standard/Move/Minor Prototype**

> **OPTIONAL RULE—EXPERIMENTAL** Rename the turn resources:

- **Standard Action:** most current Actions.

- **Move Action:** move up to Speed or stand from Prone.

- **Minor Action:** effects currently using a Bonus Action.

- **Reaction:** unchanged.

- **Committed Action:** consumes both Standard and Move, and prevents a Minor Action.

Committed Actions can support a Sprint, careful Aim, full defense, or large siege operation. This is a useful design vocabulary even if the full model is rejected.

## **6.7 Decision Gate**

> **OPEN DECISION** Before any deep class or monster rewrite, select one:

1.  **Recommended:** 2024-style Core; action compression appears in features; Committed Actions are an occasional template.

2.  2024-style Core plus a later, separately balanced three-action variant.

3.  Universal three-action rewrite, accepting that “2024 compatible” becomes “convertible” rather than “drop-in.”

The current draft assumes option 1.

# **7. COMBAT DRAFT**

## **7.1 Combat Procedure**

> **CORE RULE** Use combat rounds when timing, position, and hostile opposition require action-by-action resolution.

1.  **Establish the battlefield.** The GM identifies visible creatures, major terrain, cover, hazards, objectives, and escape routes.

2.  **Determine surprise and Initiative.**

3.  **Take turns in Initiative order.**

4.  **Resolve end-of-round events.** Check morale, advancing Hazards, reinforcements, and clocks when triggered.

5.  **End combat when the sides no longer contest an objective.** Flight, surrender, parley, concealment, or completed objectives can end combat without every foe reaching 0 Hit Points.

## **7.2 Initiative and Surprise**

> **CORE RULE** Each combatant rolls Initiative with a Dexterity check unless a feature changes it. The GM may roll once for a group of identical creatures. Ties are resolved by the higher Dexterity score; remaining ties are decided by the players for player characters and by the GM otherwise.

A creature is **Surprised** if combat begins and it was unaware of an immediate threat. A Surprised creature has Disadvantage on its Initiative roll. Surprise is not a separate round and does not normally erase a creature’s turn.

### **Initiative Posture**

> **OPTIONAL RULE** During structured exploration, a character’s declared task can change Initiative:

- **Keep Watch:** use Wisdom instead of Dexterity.

- **Scout:** use Dexterity and gain Advantage if the threat comes from the scouted direction.

- **Study a Threat:** use Intelligence if the studied creature or Hazard begins the combat.

- **Distracted Task:** Disadvantage if the task made the threat harder to notice.

## **7.3 Movement and Position**

A creature can move up to its Speed on its turn, dividing movement before and after Actions. Difficult Terrain costs 1 extra foot of movement per foot moved. Standing from Prone costs movement equal to half Speed.

Diagonal movement on a square grid uses the table’s chosen convention:

- **Simple:** every square costs 5 feet.

- **Alternating:** the first diagonal costs 5 feet, the second 10 feet, alternating thereafter.

The Simple method is Core for compatibility. Alternating diagonals are an optional precision rule.

## **7.4 Size, Space, and Occupation**

| **Size**   | **Typical occupied space** | **Momentum Die** |
|------------|----------------------------|------------------|
| Tiny       | 2½-foot square             | d4               |
| Small      | 5-foot square              | d6               |
| Medium     | 5-foot square              | d8               |
| Large      | 10-foot square             | d10              |
| Huge       | 15-foot square             | 2d10             |
| Gargantuan | 20-foot square or larger   | 3d10             |

Occupied Space is the area a creature controls, not necessarily the literal dimensions of its body. A creature can move through a nonhostile creature’s space. It can move through a hostile creature’s space only if a rule, size difference, Overrun, or Tumble permits it. It cannot willingly end movement in another creature’s space unless a rule allows it.

## **7.5 Opportunity Attacks**

> **CORE RULE** A creature can make an Opportunity Attack when a hostile creature it can see leaves its reach using its movement, Action, Bonus Action, or Reaction. The attack uses the creature’s Reaction and occurs immediately before the target leaves reach.

Teleportation and movement that does not use the target’s movement, Action, Bonus Action, or Reaction do not provoke.

## **7.6 Cover**

| **Cover**            | **Effect**                                                                            |
|----------------------|---------------------------------------------------------------------------------------|
| Half Cover           | +2 to AC and Dexterity Saving Throws                                                  |
| Three-Quarters Cover | +5 to AC and Dexterity Saving Throws                                                  |
| Total Cover          | Cannot be targeted directly by an attack or effect that requires an unobstructed path |

Determine cover from the relevant origin point. An environmental effect may damage or remove cover, but doing so uses the object and interaction rules rather than retroactively changing an attack already resolved.

## **7.7 Unarmed Strikes, Grappling, and Shoving**

> **CORE RULE** When a creature hits with an Unarmed Strike, choose one option permitted by the compatibility baseline:

- **Damage:** deal 1 + Strength modifier Bludgeoning damage.

- **Grapple:** the target makes a Strength or Dexterity Saving Throw, its choice, against DC 8 + the attacker’s Strength modifier + Proficiency Bonus. On a failure, the target has the Grappled condition.

- **Shove:** the same save; on a failure, push the target 5 feet or give it the Prone condition.

The target must normally be no more than one size larger than the attacker. A feature can alter size limits, DC ability, or effect.

### **Escape**

A Grappled creature can take an Action to make a Dexterity (Acrobatics) or Strength (Athletics) check against the escape DC. Forced movement that places the grappler and target beyond the grapple’s reach ends it unless a rule maintains the hold.

## **7.8 Forced Movement**

> **CORE RULE** Forced movement moves a creature without spending that creature’s movement. Unless a rule says otherwise, it does not provoke Opportunity Attacks and stops at an impassable space.

Forced movement into a creature or hard obstacle does not automatically deal damage. If at least 10 feet of forceful movement remains and the impact is consequential, use the Collision rule in Section 8. An effect cannot gain both its full forced-movement benefit and an unpriced large damage rider merely because a wall is nearby.

## **7.9 Bloodied**

> **CORE RULE** A creature is **Bloodied** while it has half its Hit Point maximum or fewer Hit Points. Bloodied has no universal penalty. It is a visible state and a trigger for features, morale, monster behavior, and some Hazards.

The GM tells players when a visible creature becomes Bloodied unless its nature conceals damage.

## **7.10 Morale in Combat**

Morale is Core for non-player creatures. See Section 10 for the full procedure.

Common combat triggers are:

- the first allied creature is killed or incapacitated;

- the side has half or fewer of its starting combatants able to fight;

- the leader becomes Bloodied, flees, or falls;

- the objective is lost; or

- an overwhelming supernatural or environmental event changes the situation.

Morale normally triggers no more than twice in one encounter.

## **7.11 Retreat, Pursuit, and Surrender**

> **CORE RULE** A side that clearly abandons the contested objective may attempt a retreat. If the other side cannot or will not pursue, combat ends. If pursuit matters, transition to a **Pursuit Challenge** instead of playing empty Dash turns indefinitely.

### **Pursuit Challenge**

Set a lead from 0 to 3:

- **0:** pursuers are in reach;

- **1:** close;

- **2:** separated by terrain or distance;

- **3:** escape.

Each round, both sides choose an approach. Resolve one relevant check for each side or compare a check against a fixed DC. The winner shifts the lead one step. A side may spend a resource, split up, drop treasure, create a Hazard, or accept a complication for Advantage. At lead 3 the quarry escapes; at lead 0 the pursuer can force combat or capture if the fiction permits.

Surrender is an Influence scene shaped by the opponents’ attitude, needs, reputation, and ability to secure prisoners. Intelligent enemies do not fight to the death without a reason.

## **7.12 Large Creature Movement**

A Large or larger creature does not harm smaller creatures merely by moving. It may use **Overrun**, a **Trample** Action or trait, or a specific movement feature. This cost protects the ordinary turn economy and makes mass an authored tactical option.

The full Momentum, Overrun, Trample, Collision, and Pinning rules appear in Section 8.

## **7.13 Conditions**

The v0.1 Core retains the 2024-compatible conditions. Future revision should:

- give each condition one canonical entry;

- state whether it affects movement, Actions, attacks, D20 Tests, senses, targeting, and speech;

- state how it ends;

- avoid creating a new condition for a one-round numerical modifier; and

- distinguish physical restraint from mental compulsion.

### **New Object State: Corroded**

**Corroded.** An object’s Damage Threshold is reduced by 5, to a minimum of 0. If it has no Damage Threshold, attacks or effects that deal Acid damage to it have Advantage or the object has Disadvantage on relevant saves. Corroded ends only through repair or replacement.

Corroded is an object state, not a creature condition.

## **7.14 Damage and Healing**

Use 2024-compatible damage, resistance, vulnerability, immunity, healing, Hit Dice, death saving throws, and Massive Damage rules during v0.1.

### **Damage Timing**

- Combine damage dice from one source before applying resistance or vulnerability.

- An environmental rider produced by that same source is not a separate source for the directly affected target unless the rule explicitly says so.

- Persistent Hazards deal damage at the trigger and timing stated in their entry.

- A creature cannot be damaged by the same environmental Hazard more than once per turn unless the Hazard explicitly says otherwise.

### **Healing and Fiction**

Hit Point healing does not automatically repair a lingering injury, broken item, disease, lost limb, social consequence, or exhaustion. Those consequences use their own recovery rules.

## **7.15 Death and Dying**

The Core retains the familiar 0 Hit Point and death-save procedure for compatibility. The following clarification applies:

> **CORE RULE** A creature at 0 Hit Points is not automatically safe because combat ends. The GM continues death saves by round or converts them into an immediate stabilization check only if timing no longer matters.

Enemies may capture, stabilize, ignore, or finish fallen foes according to motive and tone. The GM should establish the campaign’s expectations about attacks against Unconscious characters before play.

## **7.16 Optional Wounds and Injuries**

> **OPTIONAL RULE** A player character risks a **Wound** when one of these triggers occurs:

- it takes damage equal to or greater than half its Hit Point maximum from one source;

- it drops to 0 Hit Points from a Critical Hit;

- it fails a death saving throw by 5 or more; or

- a specific Hazard inflicts a Wound.

The character makes a Constitution Saving Throw with DC 10 or half the triggering damage, whichever is higher. On a failure, choose or roll a fitting Wound. The player may accept a scar, damaged item, or short-term impairment when that better fits the fiction.

| **d6** | **Wound**    | **Effect**                                                                   | **Recovery**                                      |
|--------|--------------|------------------------------------------------------------------------------|---------------------------------------------------|
| 1      | Concussion   | Disadvantage on Concentration checks and Intelligence checks                 | Three Long Rests or treatment                     |
| 2      | Deep Cut     | Lose one Hit Die after each strenuous scene until treated                    | Medicine check and one Long Rest                  |
| 3      | Sprain       | Speed reduced by 10 feet                                                     | Three Long Rests or magical healing of 3rd level+ |
| 4      | Cracked Ribs | When taking the Dash Action, take one Hit Die of damage                      | Five Long Rests or treatment                      |
| 5      | Damaged Hand | Disadvantage on checks using that hand; cannot use it for Somatic components | Three Long Rests or treatment                     |
| 6      | Lasting Scar | No mandatory penalty; mark the event and gain Heroic Inspiration             | Permanent unless transformed                      |

A character can have at most one untreated mechanical Wound. A new Wound worsens recovery time or creates a narrative scar rather than stacking multiple disadvantage effects.

> **DESIGN RECOMMENDATION** Keep Wounds optional. They alter the meaning of Hit Points and healing magic, and should be tested with the chosen rest model.

# **8. ENVIRONMENTAL INTERACTIONS AND FANTASY PHYSICS**

## **8.1 Purpose and Boundary**

This chapter answers a recurring table question: “The effect obviously interacts with the environment—what happens?” It supplies a bounded procedure, not a catalog of every chemical and physical possibility.

> **CORE RULE** When damage, movement, terrain, an Object, creature size, or mass interacts in an obvious and consequential way, the GM may resolve **one Environmental Rider**. Identify the Source and Medium, choose Severity, call for one D20 Test if needed, and apply one rider.

The interaction must be:

- **established:** the Source and Medium are actually present;

- **legible:** a competent creature could anticipate the broad result, unless the properties are deliberately hidden;

- **consequential:** the result changes position, access, information, resources, or danger;

- **priced:** a strong effect consumes an Action, attack, spell, trait, setup, or environmental opportunity; and

- **bounded:** one originating effect creates no more than one immediate rider.

## **8.2 Definitions**

**Source.** The energy, material, movement, or force that initiates the interaction: Fire, Lightning, Cold, Thunder, Acid, Force, Poison, Radiant, Necrotic, falling, collision, forced movement, pressure, or a charging body.

**Medium.** The creature, Object, terrain, substance, or space through which the Source acts: connected water, oil, metal, ice, wood, stone, rope, smoke, gas, glass, mud, flesh, foliage, or a confined space.

**Environmental Rider.** The one mechanical consequence created in addition to, or instead of, the Source’s ordinary effect.

**Interaction Die.** A die that scales incidental damage by the tier of the initiating creature, effect, Hazard, or adventure.

**Hazard.** An environmental danger with a trigger and procedure. A Hazard can be static, persistent, complex, or creature-created.

**Object.** A discrete noncreature with Armor Class and Hit Points when those statistics matter.

**Structure.** A large construction divided into meaningful components rather than treated as one enormous Object.

## **8.3 Environmental Interaction Procedure**

> **CORE RULE** Resolve an interaction in five steps.

### **Step 1: Identify the Source**

Name the damage type, physical force, moving body, or supernatural effect. The source’s rule still resolves normally.

### **Step 2: Identify the Medium**

Name the affected material or space and one relevant trait.

| **Medium Trait** | **Meaning**                                                      |
|------------------|------------------------------------------------------------------|
| **Brittle**      | Can crack, shatter, or throw fragments                           |
| **Conductive**   | Carries electricity or magical charge through connected material |
| **Corrodible**   | Acid or decay can degrade it                                     |
| **Flammable**    | Can sustain Burning after ignition                               |
| **Flexible**     | Can bend, tangle, snap, or transmit force                        |
| **Freezable**    | Can become solid, slick, or obstructive under Cold               |
| **Living**       | Organic and metabolically alive                                  |
| **Loose**        | Can scatter, collapse, slide, or become airborne                 |
| **Obscuring**    | Can block sight as smoke, dust, mist, foliage, or darkness       |
| **Pressurized**  | Confinement can amplify or redirect a release                    |
| **Reinforced**   | Resists damage until a threshold is overcome                     |
| **Unstable**     | Already near collapse, ignition, detonation, or release          |

The GM states obvious traits when the Medium becomes relevant. Hidden traits require clues, Study, or experimentation.

### **Step 3: Choose Severity**

Choose the lowest severity that produces the obvious fictional result.

| **Severity** | **Default DC** | **Incidental damage** | **Typical scope**                                                 | **Examples**                                                          |
|--------------|----------------|-----------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------|
| **Minor**    | 10             | None or 1 point       | Cosmetic or one small positional fact                             | Ignite tinder; reveal wet footprints; crack a pane; push loose papers |
| **Moderate** | 13             | 1 Interaction Die     | One target, one 5-foot space, or one small Object                 | Burning oil; slick ice; a short electrical arc; splintered cover      |
| **Major**    | 15             | 2 Interaction Dice    | Several nearby targets, a 10-foot area, or a structural component | Collapsing balcony; exploding glass; ruptured pipe; large collision   |
| **Extreme**  | 18+            | 4 Interaction Dice    | Set-piece area or catastrophic component failure                  | Bridge collapse; magazine detonation; tower section falling           |

**Extreme** is not the default reward for a clever description. It requires an extreme Source, an unstable setup, substantial preparation, or an authored set piece.

### **Step 4: Call for a D20 Test if Needed**

Do not add a roll if the original attack or save already establishes the affected creature’s exposure. For secondary creatures or uncertain control, use:

- the Source’s existing save DC;

- the initiating creature’s feature DC; or

- the Severity DC.

Choose Strength to resist displacement or crushing, Dexterity to avoid a visible sudden area, and Constitution to endure inhaled or bodily exposure.

### **Step 5: Resolve One Rider**

Choose one:

| **Rider**             | **Mechanical job**                                                                                     |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| **Incidental Damage** | Deal the severity’s Interaction Dice to secondary targets or an Object                                 |
| **Displace**          | Push, pull, slide, or drop a target a short distance                                                   |
| **Impair**            | Prone, brief sensory interference, loss of grip, or another one-turn limitation                        |
| **Alter Terrain**     | Create or remove Difficult Terrain, cover, an opening, unstable footing, or obscurity                  |
| **Alter Object**      | Ignite, extinguish, break, jam, corrode, freeze, reveal, or deform an Object                           |
| **Create Hazard**     | Create a simple Hazard with one trigger, one effect, and a short duration                              |
| **Reveal or Conceal** | Expose tracks, silhouettes, residue, seams, or hidden space; or produce smoke, dust, mist, or darkness |

The rider can combine closely linked description and mechanics—“the ice becomes Difficult Terrain, and a creature that Dashes across it must save or fall Prone” is one terrain rider. It cannot also deal damage and restrain every creature without increasing the severity and authoring a Hazard.

## **8.4 Interaction Dice**

> **CORE RULE** Use the tier of the initiating effect or creature. For a fixed location, use the adventure’s expected tier or the Hazard’s authored tier.

| **Tier**   | **Character level or approximate CR** | **Interaction Die** |
|------------|---------------------------------------|---------------------|
| Adventurer | 1–4                                   | d4                  |
| Hero       | 5–10                                  | d6                  |
| Paragon    | 11–16                                 | d8                  |
| Legend     | 17–20                                 | d10                 |

Interaction Dice scale incidental consequences without reproducing the full damage of the original spell or attack. They are not added to every damage-type effect.

## **8.5 Limits: No Double Dipping and No Cascades**

> **CORE RULE** Apply all of these limits unless an authored feature says otherwise.

1.  **One Source, one rider.** One attack, spell, fall, or movement event creates at most one immediate Environmental Rider.

2.  **Modify the direct target.** A creature already directly affected by the Source normally takes no additional Interaction Dice. Change terrain, damage an Object, alter position, or substitute part of the result.

3.  **Do not re-hit an area.** A creature already included in the Source’s area is not a secondary target of the rider.

4.  **One Hazard trigger per turn.** A creature suffers a particular simple Hazard no more than once per turn.

5.  **No immediate rider chains.** An Environmental Rider cannot itself cause another rider in the same resolution.

6.  **A later trigger can matter.** A persistent Burning Hazard may ignite a new fuel source on a later turn if a creature acts, time passes, or the Hazard’s entry provides an escalation.

7.  **Choose, do not pile.** If an effect could reasonably push, damage, deafen, shatter, and obscure, choose the consequence that best matches the players’ intent and the established Medium.

> **GM GUIDANCE** The interaction system rewards setup, not vocabulary. Naming more real-world phenomena does not grant more riders.

## **8.6 Damage-Type Interaction Matrix**

| **Source**               | **Common Medium traits**                         | **Default interaction**                                         | **Important limit**                                            |
|--------------------------|--------------------------------------------------|-----------------------------------------------------------------|----------------------------------------------------------------|
| **Acid**                 | Corrodible, Reinforced                           | Damage or Corrode an Object; weaken a component                 | Worn or carried gear is protected unless specifically targeted |
| **Cold**                 | Freezable, Brittle, Living                       | Freeze water; make slick terrain; embrittle an Object           | Does not automatically encase or Restrict a creature           |
| **Fire**                 | Flammable, Obscuring, Pressurized                | Ignite; create Burning; consume oxygen; make smoke              | Worn or carried gear does not ignite by default                |
| **Force**                | Brittle, Flexible, Loose, Reinforced             | Push, deform, break, clear, or collapse                         | Scale must be sufficient for the Object or structure           |
| **Lightning**            | Conductive, connected water or metal             | Arc to secondary targets; energize or disable a device          | Original and already-area targets take no extra damage         |
| **Necrotic**             | Living, organic, potable                         | Wither, spoil, foul, preserve as dead matter, reveal blight     | Does not add creature damage to a target already hit           |
| **Poison**               | Living, Obscuring, Pressurized                   | Create, move, concentrate, or disperse toxic gas/liquid         | Only a gas tagged Flammable ignites                            |
| **Radiant**              | Obscuring, supernatural darkness, hidden residue | Illuminate, reveal traces, suppress mundane darkness            | Does not automatically end magical Darkness or invisibility    |
| **Thunder**              | Brittle, Loose, Pressurized, confined            | Shatter, scatter, deafen briefly, or collapse unstable material | Choose object/terrain effect or creature impairment            |
| **Bludgeoning / impact** | Brittle, Loose, Flexible                         | Break, knock loose, deform, or create debris                    | Use Object statistics and Momentum when scale matters          |
| **Slashing**             | Flexible, taut, soft                             | Cut rope, canvas, foliage, or bindings                          | Hard objects may be immune or have a threshold                 |
| **Piercing**             | Pressurized, thin, brittle                       | Puncture, vent, pin, or make a small breach                     | A small hole is not a destroyed component                      |

The matrix is permission and guidance, not a promise that every attack creates an interaction.

## **8.7 Specific Elemental Interactions**

### **Lightning and Connected Water**

> **CORE RULE** When a Lightning effect strikes a creature or point in a connected body of water, the GM may create a **Moderate Conductive Rider**.

Choose up to two secondary creatures in the same connected water within 10 feet of the point of impact. Each makes a Dexterity or Constitution Saving Throw against the Source DC or DC 13. On a failure, it takes one Interaction Die of Lightning damage; on a success, it takes no damage. The direct target and creatures already affected by the Source take no additional damage.

Increase to Major only for a powerful electrical Source in a confined conductive system, such as a metal flooded chamber. A puddle touching another puddle only through damp ground is not automatically connected.

**Example:** A 7th-level sorcerer casts a single-target Lightning spell at a sahuagin standing waist-deep in a cistern. The spell resolves against the sahuagin. Two other sahuagin within 10 feet in the same water make saves; each failure takes 1d6 Lightning damage. The original target takes no extra die.

### **Fire and Flammable Material**

Readily flammable unattended material—dry straw, exposed oil, loose paper, tinder, a dry curtain—can ignite without a roll when touched by sustained Fire. Dense timber, damp cloth, green wood, and treated construction may require a Moderate or Major interaction.

**Burning Hazard (Moderate).** A 5-foot space or Small Object burns for 3 rounds unless fuel suggests otherwise. A creature that enters the space for the first time on a turn or ends its turn there makes a DC 13 Dexterity Saving Throw. Failure: one Interaction Die of Fire damage. Success: no damage. Smothering, dousing, removing fuel, or a suitable Utilize Action ends it.

Worn or carried items do not ignite merely because their bearer takes Fire damage. A rule must target the item, state ignition, or establish that the bearer is immersed in an ongoing Burning Hazard.

### **Cold, Water, and Ice**

A Moderate Cold interaction freezes up to one 5-foot square of shallow water or creates a skin of ice on a wet surface.

**Slick Ice.** The space is Difficult Terrain. A creature that moves more than half its Speed across the connected ice in one turn must succeed on a DC 13 Dexterity Saving Throw or fall Prone and stop moving. A creature that moves carefully does not roll.

Major Cold can freeze a 10-foot area, seal a Small opening, or form temporary load-bearing ice if the fiction supports it. The GM states what weight it supports. Cold does not automatically freeze a creature solid or apply Restrained.

### **Thunder and Brittle Material**

Thunder can shatter ordinary glass, crack brittle stone, scatter loose material, or create a brief concussive effect in a confined space.

- **Minor:** crack a pane, extinguish small flames through pressure, scatter loose papers.

- **Moderate:** shatter windows or crockery in a 5-foot area, creating either a shards Hazard or obscuring debris.

- **Major:** break unstable masonry, rupture a brittle component, or create falling debris.

If a Thunder effect already damages creatures in the area, use the rider on the environment. Do not add another Thunder damage roll to the same creatures.

### **Acid and Corrosion**

Acid deals damage to a susceptible unattended Object using the interaction’s dice or the effect’s stated object damage, not both. A Major Acid interaction can apply **Corroded** to one structural component or reinforced Object.

Ordinary Acid cannot dissolve an entire locked door in one round. It may destroy a lock, weaken a hinge, create a hand-sized breach, or lower a Damage Threshold. The altered component then creates a new approach.

### **Force and Structures**

Force can push loose objects, deform flexible barriers, crack brittle Objects, or transmit impact. It does not ignore an Object’s AC, Hit Points, or Damage Threshold unless the effect says it does.

Compare scale:

| **Source scale**                                  | **Typical result**                               |
|---------------------------------------------------|--------------------------------------------------|
| Cantrip, weapon blow, or Small creature           | Loose Object, latch, pane, fragile furnishing    |
| Leveled spell, siege weapon, or Large creature    | Door, barricade, wall section, vehicle component |
| High-level spell, siege monster, or Huge creature | Major structural component                       |
| Legendary effect or engineered demolition         | Tower section, bridge span, fortification breach |

### **Poison Gas, Wind, and Fire**

Wind can disperse, redirect, or thin a gas Hazard. The direction and strength become visible information before the choice when possible.

Only gas marked **Flammable** ignites. Ignition replaces the Poison gas Hazard with a Fire or concussive Hazard; it does not apply full Poison and Fire effects simultaneously to the same exposure. A Major ignition can create a brief area effect and consume the gas.

### **Radiant Light and Darkness**

Radiant energy can create a Minor reveal rider: outline a creature in mundane darkness, expose residue, show a hidden seam through contrast, or illuminate an area until the start of the source’s next turn.

Magical Darkness and invisibility end only if the source’s rule or an authored interaction says so. Radiant damage is not universally sunlight.

### **Necrotic Energy and Living Matter**

Necrotic energy can wither plants, spoil exposed food, foul a small quantity of water, reveal prior blight, or kill fragile mundane organisms. Severity determines quantity.

| **Severity** | **Suggested scope**                                                  |
|--------------|----------------------------------------------------------------------|
| Minor        | A flower, handful of seed, cup of water, or visible patch of moss    |
| Moderate     | One 5-foot patch of vegetation, a meal, or a waterskin               |
| Major        | A small tree, field strip, barrel, or wellhead                       |
| Extreme      | An authored crop blight, grove, reservoir, or supernatural dead zone |

This rider does not add damage to a creature already affected by the Necrotic source.

## **8.8 Objects**

> **CORE RULE** Use Object statistics only when an Object’s survival is uncertain and consequential. An appropriate tool used with time can bypass Hit Points. An inappropriate damage type may have no effect.

### **Object Armor Class**

| **Material**        | **AC** |
|---------------------|--------|
| Cloth, paper, rope  | 11     |
| Crystal, glass, ice | 13     |
| Wood, bone          | 15     |
| Stone               | 17     |
| Iron, steel         | 19     |

### **Object Hit Points**

| **Size** | **Fragile** | **Resilient** |
|----------|-------------|---------------|
| Tiny     | 2           | 5             |
| Small    | 3           | 10            |
| Medium   | 4           | 18            |
| Large    | 5           | 27            |

Huge and Gargantuan constructions should be divided into components.

### **Damage Threshold**

> **ADVANCED RULE** A reinforced Object or structural component has a **Damage Threshold**. A single damage instance below the threshold deals 0 damage. Equal or greater damage is applied normally.

| **Construction**                            | **Suggested threshold** |
|---------------------------------------------|-------------------------|
| Fragile barrier or light furniture          | 0                       |
| Heavy timber, barred door, cart frame       | 10                      |
| Masonry component, portcullis, hull section | 15                      |
| Reinforced gate, heavy vehicle frame        | 20                      |
| Fortification or legendary material         | 25+                     |

Acid, appropriate tools, weak points, Study, or prior damage can reduce a threshold. Damage type matters: a rapier is poor at destroying masonry; a maul or siege engine is appropriate.

Objects are normally immune to Poison and Psychic damage. The GM can assign additional resistances, vulnerabilities, or immunities from material.

### **Attended Objects**

An Object worn or carried by a creature is protected by that creature’s position and defenses. It cannot normally be targeted by an area interaction or incidental rider. A rule that targets attended Objects should grant the bearer a save or require an attack.

## **8.9 Structures**

> **CORE RULE** A Structure is divided into **components** whose failure changes play: a door, support, wall panel, parapet, bridge span, stair, mast, axle, or engine.

Each component has:

- material and Medium traits;

- AC;

- Hit Points;

- optional Damage Threshold;

- a **Bloodied effect** at half Hit Points, if useful;

- a failure result at 0 Hit Points; and

- repair requirements.

### **Example Component: Timber Bridge Span**

**Large Structure Component; wood, Flammable, Flexible; AC 15; HP 40; Threshold 10**

- **Bloodied—Sagging:** the span becomes Difficult Terrain and its safe load is halved.

- **Failure—Collapse:** creatures on the span make a DC 15 Dexterity Saving Throw. Success: reach a stable edge and fall Prone. Failure: fall with the span. Resolve one Major falling-debris interaction; no immediate chain.

The bridge’s rails and ropes may be separate Small or Medium Objects, allowing clever sabotage without chewing through all 40 Hit Points.

## **8.10 Vehicles**

Vehicles use components: frame or hull, locomotion, control, cargo, and special systems.

> **ADVANCED RULE** A vehicle component becomes **Broken** at half Hit Points. A Broken locomotion component halves Speed. A Broken control component imposes Disadvantage on control checks. At 0 Hit Points, the component fails.

The driver uses an appropriate vehicle or tool proficiency for dangerous maneuvers. Ordinary movement on clear ground needs no check.

**Research Basis.** Pathfinder 2e separates object Hardness, Hit Points, and a Broken Threshold, and gives vehicles collision and Run Over procedures. Hearth & Hazard borrows the component logic but uses fifth-edition AC, Hit Points, saves, and Action costs. \[R6\]

## **8.11 Momentum**

Momentum abstracts moving mass without calculating weight or velocity.

> **CORE RULE** A creature or falling Object uses the Momentum Die for its size from Section 7. A rule that deals **Momentum Damage** rolls that die. Huge and Gargantuan entries already include multiple dice.

### **Speed Bonus**

For a deliberate straight-line charge or uncontrolled fall:

- after at least 20 feet, use the normal Momentum Dice;

- after at least 40 feet, add one copy of the base die;

- after at least 80 feet, add two copies of the base die.

The maximum is double the listed number of dice unless an authored siege or legendary effect says otherwise.

**Example:** A Large war mammoth has a listed Momentum Die of d10. After a 40-foot charge, its momentum damage is 2d10. A Huge boulder has 2d10 and becomes 4d10 after a sufficiently long fall.

## **8.12 Impact Save**

An **Impact Save** resists a collision, overrun, or moving mass. The target chooses Strength or Dexterity unless the effect says otherwise:

- Strength braces, blocks, or absorbs;

- Dexterity avoids, rolls aside, or keeps footing.

The default DC for a creature-caused impact is:

**Impact DC = 8 + source’s Strength modifier + source’s Proficiency Bonus**

A vehicle, Hazard, spell, or monster trait can use its own save DC.

## **8.13 Overrun**

> **CORE RULE** **Overrun \[Action or Attack Replacement\].** A creature moves through one hostile creature no more than one size larger and continues up to half its Speed. The target makes an Impact Save.

- **Success:** the mover stops in the nearest legal space before the target.

- **Failure:** the mover can pass through the target’s space. If the mover is larger, the target also falls Prone.

- **Failure by 5 or more:** if the mover is at least two sizes larger, it may deal its Momentum Damage or push the target 5 feet. Choose one.

The mover must have enough movement to leave the target’s space. Overrun provokes Opportunity Attacks normally unless another rule prevents them. A creature can attempt only one Overrun per turn.

## **8.14 Trample**

Trample is not free movement. It is an authored Action, attack replacement, Recharge trait, or mount maneuver.

> **CORE RULE TEMPLATE** **Trample \[Action\].** The creature moves up to its Speed in a reasonably straight path and may enter the spaces of creatures smaller than it. Each target can be affected once and makes a Dexterity Saving Throw against the trampler’s Impact DC. Failure: Momentum Damage and Prone. Success: half damage and the target moves to the nearest safe space. The trampler cannot end in an occupied space unless it can Pin.

A monster’s Trample should normally replace Multiattack or one high-value attack. A player-facing Trample needs a feature, mount training, or appropriate form.

### **Example: Ogre Trample**

**Trample \[Action\].** The ogre moves up to 40 feet in a straight line through the spaces of Medium or smaller creatures. Each target makes a DC 14 Dexterity Saving Throw. Failure: 1d10 + 4 Bludgeoning damage and Prone. Success: half damage, no Prone. The ogre cannot affect the same creature twice.

## **8.15 Pinning**

> **ADVANCED RULE** A creature can Pin another only if it is at least two sizes larger and has a trait, succeeds with a dedicated Action, or ends a Trample in a space the rule permits it to occupy.

**Pin \[Action\].** The larger creature makes an Unarmed Strike to Grapple. On a success, the target is Grappled and Restrained while sharing the larger creature’s space. The larger creature’s Speed is halved.

The pinned target can use an Action to attempt escape against the Impact DC. An adjacent ally can Help. The pinner deals no automatic damage; crushing requires an Unarmed Strike, Bonus Action, or trait. If the pinner moves away, is Incapacitated, or cannot maintain the shared space, the Pin ends.

> **DESIGN RECOMMENDATION** Keep Pinning Advanced. Shared-space exceptions are powerful and create grid questions; only monsters and forms built around the tactic need them.

## **8.16 Collisions and Forced Movement into Obstacles**

> **CORE RULE** When at least 10 feet of forceful movement would drive a creature into a hard obstacle or another creature, the source may trade the unused movement for one **Collision Rider**.

Choose one:

- deal one Interaction Die of Bludgeoning damage for each full 10 feet of unused forced movement, maximum two dice;

- knock the moved creature Prone; or

- damage the obstacle with the same dice.

If the original effect already deals damage, the direct target takes at most one additional Interaction Die unless the effect was specifically designed as a collision. If the obstacle is another creature, that creature makes an Impact Save; on a failure, split the collision damage between them and it falls Prone. On a success, only the moved creature is affected.

### **Hard and Soft Obstacles**

A stone wall, metal gate, large tree, or cliff face is hard. A curtain, hedge, stack of empty crates, or yielding creature may instead break, move, or become Difficult Terrain with no extra damage.

**Example:** A warlock pushes a bandit 20 feet, but a wall is 10 feet behind the bandit. The bandit moves 10 feet and hits the wall. Because the spell already deals damage, the GM adds at most one Interaction Die, or chooses Prone instead. The wall does not create a second full instance of the spell’s damage.

## **8.17 Falling Objects**

> **CORE RULE** A falling Object threatens a space based on its size. A creature that can perceive the fall makes a Dexterity Saving Throw against the Severity DC.

| **Fall distance**  | **Damage dice**                | **Default severity**           |
|--------------------|--------------------------------|--------------------------------|
| 10–20 feet         | Listed Momentum Dice           | Moderate                       |
| 30–60 feet         | Add one copy of the base die   | Major                          |
| 70–120 feet        | Add two copies of the base die | Major                          |
| More than 120 feet | Double listed Momentum Dice    | Extreme only if scale warrants |

- **Success:** move to the nearest safe space within 5 feet, or take half damage if no safe space exists.

- **Failure:** take the damage and fall Prone. If the Object is at least two sizes larger, the target may also be trapped beneath it as an authored Major or Extreme effect.

The Object takes the same damage unless its material or shape prevents it. A falling object’s area, notice, and damage should be telegraphed when it is a deliberate player choice.

## **8.18 Falling Creatures onto Creatures**

When a falling creature lands on another creature, the lower creature makes a DC 15 Dexterity Saving Throw.

- **Success:** the lower creature moves to an adjacent safe space; the falling creature lands normally.

- **Failure:** divide the falling damage evenly between them, and both fall Prone.

If the falling creature is at least two sizes larger, use its Momentum Dice as a minimum for the lower creature’s share. This resolution is the Environmental Rider; do not add a separate collision rider.

## **8.19 Simple Hazards**

> **CORE RULE** A **Simple Hazard** resolves from one trigger and one effect. It may remain in place, but each exposure uses the same entry.

Every Hazard entry includes:

| **Field**             | **Required content**                                                   |
|-----------------------|------------------------------------------------------------------------|
| **Name and tier**     | Reader-facing identity and expected level band                         |
| **Severity and tags** | Minor, Moderate, Major, or Extreme; damage, material, and sensory tags |
| **Clue**              | What a creature can perceive before triggering it                      |
| **Trigger**           | Exact event that activates the Hazard                                  |
| **Area or target**    | Spaces or creatures affected                                           |
| **Test**              | Save or check, DC, and who rolls                                       |
| **Failure / Success** | Complete outcomes                                                      |
| **Countermeasures**   | At least one way to avoid, disable, contain, or exploit it             |
| **Duration / reset**  | How long it persists and whether it resets                             |

### **Complex Hazards**

> **ADVANCED RULE** A **Complex Hazard** rolls Initiative or acts at a fixed count, has multiple components or stages, and ends when a clock, component, or countermeasure is completed. Complex Hazards should have an XP value or encounter-budget cost in the final system.

## **8.20 Hazard Example: Alchemist’s Vapor**

**Alchemist’s Vapor; Hero Tier; Major \[Poison, Gas, Obscuring, Flammable\]**

- **Clue:** Bitter almond and hot-metal odor; green vapor hugging the floor; scorched vent covers.

- **Trigger:** A creature opens the cracked retort, damages the pipe, or enters the sealed lab after the release.

- **Area:** The vapor fills a 15-foot-radius floor-level area and lightly obscures it.

- **Constitution Saving Throw:** DC 15 when a breathing creature enters for the first time on a turn or ends its turn there.

- **Failure:** 2d6 Poison damage and Poisoned until the end of the creature’s next turn.

- **Success:** Half damage; not Poisoned.

- **Countermeasures:** Strong wind disperses one 5-foot band per round. Sealing the leak requires a DC 15 Dexterity (Alchemist’s Supplies or Tinker’s Tools) check. A creature above the vapor may avoid exposure.

- **Fire interaction:** A Fire source can replace the vapor with a one-time 15-foot-radius ignition. Creatures make a DC 15 Dexterity Saving Throw, taking 2d6 Fire damage on a failure or half on a success. The vapor then ends. They do not also take Poison damage from that exposure.

- **Duration:** 10 minutes in the sealed room, or until dispersed or ignited.

## **8.21 Hazard Example: Failing Masonry**

**Failing Masonry; Adventurer Tier; Moderate \[Bludgeoning, Brittle, Unstable\]**

- **Clue:** Fresh dust, bowed stones, and a grinding sound under heavy steps.

- **Trigger:** A creature Dashes across, deals Thunder damage in the passage, or places a Large load on the floor.

- **Area:** One 10-foot square.

- **Dexterity Saving Throw:** DC 13.

- **Failure:** 1d4 Bludgeoning damage, Prone, and the space becomes Difficult Terrain.

- **Success:** Move to the nearest safe edge.

- **Countermeasures:** Move at half Speed; brace the arch with timber; use Mason’s Tools and 10 minutes; trigger it from a distance.

- **Reset:** None.

## **8.22 Worked Interaction Examples**

### **Example A: Frozen Escape**

A wizard casts a Cold spell at a creature standing beside a canal. The player’s intent is to freeze an escape route, not gain extra damage. The spell resolves normally. The GM chooses a Moderate terrain rider: one 5-foot water space freezes into Slick Ice. No second save is added to the original target.

### **Example B: Shattering the Chandelier**

A bard uses Thunder against a crystal chandelier over two guards. The chandelier is Brittle and overhead. The bard can choose the spell’s normal creature effect or aim the interaction at the chandelier if the spell permits the target. The GM sets a Major rider because the large fixture can fall: the guards make DC 15 Dexterity saves against 2d6 falling-object damage. This consumes the one rider; no shards Hazard appears immediately.

### **Example C: The Ram and the Gate**

A Huge giant charges 40 feet and slams a reinforced gate. Its listed Momentum Dice are 2d10; the charge raises this to 4d10. The gate has AC 15, 45 Hit Points, and Threshold 20. The giant spends its Action on the impact. Damage above the threshold is applied once. At half Hit Points the gate becomes Broken and gains a visible gap; it does not explode merely because the giant is Huge.

### **Example D: Force into a Brazier**

A spell pushes a cultist 15 feet into a lit brazier 10 feet away. The spell resolves, moves the cultist 10 feet, and can create one rider. The GM offers the player a choice: the cultist falls Prone at the brazier, or the brazier overturns and creates a Moderate Burning Hazard in one adjacent space. The cultist does not take collision damage and Burning damage from the same rider.

## **8.23 Environmental GM Fiat**

> **GM GUIDANCE—ADJUDICATION CLAUSE**

- If the result is harmless and obvious, narrate it.

- If a player invested an appropriate action or resource in a reasonable setup, produce a useful effect even if the exact chemistry is uncertain.

- Reveal obvious Medium traits before commitment.

- Do not retroactively declare every room fireproof, every chain insulated, or every wall indestructible because a tactic is effective.

- Likewise, do not let a cantrip demolish a fortress because the player used technical vocabulary.

- If scale is uncertain, choose Moderate, resolve one rider, and record the question for later.

- When an interaction would trivialize a set piece, ask whether the players discovered the intended weakness, paid an appropriate resource, and accepted a meaningful risk. If yes, let the world change.

## **8.24 Environmental Module Status**

> **DESIGN RECOMMENDATION** The five-step procedure, one-rider limit, Interaction Dice, object baseline, and priced Overrun/Trample rules should be Core. Pinning, detailed thresholds, Broken vehicle components, and Complex Hazards should remain Advanced.
>
> **OPEN DECISION** Do damage types receive universal default interactions printed in the player rules, or are the matrix and examples GM-facing permissions? The current draft makes the procedure Core but keeps most specific interactions in the GM chapter to avoid turning every damage spell into a mandatory combo.

# **9. EXPLORATION AND RESOURCE MANAGEMENT**

## **9.1 Exploration Modes**

> **CORE RULE** Use the least structured time scale that preserves meaningful decisions.

| **Mode**               | **Use when**                                                                | **Time unit**   |
|------------------------|-----------------------------------------------------------------------------|-----------------|
| **Free Play**          | Conversation, safe movement, and ordinary activity without active pressure  | Flexible        |
| **Exploration Rounds** | Light, spells, noise, searches, Hazards, and encounter risk interact        | 10 minutes      |
| **Travel Watches**     | Crossing regions where weather, navigation, supplies, and encounters matter | 4 hours         |
| **Combat Rounds**      | Hostile action requires second-by-second order                              | 6 seconds       |
| **Downtime Turns**     | Projects, relationships, training, and factions develop                     | 1 day or 1 week |

Do not remain in Exploration Rounds while characters conduct routine business in a secure inn. Do not stay in Free Play while torches burn beside a locked door in hostile territory.

## **9.2 The Exploration Round**

> **CORE RULE** One Exploration Round is approximately 10 minutes. Use this procedure:

1.  **Orient.** The GM describes immediately perceivable exits, terrain, sensory clues, known threats, and active time pressure.

2.  **Choose tasks.** Each character declares one Exploration Task or a specific action.

3.  **Resolve movement and tasks.** Use automatic outcomes first; roll only for uncertainty with consequence.

4.  **Mark time and resources.** Advance light, spell durations, supplies, fatigue, projects, and Hazards.

5.  **Apply pressure.** Make an encounter/event check or advance the relevant clock when required.

6.  **Update the situation.** Reveal consequences and begin the next round only if structure still matters.

### **Exploration Tasks**

| **Task**            | **Effect**                                                                       |
|---------------------|----------------------------------------------------------------------------------|
| **Advance**         | Guide the group at the chosen pace; navigate obvious routes                      |
| **Keep Watch**      | Watch one direction or category of threat; normally use Passive Perception       |
| **Search**          | Physically examine one defined area or object for concealed details              |
| **Study**           | Analyze a clue, mechanism, map, creature sign, text, or magical phenomenon       |
| **Map**             | Maintain a usable route record; helps prevent becoming lost and supports retreat |
| **Scout**           | Move ahead or along a flank; risk separation to gain earlier information         |
| **Work**            | Pick a lock, force a door, treat an injury, repair, excavate, or use a tool      |
| **Forage**          | Seek food, water, fuel, or useful materials where the environment permits        |
| **Guard or Assist** | Protect a working character or provide qualified Help                            |

A character can perform one substantial task per round. Brief communication and ordinary movement are included.

## **9.3 Dungeon Movement**

Use bands unless exact movement matters:

| **Pace**     | **Distance per 10-minute round** | **Effect**                                                                                |
|--------------|----------------------------------|-------------------------------------------------------------------------------------------|
| **Cautious** | 150 feet                         | Map, watch, and notice obvious clues normally; can stop before visible Hazards            |
| **Standard** | 300 feet                         | Normal expedition pace; one task per character                                            |
| **Hurried**  | 600 feet                         | Disadvantage on Search and Study; cannot map accurately; noise may force a pressure check |

These distances abstract pauses, formation, doors, footing, and observation. In a mapped, cleared, and safe route, the GM can move the party directly without counting rounds.

## **9.4 Light and Darkness**

Track who carries light, its radius, and its remaining duration when darkness creates risk.

### **Light Source Baselines**

| **Source**       | **Bright / Dim radius** | **Duration**      | **Notes**                     |
|------------------|-------------------------|-------------------|-------------------------------|
| Candle           | 5 / 5 feet              | 1 hour            | Fragile in wind               |
| Torch            | 20 / 20 feet            | 1 hour            | One hand; can ignite material |
| Hooded lantern   | 30 / 30 feet            | 6 hours per flask | Hood can reduce to Dim Light  |
| Bullseye lantern | 60-foot cone / +60 Dim  | 6 hours per flask | Directional                   |
| Campfire         | 20 / 20 feet or more    | Fuel-dependent    | Smoke and visibility matter   |

One hour equals six Exploration Rounds.

> **CORE RULE** At the start of an expedition, record each tracked light source with six boxes per hour. Mark one box after each Exploration Round. Combat normally consumes one box only if ten minutes of total time pass.

### **Real-Time Torches**

> **OPTIONAL RULE** A torch expires after 60 minutes of real table time. Start a visible timer when lit; it continues during combat and discussion unless play pauses. Magical light uses written game-time duration unless the campaign converts it too.

**Research Basis.** Shadowdark makes torch time real time and explicitly continues the timer during combat. Its official guidance also ties checks to time pressure and consequences. Old-School Essentials instead uses ten-minute turns, with a torch lasting six turns. \[R7\] \[R8\]

> **DESIGN RECOMMENDATION** Use six Exploration Rounds in the Core. Real-time torches create urgency but make out-of-character deliberation a character resource; that should be an opt-in table contract.

## **9.5 Darkvision**

### **Compatibility Core**

> **CORE RULE** Darkvision converts Darkness within its range to Dim Light for that creature. In Dim Light, sight-based Wisdom (Perception) checks have Disadvantage. Darkvision alone cannot discern ordinary color.

In addition, this draft proposes:

- fine visual Search and Study involving color, ink, hairline seams, surface texture, or distant detail require a light source or a nonvisual method;

- total cover and opaque darkness still block sight;

- a hidden creature is not automatically detected merely for entering Darkvision range; and

- mundane Darkvision does not reveal magical Darkness.

### **Limited Darkvision**

> **OPTIONAL RULE** Replace most ancestry Darkvision with **Low-Light Vision**: the creature ignores Disadvantage from Dim Light but gains no sight in Darkness. Ancestries with supernatural darkness identities may retain Darkvision.

### **No Default Darkvision**

> **OPTIONAL RULE** Remove ordinary ancestry Darkvision. Replace it with Low-Light Vision, another sense, a skill permission, or a modest ancestry trait. Darkvision becomes magical, monstrous, or rare.
>
> **OPEN DECISION** Darkvision is one of the highest-impact campaign dials because it changes ancestry balance, encounter visibility, stealth, light inventory, and published maps. Choose Compatibility, Limited, or None before ancestry redesign.

## **9.6 Pressure and Random Encounters**

Random encounters are not a punishment for rolling badly; they make time, noise, and route choice consequential.

> **CORE RULE** Assign the current site a Pressure rate.

| **Pressure** | **Check frequency**        |
|--------------|----------------------------|
| **Calm**     | Every 3 Exploration Rounds |
| **Alert**    | Every 2 Exploration Rounds |
| **Hostile**  | Every Exploration Round    |

At the end of the required round, roll 1d6:

| **d6** | **Result**                                                       |
|--------|------------------------------------------------------------------|
| 1      | Encounter or active threat                                       |
| 2      | Omen, evidence, faction movement, Hazard shift, or clock advance |
| 3–6    | No immediate event                                               |

Loud violence, alarms, demolition, or repeated failed forcing attempts can cause an immediate check or raise Pressure. Clever concealment, disabling alarms, securing a route, or defeating the active faction can lower it.

An encounter result is a prompt, not necessarily a fight. Roll reaction, consider distance and goals, and provide warning when the fiction allows.

## **9.7 Search, Study, and Investigation**

> **CORE RULE** A player describes an area and method. If the method would reveal the fact and time is available, the GM reveals it. Roll only when the clue is uncertain, concealed against skill, or costly to obtain under pressure.

### **Search**

Search covers immediate sensory examination: feel the wall, lift the rug, listen at the door, sift the ashes, check the corpse, smell the vial.

### **Study**

Study covers analysis and recall: infer the mechanism, identify the heraldry, reconstruct the battle, determine the spell school, compare the tracks, translate the inscription.

### **One Approach, One Resolution**

A failed Search or Study resolves that approach. Repeating the same words does not produce a new roll. The players may:

- spend another Exploration Round for a more thorough method;

- use a tool, spell, light source, or new vantage;

- risk triggering or partially dismantling the feature;

- consult a relevant expert or record; or

- leave the uncertainty unresolved.

> **GM GUIDANCE** Give clues that invite action. “The flagstone is clean around its edge” produces play; “make a Perception check” postpones it.

## **9.8 Traps**

Traps use three layers:

1.  **Notice the clue.** Passive Perception or declared Search reveals evidence appropriate to the approach.

2.  **Understand the danger.** Study, tools, experimentation, or contextual knowledge reveals trigger and likely effect.

3.  **Bypass or counter.** Utilize, tools, movement, expendable gear, magic, or accepting a different route resolves the obstacle.

No layer requires a roll if the method clearly works. A check is useful when speed, delicacy, hidden complexity, or a dangerous consequence matters.

### **Trap Writing Standard**

Use the Hazard template from Section 8. Include at least one non-roll countermeasure and one consequence other than Hit Point damage when possible.

### **Example: Scything Threshold**

**Scything Threshold; Adventurer Tier; Major \[Trap, Slashing, Mechanical\]**

- **Clue:** Parallel cuts in the door frame; a taut wire glimpsed at ankle height.

- **Trigger:** More than 20 pounds crosses the wire.

- **Area:** 5-foot-wide line across the doorway.

- **Dexterity Saving Throw:** DC 15.

- **Failure:** 2d4 Slashing damage and pushed 5 feet into the room.

- **Success:** Half damage; no push.

- **Countermeasures:** Step over after spotting it; cut the drive cable from the safe side; pin the blade housing with Thieves’ Tools; trigger it with a pole.

- **Reset:** Manual reset from a concealed panel.

## **9.9 Doors, Locks, and Secret Passages**

### **Doors**

State whether a door is open, closed, stuck, barred, locked, sealed, trapped, or magically secured. These states are not interchangeable.

- **Stuck:** force with Strength; failure costs time/noise or worsens position.

- **Barred:** attack the door, reach the bar, break a component, or use leverage.

- **Locked:** use the key, tools, magic, bypass the frame, or destroy the lock.

- **Sealed:** identify the seal and its condition.

### **Locks**

A routine lock opened by a proficient character with proper tools and no pressure needs no roll; it costs an Exploration Round. Roll when the lock is exceptional, time matters, the tools are poor, or failure has a consequence.

### **Secret Passages**

Secret passages should have discoverable traces: airflow, architectural asymmetry, wear, sound, dust, mismatched mortar, or a suspicious void on a map. A check can locate or interpret the trace, but the passage should not exist only behind a blind roll.

## **9.10 Encumbrance**

### **Compatibility Weight**

> **CORE RULE—PROVISIONAL** Until a campaign selects another method, use the 2024-compatible carrying rules. Containers, armor, weapons, ammunition, rations, light, tools, treasure, and bulky Objects still matter when their weight becomes consequential.

### **Slot Encumbrance**

> **OPTIONAL RULE** A character has **Load Slots = 10 + Strength modifier**, minimum 5. It can carry up to twice that number.

| **Item**                                              | **Slots**                     |
|-------------------------------------------------------|-------------------------------|
| Tiny worn item, one coin, incidental component        | 0; bundle sensible quantities |
| Light weapon, tool kit, lantern, 3 rations, 100 coins | 1                             |
| Shield, one-handed martial weapon, bulky pack item    | 2                             |
| Light armor                                           | 2                             |
| Medium armor                                          | 3                             |
| Heavy armor                                           | 4                             |
| Two-handed weapon or large adventuring tool           | 2                             |
| Awkward or oversized Object                           | 3+ and may require hands      |

- At or below Load Slots: no penalty.

- Above Load Slots: **Encumbered**; Speed reduced by 10 feet.

- Above twice Load Slots: cannot travel or fight effectively; the GM requires dropping, dragging, a vehicle, or assistance.

Worn clothing, one set of belt pouches, and a negligible amount of personal items are free. Containers organize items but do not create capacity.

> **OPEN DECISION** Slot encumbrance creates stronger expedition choices than pounds but requires an equipment conversion. It should be tested before being declared Core.

## **9.11 Food, Water, Weather, and Exhaustion**

Use the current Exhaustion track:

- each level imposes a cumulative −2 penalty to D20 Tests;

- each level reduces Speed by 5 feet;

- six levels cause death;

- a qualifying Long Rest reduces Exhaustion by one.

> **CORE RULE** When a creature lacks required food, water, shelter, breathable air, or weather protection, the relevant travel or Hazard procedure states when it gains Exhaustion. Do not call for a daily Survival check if failure has no consequence beyond calling for the same check again.

### **Daily Supply Baseline**

One Medium creature normally consumes:

- 1 ration or equivalent food;

- 1 gallon of water in temperate conditions, more in heat or strenuous travel; and

- appropriate protection for the weather.

Foraging produces **Supply Units** rather than tracking exact calories. One Supply Unit feeds one Medium creature for one day or provides its normal water requirement, chosen when gathered.

### **Weather as a Hazard**

Write severe weather as a Hazard with interval, save, failure, and countermeasures. Proper clothing, route choice, shelter, pace, and acclimation should change the save or eliminate it.

## **9.12 Travel Watches**

Divide a travel day into three 4-hour Watches: two for ordinary travel and one for camp, rest, or an additional forced march.

For each travel Watch:

1.  choose pace and route;

2.  assign navigation, watch, forage, scout, and support tasks;

3.  resolve weather and terrain;

4.  mark supplies and distance;

5.  make the region’s event check; and

6.  update fatigue, location, and faction clocks.

### **Travel Pace**

| **Pace** | **Distance** | **Effects**                                             |
|----------|--------------|---------------------------------------------------------|
| Slow     | ⅔ normal     | Easier stealth, foraging, mapping, and Hazard avoidance |
| Normal   | Normal       | No modifier                                             |
| Fast     | 1⅓ normal    | Reduced observation; higher navigation or fatigue risk  |

The campaign map defines normal daily distance by terrain. Do not pretend forest, road, mountain, swamp, and open sea share one useful rate.

## **9.13 Resting**

### **Compatibility Rest**

Use 2024 Short and Long Rests during the first combat baseline test.

### **Safe-Haven Rest**

> **OPTIONAL RULE** A **Long Rest** grants full recovery only in a secure place with shelter, food, water, and a reasonable expectation of uninterrupted sleep. A field camp grants a **Field Rest**: recover expended Hit Dice as a Long Rest, reduce Exhaustion if supplied, and regain features that explicitly allow Field Rest recovery, but do not restore all Hit Points or all spell slots.

This draft intentionally leaves the exact Field Rest recovery table open until class resource audits are complete.

> **DESIGN RECOMMENDATION** Test exploration first with ordinary Long Rests, then add Safe-Haven Rest. Changing rests alters encounter pacing, class balance, healing, spell slots, and adventure geography simultaneously.

## **9.14 Retreating from a Dungeon**

> **CORE RULE** If the party has a mapped, cleared route and no active pursuit, the GM can charge the expected time and pressure checks rather than replay every room. If the route has changed, enemies reorganized, or a Hazard advanced, resolve the return through Exploration Rounds.

A successful retreat preserves information and recovered treasure. It is a strategic choice, not a failed adventure.

# **10. SOCIAL AND ROLEPLAY MECHANICS**

## **10.1 Social Resolution Principle**

> **CORE RULE** Social mechanics determine how an NPC responds within its motives, knowledge, authority, and risk tolerance. They do not transfer control of the NPC to the roller.

Before a check, establish:

- what the player character wants;

- what the NPC wants, fears, or protects;

- the NPC’s attitude;

- what the NPC can actually do;

- what would make the request acceptable; and

- the likely consequence of refusal or pressure.

## **10.2 NPC Attitudes**

Use three compatibility attitudes:

| **Attitude**    | **Posture**                                                                  |
|-----------------|------------------------------------------------------------------------------|
| **Friendly**    | Wants to help within reasonable cost and loyalty                             |
| **Indifferent** | Helps when the request aligns with interest, duty, fairness, or compensation |
| **Hostile**     | Opposes the characters or treats their success as a cost                     |

Attitude is not emotion alone. A furious sworn ally can remain Friendly to the party’s objective; a charming rival can remain Hostile.

## **10.3 Reaction Rolls**

> **CORE RULE** When the GM does not already know an unplanned creature or group’s starting posture, roll 2d6 and apply no more than ±2 from obvious circumstances, reputation, language, surprise, or offers.

| **2d6** | **Starting reaction**                                              |
|---------|--------------------------------------------------------------------|
| 2       | Immediate hostility, attack, alarm, or intolerable demand          |
| 3–5     | Unfriendly; suspicious, defensive, exploitative, or ready to leave |
| 6–8     | Uncertain; curious, cautious, divided, or willing to hear terms    |
| 9–11    | Favorable; open, practical, or willing to trade information        |
| 12+     | Helpful; sees common cause or a valuable opportunity               |

The result sets the opening posture, not a compulsory action. Apply the NPC’s motive and the situation.

**Research Basis.** Basic and old-school D&D procedures commonly use 2d6 reaction results to prevent every uncertain encounter from defaulting to combat. Shadowdark foregrounds reaction checks in its compact encounter procedure. \[R7\] \[R8\]

## **10.4 The Influence Action**

> **CORE RULE** A creature takes the **Influence Action** to make a bounded request, bargain, appeal, threat, deception, or command when the outcome is uncertain.

1.  **State the request and approach.**

2.  **Determine willingness.**

3.  **Resolve automatically or set a DC.**

4.  **Apply the NPC’s response and consequence.**

### **Willingness**

| **State**     | **Resolution**                                                                                      |
|---------------|-----------------------------------------------------------------------------------------------------|
| **Willing**   | The NPC agrees without a check, subject to logistics                                                |
| **Hesitant**  | A check, concession, proof, or changed circumstance can secure agreement                            |
| **Unwilling** | No check can secure this request now; play must change motive, leverage, authority, or circumstance |

Use DC 15 for a meaningful request from a Hesitant NPC, modified by stakes:

| **Circumstance**                                     | **DC adjustment** |
|------------------------------------------------------|-------------------|
| Request strongly aligns with motive or duty          | −5                |
| Fair exchange, trusted proof, or useful leverage     | −2                |
| Significant cost, risk, delay, or loss of face       | +2                |
| Severe danger, betrayal, taboo, or lasting sacrifice | +5 or Unwilling   |

Choose the ability and skill from the approach. Deception can win agreement but creates a later consequence when exposed. Intimidation can produce compliance while worsening attitude, reputation, or future cooperation.

### **Influence Outcomes**

- **Success:** the NPC agrees to the bounded request, offers acceptable terms, or reveals what would complete the agreement.

- **Failure:** the NPC refuses, asks a meaningful price, delays, narrows the offer, becomes guarded, or acts on the pressure. Failure does not erase earlier truthful information.

- **Success by 5 or more:** when useful, improve terms or attitude by one step for the scene.

- **Failure by 5 or more:** when telegraphed, worsen attitude, close the current approach, or trigger a social consequence.

> **GM GUIDANCE** “Persuasion is not mind control” becomes actionable when the GM identifies willingness before the roll. An Unwilling target needs changed circumstances, not a higher modifier.

## **10.5 Requests by Scale**

| **Request**        | **Typical result on success**                                                |
|--------------------|------------------------------------------------------------------------------|
| **Trivial**        | Information already safe to share; ordinary courtesy; small favor            |
| **Minor**          | Short assistance, modest discount, introduction, temporary access            |
| **Significant**    | Risk, secrecy, meaningful resources, public support, dangerous service       |
| **Transformative** | Betray a core loyalty, surrender a life’s work, accept ruin, change identity |

Transformative requests are normally Unwilling until play changes the NPC’s situation. One roll can resolve the final decision after the characters earn the possibility; it cannot replace the earning.

## **10.6 Morale**

> **CORE RULE** Non-player combatants and retainers have a **Morale Score** from 2 to 12. When a morale trigger occurs, roll 2d6. If the result exceeds the score, the group breaks. Otherwise it holds.

| **Morale** | **Typical creature**                                     |
|------------|----------------------------------------------------------|
| 4          | Untrained, coerced, cowardly, or self-preserving         |
| 6          | Ordinary hireling, hungry beast, uncertain bandit        |
| 8          | Trained soldier, territorial predator, committed cultist |
| 10         | Elite guard, fanatic, bonded war beast                   |
| 12         | Mindless, magically compelled, or utterly devoted        |

### **Triggers**

Check at most twice in one encounter, using the most relevant:

- first ally killed or clearly incapacitated;

- half the group unable to fight;

- leader Bloodied, defeated, or fleeing;

- objective lost;

- escape route opened or closed;

- terrifying display, unexpected reinforcement, or catastrophic Hazard.

### **Breaking**

On a failed morale check, choose or roll the response that fits:

- retreat toward safety;

- surrender or drop weapons;

- bargain, offer information, or release a hostage;

- scatter or hide;

- defend only an escape route; or

- abandon the objective but protect allies.

Player characters do not make Morale checks. A player may choose fear or surrender for Heroic Inspiration when it engages a Drive or Obligation.

**Research Basis.** Old-School Essentials checks 2d6 against a 2–12 Morale Score at decisive moments such as the first death and half the group being incapacitated. \[R8\]

## **10.7 Reputation**

Track Reputation separately for each important faction from −3 to +3.

| **Score** | **Standing**        |
|-----------|---------------------|
| −3        | Hunted or condemned |
| −2        | Hostile             |
| −1        | Distrusted          |
| 0         | Unknown or mixed    |
| +1        | Recognized          |
| +2        | Trusted             |
| +3        | Champion or insider |

Reputation modifies reaction by at most ±2 and changes access, prices, rumors, protection, and obligations. It does not add directly to every Charisma check.

Reputation changes after public, attributable, meaningful actions—not after every conversation.

## **10.8 Faction Clocks and Fronts**

> **CORE RULE—GM TOOLKIT** Give an active faction one **Goal Clock** and, when needed, one **Crisis Clock**. Use 4 segments for a short project, 6 for a campaign development, and 8 for a slow or difficult transformation.

Advance a clock when:

- a Downtime Turn passes and the faction has means to act;

- the characters ignore a telegraphed threat;

- an adventure outcome materially helps the faction;

- an environmental or political event creates opportunity; or

- the consequence of a failed action names that advance.

When filled, the clock changes the world. Do not fill a clock merely to preserve a prewritten plot.

**Research Basis.** Blades in the Dark uses progress clocks to represent obstacles and faction projects, advancing faction agendas during downtime. \[R12\]

## **10.9 Drives, Bonds, Oaths, and Obligations**

Each player character writes:

- **Two Drives:** outcomes the character actively pursues.

- **One Bond:** a person, place, group, or ideal the character protects.

- **One Oath or Obligation:** a duty that can demand a cost.

Good commitments are specific enough to create decisions:

- weak: “I value freedom.”

- useful: “No prisoner leaves my custody in chains.”

- weak: “I seek knowledge.”

- useful: “I will recover the atlas my mentor died hiding.”

When a commitment causes a material complication or sacrifice, the character gains Heroic Inspiration. The GM may also use it to offer a choice; the player remains free to refuse without penalty.

## **10.10 Social Consequences**

Use consequences that continue play:

- a concession or price;

- delay;

- public embarrassment or lost status;

- a promise recorded as an Obligation;

- exposure of a lie;

- damaged Reputation;

- faction-clock advance;

- restricted access;

- a rival’s counteroffer;

- partial information; or

- agreement with a condition.

Avoid “the NPC refuses and the scene ends” unless the characters knowingly risked that closure.

## **10.11 Downtime Relationships**

> **OPTIONAL RULE** A relationship has a 4-segment **Trust Clock** and a stated boundary. During Downtime, a character can spend one Turn and an appropriate resource, favor, or act of service to attempt progress.

- On success, fill 1 segment.

- On a significant sacrifice or exceptional success, fill 2.

- On failure, do not erase earned Trust; introduce a need, misunderstanding, rival, or boundary.

- At 4 segments, the relationship grants a defined permission: sanctuary, reliable information, an introduction, a shared project, or aid within limits.

Trust is not romance currency and does not override consent, identity, or independent goals.

# **11. MAGIC SYSTEM OPTIONS**

## **11.1 Default Magic Chassis**

> **CORE RULE** Keep 2024-compatible spell slots, spell levels, spell attacks, Saving Throws, Concentration, rituals, and components during v0.1.

This preserves player content and lets environmental rules be tested without simultaneously changing casting reliability and resource cadence.

## **11.2 Spellcasting Clarity Pass**

Before rewriting a spell, its template should answer:

- What is the casting time and Action type?

- What are the range, target, and point of origin?

- Does the caster need sight, a clear path, or both?

- What does the spell affect: creatures, Objects, structures, terrain, or some subset?

- Which D20 Test occurs, and when?

- What happens on success and failure?

- How long does it last?

- Does it require Concentration?

- How does it end early?

- What increases at higher spell levels?

- Which environmental tags or interactions are explicit?

## **11.3 Concentration**

Keep one Concentration effect per caster. Concentration is a valuable limit on persistent control and stacking.

Future clarification should distinguish:

- **damage-triggered checks;**

- **environmental disruption** such as violent motion or suffocation;

- **Incapacitated and death;**

- **willingly ending Concentration;** and

- **effects maintained by a structure, ritual circle, or independent entity rather than a caster.**

Do not require Concentration merely because a spell lasts longer than one round. Use it to limit combinations and create meaningful interruption.

## **11.4 Components**

> **CORE RULE** Verbal, Somatic, and Material components remain mechanically meaningful.

- **Verbal:** audible magical utterance; silence, gagging, and stealth matter.

- **Somatic:** deliberate movement; hands, bindings, and occupied equipment matter as specified.

- **Material:** a component pouch or focus supplies unpriced components. A stated price and consumption are separate requirements.

Components should create adventure hooks for rare rituals and powerful magic without turning ordinary casting into inventory accounting.

## **11.5 Rituals**

Rituals are a primary bridge between magic and exploration.

> **DESIGN RECOMMENDATION** Expand rituals through authored procedures rather than simply adding more spells with “Ritual” tags.

A major ritual can require:

- a site or celestial time;

- one or more skilled participants;

- a material cost or recovered relic;

- a clock measured in Exploration or Downtime Turns;

- visible stages enemies can interrupt;

- a Study or Magic Action at each decisive stage; and

- consequences that alter the location on failure.

## **11.6 Environmental Tags for Spells**

Spells use tags only when they change interpretation.

| **Tag**                | **Meaning**                                                     |
|------------------------|-----------------------------------------------------------------|
| **Affects Objects**    | The spell can directly target or damage Objects under its text  |
| **Affects Structures** | It can affect structural components at an appropriate scale     |
| **Ignites**            | It can start a sustained Burning Hazard in valid fuel           |
| **Freezes**            | It can create an ice terrain rider in valid water               |
| **Conductive**         | It can create the Lightning-and-water rider                     |
| **Corrosive**          | It can apply Corroded or reduce a threshold                     |
| **Sunlight**           | Its light counts as sunlight; Radiant alone does not imply this |
| **Disperses Gas**      | It moves or removes Obscuring or Poison gas                     |

Do not attach every plausible Medium as a spell tag. The environmental procedure handles ordinary cases; tags declare exceptions and reliable permissions.

## **11.7 Cantrips**

The Core keeps at-will cantrips for compatibility.

Potential limitations:

| **Option**              | **Effect**                                                                             | **Risk**                                                   |
|-------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------|
| **No change**           | At-will, scaling cantrips                                                              | Preserves compatibility; reduces mundane resource pressure |
| **Utility limits only** | Repeated world-altering utility cantrips consume time or cannot create permanent value | Requires careful wording; can feel arbitrary               |
| **Cantrip fatigue**     | Repeating the same cantrip in a scene eventually risks a casting check                 | Adds tracking and changes caster damage baseline           |
| **Prepared cantrips**   | Swap only at rest or training                                                          | Low impact; already familiar in some classes               |
| **No combat scaling**   | Cantrips remain low damage                                                             | Requires class damage replacement                          |

> **DESIGN RECOMMENDATION** Do not limit combat cantrips in v0.1. First test whether environment and exploration rules actually produce the feared infinite-utility problems. Add explicit object/creation limits to individual cantrips where necessary.

## **11.8 Roll-to-Cast Module**

### **Full Roll-to-Cast**

> **OPTIONAL RULE—EXPERIMENTAL** A caster knows or prepares spells but has no spell slots. To cast a leveled spell, make a Spellcasting Ability Check and add Proficiency Bonus.

**Casting DC = 10 + spell level**

- **Success:** the spell is cast.

- **Failure:** the spell is not cast and cannot be attempted again until the caster completes a Long Rest.

- **Natural 1:** as failure, and roll on the Mishap table.

- **Natural 20:** the spell is cast and gains a modest authored boon, such as maximum one damage die or +1 round duration; it does not automatically double every effect.

Cantrips use DC 10 and are not lost on failure, but a natural 1 still causes a minor Mishap.

This module needs class-specific rules for prepared spells, recovery, upcasting, Counterspell, rituals, multiclassing, and magic items. It is not compatible with ordinary slot-based balance.

**Research Basis.** Shadowdark’s magic uses a roll-to-cast model: success casts the spell and failure prevents casting that spell again until rest, supporting volatile magic without daily spell slots. \[R7\]

### **Risky Overcast**

> **OPTIONAL RULE—RECOMMENDED PROTOTYPE** Keep spell slots. A caster that lacks a slot may attempt to **Overcast** a prepared spell of 1st through 5th level.

**Overcast check:** spellcasting ability check + Proficiency Bonus against DC 12 + twice the spell’s level.

- **Success:** cast the spell at its lowest level, then gain one Exhaustion level.

- **Failure:** the spell is not cast; gain one Exhaustion level and roll a Mishap.

- **Natural 1:** gain two Exhaustion levels instead and roll a Mishap.

A creature cannot Overcast if doing so would reach six Exhaustion levels. Overcast cannot create a spell component or bypass a consumed material.

This preserves the slot game while allowing desperate magic. The Exhaustion cost makes it self-limiting and should be tested carefully.

## **11.9 Spell Mishaps**

> **OPTIONAL RULE** Roll 1d8. Tailor damage to one Interaction Die for the caster’s tier.

| **d8** | **Mishap**                                                                                                                    |
|--------|-------------------------------------------------------------------------------------------------------------------------------|
| 1      | **Backlash:** take one Interaction Die of Force damage; cannot be reduced by the spell itself                                 |
| 2      | **Displacement:** teleport 10 feet to a random legal space the GM can see                                                     |
| 3      | **Flare:** emit Bright Light and loud sound; hidden position is revealed                                                      |
| 4      | **Drain:** lose one unspent Hit Die; if none, take one Interaction Die of Necrotic damage                                     |
| 5      | **Warped Medium:** create a Minor environmental rider matching the spell at the caster’s space                                |
| 6      | **Broken Focus:** a nonmagical focus or component pouch is unusable until repaired during a Short Rest                        |
| 7      | **Echo:** the nearest eligible creature perceives a brief magical image, thought, or voice from the caster                    |
| 8      | **Unstable Opening:** advance a local magical clock or give the GM one magical complication to introduce before the next rest |

Mishaps should complicate rather than randomly erase a character.

## **11.10 Magic Decision Gate**

> **OPEN DECISION** Before spell redesign:

- Are spell slots Core for the final system?

- Is Overcast a campaign option, a feat, or absent?

- Does Radiant imply light only when tagged, or by default?

- Which spells can affect Objects and structures?

- How much mundane utility may a cantrip produce over repeated time?

- Are rituals a spell property, a separate project system, or both?

- Does Counterspell use a D20 Test, automatic slot comparison, or a hybrid?

- Does safe-haven rest alter spell-slot recovery?

# **12. ADVANCEMENT AND REWARDS**

## **12.1 Reward Principle**

> **CORE RULE** Reward the behavior the campaign wants repeated. Do not claim the game values discovery, negotiation, and retreat while awarding nearly all advancement for killing monsters.

Advancement has three layers:

- **Level:** class progression and core power.

- **Character rewards:** feats, training, contacts, titles, items, and permissions.

- **World rewards:** safe routes, faction standing, domains, knowledge, and changed environments.

## **12.2 Advancement Models**

| **Model**         | **Procedure**                                                        | **Encourages**                                   | **Main risk**                                           |
|-------------------|----------------------------------------------------------------------|--------------------------------------------------|---------------------------------------------------------|
| **Milestone**     | Level after a declared arc or achievement                            | Story completion and simple bookkeeping          | Criteria can feel opaque or GM-controlled               |
| **Monster XP**    | Divide XP for defeated threats                                       | Confronting encounters                           | “Defeated” can drift toward “killed”; encounter farming |
| **Treasure XP**   | Award XP for valuables recovered to safety                           | Exploration, risk assessment, retreat, logistics | Campaign economy and level curve become linked          |
| **Goal XP**       | Award for objectives, discoveries, faction changes                   | Mission focus and diverse solutions              | Requires clear goal pricing                             |
| **Session marks** | Gain a fixed or question-based number of marks; level at a threshold | Steady pacing and explicit values                | Can flatten differences in achievement                  |
| **Hybrid**        | Combine goals, discoveries, and a smaller treasure or threat award   | Broad adventure behavior                         | More categories to explain                              |

## **12.3 Proposed Default: Adventure Marks**

> **DESIGN RECOMMENDATION** Use **Adventure Marks** for the first playtest because they make reward behavior explicit without binding advancement to an unfinished economy.

A character needs 10 Adventure Marks to gain a level. At the end of a session or expedition, award the party:

| **Achievement**                                                              | **Marks**                   |
|------------------------------------------------------------------------------|-----------------------------|
| Complete a minor stated objective                                            | 1                           |
| Complete a major objective or materially change a faction situation          | 2                           |
| Recover a significant treasure, relic, route, or body of knowledge to safety | 1                           |
| Discover and act upon a major secret, location, or opportunity               | 1                           |
| Resolve a dangerous obstacle without merely bypassing the campaign’s premise | 1                           |
| Accept a lasting consequence to uphold a party commitment                    | 1, at most once per session |

Divide marks equally. Normally award 1–3 per session and no more than 4. “Significant” is defined relative to the party’s current tier.

This rate is provisional. A level every four to seven sessions is the intended starting band, not a final promise.

## **12.4 Milestone Mode**

> **OPTIONAL RULE** Before an arc begins, state the milestone conditions in broad terms: “secure two alliances and expose the usurper,” not “when the GM feels the chapter is over.” Level when the party achieves the milestone or decisively transforms it.

Intermediate rewards—feats, Reputation, items, or permissions—prevent long arcs from feeling static.

## **12.5 Standard XP Mode**

> **OPTIONAL RULE** Use the compatibility baseline’s level thresholds and monster XP. Award full encounter XP for defeating, bypassing, converting, containing, or forcing the retreat of a threat when the party meaningfully overcame its danger. Award goal XP equivalent to encounters of the intended difficulty.

Do not award the same threat twice because it retreats and is later killed without becoming a renewed obstacle.

## **12.6 Treasure XP Mode**

> **OPTIONAL RULE** Award 1 XP per gold piece of nonmagical treasure recovered from dangerous or contested locations and brought to a safe haven. Divide XP among participating characters and retainers according to the campaign’s share rules.

- Sale value, not notional art value, determines XP unless appraised.

- Coins already owned, ordinary wages, loans, and resale loops grant no XP.

- Magic items grant no treasure XP unless permanently sold or sacrificed.

- Monster XP is absent or reduced to one-quarter.

- Treasure placement becomes adventure-balance work.

Before using this module, recalibrate treasure to the chosen level curve. Published modern treasure assumptions do not automatically support classic 1-gp-for-1-XP progression.

## **12.7 Goal and Quest XP**

Goals should be player-visible and outcome-based. Price them against expected session length and danger:

| **Goal**     | **Adventure Marks** | **Standard-XP comparison**           |
|--------------|---------------------|--------------------------------------|
| Minor        | 1                   | Low encounter                        |
| Major        | 2                   | Moderate encounter                   |
| Arc-defining | 3–4                 | High encounter or milestone fraction |

A method-neutral goal is “ensure the caravan reaches Stonebridge,” not “kill the raiders.”

## **12.8 Carousing**

> **OPTIONAL RULE** During Downtime, spend a week and a lifestyle-scaled amount of treasure to Carouse in a community.

Choose one objective: rumor, contact, Reputation, market access, faction insight, or relief from an Obligation. Make a relevant check only if uncertainty and consequence remain.

- **Success:** gain the chosen benefit.

- **Failure:** gain a reduced benefit and a complication—debt, rival, scandal, mistaken rumor, or faction attention.

Carousing can convert treasure into social and informational progress without converting it directly into class power.

## **12.9 Training**

Training can grant:

- a language capability;

- tool proficiency;

- weapon training or mastery access;

- a Capability Rank;

- a downtime technique;

- a feat when the campaign awards a feat;

- entry into a faction, school, or domain office.

> **CORE RULE** Training requires a teacher or source, time, and any stated cost. A level does not wait on training unless the campaign explicitly chooses training-for-levels.

### **Training for Levels**

> **OPTIONAL RULE** After earning advancement, a character must spend one Downtime Turn per new tier and pay a tier-scaled cost before gaining the new level. The level is never lost; it is pending. Use only if instructors, travel, and institutions are part of play.

## **12.10 Feat-Based Advancement**

> **OPTIONAL RULE** Instead of a level, a campaign reward can grant a curated feat, proficiency, spell, mastery, or +1 ability increase. Do not allow unrestricted feat purchasing with gold unless a full advancement economy is designed.

This works well for domain rewards and lateral progression at a level cap.

## **12.11 Random Advancement**

> **OPTIONAL RULE—EXPERIMENTAL** When gaining a level, roll once on a class-specific development table and choose either the rolled benefit or one adjacent result. Random benefits must be lateral and cannot replace required chassis features such as Extra Attack, spell-level access, or Hit Point growth.

Random advancement should generate texture, not permanently sabotage a character concept.

## **12.12 Advancement Decision Gate**

> **OPEN DECISION** Before classes are rewritten:

- Which advancement model is the actual Core?

- What is the expected sessions-per-level curve by tier?

- Do all characters advance together?

- Can non-level rewards increase combat math?

- Are Ability Score Improvements and feats still class-level features?

- Is multiclassing balanced against the same advancement currency?

- Does treasure purchase power directly, indirectly through training, or mainly world influence?

# **13. MONSTER AND ENCOUNTER DESIGN**

## **13.1 Monster Design Goal**

Monsters should be readable in play, behaviorally distinct, and connected to their environments. A stat block is not merely a bag of attacks; it encodes what the creature wants, how it changes the battlefield, when it retreats, and which part of the world it exploits.

For v0.1, existing 2024-compatible monsters remain usable. Add only:

- a role;

- a Morale Score;

- one sentence of tactics or motive;

- an optional Bloodied behavior; and

- at most one environmental, momentum, or lair trait unless the monster is a set piece.

## **13.2 Monster Roles**

Roles are descriptive design tags, not classes.

| **Role**       | **Battlefield job**                                       | **Common tools**                                             |
|----------------|-----------------------------------------------------------|--------------------------------------------------------------|
| **Brute**      | Threatens through high damage and durability              | Heavy hits, Momentum, simple vulnerability                   |
| **Soldier**    | Holds space and protects allies                           | High AC, marks, reactions, reach                             |
| **Skirmisher** | Changes angles and punishes isolation                     | Mobility, Disengage, hit-and-run                             |
| **Artillery**  | Projects danger at range                                  | Ranged damage, lines, zones, fragile defense                 |
| **Controller** | Changes terrain, movement, or action options              | Hazards, pushes, walls, conditions                           |
| **Support**    | Improves allies or sustains an objective                  | Healing, commands, reactions, protection                     |
| **Lurker**     | Creates a burst after concealment or setup                | Hide, ambush, delayed strike, escape                         |
| **Minion**     | Represents numerous fragile threats                       | One meaningful hit; simplified durability                    |
| **Elite**      | Counts as roughly two creatures and has action resilience | Extra Reaction, phase, recovery, strong trigger              |
| **Solo**       | Occupies a whole encounter’s attention                    | Multiple turns or actions, phase changes, control resistance |

A monster can have one primary and one secondary role. More labels usually signal a muddled design.

## **13.3 Monster Intent and Morale**

Every encounter note should answer:

- Why is the monster here?

- What does it want right now?

- What will it not risk?

- What changes its plan?

- What does it do on a failed morale check?

Suggested Morale:

| **Creature type**                                  | **Score** |
|----------------------------------------------------|-----------|
| Scavenger, coerced laborer, petty thief            | 4–6       |
| Territorial beast, ordinary guard, mercenary       | 6–8       |
| Trained warband, protecting parent, committed cult | 8–10      |
| Fanatic, construct, undead under control           | 10–12     |

Mindless does not always mean Morale 12. A programmed construct may withdraw when its ward leaves; a skeleton might preserve itself for later orders.

## **13.4 Bloodied Triggers**

Bloodied triggers create phase and information without universal penalties.

Good triggers:

- immediately move without provoking;

- recharge a signature action once;

- break armor and lower AC while increasing damage;

- release a Hazard;

- change morale or target priority;

- expose a weak point;

- shed a rider, passenger, or protective shell.

Bad triggers:

- add a new condition every round with no counterplay;

- erase successful control automatically;

- double all damage without encounter-budget accounting;

- require hidden bookkeeping the players cannot read.

> **CORE RULE** A Bloodied trigger happens once when the creature first becomes Bloodied unless the trait explicitly resets.

## **13.5 Environmental Traits**

An environmental monster trait should specify Source, Medium, cost, Severity, and rider.

### **Template**

**Trait Name \[Cost; Recharge if any\].** *Source + Medium.* Target/area. D20 Test. Failure. Success. Environmental change. Duration and limit.

### **Example: Magma Blood**

**Magma Blood \[Reaction; once while Bloodied\].** When the salamander first becomes Bloodied, it ruptures and creates a Moderate Burning Hazard in one unoccupied 5-foot space within 5 feet. The Hazard deals one Interaction Die of Fire damage and lasts 3 rounds. The triggering damage does not also gain extra Fire damage.

### **Example: Rootbreaker**

**Rootbreaker \[Trait\].** The treant’s Bludgeoning attacks deal double damage to unattended wood Objects and ignore the first 10 points of a wooden component’s Damage Threshold. This permission is narrow and visible; it does not double damage to creatures made of wood unless their stat block says so.

## **13.6 Trample and Collision Traits**

Use the Section 8 templates. Price them against Multiattack:

- a **Trample Action** generally replaces Multiattack;

- a **Trample attack replacement** affects one target and replaces one attack;

- a **Recharge Trample** may affect multiple targets and deal normal Momentum Damage;

- a **free movement rider** should deal no damage or be usable once per turn against one target;

- a **Collision Reaction** requires an enemy to create the forced movement or enter a declared line.

Large size alone grants no free damage.

## **13.7 Encounter Building Baseline**

> **CORE RULE—PROVISIONAL** Use the 2024 encounter XP budgets and monster XP values as the numerical starting point. Then review the encounter’s **danger flags** before assigning its final label.

**Research Basis.** SRD 5.2.1 presents Low, Moderate, and High XP budgets per character. Pathfinder 2e likewise builds encounters from party XP budgets and creature level, while explicitly adjusting for party size. These systems show the value of visible budgets, but their numbers are not interchangeable. \[R1\] \[R5\]

### **Encounter Construction Procedure**

1.  Identify the encounter objective and likely end conditions.

2.  Choose the intended difficulty: Low, Moderate, or High.

3.  Calculate the 2024 budget for party level and size.

4.  Select monsters and Hazards within the budget.

5.  Assign roles; check action count and range coverage.

6.  Add terrain that offers information and choices to both sides.

7.  Review danger flags.

8.  Define morale, retreat, reinforcement, and negotiation behavior.

9.  Record what changes if the characters arrive early, late, quietly, or prepared.

### **Danger Flags**

Each flag can make an encounter play above its nominal budget:

- enemies gain a large action-count advantage;

- a Solo lacks action resilience and may instead be trivialized;

- surprise is likely and hard to prevent;

- enemies begin in inaccessible range, flight, or Total Cover;

- repeated area damage punishes the party’s required formation;

- control can remove multiple characters for whole rounds;

- a Hazard acts without budget or countermeasure;

- terrain strongly favors only one side;

- reinforcements are not included in the budget;

- the party enters with depleted resources;

- escape is concealed or impossible;

- monster damage can focus a single character before the party can respond.

> **GM GUIDANCE** One mild flag calls for caution. Two strong flags usually justify treating the encounter as one difficulty band higher, reducing enemy budget, or improving telegraphed counterplay. This is a review rule, not a hidden arithmetic multiplier.

### **The Quick Lethality Check**

As a secondary warning, compare total enemy Challenge Rating to party level:

- an encounter may be deadly when total monster CR is greater than one-half the sum of character levels for characters above level 4;

- for levels 1–4, use one-quarter instead.

This is a rough diagnostic, not the Core budget. It is useful when a published encounter includes unusually dangerous monsters or when the exact budget is not at hand. \[R13\]

## **13.8 Hazards in Encounter Budgets**

Until Hazard XP values are calibrated:

- a Moderate simple Hazard that can affect one creature at a time is terrain, not a full monster;

- a Major simple Hazard that attacks multiple creatures or acts repeatedly counts as roughly one ordinary creature of the adventure tier;

- a Complex Hazard counts as one or more creatures according to its action count, durability, and control;

- a Hazard with no clues or countermeasures is a surprise tax, not legitimate difficulty.

These are provisional authoring rules. Record actual damage, lost turns, and resource expenditure during tests.

## **13.9 Lair and Environment Actions**

Lair actions make the location act. They should:

- occur at a fixed Initiative count;

- telegraph the next effect when severe;

- alter a limited area;

- offer at least one positioning or Utilize countermeasure;

- avoid repeating the same unavoidable damage;

- stop when the relevant component, ritual, or monster is defeated.

### **Example Lair Cycle**

At Initiative 20, choose one not used in the previous round:

1.  **Steam Vent:** mark two grates; at Initiative 20 next round, each erupts as a Moderate Fire/Obscuring Hazard.

2.  **Chain Sweep:** one hanging chain line becomes Difficult Terrain; a creature can Utilize it to swing or secure it.

3.  **Furnace Draw:** loose smoke moves 15 feet toward the furnace; Poison gas follows the same direction.

The cycle creates information and choices before damage.

## **13.10 Simplified Stat Block Template**

> **CORE TEMPLATE**

**NAME** *Size Type, alignment or disposition; Role; Tier*

**AC** X **Initiative** +X **HP** X (**Bloodied** X) **Speed** X **Morale** X **Senses** … **Languages** …

| **STR**      | **DEX**      | **CON**      | **INT**      | **WIS**      | **CHA**      |
|--------------|--------------|--------------|--------------|--------------|--------------|
| score (+mod) | score (+mod) | score (+mod) | score (+mod) | score (+mod) | score (+mod) |

**Saves** … **Skills** … **Resistances/Immunities** … **Traits** only those that change decisions.

**Actions**

**Attack Name.** *Melee/Ranged Attack Roll:* +X, reach/range, target. *Hit:* average (dice + mod) Damage Type damage; rider.

**Signature Action \[Recharge X–Y\].** Cost, targets, save, outcomes, duration.

**Reaction** if behaviorally important.

**Bloodied—Trigger.** One-time phase behavior.

**Environment.** Source + Medium interaction, cost, Severity, rider.

**Tactics and Morale.** Two sentences: opening behavior, change point, failed morale response.

## **13.11 Example Monster: Cinderhide Siege Boar**

**CINDERHIDE SIEGE BOAR** *Huge Monstrosity, Unaligned; Brute/Controller; Hero Tier*

**AC** 15 **Initiative** +1 **HP** 126 (**Bloodied** 63) **Speed** 40 ft. **Morale** 8 **Senses** Darkvision 60 ft., Passive Perception 13

| **STR** | **DEX** | **CON** | **INT** | **WIS** | **CHA** |
|---------|---------|---------|---------|---------|---------|
| 23 (+6) | 12 (+1) | 21 (+5) | 3 (−4)  | 13 (+1) | 8 (−1)  |

**Saves** Str +9, Con +8 **Resistances** Fire **Role Note.** Built as a demonstration, not a final CR-assigned monster.

**Heated Hide.** A creature that Grapples the boar or starts its turn Grappling it takes 1d6 Fire damage.

**Actions**

**Gore.** *Melee Attack Roll:* +9, reach 10 ft., one target. *Hit:* 19 (3d8 + 6) Piercing damage.

**Siege Trample \[Recharge 5–6\].** The boar moves up to its Speed in a straight line through spaces of Large or smaller creatures. Each target makes a DC 17 Dexterity Saving Throw. Failure: 2d10 + 6 Bludgeoning damage and Prone. Success: half damage, no Prone. A creature can be affected once. The boar deals double damage from this Action to Objects and structural components.

**Bloodied—Cinder Burst.** When first Bloodied, cracks in the boar’s hide release embers. It creates three Moderate Burning Hazards in unoccupied spaces within 10 feet. Each lasts 3 rounds. The triggering damage gains no additional rider.

**Tactics and Morale.** It tramples lines and barriers, then gores isolated creatures. On failed morale, it charges toward the clearest exit, even through a fragile barrier.

## **13.12 Monster Design Questions**

> **OPEN DECISION**

- Are monster roles printed in stat blocks or kept as designer metadata?

- Does every monster receive a Morale Score?

- How many Bloodied triggers can an Elite or Solo support?

- Do Minions use 1 Hit Point, a damage threshold, or “two hits” durability?

- Are legendary actions retained, replaced by multiple Reactions, or converted to fixed turns?

- How are Hazards priced in encounter budgets?

- Does Challenge Rating remain the monster-facing rating, or is a tier/level value added?

# **14. RULES LANGUAGE AND TEMPLATE STANDARDS**

## **14.1 House Style Principles**

Rules text should be:

- **glossary-first:** use a defined term instead of near-synonyms;

- **ordered:** trigger, cost, target, test, outcome, duration, limit;

- **active:** name who acts;

- **bounded:** state targets, range, timing, and frequency;

- **exception-aware:** say which general rule changes;

- **table-readable:** put decisive numbers before flavor; and

- **fictionally legible:** pair mechanics with an observable event.

## **14.2 Capitalization**

Capitalize a term when it names a defined game object, state, or procedure.

| **Capitalize**                                     | **Lowercase unless sentence case** |
|----------------------------------------------------|------------------------------------|
| Action, Bonus Action, Reaction                     | turn, round, scene                 |
| D20 Test, Ability Check, Saving Throw, Attack Roll | check when used generically        |
| Armor Class, Hit Points, Proficiency Bonus         | damage, healing                    |
| Advantage, Disadvantage, Heroic Inspiration        | bonus, penalty                     |
| Bloodied, Grappled, Prone, Restrained              | wounded, hidden in ordinary prose  |
| Search, Study, Influence, Utilize, Magic           | search when used as ordinary verb  |
| Hazard, Object, Structure, Occupied Space          | terrain, room, wall                |
| Exploration Round, Travel Watch, Downtime Turn     | hour, day, journey                 |
| Environmental Rider, Interaction Die, Impact Save  | fire, water, collision             |

Damage Types are capitalized when naming the game category: Fire damage, not fire Damage.

## **14.3 Keywords and Tags**

Use tags in square brackets after the name or cost line:

**Burning Pitch; Moderate \[Fire, Hazard, Flammable\]**

Tags should provide at least one of:

- a rule interaction;

- a search/filter function;

- an immunity, resistance, or countermeasure hook;

- a templating requirement.

Do not create a tag merely to restate flavor.

## **14.4 Rule Hierarchy Language**

Use:

- **must** for a requirement;

- **can** for capability;

- **may** for a choice;

- **normally** for a default with anticipated exceptions;

- **unless** to introduce a narrow exception;

- **and** when all clauses apply;

- **or** when one option applies;

- **up to** when zero is allowed;

- **once per turn/round/rest** for explicit frequency.

Avoid “should” inside binding rules. Reserve it for GM Guidance and design recommendations.

## **14.5 Action Template**

> **CORE TEMPLATE**

**NAME \[Action cost; frequency or Recharge\].** *Trigger or requirement, if any.* Choose a target within range. Make or require the named D20 Test against the stated target. **Success/Hit:** complete effect. **Failure/Miss:** complete effect. State movement, duration, ending condition, and repeat limit.

### **Example**

**Hook and Haul \[Attack Replacement; once per turn\].** Choose one Large or smaller creature within 15 feet holding or adjacent to a secured rope. The target makes a DC 15 Strength Saving Throw. **Failure:** pull it up to 10 feet toward the anchor. **Success:** pull it 5 feet. This movement does not provoke Opportunity Attacks.

## **14.6 Attack Template**

**NAME.** *Melee Attack Roll:* +X, reach X ft., one target. *Hit:* average (dice + modifier) Damage Type damage, followed by a concise rider.

For player rules, state the attack ability and proficiency if they are not inherited from a weapon or spell.

Do not hide a save after an attack in prose. Put it in a new sentence with ability and DC.

## **14.7 Saving Throw Template**

> **CORE TEMPLATE**

**Ability Saving Throw:** DC X, each \[target\] in \[area/range\]. **Failure:** complete outcome. **Success:** complete outcome.

If the save repeats, state exactly when and whether success ends the effect. If the target chooses between abilities, put the choice before the DC.

### **Example**

**Strength or Dexterity Saving Throw:** DC 14, one creature no more than one size larger than you. **Failure:** the target is pushed 10 feet and falls Prone. **Success:** the target is pushed 5 feet.

## **14.8 Hazard Template**

**NAME; tier; Severity \[tags\]**

- **Clue:** observable information.

- **Trigger:** exact activation.

- **Area/Target:** scope.

- **Test:** ability, DC, roller.

- **Failure:** outcome.

- **Success:** outcome.

- **Countermeasures:** two or more approaches when practical.

- **Duration/Reset:** persistence.

- **Escalation:** later change, if any.

A Hazard that cannot be perceived before it harms the characters needs a compelling fictional reason and should be priced as unavoidable encounter damage.

## **14.9 Environmental Interaction Template**

**NAME \[cost; frequency\].** *Source + Medium trait; Severity.* State trigger and target. State whether the direct target is excluded from extra damage. Give the test and DC. Choose one rider. State duration and chain limit.

### **Example**

**Conductive Pool \[Environmental Rider; Moderate\].** *Lightning + connected water.* After Lightning strikes a point in the pool, choose up to two secondary creatures within 10 feet in the same water. **Dexterity Saving Throw:** source DC. **Failure:** one Interaction Die of Lightning damage. **Success:** no damage. A creature already affected by the source is ineligible.

## **14.10 Optional Rule Template**

Every optional rule begins with:

- **Purpose:** the play experience it creates;

- **Replaces/Adds:** exact Core rules changed;

- **Procedure:** complete text;

- **Dependencies:** other modules or conversions required;

- **Expected effects:** pacing, balance, complexity, and player behavior;

- **Exit rule:** how to remove it between sessions or campaigns.

Do not call a rule optional if later chapters silently assume it.

## **14.11 GM Fiat Flags**

Use one of three labels:

- **GM Choice:** the rule deliberately gives a bounded menu.

- **GM Adjudication:** apply the stated procedure to an unlisted case.

- **Campaign Definition:** decide once before play and publish the answer.

Avoid “the GM decides” without criteria.

### **Adjudication Clause Template**

**GM Adjudication.** Choose the lowest Severity that produces the established result. Tell the players the observable risk before commitment. Apply one rider. If the scale remains uncertain, use Moderate and record the precedent.

## **14.12 Numbers and Measurements**

- Write “10 feet,” not “10 ft.” in player-facing prose; stat blocks may abbreviate.

- Use numerals for game quantities.

- Put average damage before dice in monster stat blocks: 11 (2d6 + 4).

- State radius, cone, line, emanation, or selected spaces precisely.

- “Within 10 feet” includes a target at the origin only if the rule does not say “another.”

- A duration ending “at the start of your next turn” differs from “until the end of your next turn.”

- Use “half its Hit Point maximum or fewer” for Bloodied.

## **14.13 Editing Checklist**

For every rule, ask:

1.  Is the trigger perceivable?

2.  Who chooses targets and options?

3.  What resource or Action does it cost?

4.  What is the range and valid target?

5.  Is there one resolution roll or an unnecessary chain?

6.  Are success and failure both complete?

7.  Does the rule say when it ends?

8.  Can it affect Objects, Structures, and Hazards?

9.  Does it stack with itself?

10. Does a specific exception identify the general rule it changes?

11. Does it create a free damage or action loop?

12. Can it be understood in under a minute at the table?

# **15. OPEN DECISIONS AND QUESTIONS**

This section is a design gate. The recommended option is marked **Recommended**, but no item is treated as final until confirmed.

## **15.1 Must Decide Now**

1.  **What is the compatibility promise?**

- **Recommended:** 2024 classes, spells, monsters, and adventures run with light annotations.

- Stricter: drop-in numerical and textual compatibility.

- Looser: recognizable d20 play, but conversion is expected.

2.  **What is the default action economy?**

- **Recommended:** Action, Bonus Action, Reaction, movement.

- True three-action economy.

- Standard/Move/Minor.

3.  **What is the default campaign tone?**

- **Recommended:** heroic characters in a consequential world, with peril modules.

- Gritty low fantasy.

- High-powered heroic fantasy.

- Explicitly equal support for all three, accepting more setup text.

4.  **Are Environmental Interactions Core?**

- **Recommended:** the five-step procedure and one-rider limit are Core; advanced mass/structure detail is modular.

- Entire chapter Optional.

- Universal damage-type riders become automatic Core rules.

5.  **Is Morale Core for non-player creatures?**

- **Recommended:** yes, with at most two checks per encounter.

- GM Toolkit only.

- Only creatures with a printed Morale trait.

6.  **Which exploration structure is Core?**

- **Recommended:** activate 10-minute Exploration Rounds only when time and pressure matter.

- Always use dungeon turns in hostile sites.

- Entirely freeform with procedures as optional tools.

7.  **What is the Core advancement model?**

- **Recommended for playtest:** Adventure Marks.

- Milestone.

- Standard XP.

- Treasure XP.

- Hybrid standard XP plus goals/treasure.

8.  **How is Darkvision handled?**

- Keep compatibility Darkvision with stronger Dim Light limits.

- **Recommended for Perilous play:** most ancestries gain Low-Light Vision instead.

- Remove default Darkvision.

## **15.2 Decide Before Class Design**

1.  Do classes remain twenty-level and subclass-based?

2.  Is the subclass level cadence universal?

3.  Are Background ability increases fixed, listed-choice, or free?

4.  Is multiclassing Core, Advanced, or excluded from the first packet?

5.  Does proficiency remain binary plus Expertise?

6.  If Master and Legendary ranks exist, are they permissions only?

7.  Do all classes need authored exploration and social features?

8.  Are Weapon Masteries retained unchanged, expanded, or replaced?

9.  How much Bonus Action compression is acceptable?

10. Are Drives/Bonds/Oaths on every character sheet?

11. What ancestry power band and scaling rule applies?

12. Which existing homebrew, including the Veteran Fighter, is a balance benchmark?

## **15.3 Decide Before Spell Redesign**

1.  Are spell slots the permanent Core?

2.  Is roll-to-cast a full alternate campaign mode, a smaller Overcast rule, or absent?

3.  Do cantrips remain at-will and level-scaling?

4.  Which spells can target unattended Objects?

5.  Which spells can damage Structures?

6.  Are environmental tags permissions, guarantees, or designer metadata?

7.  Does Radiant create light by default?

8.  Does Fire ignite only when text says **Ignites**, or through the general Medium procedure?

9.  Are rituals expanded into projects?

10. Does Concentration remain binary and limited to one effect?

11. How does Counterspell resolve?

12. How does the chosen rest module affect spell recovery?

## **15.4 Decide Before Monster Redesign**

1.  Is Challenge Rating retained as the published compatibility rating?

2.  Is a separate monster level or tier printed?

3.  Are roles visible to the GM?

4.  Does every monster receive Morale and a motive?

5.  How are Elite and Solo action economies constructed?

6.  Are legendary actions retained?

7.  How are Minions represented?

8.  How much encounter budget does a Hazard consume?

9.  How many environmental traits can an ordinary monster have?

10. Do Large creatures gain Overrun access by size, or only when printed?

11. Are Bloodied triggers common, role-specific, or reserved for major monsters?

## **15.5 Decide Before the First Public Playtest**

1.  Which modules are actually active in the packet?

2.  What level range is tested first? **Recommended: levels 3–5.**

3.  Which three encounter types must appear? **Recommended: negotiation/reaction, hazardous exploration, and tactical combat with retreat.**

4.  Which published 2024-compatible characters are allowed?

5.  How are rulings recorded?

6.  What metrics are captured: round length, rules lookups, damage, lost turns, resources, retreats, environmental uses, and GM confidence?

7.  What content is deliberately out of scope?

8.  What is the safety and tone agreement for wounds, surrender, captivity, and attacks on fallen characters?

9.  Does the packet include a conversion sheet for existing adventures?

10. What counts as a failed test versus a successful consequence?

## **15.6 Can Decide Later**

- Final working title.

- Domain scale and mass combat.

- Detailed hireling loyalty and wages.

- Naval, aerial, and spelljamming vehicle subsystems.

- Crafting recipes and item economy.

- Random advancement tables.

- Full language ranks.

- Called shots and detailed armor damage.

- Extreme weather catalogs.

- Epic-level siege mathematics.

- Psionics as a separate magic structure.

- Setting-specific ancestry terminology.

## **15.7 Recommended Answer Set for v0.2**

If no contrary preference is supplied, proceed with this temporary design lock:

| **Decision**               | **v0.2 assumption**                                                  |
|----------------------------|----------------------------------------------------------------------|
| Compatibility              | Light-annotation compatibility with 2024 material                    |
| Action economy             | 2024-style                                                           |
| Tone                       | Heroic expedition with explicit peril modules                        |
| Environmental interactions | Core procedure; advanced mass/structures modular                     |
| Morale                     | Core for non-player creatures                                        |
| Exploration                | 10-minute rounds when pressure is active                             |
| Proficiency                | Binary plus Expertise                                                |
| Darkvision                 | Compatibility Core; Low-Light module tested                          |
| Magic                      | Spell slots Core; Overcast experimental                              |
| Advancement                | Adventure Marks for tests; final model open                          |
| Monsters                   | 2024 math plus Morale, role, and optional Bloodied/environment trait |

# **16. RECOMMENDED NEXT STEPS**

Each version should answer a bounded design question and include an exit criterion. Do not rewrite all player content before the engine survives focused tests.

| **Version** | **Focus**                              | **Deliverables**                                                                                                 | **Exit criterion**                                                                           |
|-------------|----------------------------------------|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| **v0.2**    | Core mechanic and terminology lock     | Glossary; D20 Test chapter; DCs; proficiency decision; adjudication hierarchy; compatibility statement           | Five sample scenes resolve without contradictory terms                                       |
| **v0.3**    | Action economy and combat loop         | Turn rules; Initiative; movement; grapple/shove; retreat; morale; conditions audit; action templates             | Two combats at levels 3 and 5 complete with acceptable round time and no action-loop exploit |
| **v0.4**    | Environmental interactions and Hazards | Final severity table; interaction matrix; object/structure rules; momentum; ten sample Hazards; GM quick sheet   | Ten edge cases produce results in under 60 seconds each; no repeated double-dipping          |
| **v0.5**    | Character creation and advancement     | Character steps; ancestry/background boundaries; proficiency choice; advancement model; two converted characters | Existing 2024 characters and new draft characters coexist in one session                     |
| **v0.6**    | Spell and magic decision pass          | Casting chassis decision; object/structure targeting; tags; rituals; optional Overcast; 25-spell audit           | Representative spells from every damage type interact predictably without universal rewrites |
| **v0.7**    | Monsters and encounters                | Role guide; Morale values; Bloodied traits; Hazard budgeting; Elite/Solo prototype; 12-monster test set          | Encounter labels match observed danger across at least six mixed encounters                  |
| **v0.8**    | First playtest packet                  | Levels 3–5 pregens; short expedition; GM rules; quick references; feedback form                                  | Two external groups complete the packet without designer facilitation                        |
| **v0.9**    | Revision after playtest                | Issue log; rule cuts; wording pass; probability and pacing adjustments                                           | Critical contradictions closed; optional modules have explicit dependencies                  |
| **v1.0**    | Stable foundation draft                | Integrated rules document; conversion guide; starter bestiary; adventure; reference sheets                       | System supports a short campaign and has a documented compatibility and update policy        |

## **16.1 Immediate v0.2 Worklist**

1.  Answer the eight “Must Decide Now” questions in Section 15.

2.  Build a canonical glossary from Appendix B.

3.  Run a probability review of DCs 10/13/15/18 against representative bonuses at levels 1, 5, 11, and 17.

4.  Convert six ambiguous situations into worked examples:

- hidden trap under time pressure;

- reluctant guard at a barred gate;

- Lightning in water;

- forced movement into a wall;

- Large creature Overrun;

- retreat from a losing combat.

5.  Audit the Veteran Fighter against the locked action economy and rules language.

6.  Select one level-3 party and one published short adventure as compatibility fixtures.

7.  Create a one-page ruling log with: rule questioned, temporary ruling, time spent, player expectation, and later disposition.

## **16.2 First Playtest Scenario**

The first packet should be a compact expedition with:

- one uncertain reaction encounter that can become alliance, toll, chase, or combat;

- one six-round light clock;

- one clue-forward trap;

- one elemental environment with at least three visible Medium traits;

- one Large monster with a priced Trample;

- one faction clock advanced by delay;

- one clear opportunity to retreat with treasure;

- one safe-haven decision; and

- no required new class or spell content.

The test question is not “Was the adventure fun?” alone. It is:

- Did players predict consequences accurately?

- Did the added procedures create choices?

- Did the GM resolve environmental ideas consistently?

- Did any procedure cause unnecessary rolls?

- Did players retreat, negotiate, or manipulate terrain because the rules supported those choices?

- Which rules did the table ignore because they were too slow?

# **APPENDIX A. RESEARCH BASIS AND SOURCES**

This appendix separates external factual basis from Hearth & Hazard’s recommendations. Access dates are July 2026. Rules facts should be rechecked against later errata before publication.

## **R1. D&D SRD 5.2.1**

**Dungeons & Dragons System Reference Document 5.2.1**, Wizards of the Coast. Primary source for the 2024-compatible D20 Test, action names, conditions, Bloodied, Influence attitudes, object statistics, Exhaustion, and encounter-budget baseline.

[<u>https://www.dndbeyond.com/srd</u>](https://www.dndbeyond.com/srd)

[<u>https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf</u>](https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf)

## **R2. Pathfinder 2e Actions**

**Archives of Nethys, Player Core: Actions.** Primary rules reference for the three-action-plus-Reaction structure and activities with variable action costs.

[<u>https://2e.aonprd.com/Rules.aspx?ID=2268</u>](https://2e.aonprd.com/Rules.aspx?ID=2268)

## **R3. Pathfinder 2e Checks and Degrees of Success**

**Archives of Nethys, Player Core: Checks.** Primary rules reference for Critical Success, Success, Failure, Critical Failure, ten-over/under results, and natural 20/1 degree adjustment.

[<u>https://2e.aonprd.com/Rules.aspx?ID=2269</u>](https://2e.aonprd.com/Rules.aspx?ID=2269)

## **R4. Pathfinder 2e Proficiency**

**Archives of Nethys, Player Core: Proficiency.** Primary rules reference for Untrained, Trained, Expert, Master, and Legendary ranks. Hearth & Hazard does not adopt Pathfinder’s level-added bonus formula.

[<u>https://2e.aonprd.com/Rules.aspx?ID=35</u>](https://2e.aonprd.com/Rules.aspx?ID=35)

## **R5. Pathfinder 2e Encounter Design**

**Archives of Nethys, GM Core: Building Encounters, XP Budget, Choosing Creatures, and Party Size.** Primary rules references for budget-based encounter construction and party-size adjustment.

[<u>https://2e.aonprd.com/Rules.aspx?ID=2713</u>](https://2e.aonprd.com/Rules.aspx?ID=2713)

[<u>https://2e.aonprd.com/Rules.aspx?ID=2717</u>](https://2e.aonprd.com/Rules.aspx?ID=2717)

[<u>https://2e.aonprd.com/Rules.aspx?ID=2715</u>](https://2e.aonprd.com/Rules.aspx?ID=2715)

[<u>https://2e.aonprd.com/Rules.aspx?ID=2719</u>](https://2e.aonprd.com/Rules.aspx?ID=2719)

## **R6. Pathfinder 2e Environment, Objects, Vehicles, and Hazards**

**Archives of Nethys.** Primary references for environmental damage categories, material statistics, Hardness, Broken Threshold, vehicle collision/Run Over, and Hazard construction.

[<u>https://2e.aonprd.com/Rules.aspx?ID=591</u>](https://2e.aonprd.com/Rules.aspx?ID=591)

[<u>https://2e.aonprd.com/Rules.aspx?ID=195</u>](https://2e.aonprd.com/Rules.aspx?ID=195)

[<u>https://2e.aonprd.com/Rules.aspx?ID=730</u>](https://2e.aonprd.com/Rules.aspx?ID=730)

[<u>https://2e.aonprd.com/Rules.aspx?ID=1278</u>](https://2e.aonprd.com/Rules.aspx?ID=1278)

[<u>https://2e.aonprd.com/Rules.aspx?ID=1291</u>](https://2e.aonprd.com/Rules.aspx?ID=1291)

[<u>https://2e.aonprd.com/Rules.aspx?ID=1043</u>](https://2e.aonprd.com/Rules.aspx?ID=1043)

## **R7. Shadowdark**

**The Arcane Library, Shadowdark RPG product overview and official rules FAQ.** Primary publisher descriptions for no default Darkvision, gear slots, treasure XP, roll-to-cast, morale/reaction, real-time torches, compact ranges, and the “roll when time pressure, skill, and consequence matter” approach.

[<u>https://www.thearcanelibrary.com/products/shadowdark-rpg</u>](https://www.thearcanelibrary.com/products/shadowdark-rpg)

[<u>https://www.thearcanelibrary.com/blogs/shadowdark-blog/shadowdark-rules-faq</u>](https://www.thearcanelibrary.com/blogs/shadowdark-blog/shadowdark-rules-faq)

## **R8. Old-School Essentials**

**Necrotic Gnome, Old-School Essentials SRD.** Primary references for dungeon turns, one-hour torches, encounter procedures, 2d6 reactions, and 2–12 Morale.

[<u>https://oldschoolessentials.necroticgnome.com/srd/index.php/Dungeon_Adventuring</u>](https://oldschoolessentials.necroticgnome.com/srd/index.php/Dungeon_Adventuring)

[<u>https://oldschoolessentials.necroticgnome.com/srd/index.php/Encounters</u>](https://oldschoolessentials.necroticgnome.com/srd/index.php/Encounters)

[<u>https://oldschoolessentials.necroticgnome.com/srd/index.php/Morale\_%28Optional_Rule%29</u>](https://oldschoolessentials.necroticgnome.com/srd/index.php/Morale_%28Optional_Rule%29)

[<u>https://oldschoolessentials.necroticgnome.com/srd/index.php/Time%2C_Weight%2C_Movement</u>](https://oldschoolessentials.necroticgnome.com/srd/index.php/Time%2C_Weight%2C_Movement)

[<u>https://oldschoolessentials.necroticgnome.com/srd/index.php/Adventuring_Gear</u>](https://oldschoolessentials.necroticgnome.com/srd/index.php/Adventuring_Gear)

## **R9. Game Structures and “System Matters”**

Justin Alexander, **“Game Structures—Addendum: System Matters,” The Alexandrian.** Design discussion on how procedures direct play and distribute authority.

[<u>https://thealexandrian.net/wordpress/43568/roleplaying-games/game-structures-addendum-system-matters</u>](https://thealexandrian.net/wordpress/43568/roleplaying-games/game-structures-addendum-system-matters)

## **R10. Information, Choice, Impact**

Chris McDowall, **“The ICI Doctrine,” Bastionland.** Design discussion framing meaningful decisions through Information, Choice, and Impact.

[<u>https://www.bastionland.com/2018/09/the-ici-doctrine-information-choice.html</u>](https://www.bastionland.com/2018/09/the-ici-doctrine-information-choice.html)

## **R11. Procedures**

Prismatic Wasteland, **“What Even Is a Procedure?”** Design discussion defining procedures as repeatable orders of operation and examining their role at the table.

[<u>https://www.prismaticwasteland.com/blog/what-even-is-a-procedure</u>](https://www.prismaticwasteland.com/blog/what-even-is-a-procedure)

## **R12. Progress Clocks and Factions**

John Harper, **Blades in the Dark SRD: Progress Clocks, Faction Game, and Downtime Activities.** Primary open rules reference for clocks and faction projects.

[<u>https://bladesinthedark.com/progress-clocks</u>](https://bladesinthedark.com/progress-clocks)

[<u>https://bladesinthedark.com/faction-game</u>](https://bladesinthedark.com/faction-game)

[<u>https://bladesinthedark.com/downtime-activities</u>](https://bladesinthedark.com/downtime-activities)

## **R13. Encounter Benchmark Commentary**

Mike Shea, **“D&D 2024 Encounter Building Compared to the Lazy DM Benchmark”** and **“The Lazy Encounter Benchmark,” Sly Flourish.** Independent design commentary comparing the 2024 budget method to a fast lethality diagnostic.

[<u>https://slyflourish.com/2024_dmg_encounter_building_versus_the_lazy_benchmark.html</u>](https://slyflourish.com/2024_dmg_encounter_building_versus_the_lazy_benchmark.html)

[<u>https://slyflourish.com/the_lazy_encounter_benchmark.html</u>](https://slyflourish.com/the_lazy_encounter_benchmark.html)

## **Project Sources Consulted**

- **Veteran Fighter Subclass**, existing DnD Homebrew Project PDF. Used as project-specific evidence for 2024 action compression, tactical general Actions, and the importance of preserving the Action/Bonus Action/Reaction chassis.

- **SRD 5.2.1**, existing project Library copy. Used to verify terminology and compatibility baselines.

- Prior project discussion concerning a five-step Environmental Interaction system, Interaction Dice by tier, anti-double-dipping, Lightning in water, Fire and oil, Cold and ice, object effects, and priced Momentum/Trample/Collision rules.

# **APPENDIX B. WORKING GLOSSARY**

| **Term**                | **Working definition**                                                        |
|-------------------------|-------------------------------------------------------------------------------|
| **Action**              | A major activity taken on a creature’s turn or when a rule permits            |
| **Adventure Mark**      | Provisional advancement unit; 10 produce one level                            |
| **Attitude**            | Friendly, Indifferent, or Hostile posture toward a request or party           |
| **Bloodied**            | At half Hit Point maximum or fewer                                            |
| **Bonus Action**        | An additional activity available only when a rule grants it                   |
| **Broken**              | Advanced vehicle/Object state at half component Hit Points                    |
| **Capability Rank**     | Optional permission tier: Untrained through Legendary                         |
| **Component**           | A meaningful part of a Structure or vehicle with its own statistics           |
| **Corroded**            | Object state that reduces Damage Threshold or weakens defense                 |
| **Damage Threshold**    | Damage below this value deals 0 to an Object/component                        |
| **D20 Test**            | An Ability Check, Saving Throw, or Attack Roll                                |
| **Downtime Turn**       | A day or week used for projects and faction activity                          |
| **Environmental Rider** | One additional or substituted consequence from Source interacting with Medium |
| **Exploration Round**   | Approximately 10 minutes of structured expedition activity                    |
| **Hazard**              | Environmental danger with a trigger and resolution procedure                  |
| **Heroic Inspiration**  | One reroll resource, provisionally retaining the 2024-compatible name         |
| **Impact Save**         | Strength-or-Dexterity save against mass, collision, Overrun, or Trample       |
| **Interaction Die**     | Tier-scaled die for incidental environmental damage                           |
| **Medium**              | Material, terrain, Object, creature, or space through which a Source acts     |
| **Momentum Damage**     | Damage based on size and meaningful speed                                     |
| **Morale Score**        | 2–12 rating; a group breaks when 2d6 exceeds it                               |
| **Object**              | Discrete noncreature with AC and Hit Points when needed                       |
| **Occupied Space**      | Area a creature controls in tactical play                                     |
| **Pressure**            | Frequency of exploration event checks: Calm, Alert, or Hostile                |
| **Reaction**            | Immediate response to a stated trigger; normally one per round                |
| **Severity**            | Minor, Moderate, Major, or Extreme interaction/Hazard scale                   |
| **Source**              | Energy, material, movement, or force initiating an interaction                |
| **Structure**           | Large construction divided into consequential components                      |
| **Travel Watch**        | Four-hour wilderness or journey procedure                                     |

# **APPENDIX C. TABLE QUICK REFERENCES**

## **C1. D20 Test**

1.  Establish intent.

2.  State obvious stakes.

3.  Choose specific rule or test.

4.  Set ability, proficiency, and DC.

5.  Roll once.

6.  Change the situation.

**Roll only when:** uncertain outcome + meaningful consequence.

## **C2. Environmental Interaction**

1.  Source.

2.  Medium and trait.

3.  Severity.

4.  One test if needed.

5.  One rider.

| **Severity** | **DC** | **Damage**         |
|--------------|--------|--------------------|
| Minor        | 10     | None               |
| Moderate     | 13     | 1 Interaction Die  |
| Major        | 15     | 2 Interaction Dice |
| Extreme      | 18+    | 4 Interaction Dice |

| **Tier** | **Die** |
|----------|---------|
| 1–4      | d4      |
| 5–10     | d6      |
| 11–16    | d8      |
| 17–20    | d10     |

**Limits:** one Source, one rider; do not re-damage the direct target; no immediate chains; one Hazard trigger per turn.

## **C3. Exploration Round**

1.  Orient.

2.  Choose tasks.

3.  Resolve.

4.  Mark time/resources.

5.  Apply pressure.

6.  Update.

**Torch:** six rounds. **Pressure:** Calm every 3 rounds; Alert every 2; Hostile every round. **Event die:** 1 encounter; 2 omen/clock; 3–6 quiet.

## **C4. Reaction and Morale**

**Reaction 2d6:** 2 hostile; 3–5 unfriendly; 6–8 uncertain; 9–11 favorable; 12+ helpful.

**Morale:** roll 2d6 at a decisive trigger. If result exceeds Morale Score, the group breaks. Check at most twice.

## **C5. GM Ruling Hierarchy**

1.  Specific exception.

2.  Named procedure.

3.  Close precedent.

4.  Standard D20 Test.

5.  Temporary ruling.

# **APPENDIX D. OPEN RULES ATTRIBUTION**

This work includes material adapted from the **System Reference Document 5.2.1 (“SRD 5.2.1”) by Wizards of the Coast LLC**, available at [<u>https://www.dndbeyond.com/srd</u>](https://www.dndbeyond.com/srd). The SRD 5.2.1 is licensed under the **Creative Commons Attribution 4.0 International License**, available at [<u>https://creativecommons.org/licenses/by/4.0/legalcode</u>](https://creativecommons.org/licenses/by/4.0/legalcode).

Hearth & Hazard v0.1 uses and adapts open game terms and mechanics from SRD 5.2.1. Changes include new procedures, terminology choices, examples, environmental interactions, exploration rules, morale, advancement options, and editorial reorganization. Product identity, trademarks, art, and non-open text from referenced games are not claimed.

Before public distribution, perform a dedicated licensing and trademark review and replace this provisional notice with any exact attribution language required by the final publication method.

# **CLOSING DESIGN STATEMENT**

Hearth & Hazard v0.1 proposes a conservative core and ambitious edges. It keeps the part of modern D&D that already lets groups sit down and play, then gives time, terrain, objects, monsters, motives, and consequences a shared language.

The strongest candidate for the system’s identity is not a new action economy or a larger list of modifiers. It is the combination of:

- information before commitment;

- procedures when pressure matters;

- one priced environmental consequence per cause;

- noncombat outcomes with mechanical teeth;

- visible modular grit; and

- templates that make later homebrew easier to author and adjudicate.

The next draft should cut as readily as it adds. Any rule that does not create a choice, clarify an expectation, or support a repeatable play loop should justify its page.
