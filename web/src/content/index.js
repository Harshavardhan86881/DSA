import manifest from "./manifest.json";
export const { weeks, resources } = manifest;
export const byId = new Map(resources.map((r) => [r.id, r]));
export const href = (r) => `#/read/${encodeURIComponent(r.id)}`;
export const source = (r) =>
  `https://github.com/Harshavardhan86881/DSA/blob/main/${r.id}`;
