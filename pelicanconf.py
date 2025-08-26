SITENAME = 'Python Chile ¡El Blog!'
SITEURL = ""
PYTHON_CHILE_URL = "https://pythonchile.cl/"
PATH = "content"

TIMEZONE = 'America/Santiago'

DEFAULT_LANG = 'es'

THEME = "theme"


FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Variables para rutas
JINJA_GLOBALS = {
    'img_path': '{static}/img'
}

STATIC_PATHS = ['img', 'css']

ARTICLE_PATHS = ['post']

# Configuración para paginación
DEFAULT_PAGINATION = 9
INDEX_SAVE_AS = 'index.html'
PAGINATED_DIRECT_TEMPLATES = ['index']

# Configuración para resaltado de bloque de código
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.fenced_code": {},
        "markdown.extensions.codehilite": {
            "css_class": "highlight",
            "linenums": True,
            "guess_lang": False,
        },
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}

TEMPLATE_PAGES = {
    "search.json": "search.json",
}