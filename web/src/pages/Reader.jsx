import { useEffect, useState } from "react";
import Markdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { ArrowLeft, ExternalLink, CalendarPlus, Download } from "lucide-react";
import { resources, weeks, byId, href, source } from "../content";
import { useProgress } from "../lib/useProgress";
import { dateKey, resolveLink } from "../lib/progress.mjs";
import { Heading, Empty, ResourceList } from "../components/Common";
const slug = (s) =>
  s
    .toLowerCase()
    .replace(/[^\p{L}\p{N}\s-]/gu, "")
    .trim()
    .replace(/\s/g, "-");
export function Reader({ id, query }) {
  const r = byId.get(id),
    { data, update, complete } = useProgress(),
    [revealed, setRevealed] = useState(false);
  useEffect(() => {
    if (r) update((d) => ({ ...d, last: r.id }), "Resource opened", false);
  }, [r, update]); // Reading alone does not count as study activity.
  useEffect(() => {
    const anchor = new URLSearchParams(query).get("anchor");
    if (anchor)
      requestAnimationFrame(() =>
        document.getElementById(anchor)?.scrollIntoView(),
      );
  }, [id, query]);
  if (!r)
    return (
      <>
        <Heading title="Resource not found" />
        <Empty>
          This resource may have moved. Open the roadmap to find the current
          material.
        </Empty>
        <a className="button primary" href="#/roadmap">
          Back to roadmap
        </a>
      </>
    );
  const protectedType =
    ["solution", "assessment"].includes(r.type) && /answer|solution/.test(r.id);
  const sections =
    r.type === "problem" ? r.text.split(/(?=^#{1,3}\s)/m) : [r.text];
  const sensitive = (s) =>
    /^#{1,3}\s.*(?:hint|solution|approach|code.line|line.by.line|walkthrough of.*code)/i.test(
      s.split("\n")[0],
    );
  const links = resources.filter(
    (x) =>
      x.week === r.week &&
      ["starter", "solution", "example"].includes(x.type) &&
      x.title.toLowerCase().replace(/[-_ ]/g, "") ===
        r.title.toLowerCase().replace(/[-_ ]/g, ""),
  );
  const related = resources.filter(
    (x) =>
      x.id !== r.id &&
      x.week === r.week &&
      x.type === "lesson" &&
      (x.topic === r.topic || r.type === "problem"),
  );
  let task = 0;
  const markdown = (text) => (
    <Markdown
      remarkPlugins={[remarkGfm]}
      components={{
        a: ({ href: link, children }) => {
          const target = resolveLink(r.id, link, resources);
          const sol = resources.find(
            (x) => href(x) === target && x.type === "solution",
          );
          return sol && r.type === "problem" ? (
            <span className="muted">Reference solution available below</span>
          ) : (
            <a href={target}>{children}</a>
          );
        },
        h1: ({ children }) => <h1 id={slug(String(children))}>{children}</h1>,
        h2: ({ children }) => <h2 id={slug(String(children))}>{children}</h2>,
        h3: ({ children }) => <h3 id={slug(String(children))}>{children}</h3>,
        table: ({ children }) => (
          <div className="table-scroll">
            <table>{children}</table>
          </div>
        ),
        input: ({ checked }) => {
          const key = `${r.id}::task-${task++}`;
          return (
            <input
              aria-label={`Study task ${task}`}
              type="checkbox"
              checked={!!data.completed[key] || !!checked}
              onChange={(e) => complete(key, e.target.checked)}
            />
          );
        },
        code: ({ className, children }) => {
          const text = String(children),
            match = resources.find(
              (x) =>
                href(x) === resolveLink(r.id, text, resources) ||
                x.id === r.week + "/" + text.replace(/^\.\//, ""),
            );
          return match ? (
            <a href={href(match)}>
              <code>{children}</code>
            </a>
          ) : (
            <code className={className}>{children}</code>
          );
        },
      }}
    >
      {text}
    </Markdown>
  );
  return (
    <>
      <a className="back-link" href={`#/browse?week=${r.week}`}>
        <ArrowLeft size={15} /> Week{" "}
        {weeks.find((w) => w.id === r.week)?.number} · {r.topic}
      </a>
      <div className="reader-layout">
        <article className="reader">
          <div className="reader-toolbar">
            <span className="pill">
              {r.type} {r.difficulty && `· ${r.difficulty}`}
            </span>
            <a href={source(r)} target="_blank" rel="noreferrer">
              Original source <ExternalLink size={14} />
            </a>
          </div>
          {r.type === "plan" && (
            <section className="plan-tracker">
              <h2>Follow your study blocks</h2>
              <p className="muted">
                {r.plannedMinutes
                  ? `${r.plannedMinutes}${r.plannedMaxMinutes !== r.plannedMinutes ? `–${r.plannedMaxMinutes}` : ""} planned minutes in listed blocks`
                  : "Duration not specified"}{" "}
                · Check off blocks as you finish them. This does not record
                elapsed study time.
              </p>
              {r.declaredMinutes && r.declaredMinutes !== r.plannedMinutes && (
                <p className="plan-warning">
                  The source labels this a {r.declaredMinutes}-minute plan, but
                  its listed blocks{" "}
                  {r.plannedMinutes
                    ? `sum to ${r.plannedMinutes}${r.plannedMaxMinutes !== r.plannedMinutes ? `–${r.plannedMaxMinutes}` : ""} minutes`
                    : "do not specify durations"}
                  . Both are preserved without altering the course.
                </p>
              )}
              {(r.blocks || []).map((block, i) => (
                <label className="block-task" key={i}>
                  <input
                    type="checkbox"
                    checked={!!data.completed[`${r.id}::block-${i}`]}
                    onChange={(e) =>
                      update((d) => {
                        const key = `${r.id}::block-${i}`;
                        if (e.target.checked) d.completed[key] = dateKey();
                        else delete d.completed[key];
                        return d;
                      })
                    }
                  />
                  <span>
                    <strong>{block.title}</strong>
                    <small>{block.duration} planned</small>
                    <span>{markdown(block.task)}</span>
                  </span>
                </label>
              ))}
            </section>
          )}
          {protectedType && !revealed ? (
            <div className="empty">
              <h1>{r.title}</h1>
              <p>
                This is reference material. Try the exercise before opening it.
              </p>
              <button
                className="button primary"
                onClick={() => setRevealed(true)}
              >
                Reveal reference material
              </button>
            </div>
          ) : r.format === "md" ? (
            <div className="markdown">
              {sections.map((s, i) =>
                sensitive(s) ? (
                  <details className="disclosure" key={i}>
                    <summary>{s.split("\n")[0].replace(/^#+\s*/, "")}</summary>
                    {markdown(s.substring(s.indexOf("\n") + 1))}
                  </details>
                ) : (
                  <div key={i}>{markdown(s)}</div>
                ),
              )}
            </div>
          ) : (
            <>
              <h1>{r.title}</h1>
              <p className="muted">
                Reference file · {r.format.toUpperCase()} · displayed as text,
                not executed
              </p>
              <pre className="source-code">
                <code>{r.text}</code>
              </pre>
              <a
                className="button secondary"
                download={r.id.split("/").at(-1)}
                href={`${import.meta.env.BASE_URL}course/${r.id}.txt`}
              >
                <Download size={16} /> Download original file
              </a>
            </>
          )}
        </article>
        <aside className="reader-aside">
          <section className="panel">
            <span className="eyebrow">YOUR PROGRESS</span>
            {r.type === "problem" ? (
              <>
                <label>
                  Problem status
                  <select
                    value={data.problems[r.id] || "Not started"}
                    onChange={(e) =>
                      update((d) => {
                        if (e.target.value === "Not started")
                          delete d.problems[r.id];
                        else d.problems[r.id] = e.target.value;
                        return d;
                      })
                    }
                  >
                    {["Not started", "Attempted", "Solved", "Review"].map(
                      (s) => (
                        <option key={s}>{s}</option>
                      ),
                    )}
                  </select>
                </label>
                <p className="muted">
                  Self-reported status. No code is run here.
                </p>
              </>
            ) : (
              <label className="check-label">
                <input
                  type="checkbox"
                  checked={!!data.completed[r.id]}
                  onChange={(e) => complete(r.id, e.target.checked)}
                />{" "}
                Mark {r.type} complete
              </label>
            )}
            <button
              className="button secondary full"
              onClick={() =>
                update((d) => {
                  d.reviews[r.id] = { step: 0, last: null, due: dateKey() };
                  return d;
                })
              }
            >
              <CalendarPlus size={16} /> Add to revision
            </button>
            {data.reviews[r.id] && (
              <small className="muted">
                Next review: {data.reviews[r.id].due}
              </small>
            )}
          </section>
          <section className="panel">
            <label>
              Personal notes
              <textarea
                maxLength={10000}
                value={data.notes[r.id] || ""}
                placeholder="Your observations, questions, and takeaways…"
                onChange={(e) =>
                  update(
                    (d) => {
                      d.notes[r.id] = e.target.value;
                      return d;
                    },
                    "Note saved",
                    false,
                  )
                }
              />
            </label>
            <small className="muted">Saved in this browser only.</small>
          </section>
          {links.length > 0 && (
            <section className="panel">
              <h2>Practice files</h2>
              {links
                .filter((x) => x.type !== "solution")
                .map((x) => (
                  <a className="related-link" href={href(x)} key={x.id}>
                    {x.type} · {x.title}
                  </a>
                ))}
              <details>
                <summary>Reference solutions</summary>
                {links
                  .filter((x) => x.type === "solution")
                  .map((x) => (
                    <a className="related-link" href={href(x)} key={x.id}>
                      {x.title}
                    </a>
                  ))}
              </details>
            </section>
          )}
          <section className="panel">
            <h2>Related lessons</h2>
            <ResourceList items={related} />
          </section>
        </aside>
      </div>
    </>
  );
}
