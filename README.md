# Development

## Environment setup

This project uses venv to manage python dependencies

Here is an example on how to setup project dependencies locally

```
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```

## Notice

pelican often caches python sources, outputs, css files and sometimes troubleshooting is confusing. In order to ensure that environment is clear try to remove any `__pycache__`, `.sass-cache`, `output` folders

## How to run

Run this command to create a development server that automatically compiles updates to the static source files and serves the output. This uses by default the `output` folder and the `pelicanconf.py` settings file.

```bash
$ pelican

  --- AutoReload Mode: Monitoring `content`, `theme` and `settings` for changes. ---
Serving site at: http://127.0.0.1:8000 - Tap CTRL-C to stop

-> Modified: settings, content, theme, extra/robots.txt, extra/favicon.ico, extra/sitemap-index.xml, extra/sitemap-statuspages-0.xml, extra/sitemap.xml. re-generating...
Done: Processed 1 article, 0 drafts, 0 hidden articles, 1 page, 0 hidden pages and 0 draft pages in 0.19 seconds.
```

# Deployment to GitHub

Since GitHub Pages requires the output to compile into the `/docs` folder, which is different than the Pelican default `/output` folder, use this command to deploy. Note that we use `publishconf.py` to modify the settings for GitHub Pages.

```bash
$ pelican content -o docs -s publishconf.py
$ git push origin master
```

Pushing the updated `/docs` folder to the `master` branch deploys to GitHub.

# TODO

- Use jinja to make a better logos.html template based on the `edu-websites-uptime.md` file.
- Use the [HubSpot forms API](https://developers.hubspot.com/docs/api/marketing/forms) on all website forms
- Free tools API and pages
- CSS audit and purge
