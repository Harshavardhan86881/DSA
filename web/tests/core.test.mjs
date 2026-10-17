import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { scan, root } from "../scripts/content.mjs";
import {
  blank,
  validate,
  load,
  stats,
  reviewNext,
  addDays,
  streaks,
  resolveLink,
} from "../src/lib/progress.mjs";
test("all supported files discovered verbatim with unique identifiers", () => {
  const data = scan();
  assert.equal(
    data.weeks.length,
    fs.readdirSync(root).filter((n) => /^week-\d+-/.test(n)).length,
  );
  assert.equal(
    new Set(data.resources.map((r) => r.id)).size,
    data.resources.length,
  );
  for (const r of data.resources) {
    assert.equal(r.text, fs.readFileSync(path.join(root, r.id), "utf8"));
    assert.ok(data.weeks.some((w) => w.id === r.week));
    assert.ok(r.title);
  }
  assert.ok(data.resources.some((r) => r.type === "problem"));
  assert.ok(data.resources.some((r) => r.type === "plan"));
});
test("future week and lesson discovery, optional resources absent", () => {
  const temp = fs.mkdtempSync(path.join(os.tmpdir(), "dsa-content-"));
  try {
    const dir = path.join(temp, "week-08-new-topic/lessons/new-pattern");
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(
      path.join(dir, "lesson.md"),
      "# A future lesson\n\nOriginal text",
    );
    const data = scan(temp);
    assert.equal(data.weeks.length, 1);
    assert.equal(data.resources.length, 1);
    assert.equal(data.resources[0].type, "lesson");
    assert.deepEqual(data.weeks[0].topics, ["New Pattern"]);
  } finally {
    fs.rmSync(temp, { recursive: true });
  }
});
test("storage handles absent, corrupt, outdated, and unavailable values", () => {
  assert.deepEqual(load({ getItem: () => null }).data, blank());
  for (const value of ["{", '{"version":0}'])
    assert.ok(load({ getItem: () => value }).error);
  assert.ok(
    load({
      getItem: () => {
        throw Error("blocked");
      },
    }).error,
  );
  assert.throws(() => validate({ ...blank(), problems: { x: "Passed" } }));
  assert.throws(() =>
    validate({ ...blank(), reviews: { x: { due: "2026-02-30", step: 0 } } }),
  );
  assert.deepEqual(validate(blank()), blank());
});
test("progress counts only available, unique completion records", () => {
  const data = blank();
  data.completed = { a: "2026-10-17", removed: "2026-10-17" };
  data.problems = { b: "Solved", removed: "Solved" };
  const s = stats(
    [
      { id: "a", type: "lesson" },
      { id: "b", type: "problem" },
      { id: "c", type: "lesson" },
    ],
    data,
  );
  assert.deepEqual(s, {
    lessons: 2,
    done: 1,
    problems: 1,
    solved: 1,
    percent: 50,
    attempted: 1,
  });
  assert.equal(stats([], data).percent, 0);
});
test("calendar dates and spaced review intervals, including month and leap boundaries", () => {
  assert.equal(addDays("2024-02-28", 1), "2024-02-29");
  assert.equal(addDays("2026-12-31", 1), "2027-01-01");
  assert.deepEqual(reviewNext({ step: 0 }, "2026-10-17"), {
    step: 1,
    last: "2026-10-17",
    due: "2026-10-20",
  });
  assert.equal(reviewNext({ step: 5 }, "2026-10-17").due, "2026-11-16");
  assert.deepEqual(
    streaks(["2026-10-15", "2026-10-16", "2026-10-17"], "2026-10-17"),
    { current: 3, longest: 3 },
  );
  assert.equal(streaks([]).current, 0);
});
test("relative links resolve to reader and directory routes; unsafe schemes are rejected", () => {
  const rs = [{ id: "week-01/lessons/a.md" }, { id: "week-01/examples/a.py" }];
  assert.equal(
    resolveLink(rs[0].id, "../examples/a.py", rs),
    "#/read/week-01%2Fexamples%2Fa.py",
  );
  assert.equal(
    resolveLink(rs[0].id, "#test", rs),
    "#/read/week-01%2Flessons%2Fa.md?anchor=test",
  );
  assert.equal(
    resolveLink(rs[0].id, "../examples/", rs),
    "#/browse?path=week-01%2Fexamples",
  );
  assert.equal(resolveLink(rs[0].id, "javascript:alert(1)", rs), "#/missing");
});
test("plan durations preserve explicit block values, including source inconsistencies and ranges", () => {
  const data = scan();
  const day = data.resources.find((r) =>
    r.id.endsWith("curriculum/day-01-problem-solving.md"),
  );
  assert.equal(day.plannedMinutes, 210);
  assert.equal(day.declaredMinutes, 240);
  assert.equal(day.blocks.length, 4);
  const sunday = data.resources.find(
    (r) =>
      r.week.startsWith("week-02") &&
      r.type === "plan" &&
      r.id.includes("sunday"),
  );
  assert.equal(sunday.plannedMinutes, 300);
  assert.equal(sunday.plannedMaxMinutes, 330);
  const minimal = data.resources.find(
    (r) => r.week.startsWith("week-07") && r.type === "plan",
  );
  assert.equal(minimal.plannedMinutes, null);
});
