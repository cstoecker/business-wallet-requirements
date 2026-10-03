// Notify IndexNow-enabled search engines about the URLs in the deployed sitemap.
// Adapted from the spherity-research deployment flow. Never fails the deployment: failures are warned and retried on the next run.
import { readFile } from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const arg = (name, fallback) => {
  const i = process.argv.indexOf(name);
  return i >= 0 && process.argv[i + 1] ? process.argv[i + 1] : fallback;
};
const sitemapFile = path.resolve(arg("--sitemap", "_site/sitemap.xml"));
const keyFile = arg("--key-file", "");
const dryRun = process.argv.includes("--dry-run");
const siteUrl = (process.env.SITE_URL || "https://spherity.github.io/business-wallet-requirements").replace(/\/+$/, "");
const key = String(
  process.env.INDEXNOW_KEY || (keyFile ? await readFile(path.resolve(keyFile), "utf8").catch(() => "") : "")
).trim();

if (!key) { console.log("INDEXNOW_KEY is not configured; skipping IndexNow notification."); process.exit(0); }
if (!/^[A-Za-z0-9_-]{8,128}$/.test(key)) { console.error("INDEXNOW_KEY must contain 8-128 letters, digits, underscores or hyphens."); process.exit(1); }

const xml = await readFile(sitemapFile, "utf8");
const decode = (v) => v.trim().replaceAll("&amp;", "&").replaceAll("&lt;", "<").replaceAll("&gt;", ">").replaceAll("&quot;", '"').replaceAll("&apos;", "'");
const urls = [...xml.matchAll(/<loc>([\s\S]*?)<\/loc>/gi)].map((m) => decode(m[1])).filter((u) => u.startsWith(siteUrl + "/") || u === siteUrl);
if (!urls.length) { console.error(`No ${siteUrl} URLs found in ${sitemapFile}.`); process.exit(1); }

const payload = { host: new URL(siteUrl).host, key, keyLocation: `${siteUrl}/${key}.txt`, urlList: [...new Set(urls)] };
if (dryRun) { console.log(`IndexNow dry run: ${payload.urlList.length} URLs for ${payload.host}, key location ${payload.keyLocation}.`); process.exit(0); }

let lastError;
for (let attempt = 1; attempt <= 3; attempt += 1) {
  try {
    const res = await fetch("https://api.indexnow.org/indexnow", { method: "POST", headers: { "content-type": "application/json; charset=utf-8" }, body: JSON.stringify(payload), signal: AbortSignal.timeout(20000) });
    if ([200, 202].includes(res.status)) { console.log(`IndexNow accepted ${payload.urlList.length} URLs (HTTP ${res.status}).`); process.exit(0); }
    lastError = new Error(`HTTP ${res.status}: ${(await res.text()).slice(0, 300)}`);
    if (res.status < 429 || res.status >= 500) break;
  } catch (e) { lastError = e; }
  if (attempt < 3) await new Promise((r) => setTimeout(r, attempt * 1000));
}
console.warn(`IndexNow notification did not complete: ${lastError?.message || "unknown error"}. The sitemap remains public; retry on the next deployment.`);
