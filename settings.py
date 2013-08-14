# -*- coding: utf-8 -*-

TIMEZONE = 'Asia/Tokyo'

DATE_FORMATS = {
    'en': ((u'en_US', 'utf8'), u'%a, %d %b %Y',),
    'zh': ((u'zh_HK', 'utf8'), u'%Y年%m月%d日(週%a)',),
    'zhs': ((u'zh_CN', 'utf8'), u'%Y年%m月%d日(周%a)',),
    'jp': ((u'ja_JP', 'utf8'), u'%Y年%m月%d日(%a)',),
}
# windows locale: http://msdn.microsoft.com/en-us/library/cdax410z%28VS.71%29.aspx
#LOCALE = [#'usa', 'cht', 'chs', 'jpn',        # windows
#          u'en_US.utf8', u'zh_CN.utf8', u'ja_JP.utf8']  # Unix/Linux
DEFAULT_LANG = 'zh'

LOCALE = "C"

SITENAME = 'Farseerfc Blog'
AUTHOR = 'Jiachen Yang'

DISQUS_SITENAME = 'farseerfcgithub'
GITHUB_URL = 'https://github.com/farseerfc'
SITEURL = 'http://farseerfc.github.com'
GOOGLE_ANALYTICS = 'UA-29540705-1'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'

SOCIAL = (('twitter', 'http://twitter.com/farseerfc'),
          ('github', 'https://github.com/farseerfc'),
          ('facebook', 'http://www.facebook.com/farseerfc'),
          ('weibo', 'http://weibo.com/farseerfc'),
          ('renren', 'http://www.renren.com/farseer'),
          )

TWITTER_USERNAME = 'farseerfc'
SIDEBAR_CUSTOM = r"""
<li class="nav-header"><h4><i class="icon-list-alt"></i>Weibo</h4></li>
<iframe width="100%" height="550" class="share_self"  frameborder="0" scrolling="no" src="http://widget.weibo.com/weiboshow/index.php?language=zh_tw&width=0&height=550&fansRow=2&ptype=1&speed=0&skin=1&isTitle=1&noborder=0&isWeibo=1&isFans=1&uid=1862842353&verifier=b193b9de&colors=33b5e5,121417,999999,ade1f4,ffffff&dpc=1"></iframe>
"""

GOOGLE_CUSTOM_SEARCH_SIDEBAR = "001578481551708017171:axpo6yvtdyg"
GOOGLE_CUSTOM_SEARCH_NAVBAR = "001578481551708017171:hxkva69brmg"

THEME = './bootstrap2'
#THEME='notmyidea'
#CSS_FILE = "wide.css"

DEFAULT_CATEGORY = 'Others'
OUTPUT_PATH = '.'
PATH = 'posts'

#PDF_GENERATOR = True
