# Veteran Fighter Follow-Up: Quantifying Opportunity Attacks, the d10 Damage Rider, Spot the Shooter, and Size Up

## Executive assessment

After rechecking the 2024 rules, current optimization discussion, and the actual arithmetic, I think **some of the cautions in the earlier analysis were too conservative—especially where they implicitly carried over 2014 assumptions about Polearm Master/Sentinel and treated “Opportunity Attack interaction” as inherently dangerous.**

The more useful conclusion is narrower:

> **Opportunity Attacks are not intrinsically a dangerous design space for the Veteran. Reliable extra reactions are dangerous; reliably generated off-turn attacks can be strong; and attaching premium control to every Opportunity Attack can be strong. Merely improving an ordinary Opportunity Attack is usually quite manageable.**

The 2024 rules impose a hard brake: after taking a Reaction, a creature cannot take another until the start of its next turn. A normal Opportunity Attack also has a fairly restrictive trigger: a visible creature must leave your reach using its action, Bonus Action, Reaction, or one of its speeds. citeturn18view2turn18view3 Optimizer analysis has long pointed out that even Sentinel-style melee control is limited by this one-Reaction bottleneck. citeturn17view7turn15search20

More importantly, **the notorious 2014 Polearm Master + Sentinel interaction has been substantially dismantled in 2024**. Polearm Master's Reactive Strike is now its own Reaction melee attack rather than an Opportunity Attack, so Sentinel's Opportunity-Attack-specific Halt does not apply to it under the prevailing RAW reading. Current 2024 optimization discussions explicitly call this out. citeturn13search6turn13search5turn15search6 Likewise, the 2024 Great Weapon Master damage rider is tied to attacks made as part of the Attack action on your turn, rather than inflating off-turn Opportunity Attacks as the old -5/+10 feat could. citeturn15search1turn15search13

I would therefore revise the earlier risk assessment approximately as follows:

| Mechanic | Earlier concern level | Revised concern level | Why |
|---|---:|---:|---|
| Small rider on a normal Opportunity Attack | Moderate | **Low** | One Reaction, conditional trigger |
| Move an OA target 5 feet | Moderate | **Low–moderate** | Fighter already gets Push; direction matters more than distance |
| +1d10 on an OA | Moderate | **Low** | About 3.85 expected damage per *triggered* OA at 65% accuracy |
| Generate a reaction attack when an enemy attacks an ally | High | **Moderate** | Potentially frequent, but still one Reaction; Sentinel already establishes precedent |
| Call that generated attack an **Opportunity Attack** | High | **Moderate** | The OA tag activates Sentinel and other OA-specific rules |
| Speed 0 on every OA | High | **Moderate–high** | Damage isn't the issue; denying movement can deny an enemy's intended turn |
| Extra unrestricted Reaction | Very high | **Very high** | Removes the principal safety valve |
| +1d10 once per Attack action instead of once per turn | High | **Low–moderate** | Identical in ordinary turns; mainly buffs Action Surge and Haste |
| Reaction Search to “Spot the Shooter” | Worth considering | **Usually too weak** | Standard Hide already ends when the shooter attacks |
| Current Size Up | Possibly risky information extraction | **Mechanically safe; probably underpowered** | Full action + Intelligence check + qualitative answer + once/creature/day is too many gates |

The most important distinction is between **damage power** and **tempo/control power**. An extra 5–9 expected weapon damage is visible and easy to calculate, but stopping a melee monster 10 feet away from its intended target may be far more valuable. Conversely, a highly flavorful information feature can be effectively worthless if it costs three or four Fighter attacks to use.

That distinction should guide the next Veteran draft.

## Opportunity Attacks are less dangerous in 2024 than the old optimization reputation suggests

### The actual 2024 constraint is severe

A normal 2024 Opportunity Attack requires a creature you can see to leave your reach using an action, Bonus Action, Reaction, or one of its speeds. You then spend your Reaction to make **one melee weapon attack or Unarmed Strike**, and that attack occurs before the creature leaves. Once you use a Reaction, you get no further Reaction until the start of your next turn. citeturn18view2turn18view3

That means a Veteran who has an excellent Opportunity Attack does **not** automatically become a mass-lockdown character.

Against four enemies, you can normally punish one of them.

Against one enemy that never leaves your reach, ordinary OA improvements can do nothing.

Against teleportation or movement that doesn't satisfy the Opportunity Attack trigger, ordinary OA improvements can do nothing under the glossary's trigger language. citeturn18view3

Against an enemy that Disengages, ordinary Opportunity Attacks are normally avoided unless another feature specifically creates an exception.

This matches optimizer criticism of 5e "tanking": even Sentinel could only stop one creature because the Reaction system itself was the limiting resource. citeturn17view7turn15search7

So the right balance question is not:

> “Does this interact with Opportunity Attacks?”

It is:

> **“How often does this cause the Reaction attack to happen, what rider comes with the hit, and does anything bypass the one-Reaction ceiling?”**

Those are dramatically different questions.

### The old Polearm Master/Sentinel alarm bell is substantially obsolete

This is an especially important correction.

