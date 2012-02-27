# -*- coding: utf-8 -*-
import sys

TIMEZONE = 'Asia/Tokyo'

DATE_FORMATS = {
    'en':('usa',u'%a, %d %b %Y'),
    'zh':('chs',u'%x'),
    'jp':('jpn',u'%x'),
}
# windows locale: http://msdn.microsoft.com/en-us/library/cdax410z%28VS.71%29.aspx
LOCALE = ['usa', 'chs', 'jpn',        # windows
          'en_US', 'zh_CN', 'ja_JP']  # Unix/Linux
DEFAULT_LANG = 'zh'

SITENAME = 'Farseerfc Blog'
AUTHOR = 'Jiachen Yang'

DISQUS_SITENAME = 'farseerfcgithub'
GITHUB_URL = 'https://github.com/farseerfc'
SITEURL = 'http://farseerfc.github.com'
TAG_FEED  = 'feeds/%s.atom.xml'

SOCIAL = (('twitter', 'http://twitter.com/farseerfc'),
          ('github', 'https://github.com/farseerfc'),
          ('facebook', 'http://www.facebook.com/farseerfc'),
          ('weibo', 'http://weibo.com/farseerfc'),
          ('renren', 'http://www.renren.com/farseer'),
          )
          

TWITTER_USERNAME = 'farseerfc'

THEME='notmyidea'
CSS_FILE = "wide.css"

DEFAULT_CATEGORY ='Others'
OUTPUT_PATH = '.'
PATH = 'posts'



