#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'tolerious'
SITENAME = u"tolerious's blog"
SITEURL = ''

PATH = 'content'
MAIL='tolerious@seedlinktech.com'
ABOUT_TEXT='Welcome abord.'
ABOUT_IMAGE='images/picture.jpg'
GOOGLEPLUS_USER='107031989496937042842'
TWITTER_USER='tolerious'
LINKEDIN_USER='tolerious'
FACEBOOK_USER='tolerious'
WEIBO_USER='51682963'
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

DATE_FORMATS = {
        'zh_CN': '%Y-%m-%d %H:%M',
}
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'
DEFAULT_DATE = 'fs' # use filesystem's mtime
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = "./html5-dopetrope"
# Blogroll
LINKS = (('Seedlink', 'http://seedlinktech.com/'),
         ('Rcxue', 'http://rcxue.com/'),
         #('Jinja2', 'http://jinja.pocoo.org/'),
        )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
STATIC_PATHS = ['images', 'pdfs']
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
