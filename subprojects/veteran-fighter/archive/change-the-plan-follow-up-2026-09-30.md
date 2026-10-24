# Veteran Fighter: Change the Plan — Focused Follow-Up Investigation
Date: September 30, 2026
Status: Research recommendations; not accepted subclass canon.
Download edition of the preceding response. Citation markers have been replaced with source links.


Current Change the Plan is not demonstrably overpowered. Its principal problem is how it prices control attempts, not excessive damage. The previous Bonus Action replacement overcorrects for several builds and does not fully remove the underlying incentive.


My strongest recommendation is to keep an immediate, free fallback, trigger it from a missed damaging attack, support ranged weapon changes, and remove the standalone resisted-Grapple/Shove refund. A second viable direction preserves that branch by granting the follow-up weapon attack regardless of whether control succeeds—a deliberate power increase that needs closer testing.


## A. Executive conclusion


| Question | Finding |
|---|---|
| Is current total power excessive? | Not established. Its control efficiency deserves testing, particularly with environmental hazards. |
| Is its damage excessive? | Usually no. Ordinary weapon-to-unarmed damage is modest. |
| What is the main problem? | A control attempt becomes cheaper as the enemy becomes better at resisting it. |
| Does Action Surge break it? | No demonstrated break. It doubles the available responses during a resource-limited nova turn. |
| Is normal fallback Weapon Mastery problematic? | Not independently. Keep it unless a specific interaction proves excessive. |
| Does the Bonus Action proposal overcorrect? | Yes for builds with established Bonus Action attacks, and potentially for the feature’s intended immediacy. |
| Does that proposal eliminate failure fishing? | No. It adds a cost while retaining a failure-dependent weapon refund. |


The essential distinction: “You are encouraged to attempt control even when resistance is high” is a defensible complaint. “You deal excessive damage because resistance is high” generally is not.


I retrieved the preferred addendum, context pack, Master Handoff, evolution timeline, D.4.1 reference, and September 30 investigation. I used one representative of each duplicate group. Your current prompt governs this investigation; the previous report remains advisory. No subclass changes below are accepted canon.


## B. Current-feature quantitative and mechanical audit


### Assumptions


These are transparent analytical examples, not predictions for every encounter:


- Weapon hit probabilities: 50%, 65%, 80%.
- Enemy control-save success probabilities: 35%, 65%, 80%.
- Attacks before Change the Plan: 1/2/3/3/4 at Fighter 3/5/11/13/20.
- Ordinary damaging Unarmed Strike: 1 + Strength modifier.
- No magic items, external buffs, resistances, or environmental damage.
- Generated attacks are treated as part of the triggering Attack action for the main analysis. The current feature should explicitly settle this point.


The revised Fighter’s Extra Attack progression, Action Surge restriction, and Studied Attacks were checked against current official rules. Action Surge cannot supply a Magic action and remains usable only once on a turn, including after its second rest-based use arrives. [1]


### 1. Weapon miss → Unarmed Strike


With n independent attacks and hit probability p:


P(at least one miss) = 1 − pⁿ


If the fallback also hits with probability p, and deals D_U damage:


E(fallback damage) = (1 − pⁿ) × p × D_U


That calculation describes the gross fallback contribution before accounting for effects such as consuming Studied Attacks.


| Level | Attacks | Trigger at 50% accuracy | At 65% | At 80% |
|---:|---:|---:|---:|---:|
| 3 | 1 | 50.0% | 35.0% | 20.0% |
| 5 | 2 | 75.0% | 57.8% | 36.0% |
| 11 | 3 | 87.5% | 72.5% | 48.8% |
| 13 | 3 | 87.5% | 72.5% | 48.8% |
| 20 | 4 | 93.8% | 82.1% | 59.0% |


Using +3 Strength at level 3, +4 at level 5, and +5 thereafter, at 65% accuracy:


| Level | Gross ordinary Unarmed Strike damage added |
|---:|---:|
| 3 | 0.91 DPR |
| 5 | 1.88 DPR |
| 11 | 2.83 DPR |
| 13 | 3.82 DPR with Studied Attacks on the fallback |
| 20 | 4.33 DPR under the same assumption |


The level-20 row isolates Change the Plan and Studied Attacks. Against the Veteran capstone’s designated target, existing Advantage makes misses less frequent.


Finding: the ordinary damage branch is comfortably plausible for a defining combat feature.


An Unarmed Fighting investment increases its damage. That requires a Fighting Style choice and sometimes equipment concessions; the increase should be evaluated alongside those costs.


