# Horizon Walker Ranger — 2024 Revision
## Public Playtest 0.1 • October 15, 2026

**Recommendation:** Build the subclass around independent planar damage, practical dimensional investigation, and controlled spatial movement. Keep Hunter’s Mark available, but stop requiring it for the subclass to function.

This is a complete playtest design, not a claim of established balance. The main version changes only the subclass. An optional module separately addresses the base Ranger’s later Hunter’s Mark features.

## Part I — Research findings and original subclass assessment

### Rules and source status

I checked the 2024 Ranger against D&D Beyond’s official Basic Rules, its publisher overview, and the supplied reproduction. The official errata index lists the Player’s Handbook as updated October 7, 2026. The accessible errata contains no Ranger-specific replacement for the Hunter’s Mark progression. Xanathar’s accessible errata likewise contains no Horizon Walker revision.

The original subclass’s publisher chapter redirected to a purchase page. Its mechanics were checked using the supplied Wikidot reproduction; that is an unofficial transcription, not independent access to the printed book. Licensed Roll20 reproductions supplied the relevant Fey Wanderer and Gloom Stalker rules. Community discussions and homebrew posts informed problem identification, not rules authority.

The subclass’s foundation remains attractive: planar investigation, Force damage, brief phasing, repeated short teleports, and reactive defense. The problems concern when those benefits arrive, how often they matter, and what the character must surrender to use them.

### Hunter’s Mark’s actual demands

| Ranger level | Published dependency | Consequence |
|---|---|---|
| 1 | Favored Enemy prepares Hunter’s Mark and provides free casts | Saves slots, but retains the spell’s other costs |
| 13 | Relentless Hunter protects its Concentration from damage | Does not permit a second Concentration effect |
| 17 | Precise Hunter grants Advantage against its marked creature | Makes abandoning the spell substantially more expensive |
| 20 | Foe Slayer changes its damage die to d10 | The capstone benefits that spell specifically |

Favored Enemy supplies 2/3/4/5/6 free casts per Long Rest at Ranger levels 1/5/9/13/17. These are Ranger-level breakpoints, not general Proficiency Bonus scaling.

The revised spell costs a Bonus Action, requires Concentration, and adds Force damage to each successful attack roll against its target. Moving it after that target reaches 0 Hit Points also costs a Bonus Action. Importantly, the revised text does not retain the old restriction to moving it on a subsequent turn.

Free casting therefore solves only part of the resource problem. Casting another Concentration spell ends the mark. Before level 13, incoming damage can also end it; afterward, Incapacitation and switching Concentration still can.

### Original feature assessment

| Feature | Intended experience and useful strength | Main problem | Treatment |
|---|---|---|---|
| Horizon Walker Magic | Otherworldly protection and travel | Haste adds setup, Concentration risk, and another self-buff incentive | Preserve four spells; replace Haste |
| Detect Portal | Find routes between worlds | Too dependent on the adventure containing a suitable portal | Replace with Planar Resonance |
| Planar Warrior | A decisive Force-infused weapon hit | Recurring Bonus Action, short designation range, wasted setup after misses | Remove setup; create a non-stacking alternative to the mark |
| Ethereal Step | Briefly bypass physical boundaries | Brief availability; poor function on some planes | Preserve phasing; add teleportation option and alternative fuel |
| Distant Strike | Blink between scattered opponents | Late identity; damage depends on three targets | Preserve spread attack; bound teleport multiplication |
| Spectral Defense | Partially evade a damaging blow | Attack-only protection misses many high-level threats | Broaden trigger; retain one-instance limit |

The original mark and Planar Warrior can coexist across rounds; they do not both consume a Bonus Action every round. The conflict appears on casting and transfer turns, while Planar Warrior itself demands that action repeatedly. That distinction matters when comparing sustained output with the first two rounds of a fight.

Nick improves the situation for some two-weapon builds by relocating the Light-property attack into the Attack action. It does not remove competition with every Bonus Action attack, Misty Step, Nature’s Veil, or reactive offensive spells.

