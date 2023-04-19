# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'OS2Valghalla'
copyright = 'Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).'
# URL for custom footer copyright and license
html_context = {
    'copyright_url': 'https://creativecommons.org/licenses/by-sa/4.0/'
}
author = 'OS2'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
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
