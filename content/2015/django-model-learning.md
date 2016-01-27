Title: Django model总结
Category: Article
Tags: blog
Summary: 一直想写一篇关于自己学习Django model的心得。
picture: images/p.jpg


<center>Django Model总结</center>

学习Django Model最基本的就是要能够写一个model,然后把你的app的名字放到settings文件中,在Django shell环境中创建,保存,查询删除一个对象.
在学会了这个基本操作后,你就会觉得一切事情是如此简单,在一段时间内,你觉得你的需求用这一点点知识完全能够满足,但是了解更多的内容对于你解决问题会更有帮助,更快速,更高效.
接下来你需要学习一些基本的Fields,是文本,还是时间类型,整型,亦或是文件类型等等,你可以根据需要来选择合适的类型,如果Django Model中现有的类型都无法满足你的话,你甚至可以去自己定制类型.
当然学会了基本类型后,你就可以了解一些在field中的候选项了,例如blank,null,choices等等,在Django Model中你是不需要自己去指定primary key的,Django会自动帮你生成一个递增的id来作为你Model的primary key,同样的，你也可以指定自己的primary key,

查询的时候尽量使用Cache，而不要每次都去hit数据库