### 2. Studied Attacks: gross damage is not net gain


The previous report overstated the interpretation of its level-13 numbers.


A missed weapon attack already gives the base Fighter Advantage on its next attack against that creature. An immediate fallback uses that benefit, potentially leaving the next, more damaging weapon attack without it.


A simple state-based calculation illustrates the difference:


- Normal accuracy: 65%.
- Weapon hit damage: 12.
- Unarmed hit damage: 6.
- Same target throughout.
- No critical damage, Masteries, or Advantage carried into the turn.
- Track Studied Attacks after every miss.


| Attacks | Base Fighter expected damage | With current miss fallback | Actual increase |
|---:|---:|---:|---:|
| 3 | 25.09 | 27.72 | 2.63 |
| 4 | 33.68 | 36.54 | 2.86 |


The fallback itself contributes approximately 3.82/4.33 damage, but part of that replaces Advantage the Fighter would otherwise use later.


Therefore: Studied Attacks is useful synergy, not a clean additional 35% multiplier to the feature’s net contribution.


### 3. Resisted Grapple/Shove → weapon attack


Let:
- q = probability control succeeds;
- E_W = expected damage of one ordinary weapon attack.


Replacing a weapon attack with control produces:


E(damage) = (1 − q) × E_W


The expected damage surrendered is:


q × E_W


Using a weapon attack worth 7.8 expected damage:


| Enemy save success | Control success | Recovered weapon damage | Damage surrendered |
|---:|---:|---:|---:|
| 35% | 65% | 2.73 | 5.07 |
| 65% | 35% | 5.07 | 2.73 |
| 80% | 20% | 6.24 | 1.56 |


This is damage insurance for a control attempt, rather than pure extra damage.


The probability of obtaining either successful control or a fallback weapon hit is:


q + (1 − q) × p


At 65% weapon accuracy:


| Control success | Chance of control or weapon hit |
|---:|---:|
| 65% | 87.8% |
| 35% | 77.3% |
| 20% | 72.0% |


Importantly, overall useful-result reliability still falls as resistance rises. What improves is the damage refund.


The previous analysis correctly identified the refund gradient, but its “rational default” conclusion was too broad. Whether control is worthwhile depends on what successful control actually accomplishes.


### 4. Control value


| Situation | Practical value |
|---|---|
| Shove prone before several melee attacks | Potentially substantial accuracy benefit |
| Shove prone before allied ranged attacks | Can hurt the party |
| Grapple a creature that wants to remain beside you | Often limited |
| Grapple a mobile attacker away from vulnerable allies | Potentially excellent |
| Shove into an active damaging area | Potentially very strong |
| Attempt control against an ineligible creature | Not a valid attempt; no legitimate refund |
| Force a boss to spend Legendary Resistance | Situational; the boss can often simply accept minor control |


The revised Unarmed Strike uses separate Damage, Grapple, and Shove options. Ordinary Grapple/Shove requires a saving throw rather than first requiring a damaging hit. Size and free-hand restrictions still matter. [2]


A modest control attempt can become extremely valuable when another character supplies the damaging terrain. That is the most important whole-party optimization test.


### 5. Action Surge


At 65% accuracy, two Attack actions yield:


| Attacks per action | Expected responses across both actions |
|---:|---:|
| 1 | 0.70 |
| 2 | 1.16 |
| 3 | 1.45 |
| 4 | 1.64 |


These are miss-branch estimates without changing Advantage states.


Action Surge makes the feature stronger; it does not establish a broken interaction.


Changing to once per turn would approximately halve its maximum response allowance on Surge turns. That is a real nerf, even if ordinary turns remain unchanged.


### 6. Builds and feat interactions


| Build/interaction | Assessment |
|---|---|
| Sword-and-board | Damaging fallback works through kicks/headbutts. Grappling normally requires freeing the weapon hand; Shove does not. |
| Great Weapon | Ordinary punch damage is small. Shove prone can be more valuable than damage. |
| Polearm | A miss at 10 feet does not automatically put the target within ordinary Unarmed Strike reach. |
| Dexterity melee | Weak ordinary Strength-based Unarmed Strikes make current support uneven. |
| Ranged | Current ranged misses receive no response. Carrying a melee weapon is not equivalent support. |
| Thrown weapons | Current wording covers melee attacks, not ranged attacks made by throwing a Melee weapon. |
| Grappler | A damaging Unarmed Strike can also attempt Grapple when its conditions are met; Advantage against your grappled target is significant. |
| Nick | Adds a possible trigger-bearing attack, but its Light extra attack remains once per turn. |
| Dual Wielder | Free Change the Plan coexists with its Bonus Action attack; the proposed replacement competes with it. |
| Great Weapon Master | Whether the fallback belongs to the Attack action determines eligibility for Heavy Weapon Mastery. |
| Polearm Master | Free fallback coexists with Pole Strike. A Bonus Action replacement often adds little damage over an attack already available. |