The 2014 optimization ecosystem made Opportunity Attacks notorious because Polearm Master could cause a creature entering a polearm's reach to provoke an Opportunity Attack, which could then combine with Sentinel's speed-zero effect. Tabletop Builds' old optimization material correctly treated that combination as powerful under the 2014 rules. citeturn15search2turn15search11

The 2024 Polearm Master instead has **Reactive Strike**, which lets the character spend a Reaction to make a melee attack against a creature entering the relevant weapon's reach. The wording no longer calls that attack an Opportunity Attack. citeturn13search6turn17view6 Current 2024 rules discussions consequently conclude that Sentinel's Halt does not attach to Reactive Strike, and current optimization discussion identifies the loss of PAM/Sentinel synergy as a real weakening of the old combo. citeturn13search5turn15search6

This matters enormously for the Veteran.

A drill written:

> **When you hit with an Opportunity Attack...**

does **not**, under that reading, enhance Polearm Master's Reactive Strike.

A drill written:

> **When you hit with an attack you make as a Reaction...**

**does** include Polearm Master.

That means terminology itself gives you a very useful balance dial.

**Recommendation:** where a Veteran feature is truly about punishing withdrawal, make it OA-specific. Where the Veteran gains a retaliation against a missed attack, an attack against an ally, and so forth, call it simply a **Reaction to make one melee attack**, not an Opportunity Attack. That avoids accidental Sentinel interoperability without inventing any new subsystem.

### Reach is useful, but not the old impenetrable ten-foot bubble

Reach weapons still matter. A glaive, halberd, pike, and lance have Reach, and the game's official guidance applies the weapon's longer reach when determining where its Opportunity Attack occurs. A creature moving from adjacent to 10 feet from a halberd user therefore does not trigger the normal OA merely by crossing the 5-foot boundary; it must actually leave that weapon's reach. citeturn21view0turn13search21

That also weakens some imagined “Veteran with polearm locks the battlefield” scenarios.

### What is an ordinary OA actually worth in damage?

Take a simple tier-two-or-higher Fighter with Strength 20 and a 65% overall hit rate, including a 5% critical-hit chance.

For a **1d10 + 5** polearm attack without a miss-damage mastery:

\[
E[D]=0.60(10.5)+0.05(16)=7.10
\]

So an ordinary triggered OA is worth about **7.1 expected damage**.

A glaive has Graze. Graze deals the attack ability modifier on a miss, and the glaive is a 1d10 Heavy/Reach weapon. citeturn21view0turn21view1 At the same 65% accuracy:

\[
E[D]=0.60(10.5)+0.05(16)+0.35(5)=8.85
\]

So a glaive OA is roughly **8.85 expected damage**.

With Advantage, the corresponding glaive expectation rises to about **10.36**.

That sounds sizeable until trigger frequency is included:

| Chance of getting one usable OA in a round | d10+5 expected DPR | Glaive + Graze expected DPR |
|---:|---:|---:|
| 25% | 1.78 | 2.21 |
| 50% | 3.55 | 4.43 |
| 75% | 5.33 | 6.64 |
| 100% | 7.10 | 8.85 |

The 100% line is not the ordinary OA baseline. It represents a feature or encounter pattern that makes the reaction nearly guaranteed every round.

That is why **trigger expansion** deserves more scrutiny than **OA enhancement**.

### What about adding another 1d10 to the Opportunity Attack?

At 65% hit chance, assuming the extra die doubles on a critical hit:

\[
0.60(5.5)+0.05(11)=3.85
\]

A +1d10 rider on an Opportunity Attack therefore adds **3.85 expected damage each time the OA actually happens**.

Its round-by-round addition becomes:

| OA occurs in... | Expected DPR from the +1d10 |
|---:|---:|
| 25% of rounds | 0.96 |
| 50% | 1.93 |
| 75% | 2.89 |
| 100% | 3.85 |

That is simply **not an alarming DPR mechanic**.

A Veteran drill saying something like “once per turn when you hit with an Opportunity Attack, the attack deals an extra 1d10 damage” would be extremely unlikely to break the subclass on raw damage. It might not even be good enough to spend one of four precious drill selections on unless it had another benefit.

### Weapon Mastery already makes Fighter OAs tactically interesting

This is another reason not to overprice an OA drill.

At Fighter 9, Tactical Master allows the Fighter, whenever attacking with a weapon whose mastery they can use, to replace that weapon's mastery property **for that attack** with Push, Sap, or Slow. It has no “on your turn” restriction. citeturn19view2

Thus a level 9 Fighter's Opportunity Attack can already potentially:

- Push a Large-or-smaller creature 10 feet straight away.
- Give it Disadvantage on its next attack.
- Reduce its Speed by 10 feet.

Those mastery effects are defined exactly that way in the 2024 equipment rules. citeturn21view2turn21view3

A halberd's Cleave can also potentially make an additional attack against another creature standing beside the first, because Cleave is once **per turn**, not once per round. An OA occurring on another creature's turn can therefore have a fresh Cleave use if the positioning requirements exist. citeturn21view0

This substantially changes how I would evaluate something like **Hook and Turn**.

