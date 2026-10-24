# Horizon Walker Ranger — Comprehensive Research and Redesign

**Public Playtest 0.2 · October 15, 2026 · Designed for the 2024 Ranger**

**Recommendation:** Use independent planar offense with mandatory, Horizon Walker-only replacements for the Ranger’s Mark-dependent progression. Give the subclass dimensional movement at level 3, substantial investigation tools, and its familiar phasing, attack-linked teleportation, and spectral defense later.

This is a complete playable proposal supported by rules research and transparent damage modeling. It is not a claim of proven table balance. All new mechanics below are unofficial homebrew.

## 1. Scope, files, and research limits

The supplied request ends partway through its Planar Warrior subsection. This report applies the visible full-redesign objective to all original features; it does not presume additional missing requirements.

### File verification

I read the complete attached report and Playtest `(3)`, retrieved the specifically requested `(1)` and `(2)` files, and compared their bytes.

| File | Bytes | SHA-256 |
|---|---:|---|
| `Horizon_Walker_2024_Revised_Report.md` | 33,050 | `1fc63fad405aefedb31eb8d1e48a3bddf960e0e01977ef177235d62e148f1638` |
| `Horizon_Walker_2024_Revision_Playtest_0_1(1).md` | 33,149 | `fec79550857b4fd1612dc8b82bf8d249e6f09497924287f93ae484af1b07b998` |
| `Horizon_Walker_2024_Revision_Playtest_0_1(2).md` | 33,149 | Same as `(1)` |
| `Horizon_Walker_2024_Revision_Playtest_0_1(3).md` | 33,149 | Same as `(1)` |

**Finding:** All three Playtest copies are byte-for-byte identical. There are two distinct existing designs, not four.

### Authority and access

The current official Basic Rules supplied the Ranger, Hunter, spell, and glossary wording. Licensed Roll20 reproductions supplied the other 2024 subclasses. The two Wikidot references are unofficial transcriptions. The original subclass was checked against its transcription and the publisher’s original design interview; I do not claim access to the complete paid Xanathar’s chapter. [S1–S10, S14]

I checked the accessible official PHB and Xanathar’s errata pages and official errata index. Their retrieved contents supplied no Ranger or Horizon Walker amendment resolving this project’s Mark problem. The PHB page includes changes to conjuration spell upcasting, relevant to optimization. This is a bounded finding about the pages inspected, not certification that every later publication, forum answer, or digital change has been exhausted. In particular, the earlier draft’s claim about an October 7, 2026 update is not independently established here. [S11–S13]

Published official mechanics, licensed reproductions, publisher commentary, independent third-party designs, community feedback, and this report’s proposals are distinguished throughout. A third-party publisher’s own material is a primary source for that material, not official D&D rules.

## 2. Findings that drive the design

### What the original actually needs

The original’s extra damage, momentary phasing, attack-linked movement, and partial defensive disappearance give it an unusually coherent identity. The narrow portal finder and recurring damage activation undermine that identity’s delivery. Its signature repeatable teleportation also arrives very late. [S9, S14]

The original Planar Warrior and Hunter’s Mark can coexist across rounds. Their Bonus Actions compete when the mark is cast or transferred; Planar Warrior then demands the Bonus Action repeatedly. Claiming that both require fresh activation every round would overstate the conflict.

Nick can move the Light-property attack into the Attack action, but it does not free the Bonus Action from every other competing feature. Nature’s Veil, Misty Step, some feats, and certain spells remain relevant. Extra attacks amplify per-hit damage; a once-on-your-turn rider primarily becomes more reliable.

### Mark audit

| Level | Published dependency | Practical problem | Final treatment |
|---|---|---|---|
| 1 | Favored Enemy prepares Mark and grants free casts | Its resource is unattractive when choosing other Concentration spells | Keep preparation and casts; from Ranger 3, each unused free cast can instead fuel Folded Step |
| 13 | Relentless Hunter protects Mark from damage breaking Concentration | Other spells receive no corresponding progression benefit | Replace with resource-funded Relentless Focus for any spell prepared through Ranger features |
| 17 | Precise Hunter improves attacks against the marked target | Mark gains a major accuracy incentive | Replace with Advantage on the first weapon attack roll of each own turn, without a quarry |
| 20 | Foe Slayer improves Mark’s damage die | The capstone can be irrelevant to the chosen combat identity | Replace with Planar Mastery: stronger independent rider, with a Mark option retained |

These are subclass-specific exceptions. Other Rangers receive no changes. Before choosing this subclass at level 3, levels 1–2 use the published class normally. [S1, S2]

The 2024 Mark adds Force damage to successful attack rolls, requires Concentration, and spends Bonus Actions to cast and transfer. Higher slots extend duration rather than increasing the damage die. The revised transfer text does not require waiting until a subsequent turn. Its tracking benefit remains a reason to prepare it. [S3]

### Two existing designs: preserve, correct, replace

| Issue | Revised Report V1.0 | Playtest 0.1 | Decision for 0.2 |
|---|---|---|---|
| Independent damage | Useful 1d8/2d8 alternative | Same useful foundation | Preserve; do not permit automatic Mark stacking |
| Favored Enemy value | No alternate resource expenditure | Movement exchange begins at 7 | Begin limited teleportation exchange at 3 |
| Late progression | Parallel benefits retain published features | Replacements relegated to optional module | Make replacements part of the recommended version |
| Portal investigation | Broad categories; vague planar signatures and concealment | Better-defined traces and barriers | Retain precision; add dormant connections, sealed containers, and structured interpretation |
| Early movement identity | Mostly waits for 7/11 | Mostly waits for 7/11 | Limited Folded Step at 3 |
| Phasing | Invents a temporary plane with a free Fly Speed | Uses actual Etherealness and a teleport fallback | Use the existing spell; fund extra teleports, not repeated phasing from the same pool |
| Attack multiplication | Extra attack per Attack action | One extra attack and two teleports per turn | Retain turn limits; require genuine creature attacks |
| Damage conversion | “Weapon’s damage” leaves rider ambiguity | Explicitly excludes added features | Preserve the narrower conversion |
| Spell at 9 | Blink | Dispel Magic | Choose Blink; explain setup and defensive cost |
| Defense | Attacks only, then teleport | Any one damage event, then teleport | Keep broad trigger, one event, and Reaction cost |