Grappler’s Punch and Grab requires a hit with an Unarmed Strike as part of the Attack action on your turn and is once per turn. It does not make an ordinary save-only Grapple attempt deal damage automatically. [3]


Great Weapon Master’s proficiency damage applies to qualifying Heavy-weapon hits within the Attack action. Dual Wielder and Polearm Master supply separate Bonus Action attacks with their own restrictions. [4–6]


### 7. Mastery audit


Preserve normal Mastery unless testing identifies a specific problem.


- Graze: current misses can deal Graze damage and generate an Unarmed Strike.
- Vex: can improve a later attack; overlapping Advantage does not stack.
- Push: improves positioning and can interact with hazardous terrain.
- Topple: adds another save-based control opportunity after a hit.
- Sap: defensive value is meaningful, but repeated applications do not create multiplying Disadvantage.
- Slow: repeated applications do not accumulate unlimited reductions.
- Nick: does not independently give every generated attack another extra attack.


These properties were checked in the current equipment rules. [7]


At Fighter 9, Tactical Master adds existing flexibility. It should remain available normally; a different-weapon requirement should not depend on which replacement Mastery was selected.


### 8. Multiclass potential


The current feature requires Fighter 3, rather than a one-level dip.


Relevant tests:


- Barbarian: Rage and Reckless Attack can improve damaging branches; more Advantage also reduces weapon-miss activation.
- Monk: stronger Unarmed Strikes increase fallback value, but armor, shield, ability-score, and delayed progression costs matter.
- Rogue: an additional finesse weapon attack can rescue a missed Sneak Attack. It does not create a second on-turn Sneak Attack.
- Paladin: an additional eligible hit can carry a limited rider; revised Divine Smite also competes for the Bonus Action.
- Ranger/Warlock: per-hit damage can increase the value of a generated weapon attack, with setup, concentration, or other costs.


No infinite loop was found. The main multiclass concern is additional access to valuable on-hit effects, not recursion.


## C. Whole-game power context


This feature should be assessed as one subclass feature attached to a strong combat chassis, not compared directly with an entire class’s output.


### Representative martial capabilities


| Class | Relevant capability | Implication |
|---|---|---|
| Battle Master | Resource-funded damage, accuracy rescue, and control | Can concentrate power when needed; Veteran trades burst selection for repeatability |
| Champion | Persistent improvements and later reliability | A conditional free fallback is not inherently outside Fighter design |
| Eldritch Knight | Defensive spells, utility, later attack/cantrip integration | Offers capabilities Change the Plan cannot reproduce |
| Psi Warrior | Resource-funded offense, protection, movement | More controllable timing and broader defensive application |
| Barbarian | Reliable Advantage access, Rage damage/resistance, later control | Strong repeatable combat benefits already exist |
| Rogue | Sneak Attack and damage-funded Cunning Strike | Control can coexist with meaningful damage without refunding a failed attack |
| Monk | Bonus Action attacks, Flurry, Stunning Strike, mobility | Repeatable martial action compression is established |
| Ranger | Weapon attacks plus concentration damage and spells | Setup and Bonus Action pressure are genuine costs |
| Paladin | Smite, Aura, and later persistent attack damage | Strong combat packages include party defense and resource-funded burst |


Official Fighter explanatory material confirms that the revised subclasses provide varied maneuver, spell, inspiration, and psionic approaches; those are broader packages than one conditional attack response. [8]


Monk reaches three Flurry attacks at level 10, spending a Focus Point and Bonus Action. Rogue Cunning Strike exchanges Sneak Attack dice for control or movement. These are useful comparisons for cost structure, not proof that an unrestricted free Fighter attack is balanced. [9–10]


### Breakpoints


| Level | Relevant whole-game context | Change the Plan implication |
|---:|---|---|
| 3 | Full casters have second-level spells; martial subclass identities arrive | Ordinary punch fallback is modest; broad full-weapon fallback is a substantial upgrade |
| 5 | Extra Attack; third-level spells; Monk Stunning Strike | One conditional response does not match encounter-wide control |
| 11 | Fighter third attack; stronger Monk attacks; Paladin Radiant Strikes; sixth-level spells | Repeatable value matters, but control and utility remain different axes |
| 13 | Studied Attacks; seventh-level spells | Count displaced Advantage when calculating net benefit |
| 20 | Fourth Fighter attack; capstones; ninth-level spells | The feature remains useful without needing another frequency increase |


