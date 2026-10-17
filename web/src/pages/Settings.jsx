import { useState } from "react";
import { Heading, Section } from "../components/Common";
import { useProgress } from "../lib/useProgress";
import { validate } from "../lib/progress.mjs";
export function Settings() {
  const { data, update, reset, theme, setTheme } = useProgress(),
    [confirm, setConfirm] = useState(false),
    [message, setMessage] = useState("");
  function exportData() {
    const url = URL.createObjectURL(
      new Blob([JSON.stringify(data, null, 2)], { type: "application/json" }),
    );
    const a = document.createElement("a");
    a.href = url;
    a.download = "dsa-progress.json";
    a.click();
    URL.revokeObjectURL(url);
  }
  async function importData(e) {
    try {
      const file = e.target.files[0];
      if (!file) return;
      if (file.size > 2000000) throw Error("File too large (maximum 2 MB)");
      const next = validate(JSON.parse(await file.text()));
      if (
        window.confirm(
          "Replace current browser progress with this validated backup?",
        )
      ) {
        update(() => next, "Backup imported", false);
        setTheme(next.theme || theme);
        setMessage("Progress imported.");
      }
    } catch (err) {
      setMessage(`Import rejected: ${err.message}`);
    }
    e.target.value = "";
  }
  return (
    <>
      <Heading title="Make this space yours">
        Your learning, stored locally. No account. No tracking. No backend.
      </Heading>
      <Section title="Appearance">
        <label>
          Color theme
          <select value={theme} onChange={(e) => setTheme(e.target.value)}>
            <option value="light">Light</option>
            <option value="dark">Dark</option>
          </select>
        </label>
      </Section>
      <Section title="Your progress, your data">
        <p className="muted">
          Progress lives in this browser’s localStorage. It does not sync across
          devices. Export before clearing browser data. Records for removed
          resources are retained in backups but excluded from current content
          statistics.
        </p>
        <div className="actions">
          <button className="button primary" onClick={exportData}>
            Export progress
          </button>
          <label className="button secondary file-label">
            Import JSON
            <input
              type="file"
              accept="application/json,.json"
              onChange={importData}
            />
          </label>
        </div>
        <p role="status">{message}</p>
      </Section>
      <Section title="Revision schedule">
        <p>
          Reviews are suggested after 1 day, then 3, 7, 14, and 30 days
          following each review. Further reviews repeat every 30 days. Dates use
          your device’s local calendar, not elapsed 24-hour intervals.
        </p>
        <p className="muted">
          A practical default, not a universally optimal schedule. Manual
          revision is always available on resource pages. Custom intervals are
          not yet supported.
        </p>
      </Section>
      <Section title="Reset local progress">
        <p className="muted">
          This removes completion records, notes, problem statuses, and revision
          dates. Export first if you want a backup.
        </p>
        {confirm ? (
          <div className="confirmation" role="alert">
            <strong>Reset all progress in this browser?</strong>
            <div className="actions">
              <button
                className="button danger"
                onClick={() => {
                  reset();
                  setConfirm(false);
                  setMessage("Progress reset.");
                }}
              >
                Yes, reset everything
              </button>
              <button
                className="button secondary"
                onClick={() => setConfirm(false)}
              >
                Cancel
              </button>
            </div>
          </div>
        ) : (
          <button className="button danger" onClick={() => setConfirm(true)}>
            Reset progress
          </button>
        )}
      </Section>
    </>
  );
}
