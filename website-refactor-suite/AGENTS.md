# Website Refactor Suite for Jules AI

Complete 6-agent swarm that takes **any existing website** (live URL or codebase) and rebuilds the **exact same visual & behavioral experience** but with 100% clean, consistent, production-grade code + copy.

All agents follow the open Agent Skills standard (SKILL.md + scripts/ + resources/).

## The 6 Specialized Agents

### 1. site-architecture-auditor
Reviews and rebuilds page hierarchy, navigation, URL structure, and information architecture (3-click rule enforced, flat structure, SEO-friendly).
`npx skills add your-repo --skill site-architecture-auditor --global`

### 2. ui-ux-design-system-auditor
Extracts the current design language, detects every inconsistency, and outputs a single source-of-truth **DESIGN.md** + Tailwind/shadcn/ui config.
`npx skills add your-repo --skill ui-ux-design-system-auditor --global`

### 3. code-quality-refactor-auditor
Scans every file against 62 React/Next.js best practices + performance + accessibility rules and produces prioritized fix patches.
`npx skills add your-repo --skill code-quality-refactor-auditor --global`

### 4. component-consistency-builder
Converts old messy components into a clean, token-driven, shadcn/ui + Tailwind library with zero drift.
`npx skills add your-repo --skill component-consistency-builder --global`

### 5. website-rebuilder-orchestrator
Takes outputs from agents 1–4 (and 6) and generates the **complete new codebase** (same pages, same UX, now perfect). Runs full validation.
`npx skills add your-repo --skill website-rebuilder-orchestrator --global`

### 6. content-copy-consistency-agent
Reviews all existing copy on the site, rewrites it to be clear, benefit-driven, conversion-focused, and 100% consistent with the new design system.
`npx skills add your-repo --skill content-copy-consistency-agent --global`

## How to Use
Tell Jules:
> "Run the full Website Refactor Suite on https://old-site.com — rebuild with clean code, consistent components, shadcn/ui + Tailwind, and conversion copy."

The orchestrator will chain all 6 agents automatically.

This suite was built by merging:
- google-labs-code/jules-skills
- google-labs-code/stitch-skills
- nextlevelbuilder/ui-ux-pro-max-skill
- vercel-labs/agent-skills
- coreyhaines31/marketingskills (site-architecture + copywriting)

Ready for production use with Jules AI, Cursor, Claude Code, etc.
