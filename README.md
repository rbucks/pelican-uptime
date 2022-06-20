# Development
Run this in a tab in Terminal

```bash
$ "pelican" -lr "/Users/rbucks/Documents/Code/Uptime/pelican/content" -o "/Users/rbucks/Documents/Code/Uptime/pelican/docs" -s "/Users/rbucks/Documents/Code/Uptime/pelican/pelicanconf.py"
```
# Deployment to GitHub
```bash
$ pelican content -o docs -s pelicanconf.py
$ ghp-import docs
$ git push origin gh-pages
```