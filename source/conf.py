import datetime
#import ast

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Дипломная работа'
author = 'Сергей Зацаринный'
copyright = "%s CC-BY-SA, %s" % (datetime.date.today().year, author)

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

ogp_site_url = "https://canonical-starter-pack.readthedocs-hosted.com/"
ogp_site_name = project
ogp_image = "https://assets.ubuntu.com/v1/253da317-image-document-ubuntudocs.svg"

html_context = {
    "github_folder": "/DemoVisual/",
    "display_contributors": False,
    "sequential_nav": "both",
}

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
templates_path = ['source/_templates']
# Adds custom JavaScript files, located under 'html_static_path'
# html_js_files = []
# Adds custom CSS files, located under 'html_static_path'
#html_css_files = [
#    "css/pdf.css",
#]

extensions = [
    "canonical_sphinx",
    "sphinxcontrib.cairosvgconverter",
    "sphinx_last_updated_by_git",
]

exclude_patterns = [
    "doc-cheat-sheet*",
]


redirects = {}

disable_feedback_button = True
