import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
export const root = path.resolve(
  path.dirname(fileURLToPath(import.meta.url)),
  "../..",
);
const title = (s) =>
  s.replace(/[-_]/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
export function planBlocks(text) {
  return text
    .split("\n")
    .filter((line) => line.startsWith("|") && /\bmin(?:utes)?\b/i.test(line))
    .flatMap((line) => {
      const cells = line
        .split("|")
        .slice(1, -1)
        .map((c) => c.trim());
      const duration = cells
        .slice(0, 2)
        .join(" ")
        .match(/(\d+)(?:[–-](\d+))?\s*min/i);
      return duration
        ? [
            {
              title: cells[0],
              minutes: Number(duration[1]),
              maxMinutes: Number(duration[2] || duration[1]),
              duration: duration[0],
              task: cells.slice(cells.length >= 3 ? 2 : 1).join(" | "),
            },
          ]
        : [];
    });
}
export function scan(base = root) {
  const resources = [],
    weeks = [];
  function walk(dir) {
    return fs
      .readdirSync(dir, { withFileTypes: true })
      .sort((a, b) => a.name.localeCompare(b.name, "en"))
      .flatMap((e) =>
        e.name.startsWith(".") || e.name === "__pycache__"
          ? []
          : e.isDirectory()
            ? walk(path.join(dir, e.name))
            : [path.join(dir, e.name)],
      );
  }
  for (const folder of fs
    .readdirSync(base)
    .filter((n) => /^week-\d+-/.test(n))
    .sort()) {
    const week = {
      id: folder,
      number: Number(folder.match(/\d+/)[0]),
      title: title(folder.replace(/^week-\d+-/, "")),
      topics: [],
    };
    weeks.push(week);
    for (const file of walk(path.join(base, folder))) {
      if (!/\.(md|py|csv|txt|json)$/.test(file)) continue;
      const id = path.relative(base, file).split(path.sep).join("/"),
        parts = id.split("/"),
        text = fs.readFileSync(file, "utf8");
      const area = parts[1];
      const type =
        area === "lessons"
          ? "lesson"
          : area === "curriculum"
            ? "plan"
            : area === "problems" && file.endsWith(".md")
              ? "problem"
              : area === "problems" || parts.includes("solutions")
                ? "solution"
                : parts.includes("starter-code")
                  ? "starter"
                  : parts.includes("test-cases")
                    ? "test"
                    : area === "examples"
                      ? "example"
                      : area === "interview-prep"
                        ? "interview"
                        : area === "assessments"
                          ? "assessment"
                          : area === "revision"
                            ? "revision"
                            : "guide";
      const topic =
        area === "lessons" || area === "examples"
          ? parts.length > 3
            ? title(parts[2])
            : week.title
          : text.match(/\*\*Topics?\*\*\s*\|\s*([^|\n]+)/i)?.[1]?.trim() ||
            week.title;
      if (type === "lesson" && !week.topics.includes(topic))
        week.topics.push(topic);
      const heading = text.match(/^#\s+(.+)$/m)?.[1];
      resources.push({
        id,
        week: folder,
        type,
        topic,
        title: heading || title(path.basename(file, path.extname(file))),
        format: path.extname(file).slice(1),
        difficulty: area === "problems" ? parts[2] : "",
        text,
        blocks: type === "plan" ? planBlocks(text) : [],
        plannedMinutes:
          type === "plan"
            ? planBlocks(text).reduce((sum, b) => sum + b.minutes, 0) || null
            : null,
        plannedMaxMinutes:
          type === "plan"
            ? planBlocks(text).reduce((sum, b) => sum + b.maxMinutes, 0) || null
            : null,
        declaredMinutes:
          type === "plan"
            ? Number(
                text.match(/Estimated time[^\n]*?(\d+) hours/i)?.[1] || 0,
              ) * 60 || null
            : null,
        search:
          `${week.title} ${topic} ${heading || file} ${text}`.toLowerCase(),
      });
    }
  }
  if (new Set(resources.map((r) => r.id)).size !== resources.length)
    throw Error("Duplicate resource ids");
  return { weeks, resources };
}
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const data = scan();
  fs.mkdirSync(path.join(root, "web/src/content"), { recursive: true });
  fs.writeFileSync(
    path.join(root, "web/src/content/manifest.json"),
    JSON.stringify(data),
  );
  // Copy source bytes, preserving paths, for downloads and non-Markdown resources.
  const out = path.join(root, "web/public/course");
  fs.rmSync(out, { recursive: true, force: true });
  for (const r of data.resources.filter((r) => r.format !== "md")) {
    // Text suffix prevents generated test downloads from being collected as Python tests.
    const dest = path.join(out, r.id + ".txt");
    fs.mkdirSync(path.dirname(dest), { recursive: true });
    fs.copyFileSync(path.join(root, r.id), dest);
  }
  console.log(
    `Discovered ${data.weeks.length} weeks, ${data.resources.length} resources`,
  );
}
