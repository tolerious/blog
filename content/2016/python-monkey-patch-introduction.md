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
但是一旦这么赋值之后那么`Test`类所有的对象调用`add()`函数的时候都会应用乘法而不是加法  

上面的`new_add()`函数其实没有遵守DRY原则，因为我又自己写了函数体中的重复内容，那么下面来一个
改进版：
```
class Test():
  def add(self,x,y):
    return x+y

old_add = Test.add
def dry_new_add(self,x,y):
  return old_add(self,x,y) + 1

t = Test()
t.add(4,5)
Test.add = dry_new_add
t.dry_new_add(4,5)
```
结果是什么？
9和10
