# Website Refactor Suite

The **Website Refactor Suite** is a high-performance multi-agent framework designed to transform legacy, messy, or mirrored websites into production-grade, modular Next.js applications.

It leverages a 6-agent swarm to handle everything from information architecture and design system extraction to code refactoring and benefit-driven copywriting.

## Architecture Overview
The suite is organized into 6 specialized skills, each containing its own mission (`SKILL.md`), automated enforcers (`scripts/`), and domain knowledge (`resources/`).

1.  **Site Architecture Auditor**: Flattens hierarchy and enforces the 3-click rule.
2.  **UI/UX Design System Auditor**: Extracts design tokens and normalizes the visual language.
3.  **Code Quality Refactor Auditor**: Scans for 62 React best practices and eliminates technical debt.
4.  **Component Consistency Builder**: Rebuilds UI as a clean, shadcn/ui-powered library.
5.  **Website Rebuilder Orchestrator**: Assemblies the final codebase and validates performance/a11y.
6.  **Content & Copy Consistency Agent**: Rewrites site copy for conversion and brand alignment.

## How it Works
1.  **Snapshot**: Run the audit scripts to capture the current state.
2.  **Analyze**: Each agent processes the snapshot to create a new specification (DESIGN.md, ARCHITECTURE.md).
3.  **Generate**: The Orchestrator uses the specs to build the new repository.
4.  **Validate**: Run the final validation suite to ensure zero regressions.

## Usage
Refer to `TASK_LIST.md` for the step-by-step execution roadmap for Jules AI.
