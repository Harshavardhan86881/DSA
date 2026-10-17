import { useState, useEffect, useCallback, useRef } from "react";
import { Context } from "./useProgress";
import { load, KEY, blank, dateKey, addDays } from "./progress.mjs";
export function Provider({ children }) {
  const [initial] = useState(() =>
    load({ getItem: (key) => window.localStorage.getItem(key) }),
  );
  const storageNeedsRecovery = useRef(!!initial.error);
  const [data, setData] = useState(initial.data),
    [error, setError] = useState(initial.error),
    [message, setMessage] = useState("");
  const [theme, setThemeState] = useState(
    () =>
      data.theme ||
      (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light"),
  );
  useEffect(() => {
    document.documentElement.dataset.theme = theme;
  }, [theme]);
  const update = useCallback(
    (fn, notice = "Progress saved in this browser", activity = true) => {
      setData((old) => {
        const next = fn(structuredClone(old));
        if (activity)
          next.activity = [...new Set([...next.activity, dateKey()])].sort();
        if (storageNeedsRecovery.current && notice === "Resource opened")
          return next;
        storageNeedsRecovery.current = false;
        try {
          localStorage.setItem(KEY, JSON.stringify(next));
          setError("");
        } catch {
          setError(
            "Storage is unavailable or full. Changes only last for this session. Export a backup.",
          );
        }
        return next;
      });
      setMessage(notice);
    },
    [],
  );
  const complete = (id, on) =>
    update(
      (d) => {
        if (on) {
          d.completed[id] = dateKey();
          if (!d.reviews[id])
            d.reviews[id] = { step: 0, last: null, due: addDays(dateKey(), 1) };
        } else delete d.completed[id];
        return d;
      },
      on ? "Completion saved" : "Completion removed",
      on,
    );
  const reset = () =>
    update(() => ({ ...blank(), theme }), "Progress reset", false);
  const setTheme = (t) => {
    setThemeState(t);
    update((d) => ({ ...d, theme: t }), "Theme updated", false);
  };
  return (
    <Context.Provider
      value={{ data, update, complete, reset, theme, setTheme }}
    >
      {children}
      {error && (
        <div className="storage-alert" role="alert">
          {error}
        </div>
      )}
      <span className="sr-only" role="status">
        {message}
      </span>
    </Context.Provider>
  );
}
