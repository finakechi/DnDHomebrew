# Veteran Fighter: Level-3 Combat Identity

## Focused design investigation - September 30, 2026

**Status:** Advisory research and playtest prototypes. Nothing in this report becomes accepted subclass wording without a subsequent design decision.

**Design question:** What best expresses an experienced fighter who knows when conventional technique is the wrong response?

**Evidence labels:** **Rules** means verified revised-game text; **History** means documentary evidence; **Model** means calculation under stated assumptions; **Judgment** means a design recommendation. Bracketed references resolve to the source register in section M. Project documents are distinguished from external sources.

## A. Executive conclusion

**Recommend a compact competence-plus-application package, with genuinely asymmetric melee and ranged applications.** The strongest first playtest is **Practical Fighting**: credible body and unconventional contact attacks, plus a free choice between close work during armed combat and a repositioning shot at another opponent. It asks the player which opportunity is useful, rather than whether a deliberately unlikely grapple is worth attempting.

This recommendation is a direction to test, not a claim that the first numerical draft is solved. Its close branch is deliberately stronger than current Change the Plan's ordinary damage fallback. Its ranged branch has a real limitation: it spreads attacks across opponents. That can make the branch excellent in a crowded battle and unavailable against an isolated distant boss. The experiment must measure that difference rather than disguising it as symmetry.

The runner-up, **Use What Works**, preserves immediate fail-forward play but broadens the alternate method and supplies the competence the present feature lacks. It is a credible option if the proactive package feels too automatic or the ranged target restriction proves unsatisfying. The third finalist, **Keep Fighting**, is a serious attack-independent recovery engine. It can rescue more value than an extra attack when a battlefield obstructs the Veteran, but is materially weaker in uncomplicated stand-and-hit combat. It should not win by being safer.

**Current Change the Plan is not demonstrably overpowered.** Its main defects remain the cheap speculative-control incentive, weak Dexterity-body integration, reach restrictions, and absence of natural distant participation. Its raw ordinary damage contribution is modest; control and free action economy are more consequential. The previous Bonus Action replacement can overcorrect for builds that already use that action. Conversely, a free full weapon retry can be substantially stronger than a small punch. Neither proposition supports a blanket nerf.

The old unarmed concept was principally **too small and disconnected to carry the identity**, rather than an inherently broken idea. A d6 strike is a useful enabling rule when another part of the feature makes body work matter. Alone, it is largely a Fighting Style benefit.

The historical lesson is also narrower than a romanticized story of veterans breaking rules: advanced fighting manuals already integrate blade, hilt, body, distance, and leverage. The Veteran's distinction is **knowing when to change application**, not discovering a technique that trained fighters never knew.

## B. Historical design evolution

### Source authority and scope

The current request explicitly reopens the combat architecture and supersedes the earlier assumption that the project should continue only with Change the Plan. It does not reopen the entire subclass. The September 30 addendum overrides conflicting older drafts. Later accepted decisions outrank the Master Handoff; reports remain advisory. Duplicate uploads were treated as alternate copies, not additional witnesses.

Reviewed project material: current-state addendum; Work Context Pack; Master Handoff; Project Evolution Timeline; Veteran.md; the long chat transcript; D4.2 for historical context; the general design investigation; and the Change the Plan follow-up supplied as a text report. The transcript and timeline establish the design history, while the addendum establishes the latest consolidated state. [P1-P8]

Retained context: Hard-Won Lessons and Practical Experience remain separate level-3 features. Battlefield Readiness remains the later first-turn package. No accepted level-15 Change the Plan upgrade was recovered. This report does not silently restore the old damage upgrade or reaction engine.

| Historical direction | Fantasy and promising element | Recorded objection | Does it still apply? |
|---|---|---|---|
| Tactical Blow / utility-to-damage | Experience connects unconventional actions to combat pressure | Utility was selected mainly to unlock damage; action compression and complexity | Yes. Do not require gratuitous Search, Study, or Utilize actions as attack coupons |
| Finish the Wounded | Recognize and exploit deterioration | Strong but boring; little meaningful choice | Yes. A new condition on generic bonus damage does not solve identity |
| Field-Expedient Fighting | Use available objects, not ideal equipment | Broad improvised/unarmed package was a poor universal level-10 fit and overlapped existing options | Partly. At level 3 it can enable an active identity, but proficiency alone remains too narrow |
| Hard Knuckles | Competent fists and close contact | Generic improved unarmed damage was insufficiently appropriate as a universal feature | Partly. A standalone die upgrade still fails; weapon-integrated application changes its relevance |
| Extra Unarmed Fighting capability | Armed professionals remain effective bodily | Redundancy and a disconnected unarmed build; no evidence of a demonstrated balance failure | Mostly a packaging problem. Granting the entire style also adds grapple damage and a hands-empty incentive |
| Mastery-for-damage | Apply a weapon differently instead of its textbook effect | Still generic damage; unarmed version lacked the same meaningful sacrifice | Yes as the whole feature. A rare resistance workaround could be a small competence clause |
| Pommel, haft, shield, leverage | The tool in hand can serve another purpose | Open adjudication and uncertain weapon/unarmed interactions | Solvable by a closed Unarmed Strike equivalence, with explicit magic and Mastery boundaries |
| Weapon-assisted control | Armed grappling without becoming a wrestler | Free hands, Strength, saving throws, and control value needed definition | Still applies. Do not erase those restrictions accidentally |
| Cheap Shot / Eye Gouge | Immediate opportunism | Blinded was a major effect; literal anatomy narrowed applicability | Yes. A universal eye gouge remains an inappropriate core identity |
| Mandatory weapon/body alternation | Integration rather than separate builds | Awkward at levels 3-4 before Extra Attack | Solvable if the feature supplies its own bounded follow-up; not solved by waiting for level 5 |
| Change the Plan | Immediate response when a method fails | Current control refund encourages cheap speculation; poor ranged and Dexterity participation | The reward structure must change; failure need not remain the central trigger |
| Broad extra reactions | Veteran notices more opportunities | Multiplication and overlap with the earlier vigilance concept | Yes for broad multiplication. A single bounded reaction could be reconsidered, but competes with existing defense |

The retained design DNA is **the tool you have can become the tool you need**. The project's photographer-and-mechanic examples were specifically a correction to mandatory correct-weapon swapping. A longsword used for leverage fits better than a requirement to carry two differently labeled swords. [P2-P5]

Strength/Dexterity questions were not resolved by a canon rule granting Dexterity grapples. This investigation proposes Dexterity for damaging contact techniques, while leaving ordinary control Strength-based. Reopening historical concepts authorizes new implementations, not restoration of old text unchanged.

## C. Historical and practical combat findings

### What the documentary evidence supports

Fiore's *Fior di Battaglia*, dated approximately 1410 in Getty's catalog, is particularly useful because it depicts related combat methods in one body of material. The catalog establishes the manuscript's identity and dating, not statistical battlefield effectiveness. [7]

| Precedent | Documentary evidence | Practical inference | Appropriate game abstraction |
|---|---|---|---|
| Armored sword work | Fiore's armored plays change grip and application; when an attack is ineffective, the text proceeds to turning an opponent or grappling | Armor and contact distance change what can work | Switching from damage to ordinary shove/grapple, not ignoring armor AC |
| Crossguard/pommel applications | Armored material explicitly includes crossguard or pommel use when other applications cannot be made | One object supports different contact methods | A standardized blunt contact attack with defined damage and no inherited sword Mastery |
| Armed grappling | Narrow plays depict arm control, bindings, disarms, and throws amid sword contact | Body and weapon can operate together | A free but bounded Unarmed Strike option during armed combat |
| Shortened distance with a long weapon | Fiore's spear material expressly discusses distance being too close for the intended play | Equipment does not make distance management irrelevant | A kick/haft option at 5 feet, or a movement response; not universal extra reach |
| Leverage and hooking | The sword and poleaxe material uses the weapon to control an opponent rather than only cut | A familiar implement can be repurposed | Optional control using existing size/save restrictions |

The armored-source summary above derives from the translated primary text, not a modern anecdote. The narrow-play and spear findings similarly come from manuscript translations on Wiktenauer. These are serious documentary resources, but translations are interpretive and manuscript promises of devastating success are not experimental proof. [8-11]

### What should not be overstated

