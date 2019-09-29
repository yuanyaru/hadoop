### 参照 prepare.md 完成准备工作

### 下载 hadoop

在 hadoop-node1 主机上创建 hadoop 目录

    <span class="hljs-keyword">mkdir</span> -p /usr/<span class="hljs-keyword">local</span>/hadoop
    `</pre>

    上传到 hadoop-node1 主机上，并解压到 /usr/local/hadoop 目录下

    <pre>`tar -zxf hadoop-<span class="hljs-number">3.1</span>.<span class="hljs-number">2</span><span class="hljs-class">.tar</span><span class="hljs-class">.gz</span> -C /usr/local/hadoop/
    `</pre>

    配置环境变量

    <pre>`vi /etc/profile
    <span class="hljs-comment">#在配置文件最后一行添加如下配置</span>
    <span class="hljs-comment"># hadoop</span>
    <span class="hljs-keyword">export</span> HADOOP_HOME=/usr/local/hadoop/hadoop-<span class="hljs-number">3.1</span>.<span class="hljs-number">2</span>
    <span class="hljs-keyword">export</span> PATH=<span class="hljs-variable">$PATH</span>:<span class="hljs-variable">$HADOOP_HOME</span>/bin:<span class="hljs-variable">$HADOOP_HOME</span>/sbin
    `</pre>

    运行如下命令刷新环境变量

    <pre>`<span class="hljs-keyword">source</span> <span class="hljs-regexp">/etc/</span>profile
    `</pre>

    进行测试是否成功

    <pre>`hadoop <span class="hljs-property">version</span>
    `</pre>

    ### 配置 Hadoop3.1.2

    #### 创建目录

    <pre>`<span class="hljs-comment"># 在/usr/local/hadoop目录下创建目录</span>
    cd /usr/<span class="hljs-keyword">local</span>/hadoop/
    <span class="hljs-keyword">mkdir</span> tmp     
    <span class="hljs-keyword">mkdir</span> var  
    <span class="hljs-keyword">mkdir</span> dfs  
    <span class="hljs-keyword">mkdir</span> dfs/name  
    <span class="hljs-keyword">mkdir</span> dfs/data
    `</pre>

    #### 修改配置文件

    进入 hadoop 的配置文件目录下

    <pre>`cd <span class="hljs-regexp">/usr/</span>local<span class="hljs-regexp">/hadoop/</span>hadoop-<span class="hljs-number">3.1</span>.<span class="hljs-number">2</span><span class="hljs-regexp">/etc/</span>hadoop
    `</pre>

    #### vi workers

    <pre>`删除localhost
    添加从节点主机名，例如我这里是：
    hadoop-<span class="hljs-label">node2</span>
    hadoop-<span class="hljs-label">node3</span>
    `</pre>

    #### hadoop-env.sh

    <pre>`在 #  JAVA_HOME=<span class="hljs-regexp">/usr/</span>java/testing hdfs dfs -ls一行下面添加如下代码
    <span class="hljs-keyword">export</span> JAVA_HOME=<span class="hljs-regexp">/usr/</span>local/java/jdk1<span class="hljs-number">.8</span><span class="hljs-number">.0</span>_191
    <span class="hljs-keyword">export</span> HADOOP_HOME=<span class="hljs-regexp">/usr/</span>local/hadoop/hadoop-<span class="hljs-number">3.1</span><span class="hljs-number">.2</span>
    <span class="hljs-keyword">export</span> HDFS_NAMENODE_USER=root
    <span class="hljs-keyword">export</span> HDFS_DATANODE_USER=root
    <span class="hljs-keyword">export</span> HDFS_SECONDARYNAMENODE_USER=root
    <span class="hljs-keyword">export</span> YARN_RESOURCEMANAGER_USER=root
    <span class="hljs-keyword">export</span> YARN_NODEMANAGER_USER=root
    `</pre>

    以下配置在各个文件的`<configuration> </configuration>`中添加

    #### core-site.xml

    <pre>`<span class="hljs-tag"><<span class="hljs-title">configuration</span>></span>
    <span class="hljs-tag"><<span class="hljs-title">property</span>></span>
    <span class="hljs-tag"><<span class="hljs-title">name</span>></span>fs.defaultFS<span class="hljs-tag"></<span class="hljs-title">name</span>></span>
    <span class="hljs-tag"><<span class="hljs-title">value</span>></span>hdfs://192.168.100.71:9000<span class="hljs-tag"></<span class="hljs-title">value</span>></span>
    <span class="hljs-tag"></<span class="hljs-title">property</span>></span>
    <span class="hljs-tag"><<span class="hljs-title">property</span>></span>
    <span class="hljs-tag"><<span class="hljs-title">name</span>></span>hadoop.tmp.dir<span class="hljs-tag"></<span class="hljs-title">name</span>></span>
    <span class="hljs-tag"><<span class="hljs-title">value</span>></span>/usr/local/hadoop/tmp<span class="hljs-tag"></<span class="hljs-title">value</span>></span>
    <span class="hljs-tag"></<span class="hljs-title">property</span>></span>
    <span class="hljs-tag"></<span class="hljs-title">configuration</span>></span>
    `</pre>

    #### hdfs-site.xml

    <pre>`<<span class="hljs-keyword">property</span>>
       <<span class="hljs-property">name</span>>dfs.<span class="hljs-property">name</span>.dir</<span class="hljs-property">name</span>>
       <value>/usr/<span class="hljs-keyword">local</span>/hadoop/dfs/<span class="hljs-property">name</span></value>
       <description>Path <span class="hljs-function_start"><span class="hljs-keyword">on</span></span> <span class="hljs-keyword">the</span> <span class="hljs-keyword">local</span> filesystem <span class="hljs-keyword">where</span> theNameNode stores <span class="hljs-keyword">the</span> namespace <span class="hljs-keyword">and</span> transactions logs persistently.</description>
    </<span class="hljs-keyword">property</span>>
    <<span class="hljs-keyword">property</span>>
       <<span class="hljs-property">name</span>>dfs.data.dir</<span class="hljs-property">name</span>>
       <value>/usr/<span class="hljs-keyword">local</span>/hadoop/dfs/data</value>
       <description>Comma separated <span class="hljs-type">list</span> <span class="hljs-keyword">of</span> paths <span class="hljs-function_start"><span class="hljs-keyword">on</span></span> <span class="hljs-keyword">the</span> localfilesystem <span class="hljs-keyword">of</span> a DataNode <span class="hljs-keyword">where</span> <span class="hljs-keyword">it</span> should store <span class="hljs-keyword">its</span> blocks.</description>
    </<span class="hljs-keyword">property</span>>
    <<span class="hljs-keyword">property</span>>
    <<span class="hljs-property">name</span>>dfs.namenode.http-address</<span class="hljs-property">name</span>>
    <value><span class="hljs-number">192.168</span><span class="hljs-number">.100</span><span class="hljs-number">.71</span>:<span class="hljs-number">50070</span></value>
    </<span class="hljs-keyword">property</span>>
    <<span class="hljs-keyword">property</span>>
    <<span class="hljs-property">name</span>>dfs.namenode.secondary.http-address</<span class="hljs-property">name</span>>
    <value><span class="hljs-number">192.168</span><span class="hljs-number">.100</span><span class="hljs-number">.71</span>:<span class="hljs-number">50090</span></value>
    </<span class="hljs-keyword">property</span>>
    <<span class="hljs-keyword">property</span>>
       <<span class="hljs-property">name</span>>dfs.replication</<span class="hljs-property">name</span>>
       <value><span class="hljs-number">2</span></value>
    </<span class="hljs-keyword">property</span>> 
    <<span class="hljs-keyword">property</span>>
          <<span class="hljs-property">name</span>>dfs.permissions</<span class="hljs-property">name</span>>
          <value><span class="hljs-constant">false</span></value>
          <description>need <span class="hljs-keyword">not</span> permissions</description>
    </<span class="hljs-keyword">property</span>>
    `</pre>

    #### yarn-site.xml

    在命令行下输入如下命令，并将返回的地址复制，在配置下面的 yarn-site.xml 时会用到。

    <pre>`hadoop <span class="hljs-keyword">classpath</span>
    `</pre>
    <pre>`<span class="hljs-tag"><<span class="hljs-title">property</span>></span>
    <span class="hljs-tag"><<span class="hljs-title">name</span>></span>yarn.resourcemanager.hostname<span class="hljs-tag"></<span class="hljs-title">name</span>></span>
    <span class="hljs-tag"><<span class="hljs-title">value</span>></span>hadoop-node1<span class="hljs-tag"></<span class="hljs-title">value</span>></span>
    <span class="hljs-tag"></<span class="hljs-title">property</span>></span>
    <span class="hljs-tag"><<span class="hljs-title">property</span>></span>
    <span class="hljs-tag"><<span class="hljs-title">name</span>></span>yarn.nodemanager.aux-services<span class="hljs-tag"></<span class="hljs-title">name</span>></span>
    <span class="hljs-tag"><<span class="hljs-title">value</span>></span>mapreduce_shuffle<span class="hljs-tag"></<span class="hljs-title">value</span>></span>
    <span class="hljs-tag"></<span class="hljs-title">property</span>></span>
    <span class="hljs-tag"><<span class="hljs-title">property</span>></span>
    <span class="hljs-tag"><<span class="hljs-title">name</span>></span>yarn.application.classpath<span class="hljs-tag"></<span class="hljs-title">name</span>></span>
    <span class="hljs-tag"><<span class="hljs-title">value</span>></span>输入刚才返回的Hadoop classpath路径<span class="hljs-tag"></<span class="hljs-title">value</span>></span>
    <span class="hljs-tag"></<span class="hljs-title">property</span>></span>
    `</pre>

    #### mapred-site.xml

    <pre>` <span class="hljs-tag"><<span class="hljs-title">property</span>></span>
        <span class="hljs-tag"><<span class="hljs-title">name</span>></span>mapred.job.tracker<span class="hljs-tag"></<span class="hljs-title">name</span>></span>
        <span class="hljs-tag"><<span class="hljs-title">value</span>></span>hadoop-node1:49001<span class="hljs-tag"></<span class="hljs-title">value</span>></span>
    <span class="hljs-tag"></<span class="hljs-title">property</span>></span>
    <span class="hljs-tag"><<span class="hljs-title">property</span>></span>
          <span class="hljs-tag"><<span class="hljs-title">name</span>></span>mapred.local.dir<span class="hljs-tag"></<span class="hljs-title">name</span>></span>
           <span class="hljs-tag"><<span class="hljs-title">value</span>></span>/usr/local/hadoop/var<span class="hljs-tag"></<span class="hljs-title">value</span>></span>
    <span class="hljs-tag"></<span class="hljs-title">property</span>></span>
    <span class="hljs-tag"><<span class="hljs-title">property</span>></span>
           <span class="hljs-tag"><<span class="hljs-title">name</span>></span>mapreduce.framework.name<span class="hljs-tag"></<span class="hljs-title">name</span>></span>
           <span class="hljs-tag"><<span class="hljs-title">value</span>></span>yarn<span class="hljs-tag"></<span class="hljs-title">value</span>></span>
    <span class="hljs-tag"></<span class="hljs-title">property</span>></span>
    `</pre>

    #### 同步

    使用 scp 命令将 hadoop-node1 下的目录复制到各个从节点的相应位置上

    <pre>`scp -r <span class="hljs-regexp">/usr/</span>local<span class="hljs-regexp">/java hadoop-node2:/</span>usr<span class="hljs-regexp">/local/</span>java
    scp -r <span class="hljs-regexp">/usr/</span>local<span class="hljs-regexp">/hadoop hadoop-node2:/</span>usr<span class="hljs-regexp">/local/</span>hadoop
    scp -r <span class="hljs-regexp">/etc/</span>profile hadoop-<span class="hljs-string">node2:</span><span class="hljs-regexp">/etc/</span>

    scp -r <span class="hljs-regexp">/usr/</span>local<span class="hljs-regexp">/java hadoop-node3:/</span>usr<span class="hljs-regexp">/local/</span>java
    scp -r <span class="hljs-regexp">/usr/</span>local<span class="hljs-regexp">/hadoop vnode3:/</span>usr<span class="hljs-regexp">/local/</span>hadoop
    scp -r <span class="hljs-regexp">/etc/</span>profile hadoop-<span class="hljs-string">node3:</span><span class="hljs-regexp">/etc/</span>
    `</pre>

    #### 在从节点上分别运行下述命令刷新环境变量

    <pre>`<span class="hljs-keyword">source</span> <span class="hljs-regexp">/etc/</span>profile
    `</pre>

    #### 格式化节点

    在 hadoop-node1 中运行下述命令，格式化节点

    <pre>`hdfs namenode -<span class="hljs-built_in">format</span>
    `</pre>

    运行之后不报错，并在倒数第五六行有 successfully 即为格式化节点成功

    ![image](https://github.com/yuanyaru/hadoop/blob/master/images/start-hadoop.jpg)

    运行以下命令，启动 hadoop 集群的服务

    <pre>`<span class="hljs-operator"><span class="hljs-keyword">start</span>-<span class="hljs-keyword">all</span>.sh</span>
    `</pre>

    在 hadoop-node1 上输入 jps 可以看到 hadoop-node1 下的节点

    <pre>`[root<span class="hljs-property">@hadoop</span>-node1 hadoop]<span class="hljs-comment"># jps</span>
    <span class="hljs-number">3667</span> NameNode
    <span class="hljs-number">21157</span> Jps
    <span class="hljs-number">12792</span> ResourceManager
    <span class="hljs-number">3930</span> SecondaryNameNode
    `</pre>

    在 hadoop-node2 下的节点

    <pre>`[root<span class="hljs-property">@hadoop</span>-node2 ~]<span class="hljs-comment"># jps</span>
    <span class="hljs-number">18352</span> Jps
    <span class="hljs-number">18178</span> NodeManager
    <span class="hljs-number">3547</span> DataNode

### 在浏览器上访问 hdfs 的 web 界面

在浏览器上输入[http://192.168.100.71:8088(前者为主节点ip地址，后者为hdfs的web进程对应的端口号](http://192.168.100.71:8088(前者为主节点ip地址，后者为hdfs的web进程对应的端口号))

![image](https://github.com/yuanyaru/hadoop/blob/master/images/8088.jpg)

在浏览器上访问 [http://192.168.100.71:50070](http://192.168.100.71:50070)

![image](https://github.com/yuanyaru/hadoop/blob/master/images/50070.jpg)

在浏览器上访问 [http://192.168.100.71:50090](http://192.168.100.71:50090)

![image](https://github.com/yuanyaru/hadoop/blob/master/images/50090.jpg)