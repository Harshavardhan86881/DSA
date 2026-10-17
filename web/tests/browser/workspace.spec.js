import { test, expect } from "@playwright/test";
import { scan } from "../../scripts/content.mjs";
const content = scan(),
  lessonCount = content.resources.filter((r) => r.type === "lesson").length,
  problemCount = content.resources.filter((r) => r.type === "problem").length;
const lesson = "week-01-foundations/lessons/arrays/arrays-and-lists.md";
const problem = "week-01-foundations/problems/easy/two-sum.md";
const read = (id) => `#/read/${encodeURIComponent(id)}`;
test("zero-state dashboard, roadmap, search, reader, persistent progress and revision", async ({
  page,
}) => {
  const errors = [];
  page.on("pageerror", (e) => errors.push(e.message));
  await page.goto("./");
  await expect(
    page.getByRole("heading", { name: "A little progress, every day." }),
  ).toBeVisible();
  await expect(
    page.getByText(`0 / ${lessonCount}`, { exact: true }),
  ).toBeVisible();
  await page.goto("./#/roadmap");
  await expect(page.locator(".week-card")).toHaveCount(content.weeks.length);
  await page.getByLabel("Search all learning content").fill("binary search");
  await expect(page.locator(".search-popover a").first()).toBeVisible();
  await page.locator(".search-popover a").first().click();
  await expect(page.locator(".reader")).toBeVisible();
  await page.goto("./" + read(lesson));
  await expect(page.locator(".markdown h1")).toContainText("Arrays");
  await expect(page.locator(".markdown pre").first()).toBeVisible();
  await page.getByLabel("Mark lesson complete").check();
  await page.reload();
  await expect(page.getByLabel("Mark lesson complete")).toBeChecked();
  await page.goto("./#/statistics");
  await expect(
    page.getByText(`1 / ${lessonCount}`, { exact: true }),
  ).toBeVisible();
  await page.goto("./#/revision");
  await expect(page.locator(".review-row")).toHaveCount(1);
  await page.getByRole("button", { name: "Reviewed" }).click();
  await expect(page.locator(".review-row")).toContainText("Last reviewed");
  await page.goto("./" + read(problem));
  await expect(page.locator(".markdown h1")).toHaveText("Two Sum");
  await page.getByLabel("Problem status").selectOption("Solved");
  await page.getByLabel("Personal notes").fill("Try complements");
  await page.reload();
  await expect(page.getByLabel("Problem status")).toHaveValue("Solved");
  await expect(page.getByLabel("Personal notes")).toHaveValue(
    "Try complements",
  );
  await page.goto("./#/plans");
  await expect(page.locator(".resource-row").first()).toBeVisible();
  await page.locator(".resource-row").first().click();
  await expect(page.locator(".markdown")).toContainText("45 min");
  await page.getByRole("button", { name: "Switch to dark theme" }).click();
  await page.reload();
  await expect(page.locator("html")).toHaveAttribute("data-theme", "dark");
  await page.goto("./#/settings");
  await page
    .getByRole("button", { name: "Reset progress", exact: true })
    .click();
  await expect(
    page.getByRole("button", { name: "Yes, reset everything" }),
  ).toBeVisible();
  await page.getByRole("button", { name: "Cancel", exact: true }).click();
  await page.goto("./" + read(lesson));
  await expect(page.getByLabel("Mark lesson complete")).toBeChecked();
  await page.goto("./#/settings");
  await page
    .getByRole("button", { name: "Reset progress", exact: true })
    .click();
  await page.getByRole("button", { name: "Yes, reset everything" }).click();
  await page.goto("./" + read(lesson));
  await expect(page.getByLabel("Mark lesson complete")).not.toBeChecked();
  await page.goto("./#/nonexistent");
  await expect(
    page.getByRole("heading", { name: "Page not found" }),
  ).toBeVisible();
  await page.goto("./" + read("unknown.md"));
  await expect(
    page.getByRole("heading", { name: "Resource not found" }),
  ).toBeVisible();
  expect(errors).toEqual([]);
});
test("search filters and safe corrupt storage recovery", async ({ page }) => {
  await page.goto("./#/practice");
  await page.getByLabel("Search resources").fill("two sum");
  await expect(page.locator(".resource-row").first()).toContainText("Two Sum");
  expect(await page.locator(".resource-row").count()).toBeLessThan(
    problemCount,
  );
  await page.getByLabel("Search resources").fill("no-such-resource");
  await expect(page.getByText("A little room to grow")).toBeVisible();
  await page.getByRole("button", { name: "Clear filters" }).click();
  await expect(page.locator(".resource-row").first()).toBeVisible();
  await page.evaluate(() => localStorage.setItem("dsa-workspace-v1", "{bad"));
  await page.reload();
  await expect(page.getByRole("alert")).toContainText("could not be read");
  await expect(page.locator(".resource-row").first()).toBeVisible();
});
for (const width of [375, 768, 1440])
  test(`responsive ${width}px, keyboard navigation, screenshots`, async ({
    page,
  }) => {
    await page.setViewportSize({ width, height: 1000 });
    await page.goto("./");
    await expect(page.locator(".hero")).toBeVisible();
    if (width < 801) {
      await page.getByRole("button", { name: "Open navigation" }).click();
      await expect(page.locator(".sidebar")).toBeVisible();
      await page.getByRole("link", { name: "Learning roadmap" }).click();
      await expect(page.locator(".sidebar")).not.toHaveClass(/open/);
      await page.goto("./");
    }
    await page.screenshot({
      path: `test-results/dashboard-${width}.png`,
      fullPage: true,
    });
    expect(
      await page.evaluate(
        () => document.documentElement.scrollWidth <= window.innerWidth,
      ),
    ).toBeTruthy();
    await page.goto("./" + read(lesson));
    await expect(page.locator(".markdown h1")).toBeVisible();
    expect(
      await page.evaluate(
        () => document.documentElement.scrollWidth <= window.innerWidth,
      ),
    ).toBeTruthy();
    await page.screenshot({
      path: `test-results/lesson-${width}.png`,
      fullPage: true,
    });
    await page.keyboard.press("Tab");
    await expect(page.locator(":focus")).toHaveCount(1);
  });
