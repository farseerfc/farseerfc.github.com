# -*- coding: utf-8 -*-
import sys

TIMEZONE = 'Asia/Tokyo'

DATE_FORMATS = {
    'en':('usa',u'%a, %d %b %Y'),
    'zh':('chs',u'%Y-%m-%d'),
    'jp':('jpn',u'%Y/%m/%d(%a)'),
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
GOOGLE_ANALYTICS = 'UA-29540705-1'
TAG_FEED  = 'feeds/%s.atom.xml'

SOCIAL = (('twitter', 'http://twitter.com/farseerfc'),
          ('github', 'https://github.com/farseerfc'),
          ('facebook', 'http://www.facebook.com/farseerfc'),
          ('weibo', 'http://weibo.com/farseerfc'),
          ('renren', 'http://www.renren.com/farseer'),
          )
          

TWITTER_USERNAME = 'farseerfc'
SIDEBAR_CUSTOM = r"""
<li class="nav-header"><h4><i class="icon-list-alt"></i>Weibo</h4></li>
<iframe width="100%" height="550" class="share_self"  frameborder="0" scrolling="no" 
src="http://widget.weibo.com/weiboshow/index.php?language=&width=0&height=550&fansRow=1&ptype=1&speed=0&skin=2&isTitle=1&noborder=1&isWeibo=1&isFans=1&uid=1862842353&verifier=b193b9de&dpc=1">
</iframe>
<li class="nav-header"><h4><i class="icon-search"></i>Google Search</h4></li>
<div id="cse" style="width: 100%;">Loading</div>
<script src="http://www.google.com/jsapi" type="text/javascript"></script>
<script type="text/javascript"> 
  google.load('search', '1', {language : 'zh-CN'});
  google.setOnLoadCallback(function() {
    var customSearchOptions = {};  var customSearchControl = new google.search.CustomSearchControl(
      '001578481551708017171:axpo6yvtdyg', customSearchOptions);
    customSearchControl.setResultSetSize(google.search.Search.SMALL_RESULTSET);
    customSearchControl.draw('cse');
  }, true);
</script>
<link rel="stylesheet" href="http://www.google.com/cse/style/look/default.css" type="text/css" />
"""

THEME='bootstrap2'
#THEME='notmyidea'
#CSS_FILE = "wide.css"

DEFAULT_CATEGORY ='Others'
OUTPUT_PATH = '.'
PATH = 'posts'

#PDF_GENERATOR = True

