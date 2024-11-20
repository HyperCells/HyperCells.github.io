# ===============================================================================================
# HyperCells-Website configuration file :
# ===============================================================================================
# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# ===============================================================================================
# Import needed packages :
# ===============================================================================================

import sys, os
import datetime
sys.path.append(os.path.abspath("sphinxext"))

# ===============================================================================================
# Execute preliminary functions; inter-link:
# ===============================================================================================
# If you want to disable the execution of this code section, please make sure to delete the code:
# .. include:: interlinkTutorials.rst
#   :start-line: 2
# which is part of the contents/Tutorials/tutorials.rst file.

sys.path.append(os.path.abspath('execCode'))
import ExeInterlink

# ===============================================================================================
# Project information :
# ===============================================================================================
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# Get current year.
date = datetime.datetime.now().date()
year = date.strftime("%Y")

project = "HyperCells and HyperBloch documentation"
copyright = f"2023-{year}, Patrick M. Lenggenhager, Joseph Maciejko and Tomáš Bzdušek. Website development and tutorials by Marcelo Looser" 
author = "by the HyperCells development team"
release = "0.1.0"
version = "0.1.0"

# ===============================================================================================
# General configuration :
# ===============================================================================================
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",  
    "sphinx_design", 
    "sphinx_copybutton",
    "notfound.extension", 
    "sphinx_reredirects", 
    "sphinx_togglebutton",
    "sphinx.ext.mathjax"
]

myst_enable_extensions = ["colon_fence"]

# imgmath extension configuration.
imgmath_image_format = "svg"
imgmath_dvipng_args = ["-gamma", "1.5", "-D", "110", "-bg", "Transparent"]

# The file extensions of source files. 
source_suffix = [".rst", ".md"]

templates_path = ["_templates"]
exclude_patterns = []

# The encoding of all reST source files.
source_encoding = "utf-8-sig"

# master_doc: The document name of the “root” document, that is, 
# the document that contains the root toctree directive. 
master_doc = "index"

# If true, figures, tables and code-blocks are automatically numbered if they have a caption.
numfig = False

# ===============================================================================================
# 404 not found page configuration :
# ===============================================================================================

#notfound_pagename = "404"
#notfound_urls_prefix = "/HyperCells.github.io/"

# ===============================================================================================
# Options for HTML output :
# ===============================================================================================
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Path to static objects.
html_static_path = ["_static"]
html_extra_path = ["assets"]

# Title to concatenated with tab title in browser.
html_title = "HyperCells & HyperBloch"

# Theme template and custom css file path.
html_theme = "pydata_sphinx_theme"
html_css_files = ["css/custom.css"]

# Logo on browser tab.
html_favicon = "_static/images/lightMode/favicon.ico"

# Logo on webpage title.
html_logo = "_static/images/lightMode/html_logo_HyperSupercells2_light.png"

# html light/dark mode setting.
# Note, I will set this to automatic eventually.
html_context = {"default_mode": "light"}

# Drop primary sidebar (left, called Section Navigation) of pages.
# Note, in order to drop the secondary sidebar (right), one needs to
# adjust the .md and .rst files it self.
html_sidebars = {
  "contents/Installation/installation": [],
  "contents/GettingStarted/Getting_started": [],
  "contents/About/about": [],
  "contents/Gallery/gallery": [],
  "contents/Gallery/SubgroupTreegraph64": [],
  "contents/Gallery/PrimitiveCell64GAP": [],
  "contents/Publications/publications": [],
  "contents/Contribute/contribute": [],
  "contents/Contact/contact": [],
  "contents/Cite/cite": [],
  "contents/Documentation/documentation": [],
  "contents/LicenseCopyright/licenseCopyright": []
}

# Adjust the theme.
html_theme_options = {

    "body_max_width": "none",

    "secondary_sidebar_items": {
        "**": ["page-toc"]
    },

   "logo": {
      "image_light": "_static/images/lightMode/html_logo_HyperSupercells2_light.png",
      "image_dark": "_static/images/darkMode/html_logo_HyperSupercells2_dark.png"
   },
   
    # Number of header links displayed
    "header_links_before_dropdown": 5,

    # Number of links in header link dropdown
    "navigation_depth": 10,

    # Link icons that appear on the right upper corner of front page (desktop view),
    # or burger menu in reduced and mobile view.
    "icon_links": [
        {
            # Label for this link
            "name": "Github",
            # URL where the link will redirect
            "url": "https://github.com/HyperCells",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-square-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
    ],

    # Footer options.
    "article_footer_items": []
}

# ===============================================================================================