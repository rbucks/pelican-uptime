# Development
Run this command to create a development server that automatically compiles updates to the static source files and serves the output. This uses by default the `output` folder and the `pelicanconf.py` settings file.  

```bash
$ pelican -lr content 

  --- AutoReload Mode: Monitoring `content`, `theme` and `settings` for changes. ---
Serving site at: http://127.0.0.1:8000 - Tap CTRL-C to stop

-> Modified: settings, content, theme, extra/robots.txt, extra/favicon.ico, extra/sitemap-index.xml, extra/sitemap-statuspages-0.xml, extra/sitemap.xml. re-generating...
Done: Processed 1 article, 0 drafts, 0 hidden articles, 1 page, 0 hidden pages and 0 draft pages in 0.19 seconds.
```
# Deployment to GitHub
Since GitHub Pages requires the output to compile into the `/docs` folder, which is different than the Pelican default `/output` folder, use this command to deploy. Note that we use `publishconf.py` to modify the settings for GitHub Pages. 
```bash
$ pelican content -o docs -s publishconf.py
$ ghp-import docs
$ git push origin gh-pages
```