export const KEY = "dsa-workspace-v1";
export const blank = () => ({
  version: 1,
  completed: {},
  problems: {},
  reviews: {},
  notes: {},
  activity: [],
  last: null,
  theme: null,
});
export const dateKey = (date = new Date()) =>
  `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, "0")}-${String(date.getDate()).padStart(2, "0")}`;
export function addDays(day, n) {
  const d = new Date(`${day}T12:00:00`);
  d.setDate(d.getDate() + n);
  return dateKey(d);
}
const validDate = (v) =>
  typeof v === "string" &&
  /^\d{4}-\d{2}-\d{2}$/.test(v) &&
  !Number.isNaN(new Date(`${v}T12:00:00`).getTime()) &&
  dateKey(new Date(`${v}T12:00:00`)) === v;
export function validate(value) {
  if (!value || value.version !== 1)
    throw Error("Unsupported progress version; import a version 1 export.");
  const out = blank();
  for (const key of ["completed", "problems", "reviews", "notes"]) {
    if (
      !value[key] ||
      typeof value[key] !== "object" ||
      Array.isArray(value[key])
    )
      throw Error(`Invalid ${key} records`);
    for (const [id, v] of Object.entries(value[key])) {
      if (["__proto__", "constructor", "prototype"].includes(id)) continue;
      if (key === "completed" && validDate(v)) out[key][id] = v;
      else if (
        key === "problems" &&
        ["Attempted", "Solved", "Review"].includes(v)
      )
        out[key][id] = v;
      else if (key === "notes" && typeof v === "string")
        out[key][id] = v.slice(0, 10000);
      else if (
        key === "reviews" &&
        v &&
        validDate(v.due) &&
        Number.isInteger(v.step) &&
        v.step >= 0 &&
        v.step <= 5 &&
        (!v.last || validDate(v.last))
      )
        out[key][id] = { due: v.due, step: v.step, last: v.last || null };
      else throw Error(`Invalid ${key} entry`);
    }
  }
  out.activity = Array.isArray(value.activity)
    ? [...new Set(value.activity.filter(validDate))].sort()
    : [];
  out.last = typeof value.last === "string" ? value.last : null;
  out.theme = ["light", "dark"].includes(value.theme) ? value.theme : null;
  return out;
}
export function load(storage) {
  try {
    const raw = storage.getItem(KEY);
    return { data: raw ? validate(JSON.parse(raw)) : blank(), error: "" };
  } catch {
    return {
      data: blank(),
      error:
        "Saved progress could not be read. Using an empty session; the original stored value is unchanged until you make a change. Export a backup before resetting.",
    };
  }
}
export const schedule = [1, 3, 7, 14, 30];
export function reviewNext(record, today = dateKey()) {
  const step = Math.min((record?.step || 0) + 1, 5);
  return {
    step,
    last: today,
    due: addDays(today, schedule[Math.min(step, 4)]),
  };
}
export function stats(resources, data) {
  const lessons = resources.filter((r) => r.type === "lesson"),
    problems = resources.filter((r) => r.type === "problem");
  const done = lessons.filter((r) => data.completed[r.id]).length,
    solved = problems.filter((r) => data.problems[r.id] === "Solved").length;
  return {
    lessons: lessons.length,
    done,
    problems: problems.length,
    solved,
    percent: lessons.length ? Math.round((100 * done) / lessons.length) : 0,
    attempted: problems.filter((r) => data.problems[r.id]).length,
  };
}
export function streaks(days, today = dateKey()) {
  const set = new Set(days);
  let current = 0,
    d = set.has(today) ? today : addDays(today, -1);
  while (set.has(d)) {
    current++;
    d = addDays(d, -1);
  }
  let longest = 0,
    run = 0,
    prev = null;
  for (const day of [...set].sort()) {
    run = prev && addDays(prev, 1) === day ? run + 1 : 1;
    longest = Math.max(longest, run);
    prev = day;
  }
  return { current, longest };
}
export function resolveLink(id, href, resources) {
  if (!href || /^(https?:|mailto:)/i.test(href)) return href;
  if (/^[a-z]+:/i.test(href) || href.startsWith("//")) return "#/missing";
  const [pathname, anchor] = href.split("#");
  const parts = pathname ? id.split("/").slice(0, -1) : id.split("/");
  if (pathname)
    for (const part of decodeURIComponent(pathname).split("/")) {
      if (part === "..") parts.pop();
      else if (part && part !== ".") parts.push(part);
    }
  const target = parts.join("/").replace(/\/$/, "");
  if (resources.some((r) => r.id === target))
    return `#/read/${encodeURIComponent(target)}${anchor ? `?anchor=${encodeURIComponent(anchor)}` : ""}`;
  if (resources.some((r) => r.id.startsWith(target + "/")))
    return `#/browse?path=${encodeURIComponent(target)}`;
  return `https://github.com/Harshavardhan86881/DSA/blob/main/${target}${anchor ? "#" + anchor : ""}`;
}
