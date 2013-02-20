GNU/Linux上多显示器支持之现状
=======================================

:slug: multihead
:lang: zhs
:date: 2013-02-13 14:20:21
:tags: multihead, X11, wayland, linux

.. contents::

起　背景
++++++++++++++++++++++++++++++++++

研究室新进了27吋的显示器，安置了1台在我的办公桌上。于是又从报废的机器堆里
翻出了1台小显示器和一块Radeon显卡，组成4显示器的配置。没想到添加硬件本身
很容易，让它们在我的Archlinux上正常工作却花了不少时间。来来回回折腾各种配置
文件甚至改写源代码(xorg, awesome, compton, ...），经过了1个多月之后，现在的
配置总算比较满意，能够让我正常工作了。折腾的过程中尝试了不少解决方案，觉得
这方面的文档实在少得可怜，同时最近又看到一些关于Wayland 和 RandR 的新进展，
于是稍微整理一番。

GNU/Linux 在桌面领域的发展相比较于服务器端而言一直缓慢，市场份额远不及
Windows 和 OSX ，其原因必将是多方面的，多显示器支持(`Multihead
<http://en.wikipedia.org/wiki/Multi-monitor>`_)也即是其硬伤之一。

当然这个过错不在 Linux 这边， Unix 世界采用 X 作为显示服务器成为事实标准已经
历史悠久， X 协议出现以来已经有了近 30 年，现在的“最新”版本 X11 发布以来也
已经超过了 25 年 [1]_ ，比 Linux 的年龄要老不少。这期间显示设备也发生了多代
变革，如此古老的架构要跟上现代显示设备和应用的需求也着实不易。

而且造成问题的不仅仅是 X11 这边，更大的问题在各个硬件厂商对于开发驱动程序的
热情不足，甚至惹怒 `Linus 当众对Nvidia竖起中指 
<http://cn.engadget.com/2012/06/18/linus-torvalds-nvidia-linux/>`_ 。

.. [1] 参考 `X窗口系统 <http://zh.wikipedia.org/wiki/X_Window系统>`_ 。
       「最初是1984年麻省理工学院的研究…… X11，是在1987年9月所发布。」

承　X11 的多显示器支持
++++++++++++++++++++++++++++++++++

零　传统 X11 协议的 Multiseat 支持
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
我不知道 `Multiseat <http://en.wikipedia.org/wiki/Multiseat_configuration>`_ 
这个术语翻译成中文的话应该怎么写，直译作「多座位」的话感觉不明所以，翻译成
「多终端」的话容易让人联想到早期 `电传打字机 
<http://zh.wikipedia.org/wiki/电传>`_ 组成的终端设备，于是留作 Multiseat 
不译。Multiseat 的概念很简单，就是多个用户通过多组输入输出设备（通常是鼠标、
键盘、显示器）登录到同一台服务器上，各自独立执行自己的程序。

Multiseat 应该不属于 Multihead 的一种，只是为了完整性这里也说一下传统 X11 
协议的 Multiseat 支持。一个典型的 Multiseat 配置如下图所示：

.. figure:: https://www.lucidchart.com/publicSegments/view/511d9eab-66c8-4a8c-997c-536f0a004234/image.png 
   :alt: Multiset Setup on X11
   :width: 90%

   图1 X11 协议中对 Multiseat 的支持 (`PDF下载
   <https://www.lucidchart.com/publicSegments/view/511d9dc3-33c4-49a2-a8d2-46490a004d18/image.pdf>`_)


图中我们可以看到，整个系统有多组输入输出设备，然后每一组设备上面运行一套
X server ，相互之间互相独立。每个 X server 被分配一个独立的 Display ，有个
Display 号码，通常从 0 开始计算。服务器名加上 Display 号构成一个显示地址，
有点像 TCP 的 URL 中 ``domain:port`` 这样的格式， X 的显示地址是
``server:display`` 这样的格式。然后一般会有一个 `窗口管理器 
<http://zh.wikipedia.org/wiki/X窗口管理器>`_ 作为一个 client 连在 X server
上，管理这个屏幕上的所有窗口。 Multiseat 的配置中所有 X server 相互独立，所以
每个登录用户可以用自己的窗口管理器，相互没有干扰。另外也有一些 X server 可以
提供虚拟的显示设备，比如图中的 Xephyr 就是把一个窗口的区域虚拟成一套独立的
显示设备，从而用于调试等工作，再比如 Xvnc 就是一个基于 VNC 的 X server 。

.. topic:: 关于 X 里面 server/client 的称呼
   :class: well

   X 和很多别的程序对 server 和 client 的称呼不一样。对于一般的服务器/客户端
   程序而言，通常把运行在远程机器上的程序称为服务器，比如数据库服务器或者
   计算服务器。而对于 X 而言，连着鼠标和显示器的，你眼前的这台机器才是 X 的
   服务器，在远程运行程序的是客户端。


壹　传统 X11 协议的多 Screen 支持
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

转　Wayland是未来么？
++++++++++++++++++++++++++++++++++

合　别的系统上的多显示器支持
++++++++++++++++++++++++++++++++++

