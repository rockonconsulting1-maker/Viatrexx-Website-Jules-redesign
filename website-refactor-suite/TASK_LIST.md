# Scheduled Task List for Jules AI

Follow this sequence to execute the redesign. For each task, use the provided prompt.

---

### Task 1: Information Architecture Audit
**Agent**: `site-architecture-auditor`
**Prompt**:
> "Run the `site-architecture-auditor` on the current `site_snapshot.json`. Analyze the page hierarchy, apply the 3-click rule to flatten the structure, and output a new `ARCHITECTURE.md` including a Mermaid sitemap and a 301 redirect plan."

---

### Task 2: Design System Extraction
**Agent**: `ui-ux-design-system-auditor`
**Prompt**:
> "Run the `ui-ux-design-system-auditor` on `current_styles.txt` and the root HTML files. Extract primary/secondary colors, typography tokens, and spacing rules. Detect any design anti-patterns. Output a source-of-truth `DESIGN.md` and a `tailwind.config.ts` snippet."

---

### Task 3: Content & Copy Transformation
**Agent**: `content-copy-consistency-agent`
**Prompt**:
> "Using `current_copywriting.txt` and the newly generated `DESIGN.md`, rewrite the copy for the Homepage and Services pages. Apply the PAS (Problem-Agitation-Solution) framework. Ensure the tone is confident and benefit-driven. Output to `REFACTORED_COPY.md`."

---

### Task 4: Technical Debt & Quality Audit
**Agent**: `code-quality-refactor-auditor`
**Prompt**:
> "Scan the mirrored scripts in `stcdn.leadconnectorhq.com/_preview/` and the root HTML components. Apply the 62 React/Next.js best practices. Identify inline styles and hardcoded logic that should be moved to hooks or components. Output a `REFACTOR_REPORT.md`."

---

### Task 5: Component Library Generation
**Agent**: `component-consistency-builder`
**Prompt**:
> "Based on `DESIGN.md` and `REFACTOR_REPORT.md`, build a core set of shadcn/ui components (Button, Card, Navbar, Footer) in a new `components/` directory. Ensure they are token-driven and fully accessible."

---

### Task 6: Full Site Assembly
**Agent**: `website-rebuilder-orchestrator`
**Prompt**:
> "Orchestrate the final rebuild. Use `ARCHITECTURE.md`, `DESIGN.md`, and `REFACTORED_COPY.md` to assemble a complete Next.js app structure in a folder named `rebuilt-site`. Generate the main pages and link the new components."

---

### Task 7: Final Validation & Launch Readiness
**Agent**: `website-rebuilder-orchestrator`
**Prompt**:
> "Perform a final audit on the `rebuilt-site` folder. Run accessibility checks, verify 301 redirects, and ensure Lighthouse scores for Performance and Best Practices are above 90. Provide a final `VALIDATION_REPORT.md`."