If Hook and Turn merely pushes the creature 5 feet directly away, it is **too redundant**, not too powerful: Tactical Master can already Push 10 feet at Fighter 9. citeturn19view2turn21view2

If Hook and Turn instead says something like:

> When you hit a creature with an Opportunity Attack, you can move it up to 5 feet to an unoccupied space within your reach.

that is interesting because **lateral repositioning** differs from Push's mandatory straight-away direction. The risk would come from hazards and forced-position combinations, not raw distance. Five feet is probably a reasonable starting point.

### Sentinel is a concern, but a very specific one

Current Sentinel rules include a Guardian trigger that can create an Opportunity Attack after a nearby creature Disengages or hits somebody other than the Sentinel, and Halt sets a creature's Speed to 0 for the rest of the current turn after the Sentinel hits with an Opportunity Attack. Current rules discussions quote and analyze precisely this interaction. citeturn13search17turn13search13

This produces two design consequences.

First, if a Veteran feature says:

> “When X happens, make an **Opportunity Attack**...”

then a Veteran who also has Sentinel can potentially apply Halt to that subclass-created OA.

Second, this still doesn't create two Reactions. If both Sentinel and the Veteran drill trigger, the character still has the same one-Reaction limitation. citeturn18view2

So I would downgrade “Sentinel interaction” from **potential exploit** to **deliberate interoperability choice**.

The safest rule is:

**Movement punishment → Opportunity Attack.**

**Retaliation/counterattack → Reaction melee attack.**

That is enough. No elaborate anti-feat language is necessary.

### The genuinely important OA multiclass is Rogue

Here there **is** a real optimization issue, but even this should not be exaggerated.

2024 Sneak Attack remains “once per turn,” not “once on your turn.” A Rogue can therefore Sneak Attack on their own turn and potentially Sneak Attack again on somebody else's turn with a qualifying reaction attack. citeturn22view0turn22view1

A Veteran feature that **reliably manufactures reaction attacks** can consequently become more valuable on Veteran/Rogue than on a pure Veteran.

For example, a hypothetical Veteran 7/Rogue 13 has 7d6 Sneak Attack. citeturn22view0 With a rapier and Dexterity 20, at our 65%/5%-crit assumptions, a qualifying off-turn Sneak Attack is worth approximately:

Weapon:

\[
0.60(9.5)+0.05(14)=6.4
\]

Sneak Attack:

\[
0.60(24.5)+0.05(49)=17.15
\]

Total:

\[
23.55
\]

So a **guaranteed qualifying reaction attack every round** would indeed be substantial on that multiclass.

But three qualifications matter.

First, the attack still has to meet Sneak Attack's Finesse/Ranged and Advantage-or-adjacent-ally requirements. citeturn22view0

Second, a Rogue of level 5 or higher also uses its Reaction for Uncanny Dodge, creating a real offensive/defensive opportunity cost. citeturn22view2

Third—and most importantly—**Sentinel already provides Rogues with a route to off-turn Sneak Attack**. The Veteran would not invent that optimization pattern. citeturn15search16

Therefore:

> A Veteran feature that adds a **reliable new reaction-attack trigger** deserves testing with Rogue. A Veteran feature that simply makes ordinary Opportunity Attacks somewhat better does not deserve panic.

That is a materially less restrictive design conclusion than the earlier one.

## The d10 question: “once per Attack action” is not remotely the same problem as “per attack”

This is another place where wording can make the mechanic sound scarier than the math actually is.

There are three very different mechanics:

> **Once on your turn:** one possible +1d10.

> **Once per Attack action:** normally one +1d10, with additional opportunities from Action Surge or Haste.

> **Once per attack:** two, three, four, five, or more +1d10s depending on the build.

The third is potentially enormous.

The second usually is not.

### On an ordinary Fighter turn, “per Attack action” and “once per turn” are functionally identical

A 2024 Fighter gets two attacks at level 5, three at level 11, and four at level 20 **when taking the Attack action on the Fighter's turn**. citeturn19view1turn19view2turn19view4

Nick can put the Light property's extra attack inside the Attack action, but Nick is still just an extra attack inside that same action and is limited to once per turn. citeturn21view1

Likewise, Polearm Master's bonus attack is not another Attack action. citeturn17view6

Therefore this:

> Once during each Attack action, when you hit...

does **not** mean the Fighter gets the die two times at level 5, three times at 11, and four times at 20.

It remains **one die**.

On 95%+ of ordinary turns in many campaigns, there is no difference whatsoever between the two trigger structures.

### How much is the d10 itself worth?

Using 65% total accuracy, including 5% critical hits, and assuming the Veteran spends the die on the first successful attack, the expected +1d10 is:

| Attacks available in that Attack action | Expected +1d10 contribution |
|---:|---:|
| 1 | 3.85 |
| 2 | 5.20 |
| 3 | 5.67 |
| 4 | 5.83 |

The value approaches 5.92 rather than exactly 5.5 because a critical hit doubles the extra damage die under the normal critical-hit rules, while additional attacks make it increasingly unlikely that no attack hits.

With Advantage:

