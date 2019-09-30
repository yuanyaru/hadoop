# /usr/bin/python
# -*- encoding:utf-8 -*-

# hadoop退出安全模式: hadoop dfsadmin -safemode leave
"""
requests.exceptions.ConnectionError: HTTPConnectionPool:
在运行python程序的主机的hosts文件中加上主机名和ip的映射
"""
# pip3 install pyhdfs
import pyhdfs


def test():
    client = pyhdfs.HdfsClient("192.168.100.71,8088", "yyr")
    hdfs_path = "/"
    # 新建目录
    client.mkdirs("/test-hadoop", permission=777)
    client.rename("/test-hadoop", "/py-hadoop")
    # 获取目录下文件
    # hdfs dfs -ls -R /
    print(client.listdir(hdfs_path))
    # 删除目录
    # hdfs dfs -rm -R /py-hadoop/test-hadoop
    # client.delete("/test-hadoop")
    # 判断目录是否存在
    print(client.exists("/test-hadoop"))
    # 将本地文件上传至hadoop
    # client.copy_from_local(r"D:/Distributed System Deploy and Test/hadoop/prepare.md", r"/py-hadoop/prepare.md")
    # 将hadoop文件down到本地
    # client.copy_to_local(r"/py-hadoop/prepare.md", r"D:/prepare.md")


if __name__ == '__main__':
    test()
