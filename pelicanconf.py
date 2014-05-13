#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os

AUTHOR = u'Jacob Hummel'

SITENAME = u'Jacob Hummel'
SITESUBTITLE = u'Adventures in python and computational astrophysics.'
SITEURL = '' # change in publishconf.py

# Times and dates
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'US/Central'
DEFAULT_LANG = u'en'

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Title menu options
MENUITEMS = [('Archives', '/archives.html'),
             ('Home Page', 'http://www.as.utexas.edu/~jhummel')]
NEWEST_FIRST_ARCHIVES = False

#Github include settings
#GITHUB_USER = 'hummel'
#GITHUB_REPO_COUNT = 0
#GITHUB_SKIP_FORK = True
#GITHUB_SHOW_USER_LINK = True

# Blogroll
#LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#          ('Python.org', 'http://python.org'),
#          ('Jinja2', 'http://jinja.pocoo.org'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# STATIC_OUT_DIR requires https://github.com/jakevdp/pelican/tree/specify-static
#STATIC_OUT_DIR = ''
#STATIC_PATHS = ['images', 'figures', 'downloads']
#FILES_TO_COPY = [('favicon.png', 'favicon.png')]

# This requires Pelican 3.3+
STATIC_PATHS = ['images', 'figures', 'downloads', 'favicon.png']

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# Theme and plugins
THEME = 'pelican-octopress-theme/'
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']

DISPLAY_PAGES_ON_MENU = False


# The theme file should be updated so that the base header contains the line:
#
#  {% if EXTRA_HEADER %}
#    {{ EXTRA_HEADER }}
#  {% endif %}
# 
# This header file is automatically generated by the notebook plugin
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found.  "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

# Sharing
TWITTER_USER = 'astrotoaster'
#GOOGLE_PLUS_USER = 'jakevdp'
#GOOGLE_PLUS_ONE = True
#GOOGLE_PLUS_HIDDEN = False
FACEBOOK_LIKE = True
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'


# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'


# Search
SEARCH_BOX = True