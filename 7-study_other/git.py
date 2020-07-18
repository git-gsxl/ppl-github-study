'''
一、更新代码：
1.git  status
2.git add *
3.git commit  –m  “updata detail”
4.git pull （同步当前分支代码）
5.git push origin master

二、Git Bash：
①删除：.SSH文件下的known_hosts(.SSH在C:\Users\Windows用户名目录下)
②输入：ssh-keygen -t rsa -C "你的名字/你的邮箱"
③用记事本打开目录下的id_rsa.pub，将里面的内容复制git上的SSH秘钥

三、下载git代码
1.在一个目录里新建一个git文件：git init
2.git clone https://github.com/lyl-git/Studyxx.git

四、bat脚本自动更新同步代码

H:                               		# 盘符
cd Study_python\xxx                     # 文件目录
git status
git add *
git commit -m "xxx"
git pull
git push origin master
pause

五、git pull 或者提交冲突失败输入：git reset --hard FETCH_HEAD


六、分支操作：

1.--远程未有分支：
①先克隆：git clone xxx.git
②创建分支：git branch newname
③将本地分支推送到远程：git push origin name:name


2.--远程已有分支：
①新建本地分支并对应远程分支：git checkout -b 本地name origin/远程name
②查看分支对应关系：git branch –vv

切换分支：git checkout 分支名
查看本地分支和远程分支：git branch –a
'''