Title: .bashrc和.bash_profile之间的不同
Category: Article
Tags: blog
Summary: .bashrc和.bash_profile之间的不同
picture: images/p.jpg

<center style="font-weight:bold"></center>

区分两者之间的区别，首先要搞清楚`login shell`和`no-login shell`之间的区别。
* login shell
当你通过终端输入用户名和密码，然后进入到terminal，这时候进入的shell环境就叫做是login shell，
例如，通过`ssh`远程进入到主机。
* no-login shell
顾名思义就是不需要输入用户名密码而进入的shell环境，例如你已经登陆了你的桌面电脑，这时候在应用管理
器中找到`termianl`图标，然后双击打开终端，也就是通过像`gnome`,`KDE`这种桌面环境而进入的终端，
这时候你进入的shell环境就是所谓的`no-login shell`环境。

简而言之，就是把你想通过`login shell`运行的shell命令放入到`.bash_profile`中，把想通过`no-login shell`
运行的shell命令放入到`.bashrc`文件中。

* 例外
有一个例外就是在`Mac OS`系统中，当你每次运行termianl的时候，系统都会默认的给你运行一个`login shell`环境，
所以你看到在`Mac OS`系统中`~/`目录下只有一个`.bash_profile`文件而没有`.bashrc`文件，就是这个道理了。

* 如何同时使用两个文件？
那么如果我在`Mac OS`系统中也想把一些shell命令放到`.bashrc`文件中呢？当然不推荐这么做，也没什么意义，那么你可以
创建一个`.bashrc`的文件。然后在`.bash_profile`文件中写上如下代码,
```
if [ -f ~/.bashrc ]; then
   source ~/.bashrc
fi
```
在terminal读取`.bash_profile`文件后就会load`.bashrc`文件中的内容。
