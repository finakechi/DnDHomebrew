# Veteran Fighter — Deep Research and Critical Design Audit

Use Deep Research to determine the strongest design direction for my **Veteran**, a homebrew Fighter subclass for **D&D 2024 / 5.5e**. This is a critical design-and-balance investigation, not merely a wording pass or an instruction to preserve the current draft.

## Primary objective

Determine whether the Veteran’s current architecture, mechanics, and identity are worth retaining; identify balance problems, exploits, weak or redundant mechanics, and thematic gaps; research overlooked design space; and recommend the strongest next design direction.

Be skeptical and evidence-driven. Do not assume the subclass is good because I like the concept, and do not change functioning mechanics merely for novelty.

## 1. Reconstruct the current project state first

Before evaluating the subclass, review the relevant project chats and files, especially:

- **Homebrew Veteran Fighter Subclass**
- **Veteran Fighter Subclass Design**
- **VETERAN FIGHTER SUBCLASS — MASTER PROJECT HANDOFF.md**
- **PROJECT EVOLUTION TIMELINE.md**
- **Veteran Fighter Subclass: Design, Balance, and Optimization Research Report**
- **Veteran.md / Iteration D.4.1**
- any newer Veteran notes, files, or decisions in this project

Use this authority order when sources conflict:

1. My newest explicit decisions.
2. Decisions made after the Master Project Handoff.
3. The Master Project Handoff’s accepted/provisional state.
4. The most recent accepted feature wording.
5. D.4.2 wording for features not later changed.
6. D.4.1 for unchanged material.
7. Prior research conclusions.
8. Older brainstorming or rejected drafts.

Start the report with a concise **current-state reconstruction** separating:
- accepted mechanics;
- provisional mechanics;
- unresolved design questions;
- rejected/superseded mechanics;
- historical material that is useful only as inspiration.

Do not resurrect a rejected mechanic simply because it appears in an older complete draft.

## 2. Preserve the intended fantasy

The Veteran is an **experienced front-line soldier, campaigner, and survivor** whose strength comes from accumulated experience, fieldcraft, preparedness, observation, adaptability, practical violence, equipment use, dirty tricks, timing, and knowing what to do when a plan fails.

The Veteran is not meant to become:
- a Warlord or officer;
- a noble/famous champion;
- a magical or supernatural warrior;
- a Rogue substitute;
- a Ranger with military flavor;
- a Bard-like support character;
- a Cavalier/Sentinel lockdown specialist;
- an Eldritch Knight without spells;
- or simply a Battle Master with a different maneuver list.

Some mechanical overlap is acceptable. Judge the **overall play pattern and identity**, not superficial similarities.

## 3. Treat the current architecture as testable, not sacred

The current design centers on **Hard-Won Lessons**, with other features expressing readiness, adaptation, fail-forward combat, and veteran experience.

Investigate the current versions and interactions of:
- **Practical Experience** / the current level-3 fieldcraft feature;
- **Hard-Won Lessons** and the current Lesson roster/progression;
- **Change the Plan**;
- **Battlefield Readiness**;
- **Been Here Before**;
- **No Lesson Wasted**;
- **Veteran of a Hundred Fights**;
- and any later accepted changes found in the project chats.

Key architectural questions:
- Is Hard-Won Lessons actually the right core system?
- Does the Lesson menu produce meaningfully different Veterans in play?
- Are evergreen Lessons crowding out niche Lessons?
- Do recall/swap mechanics make permanent niche selections irrational?
- Is Change the Plan genuinely “fail-forward adaptation,” or mostly disguised attack multiplication?
- Has Unarmed Strike/Grapple become too central to a broader Veteran concept?
- Does Battlefield Readiness create real first-round choices, or collapse into a routine default?
- Is the subclass overly melee-focused, and can a ranged Veteran fit the same fantasy?
- Does the subclass create tactical decisions or mostly passive numerical superiority?
- Are there too many independent mechanical theses competing for attention?
- At high levels, does mundane expertise still feel exceptional without becoming supernatural?

Do not automatically solve problems with more attacks, damage dice, reactions, free actions, or feature stacking.

## 4. Research the 2024 Fighter design space

