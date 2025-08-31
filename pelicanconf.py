import os
import sys
sys.path.append(os.path.dirname(__file__))

from social_networks import SOCIAL_NETWORKS
from contributors import CONTRIBUTORS

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

# Variables custom para JINJA
JINJA_GLOBALS = {
    'img_path': '{static}/img',
    'social_networks': SOCIAL_NETWORKS,
    'contributors': CONTRIBUTORS,
}

# Todos las carpetas con archivos estáticos dentro de content/
STATIC_PATHS = [
    'img',
]

# Carpeta donde se alojan los archivos para crear post. Pelican por defecto tiene basepath content/
ARTICLE_PATHS = ['post']

# Configuración para paginación dentro de theme/
DEFAULT_PAGINATION = 9
INDEX_SAVE_AS = 'index.html'
PAGINATED_DIRECT_TEMPLATES = ['index']

# Configuración para resaltado de bloque de código dentro de archivos markdown
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
        'markdown.extensions.admonition': {}
    },
    "output_format": "html5",
}

# Archivos que debe considerar JINJA2/Pelican para crear sitio estático dentro de theme/templates
# Los cuales no son los por defectos
TEMPLATE_PAGES = {
    "search.json": "search.json",
    "contributors.html": "contributors.html",
    "contact.html": "contact.html",
}