The prior scorecards are design opinions, not evidence that a whole subclass is balanced. Neither a high mobility score nor a low personal DPR establishes appropriate total power.

V1.0’s no-critical longbow calculations are broadly reproducible under its stated assumptions. Playtest 0.1’s first-hit critical model is also reproducible: its level-11 no-Mark routine is approximately 21.31. Their different assumptions explain much of their numerical disagreement. Comparing the tables without accounting for criticals and late accuracy would be misleading.

V1.0’s exclusion checks the present Concentration state and earlier Mark damage but does not clearly forbid dealing the planar rider before casting Mark later that turn. Playtest 0.1 closes that order-of-operations gap. The new rules retain that protection.

The most important substantive shortcoming is admitted by Playtest 0.1 itself: its default leaves the late Mark pressure in place. That is incompatible with this request’s highest-priority goal. Adding concentration support or one advantaged attack alongside unchanged base features, as in V1.0, also risks accumulating benefits rather than making an explicit exchange.

## 3. Official and independent comparison

### Official reference envelope

| Comparator | Relevant evidence | Implication |
|---|---|---|
| Hunter 2024 | Consistent or spread weapon offense; Mark-linked information and later splash; strong reactive defense | Independent damage is not unprecedented, but full spell-backed Hunter damage is a meaningful comparator |
| Fey Wanderer 2024 | Per-target rider, broad noncombat specialty, optional Concentration-free Summon Fey, later party teleportation | Compare summon value and multi-target output, not just its small printed rider |
| Gloom Stalker 2024 | Conditional invisibility, initiative, limited damage/control bursts, reactive repositioning | Visibility and encounter conditions can matter more than a static DPR row |
| Beast Master 2024 | Companion action economy, two beast strikes later, Mark synergy, spell sharing | Count a second body, utility, and command costs; do not compare only the Ranger’s own attacks |
| Warrior of Shadow 2024 | Repeatable conditional teleportation at 6; paid unrestricted upgrade with an attack at 11 | Level-3 limited short movement is defensible; unrestricted free teleport-plus-attack at 3 would not be |

Sources: [S1, S5–S8]. These establish comparison mechanics, not a numerical “official balance score.” Hunter and Beast Master contain additional subclass-specific Mark links; those are not inherited by a Horizon Walker and require no replacement here.

Fey Wanderer’s summon is a genuine precedent for a narrowly defined Concentration exception, not permission for every Ranger damage spell to ignore Concentration. The 2025 official Conjurer playtest also demonstrates that broader damage-proof Concentration has been explored, but Unearthed Arcana is playtest material and cannot establish current final rules. [S5, S15]

### Third-party research and community disagreement

| Source/status | Design concept examined | What survives scrutiny |
|---|---|---|
| Kobold Press, *Planar Warden*; independent publisher article | Planar opposition knowledge, mixed ranged/melee tactics, slot-funded dimensional attacks | Broader expertise is useful. Additional ability modifiers to save DCs and old attack structures do not transfer safely to this chassis |
| laserllama, *Alternate Ranger / Planar Warden*; independent homebrew | Expanded awareness, earlier attack-linked steps, planar damage and multi-target strikes | Supports earlier identity and practical detection; depends on a different base class, so its numbers are not drop-in benchmarks |
| 11Sirus11, *Ranger Subclasses, Altered*; community homebrew | No recurring Planar Warrior activation; serial portal search; different defensive progression | Removing the activation tax is a recurring solution. Unrestricted full-damage stacking still needs a fresh 2024 budget |
| GM Binder revised Horizon Walker; community homebrew | Forced teleport on weapon hit and a travel-denial Reaction | Useful tactical ideas, but forced teleport can bypass positioning defenses and enable hazards; broad travel denial needs precise timing and counterplay |
| The Planar DM; independent campaign analysis | Planar expertise, environmental competence, an Outer Planes phasing workaround | Strong criticism of a planar specialist’s tools failing outside its home environment; universal hazard immunity would be too broad |
| 2025 r/onednd proposal and responses; anecdotal feedback | Mark-cast teleportation, small stacking rider, reactive attack | Good evidence of action congestion and delayed identity. It deliberately keeps Mark central, contrary to this brief |

Sources: [S16–S21]. These are primary sources for their own proposals, not evidence of official approval or controlled playtest results.

There is real disagreement. Some community authors reduce the rider to 1d4 so it can stack; others want to retain 1d8/2d8 and remove the Bonus Action. Some want boss damage instead of three-target attacks; others regard spreading attacks as essential identity. This report preserves the three-target specialty while using a larger non-stacking rider for boss fights. It does not pretend those preferences have been settled by popularity.

The original publisher interview explicitly discusses narrowing detection to avoid revealing every portal in a large area. That supports keeping the long-range search limited, while making close investigation more capable. Its warning concerns information scope, not a prohibition on useful exploration features. [S14]

## 4. Three distinct Mark solutions, plus the recommended hybrid

These are design candidates, not simultaneously usable rules.

### A. Transform the spell: Planar Pursuit

Candidate: when casting Mark, trade its per-hit damage for one 1d8 rider on each own turn and a 10-foot Bonus Action teleport while it lasts; that casting no longer requires Concentration and lasts 1 minute. At 13, improve pursuit through barriers; at 17 grant one advantaged weapon attack against its quarry; at 20 use 3d8. Rewrite each affected class feature for this form explicitly.

It can be made workable, but it is effectively an alternate spell plus a new late progression. It retains a cast/transfer routine and makes free casts the primary combat fuel. Calling it Mark also invites confusion about which original benefits survive. A more permissive concentration-free per-hit version is substantially riskier, especially on multiclass attack engines.

### B. Independent alternative, unchanged class

Candidate: retain the 0.1 independent 1d8/2d8 rider and movement exchange; leave Relentless Hunter, Precise Hunter, and Foe Slayer unchanged.

This is straightforward at levels 3–12 and leaves Mark competitive for many-attack builds. It fails the explicit late-progression requirement: choosing another spell still forfeits several advancing class features. It is a reasonable conversion for a different brief, not this one.

### C. Replace the Mark system entirely

Candidate: upon taking this subclass, remove Mark’s special preparation and free casts; gain a pool of planar exertions of the same size. Exertions buy steps, later concentration protection, and limited accuracy boosts. Replace all three late features. An independent once-turn rider supplies baseline offense.

This cleanly removes the dependency but unnecessarily deletes a tracking spell and a legitimate optional combat choice. It also requires more character-sheet changes and becomes a broader class rewrite.

