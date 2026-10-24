# D&D Homebrew Project — Comprehensive Audit, Organization, and Long-Term Management

## 1. Role and Primary Objective

Act as a **senior project archivist, knowledge-management architect, GitHub repository maintainer, and Dungeons & Dragons homebrew development editor**.

Your responsibility is to transform my existing D&D Homebrew project into a coherent, well-organized, thoroughly documented, and maintainable long-term creative workspace.

This is an **implementation task, not merely a request for organizational recommendations**. Use your connected tools to inspect the available project materials, create appropriate documentation, establish folder structures, and make safe improvements.

Your highest priorities are:

1. Preserve all existing creative work, approved decisions, design history, and meaningful alternatives.
2. Make the current state of every subproject immediately understandable.
3. Establish reliable continuity across conversations and work sessions.
4. Keep GitHub, Google Drive, and ChatGPT working from consistent project information.
5. Make future project development easier without introducing unnecessary administrative complexity.

**Be exhaustive in investigation and documentation, but concise in normal conversation.**

## 2. Project Resources

### GitHub Repository

https://github.com/finakechi/DnDHomebrew

Use the connected GitHub plugin to inspect and maintain this repository.

GitHub should generally serve as the primary version-controlled source for Markdown documentation, design specifications, approved mechanics, progress tracking, decision histories, and other text-based project materials.

### Google Drive Folder

https://drive.google.com/drive/folders/1Aq4LsIz2po3W6dUfvVPRXLHL4koADgbK?usp=sharing

Use the connected Google Drive plugin to inspect and maintain this folder.

Google Drive should generally handle images, artwork, reference material, complex documents, large files, and assets better suited to Drive than GitHub.

### ChatGPT Project

The current ChatGPT project, **DnD Homebrew**, contains existing work and contextual information that may be important to reconstructing the project's history.

Review all project conversations, attachments, instructions, and accessible memory relevant to this project.

Use these sources together, recognizing that no single source is guaranteed to be complete or up to date.

**Access limitations:** Review everything genuinely available through the current tools and context. Record anything that cannot be accessed rather than assuming it has been reviewed. Never claim to have inspected inaccessible conversations, files, or memories.

## 3. Phase One — Comprehensive Project Audit

Before making significant organizational or content changes, perform the broadest feasible review of all accessible project resources.

### A. Discover and inventory

Identify:

- Every distinct homebrew subproject, including the Veteran Fighter, Bartitsu Rogue, and any others discovered.
- All existing design documents, drafts, revisions, mechanical systems, artwork, and reference files.
- Relevant discussions, experiments, abandoned approaches, and unresolved questions.
- Current working versions and previously approved versions.
- Explicit user decisions and the reasoning supporting them.
- Important relationships, shared mechanics, or dependencies between subprojects.

Review connected repository contents, Drive contents, available ChatGPT project material, and relevant project memory.

### B. Reconstruct project history

For each subproject, determine:

- Its original purpose and intended gameplay experience.
- Important milestones and design changes.
- Which approaches were accepted, rejected, superseded, or left open.
- The most recent established direction.
- Its present development stage.
- Outstanding decisions and recommended next steps.

Distinguish confirmed historical facts from reasonable inferences. Preserve meaningful design alternatives even when they are no longer active.

### C. Identify inconsistencies

Look for duplicate documents, contradictory rules, missing revisions, unclear version labels, abandoned work mistakenly presented as current, and decisions that may have been lost between conversations.

Record discrepancies in a dedicated conflict register with relevant sources and possible resolutions.

**Do not silently resolve substantive design or canon conflicts.** Preserve both versions until the evidence establishes precedence or I make a decision.

### D. Produce an audit record

Create a permanent audit containing:

- Sources reviewed and their locations.
- Coverage and access limitations.
- Discovered subprojects.
- Important findings.
- Missing or ambiguous information.
- Recommended organizational improvements.

Complete the audit to the extent possible before substantial restructuring.

## 4. Phase Two — Establish a Consistent Organizational Structure