| Attacks | Expected +1d10 |
|---:|---:|
| 1 | 5.36 |
| 2 | 6.02 |
| 3 | 6.10 |
| 4 | 6.11 |

So an at-will d10 rider is a **meaningful subclass damage feature**, but it is not remotely equivalent to adding 1d10 to every Fighter attack.

### It is meaningful at low level, however

This point should not get lost.

Take a simplified no-feat greatsword/Graze Fighter. Greatswords deal 2d6 and have Graze; Graze deals the attack ability modifier when the attack misses. citeturn21view0turn21view1

Using the same 65% hit assumption:

| Fighter level | Assumed ability mod | Attacks | Approx. base Attack-action damage | +1d10 rider | Increase |
|---:|---:|---:|---:|---:|---:|
| 3 | +3 | 1 | 7.9 | 3.85 | **48.7%** |
| 5 | +4 | 2 | 17.8 | 5.20 | **29.2%** |
| 11 | +5 | 3 | 29.7 | 5.67 | **19.1%** |
| 20 | +5 | 4 | 39.6 | 5.83 | **14.7%** |

Those percentages are against an intentionally simple no-feat baseline, so optimized GWM, magic weapons, bonus attacks, buffs, and subclass effects make the percentage smaller.

Still, this shows an important nuance:

**“Once per Attack action rather than once per turn” isn't the dangerous part.**

**“Free at-will 1d10 starting at level 3” is itself a substantial damage feature.**

Those are separate design questions.

A +1d10-at-level-3 Veteran could be perfectly defensible, but it should be recognized as one of the subclass's principal combat features rather than a tiny ribbon added on top of an already full level-3 package.

### There is a strong official comparison: Hunter's Colossus Slayer

The 2024 Hunter Ranger gets Colossus Slayer at level 3: when it hits a creature with a weapon, the weapon deals an additional **1d8** if the target is missing Hit Points, once per turn. citeturn22view1

That is extremely relevant to a proposed Veteran **Finish the Wounded**.

At the same 65% accuracy, a once-per-turn d8 applied to the first successful attack is worth approximately:

| Attacks available | Expected d8 contribution |
|---:|---:|
| 1 | 3.15 |
| 2 | 4.25 |
| 3 | 4.64 |
| 4 | 4.77 |

The Veteran d10 version is therefore only about **0.7–1.1 DPR ahead of the d8 itself**, depending on attack count.

That is not an unreasonable gap.

In fact, this comparison makes me considerably more comfortable with:

> **Finish the Wounded.** Once during each Attack action you take on your turn, when you hit a creature that was already missing Hit Points, you can cause the attack to deal an extra 1d10 damage.

The question becomes whether the rest of the level-3 Veteran package is also very strong, not whether a d10 is inherently excessive.

### Action Surge is the first actual difference between the wordings

Action Surge gives one extra action on the Fighter's turn, excluding the Magic action. It recharges on a Short or Long Rest, and at Fighter 17 there are two uses between rests but still only one use on a turn. citeturn19view0turn19view4

Suppose the Fighter takes Attack, then Action Surge → Attack.

A “once per turn” d10 is still one use.

A “once per Attack action” d10 can trigger twice.

How large is that difference?

Using the same no-feat greatsword model:

| Level | Surge turn, once/turn rider | Surge turn, per-Attack-action rider | Difference |
|---:|---:|---:|---:|
| 5 | ~41.4 | ~46.0 | **+4.6** |
| 11 | ~65.3 | ~70.7 | **+5.4** |
| 20 | ~85.1 | ~90.9 | **+5.7** |

So even on the Fighter's marquee nova turn, changing the restriction from once on the turn to once per Attack action adds roughly **five expected damage**.

As a percentage of that entire surged turn, it is roughly:

- 11% around level 5,
- 8% around level 11,
- 7% around level 20.

That is real.

I would not describe it as huge.

Over a three-round encounter containing one Action Surge, the distinction averages only about **1.5–1.9 DPR**.

Over six combat rounds between rests with one Surge, it averages under **1 DPR**.

This is precisely the kind of interaction that deserves documentation but **not automatic removal**.

### Haste is the larger edge case

Haste grants a second action every turn, and that action can explicitly take the Attack action, although it can make only one attack. citeturn20view0 A Potion of Speed reproduces Haste without Concentration and without Haste's normal ending lethargy. citeturn20view1

That means a per-Attack-action rider can trigger from:

1. the ordinary Attack action;
2. Haste's one-attack Attack action;
3. an Action Surge Attack action on the nova turn.

At 65% accuracy, Haste's one-attack action makes the d10 rider worth approximately 3.85 additional expected damage when considered independently.

More exactly, because the once-per-turn version can fall back on the Haste attack if the ordinary attacks all miss, the difference between the two wordings is approximately:

| Fighter attacks in normal Attack action | Additional DPR from changing once/turn → once/Attack action while Hasted |
|---:|---:|
| 2 | ~3.38 |
| 3 | ~3.69 |
| 4 | ~3.79 |

With Haste **and** Action Surge on the same turn, the difference becomes roughly 8–10 expected damage.

That is a worthwhile optimization interaction.

It is still not a broken one.

