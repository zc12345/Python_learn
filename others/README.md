# 一些Python练手

## 1. 常见的递归

## 2. matplotlib绘制心形图

## 3. python生成和识别二维码

### 3.1 依赖包
```
pip install qrcode
pip install image
pip install colorama
```

### 3.2 命令行执行
```
$ qr "hello world" > test.png
```
> references
> 1. [Python将文本生成二维码](https://www.cnblogs.com/babycool/p/4734819.html)
> 2. [python二维码生成库(qrcode)简介和实例](http://blog.csdn.net/henni_719/article/details/54580732)
> 3. [使用Python的库qrcode生成二维码](https://www.jianshu.com/p/b4b14e314b2a)
> 4. [有关python下二维码识别用法及识别率对比分析](https://www.cnblogs.com/zhongtang/p/7148375.html)
> 5. [用python写的opencv实时监测和解析二维码和条形码最牛教程](http://blog.csdn.net/qq_25491201/article/details/51065547)

## 4. 随机游走算法

### 4.1 算法简介
随机游走（英语：Random Walk，缩写为 RW），是一种数学统计模型，它是一连串的轨迹所组成，其中每一次都是随机的。它能用来表示不规则的变动形式，如同一个人酒后乱步，所形成的随机过程记录。1905年，由卡尔·皮尔逊首次提出。

随机游走(random walk)矩阵可以看做是马尔科夫链的一种特例。马尔可夫链（英语：Markov chain），又称离散时间马尔可夫链（discrete-time Markov chain，缩写为DTMC），为状态空间中经过从一个状态到另一个状态的转换的随机过程。该过程要求具备“无记忆”的性质：下一状态的概率分布只能由当前状态决定，在时间序列中它前面的事件均与之无关。这种特定类型的“无记忆性”称作马尔可夫性质。

通常，我们可以假设随机游走是以马尔可夫链或马可夫过程的形式出现，但是比较复杂的随机游走则不一定以这种形式出现。在某些限制条件下，会出现一些比较特殊的模式，如醉汉走路（drunkard's walk）或莱维飞行（Lévy flight）。

### 4.2 随机游走算法用于求全局最优解
梯度下降法可以求最优解在精度要求不高的情况下可以使用，但可能会陷入局部最优解。随机游走算法是一种比较简单的求全局最优解的方法。基本的随机游走算法对于初始点比较敏感，当初始点位于最优点附近时，可以很好地达到全局最优点；如果将初始点设置得离最优点较远，可能会陷入局部最优解，这时候可以通过增加初始步长扩大求解空间和通过增加迭代次数寻到最优解。步长λ越大，意味着初始可以寻找最优解的空间越大，但同时也意味着更多的迭代次数(要搜索空间变大，寻找次数变多，相应时间自然要增加)。如果步长取得过小，即使N很大，也很难达到最优解。无论对于随机游走算法还是改进的随机游走算法皆是如此。所以理论上步长λ越大越好。但是步长越大，迭代总次数越高，算法运行时间越长。

### 4.3 随机游走算法PersonalRank实现基于图的推荐

> references
> 1. [浅谈随机游走](http://blog.csdn.net/songzitea/article/details/18087401)
> 2. [基于随机游走的personalrank算法实现推荐](http://zhangxiong0301.iteye.com/blog/2249310)
> 3. [机器学习->推荐系统->基于图的推荐算法(PersonalRank)](http://blog.csdn.net/mr_tyting/article/details/65638435)
> 4. [介绍一个全局最优化的方法：随机游走算法(Random Walk)](http://www.cnblogs.com/lyrichu/p/7209529.html)
> 5. [比较PageRank算法和HITS算法的优缺点](http://blog.sina.com.cn/s/blog_72995dcc01013bkb.html)
> 6. [聚类 - 5 - 谱和谱聚类](http://blog.csdn.net/xueyingxue001/article/details/51966980)