Community criticism repeatedly identifies this congestion and the delayed arrival of the subclass’s signature movement. These are useful reports of player experience, not proof that every Horizon Walker build performs poorly. A 2025 community revision added teleportation to Hunter’s Mark; I reject that direction here because it deepens the dependency the project aims to reduce.

The official comparison also argues against excessive caution: Fey Wanderer receives independent damage and later a Concentration-free summon option; Gloom Stalker supplies strong situational visibility benefits and late reactive teleportation. A revised Horizon Walker can possess meaningful utility and movement without spending every feature on damage.

## Part II — Major design decisions

### Independent damage, with an explicit trade-off

Planar Warrior supplies 1d8 extra Force damage once on your own turn, increasing to 2d8 at Ranger level 11. It has no activation action, designated quarry, resource cost, or Concentration requirement. Its extra damage is unavailable on a turn during which you concentrate on your own Hunter’s Mark.

This makes an actual alternative: use planar damage alongside Entangle, Spike Growth, protection, a summon, or no spell. Alternatively, use Hunter’s Mark when repeated hits, later Advantage, or extended tracking justify it.

The restriction applies to the whole turn. A character cannot take planar damage, then cast Hunter’s Mark later that turn and receive both benefits. Force conversion remains available in either mode.

I rejected unrestricted stacking because removing Planar Warrior’s recurring cost while retaining its original damage and adding the mark produces a large automatic package. I also rejected concentration-free, per-hit Hunter’s Mark: that exports a powerful damage engine into multiclass builds and compounds other Concentration effects.

A smaller die that stacks would be easy to balance, but would do less to change the player’s decision. Rebranding the spell as a planar quarry would change the presentation more than the underlying dependency.

### Give free casts a different job

From level 7, unused Favored Enemy casts can fuel Ethereal Step. Spending one this way casts no Hunter’s Mark. This is an added subclass permission, not a claim that the published class already allows that exchange.

Consequently, a character who favors other spells still gets something useful from the level-1 resource. The exchange buys movement or phasing, not additional attacks.

There remains a deliberate limit: the main design does not redirect Relentless Hunter, Precise Hunter, or Foe Slayer. The full class still encourages the mark late in play. Adding unrestricted late Advantage and damage protection while leaving Concentration free would exceed the intended scope of this subclass’s budget. Part VI provides an explicit replacement module for groups that want to remove that remaining pressure.

### Awareness that supplies evidence

Planar Resonance combines short-range warning, deliberate local investigation, distant portal searching, and Wisdom-based planar knowledge.

Its detectable subjects are enumerated. A creature’s type or birthplace alone does not qualify. “Extraplanar” is not a general condition in the rules, and a Fiend is not automatically a walking breach.

Recent teleportation residue is an expressly created homebrew effect. It gives investigators a location and a rough time window, not a destination or identity. This supports a wizard’s disappearance, a disturbed shrine, or an unusual container without functioning as unrestricted Detect Magic, See Invisibility, or Scrying.

Automatic detection of a destination plane, spell identity, activation password, or creature origin was rejected. Those answers should require knowledge, investigation, or stronger magic.

### Preserve movement without multiplying everything

Ethereal Step retains its memorable brief phasing. Its teleport option prevents the feature from becoming unusable merely because a campaign visits a plane without a Border Ethereal.

Distant Strike retains attacks across three opponents. Two short teleports per turn are enough to establish its identity while avoiding runaway increases from Nick, Haste, and Action Surge. Its single-target improvement comes from Planar Warrior’s die increase; it does not receive an unconditional third attack. The official Shadow Monk’s level-11 teleport-and-attack upgrade is another useful tier benchmark; this design instead allows shorter movement without a Bonus Action.

Spectral Defense protects against one damage event and provides a short escape. It offers more reliable mitigation than an accuracy penalty, but less ongoing protection than the Hunter’s same-type resistance and less repositioning than Gloom Stalker’s 30-foot defense.

## Part III — Complete revised Horizon Walker

*Guard the Thresholds of the Multiverse*

Horizon Walkers read the places where reality wears thin. A misplaced echo, a door whose shadow falls inward, or footprints ending on bare stone can reveal a passage that others overlook. These Rangers study the dangers beyond familiar skies and follow intruders through the seams of the world.

