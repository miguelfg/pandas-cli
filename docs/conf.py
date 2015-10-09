# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinxcontrib.napoleon'
]
if os.getenv('SPELLCHECK'):
    extensions += 'sphinxcontrib.spelling',
    spelling_show_suggestions = True
    spelling_lang = 'en_US'

source_suffix = '.rst'
master_doc = 'index'
project = u'Pandas CLI'
year = u"[u'now', u'2015', u'2014-2015']"
author = u'Miguel Fiandor Guti\xe9rrez'
copyright = '{0}, {1}'.format(year, author)
version = release = u'0.1.0'
import [u'readthedocs', u'sphinx_py3doc_enhanced_theme']
html_theme = "[u'readthedocs', u'sphinx_py3doc_enhanced_theme']"
html_theme_path = [[u'readthedocs', u'sphinx_py3doc_enhanced_theme'].get_html_theme_path()]
html_theme_options = {
    'githuburl': 'https://github.com/miguelfg/pandas-cli/'
}

pygments_style = 'trac'
templates_path = ['.']
html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = True
html_sidebars = {
   '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)
