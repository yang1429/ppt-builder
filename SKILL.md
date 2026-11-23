---
name: ppt-builder
description: This skill should be used when a user asks to create a PowerPoint presentation from a topic, outline, brief, Word or Markdown document, or existing material, or asks to check, restyle, or finish a generated PPTX. It provides an outline-first workflow, design rules, and a dependency-free PPTX checker.
agent_created: true
version: 0.1.0
---

# PPT Builder

## Overview

Turn a topic or source material into a review-ready PowerPoint file with an outline-first workflow, an explicit design spec, and a mechanical validation pass before delivery.

## Workflow Decision Tree

- New topic or rough brief → follow Steps 1–6.
- Source document provided → extract and structure material first, then continue from Step 2.
- Existing PPTX to inspect → run Step 4 validation and Step 5 render check, then fix reported issues.
- User asks only for an outline → stop after Step 2 and deliver the outline.

## Step 1: Confirm the minimum inputs

Confirm three items in one pass: audience and purpose, target slide count (default 10–14), and mandatory brand colors, fonts, logo, or language. Do not ask about details that can be reasonably inferred. Record the answers in the outline file.

## Step 2: Write the outline before any slide

Create an outline from `assets/outline-template.md`. One slide carries one message. Each slide entry must contain a one-line headline that states a conclusion, 2–5 supporting points, and the visual form (table, chart, diagram, or image). Reject outlines whose headlines are only topic labels.

## Step 3: Produce the deck

Use the PPTX generation toolchain available in the current environment. Prefer a dedicated presentation generator such as `tencent-pptx` when installed; otherwise use `python-pptx`. Follow `references/design-spec.md` for typography, spacing, color, and chart rules. Keep every number traceable to the source; mark unverified figures as placeholders instead of inventing them.

## Step 4: Validate the file mechanically

Run `python scripts/validate_pptx.py <path-to-pptx>`. The checker needs no third-party packages. Fix every error it reports, especially empty slides, text overflow risks, and missing titles, then rerun until no errors remain.

## Step 5: Check the rendered result

Export slide images when a renderer is available (PowerPoint COM on Windows, or an installed converter). Inspect every page for clipping, overlap, and unreadable text. When no renderer exists, state that limitation in the delivery note instead of claiming visual verification.

## Step 6: Deliver

Return the PPTX path, slide count, and a one-sentence summary of the story. Mention any placeholders or unverified data explicitly.

## Resources

- `references/design-spec.md` — typography, color, spacing, and chart conventions.
- `scripts/validate_pptx.py` — dependency-free structural checker.
- `assets/outline-template.md` — outline skeleton to copy before designing slides.
