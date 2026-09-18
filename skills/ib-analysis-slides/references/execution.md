# Build and review

The skill is a directory of instructions, profiles and editable examples. Install the whole directory. It has no private-file, original-report or companion-skill requirement for HTML generation.

## Runtime

Use an agent with file access, a browser capable of actual rendering, and input readers appropriate to the user's material. Plain HTML needs no build system. The optional bundled capture helper uses Node.js, Playwright and Chromium/Chrome; the repository package-lock fixes its tested dependency. Python 3 standard library runs the package/static-example checks. PDF readers and PPT exporters are task-specific and are not bundled.

In a clone of this repository, the user can install the screenshot tooling with `npm ci` and `npx playwright install chromium`. Installation requires network/disk access and is not needed merely to read this skill. An agent should use existing dependencies first and follow the environment's installation permissions.

If the skill was copied without repository node_modules, set `NODE_PATH` to an existing node_modules containing Playwright, or run the helper from a repository clone. `BROWSER_EXECUTABLE_PATH` optionally selects an installed Chromium-compatible browser. Never hardcode the author's machine paths in deliverables.

## Author directly

Use the selected profile and a matching example as a structural reference. Write standalone HTML containing a `head`, UTF-8 metadata, `lang="en"`, scoped CSS and ordered `article.slide` elements. Default 960×540 screen dimensions; the white analytical theme uses 720×405 source coordinates scaled by 4/3, while financial pages use 960×540 source coordinates directly. SVG text is editable but has no spreadsheet link. Financial cells use real HTML tables with header associations and explicit units.

A small Python or JavaScript generator is optional when it actually reduces repetitive work. Keep its data, arithmetic checks and rebuild instructions with the output. No PE builder is required. Output records live in the user's work directory, not inside the installed skill.

For each page, record: question and conclusion; full copy; evidence/source; selected relationship and expression; main/supporting areas; missing data; review status. Keep calculations and source conflicts outside the reader-facing slide except where the qualification changes its meaning.

## Rendering

Run package/static checks on the distributed examples:

```sh
python3 scripts/check_package.py
```

The checker can also inspect a new HTML document for active content, network dependencies, language and slide presence:

```sh
python3 scripts/check_package.py /path/to/output.html
node scripts/capture_pages.cjs /path/to/output.html /path/to/new-qa-directory
```

Paths above are relative to the installed skill directory. Capture refuses to overwrite an existing QA directory. It hides page-external navigation, captures every slide, records its HTML hash, and reports SVG text overflow and text bounding-box intersections. It blocks HTTP(S) requests; any such request needs investigation. Screenshot filenames are generated from page numbers, not input-controlled IDs.

The static check is a conservative lint for locally authored documents, not a sandbox for hostile HTML. Only render documents you authored or have inspected. The capture helper does not prove HTML-element overlap, correct facts, ideal density or chart semantics. Rotated label boxes can overlap while actual glyphs do not.

View every actual screenshot at its intended size. Verify title/body/footnote hierarchy, table rows, label association, long labels, signs, zero lines, source visibility, alignment and meaningful use of space. Compare the selected theme and examine the whole deck for repeated evidence or inconsistent scopes. If the preview appears suspicious, verify actual pixels/DOM before changing correct coordinates.

After any change, recapture the final HTML and record the matching hash. Do not reuse a prior QA report against newer bytes. Report four dimensions separately: evidence/calculation, structure, actual visual review and whole-deck consistency. PPT/PDF needs its own format review.

[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
