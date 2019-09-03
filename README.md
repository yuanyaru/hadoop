* Hadoop 实现了一个分布式文件系统（Hadoop Distributed File System），简称 HDFS。

* HDFS有高容错性的特点，并且设计用来部署在低廉的（low-cost）硬件上；而且它提供高吞吐量（high throughput）来访问应用程序的数据，适合那些有着超大数据集（large data set）的应用程序。

* HDFS放宽了（relax）POSIX 的要求，可以以流的形式访问（streaming access）文件系统中的数据。

* Hadoop 框架最核心的设计就是：HDFS 和 MapReduce。HDFS 为海量的数据提供了存储，而 MapReduce 则为海量的数据提供了计算。