Ranger’s later concentration protection and marked-target accuracy improvements, Paladin’s persistent attack damage, and Sorcerer’s Metamagic support demonstrate different forms of scaling and resource dependence. [11–13]


### Representative spell capabilities


- Wizard/Sorcerer/Bard: area damage, multi-target disabling, battlefield separation, and utility.
- Cleric: sustained area damage and movement restriction, alongside healing and buffs.
- Druid: terrain control, summons, and transformation.
- Warlock: repeatable attack damage/forced movement, supplemented by a smaller rest-based spell pool.


For a numerical example, an 8d6 area spell averages 28 damage before saves. At a 50% save-success rate with half damage on success, that becomes approximately 21 per target, excluding rounding. Three targets produce about 63 damage—but consume a slot and an action.


Hypnotic Pattern can disable multiple eligible targets until disrupted; Spirit Guardians combines repeated area damage with movement restriction. Both require concentration. [14]


Whole-game conclusion: current Change the Plan is not alarmingly powerful within this envelope. Its unlimited use matters over long days; spellcasting’s target count, duration, denial, and utility matter in ways DPR does not capture.


Neither observation establishes an exact subclass budget.


## D. Exact incentive diagnosis


The unhealthy gradient is:


greater resistance → more frequent refund → lower damage cost of attempting control


However, an important mathematical qualification follows.


If successful control has practical value V, then:


E(attempt) = qV + (1 − q)E_W


Relative to simply attacking:


E(attempt) − E_W = q(V − E_W)


Under this simplified model:


- If control is more valuable than the weapon attack, attempting it is worthwhile.
- If control is less valuable, attempting it remains worse.
- Higher resistance makes either difference smaller.


Thus, high resistance does not magically make worthless control profitable. It makes speculative control low-risk.


The stronger criticism is behavioral: a Veteran with little investment in grappling can repeatedly make a low-cost speculative attempt before returning to their normal weapon routine.


The previous Bonus Action proposal changes the refund to something like:


(1 − q) × (weapon value − Bonus Action opportunity cost)


It reduces efficiency, but preserves the resistance-dependent refund.


## E. Surgical repairs


| Repair | Removes the incentive? | Power consequence | Verdict |
|---|---|---|---|
| Once per turn | No | Reduces Surge value | Frequency adjustment, not a solution |
| Remove fallback Mastery | No | Reduces damage/control value | Targets the reward rather than the cause |
| Require a prior damaging hit | Partly | Restricts availability | Still rewards a later failed control attempt |
| Allow only Grappler’s resisted Punch and Grab | Partly | Concentrates power in one feat | Too build-specific |
| Give movement instead after failed control | Partly | Usually weaker | Can still make speculative control cheap |
| Grant weapon follow-up on either control outcome | Yes, for failure preference | Significant increase | Serious alternative |
| Remove save-only refund; broaden damaging-miss fallback | Yes | Redistributes power | Strongest starting direction |


The smallest clean repair to the bad branch is outcome neutrality.


The strongest overall repair is changing what qualifies as the failure while preserving a free response.


## F. Redesign candidates


The following candidates are deliberately different. Numerical estimates describe their stated mechanics rather than a finalized subclass budget.


### Candidate 1 — Free Different-Method Fallback


Concept:


Once per Attack action on your turn, after missing with a weapon attack or the Damage option of an Unarmed Strike:


- Make a free immediate attack against that creature.
- A weapon opener requires a different weapon kind or an Unarmed Strike.
- An Unarmed opener requires a weapon.
- The fallback belongs to the Attack action.
- Normal Mastery applies.
- Save-only control does not trigger it.
- Choose between damage caused by the triggering miss and this response.


Why the final clause matters: allowing a full heavy-weapon fallback on top of Graze creates a stronger incentive to choose a poor Graze opener. Making those benefits alternatives narrows that incentive without taxing the Bonus Action.


Expected value:


At 65% accuracy, a fallback worth 6.4 expected damage adds approximately:


| Attacks | Gross fallback damage |
|---:|---:|
| 1 | 2.24 |
| 2 | 3.70 |
| 3 | 4.64 |
| 4 | 5.26 |


Those figures include a 5% critical chance for a d8 + 5 weapon. They exclude Studied Attacks and displaced miss damage.


