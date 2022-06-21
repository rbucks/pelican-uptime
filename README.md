# Development
Run this in a tab in Terminal

```bash
$ pelican -lr content -o docs -s pelicanconf.py

  --- AutoReload Mode: Monitoring `content`, `theme` and `settings` for changes. ---
Serving site at: http://127.0.0.1:8000 - Tap CTRL-C to stop

-> Modified: settings, content, theme, extra/robots.txt, extra/favicon.ico, extra/sitemap-index.xml, extra/sitemap-statuspages-0.xml, extra/sitemap.xml. re-generating...
Done: Processed 1 article, 0 drafts, 0 hidden articles, 1 page, 0 hidden pages and 0 draft pages in 0.19 seconds.
```
# Deployment to GitHub
```bash
$ pelican content -o docs -s pelicanconf.py
$ ghp-import docs
$ git push origin gh-pages
```