Use current sources and clearly distinguish **2024/5.5e rules** from 2014 material.

Prioritize:
1. official rules, errata, SRD material, and official D&D Beyond/Wizards explanations;
2. reliable rules and optimization analysis;
3. well-reasoned community play experience.

Research the Fighter chassis wherever relevant, especially:
- Weapon Mastery;
- Fighting Style;
- Second Wind / Tactical Mind;
- Action Surge;
- Tactical Shift;
- Extra Attack progression;
- Tactical Master;
- Studied Attacks;
- Indomitable;
- relevant high-level Fighter features.

A central question is:

> What mechanically distinctive territory remains for the Veteran now that the 2024 Fighter is already much more tactical and adaptable?

## 5. Benchmark against official Fighter subclasses

Compare the Veteran with relevant current official Fighter subclasses, at minimum:
- Battle Master;
- Champion;
- Eldritch Knight;
- Psi Warrior;

and use older compatible subclasses such as Cavalier, Samurai, Rune Knight, or others when they provide useful comparison points.

Do not compare only DPR. Compare:
- sustained damage;
- nova potential;
- defense;
- control;
- mobility;
- action and reaction economy;
- resource dependence;
- exploration and information utility;
- social utility;
- adaptability;
- reliability;
- build diversity;
- complexity and table burden.

The goal is not for the Veteran to outperform every subclass. Evaluate whether its **total package, costs, limits, and niche** are appropriate.

## 6. Perform quantitative and exploit analysis

Use transparent assumptions and actual math where practical.

Test important Fighter levels, especially **3, 5, 7, 10, 11, 13, 15, 18, and 20**.

Use several representative builds rather than one optimized character, including where relevant:
- sword-and-board;
- heavy two-handed weapon;
- polearm;
- dual wielding;
- ranged;
- Unarmed Strike/Grapple.

For **Change the Plan** and other relevant features, examine:
- activation probability;
- expected value;
- sustained and nova DPR;
- Advantage/Disadvantage;
- Action Surge;
- Weapon Mastery, including Graze where relevant;
- Studied Attacks;
- Grappler and other relevant feats;
- Fighting Styles;
- Extra Attack;
- weapon swapping;
- reach and positioning;
- multiclass dips;
- recursive triggers and action-economy abuse.

Act like an optimizer trying to break the subclass. Audit current 2024 feats and multiclass combinations for:
- attack multiplication;
- reaction abuse;
- Advantage loops;
- forced-movement/control loops;
- Weapon Mastery stacking;
- Ready interactions;
- Magic-action loopholes;
- wording ambiguities.

Classify serious interactions as:
- theoretical/impractical;
- situationally powerful;
- strong but acceptable;
- likely balance problem;
- primarily a wording problem.

Also account for **opportunity cost**. Search, Study, Help, Dodge, Ready, Utilize, Dash, and similar actions can cost a Fighter multiple attacks at higher levels; do not treat non-damage actions as free or assume all utility can be converted cleanly into DPR.

## 7. Research overlooked Veteran design space

Research real historical and practical experience of rank-and-file soldiers, mercenaries, guards, sailors, caravan hands, frontier fighters, and similar working combatants for inspiration.

Look beyond combat technique alone. Explore areas such as:
- marching and fatigue management;
- watch and sentry routines;
- ambush recognition;
- terrain and route reading;
- camp discipline;
- cover and fortifications;
- logistics and rationing;
- equipment maintenance and improvised repair;
- field medicine;
- weather and survival;
- threat recognition;
- fighting in confined or disadvantageous conditions;
- mundane objects, breaching, sabotage, and preparation;
- prisoner handling;
- recognizing morale or behavioral shifts;
- interacting with other working soldiers;
- recovering from failed tactics;
- conserving effort;
- recognizing familiar patterns in unfamiliar threats.

These examples are not exhaustive.

The goal is to find **mechanical fantasies that feel obvious in retrospect but are missing now**. Do not simply turn every historical skill into a skill bonus.

## 8. Generate and filter new mechanics

Create a substantial idea bank across:
- combat;
- defense;
- mobility;
- reactions;
- preparedness;
- first-round behavior;
- fail-forward mechanics;
- equipment/environment interaction;
- exploration;
- information gathering;
- social interaction;
- teamwork without command;
- survival/fieldcraft;
- high-level veteran mastery.