A full heavy-weapon fallback is stronger, particularly with Great Weapon Master. This is a real buff over ordinary punch damage, not a disguised equal-power substitution.


Behavior:


- Melee: sword → kick, greatsword → maul, spear → handaxe.
- Ranged: longbow → shortbow, crossbow → thrown weapon, firearm → sidearm.
- Grapple/Shove: remain available as a fallback after a weapon miss.
- Action Surge: retains a second response allowance.
- Studied Attacks: naturally affects the fallback.
- Bonus Action/Reaction: neither consumed.
- Optimization: prepare two effective methods; attack normally.
- Risk: heavy-weapon pairing, magic-weapon disparities, on-hit riders.
- Complexity: low to moderate.
- Theme: excellent.


Classification: stronger in some circumstances / weaker in others. Usually stronger for ordinary weapon builds; loses standalone control insurance and Graze stacking.


Recommendation: first playtest choice.


### Candidate 2 — Outcome-Neutral Control Transition


Concept:


Keep weapon-miss fallback support, including ranged different-weapon responses. Replace the failed-control branch with:


“Immediately after resolving a Grapple or Shove attempt that replaces one of your normal attacks, make one weapon attack against that creature, whether the control attempt succeeded or failed.”


The control attempt cannot originate from an attack generated by this feature.


Expected value:


For the control route:


E(damage) = E_W


Successful control is added without sacrificing the replaced weapon attack’s expected damage.


Compared with current control-first behavior, it restores:


q × E_W


Using E_W = 7.8, that means +1.56 to +5.07 expected damage, depending on control success.


Behavior:


- Melee: grab/shove → weapon, regardless of result.
- Ranged: ranged miss → different weapon; close-range control can precede a ranged attack if legal.
- Grapple/Shove incentives: success is now desirable; weak control DC provides no damage advantage.
- Action Surge: up to two control transitions.
- Mastery: normal follow-up Mastery.
- Studied Attacks: control saves do not themselves create it.
- Graze: weapon-miss route should use the same either/or protection as Candidate 1.
- Feats: Grappler is no longer necessary for damage-preserving control.
- Bonus Action/Reaction: neither consumed.
- Optimization: one control attempt per available response becomes attractive whenever it has value.
- Risk: routine control, hazard dragging, prone amplification.
- Complexity: moderate.
- Theme: good, although it becomes “combine methods” rather than exclusively “change after failure.”


Classification: materially stronger.


It removes failure fishing by making success equally compatible with damage, not by reducing the feature.


Recommendation: second serious playtest choice if retaining control-first play is important.


### Candidate 3 — Free Positional Recovery


Concept:


Once per Attack action after a damaging attack misses or control is resisted, choose one:


- Move up to half your Speed without provoking from that target.
- Stand from Prone without spending movement.
- Move 5 feet and take cover behind an existing suitable obstacle; gain no invented cover or Dodge benefit.


No additional attack.


Expected value:


There is no fixed DPR contribution. It can preserve later attacks, escape a dangerous position, or remove a movement cost.


It does not generally replace the value of current damage plus control insurance.


Behavior:


- Melee/ranged: broadly accessible.
- Control incentive: the refund is positional rather than damage, but speculative control can still purchase escape.
- Action Surge: potentially two recoveries.
- Mastery: no generated attack.
- Studied Attacks: preserved for the next normal attack.
- Graze: can coexist.
- Feats: overlaps mobility options; less pressure on attack feats.
- Bonus Action/Reaction: neither consumed.
- Scaling: terrain dependence rather than attack damage.
- Routine: miss → disengage/reposition.
- Risk: repeated kiting, especially with forced movement.
- Complexity: low.
- Theme: excellent survivor theme.


Classification: materially weaker in ordinary combat; stronger in particular positional emergencies.


Verdict: useful ingredient, insufficient standalone replacement under your governing principle.


### Candidate 4 — Reaction Backup Attack


Concept:


After a damaging attack misses during your Attack action, spend your Reaction for an immediate different-method attack.


Once per Attack action; the Reaction normally limits it to once between your turns.


Expected value:


Gross attack damage can resemble Candidate 1, but its practical cost includes forfeiting an Opportunity Attack, defensive Reaction, or Lesson use.


Behavior:


