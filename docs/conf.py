# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


import os
import sys

sys.path.insert(0, os.path.abspath('..'))
from vsensebox.utils.about import getVersionString

project = 'VSenseBox'
copyright = '2024, UMONS-Numediart, Ratha SIV'
author = 'Ratha SIV'
version = getVersionString()
release = version

show_authors = True

extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx_search.extension',
    'myst_parser',
]

autodoc_preserve_defaults = True
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md', '.gitignore']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}

pygments_style = 'sphinx'
source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser'}
master_doc = 'index'

man_pages = [
    (master_doc, 'vsensebox', u'VSenseBox Documentation', [author], 1)
]

# pip install sphinx myst-parser pydata-sphinx-theme readthedocs-sphinx-search

htmlhelp_basename = 'VSenseBox Documentation'
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "logo": {
        "text": "👁️📦 VSenseBox",
    },
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/numediart/vsensebox",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
    ],
    "secondary_sidebar_items": ["page-toc", "edit-this-page"],
    "show_toc_level": 3,
    "navigation_with_keys": 'False',
}

# remove some primary sidebar
html_sidebars = {
    'getstarted': [], 
    'vsensebox/vsense': [],  
    'vsensebox/config': [], 
    'vsensebox/utils': [], 
    'releasenotes': []
}

html_static_path = ['_static']
html_show_sphinx = False
# html_show_sourcelink = False