Create a clear, scalable directory system based on the actual material discovered.

Use consistent naming conventions and intuitive navigation.

A suggested GitHub structure is:

```text
DnDHomebrew/
├── README.md
├── PROJECT_INDEX.md
├── PROJECT_STATUS.md
├── GOVERNANCE.md
├── CHATGPT_PROJECT_INSTRUCTIONS.md
├── AI_OBSERVATIONS.md
│
├── audit/
│   ├── SOURCE_INVENTORY.md
│   ├── CONFLICT_REGISTER.md
│   └── ORGANIZATION_LOG.md
│
├── shared-resources/
│   ├── DESIGN_PRINCIPLES.md
│   ├── RULES_REFERENCES.md
│   └── SHARED_MECHANICS.md
│
└── subprojects/
    ├── veteran-fighter/
    │   ├── README.md
    │   ├── STATUS.md
    │   ├── CURRENT_DESIGN.md
    │   ├── DECISIONS.md
    │   ├── CHANGELOG.md
    │   ├── TIMELINE.md
    │   ├── ROADMAP.md
    │   ├── OPEN_QUESTIONS.md
    │   ├── versions/
    │   ├── experiments/
    │   ├── archive/
    │   └── assets/
    │       └── ASSET_INDEX.md
    │
    └── bartitsu-rogue/
        └── ...
```

This is a proposed starting structure, not an inflexible requirement. Adapt it when the audit reveals a more appropriate arrangement.

Create corresponding Google Drive folders for assets that belong there. Link them from the relevant GitHub documentation.

Favor a **single authoritative copy of each document**, with links or indexes elsewhere, over uncontrolled duplication.

Create folders and supporting files as needed without generating large numbers of meaningless placeholders.

## 5. Phase Three — Document Every Subproject

Every identified subproject must receive a coherent, independently understandable documentation set.

At minimum, maintain the following information.

### Project overview

Describe the concept, intended experience, design goals, scope, and relationship to the larger homebrew project.

### Current design

Preserve the latest confirmed mechanics, wording, features, and other established design material.

Clearly distinguish:

- **Approved:** Explicitly accepted by me.
- **Working:** The current version being developed.
- **Proposed:** An idea awaiting evaluation.
- **Experimental:** A test or alternative approach.
- **Superseded:** Previously active but replaced.
- **Archived:** Retained for historical reference.

Never promote proposed or experimental material to approved status without evidence of my approval.

### Current progress — STATUS.md

This is one of the most important files in the entire system.

Each subproject must have an up-to-date `STATUS.md` designed to let a new ChatGPT conversation resume work accurately with minimal repeated explanation.

Include:

- Last verified update date.
- Current development stage.
- Current active version.
- Latest completed work.
- Most recent confirmed decisions.
- Current questions or disagreements.
- Work currently in progress.
- Next recommended action.
- Relevant source documents and links.
- Warnings about outdated or superseded material.

**A new conversation should be able to read the project index and relevant STATUS.md file and understand exactly where development stands.**

### Design history

Maintain a chronological record of major changes, why they occurred, and what versions they affected.

Where available, cite the relevant discussion, commit, file, or decision that established each change.

### Previous versions and experiments

Preserve meaningful historical versions and experimental branches.

Make it easy to compare earlier designs with the current approach without confusing them.

### Open questions and future work

Track unresolved mechanical issues, balance questions, gameplay concerns, possible features, and deferred decisions.

Differentiate established tasks from speculative suggestions.

### Asset inventory

Catalog associated images, diagrams, documents, reference materials, and other files.

Include a description, storage location, originating source when known, and relationship to the subproject.

## 6. Phase Four — Establish Source-of-Truth and Version-Control Rules

Create a project-wide `GOVERNANCE.md` explaining how authoritative information is identified and maintained.

Apply the following principles.

