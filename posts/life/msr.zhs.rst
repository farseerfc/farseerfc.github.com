MSR 2012 @ ICSE 
=======================================================================

:slug: msr2012
:lang: zhs
:date: 2012-06-02 10:42
:tags: msr, icse, mining, software, repository

Mining Software Repository 2012 @ ICSE
+++++++++++++++++++++++++++++++++++++++

参加了今年的MSR，会场在University of Zurich。一大早来到大学，注册有点
小插曲，显然瑞士人搞不清楚中国人的名字，3个杨（Yang）姓的中国人的名牌
被搞错了。

MSR(MicroSoft Research) talk @ MSR(Mining Software Repositories)
-----------------------------------------------------------------------

首先是来自微软亚洲研究院（MicroSoft Research @ Asia, MSR Asia）的演讲，
于是就变成了MSR在MSR的演讲。MSR的张冬梅（Dongmei Zhang）女士的演讲
分为关于Software Analysis和XIAO的两部分。XIAO是MSRA开发的Code Clone 
Detector，似乎我要给井上研做的就是这个。演讲结束的时候的鼓掌导致了话筒
的小鼓掌。


Towards Improving BTS with Game Mechanisms Tracking
-----------------------------------------------------------------------

Improve bug report

GHTorrent
-----------------------------------------------------------------------

Data exporter for github

Topic Mining
-----------------------------------------------------------------------

with DE and AIC

SeCold
-----------------------------------------------------------------------

A linked data platform for mining software repositories


一些感想
-----------------------------------------------------------------------

基于自然语义分析的commit分割
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

经常工具（比如git）的使用者并没有按照工具设计者的意图使用工具，这给MSR
带来很多困难。举个例子，git有非常完美的branch系统，通常期望git的使用者
能够在一次commit里commit一个功能，比如一个bug的修复，或者一个feature的
添加，但是事实上经常有很多逻辑上的commit被合并在一个里面了。

或许这不是使用者的错，而是工具仍然不够人性的表现。或许我们可以自动把
一次的commit按照语义分割成多个。

分割之后，可以更容易地把issue和commit关联，也更容易组织更多的研究。

关于这次发表中大家用的slides系统
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

题目为``Incorporating Version Histories in Information Retrieval Based 
Bug Localization''的人用的slide是beamer的。公式很多，overlay很多，列表
很多，图片很少，典型的beamer做出的slide。思维导图用得很不错。

题目为``Towards Improving Bug Tracking Systems with Game Mechanisms''
的人用了prezi，图片很多，过度很多。但是比如没有页号没有页眉页脚，正式
会议的场合不太方便。

至少有两个以上用了Apple Keynotes，Keynotes做出来的东西真的和Powerpoint
做出来的很难区别，这两个人用了初始的主题所以才看出来。还有至少两个人
的slide的动画效果是PPT绝对做不出来的，估计是Keynotes。

剩下的自然是PPT。MSRA的刘女士做的虽然是PPT，倒是有很多beamer的感觉，
比如页眉页脚和overlay的用法。这些如果都是PPT做出来的，会多很多额外的
人力吧。

