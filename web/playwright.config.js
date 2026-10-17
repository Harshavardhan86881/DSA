import { defineConfig } from "@playwright/test";
let launchOptions = {};
if (process.env.DSA_BUNDLED_BROWSER) {
  const { default: chromium } = await import("@sparticuz/chromium");
  launchOptions = {
    executablePath: await chromium.executablePath(),
    args: chromium.args.filter(
      (a) =>
        ![
          "--single-process",
          "--disable-web-security",
          "--allow-running-insecure-content",
        ].includes(a),
    ),
  };
}
export default defineConfig({
  testDir: "./tests/browser",
  workers: 1,
  use: {
    baseURL: process.env.DSA_TEST_URL || "http://localhost:5173/DSA/",
    launchOptions,
    headless: true,
  },
  webServer: process.env.DSA_TEST_URL
    ? undefined
    : {
        command: "npm run dev",
        url: "http://localhost:5173/DSA/",
        reuseExistingServer: !process.env.CI,
      },
  reporter: "list",
});
