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


在使用Django时，默认是开启对多时区的支持的，在获取时间的时候会是如下形式：

datetime.datetime(2014, 4, 18, 15, 37, 7, tzinfo=<UTC>)

我们可以利用django.utils.timezone中提供的localtime方法来将该时间转换为本地时间：


>>> dt
datetime.datetime(2014, 4, 18, 15, 37, 7, tzinfo=<UTC>)
>>> localtime(dt)
datetime.datetime(2014, 4, 18, 23, 37, 7, tzinfo=<LocalTimezone>)
有时候，我们需要将该时间与当前时间做比较，例如计算差值，你可能会想到直接这么做：


>>> import datetime
>>> now = datetime.datetime.now()
>>> now - dt
不过这是不对的，并告知如下错误：


Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: can't subtract offset-naive and offset-aware datetimes
问题就出在利用datetime.datetime.now()得到的当前时间是offset-naive的，而另外一个却是offset-aware的，因此我们需要将这里的dt转成与now一样的形式，可以这么做：


>>> dt = dt.replace(tzinfo=None)
>>> dt
datetime.datetime(2014, 4, 18, 15, 37, 7)
>>> now - dt
datetime.timedelta(0, 34108, 443000)