AUTHOR = 'Uptime'
SITENAME = 'Uptime.com'
SITEURL = 'http://127.0.0.1:8000'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = "themes/uptime"

STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/favicon.ico',
    'extra/sitemap-index.xml',
    'extra/sitemap-statuspages-0.xml',
    'extra/sitemap.xml',
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/sitemap-index.xml': {'path': 'sitemap-index.xml'},
    'extra/sitemap-statuspages-0.xml': {'path': 'sitemap-statuspages-0.xml'},
    'extra/sitemap.xml': {'path': 'sitemap.xml'}
}

PATH_METADATA = '(?P<dirname>.*)/(?P<basename>.*)\..*'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

# CATEGORY_SAVE_AS = TAG_SAVE_AS = AUTHOR_SAVE_AS = DRAFT_SAVE_AS = ARTICLE_SAVE_AS = #''
# title does not always correspond to URL
FILENAME_METADATA = '(?P<title>.*)'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Please keep this setting enabled. Clean up prevents from SCSS caching
# SCSS files are imported hierarchically from uptime.scss and build system cannot notice any SCSS file change unless it's an entry point
# A solution to this is one by one import of all SCSS files in the correct order which is challenging to acomplish
DELETE_OUTPUT_DIRECTORY = True

# Jinja2content plugin
JINJA2CONTENT_TEMPLATES = ['content']
LOAD_CONTENT_CACHE = False
