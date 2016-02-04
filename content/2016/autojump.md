Title: 切换目录的利器Autojump
Category: Article
Tags: blog
Summary: 神之利器Autojump
picture: images/p.jpg

<center style="font-weight:bold">自动补全还没完，跳转目录才是王道</center>

编程中常常遇到在不同目录下切换的需要，但是你所要切换的目录可能比较长，名字你也记不得，所以你要不停的
按下`Tab`键，有一个工具可以为你解决这个烦恼，那就是`Autojump`。

下面讲讲如何配置`Autojump`.操作系统`Ubuntu 14.04`

* 下载
地址为[这里](http://pan.baidu.com/s/1mh4G5bq)

* 安装  
1. 下载安装包后进入到目录。
2. `chmod +x install.sh`  `./install.sh`
3. 根据终端内的提示把`[[ -s ~/.autojump/etc/profile.d/autojump.sh ]] && . ~/.autojump/etc/profile.d/autojump.sh`
添加到你的`.bashrc`文件中。
4. 运行`source ./bashrc`

* 使用autojump
例如你的nginx配置文件目录在`/usr/local/nginx/conf`你下次想直接进入到这个目录，你只要先进去这个目录，然后跳回
home目录再输入`j conf`，看看发生了什么，你一下子就进入到了nginx配置文件的目录。


一些常用的命令
========================
* j  目录名称   
跳转到曾经的历史，例如上文所说的跳转到nginx的配置文件目录

* j --stat

<img src="/images/autojump-1.png">

如图所示，冒号前面显示的小数代表的是你在这个目录停留的时间长短，如图上，有两个叫conf的文件夹，那么当我运行`j conf`命令的时候会跳到
那个文件夹呢？答案是冒号前面的数字哪个大就会跳转到哪个的前面。