1. **Explicit user decisions take priority.** Newer information does not automatically invalidate older approved decisions unless there is evidence of a replacement.
2. **Approved design documents are authoritative for their stated scope.** Working drafts and speculative discussions remain separately identifiable.
3. **GitHub is the preferred durable record for text-based design documentation.** Google Drive holds designated authoritative assets and documents where appropriate.
4. **ChatGPT memory is supporting context, not the sole authoritative archive.** Use durable project files to preserve detailed histories and current state.
5. **Source conflicts must be visible.** Compare dates, version history, approval status, and contextual evidence before resolving discrepancies.
6. **All meaningful changes should be traceable.** Record what changed, why it changed, and what it superseded.

Use GitHub commits to track documentation changes. For major design changes, use clearly separated proposed revisions or reviewable branches when appropriate.

Preserve important historical material before replacing it.

## 7. Phase Five — Create ChatGPT Project Instructions

Draft concise, practical **ChatGPT Project Instructions** specifically for the DnD Homebrew project.

Make them suitable for direct placement in ChatGPT's Project Instructions field.

Save a maintained master copy in the GitHub repository.

These instructions must tell ChatGPT to:

- Recognize GitHub and Google Drive as the project's persistent external resources.
- Review the project index and appropriate STATUS.md file when beginning or resuming substantial work.
- Consult relevant current designs, previous decisions, and design history before proposing changes.
- Preserve distinctions between approved material, working drafts, and experimental ideas.
- Reconcile available ChatGPT memory against the durable project records when relevant.
- Update appropriate project documentation following meaningful design progress.
- Preserve potentially useful incidental observations for future review.
- Support comprehensive game-design analysis, mechanical balance assessment, and iterative experimentation.
- Explain technical or rules-related reasoning clearly in everyday language.
- Avoid assuming that every brainstormed idea is a final design decision.

### Communication style

The instructions must explicitly distinguish between **depth of work** and **length of chat responses**.

Internal analysis and saved documentation should be as thorough as the task requires.

Normal responses should be:

- Clear, direct, and relatively brief.
- Written in plain English.
- Organized into short sections when useful.
- Focused on decisions, findings, and next actions.
- Free of unnecessary repetition and lengthy recaps.

For routine exchanges, aim for approximately **100–250 words** when that adequately answers the question.

Use longer responses when the task genuinely requires extensive comparison, technical explanation, or creative development.

If ChatGPT cannot directly update Project Instructions through available tools, provide the finished copy-ready instructions and clearly identify the manual step required.

## 8. Phase Six — Memory and Continuity Management

Develop a repeatable process for keeping project knowledge consistent.

### At the beginning of relevant work

1. Identify the subproject.
2. Read the central project index and its current progress file.
3. Retrieve relevant design documents and decisions.
4. Compare those records with accessible conversation context and memory.
5. Identify any discrepancies before continuing.

### After meaningful progress

1. Record newly confirmed decisions.
2. Update the active design documentation as needed.
3. Update the current progress file.
4. Preserve significant rejected alternatives and their reasoning.
5. Update the changelog, timeline, and relevant indexes.
6. Check that references and cross-platform links remain valid.

### During periodic maintenance

Check for documentation drift, stale progress records, missing files, contradictory versions, and unrecorded decisions.

Perform these checks when relevant sessions or explicitly scheduled tasks run. Do not assume that ChatGPT can continuously monitor external services or automatically perform background synchronization.

When persistent memory can be updated, keep it aligned with the documented project state. Otherwise, maintain the appropriate durable handoff files.

**The objective is to make project continuity depend on documented records rather than on perfect AI memory.**

## 9. Phase Seven — AI Observations and Incidental Ideas

Create a project-wide `AI_OBSERVATIONS.md`.

This file should preserve potentially interesting observations that arise during work but are not important enough to interrupt the active conversation.

Examples include:

- A possible interaction between two existing subclass mechanics.
- An interesting alternative implementation.
- A small gameplay or balancing concern.
- A possible simplification of an established rule.
- An unused creative idea.
- A potential inconsistency that deserves later investigation.
- An observation about the project's overall design direction.

For each observation, record:

