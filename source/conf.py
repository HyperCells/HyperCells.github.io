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
# Execute preliminary functions:
# ===============================================================================================
# If you want to disable the execution of this code section, please make sure to delete the code:
# .. include:: interlinkTutorials.rst
#   :start-line: 2
# which is part of the contents/Tutorials/tutorials.rst file.

# interlink featured functions and tutorials
sys.path.append(os.path.abspath('execCode'))
from interlink import ffspageDict, interlinkFile

cwd = os.getcwd() # current directory
dirTutorials = "/contents/Tutorials/" # relative path to the tutorials

# list of excluded files
exclude_files = [
    "tutorials.rst",
    "AdvancedVisualization.md",
    "interlinkTutorials.rst"
]

files = [f for f in os.listdir(cwd + dirTutorials) 
        if os.path.isfile(os.path.join(cwd + dirTutorials, f))
        and f not in exclude_files ]

[ffspDics, rstLinks] = ffspageDict(cwd + dirTutorials, files, rstLinks=True)
interlinkFile(cwd + dirTutorials, "interlinkTutorials", ffspDics, rstLinks=rstLinks)

# ===============================================================================================
# If you want to disable the execution of this code section, please make sure to delete the code:
# .. include:: interlinkGetSetGo.rst
#   :start-line: 2
# which is part of the contents/GettingStarted/getting_started.rst file.

# interlink featured functions and getSetGo files
dirGetSetGo = "/contents/GettingStarted/" # relative path to the getSetGo files

# list of excluded files
exclude_files = [
    "getting_started.rst",
    "interlinkGetSetGo.rst"
]

files = [f for f in os.listdir(cwd + dirGetSetGo) 
        if os.path.isfile(os.path.join(cwd + dirGetSetGo, f))
        and f not in exclude_files ]

[ffspDics, rstLinks] = ffspageDict(cwd + dirGetSetGo, files, rstLinks=True)
interlinkFile(cwd + dirGetSetGo, "interlinkGetSetGo", ffspDics, rstLinks=rstLinks)


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
release = "0.0.2"
version = "0.0.2"

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

notfound_pagename = "404"
notfound_urls_prefix = "/build/"

# ===============================================================================================
# Options for HTML output :
# ===============================================================================================
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Path to static objects.
html_static_path = ["_static"]
html_extra_path = ["assets"]

# Title to concatenated with tab title in browser.
html_title = "HyperCells & HyperBloch"

# Theme template and cotum css file path.
html_theme = "pydata_sphinx_theme"
html_css_files = ["css/custom.css"]

# Logo on browser tab.
html_favicon = "_static/images/lightMode/html___logo___tab.ico"

# Logo on webpage title.
html_logo = "_static/images/lightMode/html_logo_HyperSupercells2_light.png"

# html light/drak mode setting.
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
  "contents/Documentation/documentation": []
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
            "name": "HyperCells",
            # URL where the link will redirect
            "url": "https://github.com/patrick-lenggenhager/HyperCells",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-square-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
        {
            # Label for this link
            "name": "HyperBloch",
            # URL where the link will redirect
            "url": "https://github.com/patrick-lenggenhager/HyperBloch",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-square-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
    ],

    # Footer options.
    "article_footer_items": []
}


#   "external_links": [
#      {"name": "link-one-name", "url": "https://<link-one>"},
#      {"name": "link-two-name", "url": "https://<link-two>"} 
#   ]
#

# Prevent the copy button from appearing on top of notebook cell numbers:
#copybutton_selector = ":not(.prompt) > div.highlight pre"

# ===============================================================================================
# Latex and simplepdf configurations (to be dropped once the website is online)
# ===============================================================================================

latex_elements = {
   'papersize':'a4paper',
   'pointsize':'11pt',
   'classoptions': ',openany',
   'babel': '\\usepackage[english]{babel}',

}

simplepdf_vars = {
    'cover-bg': 'url(images/pdf_cover_temp.png) no-repeat center'
}

# ===============================================================================================