- Melee/ranged: both supported.
- Grapple/Shove: save-only refund removed.
- Action Surge: normally cannot produce a second response without another Reaction.
- Mastery: normal.
- Studied Attacks: applies, potentially displacing future Advantage.
- Graze: choose either miss damage or response.
- Feats: conflicts with Polearm Master’s Reactive Strike and Sentinel-style reactions.
- Bonus Action: free.
- Scaling: competing Reactions often become more valuable.
- Routine: use when no better Reaction is expected.
- Risk: low.
- Complexity: low.
- Theme: immediate, but mechanically awkward to charge your defensive readiness.


Classification: materially weaker for Reaction-focused builds; approximately comparable when the Reaction would otherwise go unused.


Verdict: preferable to the Bonus Action proposal for some builds, but unnecessary as the default.


### Candidate 5 — Change the Target


Concept:


Once per Attack action after missing with a damaging attack:


- Make a free immediate attack against a different creature.
- The same weapon is permitted.
- Alternatively, make an Unarmed Strike against the original creature.
- No resisted-control refund.


Expected value:


Against multiple enemies, it can generate a full normal weapon attack. Against an isolated distant boss, it provides no ranged response.


Behavior:


- Melee: strike another opponent or use the current unarmed fallback.
- Ranged: redirect fire without drawing another weapon.
- Grapple/Shove: no failure fishing.
- Action Surge: second response allowed.
- Mastery: normal; Cleave remains independently limited.
- Studied Attacks: Advantage earned against the first creature does not transfer to the second.
- Graze: choose miss damage or response.
- Feats: supports ordinary attack routines without action competition.
- Scaling: stronger with larger weapon/rider damage.
- Routine: attack the priority enemy; redirect a miss when another target matters.
- Risk: target selection can become damage distribution rather than adaptation.
- Complexity: low.
- Theme: credible, but changes target rather than method.


Classification: stronger in some circumstances / weaker in others.


Verdict: a good distinct alternative, but inadequate ranged boss support keeps it behind Candidates 1 and 2.


## G. Comparison table


| Version | Response cost | Ranged support | Failure-fishing repair | Surge allowance | Relative practical power |
|---|---|---|---|---|---|
| Current | Free | None from ranged misses | None | Two | Reference |
| Previous Bonus Action Backup Method | Bonus Action | Yes, with equipment limits | Partial; refund survives | One | Often materially weaker; improves ranged access |
| 1. Different-Method Fallback | Free | Yes, with equipment limits | Removes save-only refund | Two | Stronger in some cases / weaker in others |
| 2. Outcome-Neutral Transition | Free | Yes | Removes preference for control failure | Two | Materially stronger |
| 3. Positional Recovery | Free | Yes | Partial | Two | Usually materially weaker |
| 4. Reaction Backup | Reaction | Yes | Removes save-only refund | Usually one | Build-dependent, often weaker |
| 5. Change the Target | Free | Yes against multiple targets | Removes save-only refund | Two | Stronger in some cases / weaker in others |


The Bonus Action version has another material issue: moving the attack outside the Attack action changes eligibility for features such as Grappler and Great Weapon Master. Its cost is therefore more than simply spending the Bonus Action.


## H. Recommended direction


Playtest Candidate 1 first. Preserve the free response, per-Attack-action frequency, and normal Mastery.


Its central exchange is:


- Remove speculative standalone control insurance.
- Add genuine ranged participation.
- Let damaging Unarmed Strikes transition into weapons.
- Allow full weapon alternatives.
- Prevent stacking the response with damage from the triggering miss.


This is a redistribution and, for several builds, an increase in power. That is acceptable to investigate because current ordinary damage does not establish a need for a nerf.


Do not introduce once-per-turn, Bonus Action, and Mastery restrictions simultaneously. That would obscure which change solves which problem.


Candidate 2 deserves testing alongside it because it answers your question through a different principle: make successful control desirable instead of penalizing the response.


### What “different method” should mean


| Definition | Assessment |
|---|---|
| Different physical weapon | Too easy to satisfy with identical copies; weak thematic distinction |
| Different weapon kind | Best balance of clarity and usability |
| Different Mastery | Complicates Tactical Master and excludes useful loadouts |
| Melee versus ranged | Too restrictive |
| Weapon versus Unarmed Strike | Clear but reproduces current narrowness |
| Different target | Clear alternative, but fails isolated ranged encounters |


“Different kind” means longsword versus handaxe, not longsword A versus longsword B.


Longbow versus shortbow is a modest distinction, but enforcing a more elaborate difference would create more tracking than it earns. Most practical differentiation will come from range, damage, Mastery, and equipment.


### Drawing and stowing


The Attack action permits equipping or unequipping one weapon for each attack within it. Thrown weapons also have drawing support. Neither rule automatically makes every two-handed weapon transition convenient.


