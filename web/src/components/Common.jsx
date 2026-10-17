import { ArrowUpRight, BookOpen, Check, ChevronRight } from "lucide-react";
import { href } from "../content";
import { useProgress } from "../lib/useProgress";
export function Empty({ children = "No resources available yet." }) {
  return (
    <div className="empty">
      <BookOpen size={26} />
      <h3>A little room to grow</h3>
      <p>{children}</p>
    </div>
  );
}
export function Heading({
  eyebrow = "YOUR LEARNING WORKSPACE",
  title,
  children,
}) {
  return (
    <div className="page-heading">
      <span className="eyebrow">{eyebrow}</span>
      <h1>{title}</h1>
      {children && <p>{children}</p>}
    </div>
  );
}
export function ResourceList({ items }) {
  const { data } = useProgress();
  return items.length ? (
    <div className="resource-list">
      {items.map((r) => (
        <a key={r.id} href={href(r)} className="resource-row">
          <span
            className={`resource-icon ${data.completed[r.id] ? "done" : ""}`}
          >
            {data.completed[r.id] ? (
              <Check size={18} />
            ) : (
              <BookOpen size={18} />
            )}
          </span>
          <span className="resource-label">
            <strong>{r.title}</strong>
            <small>
              {r.topic} · {r.type}
              {r.difficulty ? ` · ${r.difficulty}` : ""}
            </small>
          </span>
          <span className="pill">
            {data.problems[r.id] ||
              (data.completed[r.id] ? "Complete" : r.type)}
          </span>
          <ChevronRight size={16} />
        </a>
      ))}
    </div>
  ) : (
    <Empty />
  );
}
export function ProgressBar({ value }) {
  return (
    <div
      className="progress-track"
      role="progressbar"
      aria-valuenow={value}
      aria-valuemin={0}
      aria-valuemax={100}
      aria-label="Lesson completion"
    >
      <span style={{ width: `${value}%` }} />
    </div>
  );
}
export function Section({ title, link, children }) {
  return (
    <section className="panel">
      <div className="section-heading">
        <h2>{title}</h2>
        {link && (
          <a href={link}>
            View all <ArrowUpRight size={14} />
          </a>
        )}
      </div>
      {children}
    </section>
  );
}
