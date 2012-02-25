Try Pelican
===========

:slug: try-pelican
:lang: en
:date: 2012-02-24

This is my first blog with Pelican!

My settings.py
++++++++++++++

.. code-block:: python
    
    TIMEZONE = 'Asia/Tokyo'
    DATE_FORMATS = {
        'en':'%a, %d %b %Y',
        'zh':'%Y年%m月%d日, 周%a',
        'jp':'%Y年%ｍ月%d日(%a)',
    }
    # windows locale: http://msdn.microsoft.com/en-us/library/cdax410z%28VS.71%29.aspx
    LOCALE = ['chn', 'jpn','usa',       # windows
            'en_US', 'zh_CN', 'ja_JP']  # Unix/Linux
    DEFAULT_LANG = 'zh'
    
    SITENAME = 'Farseerfc Blog'
    AUTHOR = 'Jiachen Yang (farseerfc@gmail.com)'
    
    DISQUS_SITENAME = 'farseerfcgithub'
    GITHUB_URL = 'https://github.com/farseerfc'
    SITEURL = 'http://farseerfc.github.com'
    TAG_FEED  = 'feeds/%s.atom.xml'
    
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

