# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import django

# Add the parent directory to the module search path
sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'MySite.settings'
django.setup()

# Project information
project = 'MySite'
author = 'Calvin Hatttingh'
release = '0.1'

# General configuration
extensions = [
    'sphinx.ext.autodoc',            # Automatic documentation generation from docstrings
    'sphinx.ext.napoleon',           # Support for Google and NumPy style docstrings
    'sphinx.ext.viewcode',           # Add links to the source code
    'sphinx.ext.autosummary',        # Generate summary tables
    'sphinx_autodoc_typehints',      # Add type hints to autodoc
]

# Paths for templates and static files
templates_path = ['_templates']
html_static_path = ['_static']

# Options for HTML output
html_theme = 'alabaster'
html_theme_options = {
    'sidebar_collapse': True,
    'page_width': 'auto',
}
