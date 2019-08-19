#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'firemark'
SITENAME = 'Hackerspace Silesia'
SITEURL = ''

PATH = 'content'
THEME = 'Flex'

TIMEZONE = 'Europe/Warsaw'
PAGE_ORDER_BY = 'date'

DEFAULT_LANG = 'pl'

SITELOGO = '/images/logo.png'
FAVICON = '/images/favicon.ico'

COPYRIGHT_NAME = '''
<a href="https://hs-silesia.pl">hs-silesia</a> team 2019.
Hosted on <a href="http://www.vultr.com/?ref=6819909">vultr</a>
'''

HOME_HIDE_TAGS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGINS = ['jinja2content']
JINJA2CONTENT_TEMPLATES = ['../templates']
STATIC_PATHS = ['extra', 'images']

LINKS = (
    ('HS wiki', 'https://wiki.hs-silesia.pl/'),
    ('Planowane spotkania', 'https://wiki.hs-silesia.pl/wiki/Planowane_spotkania'),
    ('Finanse', 'http://finanse.hs-silesia.pl/'),
    ('E-mail do zarządu', 'mailto:info@hs-silesia.pl'),
    ('Grupa dyskusyjna', 'https://lists.hs-silesia.pl/archives/open/'),
)

SOCIAL = (
    ('facebook', 'https://www.facebook.com/HackerspaceSilesia'),
    ('twitter', 'https://twitter.com/hs_silesia'),
    ('github', 'https://github.com/hackerspace-silesia'),
    ('envelope', 'mailto:info@hs-silesia.pl'),
)

DEFAULT_PAGINATION = False

MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.toc': {
    },
    'markdown.extensions.codehilite': {'css_class': 'highlight'},
    'markdown.extensions.extra': {},
    'markdown.extensions.meta': {},
  },
  'output_format': 'html5',
}
CUSTOM_CSS = 'extra/custom.css'
