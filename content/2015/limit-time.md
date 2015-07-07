Title: Python时间问题
Category: Article
Tags: blog
Summary: Python时间问题
picture: images/p.jpg


<center>Python时间问题</center>

如何计算一个时间是不是在当天？  
today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)  
today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)

这样就可以很方便的计算一个人一些行为是否发生在当天了。