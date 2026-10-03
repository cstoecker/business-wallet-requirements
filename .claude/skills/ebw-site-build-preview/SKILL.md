---
name: ebw-site-build-preview
description: Build, check, preview and push the European Business Wallet Requirements site (Jekyll, Just the Docs). Use after any content, style or script change, before committing, and whenever the user asks to push or to see the HTML on the fork (cstoecker).
---

# Build, check and preview the site

Repo: `cstoecker/business-wallet-requirements` (fork of `spherity/business-wallet-requirements`). Work branch: `claude/friendly-brown-gplwfl`. Never push to `main`, never open a pull request unless the user asks.

## Steps

1. **Data checks:** `python3 scripts/check_concepts.py` (requirements, sources, concepts, figures, brand rules; must print `OK`).
2. **Downloads:** `python3 scripts/build_downloads.py` (Excel, CSV and JSON-LD into `assets/downloads/`, gitignored).
3. **Local build** (the `jekyll` CLI does not run here; call the library):
   ```
   printf 'url: http://localhost:4000\nbaseurl: ""\n' > /tmp/local.yml
   rm -rf /tmp/ebw-local/*
   BUNDLE_GEMFILE=$PWD/Gemfile bundle exec ruby -e 'require "jekyll"; Jekyll::Commands::Build.process({"source"=>Dir.pwd,"destination"=>"/tmp/ebw-local","config"=>["_config.yml","/tmp/local.yml"],"quiet"=>true})' 2>&1 | grep -i "liquid\|error"
   ```
4. **Site checks:** `BASEURL= python3 scripts/check_site.py /tmp/ebw-local` (metadata, JSON-LD, sitemap, internal links, Excel consistency; must print `OK`). A Liquid error means a page silently lost content: look for text like `## Heading` rendered inline.
5. **Look at it:** serve with `cd /tmp/ebw-local && setsid nohup python3 -m http.server 4000 >/dev/null 2>&1 < /dev/null &` (never `pkill -f` a pattern that matches your own command line; never delete the served directory without restarting the server). Screenshot: `/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --no-sandbox --disable-gpu --window-size=1500,1700 --screenshot=/tmp/x.png http://localhost:4000/<path>/`. For interaction tests use `/opt/node-tools/node_modules/playwright` with `executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'`.
6. **Commit and push:** commit message ends with the attribution lines from the session reminder; `git push -u origin claude/friendly-brown-gplwfl` (retry up to four times with 2, 4, 8, 16 s backoff on network errors only).
7. **Preview on `gh-pages`** (orphan branch, noindex, force-pushed):
   ```
   rm -rf /tmp/ebw-prev && BUNDLE_GEMFILE=$PWD/Gemfile bundle exec ruby -e 'require "jekyll"; Jekyll::Commands::Build.process({"source"=>Dir.pwd,"destination"=>"/tmp/ebw-prev","config"=>["_config.yml","_config.preview.yml"],"quiet"=>true})'
   cd /tmp/ebw-prev && rm -f a3fe5ee5880a644a4124489d4d1fce86.txt && touch .nojekyll && git init -q -b gh-pages && git add -A && git -c user.name=Claude -c user.email=noreply@anthropic.com commit -q -m "Preview build" && git remote add origin <origin url> && git push -f origin gh-pages
   ```
   Live at https://cstoecker.github.io/business-wallet-requirements/ one to two minutes after the push.

## Gotchas

- Liquid: an empty string is truthy; compare with `!= ""`. `for x in "a,b" | split` is invalid: `assign` first. Flow-style YAML breaks on commas in values: use block style or quote.
- A `{%- assign ... -%}` right after a paragraph can swallow the blank line before the next heading.
- Requirement front matter key is `req_id` (Jekyll reserves `id`). Concept stubs are `noindex` and `sitemap: false` exactly while status is `planned`.
- Fonts come from Google Fonts until self-hosted (launch blocker, see docs/04).

## Report to the user

Say what was pushed (commit), the preview link, what the checkers said, and what was not verified.