Haste is a level-3 Concentration spell and represents an external resource and action investment unless supplied through an item. citeturn20view0

### My revised recommendation on the wording

If the design intent is:

> “The Veteran is exceptionally good at converting each concerted offensive effort into one nasty hit, and Action Surge should make that slightly better,”

then **once per Attack action is defensible**.

I would write it deliberately:

> **Once during each Attack action you take on your turn, when you hit a creature with a weapon or an Unarmed Strike, you can deal an extra 1d10 damage to it.**

The phrase **“on your turn”** eliminates peculiar Ready/off-turn Attack-action interactions while intentionally retaining Action Surge and Haste.

If you do **not** want Haste to multiply it, use:

> **Once on each of your turns, when you hit a creature with an attack made as part of the Attack action...**

I no longer think balance alone compels the latter wording.

The choice is mainly one of desired synergy.

## Spot the Shooter is currently too niche to deserve a scarce drill selection

Here I would move in the **opposite** direction: the previous concern was not that this is too strong. It is that, under the actual 2024 Hide rules, the obvious version is considerably weaker than it first appears.

### A normal hidden shooter already reveals itself by attacking

The 2024 Hide action says that a successful Hide grants the Invisible condition while hidden, records the Stealth result as the DC to find the creature, and then says the creature stops being hidden immediately after it makes an attack roll, among other termination conditions. citeturn18view0

So consider:

> **Spot the Shooter.** When a hidden creature attacks you, use your Reaction to take the Search action to locate it.

Normally:

1. archer is hidden;
2. archer attacks;
3. making the attack roll ends Hidden;
4. Veteran's reactive Search becomes unnecessary.

That is a serious rules problem for the feature's value.

### There are exceptions—but they prove how niche it is

The 2024 Skulker feat has a Sniper component that allows a hidden creature that **misses** its attack to avoid revealing its location. Official D&D Beyond discussion of the feat highlights that function. citeturn16search10

The level-9 Thief can spend Sneak Attack damage through Supreme Sneak's Stealth Attack option so an attack does not end the Hide action's Invisible condition if the Thief finishes the turn behind Three-Quarters or Total Cover. citeturn22view2

Against those special cases, reactive searching is useful.

But that makes the proposed drill something like:

> “Spend one of your limited Veteran Drill selections so you can respond to enemies using Skulker, level-9 Thief technology, or bespoke monster hiding exceptions.”

That is not competitive with Forced March, Size Up, Shield the Line, Quick Barricade, Sabotage, or a strong Help drill.

### Observant also gives us an action-economy benchmark

The 2024 Observant feat includes Quick Search; D&D Beyond's current feat index lists that capability, and rules discussion identifies it as allowing Search as a Bonus Action. citeturn17view6turn13search3

So “Search faster than an ordinary character” is absolutely legitimate feat/subclass design space.

The problem with Spot the Shooter isn't action compression.

It is the **trigger/payoff combination**.

### What would make the concept worthwhile?

I see three viable approaches.

**Best choice: fold it into a broader Search drill.** For example:

> **Threat Scan — Search.** When you take the Search action, you have Advantage on the Wisdom check if you are searching for a creature that has attacked, moved, or made an audible sound since the end of your last turn. If you find a hidden creature this way, you also learn the direction from which it last moved or attacked.

That is useful against ambushers, hidden creatures, tracks in combat, invisible-but-audible creatures where the rules permit a Search, and other threats. It isn't one extremely narrow counter-sniper button.

A stronger version could make it:

> When a creature you can't see makes an attack against you or a creature you can see within 30 feet, you can use your Reaction to make a Wisdom (Perception) check to Search for that creature.

But even there, I would **not** have it automatically negate magical Invisibility or allow perception through Total Cover. That turns mundane observation into quasi-Truesight.

The third option is simply to **cut Spot the Shooter**.

For a 10–14-drill subclass in which the player knows only four or five early on, I currently favor cutting it unless folded into something broader.

This leads to a useful menu-design principle:

> **A narrow feature can be flavorful enough to include in a broad baseline feature. It is not necessarily valuable enough to charge a drill-known slot for it.**

That distinction matters a lot for Veteran.

## Size Up is much more likely to be underpowered than overpowered

Your current wording is:

> **Size Up — Study.**  
> When you take the Study action, you can use a creature you can see within 60 feet as the source of knowledge you are studying. If the Intelligence check succeeds, choose one of the following subjects: **defenses, movement, attacks, or apparent condition**. The DM tells you one useful qualitative fact about the chosen subject that could reasonably be inferred from the creature's appearance, equipment, behavior, or known lore.  
>
> This drill never reveals exact Armor Class, Hit Points, ability scores, saving-throw modifiers, attack bonuses, spell slots, legendary-resource counts, or a hidden trait that cannot reasonably be inferred.  
>
> Once you use this drill successfully on a creature, you can't use it on that creature again until you finish a Long Rest.

### The underlying rules interpretation is sound

The 2024 Study action is indeed an Intelligence check used to examine memory, a book, a clue, **or another source of knowledge** and call to mind important information. Its knowledge table associates History with wars, Giants and Humanoids; Nature with terrain and creature categories such as Beasts and Dragons; Arcana and Religion with other creature categories; and Investigation with traps, mechanisms, ciphers, and similar matters. citeturn18view1

