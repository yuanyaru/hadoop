### 集群机器
* hadoop-node1：192.168.100.71
* hadoop-node2：192.168.100.72
* hadoop-node3：192.168.100.73

# 准备工作
### 事先设置好集群机器的主机名
``` bash
hostnamectl set-hostname hadoop-node1
hostnamectl set-hostname hadoop-node2
hostnamectl set-hostname hadoop-node3
```
### 修改/etc/hosts文件，添加：
* 192.168.100.71 hadoop-node1
* 192.168.100.72 hadoop-node2
* 192.168.100.73 hadoop-node3 

然后执行 reboot 命令重启，确保修改后的主机名生效

### 配置 ssh 免密登陆
设置 hadoop-node1 的 root 账户可以无密码登录所有节点
``` bash
ssh-keygen -t rsa
ssh-copy-id root@hadoop-node1
ssh-copy-id root@hadoop-node2
ssh-copy-id root@hadoop-node3
```
* 可用以下命令测试ssh免密登陆是否设置成功
``` bash
ssh root@node2  #不需输入密码即为成功
exit            #退出ssh
```

### 关闭防火墙
实验环境中关闭防火墙，防止后续查看web页面访问受阻。
``` bash
systemctl stop firewalld    # 临时关闭
systemctl disable firewalld  # 禁止开机启动
```

### 安装JDK
``` bash
mkdir -p /usr/local/java
tar -zxf jdk-8u191-linux-x64.tar.gz -C /usr/local/java/
```
配置环境变量
``` bash
vi /etc/profile
#在配置文件的最后添加如下配置
# java
JAVA_HOME=/usr/local/java/jdk1.8.0_191   #自己解压后的jdk目录名称
JRE_JOME=/usr/local/java/jdk1.8.0_191/jre
CLASS_PATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib
PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin
export JAVA_HOME JRE_JOME CLASS_PATH PATH
```
保存退出后，执行以下命令刷新环境变量
``` bash
source /etc/profile
```
进行测试是否成功
``` bash
java -version
```