Their weapons carry planar force, and their movements briefly abandon ordinary distance.

| Ranger Level | Features |
|---|---|
| 3 | Horizon Walker Spells, Planar Resonance, Planar Warrior |
| 7 | Ethereal Step |
| 11 | Distant Strike, Planar Warrior improvement |
| 15 | Spectral Defense |

### Level 3: Horizon Walker Spells

Your planar studies ensure you always have certain spells ready. When you reach a Ranger level specified in the Horizon Walker Spells table, you thereafter always have the listed spell prepared. The spells count as Ranger spells for you, and they don't count against the number of spells you can prepare.

**Horizon Walker Spells**

| Ranger Level | Spell |
|---|---|
| 3 | *Protection from Evil and Good* |
| 5 | *Misty Step* |
| 9 | *Dispel Magic* |
| 13 | *Banishment* |
| 17 | *Teleportation Circle* |

### Level 3: Planar Resonance

Your training attunes you to disturbances in the boundaries between planes. You gain the benefits below. The feature's magical detection functions only on your current plane, including at points where something arrives from or departs to another plane.

**Planar Lore.** You gain proficiency in Arcana. If you already have that proficiency, you instead gain proficiency in Investigation or Religion (your choice).

When you make an Intelligence (Arcana) check to recall information about planes, planar travel, teleportation, or a creature's connection to a plane, you can make the check using Wisdom instead of Intelligence.

**Boundary Warning.** While you don't have the Incapacitated condition, you magically sense the following within 30 feet of yourself:

- An open portal connecting different planes.
- An open entrance to an extradimensional space.
- An occurrence of teleportation or travel between planes.

When you sense an opening, you learn only that at least one such opening is within range. When you sense teleportation or planar travel, you learn the direction of the event and which kind of travel occurred. You sense an arrival and a departure separately if each occurs within range.

This sense requires no action. It doesn't reveal a creature's identity or space, grant sight, or warn you when an opening leaves your range. Total Cover blocks the sense.

**Read the Seams.** You can spend 1 minute examining your surroundings. During this time, you must remain in the same space and take the Magic action on each of your turns. If you take another action or gain the Incapacitated condition, the examination ends without effect, and you must start over.

At the end of the minute, you magically learn the location and category of each of the following within 60 feet of yourself:

- An open portal between planes or an open entrance to an extradimensional space.
- An ongoing magical effect that specifically prevents teleportation or planar travel.
- An ongoing overlap with another plane specified by a location's description or a magical effect.
- A point where teleportation or travel between planes occurred within the past 10 minutes.

The last category appears as a trace at the location of the event. For each trace, you learn whether it marks an arrival, a departure, or both, and whether its most recent event occurred within the past minute or earlier. Multiple events at the same point create only one detectable trace. A trace doesn't move with a creature or object and disappears 10 minutes after the event. Traces exist only for the purposes of this feature; they aren't objects or spell effects.

This examination doesn't reveal the identity or number of travelers, any destination or plane of origin, the name of a spell, a portal's key or operating instructions, or a creature merely because of its type or origin. It can't detect closed or dormant portals or sealed entrances to extradimensional spaces.

The examination can penetrate barriers, but it is blocked by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt. You can perform the examination any number of times, and it requires no Concentration.

**Distant Threshold.** You can spend 1 minute searching for an open portal that connects your current plane to another plane. During this time, you must remain in the same space and take the Magic action on each of your turns. At the end of the minute, you learn the direction and distance (rounded to the nearest 100 feet) of the nearest qualifying portal within 1 mile of yourself, if one exists.

Nonmagical barriers don't block this search, but entrances to extradimensional spaces don't qualify. The search requires no Concentration. If you take another action or gain the Incapacitated condition before the minute ends, the search ends without effect, and you must start over.

Once you complete this search, you can't use it again until you finish a Short or Long Rest, even if you found no portal. An interrupted search doesn't expend its use.

**Concealment.** Antimagic suppresses the magical detection granted by this feature. A source protected by *Nondetection* can't be detected by it. *Nystul's Magic Aura* can conceal an object-based source if it causes the object to appear nonmagical. A traveler protected by either applicable concealment effect leaves no trace detectable by this feature while protected.

