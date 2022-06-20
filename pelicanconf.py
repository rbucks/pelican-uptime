AUTHOR = 'Uptime'
SITENAME = 'Uptime'
SITEURL = 'http://127.0.0.1:8000'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = "themes/uptime"

STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'extra/sitemap-index.xml', 'extra/sitemap-statuspages-0.xml', 'extra/sitemap.xml']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/sitemap-index.xml': {'path': 'sitemap-index.xml'},
    'extra/sitemap-statuspages-0.xml': {'path': 'sitemap-statuspages-0.xml'},
    'extra/sitemap.xml': {'path': 'sitemap.xml'}
}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True