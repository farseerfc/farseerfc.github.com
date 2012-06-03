MSR 2012 @ ICSE 
=======================================================================

:slug: msr2012
:lang: jp
:date: 2012-06-02 10:42
:tags: msr, icse, mining, software, repository

Mining Software Repository 2012 @ ICSE
+++++++++++++++++++++++++++++++++++++++

今年のMSRを参加しました、会場はチューリッヒ大学にあります。朝早く大学に
着いて、登録するときちょっと事情をありました。スイス人は明らかに中国人
の名前をわからないから、３つの中国からの楊（Yang）の名札を間違えた。そ
して堀田先輩の名札に"Japan, Japan"になって、日本代表になった。

MSR(MicroSoft Research) talk @ MSR(Mining Software Repositories)
-----------------------------------------------------------------------

まず一番目のKeynoteはマイクロソフトアジア研究院(MicroSoft Research @ Asia
,MSR Asia)のZhang氏が発表する、こうしてMSRがMSRに発表するになった。

Zhangの発表はSoftware AnalysisとXIAOの２つの紹介です。XIAOはマイクロソフト
が開発したCode Clone Detector、ある会社が私達に任せるのもこのようなシステム
です。もっと詳しく知りたいが、実装に関わるものは言ってなかった。

Towards Improving BTS with Game Mechanisms 
-----------------------------------------------------------------------

これの内容は基本的にこのブロクに書いています：

http://www.joelonsoftware.com/items/2008/09/15.html

同じ理論をIssue Trackingとかに応用できるかを言いました。個人的にこれは
意味ない気がします。stackoverflowの成功はOpen Software Communityにもと
もとある名誉システムを具現化したですから、それを会社の中に応用するのは
難しい気がする。

GHTorrent
-----------------------------------------------------------------------

Data exporter for github. Githubの主なデータはコード、それは既にgitから
アクセスできます、wikiはgitとして保存しているからそれも含まれている。
ですからこのプロジェクトの目的は他のデータを表せる、つまりissues, commit
commentsなど。このプロジェクトはgithub apiを通じて、分布システムとして
apiの制限を超える、そしてtorrentの形で歴史をdownloadできます。元のデータ
はbsonとしてMongoDBの保存して、Schemaを追加したデータはMySQLに保存する。

わたしの意見では、データをgitのrepoの形で保存するの方がいいかもしれない。
今のwikiのように、そしてgitoliteも全てのデータをgit自身の中に保存している。

The evolution of software
-----------------------------------------------------------------------

二日目のkeynotes, social mediaをソフトウェア開発に巻き込めるについて
話しました。

第二天的Keynotes，關於將Social Media和Software Development相結合的想法。
或許就是Github賴以成功的基礎。講到代碼中的comment, Tags, uBlog, blog之類
的social的特性和IDE的融合的趨勢。

Do Faster Releases Imporve Software Quality?
-----------------------------------------------------------------------

使用Firefox作爲例子。

結論是快速發佈導致bug更多，更容易crash，但是bug更快得到修復，並且用戶
更快轉向新的發佈。

Security vs Performance Bugs in Firefox
-----------------------------------------------------------------------

Performance bugs are regression, blocks release.

-----------------------------------------------------------------------

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
很多，圖片很少，典型的beamer做出的slide。思維導圖用得很不錯。今天一天
有至少3個slide是用beamer做的。

題目爲``Towards Improving Bug Tracking Systems with Game Mechanisms''
的人用了prezi，圖片很多，過度很多。但是比如沒有頁號沒有頁眉頁腳，正式
會議的場合不太方便。

至少有六個以上用了Apple Keynotes，Keynotes做出來的東西真的和Powerpoint
做出來的很難區別，其中兩個人用了初始的主題所以才看出來。

剩下的自然是PPT。MSRA的張女士做的雖然是PPT，倒是有很多beamer的感覺，
比如頁眉頁腳和overlay的用法。這些如果都是PPT做出來的，會多很多額外的
人力吧。

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

