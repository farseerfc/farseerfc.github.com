State of Multihead Support on Linux
=======================================

:slug: multihead
:lang: en
:date: 2013-02-23 14:20:21
:tags: multihead, X11, wayland, linux

Recently our lab have purchased some 27 inch monitors, so I got one on my
desktop.

研究室新進了27吋大顯示器，安置了1臺在我的辦公桌上。於是又從報廢的機器堆裏翻出了1臺小顯示器和一塊Radeon顯卡，
組成4顯示器的配置。沒想到添加硬件本身很容易，讓它們在我的Archlinux上正常工作卻花了不少時間。來來回回折騰
各種配置文件甚至改寫源代碼(xorg, awesome, compton, ...）經過了1個多月之後，現在的配置總算比較滿意，
能夠讓我正常工作了。

