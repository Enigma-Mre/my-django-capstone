# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import django

# Add your Django project to the Python path
sys.path.insert(0, os.path.abspath('../your_django_project'))  # Adjust path as necessary
os.environ['DJANGO_SETTINGS_MODULE'] = 'your_django_project.settings'  # Update with your settings module
django.setup()

# Project information
project = 'Your Django Project Name'
author = 'Your Name'
release = '0.1'  # Version of your project

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
html_theme = 'alabaster'  # Change the theme as desired
html_theme_options = {
    'sidebar_collapse': True,
    'page_width': 'auto',
}
