MSR 2012 @ ICSE 
=======================================================================

:slug: msr2012
:lang: en
:date: 2012-06-02 10:42
:tags: msr, icse, mining, software, repository

Mining Software Repository 2012 @ ICSE
+++++++++++++++++++++++++++++++++++++++

I participated MSR of this year. We came to University of Zurich early
in the morning. The registration got something wrong when it seems that 
Swisser cannot tell the difference among Asians so that name cards of
3 Chinese with family name of Yang are misplaced. And also the 
organization field of Hotta was ``Japan, Japan``, as if he represented
the Japan.

MSR(MicroSoft Research) talk @ MSR(Mining Software Repositories)
-----------------------------------------------------------------------

The first talk was the keynote given by Mrs Zhang from MSR(MicroSoft 
Research @ Asia), so it turned out to be MSR gave keynote of MSR.
The talk was about Software Analysis and their clone detection tool 
called XIAO. XIAO was a clone detector developed by MSRA which can be
used as a plugin for Microsoft Visual Studio. XIAO has two part, or 
system state: the statical state analysis all the clones which didn't
consider the runing time, while the dynamic state need real time response.
The thing I need to develop for Samsung is something like dynamic mode.
I wanted to know more about the internal details about Xiao but the talk
was finished there. 

Towards Improving BTS with Game Mechanisms 
-----------------------------------------------------------------------

The contents of this talk is very much like this blog:

http://www.joelonsoftware.com/items/2008/09/15.html

The talk discussed whether the same game mechanism can be applied to
the things like issue tracking or similiar. From my point of view, it
is useless to use game machanism in this situation. The reason that
stackoverflow can success lies on that they just captured the  use of 
fade system in opensource community, as all hackers like to be approved
as great hacker, as what is happening in wikipedia. Whether the same 
theroy can be applied in issue tracking systems inside a internal 
company is questionable. Although MSDN has basic the same structure 
as wikipedia, the content of MSDN and wikipedia have different 
involvement of users. So I myself didn't approve this research.

GHTorrent
-----------------------------------------------------------------------

They slide of this talk can be found from here:
http://www.slideshare.net/gousiosg/ghtorrent-githubs-data-from-a-firehose-13184524

Data exporter for github. Main part of data of Github, namely the hosted 
code, are already exposed as git repos, and wiki of repos are stored in
git repo. So the aim of this project is to expose other data such as 
issues, code comments, etc. The project access github api and fetch the 
needed data as distributed system in order to overcome the limitations 
of the github api. The project will provide download history as torrents.
The json data from github api is stored as bson in MongoDB and the parsed
data is stored in MySQL with schema.

From my point of view, it will be better if the format of data can be 
uniformed and all data are stored in the git repo as wiki pages. 
As the history stored in git repo is more nature, and using ``git blame``
to trace author of code comments should also be more useful. Of course
it is harder to read and write the raw data of git as we need more 
understanding of the internal format of git. Maybe only people from 
github can do this.

Topic Mining
-----------------------------------------------------------------------

I can not understand the two parameters, DE, AIC, used in this research,
study this later. The experiment target of this research are Firefox,
Mylyn and Eclipse. They are trying to analysis the identifiers and 
comments from source codes in software repos and find the relationship
between topics and bugs, like what kind of topics are more likely to 
contain buggy codes.

The result of this research is not so clear. Such as it said that the 
core functions of Firefox have more bug reports, but it said no reason
about this. Maybe this only means that the core features are well 
tested, rather than that the core features are more buggy.

But the slides showed by auther are pretty and easy to understand.

The evolution of software
-----------------------------------------------------------------------

The keynote talk of the second day. It is about how should we combine
the social media with software development. Maybe this is the reason
why Github successed. In the talk she told about accessing tags, 
uBlogs, blogs etc. directly from Intergrated Development Environments,
or should we need cloud IDE such as Cloud9.

Do Faster Releases Imporve Software Quality?
-----------------------------------------------------------------------

Used firefox as example.

The conclusion is that faster releases will lead to more bugs and more
frequent crash, but bugs are get fixed more quickly and user will switch
to new released more quickly.

Security vs Performance Bugs in Firefox
-----------------------------------------------------------------------

Performance bugs are regression, blocks release.

-----------------------------------------------------------------------

Some of my thoughts
-----------------------------------------------------------------------

Seperation of commits based on Semantic analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The user of some tools (such as git) are not following the design 
purposes of these tools which brings some difficulty to MSR. For example
git has a prefect branch system, so it is desired for users of git to 
commit per topic. Commit per topic means that user send a commit for a 
single implementation of a feature or a bug fix, etc. If it is difficult
to contain all modifications in a commit, then it should be in a 
seperate branch and merged into master branch. But acturely
user tends to send very large commits, that contains many logical 
features, and they can not predict to open a new branch until a few
commits.

Maybe this is not the fault of the user of tools, this is the tools 
that are not smart enough. We should seperate the commits according
to the semantica topics inside a commit. 

About the slide systems used today
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The study with title ``Incorporating Version Histories in Information 
Retrieval Based Bug Localization`` used the slides made by beamer. It 
contains many equations, used many overlays are iterations, with few
figures, is a typical beamer slide. It also used mindmap very well.

There are at least 3 slides that are made by beamer today.

The study with title ``Towards Improving Bug Tracking Systems with 
Game Mechanisms`` presented with prezi. It have many pictures and many
transitions. But because of it is made by prezi, there are no headers
and footers so no page numbers and section titles etc. This is not
so convinient in such a official occations because people need to 
refer to the page number in question session.

There are at lease 6 presents used Apple Keynote. It is really 
difficult to tell the differece between slides made by powerpoints
and Keynote. 2 of them used the default theme of keynote.

The rest are using powerpoint. Mrs Zhang from Microsoft used powerpoint
but her slides looks like beamer very much such as the usage of footer 
and header and overlays. If these are made by powerpoint that will 
involve many manually operations.

值得一提的是有一個題目爲``Green Mining: A Methodology of Relating 
Software Change to Power Consumption''的人的slide全是``劣質''的手繪漫畫，
效果意外地好，很低碳很環保很綠色很可愛。具體效果可以參考下面的動畫，雖然
現場看到的不是一個版本：

http://softwareprocess.es/a/greenmining-presentatation-at-queens-20120522.ogv

微軟是個腹黑娘！
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

嘛雖然這也不是什麼新聞了。MSR2012的Mining Challenge的贊助商是微軟，管理
組織者來自微軟研究院，獎品是Xbox和Kinect。然後今年的題目是：

::

        Mining Android Bug

我看到了微軟滿滿的怨氣……