Half-swording is supported as a distinct grip/application; it is not a universal permission to negate plate armor. Hilt and crossguard striking is supported; it does not establish that every blow with every weapon butt is especially damaging. The familiar label **Mordhau** belongs to particular German material and should not be casually substituted for all of Fiore's armored methods. This investigation did not independently establish its prevalence across ordinary battlefield troops, so it is inspiration to verify further, not evidence for a universal anti-armor rule.

Shield manipulation is plausible and appears in wider martial traditions, but this source set does not justify a detailed shield-lock subsystem. A shield strike in the prototype is a game abstraction. Likewise, a bow being usable as an emergency contact implement is a practical inference, not a claim that medieval manuals prescribe routinely hitting armored opponents with fragile bows.

No retrieved historical evidence establishes a distinctive veteran archer's repeatable extra-shot technique. The ranged prototype abstracts **movement, changing the available target, and exploiting another opening**. Its balance and identity must stand on game design, not borrowed authority from sword manuals.

These techniques were often part of formal advanced instruction. The fantasy therefore works best as a contrast between rigid reliance on a preferred method and experienced selection among methods. It need not insult training or celebrate recklessness. Nor do elite instructional manuscripts prove how frequently common soldiers performed these actions in chaotic campaigns.

## D. 2024 rules-space audit

### Verified foundations

The following concise audit separates the official rules from prototype exceptions. It reflects the retrieved revised rules and the current accessible errata page; no relevant later amendment was found. [1-6,12-17]

| Topic | Verified rule relevant to the design | Design consequence |
|---|---|---|
| Attack / weapon handling | An attack in the Attack action permits one equip or unequip, before or after it | A two-step switch is easier with another attack; no universal free swap of every item |
| Unarmed Strike | Damage uses Strength; grapple/shove allow the target's choice of Strength or Dexterity save; control DC uses Strength | Dexterity damage requires an explicit exception; Dexterity control is a separate grant |
| Contact limits | Unarmed reach is 5 feet; grapple needs a free hand; control has a size limit | Kicks work with occupied hands; ordinary grapple restrictions remain |
| Improvised weapons | Normally no proficiency, d4 damage, thrown range 20/60; DM can recognize weapon equivalents | Blanket proficiency is useful competence but does not automatically create Mastery |
| Extra Attack | Fighter attacks become 2/3/4 at levels 5/11/20 | A per-Attack-action application is bounded, not one application per individual attack |
| Action Surge | Supplies another action, excluding Magic; later two uses, at most one in a turn | A per-action application can occur twice, not infinitely |
| Tactical Master / Studied Attacks | Level 9 can substitute Push/Sap/Slow; level 13 grants next-attack Advantage after a miss | Extra control menus overlap base Fighter; a punch may consume Advantage better used on a weapon |
| Shield | Revised errata uses Utilize to don or doff | Equipping a weapon is not instantly equipping a shield |
| Ranged combat | Close enemies can impose Disadvantage; normal/long range and ammunition/loading still apply | Movement can recover accuracy; an extra shot cannot ignore Loading or conjure ammunition |
| Thrown weapons | Draw as part of the attack; melee thrown weapons retain their normal ability rules | Javelins remain Strength-based; a feature need not give all thrown weapons Finesse |

**Mastery audit:** Graze deals the attack ability modifier on a miss; Nick relocates the one Light extra attack; Vex supports a later attack on the same target; Push moves a qualifying target 10 feet; Topple uses a Constitution save; Sap affects the next attack; Slow reduces speed 10 feet without accumulating from repeated Slow. These are existing effects, not blank territory for Veteran techniques. [2]

**Feat/style audit:** Unarmed Fighting offers d6, d8 when no weapon or shield is held, and start-turn grapple damage. Tavern Brawler supplies d4, a reroll of 1s, improvised proficiency, and a bounded push. Grappler combines damage with a grapple attempt once per turn and rewards maintaining the grapple. Polearm Master offers a Bonus Action pole strike and a separate reactive strike. Dual Wielder supplies a Bonus Action extra attack after a Light attack; Nick does not itself create another extra attack. Great Weapon Master adds proficiency damage to qualifying Heavy attacks in the Attack action and has a Bonus Action benefit. Heavy ranged weapons can qualify for its damage clause, but the feat requires Strength 13. [4,12-16]

### Occupied mechanical territory

Base Fighter already changes weapon effects, moves with Second Wind, and learns after misses. A new generic Advantage-after-failure feature is redundant. Battle Master already expresses selected special techniques through a resource-bearing maneuver menu. Monk already combines body attacks, Dexterity control, mobility, and escalating unarmed dice; Martial Arts has equipment restrictions. Tavern Brawler already owns basic improvised proficiency and the d4 brawler package. Grappler rewards a sustained grapple plan. [3-5,12-13]

The useful opening is **making ordinary armed combat include another practical application, or restoring meaningful action when circumstances obstruct a preferred method**. Neither requires a second Mastery list or an inexhaustible catalog of trip/disarm/blind maneuvers.

### Important interpretation boundaries

All generated attacks in the publishable prototypes are expressly part of the triggering Attack action. That settles feat timing rather than relying on an inference from immediacy. An Unarmed Strike proxy is not simultaneously a normal weapon attack. A magical sword's attack bonus, damage riders, and Mastery do not automatically apply to a hilt proxy.

Unarmed Fighting and a prototype d6 are alternative damage rules, not added dice. Tavern Brawler's reroll and push can still matter. Two-Weapon Fighting modifies the extra attack of Light, not every additional attack that lacks an ability modifier. A free action feature does not grant another Bonus Action. An Opportunity Attack remains a Reaction; avoiding Opportunity Attacks does not prevent Polearm Master's separately named Reactive Strike.

Firearms in the revised equipment list can use the ranged options if available in the campaign. Loading and ammunition remain restrictions; modern repeating-fire assumptions, optional explosives, and homebrew gun rules are outside this investigation. No prototype grants a universal reload exemption.

## E. Broad mechanical concept exploration

### Design criteria before mechanics

The identity should produce a recognizable recurring decision: **continue the preferred method, apply the available tool another way, or change the circumstances**. A professional should not have to narrate incompetence to activate expertise. A good feature can be proactive because experience recognizes the problem before failure occurs.

Competence and application may be separate clauses if each makes the other useful. Competence alone is too small. Application without competence makes a Dexterity archer's kick or a shield user's contact strike implausibly bad. A huge menu, however, would recreate the discarded universal-action engine.

The following concepts were explored before choosing finalists. Estimates refer to marginal value above the base Fighter, not total character DPR.

### 1. Genuine fail-forward method switch - unified, reactive

After a damaging attack misses, choose another weapon type or body contact for one free follow-up; alternatively reposition. The choice is which genuinely different method is available. Melee can use the weapon in hand as a contact proxy; distant ranged users can change weapon type, or move without requiring a second gun/bow. Strength and Dexterity damage are supported, but control remains Strength. Per-Attack-action use scales through greater trigger availability and Action Surge. Mastery and Studied Attacks apply normally to true weapon attacks. Main routine: trigger the best available full weapon retry. Main exploit: cheap access to an expensive weapon's full riders. Moderate complexity and good theme; much broader than simply adding ranged wording to old Change the Plan, but still failure-centered. **Finalist 2.**

### 2. Integrated contact plus ranged opening - asymmetric, proactive

Competent body/implement contact enables a free ordinary Unarmed Strike during weapon combat. Ranged attacks instead offer a moving shot at another opponent, with an ability-damage limitation. The decision is damage versus control up close, or whether spreading fire improves the situation. Strength controls; Dexterity can damage; normal thrown abilities remain. No Bonus Action tax. More attacks in an action increase tactical sequencing, not uses. Main routines are weapon-plus-body and two-target firing. Grappler, Heavy ranged damage, and magical riders require testing. Moderate complexity; strong mundane identity and useful power. **Finalist 1.**

### 3. Recover the fight - attack-independent

A once-turn free recovery choice: traverse safely, escape one grapple with the ordinary check, or get up and reset weapon handling. The decision concerns circumstances rather than target AC. Both ranged and melee benefit; Strength/Dexterity retain their normal roles. No extra attacks and no failure trigger. Value scales with the attacks saved, especially at 11/20. Main routine becomes repeated safe kiting, not an attack combo. Resembles mobility classes in effect, but restores a front-line fighter's method rather than granting stealth or supernatural travel. Low-to-moderate complexity. **Finalist 3.**

