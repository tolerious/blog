Title: Python中的Monkey Patch
Category: Article
Tags: blog
Summary: Python中的猴子补丁
picture: images/p.jpg

<center>Python中的猴子补丁</center>

猴子补丁就是一种在运行时，动态修改函数或者方法的本来行为从而达到改变一个模块，库或者是类的行为。

一个简单的例子：
```
class Test():
  def add(self,x,y):
    return x+y


t = Test()
def new_add(self,x,y):
  return x*y

Test.add = new_add
t.add(4,5)
```   
那么请问结果是多少呢？  
答案是：20而不是9
