#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'tolerious'
SITENAME = u"赫龙的小站"
SITEURL = ''
SITEUNAME = u"冷眼看八卦,娱乐猛回头"

PATH = 'content'
MAIL='tolerious#qq.com'
ABOUT_TEXT='This is tolerious.'
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
LINKS = (('美泊', 'http://meiparking.com'),
         ('机场代泊', 'http://service.meiparking.com/wechat/reserve/park/'),
         ('Coding个人主页', 'https://coding.net/?ref=tolerious'),
         #('Jinja2', 'http://jinja.pocoo.org/'),
        )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 6
STATIC_PATHS = ['images', 'pdfs']
LOCALE = ('en_US','ja_JP')
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