So the Veteran saying:

> “I can use the creature's equipment, posture, scars, locomotion, and observed behavior itself as another practical source”

is a reasonable subclass modification to Study.

It does not look like a rules exploit.

It also doesn't trespass heavily on Battle Master.

The 2024 Battle Master's Know Your Enemy was specifically revised to a **Bonus Action** and reveals the target's Immunities, Resistances, and Vulnerabilities. citeturn17view5 Size Up is broader but softer, requires a Study check, costs the Study action, and explicitly prevents unrestricted numerical extraction.

If anything, Battle Master establishes that **much harder mechanical information can safely be revealed at level 7 for much less action cost**. citeturn17view5

That is evidence in favor of strengthening Size Up, not weakening it.

### The current feature has four simultaneous brakes

At present the player must:

1. spend a full action;
2. make an Intelligence check;
3. succeed;
4. receive only one qualitative fact;
5. then be locked out of that creature until the next Long Rest.

That is actually five brakes.

For a Fighter, the first is enormous.

At level 5, the Fighter sacrifices two attacks to Study. At level 11 it sacrifices three. At level 20 it sacrifices four. Extra Attack explicitly scales only when the Fighter takes the Attack action on its turn. citeturn19view1turn19view2

Using the same intentionally modest greatsword/Graze model:

| Fighter level | Approx. damage forgone by taking Study instead of Attack |
|---:|---:|
| 3 | 7.9 |
| 5 | 17.8 |
| 11 | 29.7 |
| 20 | 39.6 |

Optimized feat and magic-weapon builds can make that opportunity cost larger.

Consequently, in a combat at level 11, the current Size Up effectively asks:

> “Would you trade roughly thirty expected damage for one GM-described qualitative observation after succeeding on an Intelligence check?”

Usually the optimizer's answer is **no**.

That does not make the feature bad conceptually. It means its natural habitat is **before combat and outside combat**.

And that may actually suit the Veteran beautifully.

The grizzled soldier should be the person watching the ogre camp from the ridge, examining the mercenary captain across the tavern, inspecting the griffon's saddle and gait, or looking over a fighting pit before deciding how to approach the problem.

But if that is the intention, I would stop evaluating Size Up as though it is supposed to compete with Attack during initiative. It doesn't need to.

### Its check is also less reliable than it looks

Study does not provide one universal fixed DC; the DM adjudicates the Intelligence check according to the information involved. citeturn18view1

For illustration only, suppose a fairly typical useful fact is DC 15.

An Intelligence 10 Veteran would have the following raw success probabilities:

| Relevant Study bonus | DC 15 success |
|---:|---:|
| +0 | 30% |
| +2 | 40% |
| +3 | 45% |
| +4 | 50% |
| +5 | 55% |
| +6 | 60% |

That is not great for a limited drill whose entire payoff disappears on failure.

The 2024 Fighter's Tactical Mind helps substantially. After failing an ability check, the Fighter can spend Second Wind to add 1d10; if that still fails, the Second Wind use is not expended. citeturn19view0

If the player always invokes Tactical Mind after a DC 15 failure, I calculate these combined success rates:

| Initial check bonus | Raw success | Success after Tactical Mind opportunity |
|---:|---:|---:|
| +0 | 30% | **57.5%** |
| +2 | 40% | **67.5%** |
| +3 | 45% | **72.5%** |
| +4 | 50% | **77.5%** |
| +5 | 55% | **82.0%** |
| +6 | 60% | **86.0%** |

That synergy is actually good design: Size Up gives the Fighter something distinctive to do with an Intelligence check, while Tactical Mind makes an otherwise mediocre Fighter Intelligence build capable of pulling through when the information matters. citeturn19view0turn18view1

Importantly, this does **not** duplicate Tactical Mind. Size Up creates a new meaningful use case; Tactical Mind merely supports the normal check.

### The bigger weakness is the value of the answer

Consider each category.

**Defenses** can easily result in:

> “It is heavily armored.”

The player could already see that.

**Movement** might result in:

> “It looks quick.”

Again, potentially obvious.

**Attacks** could produce:

> “It relies heavily on that long spear.”

Visible information.

**Apparent condition** risks either being obvious or turning into coded HP extraction.

The 2024 rules formally define **Bloodied** as having half Hit Points or fewer. citeturn17view4 If “apparent condition” permits the DM to say “it is Bloodied,” that is mechanically useful qualitative information without revealing an exact HP total—but it is worth deciding explicitly whether that is intended.

So your anti-stat-block clause works, but the drill needs the opposite protection too:

> **the successful answer should not be allowed to be useless.**

I would add the word **meaningful** or explicitly require that the fact provide information not already obvious to the character.

Something like:

> “The fact must be truthful and useful, and can't merely repeat something already obvious to you.”

That is unusual rules language, but for a GM-facing information power it may be justified.

### I would also change “apparent condition”

“Condition” is already a loaded game term. The rules contain formal Conditions such as Prone, Stunned, Invisible, and so forth. citeturn18view2

