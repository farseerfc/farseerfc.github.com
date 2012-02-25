
# -*- coding: utf-8 -*-

DATE_FORMATS = {
    'en':'%a, %d %b %Y',
    'zh':'%Y %b %d, %a',
    'jp':'%Y %b %d(%a)',
}

## locale setting is only valid on windows, see 
## http://msdn.microsoft.com/en-us/library/cdax410z%28VS.71%29.aspx
LOCALE = ['usa', 'chn', 'jpn'] 
## On Unix/Linux, use:
# LOCALE = ['en_US', 'zh_CN', 'ja_JP'] 

TAG_FEED  = 'feeds/%s.atom.xml'

SITENAME = 'Farseerfc Blog'
AUTHOR = 'Jiachen Yang'

DISQUS_SITENAME = 'farseerfcgithub'
GITHUB_URL = 'https://github.com/farseerfc'
SITEURL = 'http://farseerfc.github.com'

SOCIAL = (('twitter', 'http://twitter.com/farseerfc'),
          ('github', 'https://github.com/farseerfc'),
          ('facebook', 'http://www.facebook.com/farseerfc'),
          ('weibo', 'http://weibo.com/farseerfc'),
          )
TWITTER_USERNAME = 'farseerfc'


THEME='notmyidea'



DEFAULT_CATEGORY ='Others'
OUTPUT_PATH = '.'
PATH = 'pages'
TIMEZONE = 'Asia/Tokyo'

