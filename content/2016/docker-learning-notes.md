Title: Docker学习笔记
Category: Article
Tags: blog
Summary: Docker入门笔记
picture: images/p.jpg

<center>记录下Docker学习中的乐趣</center>


* re-attach container  

通过命令`docker run -i -t image-name /bin/bash`而创建container以后，想要退出这个container你可以
按住Ctrl+p然后再按Ctrl+q暂时离开当前container，这时离开的container还是在运行的。直接输入exit命令
这个container在你退出的时候就关闭了，


* 保存container中的状态,并且把改动打包成为一个images

`docker commit <container> <some_name>:<your_tag>`

`docker commit -m "some infomation" -a "tolerious" <container> <some_name>:<your_tag>`

`<some_name>`为`tolerious/tolerious-ubuntu`这种格式。

* 从`Dockerfile`构建自己的image

首先写好的`Dockerfile`,具体命令不再赘述，然后运行命令`docker build -t <some_name>:<tab_name> .`
最末尾的那个“.”千万不要忘记，

* push自己构建的image到DockerHub
