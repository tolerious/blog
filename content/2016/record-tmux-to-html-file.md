Title: 记录tmux内容到html页面
Category: Article
Tags: blog
Summary: 记录tmux
picture: images/p.jpg

<center>记录tmux内容到html页面</center>


* 为何使用  
当使用tmux的时候你时常需要把当前tmux会话中的内容保存下来，tmux2html这个工具可以很方便的让你把
会话中的内容在html页面中进行查看，这样很方便查看tmux会话中的历史。

* 安装
pip install tmux2html

* 使用
tmux2html 2 -o filename --history 8888
保存会话2中的内容到文件filename中， 保存的记录行数是8888行

效果如图所示:
<div>
<img src="/images/tmux2html.png" style="width:800px;height:700px">
</div>

<!-- ![Alt text](/images/tmux2html.png) -->