### 4. Two contrasting practical attacks instead of one - unified, proactive

Replace an attack with two standardized d6 applications, each with a different purpose. At range these might be deliberate shot and pressure shot; up close weapon and body. It solves pre-Extra-Attack integration, but remote control quickly becomes another maneuver/Mastery system. If both are merely damage rolls, it is an extra attack disguised as a new term. Heavy properties and magic transfer become exceptions. Medium-high power, high definition burden. Retain the combination insight, not this subsystem.

### 5. Alternate weapon application - proactive

Once an action, trade a weapon's Mastery for a specific alternate application: blunt contact, hooking, or repositioning. Uses the normal attack ability for damage; actual grappling stays Strength unless explicitly changed. Melee is natural; ranged often collapses into cover ignoring or another accuracy bonus. Good resistance workaround, poor primary identity. Repeat routine chooses the numerically best application every time; Tactical Master makes overlap worse at 9. Low-medium power, medium complexity. Keep a closed contact equivalence, not a second Mastery system.

### 6. Additional Unarmed Fighting - passive

Gain the style in addition to the usual one. Easy to explain, does not cost actions, and improves unarmed durability of the concept. Strongest when grappling and holding no weapon, which steers away from armed integration. Ranged users benefit only in emergencies; Dexterity still needs another rule. No exciting recurring decision. Low standalone identity, appreciable build-specific power. Reject as the entire feature; selected equivalent benefits are useful scaffolding.

### 7. Field-expedient equipment action - attack-independent

Once a turn use bounded mundane gear while fighting, or replace an attack with its use. The player lays obstacles, opens routes, or changes tools. Both ranges can benefit; most effects are not ability-based. Scaling depends on the gear, while late attack replacement grows relatively cheaper. Main routine becomes strongest consumable use, including poison/explosive problems. Hard-Won Lessons already affect action selection. A strict object whitelist is publishable but bloated and campaign-dependent. Reject as primary; equipment handling is an enabling clause, not unrestricted free Utilize.

### 8. Distance specialist - asymmetric

Melee can shorten a long weapon's use or attack inside reach; ranged can escape close interference or fire from unfavorable positions. The decision is where to stand, not what die to roll. Supports all abilities without turning Strength functions into Dexterity. Free movement can be powerful; pure removal of common penalties becomes invisible in favorable encounters. Likely routine is ranged kiting and reach disengagement. Good supporting package; inadequate sole feature unless movement is strong and repeatable. Incorporated into finalists rather than selected alone.

### 9. Opportunity response - reactive, enemy-triggered

When an enemy misses, changes distance, or commits to another target, choose one bounded movement or contact response. Ranged response can withdraw or change a firing lane instead of copying a melee riposte. Uses Reaction, so defense and Polearm Master compete. Attack-generation routes interact strongly with Rogue's off-turn Sneak Attack. Strong theme but enemy/DM-dependent activation and resemblance to Battle Master/Sentinel. Reject broad triggers; worth revisiting if turn-based options prove too automatic.

### 10. Practical leverage without an extra attack - proactive control

Once an action, a successful weapon hit enables a grapple/shove save in place of some damage or Mastery. Great melee fantasy and no failure fishing. Ranged needs a different option, because an arrow cannot normally maintain a physical hold. Strength should determine close control; weapon accuracy can remain Dexterity. Likely routine is save control on every hit; Grappler and Topple overlap. Medium-high control value, two rolls, resource-free maneuver resemblance. Less distinct than letting a Veteran integrate ordinary Unarmed Strike options.

### 11. Environmental exploitation - circumstance-triggered

Use cover, walls, cramped space, or nearby obstacles for a bounded effect. Player looks at the map rather than inventory. Both combat ranges can work; ability dependence can remain situational. Repeat value is substantial on detailed maps and near zero elsewhere. Deliberately creating qualifying terrain can become the new failure fishing. Open stunts slow play; closed effects begin duplicating cover and Mastery. Retain environmental flavor and movement interactions, not compulsory environment gating.

### 12. Professional guard / protect the method - attack-independent defense

Choose a stance that trades movement or a tactical opportunity for protection against one incoming attack. Both ranges benefit, no extra attack required. Strong durability could match current power, but generic AC/DR with a new name does not express unconventional expertise. Reaction versions compete; free versions can become unconditional damage reduction. Low table complexity, weak identity, potentially strong power. Reject as primary rather than selecting it for conservatism.

### 13. Standardized unconventional attack - possible shared abstraction

Define one proficiency-based d6 contact attack, use Strength/Dexterity for damage, and label kicks, hafts, shields, and improvised objects with it. Extra Attack supports it. The problem is classification: weapon riders, Grappler, Mastery, magic bonuses, and remote applications need separate answers. It reduces adjudication only if it **uses an existing rules category**. The prototypes therefore use a narrowly defined Unarmed Strike equivalence for contact. They do not introduce a capitalized new attack category or call ordinary archery an unconventional body strike.

## F. Comparative concept table

Ratings are design judgments, not numerical rankings. Practical power is terrain- and build-dependent.

| Concept | Decision / identity | Repeat power | Melee / ranged | Main overlap or risk | Disposition |
|---|---|---|---|---|---|
| Current Change the Plan | Failure -> another method | Moderate damage; meaningful control | Strong melee identity / absent distant branch | Cheap control speculation | Baseline |
| Bonus Action Backup Method | Failure -> spend BA | Build-dependent | Broad if written broadly | Competes with core combat/healing actions | Comparator, not default |
| Practical Fighting | Integrate contact or take another firing opportunity | High at low tier; controlled additional use | Deliberately asymmetric | Automatic punch; Hunter-like split shot; Grappler | Finalist 1 |
| Use What Works | Choose another real method after damaging failure | Moderate to high | Unified rule, different available methods | Weapon-rider optimization; inventory incentives | Finalist 2 |
| Keep Fighting | Remove obstruction or recover position | Low to very high by circumstance | Naturally unified | Kiting; overlap with Tactical Shift | Finalist 3 |
| Two standardized attacks | Use a bounded combination | Medium-high | Remote option is awkward | New subsystem or disguised bonus attack | Do not develop |
| Alternate application | Trade conventional benefit | Moderate | Melee natural; ranged less distinct | Another Mastery system | Ingredient only |
| Extra Unarmed Fighting | Body competence | Low alone, useful support | Melee/emergency | Another Fighting Style | Ingredient only |
| Free equipment use | Change circumstances with gear | Highly variable | Both | Consumable abuse; Lesson compression | Do not develop |
| Distance adaptation | Restore usable distance | Situationally high | Both, asymmetrically | Invisible in favorable situations | Ingredient |
| Enemy-triggered response | Notice a commitment | Medium-high | Both | Reaction competition and Rogue off-turn damage | Reserve direction |
| Weapon-assisted control | Convert contact into leverage | High control | Melee; requires separate ranged effect | Battle Master / Topple / Grappler | Ingredient |
| Environment exploitation | Use battlefield objects | Highly variable | Both | DM dependence and manufactured setup | Flavor, not core gate |
| Practical guard | Protect current method | Potentially high | Both | Generic defensive bonus | Reject as identity |

## G. Three finalists

### Finalist 1: Practical Fighting - proactive asymmetric package

**Prototype concept.** Competence: d6 damaging Unarmed Strikes using Strength or Dexterity; defined contact with a held weapon or donned shield can use Damage/Shove Unarmed rules; improvised proficiency. Application: once during each Attack action on your turn, after a weapon attack, choose a free Unarmed Strike within 5 feet, or, after a ranged weapon attack, move 10 feet safely and attack another creature with a ranged/thrown weapon. The extra ranged attack omits a positive ability modifier from damage. All attacks remain in that Attack action. No recursion.

**A normal turn:** attack with the preferred weapon; assess whether a close target should be struck, displaced, or grabbed, or whether a different distant target and firing position matter. Continue any remaining normal attacks. No intentional miss or sacrificial grapple is required.

**Melee:** sword-and-board uses a kick or shield contact; great weapons use body contact without sacrificing the normal great-weapon attack; polearms can engage a second nearby creature even when their original target is 10 feet away. A free grapple still requires a free hand. A Dexterity duelist gets credible contact damage but does not automatically become an equally good wrestler.

