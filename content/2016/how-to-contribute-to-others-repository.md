Title: 如何向别人的项目贡献自己的代码
Category: Article
Tags: blog
Summary: 提交自己的代码到别人的项目
picture: images/p.jpg

<center>如何在Github上向别人的项目贡献自己的代码</center>

* 点击别人项目上的`Fork`按钮

* clone你fork别人的项目到本地  

* clone好后，进入项目目录，运行如下命令`git remote add origin url`其中`origin`根据个人的
喜好，任意配置，url的内容为这个仓库主人的仓库地址，而不是你的，重要的事情说三遍，不是你的仓库地址，
不是你的仓库地址，不是你的仓库地址。

* 操作完成后，我们本地会有一个master分之，记住，你写代码，不要在这个master分之上，因为我们用这个
master分之来跟踪项目主人对这个项目的更新，`git pull origin master`命令会拉取项目主人最新的代码。

* 建立自己的分支，`git checkout -b your_own_branch`其中`your_own_branch`根据你自己的喜好，
随便填写。

* 在你自己的分之进行开发，文档等等。

* 同步项目主人的代码，`git checkout master&&git pull origin master`,`git checkout your_own_branch`,
`git rebase master`,`git push origin your_own_branch`.

* 如果你开发好了功能，想要提交给项目的主人，进入Github页面，点击`pull request`按钮儿，点击完成后，
到项目主人的仓库去看，你会看到在`pull request`中已经有你的`request`了，就等项目的主人审查你的代码就好了。
