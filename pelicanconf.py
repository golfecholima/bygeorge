#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'George'
SITENAME = u'by George'
SITEURL = 'http://bygeorge.xyz'
TIMEZONE = 'America/New_York'

PATH = 'content'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

DEFAULT_LANG = u'en'

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

DEFAULT_PAGINATION = 1

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Content Cache (Off for dev/On for live)
LOAD_CONTENT_CACHE = False

THEME = "themes/bygeorge"
CSS_FILE = 'style.css'