**Ranged:** bow, crossbow, javelin, or permitted firearm can exploit another target and reposition. A distant solitary creature supplies no second target: only the movement part remains available. That is a real cost. A nearby threat permits Close Work even after a ranged weapon attack, and a damaging kick can be used before later ranged shots only if ordinary close-range interference is actually resolved by movement/control.

**Non-attack application:** the ranged choice's movement matters even when another shot is impossible. The feature is nevertheless attack-based overall; it does not pretend to be the attack-independent finalist.

**Scaling:** level 3 gets a self-contained combination, solving the old pre-Extra-Attack problem. At 5 the player can order body/control before a second weapon attack. At 11 there are more opportunities to exploit prone/grapple and more tactical timing. At 13 the body attack may consume Studied Attacks or Vex; timing is an actual choice. At 20 its one additional application remains meaningful, but is a smaller percentage of the Fighter's normal attacks. Action Surge grants a second application, preserving the existing per-action structure.

**Mastery:** ordinary weapons retain it, including the additional ranged shot. Contact proxies do not. Graze can coexist with Close Work because the additional strike is no longer a refund for the same failed method. This increases power; it is not a bug hidden by narrative. Push can move a target out of body reach; Topple can improve later contact accuracy. The player must sequence them.

**Styles/feats:** Dueling/GWM do not add to contact; Archery supports the shot's accuracy; Thrown Weapon Fighting can add its qualifying damage; Unarmed Fighting's damage choice does not stack, although its grapple rider remains; Tavern Brawler can reroll and push; Grappler can combine contact damage and a grapple once per turn. Nick/Light/Dual Wielder/Polearm Master remain additional options rather than competition for the feature's action cost.

**Magic:** the extra true ranged attack can carry a magic weapon's effects; a sword used as an Unarmed proxy cannot. Unarmed-specific magic may enhance body/proxy attacks if its wording applies. This separation avoids copying every magical weapon rider into a shield bash.

**Multiclass:** a three-level Fighter investment can improve Monk attack volume, though armor/weapon restrictions still constrain Martial Arts; Rage can enhance Strength contact damage; Rogue benefits from another chance to deliver one on-turn Sneak Attack with a qualifying ranged weapon, not an extra off-turn Sneak Attack. Damage/contact rules do not confer universal Dexterity control.

**Optimal routine:** early free contact every action, use Grappler when worthwhile, spread ranged attacks while reserving high-value normal attacks for priority targets. The split-target rule can be gamed by making the qualifying attack against a secondary opponent and the extra shot against the priority opponent. This is legal, but commits one real attack to that opponent rather than a nominal failed control attempt.

**Hunter comparison:** Horde Breaker already supplies an additional same-weapon attack against another nearby target, with a once-turn limit and a target not previously attacked that turn. This prototype's ranged option shares that extra-target architecture. Its movement, broader target spacing, per-action timing and reduced ability damage distinguish the implementation, but do not make that overlap disappear. The Veteran's whole package is weapon/contact integration plus opportunistic position; if players experience it mainly as improved Horde Breaker, the asymmetric branch has failed the distinctiveness test. [3]

**Classification: stronger in some circumstances, and materially stronger in common close melee damage/control turns.** It is not numerically equivalent to current Change the Plan. Its merit is a much more direct identity with healthier incentives. Its main risk is an automatic extra punch overtaking the intended tactical choice, and ranged branch inequality. Complexity is moderate: one shared use and two ordinary effect categories.

### Finalist 2: Use What Works - unified reactive package

**Prototype concept.** Same contact competence. Once each Attack action after a damaging weapon attack or damaging Unarmed Strike misses a creature, either make a free different-method damaging attack against that creature, or move up to half Speed without Opportunity Attacks. A different weapon **type**, weapon versus Unarmed Strike, or a held weapon's contact proxy qualifies. Two identical weapons do not. The alternate attack must be in legal reach/range. If the original miss offers Graze damage, choose that damage or this response, not both.

**A normal turn:** attack normally. On a miss, assess the available alternative or change position. No control attempt triggers a free weapon attack. A failed grapple remains an ordinary failed grapple, and a successful grapple remains useful for its own reasons.

**Melee:** a longsword can immediately become hilt contact at 5 feet; a polearm miss at 10 feet cannot magically extend the body strike, but can permit movement or a different weapon. Sword-and-board can use shield contact. Dexterity melee gains a usable fallback. Taking a poor damaging attack can still raise trigger frequency, but costs expected initial damage; it is not the old zero-damage control-refund structure.

**Ranged:** a bow miss permits a dagger/javelin/crossbow alternative if genuinely available and legal, or a safe reposition without an inventory obligation. Two longbows do not qualify. A firearm's Loading still matters. An alternative ranged weapon cannot automatically solve adjacent-enemy Disadvantage; the movement choice may be preferable.

**Scaling:** trigger probability rises with Extra Attack at 5/11/20, subject to Vex/Studied changing accuracy. Level 13 increases follow-up accuracy but may displace Advantage on a better remaining attack. Action Surge gives another per-action chance. Movement uses grow with Surge but remain bounded by two Attack actions, not by attack count.

**Mastery/Graze:** genuine fallback weapons use ordinary Mastery; contact proxies do not. The Graze either/or clause prevents rewarded-miss double recovery, but reduces damage relative to the present Graze-plus-punch interaction. This is a specific trade, not a universal Mastery removal. Tactical Master can alter the fallback weapon's ordinary property.

**Styles/feats:** general weapon styles apply only when the actual attack qualifies. Body competence makes Unarmed Fighting less essential; Grappler is not granted a free grapple by this prototype because follow-ups use Damage only. Tavern Brawler's hit push remains useful. Nick gives more eligible ordinary attacks but only one response per action. Bonus Actions and Reactions remain free for Second Wind, Polearm Master, Dual Wielder, spells, and defense.

**Magic/multiclass:** swapping to a stronger magical weapon after missing with a weaker one is the main weapon-rider concern; arithmetic below tests whether deliberate poor accuracy becomes profitable. Rage and Monk can improve a body response; ranged Rogue gains a second chance to deliver Sneak Attack, once on the same turn. No broad off-turn engine appears.

**Optimal routine:** attack with a credible weapon, use the most valuable legal different method after a miss. Inventory diversity is useful, but a compulsory two-identical-weapons loop is excluded. If the same best fallback is selected on nearly every turn, the feature has adaptation flavor but little actual tactical variety.

**Classification: stronger in some circumstances, weaker in others.** The d6 contact fallback is stronger than an ordinary punch; full weapon fallback and ranged access add power. Removing the failed-control refund and Graze stacking removes specific value. It is approximately comparable for contact-based play with those losses considered, but can be materially stronger for optimized true-weapon retries. Moderate complexity; excellent immediate theme, weaker proactive professional identity than finalist 1.

### Finalist 3: Keep Fighting - attack-independent recovery

**Prototype mechanics for investigation:** gain the contact competence above. Once on your turn, without an action, choose one: **Reposition**, move up to half Speed without Opportunity Attacks and ignore Difficult Terrain during that movement; **Break Contact**, make one ordinary escape check against one grapple; **Reset**, stand from Prone by spending 5 feet of movement and equip or unequip up to two weapons. These are alternatives, not a chain. You must be able to act; movement requires a nonzero usable Speed. Reset is unavailable if you cannot spend its movement. It does not don/doff a shield. Escape uses the existing escape rule and DC, not automatic success.

**A normal turn:** choose the obstruction that matters, recover, then take the best action. A Veteran can Help, Dodge, use a Lesson, or attack after the recovery. This architecture does not require making an attack to justify knowing how to get out of trouble.

**Melee/ranged:** melee reaches a target across rubble, leaves a losing engagement, or escapes a grab without losing its Attack action; an archer establishes a firing lane or exits contact before shooting. Both can reset after being knocked down. Strength and Dexterity do not become interchangeable outside existing escape choices.

**Scaling:** at 3, saving an action means saving one attack or a useful non-attack action. At 5 it may preserve two attacks; at 11/20 three/four. At 13 it does not consume Studied Attacks. Action Surge gives no second recovery because this is once turn. This is a real contrast with current Change the Plan, not an automatic rule simplification applied to all finalists.