Both leading candidates should explicitly permit stowing the opener and drawing the fallback. This does not permit donning or doffing a shield, bypass Loading, create ammunition, or ignore occupied hands.


Crossbows and firearms retain their normal restrictions. A fallback that is part of the same Attack action does not reset Loading.


## I. Publishable wording for the two strongest candidates


These are proposed rules text for testing, not accepted replacements.


### Candidate 1: Change the Plan — Different Method


Level 3: Change the Plan


Once during each Attack action you take on your turn, immediately after you miss a creature with a weapon attack or with the Damage option of an Unarmed Strike, you can make one additional attack against that creature as part of the same action.


If the missed attack used a weapon, the additional attack must use a different kind of weapon or an Unarmed Strike. If the missed attack was an Unarmed Strike, the additional attack must use a weapon.


Before making the additional attack, you can stow the weapon used for the missed attack and draw the weapon used for the additional attack.


If you use this response, the missed attack deals no damage, including damage from the Graze property.


An attack made with this feature, and any Grapple or Shove attempt included in that attack, can’t trigger this feature.


Rules implications:


- “One additional attack” permits normal Unarmed Strike options.
- Damaging Unarmed Strike misses qualify; resisted control does not.
- Mastery operates normally.
- The additional attack is explicitly within the Attack action.
- No extra movement is included.
- All normal reach, range, equipment, and weapon restrictions apply.


### Candidate 2: Change the Plan — Follow Through


Level 3: Change the Plan


Once during each Attack action you take on your turn, you can use one of the following responses:


Different Method. Immediately after you miss a creature with a weapon attack, you can make one additional attack against that creature with a different kind of weapon or an Unarmed Strike. If you use this response, the missed attack deals no damage, including damage from the Graze property.


Follow Through. Immediately after resolving a Grapple or Shove attempt made in place of one of the attacks normally granted by that action, you can make one weapon attack against that creature, whether it succeeded or failed on its saving throw.


An additional attack made with this feature is part of the same Attack action. Before making it, you can stow one weapon you are holding and draw the weapon used for the attack.


An attack made with this feature, and any Grapple or Shove attempt included in that attack, can’t trigger this feature.


Rules implications:


- Follow Through does not trigger from Grappler’s additional grapple attached to a damaging hit.
- It does not trigger from the fallback Unarmed Strike.
- Successful control can enhance the follow-up attack through positioning or an applicable feat.
- This deliberately gives damage-preserving control once per Attack action.


## J. Playtest plan


Test the current version, Bonus Action version, Candidate 1, and Candidate 2 using the same encounter and build.


Use Fighter 3, 5, 11, 13, and 20. At level 20, test both with and without the capstone’s designated-target Advantage.


### Required builds


- Sword-and-board.
- Great Weapon Master with greatsword/maul.
- Polearm Master.
- Nick plus Dual Wielder.
- Longbow with backup shortbow/thrown weapon.
- Crossbow and firearm with applicable Loading support.
- Unarmed Fighting/Grappler.
- Representative Fighter 3 multiclass builds.


### Required encounters


| Test | What it reveals |
|---|---|
| Isolated durable enemy | Boss damage, control frequency, ranged usability |
| Several weaker enemies | Target switching, Cleave, damage distribution |
| High AC, weak control saves | Whether adaptation chooses the correct defense |
| Moderate AC, strong control saves | Current failure-fishing behavior |
| Narrow passage | Grapple, prone, reach, equipment constraints |
| Open terrain | Ranged fallback range and movement |
| Active damaging area | Whole-party forced-movement amplification |
| Surprise/poor starting position | Whether the feature helps recovery |
| Long sequence without rests | Value of unlimited availability |
| Short day with frequent rests | Comparison with resource-heavy alternatives |


### Record


- Trigger opportunities and responses used.
- Damage from generated attacks.
- Net damage after displaced Advantage and miss damage.
- Successful control and its actual consequences.
- Bonus Actions or Reactions displaced.
- Weapon switches and adjudication delays.
- Times the player chose an unlikely control attempt primarily for the refund.
- Times the feature was unavailable because of range, Loading, hands, or equipment.


### Decision indicators


