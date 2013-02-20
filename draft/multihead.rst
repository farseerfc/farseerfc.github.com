GNU/Linux上多顯示器支持之現狀
=======================================

:slug: multihead
:lang: zh
:date: 2013-02-13 14:20:21
:tags: multihead, X11, wayland, linux

.. contents::

起　背景
++++++++++++++++++++++++++++++++++

研究室新進了27吋的顯示器，安置了1臺在我的辦公桌上。於是又從報廢的機器堆裏
翻出了1臺小顯示器和一塊Radeon顯卡，組成4顯示器的配置。沒想到添加硬件本身
很容易，讓它們在我的Archlinux上正常工作卻花了不少時間。來來回回折騰各種配置
文件甚至改寫源代碼(xorg, awesome, compton, ...），經過了1個多月之後，現在的
配置總算比較滿意，能夠讓我正常工作了。折騰的過程中嘗試了不少解決方案，覺得
這方面的文檔實在少得可憐，同時最近又看到一些關於Wayland 和 RandR 的新進展，
於是稍微整理一番。

GNU/Linux 在桌面領域的發展相比較於服務器端而言一直緩慢，市場份額遠不及
Windows 和 OSX ，其原因必將是多方面的，多顯示器支持(`Multihead
<http://en.wikipedia.org/wiki/Multi-monitor>`_)也即是其硬傷之一。

當然這個過錯不在 Linux 這邊， Unix 世界採用 X 作爲顯示服務器成爲事實標準已經
歷史悠久， X 協議出現以來已經有了近 30 年，現在的“最新”版本 X11 發佈以來也
已經超過了 25 年 [1]_ ，比 Linux 的年齡要老不少。這期間顯示設備也發生了多代
變革，如此古老的架構要跟上現代顯示設備和應用的需求也着實不易。

而且造成問題的不僅僅是 X11 這邊，更大的問題在各個硬件廠商對於開發驅動程序的
熱情不足，甚至惹怒 `Linus 當衆對Nvidia豎起中指 
<http://cn.engadget.com/2012/06/18/linus-torvalds-nvidia-linux/>`_ 。

.. [1] 參考 `X窗口系統 <http://zh.wikipedia.org/wiki/X_Window系統>`_ 。
       「最初是1984年麻省理工學院的研究…… X11，是在1987年9月所發佈。」

承　X11 的多顯示器支持
++++++++++++++++++++++++++++++++++

零　傳統 X11 協議的 Multiseat 支持
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
我不知道 `Multiseat <http://en.wikipedia.org/wiki/Multiseat_configuration>`_ 
這個術語翻譯成中文的話應該怎麼寫，直譯作「多座位」的話感覺不明所以，翻譯成
「多終端」的話容易讓人聯想到早期 `電傳打字機 
<http://zh.wikipedia.org/wiki/電傳>`_ 組成的終端設備，於是留作 Multiseat 
不譯。Multiseat 的概念很簡單，就是多個用戶通過多組輸入輸出設備（通常是鼠標、
鍵盤、顯示器）登錄到同一臺服務器上，各自獨立執行自己的程序。

Multiseat 應該不屬於 Multihead 的一種，只是爲了完整性這裏也說一下傳統 X11 
協議的 Multiseat 支持。一個典型的 Multiseat 配置如下圖所示：

.. figure:: https://www.lucidchart.com/publicSegments/view/511d9eab-66c8-4a8c-997c-536f0a004234/image.png 
   :alt: Multiset Setup on X11
   :width: 90%

   圖1 X11 協議中對 Multiseat 的支持 (`PDF下載
   <https://www.lucidchart.com/publicSegments/view/511d9dc3-33c4-49a2-a8d2-46490a004d18/image.pdf>`_)


圖中我們可以看到，整個系統有多組輸入輸出設備，然後每一組設備上面運行一套
X server ，相互之間互相獨立。每個 X server 被分配一個獨立的 Display ，有個
Display 號碼，通常從 0 開始計算。服務器名加上 Display 號構成一個顯示地址，
有點像 TCP 的 URL 中 ``domain:port`` 這樣的格式， X 的顯示地址是
``server:display`` 這樣的格式。然後一般會有一個 `窗口管理器 
<http://zh.wikipedia.org/wiki/X窗口管理器>`_ 作爲一個 client 連在 X server
上，管理這個屏幕上的所有窗口。 Multiseat 的配置中所有 X server 相互獨立，所以
每個登錄用戶可以用自己的窗口管理器，相互沒有干擾。另外也有一些 X server 可以
提供虛擬的顯示設備，比如圖中的 Xephyr 就是把一個窗口的區域虛擬成一套獨立的
顯示設備，從而用於調試等工作，再比如 Xvnc 就是一個基於 VNC 的 X server 。

.. topic:: 關於 X 裏面 server/client 的稱呼
   :class: well

   X 和很多別的程序對 server 和 client 的稱呼不一樣。對於一般的服務器/客戶端
   程序而言，通常把運行在遠程機器上的程序稱爲服務器，比如數據庫服務器或者
   計算服務器。而對於 X 而言，連着鼠標和顯示器的，你眼前的這臺機器纔是 X 的
   服務器，在遠程運行程序的是客戶端。


壹　傳統 X11 協議的多 Screen 支持
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

轉　Wayland是未來麼？
++++++++++++++++++++++++++++++++++

合　別的系統上的多顯示器支持
++++++++++++++++++++++++++++++++++