### D. Recommended hybrid: independent offense and explicit replacements

Keep the spell available. Repurpose its free-cast resource without needing to cast it. Replace the three late Mark features rather than granting parallel benefits. No target designation is needed for planar offense or precision.

| Criterion | A: transformed spell | B: independent only | C: full replacement | D: recommended hybrid |
|---|---|---|---|---|
| Damage consistency | Good while form active | Good early; late Mark pressure | Good if pool isn’t mandatory for damage | Rider always available; Mark rewards more hits |
| Concentration | Alternative form frees it | Free with rider, but late opportunity cost rises | Fully independent | Fully independent progression |
| Bonus Actions | Cast/transfer and optional steps | Rider free | Depends on exertion | Rider free; movement optional |
| Free casts and slots | Casts remain combat activations | Alternative fuel only partially fixes progression | New pool; larger sheet change | Existing pool funds movement or protection |
| 13/17/20 | Needs bespoke transformations | Leaves central problem | Complete redesign | Explicit complete treatment |
| Multiclassing | Spell/form export risk | Modest rider dip | Pool scaling must be fenced | Ranger-level scaling, weapon-only rider |
| Class compatibility | Many spell-specific exceptions | Highest drop-in compatibility | Most invasive | Three named replacements; rest preserved |
| Ease at table | Two versions of one spell | Easiest | New subsystem | One resource, one rider, three clear exchanges |
| Theme | Strong pursuit | Strong planar combat | Strong planar identity | Investigation, combat, and travel together |
| Main exploit risk | Unintended Mark inheritance | Late stacking patches | Exertion damage multiplication | Short-rest movement and aura delivery |

**Why D wins:** it directly meets the prioritized goal with fewer changes than replacing the whole class. It builds on successful prior work but changes its architecture: early resource-funded movement, integrated late progression, limited phasing fuel, and broader evidence-based investigation are core rules rather than optional repairs.

## 5. Complete player-facing rules

Everything in this section is the recommended version. The class-feature replacements are mandatory parts of this homebrew, not optional bonuses. Use the published 2024 Ranger for everything else.

### Horizon Walker

*Read the Boundaries Between Worlds*

Horizon Walkers follow paths that ordinary travelers cannot see. They recognize doors whose hinges open onto another sky, traces left by vanished travelers, and places where the world folds around an unseen space. Their training turns that knowledge into precise strikes and impossible movement.

| Ranger level | Features and improvements |
|---|---|
| 3 | Horizon Walker Spells, Planar Resonance, Planar Warrior, Folded Step |
| 7 | Ethereal Step; Folded Step improves |
| 11 | Distant Strike; Planar Warrior improves |
| 13 | Relentless Focus replaces Relentless Hunter; Planar Resonance improves |
| 15 | Spectral Defense |
| 17 | Dimensional Precision replaces Precise Hunter |
| 20 | Planar Mastery replaces Foe Slayer |

#### Level 3: Horizon Walker Spells

At each Ranger level in the table, you thereafter always have the listed spell prepared. It counts as a Ranger spell for you and doesn’t count against the number of spells you can prepare with Ranger Spellcasting. Use the 2024 spell versions and their normal component requirements.

| Ranger level | Spell |
|---|---|
| 3 | Protection from Evil and Good |
| 5 | Misty Step |
| 9 | Blink |
| 13 | Banishment |
| 17 | Teleportation Circle |

#### Level 3: Planar Resonance

You gain the following benefits.

**Planar Lore.** You gain proficiency in Arcana. If you already have that proficiency, gain proficiency in Investigation or Religion instead. When you make an Arcana check about planes, their inhabitants or hazards, teleportation, or extradimensional spaces, you can use Wisdom instead of Intelligence.

**Boundary Warning.** While you don’t have the Incapacitated condition, you magically sense the presence of an open planar portal, an open entrance to an extradimensional space, or an ongoing overlap between planes within 30 feet. You learn only that at least one is present. When teleportation or planar travel occurs, you also sense the event if its arrival or departure point is within that range on your current plane. For an event, you learn its general direction and whether it was teleportation or travel between planes; you learn no creature’s space or identity.

**Read the Seams.** You can spend 1 uninterrupted minute examining your surroundings, remaining within 5 feet of the space where you began and taking the Magic action on each of your turns. If you take a different action or become Incapacitated, you must restart. At the end, you learn the location and category of the nearest detectable phenomenon within 60 feet in each of these categories:

1. A planar portal, whether open or dormant, that still has a magical connection to another plane.
2. An entrance to an extradimensional space, including a closed container or sealed entrance whose extradimensional space still exists.
3. An ongoing overlap between planes, or a localized magical effect that specifically prevents teleportation or planar travel.
4. A trace left by teleportation or planar travel within the last 10 minutes.

If multiple phenomena in a category are equally near, the DM chooses which you detect. You can exclude phenomena whose locations you already know when you begin an examination. An overlap covering your location is detected at your location; this doesn’t map its extent.

This feature creates travel traces solely for your Planar Resonance. A trace remains at the event’s location, is neither an object nor a spell effect, and disappears after 10 minutes. You learn whether the detected trace involved arrival, departure, or both, and whether its latest event occurred within the last minute or earlier. Repeated events at a point merge into one trace and reveal no number of travelers. An event creates a trace only on a plane where an arrival or departure occurred.

An ordinary ruin of a destroyed portal, a mundane door once used as a portal, a creature’s origin or type, and an instantaneous summoning with no qualifying transportation are not detectable phenomena. A doorway or object qualifies only while an actual magical planar connection or extradimensional space remains.

You can use Read the Seams any number of times. It requires no Concentration.

**Interpret the Evidence.** After locating a phenomenon, you can examine it from within 10 feet for 1 minute, taking the Study action on each of your turns. At the end, you automatically distinguish a portal, extradimensional entrance, overlap, travel barrier, or travel trace. You also learn whether a portal is open or dormant. Then make a DC 15 Arcana check. On a success, ask the DM one of these questions:

- What plane, or broad family of planes, does this evidence identify?
- What visible or magically discernible hazard would a traveler face by interacting with it?
- Does its discernible magical structure appear stable, failing, or deliberately obstructed?