test("plan block controls, original duration warning, and relative Markdown navigation", async ({
  page,
}) => {
  await page.goto(
    "./" + read("week-01-foundations/curriculum/day-01-problem-solving.md"),
  );
  await expect(page.locator(".plan-tracker")).toContainText(
    "210 planned minutes",
  );
  await expect(page.locator(".plan-warning")).toContainText("240-minute plan");
  const block = page.locator(".block-task input").first();
  await block.check();
  await page.reload();
  await expect(page.locator(".block-task input").first()).toBeChecked();
  await page.goto(
    "./" +
      read(
        "week-06-backtracking-greedy-dynamic-programming/curriculum/day-01-backtracking.md",
      ),
  );
  await page
    .locator(".markdown")
    .getByRole("link", { name: "backtracking.md", exact: true })
    .click();
  await expect(page).toHaveURL(/read.*lessons/);
  await expect(page.locator(".markdown h1")).toContainText("Backtracking");
  await page.goBack();
  await expect(page.locator(".plan-tracker")).toBeVisible();
});
test("progress export/import validation and keyboard drawer dismissal", async ({
  page,
}) => {
  await page.goto("./#/settings");
  const download = page.waitForEvent("download");
  await page.getByRole("button", { name: "Export progress" }).click();
  expect((await download).suggestedFilename()).toBe("dsa-progress.json");
  await page
    .locator("input[type=file]")
    .setInputFiles({
      name: "invalid.json",
      mimeType: "application/json",
      buffer: Buffer.from('{"version":999}'),
    });
  await expect(page.getByRole("status").first()).toContainText(
    "Import rejected",
  );
  await page.setViewportSize({ width: 375, height: 900 });
  await page.getByRole("button", { name: "Open navigation" }).click();
  await page.keyboard.press("Escape");
  await expect(
    page.getByRole("button", { name: "Open navigation" }),
  ).toBeFocused();
  await expect(page.locator(".sidebar")).toHaveAttribute("inert", "");
});
