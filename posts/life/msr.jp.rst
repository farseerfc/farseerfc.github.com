MSR 2012 @ ICSE 
=======================================================================

:slug: msr2012
:lang: jp
:date: 2012-06-02 10:42
:tags: msr, icse, mining, software, repository

Mining Software Repository 2012 @ ICSE
+++++++++++++++++++++++++++++++++++++++

參加了今年的MSR，會場在University of Zurich。一大早來到大學，註冊有點
小插曲，顯然瑞士人搞不清楚中國人的名字，3個楊（Yang）姓的中國人的名牌
被搞錯了。

MSR(MicroSoft Research) talk @ MSR(Mining Software Repositories)
-----------------------------------------------------------------------

首先是來自微軟亞洲研究院（MicroSoft Research @ Asia, MSR Asia）的演講，
於是就變成了MSR在MSR的演講。MSR的張冬梅（Dongmei Zhang）女士的演講
分爲關於Software Analysis和XIAO的兩部分。XIAO是MSRA開發的Code Clone 
Detector，似乎我要給井上研做的就是這個。演講結束的時候的鼓掌導致了話筒
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

基於自然語義分析的commit分割
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

經常工具（比如git）的使用者並沒有按照工具設計者的意圖使用工具，這給MSR
帶來很多困難。舉個例子，git有非常完美的branch系統，通常期望git的使用者
能夠在一次commit裏commit一個功能，比如一個bug的修復，或者一個feature的
添加，但是事實上經常有很多邏輯上的commit被合併在一個裏面了。

或許這不是使用者的錯，而是工具仍然不夠人性的表現。或許我們可以自動把
一次的commit按照語義分割成多個。

分割之後，可以更容易地把issue和commit關聯，也更容易組織更多的研究。

關於這次發表中大家用的slides系統
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

題目爲``Incorporating Version Histories in Information Retrieval Based 
Bug Localization''的人用的slide是beamer的。公式很多，overlay很多，列表
很多，圖片很少，典型的beamer做出的slide。思維導圖用得很不錯。

題目爲``Towards Improving Bug Tracking Systems with Game Mechanisms''
的人用了prezi，圖片很多，過度很多。但是比如沒有頁號沒有頁眉頁腳，正式
會議的場合不太方便。

至少有兩個以上用了Apple Keynotes，Keynotes做出來的東西真的和Powerpoint
做出來的很難區別，這兩個人用了初始的主題所以才看出來。還有至少兩個人
的slide的動畫效果是PPT絕對做不出來的，估計是Keynotes。

剩下的自然是PPT。MSRA的劉女士做的雖然是PPT，倒是有很多beamer的感覺，
比如頁眉頁腳和overlay的用法。這些如果都是PPT做出來的，會多很多額外的
人力吧。

值得一提的是有一個題目爲``Green Mining: A Methodology of Relating 
Software Change to Power Consumption''的人的slide全是``劣質''的手繪漫畫，
效果意外地好，很低碳很環保很綠色很可愛。