| Observation | Response |
|---|---|
| Candidate 1 encourages intentionally inferior opening attacks | Restrict the specific interaction; inspect Graze, accuracy disparity, and riders first |
| Candidate 1 works for melee but fails routine ranged turns | Revise loadout/range support before reducing damage |
| Candidate 2 produces a control attempt every action without meaningful choice | Structural redesign; its outcome neutrality solved fishing but created mandatory control |
| Hazard movement dominates encounter results | Assess party combination and frequency; do not treat it as ordinary DPR |
| Bonus Action version is repeatedly skipped for existing attacks | Confirm overcorrection |
| Mastery repeatedly supplies excessive additional control | Identify which property and encounter pattern; avoid a blanket ban first |
| Feature takes longer to adjudicate than resolve | Simplify method/equipment wording |
| Feature matters only at low levels | Inspect high-level Advantage saturation and fallback value |
| Ordinary free response remains satisfying without determining every turn | Successful result |


## K. Source quality and limitations


Officially supported: revised attack structure, Unarmed Strike choices, weapon handling, Mastery properties, Fighter progression, relevant feat conditions, and published errata.


The current errata changes Grappler’s movement wording and clarifies grapple release; it does not replace Punch and Grab with automatic control. [15]


Mathematical results: trigger probabilities, damage-refund equations, useful-result probabilities, and the stated Studied Attacks example.


Optimization assumptions: chosen accuracy/save rates, usable backup weapons, repeated same-target attacks, and available environmental combinations.


Design judgments: whether speculative control feels unhealthy, whether weapon-kind switching expresses adaptation, and whether Candidate 2’s routine control is desirable.


Important limitations:


- No table playtests were performed.
- No encounter-weighted monster dataset was used; the save rates are sensitivity tests.
- Full weapon fallbacks can be substantially stronger with magic weapons or per-hit riders.
- The current feature’s “part of the Attack action” status needs explicit wording.
- Official subclass access was incomplete, so the Fighter subclass comparison is qualitative rather than a complete numerical ranking.
- Movement into damaging areas requires spell-specific timing checks; there is no universal forced-movement damage formula.
- Neither recommended candidate eliminates every conceivable incentive to arrange a miss. The relevant test is whether deliberately worse play becomes reliably better overall.


Recommendation: retain the free response and test Different Method against Follow Through. The evidence supports repairing the reward structure; it does not support treating a Bonus Action tax as necessary.


## Sources


[1] D&D Beyond — Revised Character Classes:
https://www.dndbeyond.com/sources/dnd/br-2024/character-classes


[2] D&D Beyond — Revised Rules Glossary:
https://www.dndbeyond.com/sources/dnd/br-2024/rules-glossary


[3] D&D Beyond — Grappler:
https://www.dndbeyond.com/feats/1789147-grappler


[4] Roll20 — Great Weapon Master, 2024:
https://roll20.net/compendium/dnd5e/Feats:Great%20Weapon%20Master?expansion=32231


[5] Roll20 — Dual Wielder, 2024:
https://roll20.net/compendium/dnd5e/Feats:Dual%20Wielder?expansion=32231


[6] Roll20 — Polearm Master, 2024:
https://roll20.net/compendium/dnd5e/Feats:Polearm%20Master?expansion=32231


[7] D&D Beyond — Revised Equipment:
https://www.dndbeyond.com/sources/dnd/br-2024/equipment


[8] D&D Beyond — 2024 Fighter vs. 2014 Fighter:
https://www.dndbeyond.com/posts/1746-2024-fighter-vs-2014-fighter-whats-new


[9] Roll20 — Revised Monk:
https://roll20.net/compendium/dnd5e/Classes:Monk?expansion=33335


[10] Wizards of the Coast — SRD 5.2.1:
https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf


[11] Roll20 — Revised Ranger:
https://roll20.net/compendium/dnd5e/Classes:Ranger?expansion=33335


[12] Roll20 — Revised Paladin:
https://roll20.net/compendium/dnd5e/Classes:Paladin?expansion=33335


[13] Roll20 — Revised Sorcerer:
https://roll20.net/compendium/dnd5e/Classes:Sorcerer?expansion=33335


[14] D&D Beyond — Revised Spell Descriptions:
https://www.dndbeyond.com/sources/dnd/br-2024/spell-descriptions


[15] D&D Beyond — Player’s Handbook Errata:
https://www.dndbeyond.com/sources/dnd/sae/players-handbook


Project sources reviewed:
- /DnD Homebrew/Veteran_Current_State_Addendum_2026-09-30.md
- Veteran_Work_Context_Pack.md
- VETERAN FIGHTER SUBCLASS — MASTER PROJECT HANDOFF.md
- PROJECT EVOLUTION TIMELINE.md
- Veteran.md (Iteration D.4.1)
- Veteran_Fighter_Design_Investigation_2026-09-30.md