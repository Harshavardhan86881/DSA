import fs from "node:fs";
import path from "node:path";
import assert from "node:assert/strict";
import { root, scan } from "./content.mjs";
const dist = path.join(root, "web/dist"),
  manifest = scan();
const index = fs.readFileSync(path.join(dist, "index.html"), "utf8");
const assets = [...index.matchAll(/(?:src|href)="([^"]+\.(?:js|css))"/g)].map(
  (m) => m[1],
);
assert.ok(assets.length >= 2);
for (const asset of assets) {
  assert.ok(asset.startsWith("/DSA/"), "Project base path is missing");
  assert.ok(fs.existsSync(path.join(dist, asset.slice("/DSA/".length))));
}
for (const r of manifest.resources.filter((r) => r.format !== "md")) {
  const file = path.join(dist, "course", r.id + ".txt");
  assert.equal(
    fs.readFileSync(file, "utf8"),
    r.text,
    `Download changed: ${r.id}`,
  );
}
console.log(
  `Verified ${assets.length} /DSA/ assets and ${manifest.resources.filter((r) => r.format !== "md").length} verbatim downloads.`,
);