The DM answers only to the extent that the phenomenon contains such evidence; “the evidence doesn’t establish that” is a valid answer. No result reveals a traveler’s identity, exact destination, hidden portal key, password, or complete activation procedure. You can attempt this check on a particular phenomenon only once per Long Rest, unless materially new evidence appears. Other characters can investigate normally.

**Distant Threshold.** As a Magic action, locate the nearest open or dormant planar portal within 1 mile on your current plane that still has a magical connection to another plane. You learn its direction and approximate distance, rounded to the nearest 100 feet. Extradimensional containers and travel traces don’t qualify. Once you use this benefit, you can’t use it again until you finish a Short or Long Rest, whether or not it finds a portal.

**Sensing Limits.** These senses reach only your current plane and don’t grant sight, reveal creatures, detect magic generally, or permit targeting a space you cannot otherwise see. A phenomenon’s connection can be detected where it touches your plane; its far side is not examined.

Boundary Warning and Read the Seams are blocked by 1 foot of stone, 1 inch of ordinary metal, a thin sheet of lead, or 3 feet of wood or dirt. Distant Threshold ignores ordinary barriers, but an intervening lead barrier blocks it. The examination for Interpret the Evidence requires an unobstructed path to the phenomenon or its trace, but not sight of an invisible phenomenon.

All magical sensing from this feature is suppressed by Antimagic at your location or the phenomenon’s location. For purposes of Nondetection and effects expressly warding against Divination spells, treat this sensing as a Divination spell. A protected phenomenon is undetectable; a protected traveler creates no trace detectable by this feature while protected. These are specific homebrew interactions. Nystul’s Magic Aura alone doesn’t conceal spatial connections or travel traces, since this feature doesn’t read magical auras or creature types. Illusions don’t erase real phenomena, and detecting a phenomenon doesn’t dispel or expose an illusion.

**Experienced Investigator.** At Ranger level 13, the local range of Read the Seams increases to 120 feet. For you, travel traces persist for 1 hour instead of 10 minutes, and you can detect them throughout that duration. Their age categories become within the last minute, 1–10 minutes, or more than 10 minutes. Boundary Warning, barrier limits, and Distant Threshold are unchanged.

#### Level 3: Planar Warrior

Once on each of your turns, when you hit a creature with an attack roll using a weapon, you can change the weapon’s Bludgeoning, Piercing, and Slashing damage from that hit to Force damage. This changes the weapon’s damage dice and modifiers added to that weapon damage, but not extra damage from another spell or feature.

The hit can also deal an extra 1d8 Force damage. You can deal this extra damage only if you haven’t concentrated on your own Hunter’s Mark or dealt its extra damage at any time during the current turn. After dealing this extra damage, you can’t cast Hunter’s Mark or begin concentrating on it until the turn ends.

The extra Force damage becomes 2d8 at Ranger level 11. The feature requires no action beyond the attack, no Concentration, and no expendable resource. Its only range limit is the attack’s normal range.

#### Level 3: Folded Step

As a Bonus Action, expend one unused casting of Hunter’s Mark that your Favored Enemy feature grants without a spell slot. You magically teleport up to 15 feet to an unoccupied space you can see. This expenditure casts no spell and doesn’t expend a spell slot.

At Ranger level 7, the teleport distance becomes 30 feet.

This feature doesn’t change Favored Enemy’s preparation or recovery rules. Its free castings remain one shared resource: using a casting for this feature makes it unavailable for casting Hunter’s Mark or any other feature that spends that casting.

#### Level 7: Ethereal Step

As a Bonus Action, choose one of the following effects:

- **Ethereal Passage.** Cast Etherealness on yourself without a spell slot or components. For this casting, the spell ends at the end of the current turn, and you can end it earlier on that turn without an action. All its other rules apply, including its planar restrictions and occupied-space return rules.
- **Folded Passage.** Magically teleport up to 30 feet to an unoccupied space you can see. This option isn’t a spell.

Once you use either option, you can’t use Ethereal Step again until you finish a Short or Long Rest. You can still use Folded Step by spending Favored Enemy castings; doing so grants teleportation, not additional Ethereal Passage castings.

#### Level 11: Distant Strike

Once on each of your turns, when you take the Attack action, you can apply these benefits to that action:

**Spatial Assault.** Immediately before each of up to two weapon attacks against creatures made as part of the action, you can magically teleport up to 10 feet to an unoccupied space you can see. After teleporting, you must make that attack against a creature you can legally attack from the destination.

**Forked Assault.** Immediately after you make weapon attacks against two different creatures as part of the action, you can make one additional weapon attack as part of that action. It must target a third creature you haven’t attacked during that action. The triggering attacks need not hit.

You can gain only one additional attack and two Spatial Assault teleports from this feature per turn, regardless of how many Attack actions or attacks you make.

#### Level 13: Relentless Focus

*Replaces Relentless Hunter for this subclass.*

When you fail a Constitution saving throw to maintain Concentration on a spell prepared through a Ranger feature, you can expend one unused spell-slot-free casting from Favored Enemy to succeed instead. You do so before that failed save ends your Concentration, and no action is required.

This feature doesn’t prevent Concentration ending for any reason other than that failed save. You no longer gain Relentless Hunter’s published benefit, including when you cast Hunter’s Mark.

#### Level 15: Spectral Defense

When you take damage, you can take a Reaction to gain Resistance to all damage in that single triggering instance. Apply the Resistance before resolving the damage or a resulting Concentration saving throw. Immediately after that damage is resolved, you can magically teleport up to 10 feet to an unoccupied space you can see.

The Resistance doesn’t protect against later attacks or later damage from the same ongoing effect. The teleport occurs after the triggering damage and doesn’t prevent that damage or cancel associated effects.

#### Level 17: Dimensional Precision

*Replaces Precise Hunter for this subclass.*

You have Advantage on the first attack roll you make using a weapon on each of your turns. This benefit requires no action, designated target, Concentration, or resource expenditure. You no longer gain Precise Hunter’s published benefit.

#### Level 20: Planar Mastery

*Replaces Foe Slayer for this subclass.*

Your Planar Warrior’s extra Force damage becomes 3d8. When you cast Hunter’s Mark, its extra damage die is a d10 instead of a d6. Planar Warrior’s restriction on combining its extra damage with your Hunter’s Mark still applies.

#### Shared teleportation rules

Teleports granted by this subclass transport only you and the objects you wear or carry; they don’t transport another creature. They expend no movement and can function with a Speed of 0, unless an effect specifically prevents teleportation. They require an unoccupied destination you can see, except that Ethereal Passage follows its spell’s distinct rules.