I would call the fourth category **physical state** instead.

That communicates “injury, exhaustion, impairment, composure” without implying that the player gets to query the Conditions field of a stat block.

### The once-per-creature Long Rest restriction is probably unnecessary in its current form

This is the part I would most strongly change.

Suppose you successfully spend an action to Study the hobgoblin captain and ask about movement.

The DM says:

> “The old injury in its left leg makes abrupt lateral movement look difficult.”

Under the current wording, you can now never ask about that captain's defenses, attacks, or physical state until tomorrow.

That is a very severe lock for one qualitative fact.

The restriction seems designed to prevent repeated fishing:

> “I Study it again. And again. And again. Eventually tell me the stat block.”

That is a legitimate concern.

But a cleaner lock is:

> **Once you learn a fact about one of these subjects for a creature, you can't choose that subject for that creature again until you finish a Long Rest.**

Now the drill naturally contains four pieces of potential information, each costing a separate Study action/check. That is hardly exploitable.

Alternatively, retain one use per creature but give **two subjects** on a successful check.

I prefer the second solution for table speed.

### Revised Size Up I would actually playtest

I would test this version:

> **Size Up — Study.** When you take the Study action, you can study a creature you can see within 60 feet, using its appearance, equipment, behavior you have observed, and your knowledge of creatures of its kind as the source of knowledge. The DM determines the applicable Intelligence skill and DC as normal.  
>
> On a successful check, choose **two** of the following subjects: **defenses, movement, attacks, or physical state**. For each chosen subject, the DM tells you one truthful and useful qualitative fact that you could reasonably infer from the creature's appearance, equipment, behavior, or known lore. A fact can't reveal a numerical statistic or resource, and it can't reveal a trait for which you have observed no evidence and possess no relevant knowledge.  
>
> Once you successfully use this drill on a creature, you can't use it on that creature again until you finish a Long Rest.

I would **not** be frightened of the two facts.

You paid a complete action and passed an Intelligence check.

The closest official subclass comparison obtains exact damage Immunities, Resistances, and Vulnerabilities using a Bonus Action at Battle Master 7. citeturn17view5

Your Veteran should not be afraid to learn that:

> “The troll's burned patches have regenerated poorly, and its long arms make it especially dangerous to withdraw from.”

That is exactly the fantasy.

### Is it worth a drill?

With **one** qualitative fact, full action, check, and once-per-creature Long Rest?

**Barely. I think optimized players would frequently skip it.**

With **two** meaningful qualitative facts?

**Yes, particularly in investigation-, exploration-, and scouting-heavy campaigns.**

As a baseline part of Veteran's Eye rather than a drill choice?

**Definitely.**

That last option may actually be best.

Size Up is so central to “old soldier who recognizes what they're looking at” that forcing it to compete with direct combat drills may be structurally wrong. You could make it part of **Veteran's Eye** and let the selectable drills specialize the generic actions further.

## A more accurate risk hierarchy for the Veteran

The quantitative review changes what I think you should be afraid of.

### The genuinely high-risk mechanics

**Extra Reactions remain the largest red flag.** The single-Reaction rule is what keeps Opportunity Attacks, Sentinel triggers, Rogue off-turn Sneak Attack, defensive reactions, and other effects mutually exclusive. citeturn18view2turn22view2 Giving a Veteran “one Reaction every turn” would remove that safety valve and remains a bad idea.

**Very reliable generated reaction attacks are more important than enhanced Opportunity Attacks.** A normal OA might occur in 25–50% of rounds depending heavily on positioning. “Whenever an adjacent enemy attacks somebody except you” can approach one usable trigger every round in the right party. That is what changes 2–4 expected DPR into 7–10 before subclass riders and multiclass effects.

**Speed 0 is much more consequential than +1d10.** Sentinel's Halt demonstrates that it is a premium control rider. citeturn13search13 A speed-zero hit can leave a melee creature unable to reach its intended target. The value can exceed an extra weapon die by a great deal even though it cannot be expressed as fixed DPR.

**Calling every custom reaction attack an Opportunity Attack is unnecessarily risky.** Not because OAs are overpowered, but because “Opportunity Attack” is an interoperability tag. Sentinel hooks into it now, and future rules can hook into it later. Use the tag when that compatibility is intentional.

**A low-level, unlimited Counterstroke deserves more scrutiny than Hook and Turn.** “When a creature misses you, attack it” can become extremely frequent on a durable frontliner. The one-Reaction cap keeps it sane, but at that point you are giving close to a repeatable Battle-Master-Riposte-shaped effect without a superiority-die resource. The issue is trigger reliability, not OA terminology.

### The moderate issues

**+1d10 once per Attack action is strong enough to count toward the subclass's damage budget, but the per-action wording itself is not a major problem.**

At level 3 the d10 is a large percentage of an otherwise plain Fighter's DPR. At levels 11–20 it is much less dramatic. The incremental advantage over “once per turn” is essentially zero on ordinary turns, about five expected damage on Action Surge turns, and about 3–4 damage per Hasted round. citeturn19view0turn20view0

I would therefore be comfortable testing it.

