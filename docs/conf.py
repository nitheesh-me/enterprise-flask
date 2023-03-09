"""Sphinx configuration."""
project = "Enterprise Flask"
author = "Nitheesh Chandra"
copyright = "2023, Nitheesh Chandra"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