All magical features are subject to Antimagic and applicable travel restrictions. Teleportation doesn’t cross intervening spaces; effects at the destination still apply according to their wording. These features don’t create portals that other creatures can use.

## 6. Why these feature choices work

### Spell selection

| Spell | Role and cost | Decision |
|---|---|---|
| Protection from Evil and Good | Situational defense and planar identity; normal Concentration and material requirements | Keep; having a useful Concentration spell is desirable once Mark is optional |
| Misty Step | Slot-funded movement before level 7; still useful when free resources run out | Keep despite overlap; Folded Step consumes a separate finite resource |
| Blink | Defensive planar disappearance without ongoing Concentration; action setup and uncertain availability | Replace Haste; avoids making another offensive self-buff the default |
| Banishment | Thematic control that competes for a valuable slot and Concentration | Keep; use current creature-type and full-duration removal rules |
| Teleportation Circle | Party logistics and connections between settlements | Keep normal casting time, components, and known-circle restrictions |

Blink’s defensive opportunity cost is real: spending an action can be poor in a short fight, and disappearing removes opportunities to interact with the original plane between turns. Its current wording should not be silently replaced with the older spell. It is an option, not assumed free precombat protection. [S22]

Dispel Magic was a defensible 0.1 choice, especially for an investigator. It is already on the Ranger list, so making it always prepared increases flexibility rather than granting a new capability. Blink adds more distinctive access. Haste remains available only if gained through another permitted source; this report does not grant all three alternatives. [S1]

No free Plane Shift, universal portal opening, automatic permanent banishment, or party-wide environmental immunity is added. Finding a connection and having the power to use or remove it remain distinct abilities.

### Planar Warrior

The rider is one useful strike per own turn, not one per target and not once on every creature’s turn. It doesn’t grow with character level in a three-level dip. The Force conversion is narrower than the original: Sneak Attack, poison, smites, and spell riders keep their own damage rules.

The first hit can still be a critical hit, doubling the rider dice normally. A player may wait for a later hit, but the modeled default uses the first hit; waiting risks losing the rider completely.

Automatic damage is intentionally the baseline, so the player isn’t asked to reactivate an alternate quarry every fight. Meaningful choices occur in spell selection, resource spending, position, and target distribution. Removing compulsory maintenance is part of the objective; inventing a differently named compulsory maintenance loop would miss it.

### Movement and defense

Level-3 movement spends the same scarce resource as a free Mark and has only 15-foot reach. Level 7 improves that option and supplies rest-based phasing. The resource pool cannot buy repeated wall-passing. This matters in a dungeon where three or four ethereal scouts could otherwise replace an entire infiltration challenge.

Distant Strike deliberately doesn’t grant an unconditional third boss attack. It still gives movement against one enemy, and the rider doubles at 11. Additional attacks improve reliability, but do not generate unlimited teleports. This preserves the original multi-opponent identity without making Nick, Haste, and Action Surge movement multipliers.

Spectral Defense uses Resistance rather than a separate halving operation. Two sources of Resistance do not multiply into quarter damage. This tracks the original designer’s explicit explanation of the feature’s balance. [S14]

## 7. Quantitative balance review

### Model and limits

I used exhaustive enumeration of miss, ordinary hit, and critical hit sequences, rather than treating the rider as an automatic hit. Accuracy is stipulated after Fighting Style and other accuracy adjustments.

Main assumptions: pure Ranger; one d8 weapon attack at 3 and two at 5+; attack modifier +3 at 3, +4 at 5–7, +5 at 11+; 65% total hit probability including a 5% critical chance; no feats, magic items, resistance, cover, external Advantage, setup actions, or damage from other Concentration spells. “First-hit” means the rider is spent on the first successful hit. Hunter’s Colossus Slayer is assumed eligible on every modeled hit, which favors its ceiling on wounded targets.

With Advantage, hit probability becomes `1 − (1 − p)²` and critical probability becomes `1 − 0.95²`. For `n` identical ordinary attacks, an on-first-hit rider with mean `R` contributes:

`R × [1 − (1 − p)^n] × (1 + c/p)`

Per-hit Mark contributes `n × M × (p + c)`. A base attack contributes `p × (weapon mean + modifier) + c × weapon mean`. Non-identical accuracy, including level-17 precision, is evaluated attack by attack. Values are rounded after calculation.

### One durable target: attacking-round DPR

| Ranger level | 0.2 without Mark | 0.2 with Mark instead | Published Hunter + Mark + Colossus Slayer |
|---|---:|---:|---:|
| 3 | 8.25 | 7.55 | 10.70 |
| 5 | 15.75 | 16.40 | 20.65 |
| 7 | 15.75 | 16.40 | 20.65 |
| 11 | 21.31 | 17.70 | 21.95 |
| 13 | 21.31 | 17.70 | 21.95 |
| 15 | 21.31 | 17.70 | 21.95 |
| 17 | 24.72 | 21.04 | 29.30 |
| 20 | 29.50 | 24.39 | 33.20 |

The 0.2 Mark column receives only this revision’s first-attack Advantage at 17+, not published Precise Hunter. The Hunter column receives published Advantage on all attacks against its quarry and its normal capstone at 20. Hunter’s level-11 splash is excluded because this table has one enemy.

**Interpretation:** the revision has a substantial early personal-damage deficit against a fully funded Hunter, then closes much of the gap without spending Concentration. It is not a claim of equal full-package output. A spell supporting the independent routine can materially change the outcome, as can a Hunter’s other resource choices.

### Attack-count and accuracy sensitivity at Ranger 11

These are generic d8 weapon attack sequences with a +5 modifier, not complete legal build sheets for every row. The three-attack case can represent an available third target; four attacks require a suitable build or added action.

| Hit probability | Attacks | Planar routine | Mark routine without another subclass rider |
|---|---:|---:|---:|
| 50% | 2 | 17.38 | 13.80 |
| 50% | 3 | 23.59 | 20.70 |
| 50% | 4 | 29.18 | 27.60 |
| 65% | 2 | 21.31 | 17.70 |
| 65% | 3 | 28.48 | 26.55 |
| 65% | 4 | 35.15 | 35.40 |
| 80% | 2 | 24.83 | 21.60 |
| 80% | 3 | 32.96 | 32.40 |
| 80% | 4 | 40.85 | 43.20 |

