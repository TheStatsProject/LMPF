# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'The Truth Project'
copyright = '2025, TheOs'
author = 'THEOS'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.images',
    'sphinxcontrib.mermaid',
    'sphinx_design',
    'sphinx_copybutton',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

#charge html

html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

#logo and favicon
# Logo and Favicon Configuration
# Path to the logo image
html_logo = "_static/logo.png"

# Path to static files (ensure the logo and favicon reside here)
html_static_path = ['_static']

# Path to the favicon image
html_favicon = "_static/favicon.ico"

# Note: To adjust the size of the logo, use the 'custom.css' file in the '_static' directory.
# Example CSS for logo size adjustment:
# img.logo {
#     width: 150px; /* Set desired width */
#     height: auto; /* Maintain aspect ratio */
# }

html_logo = "_static/logo.png"
html_static_path = ['_static']
html_favicon = "_static/favicon.ico"

#extensions