Other effects that expressly prevent magical detection also apply. An ordinary illusion doesn't erase a qualifying phenomenon, but sensing that phenomenon doesn't reveal the illusion or let you see through it.

### Level 3: Planar Warrior

Once on each of your turns, when you hit a creature with an attack using a weapon, you can channel planar energy through the attack, gaining the following benefits:

- You can change any Bludgeoning, Piercing, or Slashing damage dealt by the weapon itself to Force damage. This includes the weapon's damage dice and any modifiers added to that damage, but not extra damage from a spell or another feature.
- The attack deals an extra 1d8 Force damage if you haven't concentrated on your own *Hunter's Mark* spell at any time during the current turn. If you deal this extra damage, you can't cast *Hunter's Mark* or begin concentrating on it until the turn ends.

The extra Force damage increases to 2d8 when you reach Ranger level 11.

### Level 7: Ethereal Step

As a Bonus Action, you can choose one of the following effects:

**Ethereal Passage.** You cast *Etherealness* without expending a spell slot or providing spell components. For this casting, the spell affects only you and ends at the end of the current turn. You can end it earlier (no action required). All other restrictions of the spell apply, including its limitations on which planes it functions on and its rules for returning to an occupied space.

**Folded Distance.** You magically teleport up to 30 feet to an unoccupied space you can see. This effect isn't a spell.

Neither effect transports another creature.

Once you use this feature, you can't use it again until you finish a Short or Long Rest. You can use it again before then by expending one of your remaining uses of Favored Enemy that would otherwise let you cast *Hunter's Mark* without a spell slot. Spending a use in this way doesn't cast the spell.

### Level 11: Distant Strike

Once on each of your turns, when you take the Attack action, you can gain the following benefits during that action:

**Dimensional Movement.** Immediately before each of up to two attacks you make using a weapon as part of the action, you can magically teleport up to 10 feet to an unoccupied space you can see.

**Forked Assault.** Immediately after you've made attacks using weapons against two different creatures as part of the action, you can make one additional attack using a weapon as part of that action. You must target a third creature that you haven't attacked during the action, and the attack must meet the weapon's normal requirements. The qualifying attacks don't need to hit.

You can make only one additional attack with this feature per turn. Taking another Attack action on the same turn doesn't grant additional uses of either benefit.

These teleports transport only you and don't expend any of your movement. You can use them while your Speed is 0 unless an effect specifically prevents teleportation. You must still be able to see the destination.

### Level 15: Spectral Defense

When you take damage, you can take a Reaction to give yourself Resistance to all damage dealt by the triggering attack or effect in that instance. Apply the Resistance before resolving the damage, including any saving throw to maintain Concentration.

Immediately after the damage is resolved, you can magically teleport up to 10 feet to an unoccupied space you can see. This teleport transports only you.

The Resistance doesn't apply to later attacks or other instances of damage, even if they come from the same creature or ongoing effect. The teleport occurs after the triggering damage and doesn't prevent that damage or any associated effects.

## Part IV — Balance and compatibility review

### Comparative scores

These are provisional judgments of the complete package across levels 3–20. A 3 is an appropriate official baseline; 4 indicates a strong specialty, not proof of superior overall balance. Scores aren’t added into a purported mathematical balance rating.

| Category | Revised Horizon Walker | Hunter | Fey Wanderer | Gloom Stalker |
|---|---:|---:|---:|---:|
| Combat effectiveness | 3 | 3 | 3 | 3 |
| Action economy | 4 | 3 | 3 | 4 |
| Resource management | 4 | 3 | 3 | 3 |
| Mobility | 4 | 2 | 4 | 3 |
| Exploration | 4 | 2 | 3 | 3 |
| Defense | 3 | 4 | 3 | 4 |
| Thematic identity | 4 | 3 | 4 | 4 |
| Scaling | 3 | 3 | 3 | 3 |
| Usability | 3 | 4 | 3 | 4 |
| Campaign versatility | 3 | 4 | 4 | 3 |

