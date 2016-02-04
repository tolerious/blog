Title: Ubuntu14.04安装Nginx
Category: Article
Tags: blog
Summary: 如何安装Nginx
picture: images/p.jpg

<center>安装Nginx1.8.1</center>

* [下载](http://nginx.org/download/nginx-1.8.1.tar.gz)Nginx1.8.1

* 安装依赖包  
1. apt-get install libpcre3 libpcre3-dev  
2. sudo apt-get install libssl-dev

* 编译
1. ./configure --with-http_ssl_module --with-mail --with-mail_ssl_module
2. make && sudo make install

* 后续步骤
1. 在/etc/init.d/文件夹中创建名称为nginx的文件，可在如下地址[下载](http://pan.baidu.com/s/1eRnXnQa)
2. 运行如下命令`sudo /usr/sbin/update-rc.d -f nginx defaults`

* 重启Nginx
1. sudo service nginx restart

* 安装完成


安装完成后，`nginx.conf`配置文件所在路径为`/usr/local/nginx/conf`
