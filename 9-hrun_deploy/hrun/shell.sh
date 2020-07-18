# 首先上 data 传包，安装：yum install -y unzip zip，解压后再执行：. shell.sh
# 一、设置虚拟内存 1G
touch /root/swapfile
sed -i "1c vm.swappiness = 60" /etc/sysctl.conf
dd if=/dev/zero of=/root/swapfile bs=1M count=1024
mkswap /root/swapfile
swapon /root/swapfile
echo "/root/swapfile swap swap defaults 0 0 ">> /etc/fstab


# 二、安装 docker
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
sudo yum makecache fast
sudo yum install -y docker-ce
sudo systemctl start docker
sudo systemctl enable docker


# 三、安装 Mysql、禅道、jenkins
mkdir /root/hrun_mysql
mkdir /root/jenkins
chown -R 1000:1000 ~/jenkins
docker run -p 3306:3306 --name hrun -v ~/hrun_mysql/conf:/etc/mysql/conf.d -v ~/hrun_mysql/data:/var/lib/mysql -v ~/hrun_mysql/logs:/logs -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7
docker run -d -p 8888:80 -p 3386:3306 -e USER="admin" -e PASSWD="123456" -e BIND_ADDRESS="false" -e SMTP_HOST="163.177.90.125 smtp.exmail.qq.com" -v /data/zbox/:/opt/zbox/ --name zentao idoop/zentao:latest
docker run -itd -p 3006:8080 -p 50000:50000 -v ~/jenkins:/var/jenkins_home -e JAVA_OPTS=-Duser.timezone=Asia/Shanghai --name jenkins jenkinsci/blueocean


# 四、安装python3、手动上传包 or 去掉注释自动下载
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel mysql-devel
mkdir /root/python36
mv /root/Python-3.6.8.tgz /root/python36/
cd /root/python36
tar -xvf Python-3.6.8.tgz
cd Python-3.6.8
./configure --prefix=/root/python36
make
make install
ln -s /root/python36/bin/python3.6 /usr/bin/python3
ln -s /root/python36/bin/pip3 /usr/bin/pip3
pip3 install --upgrade pip
rm -rf /root/python36/Python-3.6.8.tgz /root/python36/Python-3.6.8


# 五、docker-compose 安装 easymock
mkdir /root/easymock
mv /root/docker-compose.yml /root/easymock/
pip3 install docker-compose
ln -s /root/python36/bin/docker-compose /usr/bin/
cd /root/easymock/
docker-compose up -d
chown -R 1000:1000 /root/easymock/logs
docker-compose down
docker-compose up -d


# 六、安装 hrun
# yum install -y unzip zip
mkdir /root/hrun_django
mv /root/httprunnermanger_web.zip /root/hrun_django/
echo "----->>请在 Mysql 中创建库 hrun 后，按任意键继续"
cd /root/hrun_django
unzip httprunnermanger_web.zip
cd httprunnermanger_web
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
nohup python3 manage.py runserver 0.0.0.0:8000 >djo.out 2>&1 &
ln -s /root/python36/bin/hrun /usr/bin/hrun
rm -rf /root/hrun_django/httprunnermanger_web.zip
rm -rf /root/data.zip /root/shell.sh


# 七、jenkins 加速 和 安装 python3
docker exec -itu root jenkins /bin/bash -c "cd /etc/apk/ &&\
echo "https://mirrors.ustc.edu.cn/alpine/v3.6/main/" > repositories &&\
echo "https://mirrors.ustc.edu.cn/alpine/v3.6/community/" >> repositories &&\
apk update &&\
apk add python3 &&\
pip3 install --upgrade pip &&\
touch /root/requirements.txt &&\
echo "ddt==1.2.2">> /root/requirements.txt &&\
echo "PyMySQL==0.9.3">> /root/requirements.txt &&\
echo "requests==2.22.0">> /root/requirements.txt &&\
echo "urllib3==1.25.7">> /root/requirements.txt &&\
echo "xlrd==1.2.0">> /root/requirements.txt &&\
echo "xlwt==1.3.0">> /root/requirements.txt &&\
echo "xlutils==2.0.0">> /root/requirements.txt &&\
cd /root &&\
pip3 install -r /root/requirements.txt &&\
cat /var/jenkins_home/secrets/initialAdminPassword"
echo "======>> jenkins password in 上面..."


# 八、开机自启
touch ~/start.sh
echo "ps -aux | grep python|xargs kill -9">> ~/start.sh
echo "cd ~/easymock">> ~/start.sh
echo "docker-compose down">> ~/start.sh
echo "docker restart hrun zentao jenkins">> ~/start.sh
echo "cd ~/hrun_django/httprunnermanger_web">> ~/start.sh
echo "nohup python3 manage.py runserver 0.0.0.0:8000 >djo.out 2>&1 &">> ~/start.sh
echo "cd ~/easymock">> ~/start.sh
echo "docker-compose up -d">> ~/start.sh
echo ". ~/start.sh">> /etc/rc.d/rc.local
chmod +x /etc/rc.d/rc.local
echo "======>>已经全部安装完成,请重启您的设备..."