The main costs behind these scores are the non-stacking damage modes, remaining late mark incentives, three-target requirement, limited phasing, and DM work required by supernatural investigation. Its high mobility doesn’t equal unrestricted flight, long-range teleportation, or party transportation.

### Transparent damage model

Assumptions: pure Ranger; one d8 weapon attack at level 3 and two thereafter; Dexterity 16/18/20 at levels 3/7/11+; 65% total hit chance, including 5% critical chance; no magic items, offensive feats, external Advantage, or damage resistances. The accuracy is stipulated after any Fighting Style benefit, so this isn’t a comparison of styles. The mark column applies Precise Hunter from level 17.

Planar damage is used on the first hit. These are attacking-round estimates, not full-day estimates including spell setup.

| Level | Revised, no mark | Revised, mark instead | Concentration available for another spell in no-mark mode? |
|---|---:|---:|---|
| 3 | 8.25 | 7.55 | Yes |
| 7 | 15.75 | 16.40 | Yes |
| 11 | 21.31 | 17.70 | Yes |
| 15 | 21.31 | 17.70 | Yes |
| 17 | 21.31 | 24.38 | Yes |
| 20 | 21.31 | 28.28 | Yes |

At level 11, three available opponents increase no-mark total damage to approximately **28.48**, spread among three targets. That isn’t 28.48 damage focused on a boss.

For the same level-11 two-attack model, a Hunter using the mark and Colossus Slayer deals about **21.95** to an already-wounded target. Fey Wanderer with its mark and Dreadful Strikes deals about **21.01**, before Fey Reinforcements. The latter omission is substantial: the summon adds another combatant, damage, and tactical value. These figures compare a weapon routine, not the subclasses’ full ceilings.

Gloom Stalker instead mixes conditional visibility advantages with limited bursts and control. At Wisdom 16, its three level-11 Dreadful Strikes supply 27 nominal bonus damage before criticals, plus their secondary effects. Spreading those uses across 18 attacking rounds differs greatly from spending them across 8.

At 50%/65%/80% accuracy, the level-11 planar rider contributes about **7.43/8.51/9.18** damage with two attacks; the mark contributes **3.85/4.90/5.95**, before later Advantage. More attacks favor the mark: four ordinary-accuracy hits attempted per turn yield about **9.55** planar-rider damage versus **9.80** mark damage.

A first-hit rider’s expectation is its average damage multiplied by the probability of at least one hit, plus the chance that the selected first hit is critical. Critical dice are included; assuming every rider automatically lands would overstate its value.

### Progression, defenses, and practical limits

Level 3 gains reliable identity and investigation but no free teleport. Level 7 adds phasing and an alternative use for Favored Enemy; one Short Rest gives two ordinary Ethereal Step uses, before any exchanged casts. Level 11 supplies its major combat escalation. Level 15 broadens survival without creating an extra attack.

A 30-damage event becomes 15 before rounding interactions elsewhere. Spectral Defense can help one Concentration save; it doesn’t protect against a whole Multiattack. Gloom Stalker may evade subsequent melee attacks by moving farther, while Hunter may resist repeated same-type damage on the current turn.

At level 13, choosing another spell still forfeits Relentless Hunter. At 17 and 20 the damage table shows the remaining pressure clearly. Other Concentration spells can justify the difference, but a claim that the subclass completely repairs those base features would be false.

Nature’s Veil remains a useful competing Bonus Action; Feral Senses doesn’t duplicate planar investigation. Roving supports movement between teleports. Extra attacks improve rider reliability rather than multiplying its frequency.

Teleportation is not movement through intervening spaces. Nevertheless, landing in or entering a hazardous area can trigger that effect according to its own wording. Repeated forced-movement and aura combinations require individual review.

Finally, no detection feature guarantees adventure relevance. In a campaign without spatial magic or planar clues, the subclass still has combat and movement benefits, but its exploration specialty will be quieter.

## Part V — Design rationale and change log

