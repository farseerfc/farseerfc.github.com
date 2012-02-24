C++ Tricks 3.2 标号、goto，以及switch的实现
##################################
:date: 2007-09-16 05:08
:tags: 计算机与 Internet

3.2 标号、goto，以及switch的实现
goto语句及标号(label)是最古老的C语言特性，也是最早被人们抛弃的语言特性之一。像汇编语言中的jmp指令一样，goto语句可以跳转到同一函数体中任何标号位置：
void f() {int i=0; Loop: //A label ++i; if(i<10)goto Loop; //Jump to the
label } 在原始而和谐的早期Fortran和Basic时代，我们没有if then
else，没有for和while，甚至没有函数的概念，一切控制结构都靠goto(带条件的或无条件的)构件。软件工程师将这样的代码称作“意大利面条”代码。实践证明这样的代码极容易造成混乱。
自从证明了结构化的程序可以做意大利面条做到的任何事情，人们就开始不遗余力地推广结构化设计思想，将goto像猛兽一般囚禁在牢笼，标号也因此消失。
标号唯一散发余热的地方，是在switch中控制分支流程。
很多人不甚了解switch存在的意义，认为它只是大型嵌套if then
else结构的缩略形式，并且比if语句多了很多“不合理”的限制。如果你了解到switch在编译器内部的实现机制，就不难理解强加在switch之上的诸多限制，比如case后只能跟一个编译期整型常量，比如用break结束每一个case。首先看一个switch实例：
switch (shape.getAngle()) { case 3: cout<<”Triangle”;break; case 4:
cout<<”Square”;break; case 0:case1: cout<<”Not a sharp!”;break; default:
cout<<”Polygon”; } 任何程序员都可以写出与之对应的if结构： int i=
getAngle(shape); if (i==3) cout<<”Triangle”; else if(i==4)
cout<<”Square”; else if(i==0\|\|i==1) [...]|image0|

.. |image0| image:: http://stats.wordpress.com/b.gif?host=farseerfc.wordpress.com&blog=15617405&post=9&subd=farseerfc&ref=&feed=1