At ordinary accuracy, the level-11 planar rider itself contributes about 8.51 with two attacks and 9.55 with four; Mark contributes 4.90 and 9.80 respectively. Additional accurate attacks favor Mark. That keeps a genuine optional offensive use for it without making later class features exclusive to it.

At level 3, one attack gives a d8 rider contribution of 3.15 versus Mark’s 2.45. A two-attack Light/Nick routine instead gives 4.25 versus 4.90. The low-level result therefore changes with equipment; it isn’t accurate to call either damage mode universally superior.

### Legal many-attack stress case

A level-17 Ranger using a d6 Light weapon, a Nick partner, Two-Weapon Fighting, and Dexterity 20 can make three qualifying attacks without spending its Bonus Action. With no Vex benefit or other Advantage assumed, 0.2’s no-Mark routine is about 29.02, rising to 33.93 at 20. A published Hunter with the same simplified three-attack routine, Mark and an eligible Colossus Slayer reaches about 38.63 and 44.48 respectively.

This intentionally isolates a large late deficit in the no-spell weapon routine. It does not include the independent Ranger’s additional Concentration effect. Dual Wielder, Vex, advantage from allies, or a fourth attack need a separate build-specific calculation. No old −5/+10 feat damage is imported into the 2024 rules.

### Concentration and action opportunity costs

A level-11 independent routine averages 21.31 during an attacking round. If it spends the first action of a three-round fight casting a control spell, its remaining two attacking rounds contribute about 42.61 weapon damage. A Mark routine making attacks in all three rounds contributes 53.10 before another subclass’s benefits. The control spell must justify that approximately 10.49-damage difference through damage, denied actions, positioning, protection, or party benefit. Independence does not make spell setup free.

A first-turn Summon Beast, Entangle, or Spike Growth therefore has different value in a short fight and a long one. A Bonus Action teleport can also displace a Dual Wielder attack. Record actual actions spent, not just the most favorable recurring turn.

At level 13, suppose a character’s ordinary Concentration-save success chance is 70%. Surviving three independent checks without help is 34.3%. Advantage would raise that to about 75.4%, but this design instead spends a limited shared resource on failed saves. It can protect a particularly important failure, even a very hard save, but each expenditure removes one step or free Mark casting. Five available uses are not five free spells and five teleports and five protections.

### Defense and whole-package comparison

Against one 30-damage event, Spectral Defense prevents 15 damage. Against three separate 10-damage hits, it prevents 5 from only one hit. A Hunter can outperform it against repeated same-type damage on the triggering turn; Gloom Stalker can sometimes avoid follow-up melee attacks through a longer teleport. The new feature remains useful against a breath weapon or damaging hazard. [S1, S6]

At level 11, Fey Wanderer’s one-target weapon routine with Mark and its d6 rider is approximately 21.01 in the bow model, before its summon. Its Concentration-free summon is a significant omission from that number. Gloom Stalker’s three Wisdom-based burst uses should be budgeted over the actual day rather than assumed on every turn. Beast Master must include beast accuracy, charge conditions, survival, and command choices. None can honestly be ranked by this report’s bow table alone. [S5–S7]

**Provisional verdict:** suitable for controlled playtesting within the official subclass range; conservative on unfunded single-target damage, strong in movement and investigation. The most plausible excess is repeated mobility combined with powerful area spells, not its isolated once-turn damage rider. The most plausible weakness is an early-level campaign where planar investigation rarely matters and no other Concentration spell pays back its setup.

## 8. Resources, exploits, and rules interactions

| Interaction | Ruling or risk in this revision |
|---|---|
| Favored Enemy pool | 2/3/4/5/6 castings at Ranger levels 1/5/9/13/17; all alternate expenditures share it |
| Short Rests | Restore Ethereal Step and Distant Threshold; do not restore spent Favored Enemy castings |
| Six fights, two rests, Ranger 7 | Up to three free Ethereal Step activations plus three pooled Folded Steps if no pool use is spent on Mark; only three can phase |
| Ranger 3 / Rogue | One own-turn d8 rider may combine with Sneak Attack; no extra planar rider on an off-turn Sneak Attack; only two pool-funded 15-foot steps per day |
| Ranger 3 / Fighter or Monk | More attacks improve rider reliability, not its dice or frequency; other abilities keep their own action costs |
| Full caster multiclass | Relentless Focus arrives only after 13 Ranger levels and protects spells prepared through Ranger features; it is not a three-level universal Concentration upgrade |
| Action Surge | At most one Forked Assault and two Spatial Assault teleports on the turn; no second planar rider |
| Haste | The extra limited action doesn’t independently earn a free third-target attack; the turn cap still applies |
| Nick and Dual Wielder | Can add attacks when their own requirements are met; they don’t reset subclass frequency limits |
| Vex and other Advantage | Advantage doesn’t stack. Dimensional Precision can be redundant for a supported build, which is part of its budget |
| Shillelagh | A weapon attack still qualifies. Unarmed Strikes and spell attack rolls not using a weapon don’t qualify |
| Weapon cantrips | A qualifying weapon attack can receive the rider. Distant Strike requires the Attack action, so casting a weapon cantrip with the Magic action does not enable it |
| Summons and companions | They don’t inherit the Ranger’s rider or precision. Mark’s published damage applies only as its own wording permits |
| Crusher/Piercer/Slasher | Converting the weapon damage may remove a required damage-type trigger; conversion is optional |
| Grappled or Restrained | A visible legal teleport can escape physical restraint when the governing effect allows; it doesn’t dispel persistent conditions that still apply |
| Repeated weapon swaps | Do not generate more planar riders, precision benefits, or Spatial Assault uses |
| Repeated rests | Can replenish limited phasing; encounters and time pressure still matter. Do not assume a day has a fixed rest count |
| Ally or harmless-creature attacks | Could facilitate attack-linked movement. No teleport requires hostility, but the per-turn distance cap prevents runaway travel. Don’t base a balancing claim on the DM forbidding all such behavior |
| Mark sequencing | No planar rider after dropping Mark during that turn, and no rider-then-Mark cast during the same turn. Mark can be cast on a later turn |
| Antimagic and barriers | Detection and magical movement are suppressed as written. A sense never supplies the sight required for a teleport |
| Spectral Defense and self-damage | Can trigger if a real damage event occurs, costing damage and a Reaction. It creates no attack or resource refund |