| Change | Main motivation | Result and cost |
|---|---|---|
| Always-prepared subclass spells | 2024 compatibility | Uses current preparation conventions |
| Haste → Dispel Magic | Original design and broader role | Gains investigation follow-through; loses a strong speed/self-buff option |
| Retain Protection from Evil and Good | Thematic identity | Relevant protection; still Concentration and normal component costs |
| Retain Misty Step | Recognizable mobility | Useful before Distant Strike and for a longer jump; still costs a slot normally |
| Retain Banishment | Planar hunter identity | Real control option; requires Concentration and successful spell use |
| Retain Teleportation Circle | Exploration identity | Logistics, not unrestricted travel; needs known destinations and normal components |
| Detect Portal → Planar Resonance | Original utility limitation | Broader clues; no automatic destinations or creature identification |
| Remove Planar Warrior setup | Both editions’ action economy | Useful from turn one; cannot stack its rider with the mark |
| Restrict Force conversion | Rules clarity and balance | Converts weapon damage, not every added effect |
| Add Folded Distance | Campaign versatility | Ethereal Step works on any plane; doesn’t bypass anti-teleportation |
| Exchange Favored Enemy casts | 2024 resource design | Unused casts become movement; no slot conversion or refund |
| Preserve third-target attack | Recognizable Horizon Walker | Strong spread damage; maintains a focus-fire weakness |
| Cap attack-action teleports | 2024 attack multiplication | Nick and Action Surge don’t create additional short teleports |
| Broaden Spectral Defense | High-level threat coverage | Handles saves and hazards; protects only one event |

Dispel Magic doesn’t automatically close every natural portal, erase a location’s planar nature, or end a nonspell feature. Identifying a disturbance and having authority to remove it remain separate questions.

Teleportation Circle’s 1-minute casting requires Concentration while casting under the general spellcasting rules, even though its completed effect isn’t maintained with Concentration. Ethereal Step’s free spellcasting follows the 2024 one-spell-slot-per-turn rule, not the former blanket restriction tied to Bonus Action spells.

Banishment also needs its revised rules: it isn’t a guaranteed permanent dismissal of every creature described as extraplanar. Its return and permanent-removal conditions follow the 2024 spell.

The strongest retained features are brief ethereal passage, Force-infused attacks, three-target spatial assault, and reactive partial phasing. The revision changes their delivery while preserving their recognizable purposes.

## Part VI — Optional alternative and playtesting recommendations

### Optional house-rule module: independent high-level Ranger

Use this only if the group wants to remove the remaining late-class incentives to cast Hunter’s Mark. It replaces three base-class features for this Horizon Walker. It is excluded from the preceding calculations and scores.

The following features replace the named base Ranger features for a Horizon Walker. They are optional and aren't part of the subclass's standard progression.

**Level 13: Relentless Focus (Replaces Relentless Hunter).** When you fail a Constitution saving throw to maintain Concentration on a Ranger spell, you can expend one of your remaining uses of Favored Enemy that would otherwise let you cast *Hunter's Mark* without a spell slot to succeed on the saving throw instead (no action required). You must do so before your Concentration ends as a result of the failed save. This feature doesn't prevent your Concentration from ending for any other reason.

**Level 17: Spatial Precision (Replaces Precise Hunter).** At the start of each of your turns, you can choose one creature you can see within 90 feet of yourself (no action required). You have Advantage on the first attack roll you make against that creature before the end of that turn.

**Level 20: Planar Mastery (Replaces Foe Slayer).** The extra Force damage of your Planar Warrior increases to 3d8. Alternatively, when you use *Hunter's Mark*, the spell's damage die is a d10 instead of a d6. The restriction on dealing Planar Warrior's extra damage while concentrating on *Hunter's Mark* still applies.

The exchange has genuine costs: level 13 spends a shared resource instead of granting unlimited damage-proof mark Concentration, and level 17 improves one attack instead of every attack against the quarry. The capstone retains two distinct damage modes. In the same two-attack model, the optional no-mark routine is approximately 24.72 at level 17 and 29.50 at level 20.

I recommend testing the subclass-only version first unless the table has already decided to replace the Ranger’s mark-dependent progression. This keeps subclass balance and base-class reform separately measurable.

### Focused playtests

