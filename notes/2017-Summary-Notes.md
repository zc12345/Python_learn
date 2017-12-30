# 2017 Notes Summary

## Content

* [1. Linux](#01)
* [1-1 Git bash](#01-1)
* [1-2 Linux file system](#01-2)
* [1-3 Linux remote login](#01-3)
* [1-4 Keras installation](#01-4)
* [2. MATLAB](#02)
* [2-1 MATLAB Installation](#02-1)
* [2-2 Matconvnet](#02-2)
* [2-3 MATLAB Programming](#02-3)
* [3. Python](#03)
* [3-1 Python spider](#03-1)
* [4. Deep learning](#04)
* [4-1 CNN](#04-1)
* [4-2 RNN](#04-2)
* [4-3 others](#04-3)
* [5. Paper](#05)
* [5-1 Faster R-CNN](#05-1)
* [5-2 DeLay](#05-2)
* [5-3 DeepLab](#05-3)
* [5-4 other papers](#05-4)
* [6. Keypoint detection](#06)
* [6-1 code](#06-1)
* [6-2 dataset](#06-2)
* [6-3 debug](#06-3)
* [7. Others](#07)
* [7-1 mindmap](#07-1)
* [7-2 markdown](#07-2)
* [7-3 deeplearning server](#07-3)


----------------------------

## <span id="01">01 Linux </span>
#### <span id="01-1">1-1 git bash常用命令小结</span>
```
# 创建项目并且上传到GitHub

# 方式1. 本地创建文件然后上传到远程仓库

#1.创建项目
mkdir <directory name> #新建文件夹
touch <file name> #新建文件
git init #初始化本地仓库
#2.和远程仓库关联
git remote add origin git@ github.com:<user>/<respository>.git # 设置远程仓库地址
#3.添加更改并上传
git add .            # 添加全部变更
git add <file name>  # 添加指定文件变更
git commit -m "introduction" # 保存文件
git push # 全部分支上传到远程仓库
git push origin master    # 上传master分支
git push -u origin master # 如果master分支不存在则创建master分支

# 方式2. 克隆远程仓库文件到本地

git clone <url>
git remote add pb <url> # 这一步好像并不是必需
# ... 接下来创建文件然后添加上传更改如上
```

> 参考资料
> 1. [官方文档 git docs](https://git-scm.com/docs)
> 2. [【CNblogs】 Git常用命令](http://www.cnblogs.com/cspku/articles/Git_cmds.html)

#### <span id="01-2">1-2 Linux文件操作</span>
```bash
# 1. 文件压缩与解压
$ zip <filename> <dir> #压缩zip文件
$ unzip <filename>.zip <dir> #解压zip文件
$ rar -a <filename> <dir> #压缩rar文件
$ rar -x <filename>.rar #解压rar文件
$ gzip <filename> <dir> #压缩为gz文件
$ gunzip <filename>.gz #解压gz文件
$ gzip -d <filename>.gz #解压gz文件
$ tar -xcf <filename> <dir> #压缩为tar文件
$ tar -xvf <filename>.tar #解压tar文件
$ tar -zxcf <filename> <dir> #压缩为tar.gz文件
$ tar -zxvf <filename>.tar.gz #解压tar.gz文件
# 2. 查看文件夹
$ df -h #查看一级文件夹大小、使用比例、档案系统及其挂入点
$ ls -lR|grep "^d"|wc -l #查看某文件夹下文件夹的个数，包括子文件夹里的
$ ls -lR|grep "^-"|wc -l #查看某文件夹下文件的个数，包括子文件夹里的
$ du -sh #查看当前文件夹大小
$ du -sh * | sort -n #统计当前文件夹(目录)大小，并按文件大小排序
$ du -sk filename #查看指定文件大小
# 3. 其他
$ w #最近登录用户的最近一次操作
$ who #当前用户
$ history #历史命令
```
> reference
1. [linux下解压命令大全][linux1]
2. [linux查看文件夹大小、文件个数的方法][linux2]
3. [Linux下查看文件和文件夹大小][linux3]
4. [Linux硬链接与软链接的联系与区别][linux4]
5. [linux下显卡信息的查看][linux5]

[linux1]: http://www.cnblogs.com/eoiioe/archive/2008/09/20/1294681.html "linux下解压命令大全"
[linux2]: http://blog.csdn.net/mycms5/article/details/19984893 "linux查看文件夹大小、文件个数的方法"
[linux3]: http://www.cnblogs.com/benio/archive/2010/10/13/1849946.html "Linux下查看文件和文件夹大小"
[linux4]: https://www.ibm.com/developerworks/cn/linux/l-cn-hardandsymb-links/index.html# "硬链接与软链接的联系与区别"
[linux5]: http://blog.csdn.net/wind19/article/details/17095541 "linux下显卡信息的查看"

#### <span id="01-3">1-3 linux远程登录协议 </span>

```bash
# 1. 远程登录服务器
$ ssh username@115.154.137.65 
# 2. 远程文件传输
$ scp local_dir username@servername:remote_dir #本地文件上传到远程服务器
$ scp -r local_dir username@servername:remote_dir #本地文件夹上传到远程服务器
$ scp username@servername:remote_dir local_dir #远程文件下载到本地
$ scp -r username@servername:remote_dir local_dir #远程文件夹下载到本地
# 3. 查看GPU使用情况
$ navidia-smi
$ watch -n l navidia-smi #动态监视GPU使用情况
$ lspci | grep -i vga  #查看显卡信息
$ lspci -v -s 00:0f.0  #查看指定显卡的详细信息
# 4. 查看CPU使用情况
$ top #动态实时监控CPU利用率，进程状态和内存利用率
$ mpstat #对所有处理器的全部平均值做一次报告
$ mpstat -P ALL #查看每一个CPU的情况
$ sar #收集，报告和保存系统活动信息
$ free #查看总内存、使用、空闲等情况
$ ps ux #按默认方式查看状态
$ ps -H -eo user,pid,ppid,tid,time,%cpu,cmd --sort=%cpu #指定显示列和排序方式
$ ps -eo pcpu,pid,user,args | sort -k 1 -r | head -16
```
#### <span id="01-4">1-4 keras安装 </span>

###### 1. 运行环境

1. 阿里云服务器
2. 操作系统：Ubuntu 16.04
3. 远程连接：Xshell

###### 2. 安装步骤

```
# 仅CPU版本

# 0. Ubuntu初始环境设置

# 0.1 系统升级
$ sudo apt update
$ sudo apt upgrade
# 0.2 安装python基础开发包
$ sudo apt install -y python-dev python-pip python-nose gcc g++ git gfortran vim
# 0.3 安装运算加速库
$ sudo apt install -y libopenblas-dev liblapack-dev libatlas-base-dev

# 1. 隔离环境VirtualEnv的安装和使用

$ sudo apt-get install python-pip python-dev python-virtualenv
$ virtualenv --system-site-packages ~/tensorflow
$ cd ~/tensorflow
$ source bin/activate  # 如果使用 bash
(tensorflow)$  # 终端提示符应该发生变化

# 2. Keras安装和配置（基于TensorFlow）

(tensorflow)$ pip install -U --pre pip setuptools wheel
(tensorflow)$ pip install -U --pre numpy scipy matplotlib scikit-learn scikit-image
(tensorflow)$ pip install -U --pre tensorflow # CPU版本
(tensorflow)$ pip install -U --pre keras
(tensorflow)$ python
>>> import tensorflow
>>> import keras

# 3. Keras中mnist数据集测试

(tensorflow)$ git clone https://github.com/fchollet/keras.git
(tensorflow)$ cd keras/examples/
(tensorflow)$ python mnist_mlp.py

# 4. 关闭VirtualEnv
(tensorflow)$ deactivate  # 停用 virtualenv

```

> 参考资料
> 1. [TensorFlow 中文文档](http://www.tensorfly.cn/tfdoc/get_started/os_setup.html#virtualenv_install)
> 2. [Keras 中文文档](https://keras-cn.readthedocs.io/en/latest/for_beginners/keras_linux/)
> 3. [Caffe入门与实践-简介](https://zhuanlan.zhihu.com/p/24087905)
> 4. [caffe入门与实践-LeNet MNIST 教程](https://zhuanlan.zhihu.com/p/24110318)
> 5. [Installing TensorFlow](https://www.tensorflow.org/install/)

----------------------------

## <span id="02">02 MATLAB </span>
#### <span id="02-1">2-1 MATLAB安装和使用</span>
> 说明：Linux系统，非破解版，GCC >= 4.8 

1. 官网下载安装包，使用`$unzip`命令解压，使用`./install`命令安装，安装时需要使用图形界面操作
```
$ cd ~/Downloads
$ mkdir matlab
$ cd matlab/
$ cp ~/Downloads/matlab_R2016a_glnxa64.zip ./
$ unzip matlab_R2016a_glnxa64.zip
$ ./install
```
2-1.  指定安装目录（具有root或者sudo权限）
```
$ sudo chmod -r 777 /usr/local/*  #提高读写权限
$ ln -s $MATLAB/bin/matlab matlab #创建快捷方式
$ matlab #启动matlab
```
2-2. 指定安装目录（没有sudo权限），只能安装在当前用户的文件夹下
```
$ ln -s $MATLAB/bin/matlab matlab #在常用matlab的文件目录下操作
$ ./matlab #启动matlab
```
3. 破解版matlab安装（.iso文件离线安装，需要sudo权限）
```
# 1. 挂载镜像
$ cd ~/
$ mkdir matlab
$ sudo mount -t auto -o loop Downloads/matlab R2016b linux/R2016b_glnxa64_dvd1.iso matlab/
# 2. 安装matlab（key在readme.txt中）
$ sudo ./matlab/install #调用图形界面进行可视化安装
$ sudo mount -t auto -o loop Downloads/matlab R2016b linux/R2016b_glnxa64_dvd2.iso matlab/ #挂载第二部分镜像
$ unmount matlab/ #完成安装后取消挂载
$ sudo rm -r matlab #删除空文件夹
# 3. 激活matlab
$ cd /usr/local/MATLAB/R2016b/bin
$ ./matlab #启动matlab，第一次启动建议用sudo命令
$ sudo cp Crack/R2016b/bin/glnxa64/libcufft.so.7.5.18 /usr/local/MATLAB/R2016b/bin/glnxa64 
$ sudo cp Crack/R2016b/bin/glnxa64/libinstutil.so /usr/local/MATLAB/R2016b/bin/glnxa64
$ sudo cp Crack/R2016b/bin/glnxa64/libmwlmgrimpl.so /usr/local/MATLAB/R2016b/bin/glnxa64
$ sudo cp Crack/R2016b/bin/glnxa64/libmwservices.so  /usr/local/MATLAB/R2016b/bin/glnxa64
```
> reference
1. [Ubuntu下安装MATLAB R2014a][mat1]
2. [Ubuntu 16.04安装Matlab 2016b教程][mat2]
3. [Linux系统下安装matlab2016b][mat3]

[mat1]: http://www.jianshu.com/p/60038ffa8870 "matlab R2014a 安装"
[mat2]: http://blog.csdn.net/jesse_mx/article/details/53956358 "matlab R2016b 安装1"
[mat3]: http://blog.csdn.net/Eric2016_Lv/article/details/52653915?locationNum=6#reply "matlab R2016b 安装2"

#### <span id="02-2">2-2 matconvnet安装和编译</span>
```
$ cd ~/Documents
$ git clone https://github.com/vlfeat/matconvnet.git
$ mex -setup mex -setup C++ #当前用户目录下可以在matlab界面命令行运行该命令，或者运行./mex
$ sudo apt-get install build-essential libjpeg-turbo8-dev # install LibJPEG in and Ubuntu/Debian-like distributions
$ sudo yum install gcc gcc-c++ libjpeg-turbo-devel #Fedora/Centos/RedHat-like distributions
$ matlab
$ matlab -nosplash -nodesktop [-r filename] #matlab命令行启动
> cd matconvnet/
> addpath matlab
> vl_compilenn #CPU编译
> vl_compilenn('enableGpu',true) #GPU编译
> run <MatConvNet>/matlab/vl_setupnn
> vl_testnn
```
#### <span id="02-3">2-3 MATLAB编程</span>
###### 1. 面向对象编程-类定义
```matlab
%% 类定义
classdef (ClassAttributes) MyClass < handle % 从handle类派生出子类MyClass
    properties (PropertyAttributes) % 类属性e.g.propoerties(Access = private)
        prop1 = data;
    end
    methods
        function obj = ClassName(arg1,...) % 构造方法
            obj.prop1 = arg1;
            ...
        end
        function [num1, num2, num3 ] = Method1(arg1,...) % 函数方法1
            ...
        end
        function Method2(arg1,arg2,...) % 函数方法2
            ...
        end
    end
    methods(Static) % 静态方法
        funtion staticMethod1(arg1,...)
            ...
        end
    end
    events (ListenAccess = protected) % 事件
      StateChanged
   end
end
%% 类初始化和方法调用
obj1 = MyClass(arg1,...); % 类初始化
obj2 = MyClass; % 声明类
r1 = obj1.Method2(arg1, arg2); % 调用类方法
r2 = Method2(obj, arg1, arg2);
[r3, r4, r5] = Method1(arg1)
r = MyClass.staticMethod1(arg1); % 调用静态方法
```
###### 2. 函数文件
```matlab
function [ans1, ans2] = MethodName(arg1, arg2)
%description
%code
end
```
> reference 
1. [matlab--Class Components][matdoc1]
2. [matlab--Methods and Functions][matdoc2]

[matdoc1]: https://cn.mathworks.com/help/matlab/matlab_oop/class-components.html
[matdoc2]: https://cn.mathworks.com/help/matlab/matlab_oop/specifying-methods-and-functions.html

###### 3. IO操作
1. 读取XML文件

创建用于将 XML 文件中的数据解析到包含字段 Name、Attributes、Data和Children的结构体数组的函数：
```
function theStruct = parseXML(filename)
% PARSEXML Convert XML file to a MATLAB structure.
try
   tree = xmlread(filename);
catch
   error('Failed to read XML file %s.',filename);
end

% Recurse over child nodes. This could run into problems 
% with very deeply nested trees.
try
   theStruct = parseChildNodes(tree);
catch
   error('Unable to parse XML file %s.',filename);
end


% ----- Local function PARSECHILDNODES -----
function children = parseChildNodes(theNode)
% Recurse over node children.
children = [];
if theNode.hasChildNodes
   childNodes = theNode.getChildNodes;
   numChildNodes = childNodes.getLength;
   allocCell = cell(1, numChildNodes);

   children = struct(             ...
      'Name', allocCell, 'Attributes', allocCell,    ...
      'Data', allocCell, 'Children', allocCell);

    for count = 1:numChildNodes
        theChild = childNodes.item(count-1);
        children(count) = makeStructFromNode(theChild);
    end
end

% ----- Local function MAKESTRUCTFROMNODE -----
function nodeStruct = makeStructFromNode(theNode)
% Create structure of node info.

nodeStruct = struct(                        ...
   'Name', char(theNode.getNodeName),       ...
   'Attributes', parseAttributes(theNode),  ...
   'Data', '',                              ...
   'Children', parseChildNodes(theNode));

if any(strcmp(methods(theNode), 'getData'))
   nodeStruct.Data = char(theNode.getData); 
else
   nodeStruct.Data = '';
end
```
> references
1. [【官方文档】读取XML文档并返回DOM节点](https://cn.mathworks.com/help/matlab/ref/xmlread.html)
2. [【官方文档】导入 XML 文档](https://cn.mathworks.com/help/matlab/import_export/importing-xml-documents.html)
3. [【官方文档】将工作区变量保存到文件中](https://cn.mathworks.com/help/matlab/ref/save.html)
4. [Matlab命令系列之XML读写：xmlread，xmlwrite](http://www.voidcn.com/article/p-eulwtwig-mq.html)

2. 读取文件夹下所有文件
```matlab
% read all filename in dir
img_path = './data/image/';
anno_path = './data/';

dirs = dir([img_path,'*.jpg']);
dircell = struct2cell(dirs)';
imgnames = dircell(:,1);
filename, annoname = cell(size(imgnames));

% get image names & xml file names
for i = 1:size(imgnames)
    file_name = char(imgnames(i));
    k = find('.'== file_name);
    filename{i} = file_name(1:k-1);%remove suffix
    annoname{i} = [filename{i},'.xml'];%add suffix
end
```
> references
1. [用matlab怎样按顺序读取一个文件夹里所有的.dat文件](http://blog.sina.com.cn/s/blog_a3b1929c01012qkf.html)
2. [matlab中读取某个文件夹下所有数据文件](http://blog.sciencenet.cn/blog-350278-702618.html)
3. [matlab 提取文件路径名称 带后缀与不带后缀](http://blog.csdn.net/uncle_ll/article/details/65632505)
4. [MATLAB: 读取同一目录下的所有文件名并按时间排序](http://www.voidcn.com/article/p-kesbnuwm-tr.html)
5. [Matlab如何循环读取文件](http://www.cnblogs.com/woshitianma/p/3724922.html)
6. [matlab拼接字符串的方法](http://blog.csdn.net/jirryzhang/article/details/71543683)

----------------------------

## <span id="03">03 Python </span>
#### <span id="03-1">3-1 Python爬虫</span>
###### 1.案例来源
1. [ 快来围观2W+的豆瓣电影分类排行榜（含代码）](https://mp.weixin.qq.com/s?__biz=MzIxNjA2ODUzNg==&mid=2651435876&idx=1&sn=8014f694c1c2709bb48cdf398aba9320&chksm=8c73abb3bb0422a512b08c118d05f83657a364f15f918d7eb1f0c14d36a64402d7d858b8f86a&scene=21#wechat_redirect)
2. [ 使用Python爬取网页图片 ](https://mp.weixin.qq.com/s?__biz=MzIxNjA2ODUzNg==&mid=403577828&idx=1&sn=5f5d97d5d3813a0ec3cced2a9ee18e10&scene=21#wechat_redirect)
3. [ 使用Python实现豆瓣阅读书籍信息的获取 ](https://mp.weixin.qq.com/s?__biz=MzIxNjA2ODUzNg==&mid=2651435242&idx=1&sn=f9315b81911bbc4f83f41ddba23d054e&chksm=8c73a83dbb04212b429f951a0bb12dc9dbd1057367e8edd279fa9ffc6f0dc8323a4a0049bffe&scene=21#wechat_redirect)
###### 2. 遇到的问题

1. 相关依赖包的安装
```shell
pip install requests
pip install bs4
pip install pandas
```
2. 多次爬取数据之后被封禁IP
```
解决方法：
1. 在每次爬取数据中间加上time.sleep(3)休眠一段时间，防止被发现访问异常
2. 采用代理池，轮换使用里面的代理IP
3. 对于类似 
    'Tunnel connection failed: 400 Bad Request'
    或者 
    'TimeoutError: [WinError 10060]由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。'
    一般是代理出现问题
```
3. 已经获取url的情况下下载图片

```python
from urllib import request
request.urlretrieve(url, path)#从url下载图片
```
4. 带有中文字符的文档`read()`函数报错

```python
with open('test.txt','r', encoding='utf-8') as file:
    content = file.read()
#python3中encode参数在open函数中
```

> 参考资料
> 1. [Python分析基础](https://mp.weixin.qq.com/mp/homepage?__biz=MzIxNjA2ODUzNg==&hid=3&sn=15a92c663ec584c3dc486308ce36a9bb&scene=18#wechat_redirect)
> 2. [Beautiful Soup 4.2.0 文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)
> 3. [PYTHON爬虫学习笔记——防豆瓣反爬虫](http://www.cnblogs.com/rockwall/p/5129670.html)
> 4. [为何大量网站不能抓取?爬虫突破封禁的6种常见方法](http://www.cnblogs.com/junrong624/p/5533655.html)
> 5. [Python获取免费的可用代理](http://blog.csdn.net/tobacco5648/article/details/50639288)
> 6. [python3 中自带urllib库可下载图片到本地 ](http://www.cnblogs.com/xjianhao/p/5810189.html)
> 7. [5.4 读写字节数据](http://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p04_read_write_binary_data.html)
> 8. [pandas: powerful Python data analysis toolkit](http://pandas.pydata.org/pandas-docs/stable/index.html)

----------------------------

## <span id="04">04 Deep Learning </span>

#### <span id="04-1">4-1 CNN </span>

###### 1. 基本结构

1. 卷积层
2. 池化层
3. 全连接层

###### 2. 经典网络

1. LeNet
2. AlexNet
3. VGG
4. GoogLeNet
5. ResNet

###### 3. 图像处理

1. Classification
2. Object Detection/Localization
3. Semantic/Instance Segmentation
- N-cut
- Grab cut
- CNN
- FCN

###### 4. 其他

1. SVM(支持向量机)
2. AP算法(吸引子传播算法)
3. kNN(k最近邻算法)
4. k-means
5. 梯度下降
6. 1x1卷积

#### <span id="04-2">4-2 RNN </span>
###### 1. RNN
    1. 在看完每一张图片之后，模型会输出一个标签，也会更新关于这个世界的知识。
    2. 在被给定一张新图片的时候，模型应该结合已经收集到的知识来做出更好的工作。


![image](http://i.imgur.com/ifQrKRR.png)

###### 2. LSTM
    1. 添加一个遗忘机制（forgetting mechanism）：当新的输入到来时，它需要知道记住哪些信念，以及丢弃哪些信念。
    2. 添加一个保存机制（saving mechanism）：当模型看到一副新的图片时，它需要学习关于这张图片的信息是否值得使用和保存。
    3. 所以当新的输入来临时，模型首先要忘掉任何它认为不再需要的长期记忆信息。然后学习新输入的哪些部分是值得利用的，并将它们保存在自己的长期记忆中。
    4. 将长期记忆聚焦在工作记忆中：最后，模型需要学习长期记忆中的哪些部分是即刻有用的。


![image](http://i.imgur.com/vsqgLYn.png)

> reference links

1. [YJango的循环神经网络——介绍](https://zhuanlan.zhihu.com/p/24720659)
2. [YJango的循环神经网络——LSTM](https://zhuanlan.zhihu.com/p/25518711)
3. [LSTM入门必读：从基础知识到工作方式详解](https://mp.weixin.qq.com/s/w6gUe-OmotALJR5LAhcBzA?client=tim&ADUIN=2104158177&ADSESSION=1511597282&ADTAG=CLIENT.QQ.5537_.0&ADPUBNO=26752) 对应原文：[Exploring LSTMs](http://blog.echen.me/2017/05/30/exploring-lstms/)
4. [LSTM-paper:LONG SHORT-TERM MEMORY](http://www.bioinf.jku.at/publications/older/2604.pdf)
5. [RNN-paper:Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling](https://arxiv.org/abs/1412.3555)
6. [图解--understanding LSTM networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
7. [blog--The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
#### <span id="04-3">4-3 others </span>

###### 1. 前沿

> reference
1. [My DL papers of the year](https://kloudstrifeblog.wordpress.com/2017/12/15/my-papers-of-the-year/) 对应译文 [2017年深度学习必读31篇论文](https://mp.weixin.qq.com/s?__biz=MzI1MjQ2OTQ3Ng==&mid=2247487211&idx=1&sn=24eef24570f207c770ce07d18b03fa3b&chksm=e9e20760de958e765040e274b2cc02e8c7b36c6f273a991ad7e90ab52f301327ab80a9188c0e&mpshare=1&scene=23&srcid=1219xbDZ3BvTx6aEIj1HZGB1#rd)
2. [2017年问题与预测](https://lukeoakdenrayner.wordpress.com/2017/12/27/2017-in-review-progress-problems-and-predictions/)
3. [2017计算机视觉进展盘点][h1] 对应原文 [A Year in CV][h1-1]
4. [计算机视觉简介：历史、现状和发展趋势][h2]
5. **++[Arxiv Sanity Preserver][h3]++**
6. [在Caffe中加Python Layer的方法][h4]
7. [爆款论文提出简单循环单元SRU：像CNN一样快速训练RNN（附开源代码）][h5]
8. [最全的DNN概述论文：详解前馈、卷积和循环神经网络技术][h6]
9. **++[机器学习资源][h7]++**

###### 2. 训练集、验证集与测试集

> references
1. [神经网络训练中的训练集、验证集以及测试集合](http://blog.csdn.net/jdbc/article/details/49965543)
2. [训练集(train set) 验证集(validation set) 测试集(test set)](http://blog.csdn.net/michaelliang12/article/details/51356792)
3. [机器学习中的训练集，验证集及测试集的关系](http://blog.csdn.net/losteng/article/details/50766252)

###### 3. Andrew Ng Deeplearning.ai

1. [Installing Jupyter](http://jupyter.org/install.html)
2. [deeplearning.ai编程作业](https://github.com/XingxingHuang/deeplearning.ai)
3. [numpy](https://docs.scipy.org/doc/numpy)常用函数

    - [numpy.linspace](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.linspace.html)
    - [numpy.random.randn](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.randn.html)

4. [matplotlib](https://matplotlib.org/devdocs/api/pyplot_summary.html)常用函数

    - [colormaps-reference](https://matplotlib.org/examples/color/colormaps_reference.html)
    - [matplotlib.pyplot.scatter](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.scatter.html)
    
###### 4. 人脸识别facial keypoint detection（备查）

1. [【CVPR2016论文快讯】面部特征点定位的最新进展][fkd-1]
2. [面部特征点定位概述及最近研究进展][fkd-2]
3. [人脸识别简史与近期进展][fkd-3]
4. [【发展史】基于深度学习的人脸识别技术综述][fkd-4]
5. [【混沌巡洋舰】用深度学习进行人脸识别][fkd-5]
6. [【发展现状】人脸检测与深度学习][fkd-6]
7. [kaggle-Facial Keypoints Detection][fkd-7]

> reference codes

1. [github-python:Facial-Keypoint-Detection](https://github.com/saber1988/facial-keypoints-detection)
2. [github-cpp11:CMU-Perceptual-Computing-Lab/openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
3. [github-kaggle:kfkd-tutorial](https://github.com/dnouri/kfkd-tutorial)
4. [blog-tensorflow:Detecting facial keypoints with TensorFlow](https://navoshta.com/facial-with-tensorflow/)
5. [blog-python:Using convolutional neural nets to detect facial keypoints tutorial](http://danielnouri.org/notes/2014/12/17/using-convolutional-neural-nets-to-detect-facial-keypoints-tutorial/)

###### 5. **Oxford University--Keypoint Detection**

1. [Keypoint Detection主页][ox1]
2. [matlab code实现][ox2]
3. [trained model][ox3]
4. [matconvnet框架][ox4]

> dataset

1. [西安交大-交通场景数据集][dataset1]
2. [MS COCO keypoint Dataset][dataset2]
3. [MPII Human Pose Dataset][dataset3] --> [MPII Human Pose Models][dataset3-1]
4. [PASCAL VOC 2012][dataset4]
5. [MS COCO][dataset5]

###### 6. 3D重建

1. [知乎-深度学习在3D重建上的应用][3d1]
2. [CVPR2017精彩论文解读：直接处理三维点云的深度学习模型][3d2]

###### 7. Semantic Segmentation History

index   | name  | paper | time  | score 
---     |---    |---    |---    |---
1 | FCN | [Fully Convolutional Networks for Semantic Segmentation][fcnpaper1] | 2014.11.14 | 62.2
2 | segNet | [SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation][fcnpaper2] | 2015.11.2 | 59.9
3 | 空洞卷积(Dilated Convolutions) | [Multi-Scale Context Aggregation by Dilated Convolutions][fcnpaper3] | 2015.11.23 | 71.3/75.3(CRF-RNN)
4 | DeepLab (v1和v2) | [Semantic Image Segmentation with Deep Convolutional Nets and Fully Connected CRFs(v1)][fcnpaper4-1]; [DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs(v2)][fcnpaper4-2] | 2014.12.22(v1);2016.6.2(v2) | 79.7
5 | RefineNet | [RefineNet: Multi-Path Refinement Networks for High-Resolution Semantic Segmentation][fcnpaper5] | 2016.11.20 | 84.2
6 | PSPNet | [Pyramid Scene Parsing Network][fcnpaper6] | 2016.12.4 | 82.6(paper)/85.4(rank)
7 | 大内核(Large Kernel Matters) | [Large Kernel Matters — Improve Semantic Segmentation by Global Convolutional Network][fcnpaper7] | 2017.3.8 | 82.2(paper)/83.6(rank)
8 | DeepLab v3 | [Rethinking Atrous Convolution for Semantic Image Segmentation][fcnpaper8] | 2017.6.17 | 85.7

###### 8. 基于深度学习进行场景布局分析 </span>

1. FCN + CRF（DeLay中抛弃的一种思路）

- FCN语义分割网络：在语义分割的FCN网络的基础上加以改造，训练出来的网络可以生成pixel级的分割结果，对于每个像素都指定是属于{left,front,right,ceiling,ground}中哪一个
```
输入：(w*h*3) RGB input image
输出：(w*h*5) belief map, label∈{left,front,right,ceiling,ground}
```
- CRF指定边界为直线：在FCN分割得到的结果墙体边界是锯齿形的，不规则。因此使用CRF进行限制输出结果为直线。
- 出现的问题：因为场景中杂物的干扰，得到的结果并不理想，常会沿着杂物边缘分割。
- 评价：实现最为简单，但是效果最差。

2. DeLay：FCN + 灭点建模 + 迭代优化

- FCN语义分割网络
```
输入：(w*h*3) RGB input image
输出：(w*h*5) belief map, label∈{left,front,right,ceiling,ground}
```
- logisitic regression：使用logisitic回归生成初步的(l1, l2, l3, l4)
```
预处理：只对front进行修剪，在标为front pixel的中间出现的holes使用knn算法分类
回归：检测相邻墙体的边界(wall/ceiling/ground boundaries)，看做二分类问题，得到初步的(l1, l2, l3, l4)
```
- optimization：迭代优化
```
评价指标S：用来判断优化得分，作用类似于损失函数
候选灭点采样：使用grid search暴力搜索优化灭点v，得到最优estimation (v, l1, l2, l3, l4)
候选线采样：在初步的(l1, l2, l3, l4)附近进行候选线采样，逐个取代原有(l1, l2, l3, l4)进行评估，得到最优estimation 
```
- 出现的问题：迭代优化耗费时间太长；先优化灭点后优化边界线，但是得到的灭点可能不是最优的？
- 评价：实现有些复杂（最初候选线的生成不是很清楚具体过程），准确性比较高，速度比较慢。
- 其他想法：是否可以使用别的FCN语义分割网络，比如最新的Mask R-CNN？

3. RoomNet：end-to-end
- 关键点keypoint（即墙角）评估：使用NN学习特征，直接输出keypoint位置
- 场景种类（room type）判别：YOLO、SSD判断属于哪种type的room（分为10类，对应不同的关键点数量和分布）
- keypoint refinement：加入类似RNN和LSTM的卷积层，进行关键点位置优化
- 评价：准确性和速度都是state-of-the-art，但是没有开放源码，实现起来需要自己搭建神经网络，最为复杂。

###### 9. DL的神经病应用 

1. [手写字体生成][dla1]
2. [生成宋词][dla2]
3. [生成诗歌][dla3]
4. [生成音乐][dla4]
5. [图片画风转换][dla5]
6. [震惊体标题][dla6]
7. [js画风转换][dla7]

###### 10. 博客资源 

> 国外人工智能博客

1. [斯坦福大学AI实验室](http://ai.stanford.edu/)
2. [AI weekly](http://aiweekly.co/)
4. [Machine Learning](http://subscribe.machinelearnings.co/)
5. [Chris Olah的博客](http://colah.github.io)
7. [Andrei Karpathy的博客](http://karpathy.github.io)
8. [牛津大学博士Trask的博客](http://iamtrask.github.io/)
9. [@hardmaru的博客](http://blog.otoro.net/)
11. [讲Keras框架深度学习的博客](http://blog.keras.io)
12. [Top Bots博客](http://www.topbots.com/)
13. [Denny Britz的技术博客](http://www.wildml.com/)
14. [Distill期刊博客](http://distill.pub/)
15. [FastML博客](http://fastml.com/)
16. [Jason Brownlee博士的博客](https://joanna-bryson.blogspot.de/)
17. [Sebastian Ruder博士的博客](http://sebastianruder.com/)
18. [Robbie Allen博士的博客](http://unsupervisedmethods.com/)
19. [Explosion AI工作室博客](https://explosion.ai/blog/)
20. [Tim Dettwers硕士博客](http://timdettmers.com/)
21. [Shawn Tan教授的博客](http://blog.wtf.sg/)
22. [加州大学学生运营的博客](https://ml.berkeley.edu/blog/)

[h1]: https://mp.weixin.qq.com/s/r-tl6ooNcQ_j4OFzV-5f3w "2017CV zh-cn"
[h1-1]: http://www.themtank.org/a-year-in-computer-vision "2017 CV"
[h2]: https://mp.weixin.qq.com/s?__biz=MzI4OTk2MTgwNg==&mid=2247483665&idx=1&sn=85e20c91ad8558162310222c45871fc1&chksm=ec266330db51ea265fbc282cc3fd0b5c20a12a60804fad0cb0ef51b0cd972d1546d82756cd72&mpshare=1&scene=23&srcid=1127L0l7uQx665LjOpFAvcpI#rd "cv history"
[h3]: http://www.arxiv-sanity.com/ "arxiv search"
[h4]: http://www.jianshu.com/p/e05d1b210fcb?utm_campaign=hugo&utm_medium=reader_share&utm_content=note&utm_source=weibo "caffe python layer"
[h5]: https://mp.weixin.qq.com/s?__biz=MzI4MDMwMDM3NA==&mid=2247484904&idx=2&sn=b4198d8cc5b61d6fa691a7978c4f262f&chksm=ebbbdbd1dccc52c704e97dc9ab6dee34004a45f76064efef7ca9f7ed020b96c29757103cbc1a&mpshare=1&scene=23&srcid=1129YLdJMVfY3LYzxDnkVpmd#rd "SRU"
[h6]: https://mp.weixin.qq.com/s?__biz=MzI4MDMwMDM3NA==&mid=2247484920&idx=2&sn=cd9c81b379adc07f390588641b0b4104&chksm=ebbbdbc1dccc52d72b3df54a21d25b72a16039bba2be387f94288f5062fd2f55f2ff2197b3a3&mpshare=1&scene=23&srcid=1129lYeCWC7Had39sLzRiPrZ#rd "DNN general"
[h7]: https://github.com/allmachinelearning/MachineLearning "machine learning resource"

[fcnpaper1]: https://arxiv.org/abs/1411.4038
[fcnpaper2]: https://arxiv.org/abs/1511.00561
[fcnpaper3]: https://arxiv.org/abs/1511.07122
[fcnpaper4-1]: https://arxiv.org/abs/1412.7062
[fcnpaper4-2]: https://arxiv.org/abs/1606.00915
[fcnpaper5]: https://arxiv.org/abs/1611.06612
[fcnpaper6]: https://arxiv.org/abs/1612.01105
[fcnpaper7]: https://arxiv.org/abs/1703.02719
[fcnpaper8]: https://arxiv.org/abs/1706.05587

[caps1]: https://hackernoon.com/capsule-networks-are-shaking-up-ai-heres-how-to-use-them-c233a0971952
[caps1-1]: https://mp.weixin.qq.com/s?__biz=MjM5MTQzNzU2NA==&mid=2651654965&idx=1&sn=e9104cf55069b2be1125d97681d2d3d7&chksm=bd4c2ca68a3ba5b04bafcc05198830ac72dce2c2ca5b097aa32363bed5efbfa48fdf88b0cced&mpshare=1&scene=23&srcid=1129oAYGQaCUkJWhuYyrcPec#rd
[caps2]: https://medium.com/botsupply/running-capsulenet-on-tensorflow-1099f5c67189
[caps3]: https://www.zhihu.com/question/67287444/answer/251460831
[caps4]: https://mp.weixin.qq.com/s?__biz=MzU2OTA0NzE2NA==&mid=2247483930&idx=1&sn=dc16a74e95bc401069b2814fb088f928&chksm=fc85e309cbf26a1f17ce0b2f04c4593fcf9ca3edd548d49cc508211a1c8986fcce74f4197753&scene=21#wechat_redirect
[caps4-1]: https://zhuanlan.zhihu.com/p/29435406
[caps5]: https://mp.weixin.qq.com/s?__biz=MzU2OTA0NzE2NA==&mid=2247485725&idx=1&sn=8bab696bdc3eb24b13ac1595ee35503d&chksm=fc85e80ecbf261183d85ee0388e1cc4969ddd19903b90f888ca52c7291c82bd08cff1b122cd0&mpshare=1&scene=23&srcid=1129KH9YK8r4Di72Z4whfkHF#rd
[caps6]: https://mp.weixin.qq.com/s?__biz=MzU2OTA0NzE2NA==&mid=2247484773&idx=2&sn=7b4096599740bea6c2bf079c894e6eee&chksm=fc85e476cbf26d6053605691b87f874e1833570006dab0b2e3d1264967031114745d80988d72&mpshare=1&scene=23&srcid=1129sUf65DzkzQkf5HUJnfxU#rd
[caps7]: https://mp.weixin.qq.com/s?__biz=MzA3NTIyODUzNA==&mid=2649538605&idx=1&sn=5e210d6dd4cea5923a941bae8b3cd560&chksm=876bd434b01c5d2258a478cfd83e3b6357c6c4ae26bbfc64ab73197f6044a68cba8d8aa77964&mpshare=1&scene=23&srcid=1129UjWtHAc4nSO5FYoCGdJE#rd 
[caps8]: https://medium.com/ai%C2%B3-theory-practice-business/understanding-hintons-capsule-networks-part-i-intuition-b4b559d1159b "understanding capsule network"

[fkd-1]: https://zhuanlan.zhihu.com/p/21955390 
[fkd-2]: https://zhuanlan.zhihu.com/p/21456877
[fkd-3]: https://zhuanlan.zhihu.com/p/21465605
[fkd-4]: https://zhuanlan.zhihu.com/p/24816781
[fkd-5]: https://zhuanlan.zhihu.com/p/30620870
[fkd-6]: https://zhuanlan.zhihu.com/p/25335957
[fkd-7]: https://www.kaggle.com/c/facial-keypoints-detection

[ox1]: http://www.robots.ox.ac.uk/~vgg/software/keypoint_detection/ "oxford keypoint detection"
[ox2]: https://github.com/ox-vgg/keypoint_detection "keypoint detection"
[ox3]: https://github.com/ox-vgg/keypoint_models "keypoint models"
[ox4]: http://www.vlfeat.org/matconvnet/ "matconvnet"

[dataset1]: http://trafficdata.xjtu.edu.cn/index.do "xjtu traffic data"
[dataset2]: http://cocodataset.org/#keypoints-challenge2017 "MS coco keypoint 2017"
[dataset3]: http://human-pose.mpi-inf.mpg.de/ "human pose MPII"
[dataset3-1]: http://pose.mpi-inf.mpg.de/ "pose MPII"
[dataset4]: http://host.robots.ox.ac.uk/pascal/VOC/voc2012/ "PASCAL VOC"
[dataset5]: http://cocodataset.org/#home "MS COCO"

[3d1]: https://zhuanlan.zhihu.com/p/30445504  "zhihu-3d-reconstruction"
[3d2]: https://www.leiphone.com/news/201708/ehaRP2W7JpF1jG0P.html?viewType=weixin "PointNet:Deep Learning on Point Sets for 3D Classification and Segmentation"

[dla1]: http://www.cs.toronto.edu/~graves/handwriting.html
[dla2]: http://seeleit.com/songci
[dla3]: http://freecoder.me/archives/213.html
[dla4]: http://www.cnblogs.com/charlotte77/p/5664523.html
[dla5]: https://github.com/fzliu/style-transfer
[dla6]: https://larseidnes.com/2015/10/13/auto-generating-clickbait-with-recurrent-neural-networks/
[dla7]: https://github.com/reiinakano/fast-style-transfer-deeplearnjs

[mm1]: http://www.jianshu.com/p/b477168c8105 "Xmind usage"
[mm2]: https://www.xmind.cn/ "Xmind"
----------------------------

## <span id="05">05 Paper </span>
#### <span id="05-1">5-1 Faster R-CNN</span>
###### 1. 提出背景

1. 之前提出的Fast R-CNN和SPPnet中已经减少了检测网络的运行时间代价，当前制约实现实施目标检测的瓶颈已经是区域建议这一步骤。针对这一点提出了RPN(Region Proposal Network)。
2. Region proposal methods:SS(Selective Search)和EdgeBoxes。其中SS是在faster R-CNN提出的时候最流行的区域建议方法，基本原理是从低层次的超像素开始，比较相邻区域之间的相似度，然后不断合并区域。而当时新提出的EdgeBoxes算法的速度要比SS算法快一个数量级，主要思想是根据边缘轮廓进行划分。在R-CNN中使用的是SS算法。
3. 使用深度网络定位候选框的工作：overfeat方法使用fc层训练去预测单一物体的候选框定位，fc层再转入卷积层来检测多种类别物体；multi-Box方法是从最后一个fc层生成区域建议，这个网络同时预测多个box。
4. 共享卷积层计算的工作：overfeat方法将计算的卷积特征用于分类、定位和检测；SPPnet将卷积特征提取用于使区域目标检测更加高效。
5. R-CNN：SS生成区域建议+CNN对区域建议进行特征提取+SVM进行区域分类
6. SPPnet：解决固定图像尺寸输入，截取的区域未涵盖整个目标或者缩放带来图像的扭曲的问题。在FC层前将任意大小的图像池化成为固定尺寸的图像。从而提高了特征提取的效率。
7. Fast R-CNN：依据SPP的思想，使用SS生成区域建议，将整张图像输入CNN进行特征提取，在fc层前加入RoI pooling层使每个区域建议生成固定尺寸的feature map，最后利用Softmax Loss(探测分类概率) 和Smooth L1 Loss(探测边框回归)对分类概率和边框回归(Bounding box regression)联合训练。


###### 2. 论文解读

1. 基本思想

- Faster R-CNN是由提供区域建议的RPN网络和提供目标检测的Fast R-CNN组成。其中RPN是一种FCN(全卷积网络)，和Fast R-CNN的检测网络共享卷积特征。两个网络交替进行训练。这样候选框的生成和目标检测都是在GPU上面运行的，速度得到了提升。
- RPN是end-to-end训练的，输出的是高质量的候选框，在每个位置同时预测目标位置和objectness得分。
- RPN的构造是在Fast R-CNN的卷积层的基础上添加两层，一层将每个卷积层映射位置编码为一个短的特征向量，另一层是在每个卷积层映射位置输出这个位置上多种尺度和长宽比的k个候选框的objectness得分和回归边界。
- RPN和fast R-CNN训练的时候是交替进行的。即保持候选框固定，交替微调RPN中的参数和目标检测网络的参数。

2. 主要步骤

- 输入测试图像；
- 将整张图片输入CNN，进行特征提取；
- 用RPN生成建议窗口(proposals)，每张图片生成300个建议窗口；
- 把建议窗口映射到CNN的最后一层卷积feature map上；
- 通过RoI pooling层使每个RoI生成固定尺寸的feature map；
- 利用Softmax Loss(探测分类概率) 和Smooth L1 Loss(探测边框回归)对分类概率和边框回归(Bounding box regression)联合训练.

###### 3. 相关概念

1. superpixel(超像素):在粗糙的Window级别的object detection和精细的pixel级的image segmentation之间的折中，将相近的像素分在一个不规则的小patch中.[11]
2. fps:每秒传输帧数，frame per second
3. PASCAL VOC:Pattern Analysis, Statical Modeling and Computational Learning.Pascal VOC Challenge —— 图像识别与物件分类的挑战.[9]
4. end-to-end(端对端):输入原始数据，输出期望结果。比如目标检测中是输入未处理的原图，输出候选框.[7]
5. IoU(Intersection over Union):交并比.[6]
6. objectness score:衡量候选区域中的物体是目标类或者背景的可能性
7. Semantic Segmentation:在一张图里分割聚类出不同物体的pixel，不关心是否是不同个体
8. Instance Segmentation:区分不同个体.[12]
9. mAP(mean average precision):二分类AP=precision-recall曲线下的面积，mAP是对所有类别AP求平均.[13]
10. SS(Selective Search)算法：假设现在图像上有n个预分割的区域,表示为R={R1, R2, ..., Rn}, 计算每个region与它相邻region(注意是相邻的区域)的相似度,这样会得到一个n*n的相似度矩阵(同一个区域之间和一个区域与不相邻区域之间的相似度可设为NaN),从矩阵中找出最大相似度值对应的两个区域,将这两个区域合二为一,这时候图像上还剩下n-1个区域; 重复上面的过程(只需要计算新的区域与它相邻区域的新相似度,其他的不用重复计算),重复一次,区域的总数目就少1,直到最后所有的区域都合并称为了同一个区域(即此过程进行了n-1次,区域总数目最后变成了1).[14]
11. EdgeBoxes算法：利用边缘信息（Edge），确定框框内的轮廓个数和与框框边缘重叠的轮廓个数，并基于此对框框进行评分，进一步根据得分的高低顺序确定proposal信息（由大小，长宽比，位置构成）.[5]
12. SPPnet解决的问题：固定图像尺寸输入，截取的区域未涵盖整个目标或者缩放带来图像的扭曲的问题.[4]

###### 4. 参考资料

> 相关参考

- [1] [深度学习之图像分割 《Fully Convolutional Networks for Semantic Segmentation》—FCN](http://blog.csdn.net/u010025211/article/details/51209504)
- [2] [RCNN学习笔记(8)：Fully Convolutional Networks for Semantic Segmentation(全卷积网络FCN）](http://blog.csdn.net/u011534057/article/details/51247388)
- [3] [目标检测——从RCNN到Faster RCNN 串烧](http://blog.csdn.net/xyy19920105/article/details/50817725)
- [4] [SPPNet](http://blog.csdn.net/cv_family_z/article/details/46832845)
- [5] [《Edge Boxes: Locating Object Proposals from Edges》读后感~](http://blog.csdn.net/wsj998689aa/article/details/39476551)
- [6] [目标识别（object detection）中的 IoU（Intersection over Union）](http://blog.csdn.net/lanchunhui/article/details/71190055)
- [7] [什么是 end-to-end 神经网络？](https://www.zhihu.com/question/51435499)
- [8] [计算机视觉识别简史：从 AlexNet、ResNet 到 Mask RCNN](http://www.dataguru.cn/article-11219-1.html)
- [9] [Pascal VOC Challenge —— 图像识别与物件分类的挑战](http://grunt1223.iteye.com/blog/970449)
- [10] [#Deep Learning回顾#之LeNet、AlexNet、GoogLeNet、VGG、ResNet](http://www.cnblogs.com/52machinelearning/p/5821591.html)
- [11] [Convolutional Networks for Image Semantic Segmentation](http://blog.csdn.net/yhl_leo/article/details/52857657)
- [12] [Instance Segmentation 比 Semantic Segmentation 难很多吗？](https://www.zhihu.com/question/51704852)
- [13] [图像中的mAP评价指标](http://blog.csdn.net/guojingjuan/article/details/51206256)
- [14] [目标检测--Selective Search for Object Recognition(IJCV, 2013)](http://www.cnblogs.com/zhao441354231/p/5941190.html)

> 论文解读

- [x] 0.1 [Faster R-CNN翻译](http://blog.csdn.net/liumaolincycle/article/details/48804687)
- [ ] 1. [实时的神经网络:Faster-RCNN技术分析](http://blog.csdn.net/luopingfeng/article/details/51245694)
- [ ] 2. [RCNN学习笔记(5)：faster rcnn](http://blog.csdn.net/u011534057/article/details/51247371)
- [ ] 3. [CNN目标检测与分割（一）：Faster RCNN详解](http://blog.csdn.net/zy1034092330/article/details/62044941)
- [x] 4. [faster-rcnn原理及相应概念解释](http://www.cnblogs.com/dudumiaomiao/p/6560841.html)
- [ ] 5. [Faster RCNN算法详解](http://m.blog.csdn.net/u014696921/article/details/53767153)

> 更多参考

1. [图像分类与KNN ](http://blog.csdn.net/han_xiaoyang/article/details/49949535) 
2. [目标检测--SSD（另一个有名的检测方法）](http://blog.csdn.net/smf0504/article/details/52745070)
3. [FCN译文 ](http://blog.csdn.net/scutjy2015/article/details/74500525?locationNum=2&fps=1)
4. [AlexNet译文](http://blog.csdn.net/LK274857347/article/details/53514364?locationNum=2&fps=1) 
5. [图像语义分割之FCN和CRF](https://zhuanlan.zhihu.com/p/22308032)
6. [十分钟看懂图像语义分割技术](https://mp.weixin.qq.com/s?__biz=MzA4ODgxMDY4MA==&mid=2655430607&idx=1&sn=fac0142ff44fac2d466350b922a707b1&mpshare=1&scene=23&srcid=1022SjllrZR9NdBe1GM77lsE#rd)
7. [斯坦福：「目标检测」深度学习全面指南](https://mp.weixin.qq.com/s?__biz=MzA5MzQwMDk4Mg==&mid=2651043558&idx=1&sn=0ed0c49628fc56d145bcc10d2b8d1a10&chksm=8ba96c1fbcdee5092719bb128b008319b93cd273d425c12fa119524195dd6f8a196633e33cef&mpshare=1&scene=23&srcid=1022ZtseAVMCHfNzIYe3Bn0n#rd)

> mask R-CNN相关

- [ ] 1. [目标检测分割--Mask R-CNN](http://blog.csdn.net/zhangjunhit/article/details/64920075?locationNum=6&fps=1)
- [ ] 2. [Mask R-CNN论文导读](http://blog.csdn.net/crazyice521/article/details/65448935)
- [ ] 3. [Mask R-CNN小结](http://blog.csdn.net/lancerlian/article/details/68936044)
- [ ] 4. [Mask RCNN 论文阅读](http://blog.csdn.net/Yan_Joy/article/details/66528502)

> 相关代码

1. [py-faster-rcnn](https://github.com/rbgirshick/py-faster-rcnn)
2. [matlab-faster-rcnn](https://github.com/ShaoqingRen/faster_rcnn)
3. [fast-rcnn](https://github.com/rbgirshick/fast-rcnn)

> 相关论文下载

1. [RCNN](http://fcv2011.ulsan.ac.kr/files/announcement/513/r-cnn-cvpr.pdf)
2. [SPP](https://arxiv.org/pdf/1406.4729.pdf) 
3. [Fast RCNN](https://arxiv.org/abs/1504.08083)
4. [Faster RCNN](https://arxiv.org/abs/1506.01497)
5. [Mask RCNN](https://arxiv.org/abs/1703.06870)
6. [Edge Boxes: Locating Object Proposals from Edges](https://www.microsoft.com/en-us/research/publication/edge-boxes-locating-object-proposals-from-edges/)

> 大神其人

1. [Ross Girshick (rbg)](http://www.rossgirshick.info/)
2. [Kaiming He 何恺明](http://kaiminghe.com/)
3. [Shaoqing Ren](http://www.shaoqingren.com/)
4. [Jian Sun](http://dblp.uni-trier.de/pers/hd/r/Ren:Shaoqing)

#### <span id="05-2">5-2 DeLay</span>
###### 1. 阅读材料

- [x] DeLay: Robust Spatial Layout Estimation for Cluttered Indoor Scenes

###### 2. 论文思路

> 场景布局分析：DeLay基本思路

1. 基于DeepLab的FCN网络：在语义分割的FCN网络的基础上加以改造，训练出来的网络可以生成pixel级的分割结果
```
输入：(w*h*3) RGB input image
输出：(w*h*5) belief map, label∈{left,front,right,ceiling,ground}
```
2. logisitic regression：使用logisitic回归生成初步的(l1, l2, l3, l4)
```
预处理：只对front进行修剪，在标为front pixel的中间出现的holes使用knn算法分类
回归：检测相邻墙体的边界(wall/ceiling/ground boundaries)，看做二分类问题，得到初步的(l1, l2, l3, l4)
```
3. optimization：迭代优化
```
评价指标S：用来判断优化得分，作用类似于损失函数
候选灭点采样：使用grid search暴力搜索优化灭点v，得到最优estimation (v, l1, l2, l3, l4)
候选线采样：在初步的(l1, l2, l3, l4)附近进行候选线采样，逐个取代原有(l1, l2, l3, l4)进行评估，得到最优estimation 
```

> 延伸：RoomNet

1. 这篇文章改进部分涉及到了RNN和LSTM，对这方面还不是很明白，但是大体思路还是比较清晰。
2. 思路：使用深度学习方法，直接学习几个keypoint的位置，实现end-to-end的室内布局分析。在实现的时候为了提高准确度，会先对场景进行分类（如上下左右后都有、只有左右墙等类型），然后再根据类型决定要学习几个keypoint。
3. 相对于DeLay，准确率有一定改进，但不是那种革命式的；但是处理速度改善相当大（200-600倍）。主要问题是没有公开源码，所以实现起来会有一定困难。

###### 3. 参考资料（备查）

> reference articles

1. [董卓瑶-deeplab](http://www.dongzhuoyao.com/deeplab-semantic-image-segmentation-with-deep-convolutional-nets-atrous-convolution-and-fully-connected-crfs/)[ ppt](http://vision.cs.utexas.edu/381V-fall2016/slides/kelle_paper.pdf)
2. [经典 CNNs 的 TensorFlow 实现资源汇总](http://www.jianshu.com/p/68cf89138dca)

> reference papers

1. [FCN](https://arxiv.org/pdf/1605.06211v1.pdf)
2. [RoomNet](https://arxiv.org/abs/1703.06241)
3. [DeepLab](https://arxiv.org/abs/1606.00915v1)
4. [The Manhattan World Assumption:Regularities in scene statistics which enable Bayesian inference ](http://papers.nips.cc/paper/1804-the-manhattan-world-assumption-regularities-in-scene-statistics-which-enable-bayesian-inference.pdf)

> reference codes

1. [tensorflow-FCN](https://github.com/shekkizh/FCN.tensorflow)
2. [tensorflow-deeplab-lfov](https://github.com/DrSleep/tensorflow-deeplab-lfov)
3. [tensorflow-deeplab-resnet](https://github.com/DrSleep/tensorflow-deeplab-resnet)
4. [caffe-python-DeepLab-Context](https://github.com/TheLegendAli/DeepLab-Context)
5. [caffe-c++-deeplab](https://bitbucket.org/deeplab/deeplab-public)
6. [caffe-RoomNet](https://github.com/FengyangZhang/caffe_roomnet)

#### <span id="05-3">5-3 DeepLab</span>

- [x] DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs

> reference articles

1. [语义分割中的深度学习方法全解：从FCN、SegNet到各代DeepLab](https://zhuanlan.zhihu.com/p/27794982)
2. [【读书笔记】Rethinking Atrous Convolution for Semantic Image Segmentation](https://zhuanlan.zhihu.com/p/27470685)
3. [论文阅读理解 - (Deeplab-V3)Rethinking Atrous Convolution for Semantic Image Segmentation](http://blog.csdn.net/zziahgf/article/details/75314719)
4. [图像语义分割之FCN和CRF](http://blog.csdn.net/u012759136/article/details/52434826#t9)
5. [董卓瑶-deeplab](http://www.dongzhuoyao.com/deeplab-semantic-image-segmentation-with-deep-convolutional-nets-atrous-convolution-and-fully-connected-crfs/) ，对应 [ppt](http://vision.cs.utexas.edu/381V-fall2016/slides/kelle_paper.pdf)
6. [author blog(with source code)](http://liangchiehchen.com/projects/DeepLab.html)

> reference codes

1. [tensorflow-FCN](https://github.com/shekkizh/FCN.tensorflow)
2. [tensorflow-deeplab-lfov](https://github.com/DrSleep/tensorflow-deeplab-lfov)
3. [tensorflow-deeplab-resnet](https://github.com/DrSleep/tensorflow-deeplab-resnet)
4. [caffe-python-DeepLab-Context](https://github.com/TheLegendAli/DeepLab-Context)
5. offical implement: [caffe-c++-deeplab-v1](https://bitbucket.org/deeplab/deeplab-public) |  [caffe-c++-deeplab-v2](https://bitbucket.org/aquariusjay/deeplab-public-ver2)
6. [Train DeepLab for Semantic Image Segmentation](https://github.com/martinkersner/train-DeepLab)


#### <span id="05-4">5-4 其他论文</span>

- [x] 1.Emergence of multimodal action representations from neural network self-organization
- [x] 2.Emotion-modulated attention improves expression recognition: A deep learning model
```
1.
这篇是对人的动作识别。
输入是含有声音的视频，
输出是识别人的动作是跑、跳、走等10类中的哪一种（one-hot）。
思路灵感来源：人的知觉感受是由多种类型的感受器（视觉信息，听觉信息等等）共同调制而成。
通过半监督算法，之前的信息对之后的信息进行反馈（应该类似RNN）双向联系实现增量学习。
通过同时捕获动作特征（图像视觉角度）和从speech recognition得到的label，从而实现多类型信息处理。
缺点：在视觉和听觉信息中含有的噪音对于神经网络的低层会产生影响，由此产生的错误会从低层传播到高层。

2. 
这篇是对人的表情识别。
为了增加在复杂环境下识别的难度，采用的图片是把含有上半身的人脸照片贴到一个办公室背景里面。
识别的结果是人是带有情绪的表情（比如开心、生气），面无表情还是不含人脸照片。
思路灵感来源：人和动物在处理周围视觉信息的时候，会抑制无关信息只处理相关度高的刺激信息。
这个模型包括attention部分和CCCNN（跨频道CNN）部分。
attention模型部分和普通NN不同的是，输出的结果不是直接对表情的识别，而是该区域含有表情的概率。
概率最高的区域就是表情人脸所在的区域。（实际是object localization）
CCCNN部分是从人的面部特征和手势动作两个方面，对人脸区域和半身躯体区域分别提取特征。
最终综合两个方面得出人脸表情。（实际是classification）
个人感觉：这个模型有点奇怪，有种为了仿生而仿生的感觉。
```

- [x] 3. [Dynamic Routing Between Capsules](https://arxiv.org/pdf/1710.09829v1.pdf)

> releated papers
1. [MATRIX CAPSULES WITH EM ROUTING](https://openreview.net/pdf?id=HJWLfGWRb)
> reference codes
1. [CapsNet-Tensorflow](https://github.com/naturomics/CapsNet-Tensorflow)
2. [Capsule Networks-TensorFlow](https://github.com/bourdakos1/capsule-networks)
3. [CapsNet-Implementations-List](https://github.com/loretoparisi/CapsNet)
> reference articles
1. [Capsule Networks Are Shaking up AI—Here’s How to Use Them][caps1] -- 【对应译文】[欲取代CNN的Capsule Network究竟是什么来头？它能为AI界带来革命性转折么？][caps1-1]
2. [Running CapsuleNet on TensorFlow][caps2]
3. [【知乎】如何看待Hinton的论文《Dynamic Routing Between Capsules》？][caps3]
4. [【深度】浅析Geoffrey Hinton最近提出的Capsule计划][caps4]--> [知乎原文][caps4-1]
5. [【干货】Hinton最新 Capsule Networks 视频教程分享和PPT解读（附pdf下载）][caps5]
6. [【前沿】Geoffery Hinton 的 NIPS2017 Capsule论文简读][caps6]
7. [深度学习之父Hinton备受瞩目的Capsule论文今正式公布，神经网络的走向将就此改写？][caps7]
8. [Understanding Hinton’s Capsule Networks][caps8]
9. [漫谈capsule network基本原理][caps9]


[ox1]: http://www.robots.ox.ac.uk/~vgg/software/keypoint_detection/ "oxford keypoint detection"
[ox2]: https://github.com/ox-vgg/keypoint_detection "keypoint detection"
[ox3]: https://github.com/ox-vgg/keypoint_models "keypoint models"
[ox4]: http://www.vlfeat.org/matconvnet/ "matconvnet"

[dataset1]: http://trafficdata.xjtu.edu.cn/index.do "xjtu traffic data"
[dataset2]: http://cocodataset.org/#keypoints-challenge2017 "MS coco keypoint 2017"
[dataset3]: http://human-pose.mpi-inf.mpg.de/ "human pose MPII dataset"
[dataset3-1]: http://pose.mpi-inf.mpg.de/ "pose MPII model"

[caps1]: https://hackernoon.com/capsule-networks-are-shaking-up-ai-heres-how-to-use-them-c233a0971952
[caps1-1]: https://mp.weixin.qq.com/s?__biz=MjM5MTQzNzU2NA==&mid=2651654965&idx=1&sn=e9104cf55069b2be1125d97681d2d3d7&chksm=bd4c2ca68a3ba5b04bafcc05198830ac72dce2c2ca5b097aa32363bed5efbfa48fdf88b0cced&mpshare=1&scene=23&srcid=1129oAYGQaCUkJWhuYyrcPec#rd
[caps2]: https://medium.com/botsupply/running-capsulenet-on-tensorflow-1099f5c67189
[caps3]: https://www.zhihu.com/question/67287444/answer/251460831
[caps4]: https://mp.weixin.qq.com/s?__biz=MzU2OTA0NzE2NA==&mid=2247483930&idx=1&sn=dc16a74e95bc401069b2814fb088f928&chksm=fc85e309cbf26a1f17ce0b2f04c4593fcf9ca3edd548d49cc508211a1c8986fcce74f4197753&scene=21#wechat_redirect
[caps4-1]: https://zhuanlan.zhihu.com/p/29435406
[caps5]: https://mp.weixin.qq.com/s?__biz=MzU2OTA0NzE2NA==&mid=2247485725&idx=1&sn=8bab696bdc3eb24b13ac1595ee35503d&chksm=fc85e80ecbf261183d85ee0388e1cc4969ddd19903b90f888ca52c7291c82bd08cff1b122cd0&mpshare=1&scene=23&srcid=1129KH9YK8r4Di72Z4whfkHF#rd
[caps6]: https://mp.weixin.qq.com/s?__biz=MzU2OTA0NzE2NA==&mid=2247484773&idx=2&sn=7b4096599740bea6c2bf079c894e6eee&chksm=fc85e476cbf26d6053605691b87f874e1833570006dab0b2e3d1264967031114745d80988d72&mpshare=1&scene=23&srcid=1129sUf65DzkzQkf5HUJnfxU#rd
[caps7]: https://mp.weixin.qq.com/s?__biz=MzA3NTIyODUzNA==&mid=2649538605&idx=1&sn=5e210d6dd4cea5923a941bae8b3cd560&chksm=876bd434b01c5d2258a478cfd83e3b6357c6c4ae26bbfc64ab73197f6044a68cba8d8aa77964&mpshare=1&scene=23&srcid=1129UjWtHAc4nSO5FYoCGdJE#rd 
[caps8]: https://medium.com/ai%C2%B3-theory-practice-business/understanding-hintons-capsule-networks-part-i-intuition-b4b559d1159b "understanding capsule network"
[caps9]: https://mp.weixin.qq.com/s?__biz=MzIzNDQyNjI5Mg==&mid=2247484777&idx=1&sn=a5ad7f1e5f8a70fd5ae152e51362d46d&chksm=e8f7dfb2df8056a4ae166a16b360ee1216d6cbd1f477af83cbdf364c86726cafcde8ebb5e9ac&mpshare=1&scene=23&srcid=1207vbkTD2wkoZ4eQ3xMwvYz#rd "漫谈Capsule Network基本原理"

- [x] 4.MultiNet

![image](http://outz1n6zr.bkt.clouddn.com/2017-11-23_185846.png)

> refernce
1. [MultiNet代码](https://github.com/MarvinTeichmann/KittiSeg)
2. [MultiNet论文](https://arxiv.org/abs/1612.07695)
3. [VGG论文](https://arxiv.org/abs/1409.1556)
4. [KITTI数据集](http://www.cvlibs.net/datasets/kitti/eval_object.php)

----------------------------

## <span id="06">06 Keypoint detection</span>

#### <span id="06-1">6-1 参考代码</span>

1. [Keypoint Detection主页][ox1]
2. [matlab code实现][ox2]
3. [trained model][ox3]
4. [matconvnet框架][ox4]

> dataset

1. [西安交大-交通场景数据集][dataset1]
2. [MS COCO keypoint Dataset][dataset2]
3. [MPII Human Pose Dataset][dataset3]
4. [KITTI](http://www.cvlibs.net/datasets/kitti/)
5. [人机所Road-Vehicle Dataset (RVD)](http://www.aiar.xjtu.edu.cn/xszy/RVD.htm)
6. [TuSimple自动驾驶算法比赛：车道线检测](https://dataquestion.com/competition/selfdriveaicomp_lane)

> others

1. [详述车道检测的艰难探索：从透视变换到深度图像分割(附代码)](https://zhuanlan.zhihu.com/p/26908375)

#### <span id="06-2">6-2 数据集格式</span>

###### 2.1  MPII Human Pose Dataset Annotation
```python
RELEASE
    |-.annolist(imgidx) #annotation list，其中imgidx是图片编号。[1×24987 struct]
    |   |-.image.name   #image文件名，如"010789143.jpg"
    |   |-.annorect(ridx) #body annotation，其中ridx是person序号（图中可能不止一个人）
    |   |       |-.x1, .y1, .x2, .y2 #person的head矩形框标注
    |   |       |-.scale #person身高相对于200px的比值
    |   |       |-.objpos #person中心点
    |   |       `-.annopoints.point #person关节点标注
    |   |              |-.x, .y #关节点坐标
    |   |              |-id #关节点id
    |   |              `-is_visible #关节点是否可见（被遮挡）
    |   |-.vidx #对应video的id
    |   `-.frame_sec #image在video中的帧对应时刻
    |-img_train(imgidx) #1代表作为训练集，0代表作为测试集。[1×24987 double]
    |-single_person(imgidx) #对应图片的ridx(rectangle id)列表。{24987×1 cell}
    |-act(imgidx) #对应id的image的activity/category label
    |   |-act_name #person正在进行的活动名，如 cat_name: 'winter activities'
    |   |-cat_name #图片对应分类名，如 act_name: 'skiing, downhill'
    |   `-act_id #活动id
    `-video_list(videoidx) #里面是video在YouTube上面的id。{1×2821 cell}
    #对应视频位置在 https://www.youtube.com/watch?v=video_list(videoidx) 上面可以观看。
```
###### 2.2 [validation dataset](https://cims.nyu.edu/~tompson/cs_portfolio.html)
```python
1. RELEASE_img_index #1*2958;对应index的imgid
2. RELEASE_person_index #1*2958;对应index的ridx
3. output_joints #1×14 cell array;14个关节点的名称：'rank','rkne','rhip','lhip','lkne','lank','neck','head'等
4. keypointsAll #1*2958 cell array;cell[14×2 double];对应index的所有关节点坐标
5. annolist(imgidx)
        `-.annorect
                |-.x1, .y1, .x2, .y2
                |-.scale
                |-.objpos
                `-annopoints.point
                        |-.x, .y
                        |-id
                        `-is_visible
```

###### 2.3 keypoint detection预处理之后的数据格式
```python
'''
3.0G	extractedData_256_256.mat
3.0G	MPI-baseline_imdb1.mat
2.7G	MPI_imdbsT1aug0.mat
310M	MPI_imdbsV1aug0.mat
733M	testMPI_256_256.mat
'''
# 1. extractedData_256_256.mat
1. bbox         #size = (1,28883); [1*4 double]
2. pad_train    #size = (1,28883); [1*4 double]
3. ptsAll       #size = (1,28883); [16*3 double]
4. pstRest      #size = (28883,12); [16*3 double]
5. sets_train   #size = (24987,1); logical 0/1
6. sets_train_idx #size = (28883,2); [imgidx, ridx]
7. img_final    #size = (1,28883); [256*256*3 uint8]

# 2. testMPI_256_256.mat
1. bbox     #size = (1,7247); [1*4 double]
2. pad_test #size = (1,7247); [1*4 double]
3. testMap  #size = (7247,2); [imgidx, ridx]
4. imgPath  #size = (1,7247); [256*256*3 uint8]
5. poseGT = []

# 3. MPI_imdbsT1aug0.mat
1. ptsAll   #size = (1,25925); [16*3 double]
2. imgPath  #size = (1,25925); [256*256*3 uint8]

# 4. MPI_imdbsV1aug0.mat
1. ptsAll   #size = (1,2598); [16*3 double]
2. imgPath  #size = (1,2598); [256*256*3 uint8]
3. tompson_val  #size = (2958*10); 
                #(1:2) = set_train_idx;
                #(3:6) = bbox;
                #(7:10) = pad_train;

# 5. MPI-baseline_imdb1.mat
1. patchHei = patchWi = 248
2. meta
    `-sets  #[1×3 cell array]; 'train','val','test'
3. averageImage = []
4. images
        |-data: {1×28883 cell}    #size = (1,28883); [256*256*3 unit8]
        |-labels: {1×28883 cell}  #size = (1,28883); [16*3 double]
        `-set: [1×28883 double]   #1/2
```
###### 2.4 初步设计的数据格式
```python
RELEASE
    |-.annolist(imgidx) #annotation list，其中imgidx是图片编号。
    |   |-.image.name   #image文件名，如"010789143.jpg"
    |   `-.annoroad(ridx) #road annotation
    |          |-.type #道路类型：城市道路、高速公路等或者直道、U型弯、S型弯、Z型弯、十字路口等？
    |          |-.scale #用于resize图片大小（是否有必要resize图片？）
    |          `-.annopoints.point #person关节点标注
    |                 |-.x, .y #控制点坐标
    |                 `-id #控制点id
    |-img_train(imgidx) #1代表作为训练集，0代表作为测试集。
    `-single_person(imgidx) #对应图片的ridx(road id)列表。一幅图可能存在多条道路。
```

#### <span id="06-3">6-3 调试</span>
###### 1. detection demo代码调试
```
$ cd ~/Documents
$ git clone https://github.com/ox-vgg/keypoint_detection.git
$ git clone https://github.com/ox-vgg/keypoint_models.git
$ ./matlab
> cd keypoint_detection
> run demo_detection.m #需要修改model和matconvnet的路径
```
###### 2. train model代码调试
```
# 1. download dataset
> run ./getMPIIData/getMPIIData-v3.m #数据集下载，其中dataset ~3G，validation ~0.3G
> run ./getMPIIData/splitMPIIData-V4.m #数据集分割
# 2. train model
> run trainBodyPose_example.m #使用dataset训练model
```
> reference
1. [数据集与标注等工具][label1]
2. [图像分割 | FCN数据集制作的全流程（图像标注）][label2]
3. [Matlab 多核 多个CPU 并行运算][speed1]
4. [Matlab利用cpu的多核提高运算速度][speed2]
5. [Matlab之GPU加速方法][speed3]
6. [Matlab多线程与多核运算， 以及GPU加速][speed4]

[label1]: http://blog.csdn.net/dlyldxwl/article/details/76272707 "数据集与标注等工具"
[label2]: http://blog.csdn.net/u010402786/article/details/72883421 "图像分割 | FCN数据集制作的全流程（图像标注）"
[speed1]: blog.csdn.net/zjxiaolu/article/details/44886173 "Matlab 多核 多个CPU 并行运算"
[speed2]: http://malagis.com/matlab-utilize-multicore-cpu-improve-processing-speed.html "Matlab利用cpu的多核提高运算速度"
[speed3]: blog.csdn.net/laoxuan2011/article/details/52473360# "Matlab之GPU加速方法"
[speed4]: blog.csdn.net/tianqizhenhaofly/article/details/51283758 "Matlab多线程与多核运算， 以及GPU加速"
###### 3. GPU问题
**解决方法**：切换到GPU节点

```matlab
$ ssh node8
> gpuDevice
resetting GPU

ans = 

  CUDADevice with properties:

                      Name: 'Tesla K80'
                     Index: 2
         ComputeCapability: '3.7'
            SupportsDouble: 1
             DriverVersion: 9
            ToolkitVersion: 8
        MaxThreadsPerBlock: 1024
          MaxShmemPerBlock: 49152
          ...
```
###### 4. 编译出错
```matlab
%错误报告

Error using vl_nnconv
An error occurred during PTX compilation of <image>.
The information log was:

The error log was:

The CUDA error code was: CUDA_ERROR_UNKNOWN.
Error in dagnn.Conv/forward (line 11)
      outputs{1} = vl_nnconv(...
Error in dagnn.Layer/forwardAdvanced (line 85)
      outputs = obj.forward(inputs, {net.params(par).value}) ;
Error in dagnn.DagNN/eval (line 91)
  obj.layers(l).block.forwardAdvanced(obj.layers(l)) ;
Error in cnn_train_dag_reg>processEpoch (line 259)
      net.eval(inputs, params.derOutputs, 'holdOn', s < params.numSubBatches) ;
Error in cnn_train_dag_reg (line 111)
    [net, state] = processEpoch(net, state, params, 'train') ;
Error in cnn_regressor_dag (line 120)
info = cnn_train_dag_reg(net, imdb, fn, opts.train) ;
Error in trainBodyPose_example (line 132)
cnn_regressor_dag(opts);
Error in run (line 86)
evalin('caller', [script ';']);
```
经过排查发现是matlab不支持gpuArray的运算，不清楚具体是matlab的问题还是服务器的问题。有一次程序正常运行了，但是之后服务器宕机一次，等连接恢复又不能运行了。
```matlab
%gpuArray bsxfun operation test code
R1 = rand(2,5,4,'gpuArray');
R2 = rand(2,1,4,3,'gpuArray');
R = bsxfun(@plus,R1,R2);
size(R)
```

[ox1]: http://www.robots.ox.ac.uk/~vgg/software/keypoint_detection/ "oxford keypoint detection"
[ox2]: https://github.com/ox-vgg/keypoint_detection "keypoint detection"
[ox3]: https://github.com/ox-vgg/keypoint_models "keypoint models"
[ox4]: http://www.vlfeat.org/matconvnet/ "matconvnet"

[dataset1]: http://trafficdata.xjtu.edu.cn/index.do "xjtu traffic data"
[dataset2]: http://cocodataset.org/#keypoints-challenge2017 "MS coco keypoint 2017"
[dataset3]: http://human-pose.mpi-inf.mpg.de/ "human pose MPII dataset"

----------------------------

## <span id="07">07 Others </span>

#### <span id="07-1">7-1 mindmap</span>

1. 工具：
    - 1. 电脑端应用：MindManager、Xmind、Graphviz(代码式)
    - 2. 在线网站：百度脑图、ProcessOn
2. 基本思想：树状结构
3. 常用组件

> reference

1. [【技能贴】XMind 思维导图的使用][mm1]
2. [Xmind官网][mm2]

#### <span id="07-2">7-2 markdown</span>

1. 工具：
    - 1. 电脑端应用：Typora、有道云笔记
    - 2. 在线网站：简书、GitHub
2. [基本语法](http://www.markdown.cn/)

3. 支持拓展--HTML & LaTeX

#### <span id="07-3">7-3 服务器</span>
###### 1. 曙光服务器使用

1. 登录
- 工具：Putty、XShell（推荐）、VNC（类似于Windows远程桌面，适用于使用图形化应用时）
- 登录方式：
    
    外网IP：115.154.137.65    用户名：--     密码：--

- VNC连接远程桌面
```
$vncserver  #启用VNCserver，首次启动需要设置密码，一个用户上限大概30个桌面上下
$vncpasswd  #修改密码
$vncserver -list  #查看当前启用桌面号
$vncserver -kill :<桌面号> #关闭指定桌面号远程桌面
```
```
学院服务器VNC图形界面使用
1. 使用Xftp进入VNC工具所在路径：/public/sourcecode/win_tools，拖拽到本地即可下载
2. 安装VNC的时候只需要安装viewer即可，不需要安装server
3. 使用xshell登录服务器之后命令行模式输入vncserver，会启动一个图形窗口进程，分配一个窗口号，自己设置密码即可
4. 本地启动VNC viewer，在VNC server栏输入115.154.137.65:<窗口号>
5. connect->continue->输入自己设置的密码->进入图形界面
6. 图形界面输入服务器账号密码，进入操作
7. 使用结束后最好在命令行输入vnc -kill :<桌面号>，否则进程会一直在，上限是15个左右桌面
8. 可以使用vncserver -list查看当前启动的桌面进程
```
2. 文件上传下载
- 工具：WinSCP、Xftp（推荐）
- 使用方式：图形界面，直接拖拽

3. 软件安装
- 曙光集群软件
```
1.1 编译器：GNU、intel 
1.2 数学库：mkl、fftw
1.3 MPI并行库：Intelmpi、Openmpi、mvapich
```
- 软件安装
```
2.1 rpm安装 
    $rpm -ivh <软件包名>
2.2 yum安装
    $yum install <软件包名> #自动安装依赖包
2.3 源码安装
```
4. 使用作业调度（基于PBS）
```
$pestat #查看节点状态
$qsub test.pbs  #提交作业
$qstat  #查看作业状态
$qdel 93.nodel  #删除作业
```

###### 2. GPU硬件
1. 服务器CPU
- 服务器CPU一般选用Intel Xeon（英特尔至强）系列的CPU，目前有E7/E5/E3系列，其中后缀`L=low power` `M=Mobile` `W=workstation`
- 家用电脑Intel CPU的型号Core i3<i5<i7

2. GPU显卡
- 主流显卡分为N卡（NVIDIA）和A卡（AMD）
- NVIDIA的显卡中，Tesla系列主要用于服务器，GeForce系列主要用于个人电脑，一般GTX 1080Ti>1080>1070>1060

3. 其他
- 机架式服务器结构中的1U-8U：U是服务器机箱的高度，1U等于4.45厘米。与需要购买的机柜高度等相关。
- 产品类别：机架式（入门级和工作组级）、塔式（单机性能比较有限，需要机柜）、刀片式（节省空间，散热突出）

> references

> 1. [【Intel官网】Intel Xeon(英特尔® 至强® 处理器 E5 家族)](https://www.intel.cn/content/www/cn/zh/products/processors/xeon/e5-processors.html)
> 2. [【Intel官网】CPU型号命名](https://www.intel.cn/content/www/cn/zh/processors/processor-numbers.html)
> 3. [CPU/GPU 天梯排行](http://itianti.sinaapp.com/index.php)
> 4. [塔式、机架式、刀片式服务器的区别和特点](http://blog.sina.com.cn/s/blog_4e0c21cc0102w9sy.html)
> 5. [【知乎】决定显卡性能的比较重要的几个参数是什么？](https://www.zhihu.com/question/27371880)

4. 相关链接：

- 销售服务器的官网

> 1. [AMAX](http://www.amaxchina.com/HardwareProducts/Filter/HighPerformanceComputingProducts/DevMAXServer)
> 2. [中科曙光](https://www.sugon.com/product/category/83.html)
> 3. [华硕 深度学习服务器](https://www.asus.com.cn/Commercial-Servers-Workstations/Commercial-Workstations-Products/)
> 4. [苏州科达科技](http://cn.kedacom.com/givenpro/4607.jhtml)

- 天猫京东相关销售网店

> 1. [天猫-E5双路/4路GPU 深度学习DIY定制4路GPU服务器](https://detail.tmall.com/item.htm?spm=a21m2.8958473.0.0.2bec311dDAYZ6D&id=560108309646&skuId=3497421572749)
> 2. [京东 戴尔T630 深度学习 塔式服务器主机 集成显卡](https://item.jd.com/10368467503.html)

- 云服务器服务

> 1. [google cloud图形处理器 (GPU) 测试版](https://cloud.google.com/gpu/)
> 2. [阿里云 GPU云服务器](https://www.aliyun.com/product/ecs/gpu?spm=5176.8142029.388261.404.3836dbccnPZiL0)
> 3. [AWS EC2 实例类型](https://amazonaws-china.com/cn/ec2/instance-types/)
> 4. [腾讯云 GPU云服务器](https://cloud.tencent.com/product/gpu)
> 5. [美团云 GPU云主机](https://www.mtyun.com/product/gpu)

- 知乎问答

> 1. [深度学习计算加速云服务横向对比](https://zhuanlan.zhihu.com/p/26766268)
> 2. [如何配置一台适用于深度学习的工作站？](https://www.zhihu.com/question/33996159)

- 服务器搭建

> 1. [从零开始搭建深度学习服务器](http://www.52nlp.cn/tag/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%9C%8D%E5%8A%A1%E5%99%A8)
> 2. [搭建深度学习服务器Ubuntu 16.04 LTS + GTX 1080Ti](http://www.jianshu.com/p/4e64cb45a5a4)