**Interactions:** normal Mastery, Graze, magic weapons, Fighting Styles, and feats continue on the subsequent action; the feature does not generate additional Mastery events. Tactical Shift partly overlaps, but has a Second Wind trigger and healing value. Polearm Reactive Strike can still trigger during the movement. Free repositioning makes ranged kiting strong. Carrying a grappled enemy can become hazard transport; normal carrying costs apply, but Grappler can remove them for qualifying targets. Terrain immunity applies only to this movement, not the whole turn.

**Multiclass/overlap:** armored spellcasters and Rogues value free movement or escape; it is a substantial three-level dip benefit. It cannot cast spells, use magic objects, dismiss Restrained, escape magical restraints generally, or grant free Dash/Disengage actions enhanced by other features. It overlaps Monk/Rogue mobility, but neither stealth nor focus-point offense.

**Optimal routine:** Reposition almost every turn when not needing another recovery. This avoids manufactured failure but can create perpetual kiting. Reset and escape are responses to existing adversity; deliberately going prone to use Reset does not grant an additional offensive attack.

**Classification: stronger in some circumstances, materially weaker in uncomplicated combat.** It can exceed current practical value on demanding maps or against grapplers, but passive body competence does not compensate its empty-arena DPR loss. Low-to-moderate complexity. Serious candidate, not the recommendation unless actual campaigns consistently make recovery valuable.

## H. Quantitative, action-economy, and optimization analysis

### Model and limits

Use hit probabilities **p = 0.50, 0.65, 0.80**, and control success **q = 0.25, 0.50, 0.75**. These represent enemy/ability variation, not a claim about the bestiary's average. Fighter ability modifiers are +3 at 3, +4 at 5, +5 at 11/13/20. Base weapon attacks per action are 1/2/3/3/4. Exclude magic, damage resistance, feats, advantage, crits, and control benefits in the first table so the comparison is interpretable. Those exclusions are restored selectively below.

Let **F = 1 - p^n**, the chance at least one of n eligible independent attacks misses. Current ordinary punch contribution is **F p (1+s)**. This is the weapon-miss branch only, and assumes contact remains legal. It is not the entire feature's value. Integrated contact is **p (3.5+s)** per action. A legal alternate d8 weapon fallback is **F p (4.5+s)**. A ranged extra d8 shot without the positive ability modifier is **4.5p**, conditional on a different valid target. These formulas are deliberately additive marginals, not complete Fighter DPR simulations.

| Fighter level | n / modifier | Current punch at 50% / 65% / 80% | Practical contact at 50% / 65% / 80% | Use What Works: d8 fallback at 65% |
|---|---|---|---|---|
| 3 | 1 / +3 | 1.00 / 0.91 / 0.64 | 3.25 / 4.23 / 5.20 | 1.71 |
| 5 | 2 / +4 | 1.88 / 1.88 / 1.44 | 3.75 / 4.88 / 6.00 | 3.19 |
| 11 | 3 / +5 | 2.63 / 2.83 / 2.34 | 4.25 / 5.53 / 6.80 | 4.48 |
| 13 | 3 / +5 | 2.63 / 2.83 / 2.34 | 4.25 / 5.53 / 6.80 | 4.48 |
| 20 | 4 / +5 | 2.81 / 3.20 / 2.83 | 4.25 / 5.53 / 6.80 | 5.07 |

Level 13/20 rows are **pre-Studied baselines**, not the real high-level outputs. Advantage makes misses less frequent, follow-ups more accurate, and their opportunity cost different. Add 0.175 expected critical-die damage to an always-available ordinary d6 contact attack at 5% crit chance; current ordinary punches have no damage die to double. Exact advantage/critical outputs require sequencing, not one multiplier.

### Failed-control incentive, revisited

Current control-first sequence yields expected weapon damage **(1-q)Ew**, control success q, and useful-result probability **q+(1-q)p**. A control attempt trades away only **qEw** expected weapon damage because failure refunds the weapon attack. At q = .25/.50/.75, that damage cost is 25%/50%/75% of one weapon attack. The paradox is that control becomes cheaper to speculate on precisely when it is less likely to work.

If control is worth V in weapon-damage-equivalent terms, the choice's marginal value is **q(V-Ew)**. Deliberately futile control is not automatically a positive-DPR exploit: as q approaches zero the result approaches the ordinary attack. Its unhealthy incentive is cheap option value and minimal punishment for poor method selection, not an infinite damage engine. Neither finalist 1 nor 2 refunds failed control. Finalist 1 offers control because close work is useful, regardless of success; finalist 2 does not trigger on control at all.

### Practical Fighting: damage and control

At p=.65 the close damage is roughly **4.4 / 5.1 / 5.7** after an ordinary d6 crit allowance at levels 3/5/11+. This is clearly more than the current miss-punch damage. It also supplies an optional control attempt without sacrificing a normal weapon attack. At q=.25/.50/.75, the choice offers 25%/50%/75% control success instead of those roughly 4-6 expected damage points. That is a genuine choice when control matters, but damage is the normal default.

The low-tier percentage is significant. A level-3 greatsword attack with +3, p=.65 and a 5% critical chance averages **6.85** before styles or feats. Adding the prototype's **4.40** contact damage raises that simple turn to **11.25**, about **64% above that weapon-only baseline**. Current ordinary miss-punch instead adds .91. At level 5, two greatsword attacks with +4 average **15.00** before styles/feats, and the **5.05** contact attack is about a 34% increment. Those figures explain why low-tier playtesting is essential; the recommended architecture is intentionally powerful, not a numerical repair masquerading as equivalence.

A d6 contact die also stays static while Monk's Martial Arts die grows. The prototype gives an armored, armed Fighter competence, not Monk's complete body-combat engine: it lacks the Monk's Dexterity control grant, focus options and full mobility package. Nevertheless, a Fighter/Monk can combine legal body attacks, so the comparison must count all attacks and enforce the equipment restrictions rather than treating different feature names as protection from overlap. [18]

Successful prone before two later W=12 attacks, p=.65, yields approximately **2 x (.8775-.65) x 12 = 5.46** expected extra damage while contact advantage remains applicable. Multiply by q=.50 for **2.73** before other control benefits and critical changes. Standing costs movement, not automatically the enemy's action; allies' ranged attacks may be impaired. A shove into a damaging area can be worth much more, while a flying or immune target may make control worthless. Do not price all successful shoves at one fixed damage number.

Grappler further changes the choice: a hit can deliver damage and a grapple save, once turn. At p=.65 and q=.50 the joint success probability is .325 without advantage. Maintaining the grapple can improve later attacks; a shield user without a free hand does not receive this benefit merely by narrating a shield hook. Existing feat investment explains additional power, but does not make it negligible.

Ranged d8/d10 follow-up damage at p=.65 is **2.93 / 3.58**, plus crits, with movement and Mastery. A d6 thrown weapon starts at **2.28** before its style/riders. Heavy ranged GWM can add **p x PB**: +1.95 at Fighter 5, +2.60 at 11, +3.25 at 13, +3.90 at 20, if feat requirements and timing are met. Thus a level-20 heavy-crossbow follow-up can exceed 7 expected damage before magic, but Loading can prevent using that same crossbow twice in one action. A longbow has no such Loading restriction.

These gains are against another target. Damage that does not hasten the priority enemy's defeat is not identical to focused damage. Conversely, preventing a second enemy's next turn can be better. Record kills and enemy actions, not only damage totals. Archery raises the modeled p; the table does not secretly include it. Thrown Weapon Fighting and other qualifying riders can partly erase the no-ability-modifier constraint.

### Use What Works: intentional weak attacks

For one initial attack with success a, damage on hit A, and fallback expectation B, the simple total is **aA+(1-a)B**. Its derivative with respect to a is **A-B**. Lowering accuracy becomes beneficial only if the failed method's hit value is smaller than the fallback's expected value. For ordinary same-tier weapons it usually is not. Example: A=9.5, fallback expectation B=.65x12=7.8: accuracy remains valuable. But a weak initial weapon A=4 and a heavily enhanced fallback B=12 reverses that gradient.

The prototype therefore cannot be certified exploit-free by saying the trigger uses damaging attacks. A weak dart followed by an extremely enhanced heavy/magic weapon deserves a dedicated test. Studied Attacks can make B larger after the miss. Weapon availability, range, Extra Attack opportunities, and giving up the better initial attack must be included in a real comparison. If that routine wins repeatedly, fix the weapon fallback boundary rather than imposing a universal Bonus Action cost: test contact-only follow-ups, or a bounded fallback damage rule. Both reduce breadth and need a new comparison.

