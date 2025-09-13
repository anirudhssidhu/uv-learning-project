"""Sphinx configuration."""

project = "UV demo"
author = "anirudh"
copyright = "2025, anirudh"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "shibuya"
