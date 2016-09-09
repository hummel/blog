#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Jacob Hummel'
SITEURL = 'http://localhost:8000'
SITENAME = 'Jacob Hummel'
SITETITLE = AUTHOR
SITESUBTITLE = 'Adventures in python and computational astrophysics.'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
SITELOGO = '//s.gravatar.com/avatar/f8072ec09a7106db46a1d078b3660448?s=120'
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

THEME = './flex'
PATH = 'content'
TIMEZONE = 'US/Mountain'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True

LINKS = (('Website', 'http://www.as.utexas.edu/~jhummel'),)

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/astrohummel'),
          ('github', 'https://github.com/hummel'),
          ('twitter', 'https://twitter.com/astrohummel'))
#          ('google', 'https://google.com/+NAME'),
#          ('rss', '//blog.jacobhummel.me/feeds/all.atom.xml'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2016

DEFAULT_PAGINATION = 10

MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap', 'post_stats', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.literal',
           'ipynb.markup', 'ipynb.liquid']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

DISQUS_SITENAME = "hummel"
GOOGLE_ANALYTICS = 'UA-34061646-1'
#ADD_THIS_ID = ''
#STATUSCAKE = {}

STATIC_PATHS = ['images', 'downloads']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}

CUSTOM_CSS = 'static/custom.css'

USE_LESS = True
