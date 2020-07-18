# 切记安装完 mysql 后需要创建一个库名：hrun
# 再将 httprunnermanger_web.zip 上传至目录：/root/hrun_django

# 设置虚拟内存

# 创建等会拿来交换的文件
touch /root/swapfile

# 设置永久生效比例，sed第一行，既是更改第一行。
sed -i "1c vm.swappiness = 70" /etc/sysctl.conf

# 默认设置4096M（1G）
dd if=/dev/zero of=/root/swapfile bs=1M count=1024

# 格式化交换文件：
mkswap /root/swapfile

# 启用交换文件
swapon /root/swapfile

# 设置开机启用：
echo "/root/swapfile swap swap defaults 0 0 ">> /etc/fstab

# 一、自动安装 python3.6.8
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel mysql-devel
mkdir /root/python36
cd /root/python36
wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz
tar -xvf Python-3.6.8.tgz
cd Python-3.6.8
./configure --prefix=/root/python36
make
make install
ln -s /python36/bin/python3.6 /usr/bin/python3
ln -s /python36/bin/pip3 /usr/bin/pip3
pip3 install --upgrade pip


# 二、创建目录、安装压缩软件
mkdir ~/hrun_django
yum install -y unzip zip


# 三、docker 安装
# 1.安装系统依赖工具
# 2.yum的配置管理docker软件源地址
# 3.更新 yum 缓存
# 4.安装docker
# 5.启动docker服务####################
# 6.加入开机启动项####################
sudo yum install -y yum-utils device-mapper-persistent-data lvm2

sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

sudo yum makecache fast

sudo yum install -y docker-ce

sudo systemctl start docker

sudo systemctl enable docker


# 四、mysql 5.7 安装（docker部署）
# 1.docker 安装 mysql5.7 默认3306端口，密码：123456，当前目录下：$PWD/hrun_mysql/
docker run -p 3306:3306 --name hrun -v ~/hrun_mysql/conf:/etc/mysql/conf.d -v ~/hrun_mysql/data:/var/lib/mysql -v ~/hrun_mysql/logs:/logs -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7


# 五、hrun安装（上传 httprunnermanger_web.zip 文件至 /root/hrun_django 目录）
# 1.解压后，pip3进行安装。
# 2.在httprunnermanger_web目录下，同步数据库。
# 3.后台启动web服务，动态查看日志：tali -f djo.out。
# 4.添加软链接，查看hrun版本。
# 创建账号：python3 manage.py createsuperuser
cd /root/hrun_django
unzip httprunnermanger_web.zip
cd /root/hrun_django/httprunnermanger
pip3 install -r requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate

nohup python3 manage.py runserver 0.0.0.0:8000 >djo.out 2>&1 &

ln -s /root/python36/bin/hrun /usr/bin/hrun


# 五、禅道 搭建
# 1.默认端口：8888，账号：admin 密码：123456
docker run -itd -p 8888:80 -p 3316:3306 -e USER="admin" -e PASSWD="123456" -e BIND_ADDRESS="false" -e SMTP_HOST="163.177.90.125 smtp.exmail.qq.com" -v /data/zbox/:/opt/zbox/ --name zentao idoop/zentao:latest


# 六、JDK 搭建
mkdir /usr/java
cd /usr/java
wget https://repo.huaweicloud.com/java/jdk/8u151-b12/jdk-8u151-linux-x64.tar.gz
tar -zxvf jdk-8u151-linux-x64.tar.gz

# java 环境变量，主要看jdk1.x.x_xxx目录是否对应
# 查看JDK版本： java -version
echo "export JAVA_HOME=/usr/java/jdk1.8.0_151">> /etc/profile

echo "export CLASSPATH=$JAVA_HOME/lib">> /etc/profile

echo "export PATH=$PATH:$JAVA_HOME/bin">> /etc/profile

echo "export PATH JAVA_HOME CLASSPATH">> /etc/profile

source  /etc/profile

### git 搭建
yum install git -y


#七、 jenkins 搭建（URL中也可以重启）
### 汉化插件：①Locale ②Localization: Chinese (Simplified) 
### 修改配置：界面->系统管理 -> 系统设置 -> Locale勾选，设置，中文：zh_cn；繁体：zh_tw；英文：en_us
### 配置 git，输入账号密码，描述即可。
mkdir ~/data
cd ~/data
wget https://pkg.jenkins.io/redhat-stable/jenkins-2.204.1-1.1.noarch.rpm
rpm -ivh jenkins-2.204.1-1.1.noarch.rpm
sed -i "29d" /etc/sysconfig/jenkins
sed -i '29a JENKINS_USER="root"' /etc/sysconfig/jenkins
sed -i "56d" /etc/sysconfig/jenkins
sed -i '56a JENKINS_PORT="3006"' /etc/sysconfig/jenkins
/etc/init.d/jenkins start

# 八、开机自启服务
# 1.mysql、hrun、zentao开机自启
touch ~/start.sh
echo "docker start hrun idoop/zentao">> ~/start.sh
echo "cd /root/hrun_django/httprunnermanger_web">> ~/start.sh
echo "ps -aux | grep python|xargs kill -9">> ~/start.sh
echo "nohup python3 manage.py runserver 0.0.0.0:8000 >djo.out 2>&1 &">> ~/start.sh
echo ". ~/start.sh">> /etc/rc.d/rc.local
chmod +x /etc/rc.d/rc.local

# 重启：
reboot