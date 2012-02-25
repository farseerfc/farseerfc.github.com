尝试一下Pelican
===================

:slug: try-pelican
:lang: zh

这是我用Pelican写的第一篇日志，尝试一下多语言功能。

我的设置 settings.py
++++++++++++++++++++++++

.. code-block:: python
    
    # -*- coding: utf-8 -*-
    ARTICLE_PERMALINK_STRUCTURE = '/%Y/%m/'
    DATE_FORMATS={'en':'%d/%m/%Y','zh':'%Y-%m-%d','jp':'%Y-%m-%d'}
    AUTHOR = 'Jiachen Yang'
    DISQUS_SITENAME = 'farseerfcgithub'
    GITHUB_URL = 'https://github.com/farseerfc'
    SITEURL = 'http://farseerfc.github.com'
    SITENAME = 'Farseerfc Blog'
    SOCIAL = (('twitter', 'http://twitter.com/farseerfc'),
              ('github', 'https://github.com/farseerfc'),
              ('facebook', 'http://www.facebook.com/farseerfc'),)
    TAG_FEED = 'feeds/%s.atom.xml'
    THEME='notmyidea'
    TWITTER_USERNAME = 'farseerfc'
    LOCALE = 'en'
    DEFAULT_CATEGORY ='Others'
    OUTPUT_PATH = '.'
    PATH = 'pages'
    TIMEZONE = 'Asia/Tokyo'