### Highest-priority combination: damaging Emanations

The current Conjure Woodland Beings can damage creatures when its Emanation enters their spaces, with a once-per-turn limit. That is not once per round. A mobile Ranger can deliver the area to different targets or potentially trigger damage on another creature’s turn by changing position then. [S23]

Distant Strike does not multiply a creature’s permitted saves during one turn. Spectral Defense can, however, reposition the Ranger on another turn, potentially delivering an additional Emanation exposure if that spell’s wording and the table’s teleport/entry interpretation permit it. This is a meaningful high-level synergy, also relevant to other mobile subclasses. A 10-foot Emanation dealing 5d8 averages 22.5 before saves; one extra eligible exposure could contribute 16.88 expected damage if the target fails half its saves and takes half on success.

That conditional example is not added to every DPR row. It requires a level-4 slot, an active spell, appropriate enemies, geometry, an available Reaction, a damage trigger, and an eligible new turn. It is the main playtest risk. If it makes the subclass dominate mixed encounters, first remove Spectral Defense’s teleport or restrict it to the Ranger’s own turn; do not immediately nerf the baseline rider. That would be a subsequent revision, not an unstated rule in 0.2.

No claim is made here that all published teleport/Emanation edge cases have one universally settled interpretation. Record the table’s ruling before testing and apply it equally to comparison subclasses.

## 9. Planar-investigation adjudication examples

These examples apply the homebrew rules, not a claim that official magic normally leaves these traces.

| Situation | What the Ranger can learn | What remains unresolved |
|---|---|---|
| Ordinary locked door | Nothing supernatural from this feature | Lock, trap, room contents |
| Dormant gate with an extant planar connection | Local examination locates it; distant search can find it | Activation key and exact destination |
| Destroyed gate whose magic is gone | No automatic detection | Mundane or Arcana-based historical investigation |
| Closed Bag of Holding | Local examination locates the container’s entrance as extradimensional | Contents, capacity used, owner, safe access |
| Open Rope Trick entrance | Passive nearby warning; local examination can locate the entrance | Occupants and contents of the space |
| Misty Step used six minutes ago | A location and older-than-one-minute departure/arrival trace if in range | Traveler identity and the paired endpoint |
| Teleport used forty minutes ago | No trace at low levels; detectable locally at Ranger 13 | Exact time, source spell, destination |
| Fiend standing in a tavern | No detection based on creature type or birthplace | Normal observation and knowledge checks can help |
| Persistent planar overlap | Warning or local identification if in range and not blocked | Full boundaries and every environmental consequence |
| Teleportation barrier | Local examination identifies a qualifying barrier effect’s presence and location | Spell identity, full extent, how to dispel it |
| Lead-lined portal chamber | Detection blocked where the lead intervenes | Ordinary investigation and access remain possible |
| Nondetection-protected traveler | No detectable travel trace from that protected event | Physical footprints and witness testimony remain available |
| Nystul’s Magic Aura on a container | Spatial examination can still find its actual entrance | Its misleading aura still affects aura-reading magic normally |
| Antimagic | No functioning magical sensing inside or into the suppressed area | Investigation can resume after suppression ends |

The knowledge benefit remains usable for recalling information while magical senses are suppressed; a trained skill is not itself a magical sensor.

The broader sense should create leads in thefts, disappearances, strange containers, warded rooms, haunted thresholds, and magical ruins. It cannot guarantee frequent use in an adventure with no such phenomena. Its Arcana proficiency and broad planar knowledge provide some value even then; the feature still needs honest campaign expectations.

## 10. Playtest plan and revision criteria

Run the complete integrated version first. Testing the old subclass-only design would not test this request’s main goal.

| Test | Levels/builds | Record |
|---|---|---|
| Boss fight, three rounds and six rounds | 3, 5, 11, 17, 20; bow and Nick | Priority-target damage, setup turns, chosen Concentration spell, pool spent |
| One/two/three/five targets | 11+; melee and ranged | Extra attacks actually earned, damage spread, useful teleports |
| Two-fight day versus six-fight day | 7, 13, 17; zero and two rests | Movement, phasing, free Mark, concentration protection competing for resources |
| Mixed damage defenses | 15; heavy hit, Multiattack, breath, ongoing damage | Damage prevented, follow-up attacks escaped, Reaction competition |
| Emanation stress test | 13 and 15; Conjure Woodland Beings | Enemy exposures per round, extra exposures from reaction teleports, target count |
| Supported optimization | 17+; Vex, ally Advantage, Dual Wielder | Value lost to redundant Advantage; spell-backed total output |
| Multiclass dip | Ranger 3/Rogue and Ranger 3/Fighter | Rider frequency, character-versus-class scaling, resource endurance |
| Investigation scene | Gate, sealed container, trace, ward, mundane decoy | Clues gained, mystery questions left open, adjudication time |
| Non-Ethereal plane | 7+ | Teleport fallback usefulness; phasing correctly unavailable |
| Barrier and concealment scene | Lead, stone, Nondetection, aura masking, Antimagic | Whether different tables reach the same result from the text |

### Acceptance criteria

- At levels 13, 17, and 20, the player can identify a relevant advancing class benefit without casting Mark.
- Choosing Mark is sometimes worthwhile for many-hit or tracking situations, but declining it does not disable multiple class features.
- The level-3 character can demonstrate dimensional movement during real play without waiting eight more levels.
- Planar investigation yields actionable evidence while leaving at least one meaningful investigative step in the scene.
- The subclass’s full spell-backed package does not consistently dominate official comparators in both focused and multi-target combat under the same resources and geometry.
- Pool expenditures create decisions; they are not treated as separately refreshing pools.

As a practical review trigger, investigate a sustained full-package advantage exceeding roughly 15% over several official comparators in matched scenarios. That is a project triage threshold, not an official balance law. Also investigate persistent 15% deficits when the subclass’s mobility and exploration specialty provide little compensation.

If level 3–7 feels weak, examine spell use, useful steps, and encounter duration before adding damage. If broader sensing solves mysteries outright, narrow automatic information rather than removing the entire investigator role. If late protection feels too cheap, measure failed saves and remaining pool first. If the capstone feels small, remember that its independent rider adds 4.5 nominal damage per use while leaving Concentration open; compare it to real level-20 builds, not an isolated die.

## 11. Change summary

