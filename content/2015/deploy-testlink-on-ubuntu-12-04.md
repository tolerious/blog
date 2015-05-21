Title: Ubuntu12.04部署TestLink
Category: Article
Tags: blog
Summary: TestLink是一个test case管理系统
picture: images/p.jpg






###安装包准备###
* [testlink-1.9.12.tar.gz](http://pan.baidu.com/s/1qWoKQyo)  
* Ubuntu12.04LTS  

###环境准备###
* 安装Apache，PHP  
`sudo tasksel`，出现如图所示的界面  
![Alt text](http://ww4.sinaimg.cn/mw690/a036a21agw1ep3gjxvt6sj21kw0xi7gi.jpg)  
选择`OpenSSH server`然后就会自动安装所需要的一整套环境了，但是需要注意的是这里安装的PHP版本比TestLink所要求的版本要低，所以要从另外的仓库中安装满足要求的PHP版本  
* 升级PHP  
For upgrate to PHP 5.4.x  
`sudo add-apt-repository ppa:ondrej/php5-oldstable`  
For upgrate to PHP 5.5.x  
`sudo add-apt-repository ppa:ondrej/php5`  
`sudo apt-get update`  
`sudo apt-get install php-pear php5-cli php5-common php5-curl php5-dev php5-gd php5-mcrypt php5-mysql php5-pgsql php5-xdebug`

* 解压testlink压缩包  
把下载testlink压缩包解压到`/var/www/`目录下，并注意修改权限，使得www-data用户能有权限访问  
* 安装TestLink  
在浏览器中输入http://server_ip/testlink/install/index.php，根据提示页面一步步安装，中间会提示有两个文件夹没有，根据提示的路径自己建立就好了，简单几步轻松搞定。
