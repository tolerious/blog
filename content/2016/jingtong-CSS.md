Title: <<精通CSS>>读书笔记
Category: Article
Tags: blog
Summary: 好记性不如烂笔头
picture: images/p.jpg


<center>在这本书中我们值得记住哪些东西呢?</center>


第二章
===
- 层叠

    页面展现出来的样式到底是应用的谁的呢?
    层叠采用如下的重要次序:<br>
    1.标有!important的用户样式<br>
    2.标有!important的作者样式<br>
    3.作者样式<br>
    4.用户样式<br>
    5.浏览器/用户代理应用的样式<br>

- 属性选择器

```
    <div tolerious> abc</div>
    <div tolerious='hello'>abc</div>
    <style>
        div[tolerious] { color: red}
        div[tolerious='hello'] {color: blue}
    </style>
```

显示的效果就会如下所示:
        <div tolerious> abc</div>
        <div tolerious='hello'>abc</div>
        <style>
            div[tolerious] { color: red}
            div[tolerious='hello'] {color: blue}
        </style>
       
- 相邻同胞选择器

可以用于定位同一个父元素下某个元素之后的元素.
```
    <div>
    <p class='first_child'>first child.</p>
    <p>sedond child.</p>
    <p>third child.
    </div>
    <style>
        .first_child {
            color: blue;
        }
        .first_child + p {
            color: red;
        }
    </style>
```

显示的效果如下:
<div>
    <p class='first_child'>first child.</p>
    <p>sedond child.</p>
    <p>third child.
</div>
    <style>
        .first_child {
            color: blue;
        }
        .first_child + p {
            color: red;
        }
    </style>
        
- 如何计算特殊性
选择器的特殊性分成4个等级:a,b,c,d<br>
1.如果样式是行内样式,那么a=1<br>
2.b等于ID选择器的数量<br>
3.c等于类,伪类,和属性选择器的数量<br>
4.d等于类型选择器和伪元素选择器的数量<br>

- 通过一个CSS文件引入多个CSS文件
```
    @import url(/css/name.css);
```

- 引入新的字体文件
```
    @font-face {
        font-family: "Emblema One";
        src: url('./EmblemaOne-Regular.woff')
    }
```

第三章
==========
- 
