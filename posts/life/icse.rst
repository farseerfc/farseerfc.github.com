ICSE 2012
=======================================================================

:slug: icse2012
:lang: zh
:date: 2012-06-06 10:42
:tags: icse, software

Keynote 1
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
沒怎麼聽懂，只記得講到了finance is not money但是沒聽懂這個和軟件有什麼
關係。

Cost Estimation for Distributed Software Project
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
講到他們試圖改善現有的模型去更精確地評估軟件開發的開銷。

他們會給PM建議之前的項目的歷史數據，然後對於新項目，他們建議歷史上已有
的項目的數據，從而幫助PM得到更精確的評估。他們試圖儘量減少項目評估對PM
的經驗的需求，從而幫助即使經驗很少的PM也能準確評估項目的開銷。

他們的觀點：

        Context-specfic solutions needed!

        Early user paticipation is key!

Characterizing Logging Practices in Open-Source Software
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Common mistakes in logging messages

他們學習了歷史上的log記錄，然後試圖找到重複修改的輸出log的語句，確定log
中存在的問題。他們首先確定修改是事後修改。

通常的修改的比例（9027個修改）

=== ===========
45% text
27% variable
26% verbosity
2%  location
=== ===========

他們發現有verbo等級的變化，是因爲安全漏洞之類的原因，或者在開銷和數據
之間的權衡。

大多數對log的var的修改都是爲了增加一個參數。他們之前的LogEnhancer是爲了
解決這個問題而提出的，通過靜態檢查，提醒程序員是否忘記了某個參數

對text的修改是因爲要改掉過時的代碼信息，避免誤導用戶。

他們的實驗是採用了基於code clone 的技術，找到所有log語句，然後找不一致
的clone，然後自動提出建議。

Combine Functional and Imperative Pgrm for Multicore Sw: Scala & Java
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

趨勢：到處都是多核，但是併發程序呢？

他們研究的對象是Scala和Java，因爲可以編譯後確認JVM字節碼的語義。

- Java:
      -  Shared Memory
      -  Explicit thread
      -  Synchronized
      -  Wait/Notified

- Scala:
      -  High-order fucntions
      -  Actors, message passing
      -  lists, filters, iterators
      -  while
      -  shared state, OO
      -  import java.*
      -  auto type infer

Training 4 weeks, Industry Project, 

結果：

scala 的項目平均比java多花38%的時間，主要都是花在Test和debug上的時間。

程序員的經驗和總體時間相關，但是對test和debug沒有顯著影響。

scala的爲了讓編程更有效率的設計，導致debug更困難。比如類型推導，debug
的時候需要手動推導，來理解正在發生什麼。

scala的程序比java小，中位數2.6%，平均15.2%

- 性能比較： 
        - 單核：scala的線性程序的性能比java好
        - 4核： 
                - scala 7s @ 4 threads 
                - java 4si @ 8 threads 
                - median 
                        - 83s scala 
                        - 98s java
        - 32core: best scala 34s @ 64 threads 

- 結論
        - java有更好的scalability

- scala類型推導
        - 45%說對攜帶碼有幫助
        - 85%說導致程序錯誤

- 調試
        - 23%認爲scala簡單
        - 77%認爲java簡單

multi-paradigram are better

Sound Empirical Evidence in Software Testing
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Test data generation

Large Empirical Studies - not always possible

For open source software - big enough


