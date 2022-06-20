# Deployment to GitHub

```bash
$ pelican content -o docs -s pelicanconf.py
$ ghp-import docs
$ git push origin gh-pages
```