1. **Levels 3 and 7, three-round fights:** Compare a bow, sword-and-shield, and Nick build. Record first-turn usefulness, unused Bonus Actions, and occasions when switching modes was worthwhile.
2. **Long and short adventuring days:** Run six three-round fights with two Short Rests, then two four-round fights with none. Track mark casts exchanged for movement and whether phasing becomes too plentiful.
3. **Level 11 target layouts:** Test one boss, two widely separated enemies, and three clustered enemies. Record damage to the priority target separately from total damage.
4. **Attack multiplication:** Test Nick, Dual Wielder, Haste, and Action Surge. Verify one planar rider, at most two Distant Strike teleports, and one additional third-target attack per turn.
5. **Planar investigation:** Test a concealed portal, dormant portal, closed Bag of Holding, Rope Trick entrance, recent Misty Step, and Nondetection-protected traveler. Give the DM the exact list in advance; record ambiguity and adjudication time.
6. **Boundary escape:** Test a grapple, opaque wall, barred opening, anti-teleportation area, occupied ethereal return, and a plane without a Border Ethereal. A sensed location never counts as seeing a teleport destination.
7. **Level 15 defense:** Test one heavy hit, repeated attacks, mixed damage types, a breath weapon, and ongoing damage. Check Reaction timing and Concentration saves.
8. **Levels 17–20:** Compare the published progression and optional module separately. Record how often another Concentration spell justifies abandoning the mark and whether that choice feels satisfying.

Also check a Ranger 3/Rogue build: its own-turn rider can combine with Sneak Attack, but not add another planar rider on an Opportunity Attack. Summoned allies don’t inherit your Planar Warrior. Self-inflicted damage can enable Spectral Defense’s small teleport at level 15, but costs damage and a Reaction; it produces neither attacks nor resource recovery.

**Readiness:** Complete enough for campaign playtesting. The main uncertainties are level-3 mark-free performance beside fully funded official subclasses, repeated ethereal scouting, planar-sense adjudication, and the late-level appeal of choosing other Concentration spells. Those deserve table evidence before a public “balanced” release.

## Sources and verification notes

Rules sources were accessed October 15, 2026. Publisher pages and licensed reproductions establish mechanics; the community sources illustrate opinions or proposed changes.

- Official Ranger and Hunter: https://www.dndbeyond.com/sources/dnd/br-2024/character-classes
- Publisher Ranger overview: https://www.dndbeyond.com/posts/1759-2024-ranger-vs-2014-ranger-whats-new
- Official current Hunter’s Mark: https://www.dndbeyond.com/spells/2619166-hunters-mark
- Official glossary: https://www.dndbeyond.com/sources/dnd/br-2024/rules-glossary
- Official spell descriptions: https://www.dndbeyond.com/sources/dnd/br-2024/spell-descriptions
- Official Etherealness: https://www.dndbeyond.com/spells/2619193-etherealness
- Official errata index: https://www.dndbeyond.com/sources/dnd/sae
- Current PHB errata: https://www.dndbeyond.com/sources/dnd/sae/players-handbook
- Xanathar’s errata: https://www.dndbeyond.com/sources/dnd/sae/xanathars-guide-to-everything
- Original Horizon Walker, unofficial transcription: https://dnd5e.wikidot.com/ranger:horizon-walker
- Supplied 2024 Ranger transcription: https://dnd2024.wikidot.com/ranger:main
- Licensed Fey Wanderer rules: https://roll20.net/compendium/dnd5e/Subclasses:Fey%20Wanderer?expansion=32231
- Licensed Gloom Stalker rules: https://roll20.net/compendium/dnd5e/Subclasses:Gloom%20Stalker?expansion=32231
- Official Monk mobility comparison: https://www.dndbeyond.com/posts/1758-2024-monk-vs-2014-monk-whats-new
- Community discussion of 2024 Horizon Walker: https://www.reddit.com/r/3d6/comments/1qslzy2/2024_and_horizonwalker/
- Community homebrew and responses: https://www.reddit.com/r/onednd/comments/1pufj2y/saw_someone_on_here_making_a_hombrew_update_for/

No claim is made that these accessible sources constitute an exhaustive search of every published clarification or homebrew revision.
