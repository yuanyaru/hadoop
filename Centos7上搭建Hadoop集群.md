### 参照 prepare.md 完成准备工作

### 下载 hadoop
在 hadoop-node1 主机上创建 hadoop 目录
``` bash
mkdir -p /usr/local/hadoop
```
上传到 hadoop-node1 主机上，并解压到 /usr/local/hadoop 目录下
``` bash
tar -zxf hadoop-3.1.2.tar.gz -C /usr/local/hadoop/
```
配置环境变量
``` bash
vi /etc/profile
#在配置文件最后一行添加如下配置
# hadoop
export HADOOP_HOME=/usr/local/hadoop/hadoop-3.1.2
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
``` 
运行如下命令刷新环境变量
``` bash
source /etc/profile
```
进行测试是否成功
``` bash
hadoop version
```

### 配置 Hadoop3.1.2
#### 创建目录
``` bash
# 在/usr/local/hadoop目录下创建目录
cd /usr/local/hadoop/
mkdir tmp     
mkdir var  
mkdir dfs  
mkdir dfs/name  
mkdir dfs/data  
```

#### 修改配置文件
进入hadoop的配置文件目录下
``` bash
cd /usr/local/hadoop/hadoop-3.1.2/etc/hadoop
```

#### vi workers
``` bash
删除localhost
添加从节点主机名，例如我这里是：
hadoop-node2
hadoop-node3
```

#### hadoop-env.sh
``` bash
在 #  JAVA_HOME=/usr/java/testing hdfs dfs -ls一行下面添加如下代码
export JAVA_HOME=/usr/local/java/jdk1.8.0_191
export HADOOP_HOME=/usr/local/hadoop/hadoop-3.1.2
export HDFS_NAMENODE_USER=root
export HDFS_DATANODE_USER=root
export HDFS_SECONDARYNAMENODE_USER=root
export YARN_RESOURCEMANAGER_USER=root
export YARN_NODEMANAGER_USER=root
```

以下配置在各个文件的<configuration></configuration>中添加
#### core-site.xml
``` bash
<configuration>
<property>
<name>fs.defaultFS</name>
<value>hdfs://192.168.100.71:9000</value>
</property>
<property>
<name>hadoop.tmp.dir</name>
<value>/usr/local/hadoop/tmp</value>
</property>
</configuration>
```

#### hdfs-site.xml
``` bash
<property>
   <name>dfs.name.dir</name>
   <value>/usr/local/hadoop/dfs/name</value>
   <description>Path on the local filesystem where theNameNode stores the namespace and transactions logs persistently.</description>
</property>
<property>
   <name>dfs.data.dir</name>
   <value>/usr/local/hadoop/dfs/data</value>
   <description>Comma separated list of paths on the localfilesystem of a DataNode where it should store its blocks.</description>
</property>
<property>
<name>dfs.namenode.http-address</name>
<value>192.168.100.71:50070</value>
</property>
<property>
<name>dfs.namenode.secondary.http-address</name>
<value>192.168.100.71:50090</value>
</property>
<property>
   <name>dfs.replication</name>
   <value>2</value>
</property> 
<property>
      <name>dfs.permissions</name>
      <value>false</value>
      <description>need not permissions</description>
</property>
```

#### yarn-site.xml
在命令行下输入如下命令，并将返回的地址复制，在配置下面的 yarn-site.xml 时会用到。
``` bash
hadoop classpath
```
``` bash
<property>
<name>yarn.resourcemanager.hostname</name>
<value>hadoop-node1</value>
</property>
<property>
<name>yarn.nodemanager.aux-services</name>
<value>mapreduce_shuffle</value>
</property>
<property>
<name>yarn.application.classpath</name>
<value>输入刚才返回的Hadoop classpath路径</value>
</property>
```

#### mapred-site.xml
``` bash
 <property>
    <name>mapred.job.tracker</name>
    <value>hadoop-node1:49001</value>
</property>
<property>
      <name>mapred.local.dir</name>
       <value>/usr/local/hadoop/var</value>
</property>
<property>
       <name>mapreduce.framework.name</name>
       <value>yarn</value>
</property>
```

#### 同步
使用 scp 命令将hadoop-node1下的目录复制到各个从节点的相应位置上
``` bash
scp -r /usr/local/java hadoop-node2:/usr/local/java
scp -r /usr/local/hadoop hadoop-node2:/usr/local/hadoop
scp -r /etc/profile hadoop-node2:/etc/
 
scp -r /usr/local/java hadoop-node3:/usr/local/java
scp -r /usr/local/hadoop vnode3:/usr/local/hadoop
scp -r /etc/profile hadoop-node3:/etc/
```

#### 在从节点上分别运行下述命令刷新环境变量
``` bash
source /etc/profile
```

#### 格式化节点
在 hadoop-node1 中运行下述命令，格式化节点
``` bash
hdfs namenode -format
```
运行之后不报错，并在倒数第五六行有 successfully 即为格式化节点成功

![image](https://github.com/yuanyaru/hadoop/blob/master/images/start-hadoop.jpg)

运行以下命令，启动 hadoop 集群的服务
``` bash
start-all.sh
```

在 hadoop-node1 上输入 jps 可以看到 hadoop-node1 下的节点
``` bash
[root@hadoop-node1 hadoop]# jps
3667 NameNode
21157 Jps
12792 ResourceManager
3930 SecondaryNameNode
```
在 hadoop-node2 下的节点
[root@hadoop-node2 ~]# jps
18352 Jps
18178 NodeManager
3547 DataNode

### 在浏览器上访问 hdfs 的 web 界面
在浏览器上输入http://192.168.100.71:8088(前者为主节点ip地址，后者为hdfs的web进程对应的端口号)

![image](https://github.com/yuanyaru/hadoop/blob/master/images/8088.jpg)

在浏览器上输入http://192.168.100.71:50070

![image](https://github.com/yuanyaru/hadoop/blob/master/images/50070.jpg)

在浏览器上输入http://192.168.100.71:50090

![image](https://github.com/yuanyaru/hadoop/blob/master/images/50090.jpg)
