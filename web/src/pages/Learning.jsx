import { useState } from "react";
import {
  ArrowRight,
  ArrowUpRight,
  BookOpen,
  Code2,
  Layers,
  CalendarDays,
  CheckCircle2,
} from "lucide-react";
import { weeks, resources, href, byId } from "../content";
import { useProgress } from "../lib/useProgress";
import { stats, dateKey, reviewNext, streaks } from "../lib/progress.mjs";
import {
  Heading,
  ResourceList,
  ProgressBar,
  Section,
  Empty,
} from "../components/Common";
export function Metrics() {
  const { data } = useProgress(),
    s = stats(resources, data);
  const due = resources.filter(
    (r) => data.reviews[r.id]?.due <= dateKey(),
  ).length;
  return (
    <div className="metrics">
      {[
        [
          BookOpen,
          "Lessons completed",
          `${s.done} / ${s.lessons}`,
          `${s.percent}% of your learning path`,
        ],
        [
          Code2,
          "Problems solved",
          `${s.solved} / ${s.problems}`,
          "One problem at a time",
        ],
        [Layers, "Weeks available", weeks.length, "A structured path forward"],
        [
          CalendarDays,
          "Reviews due",
          due,
          due ? "Ready for a refresh" : "All caught up for now",
        ],
      ].map(([Icon, label, value, sub]) => (
        <div className="metric" key={label}>
          <span className="metric-label">
            <Icon size={17} />
            {label}
          </span>
          <strong>{value}</strong>
          <small>{sub}</small>
        </div>
      ))}
    </div>
  );
}
export function WeekCards({ compact = false }) {
  const { data, complete } = useProgress();
  return (
    <div className="week-grid">
      {weeks.slice(0, compact ? 3 : weeks.length).map((w) => {
        const items = resources.filter((r) => r.week === w.id),
          s = stats(items, data);
        return (
          <article className="week-card" key={w.id}>
            <div className="week-card-top">
              <span className="week-number">
                {String(w.number).padStart(2, "0")}
              </span>
              <span className="pill">
                {!s.done
                  ? "Not started"
                  : s.done === s.lessons
                    ? "Completed"
                    : "In progress"}
              </span>
            </div>
            <h3>{w.title}</h3>
            <p>
              {w.topics.join(" · ") || "Explore the week’s learning resources"}
            </p>
            <div className="progress-label">
              <span>
                {s.done} / {s.lessons} lessons
              </span>
              <strong>{s.percent}%</strong>
            </div>
            <ProgressBar value={s.percent} />
            <details>
              <summary>
                Explore week <ArrowRight size={15} />
              </summary>
              <div className="week-resources">
                {w.topics.map((topic) => (
                  <div key={topic}>
                    <div className="topic-heading">
                      <strong>{topic}</strong>
                      <button
                        className="text-button"
                        onClick={() => {
                          const lessons = items.filter(
                            (r) => r.type === "lesson" && r.topic === topic,
                          );
                          const on = !lessons.every(
                            (r) => data.completed[r.id],
                          );
                          for (const r of lessons) complete(r.id, on);
                        }}
                      >
                        {" "}
                        {items
                          .filter(
                            (r) => r.type === "lesson" && r.topic === topic,
                          )
                          .every((r) => data.completed[r.id])
                          ? "✓ Complete"
                          : "Mark complete"}
                      </button>
                    </div>
                    <ResourceList
                      items={items.filter(
                        (r) => r.type === "lesson" && r.topic === topic,
                      )}
                    />
                  </div>
                ))}
                <a href={`#/browse?week=${w.id}`}>
                  All {items.length} resources <ArrowUpRight size={14} />
                </a>
              </div>
            </details>
          </article>
        );
      })}
    </div>
  );
}
export function Dashboard() {
  const [today] = useState(() => new Date());
  const { data } = useProgress(),
    lessons = resources.filter((r) => r.type === "lesson"),
    next = byId.get(data.last) || lessons.find((r) => !data.completed[r.id]);
  const plans = resources.filter((r) => r.type === "plan"),
    day = today.getDay(),
    plan =
      plans.find(
        (r) =>
          r.week === (next?.week || weeks[0]?.id) &&
          (day === 0 ? r.id.includes("sunday") : r.id.includes(`day-0${day}`)),
      ) || plans[0];
  return (
    <>
      <Heading title="A little progress, every day.">
        Your path to stronger problem-solving starts with the next small step.
      </Heading>
      <div className="hero">
        <div>
          <span className="eyebrow">STAY CURIOUS. KEEP BUILDING.</span>
          <h2>
            Build the thinking.
            <br />
            Not just the solution.
          </h2>
          <p>
            Learn the patterns, practice with purpose, and make
            <br className="desktop-break" /> what you learn stick.
          </p>
          <a className="button primary" href={next ? href(next) : "#/roadmap"}>
            {data.last ? "Continue learning" : "Start learning"}{" "}
            <ArrowRight size={17} />
          </a>
        </div>
        <div className="hero-art" aria-hidden="true">
          <div className="code-window">
            <span className="dots">● ● ●</span>
            <pre>
              <span>def</span> grow_every_day():{"\n"} learn(){"\n"} practice()
              {"\n"} <span>repeat</span>()
            </pre>
            <div className="code-caption">
              <CheckCircle2 size={15} /> Progress over perfection
            </div>
          </div>
          <div className="float-symbol">{"{ }"}</div>
        </div>
      </div>
      <Metrics />
      <div className="dashboard-columns">
        <Section title="Pick up where you left off" link="#/roadmap">
          {next ? (
            <>
              <div className="continue-info">
                <span className="resource-icon">
                  <BookOpen size={22} />
                </span>
                <div>
                  <span className="eyebrow">
                    WEEK {weeks.find((w) => w.id === next.week)?.number} ·{" "}
                    {next.type.toUpperCase()}
                  </span>
                  <h3>{next.title}</h3>
                  <p>{next.topic}</p>
                </div>
              </div>
              <a className="button secondary full" href={href(next)}>
                Open resource <ArrowRight size={16} />
              </a>
            </>
          ) : (
            <Empty>
              All available lessons are complete. Try a practice problem.
            </Empty>
          )}
        </Section>
        <Section title="Today's study plan" link="#/plans">
          {plan ? (
            <>
              <span className="plan-date">
                <CalendarDays size={16} />
                {today.toLocaleDateString(undefined, {
                  weekday: "long",
                  month: "short",
                  day: "numeric",
                })}
              </span>
              <h3>{plan.title}</h3>
              <p className="muted">
                Follow the original time blocks at your own pace. Planned time
                is not recorded study time.
              </p>
              <a href={href(plan)} className="text-link">
                Open today's plan <ArrowUpRight size={16} />
              </a>
            </>
          ) : (
            <Empty>No daily plans are available yet.</Empty>
          )}
        </Section>
      </div>
      <Section title="Your learning roadmap" link="#/roadmap">
        <p className="section-subtitle">
          A clear path. A steady pace. One concept at a time.
        </p>
        <WeekCards compact />
      </Section>
      <div className="dashboard-columns">
        <Section title="Time for a refresh" link="#/revision">
          <RevisionItems limit={3} />
        </Section>
        <Section title="Make it a habit">
          <p className="muted">
            Learning is a practice, not a race. Your activity starts when you
            complete, attempt, or review something.
          </p>
          <div className="habit-stat">
            {streaks(data.activity).current}
            <span>day current streak</span>
          </div>
          <a className="text-link" href="#/statistics">
            See your activity <ArrowUpRight size={16} />
          </a>
        </Section>
      </div>
    </>
  );
}
export function Roadmap() {
  return (
    <>
      <Heading title="Your learning roadmap">
        Explore every week, from first principles to interview-ready thinking.
      </Heading>
      <WeekCards />
    </>
  );
}
export function RevisionItems({ limit }) {
  const { data, update } = useProgress();
  const items = resources
    .filter((r) => data.reviews[r.id])
    .sort((a, b) =>
      data.reviews[a.id].due.localeCompare(data.reviews[b.id].due),
    );
  return items.length ? (
    <div className="revision-list">
      {items.slice(0, limit || items.length).map((r) => {
        const v = data.reviews[r.id],
          today = dateKey();
        return (
          <div className="review-row" key={r.id}>
            <div>
              <a href={href(r)}>
                <strong>{r.title}</strong>
              </a>
              <small>
                {v.due < today
                  ? "Overdue"
                  : v.due === today
                    ? "Due today"
                    : "Upcoming"}{" "}
                · {v.due}
                {v.last ? ` · Last reviewed ${v.last}` : ""}
              </small>
            </div>
            <button
              className="button secondary"
              onClick={() =>
                update((d) => {
                  d.reviews[r.id] = reviewNext(v);
                  return d;
                })
              }
            >
              Reviewed <CheckCircle2 size={14} />
            </button>
          </div>
        );
      })}
    </div>
  ) : (
    <Empty>
      Complete a lesson or mark any resource for revision to start your review
      schedule.
    </Empty>
  );
}
export function Revision() {
  return (
    <>
      <Heading title="Make the knowledge stick">
        Review after 1, 3, 7, 14, and 30 days. After that, keep a monthly
        rhythm.
      </Heading>
      <Section title="Your review queue">
        <RevisionItems />
      </Section>
      <Section title="Revision resources">
        <ResourceList items={resources.filter((r) => r.type === "revision")} />
      </Section>
    </>
  );
}
export function Statistics() {
  const { data } = useProgress(),
    s = stats(resources, data),
    st = streaks(data.activity);
  return (
    <>
      <Heading title="Small steps. Real progress.">
        Only your recorded activity. No estimated study time or invented
        history.
      </Heading>
      <Metrics />
      <div className="dashboard-columns">
        <Section title="Learning progress">
          <div className="big-percent">
            {s.percent}
            <span>%</span>
          </div>
          <ProgressBar value={s.percent} />
          <p className="muted">
            {s.done} completed lessons · {s.attempted} problems with a recorded
            status
          </p>
        </Section>
        <Section title="Your consistency">
          <div className="streak-pair">
            <div>
              <strong>{st.current}</strong>
              <span>Current streak</span>
            </div>
            <div>
              <strong>{st.longest}</strong>
              <span>Longest streak</span>
            </div>
          </div>
          <p className="muted">
            Activity days count completions, attempts, and reviews, not page
            views.
          </p>
        </Section>
      </div>
      <Section title="Recorded activity">
        {data.activity.length ? (
          <div className="activity-grid">
            {data.activity.map((day) => (
              <span className="activity-day" key={day}>
                <CheckCircle2 size={14} />
                {day}
              </span>
            ))}
          </div>
        ) : (
          <Empty>
            No activity recorded yet. Complete your first lesson to get started.
          </Empty>
        )}
      </Section>
    </>
  );
}
export function Library({ mode = "browse", query = "" }) {
  const params = new URLSearchParams(query),
    [week, setWeek] = useState(params.get("week") || ""),
    [type, setType] = useState(""),
    [topic, setTopic] = useState(""),
    [status, setStatus] = useState(""),
    [difficulty, setDifficulty] = useState(""),
    [q, setQ] = useState(params.get("q") || "");
  const { data } = useProgress();
  const topics = [
    ...new Set(
      resources.filter((r) => !week || r.week === week).map((r) => r.topic),
    ),
  ].sort();
  const items = resources.filter(
    (r) =>
      (mode !== "practice" || r.type === "problem") &&
      (mode !== "plans" || r.type === "plan") &&
      (!params.get("path") || r.id.startsWith(params.get("path") + "/")) &&
      (!week || r.week === week) &&
      (!type || r.type === type) &&
      (!topic || r.topic === topic) &&
      (!difficulty || r.difficulty === difficulty) &&
      (!status ||
        (status === "Complete"
          ? !!data.completed[r.id]
          : status === "Not started"
            ? !data.completed[r.id] && !data.problems[r.id]
            : data.problems[r.id] === status)) &&
      q
        .toLowerCase()
        .trim()
        .split(/\s+/)
        .every((term) => r.search.includes(term)),
  );
  // Exact title matches rise above matches found only in full lesson text.
  if (q.trim())
    items.sort(
      (a, b) =>
        Number(b.title.toLowerCase().includes(q.toLowerCase().trim())) -
        Number(a.title.toLowerCase().includes(q.toLowerCase().trim())),
    );
  return (
    <>
      <Heading
        title={
          mode === "practice"
            ? "The practice room"
            : mode === "plans"
              ? "A plan for every day"
              : "Explore your library"
        }
      >
        {mode === "plans"
          ? "Original daily plans, time blocks, goals, and tasks. Plan completion is self-reported."
          : "Find the right resource. Build understanding through deliberate practice."}
      </Heading>
      <div className="filter-panel">
        <label className="search-label">
          Search resources
          <input
            value={q}
            onChange={(e) => setQ(e.target.value)}
            placeholder="Try binary search, arrays, recursion…"
          />
        </label>
        <div className="filter-row">
          <label>
            Week
            <select
              value={week}
              onChange={(e) => {
                setWeek(e.target.value);
                setTopic("");
              }}
            >
              <option value="">All weeks</option>
              {weeks.map((w) => (
                <option key={w.id} value={w.id}>
                  Week {w.number} · {w.title}
                </option>
              ))}
            </select>
          </label>
          <label>
            Topic
            <select value={topic} onChange={(e) => setTopic(e.target.value)}>
              <option value="">All topics</option>
              {topics.map((t) => (
                <option key={t}>{t}</option>
              ))}
            </select>
          </label>
          {mode === "browse" && (
            <label>
              Resource type
              <select value={type} onChange={(e) => setType(e.target.value)}>
                <option value="">All types</option>
                {[...new Set(resources.map((r) => r.type))].map((t) => (
                  <option key={t}>{t}</option>
                ))}
              </select>
            </label>
          )}
          {mode === "practice" && (
            <label>
              Difficulty
              <select
                value={difficulty}
                onChange={(e) => setDifficulty(e.target.value)}
              >
                <option value="">All difficulties</option>
                {[
                  ...new Set(
                    resources
                      .filter((r) => r.type === "problem")
                      .map((r) => r.difficulty),
                  ),
                ].map((d) => (
                  <option key={d}>{d}</option>
                ))}
              </select>
            </label>
          )}
          <label>
            Status
            <select value={status} onChange={(e) => setStatus(e.target.value)}>
              <option value="">All statuses</option>
              {["Not started", "Complete", "Attempted", "Solved", "Review"].map(
                (s) => (
                  <option key={s}>{s}</option>
                ),
              )}
            </select>
          </label>
          <button
            className="text-button"
            onClick={() => {
              setQ("");
              setWeek("");
              setType("");
              setTopic("");
              setStatus("");
              setDifficulty("");
              location.hash = `#/${mode}`;
            }}
          >
            Clear filters
          </button>
        </div>
      </div>
      <div className="results-label">
        {items.length} resources
        {mode === "plans" && week && !items.length
          ? " · No daily plan exists for this week."
          : ""}
      </div>
      <ResourceList items={items} />
    </>
  );
}
