import { useEffect, useState, useRef, Component } from "react";
import {
  LayoutDashboard,
  Map,
  CalendarDays,
  Code2,
  RotateCcw,
  ChartNoAxesCombined,
  Settings as SettingsIcon,
  Sun,
  Moon,
  Search,
  Menu,
  X,
  ChevronLeft,
  ArrowUpRight,
  BookOpen,
} from "lucide-react";
import { Provider } from "./lib/store";
import { useProgress } from "./lib/useProgress";
import { weeks, resources, href } from "./content";
import { stats } from "./lib/progress.mjs";
import { ProgressBar, Heading, Empty } from "./components/Common";
import {
  Dashboard,
  Roadmap,
  Library,
  Revision,
  Statistics,
} from "./pages/Learning";
import { Reader } from "./pages/Reader";
import { Settings } from "./pages/Settings";
const nav = [
  ["dashboard", "Overview", LayoutDashboard],
  ["roadmap", "Learning roadmap", Map],
  ["plans", "Daily study plans", CalendarDays],
  ["practice", "Problem practice", Code2],
  ["revision", "Revision queue", RotateCcw],
  ["statistics", "Statistics", ChartNoAxesCombined],
  ["browse", "Resource library", BookOpen],
];
class Boundary extends Component {
  state = { error: false };
  static getDerivedStateFromError() {
    return { error: true };
  }
  render() {
    return this.state.error ? (
      <main>
        <Heading title="Something couldn't be loaded" />
        <p>
          Your course files are safe. Reload the page or return to the
          dashboard.
        </p>
        <a href="#/dashboard" onClick={() => location.reload()}>
          Return to dashboard
        </a>
      </main>
    ) : (
      this.props.children
    );
  }
}
function Shell() {
  const [hash, setHash] = useState(location.hash || "#/dashboard"),
    [open, setOpen] = useState(false),
    [collapsed, setCollapsed] = useState(false),
    [search, setSearch] = useState("");
  const { data, theme, setTheme } = useProgress();
  const [mobile, setMobile] = useState(
    () => matchMedia("(max-width: 800px)").matches,
  );
  const drawer = useRef(null),
    opener = useRef(null);
  useEffect(() => {
    const mq = matchMedia("(max-width: 800px)");
    const change = () => setMobile(mq.matches);
    mq.addEventListener("change", change);
    return () => mq.removeEventListener("change", change);
  }, []);
  useEffect(() => {
    if (open && mobile) drawer.current?.querySelector("a,button")?.focus();
  }, [open, mobile]);
  function closeDrawer() {
    setOpen(false);
    requestAnimationFrame(() => opener.current?.focus());
  }
  function drawerKeys(e) {
    if (!mobile || !open) return;
    if (e.key === "Escape") {
      closeDrawer();
      return;
    }
    if (e.key === "Tab") {
      const links = [...drawer.current.querySelectorAll("a,button")].filter(
        (el) => el.getClientRects().length,
      );
      const first = links[0],
        last = links.at(-1);
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    }
  }

  useEffect(() => {
    const change = () => {
      setHash(location.hash);
      setOpen(false);
      setSearch("");
      window.scrollTo(0, 0);
    };
    window.addEventListener("hashchange", change);
    return () => window.removeEventListener("hashchange", change);
  }, []);
  const [route, query = ""] = hash.replace(/^#\/?/, "").split("?"),
    page = route.split("/")[0] || "dashboard",
    s = stats(resources, data);
  let id = "";
  try {
    id = decodeURIComponent(route.slice(5));
  } catch {
    /* Friendly missing-resource state handles malformed routes. */
  }
  const hits = search.trim()
    ? resources
        .filter((r) =>
          search
            .toLowerCase()
            .trim()
            .split(/\s+/)
            .every((t) => r.search.includes(t)),
        )
        .slice(0, 7)
    : [];
  const title =
    nav.find((n) => n[0] === page)?.[1] ||
    (page === "read"
      ? "Learning workspace"
      : page === "settings"
        ? "Settings"
        : "Workspace");
  return (
    <div className={`app ${collapsed ? "collapsed" : ""}`}>
      <a
        className="skip"
        href="#main-content"
        onClick={(e) => {
          e.preventDefault();
          document.getElementById("main-content")?.focus();
        }}
      >
        Skip to content
      </a>
      {open && (
        <button
          className="scrim"
          aria-label="Close navigation"
          onClick={closeDrawer}
        />
      )}
      <aside
        ref={drawer}
        className={`sidebar ${open ? "open" : ""}`}
        inert={mobile && !open}
        onKeyDown={drawerKeys}
        aria-label="Workspace sidebar"
      >
        <a className="brand" href="#/dashboard">
          <span className="brand-mark">{"</>"}</span>
          <span>
            algo<span className="brand-light">space</span>
            <small>YOUR DSA WORKSPACE</small>
          </span>
        </a>
        <button
          className="mobile-close icon-button"
          aria-label="Close navigation"
          onClick={closeDrawer}
        >
          <X size={20} />
        </button>
        <div className="nav-caption">WORKSPACE</div>
        <nav aria-label="Main navigation">
          {nav.map(([path, label, Icon]) => (
            <a
              key={path}
              href={`#/${path}`}
              aria-current={page === path ? "page" : undefined}
              className={page === path ? "active" : ""}
              title={label}
            >
              <Icon size={19} />
              <span>{label}</span>
              {path === "roadmap" && <small>{weeks.length}</small>}
            </a>
          ))}
        </nav>
        <div className="sidebar-bottom">
          <div className="sidebar-progress">
            <div className="progress-label">
              <span>Your learning journey</span>
              <strong>{s.percent}%</strong>
            </div>
            <ProgressBar value={s.percent} />
            <small>
              {s.done} of {s.lessons} lessons completed
            </small>
          </div>
          <a href="#/settings" className={page === "settings" ? "active" : ""}>
            <SettingsIcon size={18} />
            <span>Settings & data</span>
          </a>
          <a
            href="https://github.com/Harshavardhan86881/DSA"
            target="_blank"
            rel="noreferrer"
          >
            <Code2 size={18} />
            <span>View repository</span>
            <ArrowUpRight size={14} />
          </a>
          <div className="profile">
            <span className="avatar">Y</span>
            <div>
              <strong>Your learning space</strong>
              <small>Local progress · Personal</small>
            </div>
            <span className="online-dot" />
          </div>
        </div>
      </aside>
      <div className="workspace" inert={mobile && open}>
        <header className="topbar">
          <div className="topbar-title">
            <button
              className="icon-button desktop-toggle"
              aria-label={collapsed ? "Expand sidebar" : "Collapse sidebar"}
              onClick={() => setCollapsed(!collapsed)}
            >
              <ChevronLeft size={18} />
            </button>
            <button
              ref={opener}
              className="icon-button mobile-toggle"
              aria-label="Open navigation"
              aria-expanded={open}
              onClick={() => setOpen(true)}
            >
              <Menu size={21} />
            </button>
            <span>
              Workspace <span className="breadcrumb-slash">/</span>{" "}
              <strong>{title}</strong>
            </span>
          </div>
          <div className="topbar-actions">
            <div className="global-search">
              <Search size={16} />
              <input
                aria-label="Search all learning content"
                value={search}
                placeholder="Search anything…"
                onChange={(e) => setSearch(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === "Escape") setSearch("");
                  if (e.key === "Enter" && search.trim())
                    location.hash = `#/browse?q=${encodeURIComponent(search)}`;
                }}
              />
              {search && (
                <div
                  className="search-popover"
                  role="region"
                  aria-label="Search results"
                >
                  {hits.length ? (
                    hits.map((r) => (
                      <a key={r.id} href={href(r)}>
                        <strong>{r.title}</strong>
                        <small>
                          Week {weeks.find((w) => w.id === r.week)?.number} ·{" "}
                          {r.type} · {r.topic}
                        </small>
                      </a>
                    ))
                  ) : (
                    <p>No matching resources.</p>
                  )}
                  <a
                    className="search-all"
                    href={`#/browse?q=${encodeURIComponent(search)}`}
                  >
                    See all search results →
                  </a>
                </div>
              )}
            </div>
            <button
              className="icon-button theme-toggle"
              aria-label={`Switch to ${theme === "light" ? "dark" : "light"} theme`}
              onClick={() => setTheme(theme === "light" ? "dark" : "light")}
            >
              {theme === "light" ? <Moon size={19} /> : <Sun size={19} />}
            </button>
            <span className="avatar small-avatar">Y</span>
          </div>
        </header>
        <main id="main-content" tabIndex={-1}>
          {page === "dashboard" ? (
            <Dashboard />
          ) : page === "roadmap" ? (
            <Roadmap />
          ) : page === "read" ? (
            <Reader key={id} id={id} query={query} />
          ) : ["plans", "practice", "browse"].includes(page) ? (
            <Library key={hash} mode={page} query={query} />
          ) : page === "revision" ? (
            <Revision />
          ) : page === "statistics" ? (
            <Statistics />
          ) : page === "settings" ? (
            <Settings />
          ) : (
            <>
              <Heading title="Page not found" />
              <Empty>Choose a page from the sidebar to keep learning.</Empty>
              <a className="button primary" href="#/dashboard">
                Back to dashboard
              </a>
            </>
          )}
        </main>
        <footer>
          <span>Built for understanding, not just completion.</span>
          <span>
            One concept at a time <span className="footer-dot">✦</span>
          </span>
        </footer>
      </div>
    </div>
  );
}
export default function App() {
  return (
    <Boundary>
      <Provider>
        <Shell />
      </Provider>
    </Boundary>
  );
}
