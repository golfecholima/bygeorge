#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'George'
SITENAME = u'by George'
SITEURL = 'http://bygeorge.xyz'
TIMEZONE = 'America/New_York'

# Publishing
PATH = 'content'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%A, %B %d, %Y'
SLUGIFY_SOURCE = 'title'
SUMMARY_MAX_LENGTH = 250
LOAD_CONTENT_CACHE = False # Content Cache (Off for dev/On for live)
DEFAULT_PAGINATION = 1

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

# Language
DEFAULT_LANG = u'en'

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['textile_reader']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "themes/bygeorge"
CSS_FILE = "style.css"

TWITTER_USERNAME = "rhymeswthgeorge"