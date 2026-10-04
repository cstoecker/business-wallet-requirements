// Accessibility check with axe-core (WCAG 2.1 AA + best practice) on key pages at desktop and phone width.
// Usage: serve the built site (python3 -m http.server 4000 -d _site), then
//   PLAYWRIGHT=/opt/node-tools/node_modules/playwright AXE=/tmp/axe/node_modules/axe-core/axe.min.js CHROME=/opt/pw-browsers/chromium-1194/chrome-linux/chrome node scripts/check_a11y.js
// Prints one line per violation type; no output means no violations.
const { chromium } = require(process.env.PLAYWRIGHT || 'playwright');
const fs = require('fs'); const axe = fs.readFileSync(process.env.AXE || 'node_modules/axe-core/axe.min.js', 'utf8');
const pages = ['/', '/requirements/', '/requirements/ebw-tru-012/', '/requirements/review/', '/concepts/trust-list/', '/architecture/decisions/dec-02/', '/architecture/brief/', '/legal/roadmap/', '/downloads/', '/about/', '/contact/', '/figures/'];
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROME || undefined, args: ['--no-sandbox'] });
  const all = {};
  for (const vp of [{ width: 1400, height: 900 }, { width: 390, height: 800 }]) {
    const pg = await b.newPage({ viewport: vp });
    for (const p of pages) {
      await pg.goto((process.env.BASE || 'http://localhost:4000') + p); await pg.waitForTimeout(400);
      await pg.evaluate(axe); const r = await pg.evaluate(() => axe.run({ runOnly: ['wcag2a', 'wcag2aa', 'wcag21aa', 'best-practice'] }));
      for (const v of r.violations) { const k = v.id; all[k] = all[k] || { impact: v.impact, help: v.help, pages: new Set(), n: 0, sample: v.nodes[0].html.slice(0, 140), target: v.nodes[0].target.join(' ') }; all[k].pages.add(p + '@' + vp.width); all[k].n += v.nodes.length; }
    }
  }
  for (const [k, v] of Object.entries(all)) console.log(v.impact, k, '|', v.help, '| nodes', v.n, '| pages', [...v.pages].length, '|', v.target, '|', v.sample);
  await b.close();
})();
