# Algospace — personal DSA learning workspace

A static React + Vite application around the original Python course. No backend, account, remote content API, or device synchronization.

## Quick start

Prerequisites: Node.js 22 (22.12 or newer), npm, and this **whole repository**, not just `web/`.

```sh
cd web
npm ci
npm run dev
```

Open the printed `/DSA/` URL (normally http://localhost:5173/DSA/). The development server binds to all interfaces for hosted previews. Stop it when not needed on an untrusted network.

```sh
npm run lint
npm test
npm run build
npm run check:build
npm run preview
```

Preview normally runs at http://localhost:4173/DSA/. `npm ci` uses the committed lockfile. No Python dependency is required for the website.

Browser tests:

```sh
npx playwright install --with-deps chromium
npm run test:e2e
```

On systems with browser libraries already installed, `npx playwright install chromium` is sufficient. Tests start the dev server automatically if one is not running. To test a running production preview, set `DSA_TEST_URL=http://localhost:4173/DSA/`. This sandbox has restricted downloads; its tests use the npm-packaged Chromium with `DSA_BUNDLED_BROWSER=1` and extracted NSS libraries on `LD_LIBRARY_PATH`. Normal local/CI tests use Playwright's standard browser instead. The bundled browser is a development-only dependency, never shipped to users.

From the repository root, the unchanged course checks are:

```sh
python scripts/check_structure.py
python scripts/check_links.py
python -m compileall -q scripts week-*
python -m pytest -q
```

Install pytest in a virtual environment if necessary. Test results and generated website files are ignored by Git.

## What is implemented

- Dashboard with real lesson/problem counts, resume action, today's plan, and revision reminders.
- Expandable week roadmap; per-topic completion, per-week lesson progress, and resource navigation.
- GFM Markdown reader with tables, fenced code, headings, safe links, and no raw HTML execution. Python and other source files are shown as text, not executed.
- Full-text search with week, topic, resource-type, progress, and available difficulty filters. Titles rank above body-only matches in library search.
- Practice statuses (Not started, Attempted, Solved, Review), local notes, expandable hints/approaches, and separately disclosed reference files.
- Original study plans, parsed time blocks and persistent block checkboxes. Conflicting declared durations and block sums are both shown. No planned minutes are counted as studied time.
- Manual revision queue, due/overdue/upcoming labels, review dates, and local-calendar scheduling.
- Real completion statistics, date-stamped activity, current/longest streaks, and zero-data states.
- Light/dark themes, responsive navigation, mobile keyboard focus management, native disclosures and controls, visible focus, skip link, and reduced-motion support.
- Browser-local versioned storage, validated JSON import/export, storage failure messages, and an explicit reset confirmation.

## Content discovery

`npm run content` scans **all directories matching `week-<digits>-<slug>`**, recursively, in stable order. Both `npm run dev` and `npm run build` run it first. During an already running development session, rerun `npm run content` after changing course files (or restart the server).

Original files remain the source of truth; they are never rewritten. Supported files are `.md`, `.py`, `.csv`, `.txt`, and `.json`. Hidden files, cache directories, and unsupported binaries are excluded. The generated manifest contains path-based IDs, full source text, week/topic metadata, types, block durations, and a pre-lowercased full-text search index. No second authored curriculum is maintained.

Conventions:

- Week folder: `week-08-new-patterns/` (any number of weeks).
- `lessons/<topic>/<name>.md`: lesson; topic comes from its directory.
- `curriculum/*.md`: day/revision study plans, preserving filename order.
- `problems/<difficulty>/*.md`: problem statements. Optional `**Topics**` table metadata supplies topic information.
- `examples/`, `exercises/starter-code/`, `exercises/solutions/`, and `exercises/test-cases/`: examples, starters, reference solutions, and tests.
- `revision/`, `interview-prep/`, and `assessments/`: supporting learning material. Other supported files become guides.
- The first Markdown H1 is the title; otherwise a readable filename is used. No frontmatter is required.
- Time blocks use Markdown table rows with durations such as `45 min` or `90–120 min` in the first two cells. Missing durations are not invented. Very short source plans are displayed as-is.

Generate `src/content/manifest.json` on every build; do **not** commit it. `public/course/` contains generated verbatim non-Markdown downloads with a `.txt` serving suffix (the download control retains the original filename). This avoids Python test discovery collecting generated copies. Markdown is embedded verbatim in the manifest and links to its original GitHub source. Both generated locations are ignored. Rebuild when deploying additions. Tests include a temporary future-week fixture and byte-for-byte text comparisons.

### Links and content safety

Hash routes work on GitHub Pages without server fallbacks. Supported relative file links open the reader; relative directory links open filtered resources. Fragment links retain the reader route and scroll to headings. Links outside the manifest fall back to the corresponding original GitHub path; external URLs are not assumed verified. Inline-code paths in study plans become links when they match a known resource. Unsupported formats can be accessed through source links. Arbitrary embedded HTML is not enabled. A missing file or unknown route has a friendly fallback.

## Progress and revision

Storage key: `dsa-workspace-v1`. Schema version 1 stores completion dates, problem statuses, review records, notes, activity dates, last resource, and theme. No personal profile is stored. New content starts incomplete. Removed content records remain in storage/export but are excluded from available-content metrics. Topics are completed by marking their constituent lessons; progress never counts duplicate IDs.

Malformed/unknown-version data shows a warning and starts an empty in-memory session; simply opening a resource does not overwrite the damaged value. A deliberate progress change can replace it. Export or inspect browser storage before changing anything if recovery is needed. If storage is blocked/full, changes only survive the session. This is the first schema: future schema changes must introduce an explicit migration in `src/lib/progress.mjs`; unknown schemas are currently rejected, never guessed or silently migrated. Imports are limited to 2 MB and validated before confirmation and replacement.

Completing a lesson suggests review 1 local calendar day later. Review completion schedules another review after 3, 7, 14, then 30 days; further reviews repeat every 30 days. Dates use local device calendar dates at noon for arithmetic across daylight-saving transitions. Marking an item for revision manually makes it due today. This is a practical default, not an optimal schedule for every learner. Unchecking completion does not discard an independently scheduled review; reset removes everything after confirmation. Notes, page views, and theme changes do not create study activity. Streaks count unique local dates of recorded completion, attempts/status changes, or reviews.

## GitHub Pages

Repository identity is `Harshavardhan86881/DSA`; the expected project-site URL is **https://harshavardhan86881.github.io/DSA/**. This URL is a target, not a claim of successful deployment.

`vite.config.js` sets `base: '/DSA/'`. Hash navigation and download URLs honor that base. `.github/workflows/dashboard.yml` checks the website on PRs and pushes to main, then deploys only on a main-branch push or manual main-branch run. Deployment has its own least-privilege Pages permissions. Existing validation workflow is unchanged.

One-time manual setup: repository **Settings → Pages → Build and deployment → Source → GitHub Actions**. After review and merge by the owner, check the workflow and Pages deployment status. No settings were changed by this implementation. The Pages API returned 404 during audit; this can mean Pages is not configured or not visible to the current token.

For another repository name, change Vite's base and the documented source URL helpers. Do not use history routes without adding a compatible hosting fallback.

## Structure

- `scripts/content.mjs`: deterministic discovery and generated downloads.
- `src/content/`: manifest adapter and source URL helpers.
- `src/App.jsx`: hash routing, error boundary, shell, search and mobile navigation.
- `src/components/`: shared cards, resource lists and progress indicators.
- `src/pages/`: learning views, reader, and settings.
- `src/lib/`: validated storage, date/revision/statistics calculations and React progress context.
- `src/index.css`: tokens, both themes, responsive and reading styles.
- `tests/`: Node unit/content tests and Playwright browser tests.

## Limitations and troubleshooting

- No code execution, editor, grading, actual study-duration recording, analytics, or cross-device sync. “Solved” is self-reported.
- Source code is readable in monospace; token-level syntax highlighting is not included.
- Review intervals are documented defaults, not customizable in the UI yet.
- Search currently embeds the complete supported text in the app (~2.25 MB production JavaScript before gzip, ~378 KB gzip at the initial content size). Vite emits a large-chunk warning. A much larger course should split reader text into lazy-loaded assets and retain a compact index.
- Shared root documents outside week folders open on GitHub, rather than as dashboard lessons. Unknown/binary content falls back to source; no external-link availability is claimed.
- Some source plans are brief or have inconsistent durations; the UI preserves them and does not claim the curriculum itself is complete.
- Browser/storage data is not secure against other scripts on the same origin; do not store secrets in notes or backups.
- Missing content after an edit: regenerate the manifest. Blank page on Pages: verify `/DSA/` base and Actions source. Lost progress: check browser/profile/origin and restore an exported JSON. Corrupt import: use a version 1 export rather than editing its shape manually.

See [verification.md](docs/verification.md) for the observed recovery and test record.