### Studied Attacks and sequencing

Use p=.65, Advantage hit probability .8775, W=12, body hit damage U=6, no crits/mastery, three or four weapon attacks, one target, no initial Advantage. A two-state calculation gives current ordinary weapon damage **25.09 / 33.68**. Current immediate miss-punch produces **27.72 / 36.54**: net gains **2.63 / 2.86**, smaller than treating every advantaged punch as pure added damage. These are illustrative sequences, not optimized play or the whole current feature.

Practical Fighting can delay its free body attack until after the last ordinary weapon attack, using the last attack as its trigger. In that simple model, a d6+5 body adds roughly **6.08** after three attacks and **6.07** after four, but may consume Advantage that would otherwise carry into the next turn. An early control/body attempt can improve the remaining action, while an early damaging body attack may consume a more valuable weapon's Advantage. Longer encounters require a carried-state model, target changes, and Vex. Those are explicit playtest uncertainties.

Use What Works has the same immediate-consumption problem as current Change the Plan, though a full weapon fallback can make the consumption advantageous. Keep Fighting alters positioning without consuming attack Advantage. None grants another Studied Attacks effect.

### Action economy, Surge, and opportunity cost

| Feature | Ordinary cost | Surge behavior | What competes with it? |
|---|---|---|---|
| Current Change the Plan | Free response, one per Attack action | Two applications possible | Its own other branch; advantageous attack sequencing |
| Bonus Action Backup Method | One BA after eligible failure | One BA total | Second Wind/Tactical Shift, PAM, Dual Wielder, Light without Nick, multiclass BA options |
| Practical Fighting | Free one per Attack action | Two applications possible | Close control versus damage; split-target shot versus contact |
| Use What Works | Free one per Attack action after miss | Two chances possible | Graze; alternate attack versus movement; fallback availability |
| Keep Fighting | Free one per turn | One recovery | Its other recovery choices; position/terrain rather than BA/Reaction |

A BA fallback is not automatically lower DPR in an otherwise unused-action build: a full weapon attack can outperform a punch. It is materially less accommodating in builds already consuming that BA, and does not expand use on Surge. It should be judged against an actual loadout, not described as a universally modest tax.

No finalist creates recursion. Light/Nick/Cleave and feat limits remain their own limits. Generated attacks can interact with those rules if their ordinary requirements are satisfied, but cannot regenerate the Veteran application. Surge makes per-action versions stronger; it does not alone make them broken. Extra Attack from two classes does not stack into extra Attack actions.

### Whole-game envelope at relevant breakpoints

This is context, not an assertion that spellcasting excuses any martial mechanic. The base-class comparisons below are deliberately selective. [3,5,6,17]

| Level | Relevant whole-game comparison | Implication for this feature |
|---|---|---|
| 3 | Fighter subclasses offer persistent critical/athletic benefits or limited specialized combat tools. Barbarian Rage trades uses and setup for damage/resilience; Rogue combines Sneak Attack with flexible movement; Monk combines body offense with focus options. Web supplies area control with a slot, Concentration, saves and escape actions | A useful free body/contact opportunity is meaningful, but well below multi-enemy action denial; low-tier repeatability still needs scrutiny |
| 5 | Extra Attack arrives for several weapon classes; Monk control can deny a turn but costs focus and a hit/save. Paladin spends slots for bursts; Ranger uses Concentration and target management. Fireball supplies an immediate multi-target burst | A 4-6 marginal single-target gain is substantial subclass power, not outside the game's combat envelope |
| 11 | Fighter's third attack makes control-before-remaining-attacks and saved Attack actions valuable. Rogue damage and Monk resources have grown; full casters have sixth-level spells and summons | Terrain recovery can now preserve far more than its movement distance suggests; magic-weapon riders on free attacks need renewed tests |
| 13 | Studied Attacks already improves miss recovery; full casters have seventh-level spells and major control/utility options | Avoid generic post-miss Advantage; measure who consumes the existing benefit |
| 20 | Fighter has four attacks; full casters have ninth-level options but finite slots and concentration limits. Warlock brings repeatable attacks/cantrips alongside rest-based slots and invocations | A bounded additional application remains appropriate in principle; repeatability, focus fire and rider multiplication decide the practical limit |

Wizard/Sorcerer Web and Fireball illustrate control versus burst: Web demands Concentration and enemy failures; Fireball consumes a slot and does not persist as control. Cleric Spirit Guardians and Druid battlefield spells can reward enemy movement, making a shove valuable; those zones still require their own spell expenditure, setup and positioning. Bard control/buffs and broad utility offer encounter-changing value, with limited slots and target/save restrictions. Warlock separates reliable attack output from limited rest-based casting. Paladin buffs and bursts, Ranger sustained effects, Barbarian defenses, Rogue action flexibility, and Monk body/action integration show that subclass value cannot be measured in DPR alone.

For a simple Fireball benchmark, mean damage 28 with a .50 save success rate gives **21 per target** before resistance. Two targets mean 42, but cost the action and a third-level slot; the Veteran adds roughly 5 points to an action it was already taking. Over six useful rounds that repeat contribution is about 30, with much less burst and no area. Over two rounds it is about 10. Comparing the spell to the marginal feature is informative about scale, not a complete class comparison.

Likewise, repeat free contact control is less severe than reliable stun, but a shove into a persistent spell area can convert party resources into large repeated value. Model the combination rather than counting only the Veteran's own damage. Encounter frequency, short rests, target immunities, terrain, concentration disruption and magic-item allocation can reverse rankings.

### Build and exploit checklist

| Build | Practical Fighting | Use What Works | Keep Fighting |
|---|---|---|---|
| Strength great weapon | Strong extra body/control; GWM remains on true weapon attacks | Contact fallback; heavy alternate weapon riders | Preserves approach and Attack action; no new damage |
| Dexterity melee | Credible d6 contact; weaker Strength control intentionally | Credible reactive damage | Position/reset, ordinary escape rules |
| Sword-and-board | Shield/body contact; grapple still needs hand | Same contact route after miss | Weapon reset does not change donned Shield |
| Polearm | Kick only at 5; can choose nearby second opponent | At 10 feet use another weapon or movement | Excellent distance management; Reactive Strike still matters |
| Dual wielding | Body strike adds to existing attacks; BA remains available | More miss opportunities, same shared limit | Movement competes with no attack slots |
| Bow / crossbow | Split shot and move; Loading is real | Alternate type or move | Strong kiting; no new shot |
| Thrown | True ranged branch, normal ability; draw rules help | Different weapon types actually accessible | Recover range, terrain and equipment |
| Firearm | Additional loaded weapon may be required | Different type does not waive Loading | Movement/recovery works without gun exceptions |
| Mixed loadout | Both branches available, one shared use | Most available alternatives, one response | Handling useful at 3 before many attacks |

Actual abuse candidates: enhanced-weapon retry after a deliberately weak attack; ranged Heavy feat damage and magic riders on the free shot; Grappler plus repeated contact and hazard dragging; free movement allowing indefinite ranged retreat; substitute hilt attacks incorrectly inheriting sword effects; treating equipment recovery as permission for free magic-item/poison/explosive use. These are concrete tests, not reasons to ban every interaction.

## I. Recommended architecture

**Start with Practical Fighting, with Use What Works as the alternate playtest arm.** The strongest design insight is competence plus application, not failure plus reward. Body work becomes part of armed combat immediately at level 3. Distant fighting recognizes a different practical problem: changing position and taking another available opponent rather than pretending archery is a remote kick.

The asymmetric package wins on proactive expertise, credible contact competence, and a real move/control/damage decision. It does not win on already-proven numerical balance. Its low-tier melee package is stronger than current miss-punch play, and the ranged choice has uneven availability. Those are the first two things to measure.

Keep its scope compact. Do not add shield AC manipulation, free item use, armor bypass, bonus reactions, damage-type menus, and anti-exhaustion rules to complete an imagined list of veteran experiences. The same fantasy can explain many actions without requiring all of them as mechanics.