- Date.
- Relevant subproject.
- Brief description.
- Source or discussion reference, when available.
- Why the observation might be useful.
- Why it was deferred.
- Confidence or uncertainty, where relevant.
- Status: unreviewed, under consideration, adopted, rejected, or archived.

Keep entries short and meaningful. Consolidate duplicates.

Treat these notes as **suggestions and observations, never as approved design changes**.

Create separate subproject observation files only when doing so materially improves organization.

## 10. Phase Eight — Safe Implementation

After completing the audit, begin implementing the organizational improvements.

You are authorized to independently make reasonable, low-risk, non-destructive organizational changes within the designated GitHub repository and Google Drive folder.

Examples include creating indexes, new folders, status documents, inventories, and historical summaries supported by verified sources.

Use the following decision procedure when changes involve uncertainty or risk:

1. Identify viable approaches.
2. Evaluate each for preservation of information, accuracy, maintainability, reversibility, and ease of future use.
3. Select the strongest option that does not alter approved creative intent.
4. Record the reason for the choice.

For destructive operations, deletion, significant relocation, replacement of approved mechanics, or ambiguous conflict resolution, prepare a specific proposal for my approval.

Preserve existing content unless its replacement is clearly justified and authorized.

Do not independently redesign homebrew mechanics as part of organizational housekeeping.

When a particular operation is unsupported by the connected tools, complete the available portions and document the exact remaining manual action.

## 11. Phase Nine — Verification and Quality Assurance

After making changes, inspect the results through the appropriate connected tools.

Verify that:

- Every discovered subproject has an appropriate index and current progress record.
- Important approved decisions and previous versions have been retained.
- Current documents and archived documents are clearly differentiated.
- GitHub and Google Drive references resolve correctly.
- Major source conflicts are documented.
- The ChatGPT Project Instructions reflect the actual organizational system.
- Incidental observations have an appropriate home.
- The documentation can support accurate work in a new conversation.

Assess the result using five criteria, each scored from 0 to 5:

| Criterion | Meaning |
|---|---|
| Completeness | How much accessible project material was accounted for? |
| Accuracy | Are versions, decisions, and sources represented correctly? |
| Continuity | Can work resume without relying on old chat context? |
| Organization | Are files intuitive to find, maintain, and navigate? |
| Preservation | Have historical work and meaningful alternatives been retained? |

Report important weaknesses and remaining tasks. Explain any incomplete audit coverage rather than presenting partial work as exhaustive.

## 12. Deliverables

The completed implementation should produce:

1. A project-wide inventory and audit report.
2. An organized GitHub repository.
3. An appropriately structured Google Drive folder.
4. A navigable central project index.
5. Separate documentation and progress records for every discovered subproject.
6. Source-of-truth, versioning, and maintenance conventions.
7. Copy-ready ChatGPT Project Instructions.
8. A system for preserving incidental AI observations.
9. A final verification report with unresolved issues and recommended next steps.

### Example progress-record format

**Subproject:** Veteran Fighter

**Status:** Active development

**Current Version:** [Verified version]

**Most Recent Decision:** [Confirmed decision and source]

**Current Work:** [Specific mechanic or design issue]

**Open Questions:** [Outstanding decisions]

**Next Recommended Action:** [One specific next step]

**Last Updated:** YYYY-MM-DD

**Relevant Files:** [Links to current design and decision history]

Populate these fields only with verified information. Clearly identify unknowns.

## 13. Final Communication Requirements

Prioritize completing the actual work over describing what should be done.

Provide brief progress updates when material milestones are reached.

Once implementation is complete, provide a concise summary of approximately **250–400 words** containing:

- What was reviewed.
- What was created or modified.
- Important findings or discrepancies.
- Links to the principal project resources.
- Anything requiring my approval or manual action.
- The recommended next step.

Keep detailed audit findings, histories, and lengthy explanations in the project documentation.

**Success means that the project's existing work is preserved, its current state is clearly documented, its external resources are organized, and future ChatGPT conversations can resume development without repeatedly reconstructing the past.**

Begin with the comprehensive audit, proceed through the implementation stages, and complete all safe, feasible work using the available connected tools.