For each promising concept, identify:
- fantasy expressed;
- action/resource used;
- appropriate level;
- Fighter-chassis overlap risk;
- other-class/subclass overlap risk;
- balance risk;
- complexity/table burden;
- whether it deserves further development.

Then aggressively shortlist. I prefer a smaller number of strong concepts plus explicit rejected ideas over a large undifferentiated list.

## 9. Identify the subclass’s unique mechanical thesis

Give a concise answer to:

> **What does the Veteran mechanically do that no other Fighter subclass does?**

Do not answer only with flavor words such as “experienced,” “tactical,” or “adaptable.”

Determine whether the Veteran’s primary gameplay thesis should be:
- enhanced universal actions;
- recovering from failure;
- beginning combat already prepared;
- changing tools when a tactic fails;
- dynamically adapting a learned toolkit;
- exploiting mundane battlefield features;
- or another better-supported concept.

If several theses are competing, identify which should be primary and which should be supporting.

## 10. Develop competing directions

After the research, present **2–3 coherent design directions**.

At least one should be a conservative refinement of the current architecture. More substantial alternatives are appropriate if the evidence supports them.

For each direction, explain:
- core gameplay loop;
- mechanical identity;
- level 3 / 7 / 10 / 15 / 18 skeleton;
- role of Hard-Won Lessons;
- role of Change the Plan or its replacement;
- strengths and weaknesses;
- complexity;
- optimization risk;
- thematic strengths;
- what survives and what is cut.

Do not merge every good idea into one overloaded compromise.

## 11. Recommend the next design pass

After the analysis, provide:

### A. Keep / revise / replace / cut / test
Classify every major current mechanic and explain why.

### B. Recommended level structure
Give the recommended level **3 / 7 / 10 / 15 / 18** architecture before presenting polished rules text.

### C. Candidate mechanics
Give concrete mechanics for the strongest new ideas.

### D. Sample revised wording
Provide clean 2024-style wording for changes you strongly recommend.

### E. Optional full next draft
If the research establishes a clearly superior direction, provide a complete next Veteran draft after the analytical sections. Keep it separate so individual conclusions can be accepted or rejected independently.

## 12. Build a playtest plan

Design tests that stress:
- sustained and nova combat;
- single boss and multiple enemies;
- melee and ranged play;
- grappling;
- cramped/open terrain;
- surprise and ambush;
- Search and Study;
- exploration and social utility;
- niche Lesson selection;
- Action Surge;
- Weapon Mastery;
- common feats;
- high-level capstone behavior.

For uncertain mechanics, define practical indicators for:
- too strong;
- too weak/irrelevant;
- dominant choice;
- trap option;
- acceptable;
- needs redesign rather than numerical tuning.

## Evidence and reporting standards

Use citations/source links throughout.

Clearly label the basis of important claims as appropriate:
- RAW / official rules;
- likely RAI or official explanatory material;
- mathematical result;
- historical evidence;
- optimizer assumption;
- community experience;
- design judgment.

Prefer primary sources. Do not reproduce long copyrighted rules text; paraphrase and cite.

When evidence is ambiguous, say so. When you disagree with prior research, explain why.

## Final report structure

1. Executive Summary
2. Reconstructed Current Veteran
3. Design Goals and Mechanical Thesis
4. 2024 Fighter Design-Space Analysis
5. Benchmark Methodology
6. Quantitative Balance Analysis
7. Feature-by-Feature Audit
8. Hard-Won Lessons Audit
9. Change the Plan Deep Dive
10. Feat / Multiclass / Exploit Audit
11. Official Subclass Comparison
12. Historical/Thematic Research
13. Overlooked Design Space and Idea Bank
14. Competing Design Directions
15. Recommended Direction and Level Structure
16. Candidate/Revised Mechanics
17. Optional Full Next Draft
18. Playtest Plan
19. Highest-Priority Open Questions
20. Sources

The purpose of this research is **not to defend the current Veteran**. It is to determine the strongest version of the concept and the most evidence-supported roadmap for the next design pass.
