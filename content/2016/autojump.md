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