If the ranged split-target requirement produces too many empty turns, do not automatically relax it to unrestricted full extra shots. First compare a same-target limited shot, movement-only value, and Use What Works in controlled tests. If melee becomes an automatic damage routine with no meaningful control decisions, test whether contact availability/targeting or the die needs adjustment. Apply the smallest correction to the demonstrated issue.

No separate level-15 damage upgrade is proposed. The later subclass and Lessons should be tested as they currently stand. Preserve the user's accepted sequencing and readiness architecture unless actual overlap becomes evident.

## J. Publishable prototype wording for the two strongest versions

These are mutually exclusive prototypes. The names are provisional; the rules are intended to be table-ready.

### Prototype 1: Practical Fighting

You have learned to use your weapons, your body, and your position as parts of the same fight.

**Practical Contact.** You gain proficiency with improvised weapons. You can use Strength or Dexterity for the attack and damage rolls of your Unarmed Strikes. When you use the Damage option, you can deal Bludgeoning damage equal to 1d6 plus the chosen modifier instead of the strike's normal damage.

While holding a weapon or wearing a Shield, you can use that implement for the Damage or Shove option of an Unarmed Strike against a creature within 5 feet of you. This use counts as an Unarmed Strike rather than an attack with that weapon or Shield, and it gains none of that implement's properties or magical benefits. This feature doesn't change the ability score, free-hand requirement, or size restriction of the Grapple and Shove options.

**Practical Application.** Once during each Attack action you take on your turn, immediately after you make an attack with a weapon, you can use one of these options:

- **Close Work.** Make an Unarmed Strike against a creature within 5 feet of you.
- **Find an Opening.** If the triggering attack was a ranged attack, move up to 10 feet without provoking Opportunity Attacks. You can then make one ranged attack with a weapon that has the Ammunition or Thrown property against a different creature from the triggering attack's target. You don't add your ability modifier to this attack's damage unless that modifier is negative.

An attack or Unarmed Strike made by Practical Application is part of the triggering Attack action and can't trigger Practical Application. All other requirements of the attack or Unarmed Strike still apply.

**Editorial note, outside the feature:** Find an Opening can supply movement even when a second legal attack is unavailable. Its extra shot is not the extra attack of the Light property, so Two-Weapon Fighting does not restore its ability modifier. Actual ranged weapons retain Mastery and other qualifying effects. Loading is not waived. The contact-proxy clause is an explicit homebrew exception to the usual improvised-weapon classification.

### Prototype 2: Use What Works

When your preferred method fails, you can immediately put another method to work.

**Practical Contact.** You gain proficiency with improvised weapons. You can use Strength or Dexterity for the attack and damage rolls of your Unarmed Strikes. When you use the Damage option, you can deal Bludgeoning damage equal to 1d6 plus the chosen modifier instead of the strike's normal damage.

While holding a weapon or wearing a Shield, you can use that implement for the Damage or Shove option of an Unarmed Strike against a creature within 5 feet of you. This use counts as an Unarmed Strike rather than an attack with that weapon or Shield, and it gains none of that implement's properties or magical benefits. This feature doesn't change the ability score, free-hand requirement, or size restriction of the Grapple and Shove options.

**Change Methods.** Once during each Attack action you take on your turn, immediately after you miss a creature with a weapon attack or the Damage option of an Unarmed Strike, you can choose one of the following responses:

- **Another Application.** Make one attack against that creature with a weapon of a different type, or use the Damage option of an Unarmed Strike against it. A weapon attack and an Unarmed Strike are different methods; two weapons of the same type aren't. If the triggering attack was an Unarmed Strike, this response must be a weapon attack.
- **Change Position.** Move up to half your Speed without provoking Opportunity Attacks.

If the missed attack allows you to deal damage with Graze, you can deal that damage or use Change Methods, not both. An attack or Unarmed Strike made by Change Methods is part of the triggering Attack action and can't trigger Change Methods. All other requirements of the attack or Unarmed Strike still apply.

**Editorial note, outside the feature:** Weapon type means the rules entry, such as Longsword or Longbow, not a physical copy or its Mastery property. A contact proxy is an Unarmed Strike, so it differs from the same implement's normal weapon attack. The fallback must be legal from the current position; Change Position is an alternative, not movement followed by the fallback. Ordinary weapon attacks retain Mastery. The fallback cannot choose Grapple or Shove, although a hit can have separately granted feat effects.

## K. Example combat sequences

### Practical Fighting

**Level 3 sword-and-board:** The Veteran makes a longsword attack, hit or miss, and then chooses Close Work. With both hands occupied, a kick or shield contact can deal d6 damage or try to shove, but cannot initiate a normal grapple. Against a dangerous enemy near a ledge, shove can be the useful choice. Against an isolated wounded opponent, damage can be better. No failed control attempt is required first.

**Level 5 great weapon:** Make the first weapon attack. If the foe remains at 5 feet, choose a free shove to knock it prone. The enemy saves using its permitted better ability. On success it stays upright; no refund occurs. On failure, the Veteran's second normal attack can benefit from close advantage. The trade was the free contact damage opportunity, not the first weapon attack.

**Level 5 archer:** Shoot enemy A. Choose Find an Opening, move 10 feet out from beside a blocking opponent or into a better lane, then shoot B without a positive ability modifier on damage. Make the second normal attack as desired. The movement must actually resolve close interference or cover; it does not declare those penalties gone. If only A exists, use movement but make no extra shot.

**Thrown mixed loadout:** Throw a javelin at A, use the permitted draw rules, reposition, and throw another at B. Strength applies normally to the rolls; the extra attack omits its positive ability modifier from damage. The feature does not make a javelin a Dexterity weapon. Alternatively, if a foe is nearby, choose Close Work instead.

**Level 13 sequencing:** After an early weapon miss, retain Studied Attacks for a strong second weapon attack rather than spending it on contact. After the third ordinary attack, use Close Work if a target remains close. If the last weapon missed, the contact attack can use the resulting Advantage, with the acknowledged cost of consuming a benefit that might have survived to the next turn.

**Loading example:** A heavy crossbow has already fired in the action. Find an Opening does not permit another bolt from it despite the extra attack. A legal different loaded weapon may work if hands and equipment handling permit it. A longbow does not face that Loading restriction.

### Use What Works

**Level 3 duelist:** A rapier misses at 5 feet. Use Another Application for a d6 Dexterity kick or hilt proxy. The proxy is not a magical rapier attack and has no rapier Mastery. The same rapier's normal second attack would not qualify simply because it has a new narrative grip.

**Level 3 bow user:** A bow misses at distance. A javelin within legal range or a different ranged weapon can qualify if actually available. If no useful alternate weapon is accessible, choose Change Position and take a safer lane. That response itself does not include another shot.

**Level 5 polearm:** Miss a target 10 feet away. An ordinary Unarmed Strike cannot reach it. Choose another legal weapon method or move. Do not move toward it and then claim both responses. Subsequent normal Extra Attack attacks may use the new position.

**Graze:** A greatsword misses. Choose its Graze damage, or use Change Methods for a different attack/movement response. The prototype prevents stacking the two recoveries from that miss.

**Grapple resistance:** Attempt a normal grapple instead of a weapon attack. The enemy saves. Nothing triggers Change Methods. This is exactly where the old cheap-refund routine ends.

**Action Surge:** In either prototype, a second Attack action creates another shared application opportunity. A generated attack cannot chain the feature. The Veteran still has only one Bonus Action and the ordinary Reaction budget.

### Keep Fighting: investigative examples

A knocked-down archer spends the Reset option and 5 feet of movement, stands and changes weapons, then chooses an action. A grabbed swordsman uses Break Contact, succeeds on the normal escape check, and still attacks; on failure the grapple remains. A fighter crosses rubble with Reposition to reach a foe, preserving the Attack action. None of these requires first attacking an object or deliberately missing.

## L. Playtest plan

### Structure

Use current Change the Plan as the control condition. Run Practical Fighting and Use What Works on the same characters and comparable encounters; run Keep Fighting on a smaller map-sensitive arm. Rotate order to reduce familiarity bias. Do not stack prototypes. Keep other Veteran features fixed.

Test levels **3, 5, 11, 13, 20**. Include Strength great weapon, Dexterity sword-and-board, polearm, dual wielding, bow, crossbow, Strength thrown, Dexterity thrown, and mixed loadouts. Include at least one ordinary-magic-weapon tier and one rider-heavy stress case. A three-level Fighter multiclass test should include Monk, Barbarian, Rogue and a ranged caster/weapon user.