**Five-foot forced movement on an OA is not inherently excessive.** The level-9 Fighter can already choose a 10-foot straight Push on qualifying weapon attacks through Tactical Master. citeturn19view2turn21view2 The Veteran's feature needs to be *different* rather than weaker—lateral repositioning is promising.

**Sentinel overlap is primarily an identity/feat-value issue.** A Veteran drill that exactly recreates Guardian or Halt makes Sentinel less interesting and effectively gives the subclass part of a feat. It does not automatically create a broken engine.

### The mechanics that are more likely too weak

**Spot the Shooter as a standalone drill is currently too weak**, because normal Hide ends on making an attack roll. citeturn18view0 It should be folded into a broad Search drill or removed.

**Current Size Up is too gated.** Its anti-stat-extraction limitations are fine; the problem is asking for a full action, successful Intelligence check, one qualitative result, and then a Long-Rest lockout.

**Any Help/Search/Study drill that merely makes the action “a little better” needs to overcome the Fighter's enormous Attack-action opportunity cost.** The Help action gives Advantage on one specified next check or one ally's next attack; Search and Study consume full actions by default. citeturn18view0turn18view1 A level-11 Fighter gives up three attacks to use one. That is a much stronger natural balancing mechanism than the earlier design analysis may have credited.

This is why utility drills do **not** generally need to be timid.

## Recommended design adjustments from this research

I would now use the following thresholds when building the next Veteran playtest.

| Proposed effect | My current design verdict |
|---|---|
| +1d10 once per Attack action on your turn | **Safe to playtest** |
| +1d10 once per turn | Safe but more conservative than necessary |
| +1d10 per individual attack | **Too much unless heavily limited** |
| +1d10 on an OA only | Probably **underpowered as an entire drill** without another rider |
| Move OA target 5 ft within reach | **Safe to playtest** |
| OA reduces Speed by 10 ft | Probably safe; overlaps Slow somewhat |
| OA makes Speed 0 | Premium; use prerequisite, limitation, or accept Sentinel-level power |
| Ignore Disengage | Premium but manageable alone |
| Ignore Disengage + Speed 0 | Too close to handing out the strongest Sentinel package |
| Reaction attack when enemy misses you | Moderate–strong; gate by level or frequency |
| Reaction attack when enemy hits ally | Moderate–strong; already Sentinel-adjacent |
| Call those retaliation attacks “Opportunity Attacks” | Avoid unless Sentinel interoperability is intended |
| One extra restricted Reaction per round at level 18 | Potentially testable with very narrow permitted uses |
| One Reaction on every creature's turn | Still reject |
| Reactive Search after hidden shooter attacks | **Cut/rewrite** |
| Broad “Threat Scan” Search drill | **Promising** |
| Current one-fact Size Up | **Buff** |
| Two-fact qualitative Size Up | **Promising** |
| Exact AC/save/HP extraction | Still unnecessary |
| Exact resistance/immunity extraction | Mechanically safe by precedent, but too Battle-Master-like for Veteran |
| Qualitative inferential tactical information | **Excellent Veteran territory** |

The major philosophical correction I would make to the Veteran project is this:

> **Do not balance every martial feature as though an optimizer will automatically convert it into a combo engine. First quantify whether the combo actually exists under 2024 wording.**

The 2024 Fighter already has strong built-in attack riders through Weapon Mastery, Tactical Master, and Studied Attacks; Tactical Master can place Push, Sap, or Slow on qualifying weapon attacks, while Studied Attacks grants Advantage on the Fighter's next attack after a miss. citeturn19view2turn19view3 That means Veteran design should certainly avoid duplicating those mechanics wholesale.

But it does **not** mean every extra bit of battlefield control needs to be tiny.

Similarly, 2024 Fighter optimization no longer inherits the exact 2014 PAM/GWM/Sentinel ecosystem. Community analysis of the revised rules repeatedly notes that Reactive Strike is no longer an Opportunity Attack and that GWM's major damage rider is restricted to the Attack action on the Fighter's turn. citeturn15search1turn15search6turn15search13 That materially lowers the ceiling of ordinary Opportunity-Attack synergies.

My resulting recommendation for Veteran is therefore a little bolder than before:

**Let the Veteran be good at Opportunity Attacks.**

Just don't multiply Reactions.

**Let Finish the Wounded be a meaningful d10 damage feature.**

Just understand that the free d10 itself is part of the subclass's power budget; “per Attack action” is not the scary part.

**Do not charge a precious drill slot for merely locating a shooter who usually reveals themselves automatically.**

Give Search something broader.

**Let Size Up provide genuinely useful information.**

The player is already paying an action and an Intelligence check, and the qualitative-information restriction keeps it well below genuine stat-block extraction. Against the official Battle Master's Bonus-Action Know Your Enemy, the current version is considerably more conservative than necessary. citeturn17view5

The overarching design lesson from the numbers is that the Veteran's biggest balance danger is **not raw damage dice**. It is **reliable action generation and tempo denial**. Conversely, its biggest design danger on the utility side is **charging Fighter-sized action costs for ribbon-sized benefits**.

That is where I would put the balance budget in the next playtest.