This revision keeps the recognizable Horizon Walker and changes how its identity is delivered. It provides early limited teleportation, a close-range investigative specialty with bounded information, a reliable non-Mark damage routine, normal brief ethereal scouting with a fallback, capped attack-linked repositioning, and one-event spectral protection.

The decisive architectural change is the integrated late progression. The final design does not ask a player to accept three Mark-only class rewards and then choose whether to ignore them. Instead, concentration protection, precision, and the capstone support the character’s planar identity directly.

The strongest uncertainty is the value of mobility beside powerful 2024 area spells. The weakest environment remains an early campaign with little spatial magic and short encounters that favor immediate weapon damage. Those are concrete playtest questions; neither is resolved by calling the design “balanced.”

## 12. Sources and evidence register

Links below were accessed or searched on October 15, 2026. Repeated licensed entries are grouped by their underlying page, not counted as independent corroboration. Mechanical summaries are deliberately brief; consult the actual sources for complete official rules.

### Official rules and licensed reproductions

- **[S1] Official 2024 classes, including Ranger and Hunter:** https://www.dndbeyond.com/sources/dnd/br-2024/character-classes — primary rules checked for class progression and Hunter comparisons.
- **[S2] Licensed 2024 Ranger:** https://roll20.net/compendium/dnd5e/Classes:Ranger?expansion=32231 — second presentation of the same published class, not an independent balance framework.
- **[S3] Official 2024 Hunter’s Mark:** https://www.dndbeyond.com/spells/2619166-hunters-mark — spell page; complete wording also checked in the official spell chapter below.
- **[S4] Official spell descriptions:** https://www.dndbeyond.com/sources/dnd/br-2024/spell-descriptions — checked Mark, Etherealness, Banishment, concealment, and Ranger-relevant spells.
- **[S5] Licensed 2024 Fey Wanderer:** https://roll20.net/compendium/dnd5e/Subclasses:Fey%20Wanderer?expansion=32231 — per-target rider, summon exception, and mobility comparison.
- **[S6] Licensed 2024 Gloom Stalker:** https://roll20.net/compendium/dnd5e/Subclasses:Gloom%20Stalker?expansion=32231 — limited burst, visibility, and defensive teleport comparison.
- **[S7] Licensed 2024 Beast Master:** https://roll20.net/compendium/dnd5e/Subclasses:Beast%20Master?expansion=32231 — command costs, companion scaling, Mark interaction, and spell sharing.
- **[S8] Licensed 2024 Warrior of Shadow:** https://roll20.net/compendium/dnd5e/Subclasses:Warrior%20of%20Shadow?expansion=32231 — conditional teleportation and level-11 upgrade.
- **[S9] Original Horizon Walker, unofficial transcription:** https://dnd5e.wikidot.com/ranger:horizon-walker — exact original feature structure; lower authority than the paid published book.
- **[S10] Supplied 2024 Ranger transcription:** https://dnd2024.wikidot.com/ranger:main — cross-check only, not preferred over official wording.
- **[S11] Official PHB errata:** https://www.dndbeyond.com/sources/dnd/sae/players-handbook — inspected; no Ranger section found in retrieved content.
- **[S12] Official Xanathar’s errata:** https://www.dndbeyond.com/sources/dnd/sae/xanathars-guide-to-everything — inspected; no Horizon Walker amendment found in retrieved content.
- **[S13] Official errata index:** https://www.dndbeyond.com/sources/dnd/sae — access route for current corrections; not proof that every conceivable clarification was searched.
- **[S14] Publisher interview, original Horizon Walker design:** https://www.dndbeyond.com/posts/70-new-horizon-walker-in-xanathars-guide-to — original rationale for limited distant detection, exploration, and Resistance wording.
- **[S15] Official 2025 Arcane Subclasses Unearthed Arcana:** https://media.dndbeyond.com/compendium-images/ua/arcane-subclasses-update/LEwFmioFBYHWqzpd/UA2025-ArcaneSubclassesUpdate.pdf — surfaced Focused Conjuration as a design comparison only; not treated as finalized rules or evidence about a later final Conjurer.
- **[S22] Official 2024 Blink:** https://www.dndbeyond.com/spells/2618939-blink — current non-Concentration planar defense; distinguishes it from legacy wording.
- **[S23] Official 2024 Conjure Woodland Beings:** https://www.dndbeyond.com/spells/2619051-conjure-woodland-beings — Emanation and once-per-turn optimization risk.
- **[S24] Official rules glossary:** https://www.dndbeyond.com/sources/dnd/br-2024/rules-glossary — action, condition, Concentration, teleportation, and general interaction reference.

### Independent designs and feedback

- **[S16] Kobold Press, Planar Warden:** https://koboldpress.com/planar-warden-an-archetype/ — independent third-party publisher material from the older rules environment, not a licensed official D&D subclass.
- **[S17] laserllama, Alternate Ranger:** https://www.gmbinder.com/share/-M7iu19Af89SH2G_5RGa — creator-authored alternative class and Planar Warden; a different chassis.
- **[S18] 11Sirus11, Ranger Subclasses, Altered:** https://www.gmbinder.com/share/-NEyPxD0_bX2w39NsJaS — community design; no-activation planar rider and alternate progression.
- **[S19] Revised Horizon Walker on GM Binder:** https://www.gmbinder.com/share/-NP9XMLQ66AvqcqQSqxQ/-NP9Xt8t__b7Z9kV5_3M — community forced-teleport and travel-denial concepts.
- **[S20] The Planar DM, True Planewalker revision:** https://theplanardm.com/class-makeover-transforming-the-horizon-walker-xanathars-guide-into-a-true-planewalker/ — campaign-focused critique and planar utility proposals.
- **[S21] Community 2024 proposal and discussion:** https://www.reddit.com/r/onednd/comments/1pufj2y/saw_someone_on_here_making_a_hombrew_update_for/ — author’s Mark-linked teleport proposal and conflicting reader feedback; anecdotal evidence only.

An additional Reddit revision at https://www.reddit.com/r/UnearthedArcana/comments/1inwj8a was surfaced by search, but opening it returned an error. Its excerpt was not used to establish detailed mechanics. No inaccessible paid third-party text is represented as fully reviewed.

### Original work in this report

The recommended rules, design trade-offs, resource analysis, damage calculations, risk judgments, adjudication examples, and playtest criteria are this report’s proposals or calculations. They should not be attributed to the official sources or to the independent authors listed above.