### Encounter matrix

Use six situations: isolated close enemy; isolated distant enemy; multiple spread enemies; cramped/obstructed battlefield; enemies that enter the archer's space; and armor/control-resistant enemies with meaningful objectives. Include a grappling opponent and a persistent damaging area. Run short bursts and longer sequences with and without a short rest between encounters. Use the same enemy save profiles in matched runs.

### Measures

- Marginal damage, priority-target damage, kills before enemy turns, and damage prevented.
- Application frequency, unavailable branches, control attempts/successes, failed-control speculation and deliberate weak-attack setups.
- Actions/Bonus Actions saved, movement actually needed, terrain bypasses, and escape attempts.
- Studied/Vex consumption and whether the player would have preferred the next normal weapon attack to use that Advantage.
- Whether ranged split fire felt like a useful opening or an arbitrary restriction.
- Whether contact control competed with damage, or free punch became the automatic button.
- Resolution time, rule questions, weapon handling errors, and player descriptions of why experience mattered.

### Decision gates

**Keep Practical Fighting** if both ranges obtain substantial practical value, its control choice matters, and riders do not dominate. **Revise its ranged branch** if distant single-target encounters systematically erase the identity; do not dismiss that as merely a preferred build's problem. **Revise contact power** if ordinary low-tier encounters become disproportionately easy without meaningful choice. **Prefer Use What Works** if its immediate switch consistently creates better decisions and its fallback routine remains healthy. **Reject its full weapon fallback boundary** if deliberate weak attacks repeatedly improve expected performance. **Prefer Keep Fighting only on evidence** that preserved actions and position consistently compensate its offensive loss.

There is no predeclared percentage that makes a feature balanced. Review the size of gains, availability, encounter outcomes, party synergies, and reported fun together. A strong feature is allowed to remain strong. The corrective target is the demonstrated routine, not repeatability itself.

## M. Source quality and limitations

### Project evidence

- **P1:** Veteran_Current_State_Addendum_2026-09-30.md. Latest consolidated decision record; explicitly marks Change the Plan provisional.
- **P2:** Veteran_Work_Context_Pack.md. Standalone authority/context summary; not independent evidence where it repeats other records.
- **P3:** VETERAN FIGHTER SUBCLASS - MASTER PROJECT HANDOFF.md, retrieved duplicate copy. Accepted/provisional baseline before later decisions.
- **P4:** PROJECT EVOLUTION TIMELINE.md, retrieved duplicate copy. Chronological design reasons.
- **P5:** Veteran_Fighter_chat_transcript(1).txt. Historical user decisions and discarded concepts.
- **P6:** Veteran.md and D4.2. Older complete/subclass wording where still relevant.
- **P7:** Veteran Fighter: Design, Balance, Optimization, and Thematic Investigation. Advisory general report, not canon.
- **P8:** Veteran - Change the Plan Follow-Up Investigation - 2026-09-30.txt. Advisory focused report, retrieved from the accessible file collection; independently reexamined here.

### External source register

**1. Official revised Rules Glossary:** Attack, equipping/unequipping, Unarmed Strike, improvised weapons, grapple and Opportunity Attack foundations. https://www.dndbeyond.com/sources/dnd/br-2024/rules-glossary

**2. Official revised Equipment:** weapon properties, Mastery, range, thrown, ammunition/loading and equipment entries. https://www.dndbeyond.com/sources/dnd/br-2024/equipment

**3. Official revised Character Classes:** Fighter breakpoints, base-class comparison and Hunter's Horde Breaker. https://www.dndbeyond.com/sources/dnd/br-2024/character-classes

**4. Official Grappler entry:** https://www.dndbeyond.com/feats/1789147-grappler

**5. Official Fighter revision explanation:** useful context for base/subclass territory, not a replacement for exact rule text. https://www.dndbeyond.com/posts/1746-2024-fighter-vs-2014-fighter-whats-new

**6. Official Player's Handbook errata:** retrieved September 30, 2026. https://www.dndbeyond.com/sources/dnd/sae/players-handbook

**7. Getty catalog, Il Fior di Battaglia:** manuscript identity and dating. https://www.getty.edu/cona/CONAFullSubject.aspx?subid=700002326

**8. Fiore, sword in armor:** primary-source transcriptions/translations with manuscript witnesses on Wiktenauer. https://www.wiktenauer.com/wiki/Fiore_de%27i_Liberi/Sword_in_Armor

**9. Fiore, two-handed sword narrow play:** https://www.wiktenauer.com/wiki/Fiore_de%27i_Liberi/Sword_in_Two_Hands/Narrow_Play

**10. Fiore, spear:** https://www.wiktenauer.com/wiki/Fiore_de%27i_Liberi/Spear

**11. Fiore, poleaxe:** https://www.wiktenauer.com/wiki/Fiore_de%27i_Liberi/Poleaxe

**12. Licensed revised PHB reproduction, Unarmed Fighting:** publisher rules hosted by Roll20, not community optimization advice. https://roll20.net/compendium/dnd5e/Feats%3AUnarmed%20Fighting?expansion=32231

**13. Licensed revised PHB reproduction, Tavern Brawler:** https://roll20.net/compendium/dnd5e/Feats%3ATavern%20Brawler?expansion=32231

**14. Licensed revised PHB reproduction, Great Weapon Master:** https://roll20.net/compendium/dnd5e/Feats%3AGreat%20Weapon%20Master?expansion=32231

**15. Licensed revised PHB reproduction, Polearm Master:** https://roll20.net/compendium/dnd5e/Feats%3APolearm%20Master?expansion=32231

**16. Licensed revised PHB reproduction, Dual Wielder:** https://roll20.net/compendium/dnd5e/Feats%3ADual%20Wielder?expansion=32231

**17. Official revised Spell Descriptions:** representative damage, Concentration and area-control context. https://www.dndbeyond.com/sources/dnd/br-2024/spell-descriptions

**18. Official Monk revision explanation:** Dexterity/body integration, equipment restrictions and focus comparison. https://www.dndbeyond.com/posts/1758-2024-monk-vs-2014-monk-whats-new

**19. Official revised Feats:** Fighting Style and origin-feat framework. https://www.dndbeyond.com/sources/dnd/br-2024/feats

### Confidence and what would change the recommendation

**High-confidence rules:** core attack handling, unarmed/contact limits, control saves, Fighter breakpoints, ordinary Mastery, Grappler, and the accessible feat text. Licensed reproductions were used where exact official-site feat text was not readily accessible; they are rules evidence, not forum opinions. Search surfaced many community discussions, but none was treated as official authority.

**Historical confidence:** documented integration and adaptation in the selected manuscripts is strong; battlefield frequency, soldier demographics, and comparative effectiveness are not established. Shield and ranged abstractions are explicitly design choices. A richer primary-source ranged-combat investigation could inspire better options, but is not necessary to establish the proposed game mechanics' legality.

**Model confidence:** the formulas are reproducible expected-value calculations. They are not empirical results. Independence, one target, static accuracy, absence of magic/feats in baseline tables, and fixed control success are simplifying assumptions. The Studied illustration does not optimize every possible timing policy or carry Advantage across encounters. Practical shot value depends heavily on target distribution.

**Design uncertainties:** whether proactive contact feels like experience or routine extra offense; whether split fire belongs sufficiently to Veteran rather than Hunter; whether hilt-as-Unarmed is intuitive; whether body d6 stays satisfying with high-tier magical weapons; how often maps make recovery decisive; and how full weapon fallbacks behave under unusually strong riders. These can materially change which finalist wins.

**Rules boundaries needing explicit text or table agreement:** generated attacks being part of the Attack action is specified in both prototypes; contact proxies inheriting weapon magic is explicitly prohibited; ordinary equipment handling and Loading are not waived. Unarmed-specific items that mention the attack rather than bodily contact should be reviewed individually. Optional firearm, explosive, and homebrew item rules can materially alter extra-attack/equipment abuse and were not certified here.

**Missing empirical evidence:** matched playtests, target-distance/control-resistance distributions in the intended campaign, party spell-area combinations, rest frequency, late-tier item access, and player timing data. The present source set does not support declaring any prototype perfectly balanced or canonically accepted. It does support reopening competence-plus-application instead of treating a Bonus Action nerf as the inevitable solution.
