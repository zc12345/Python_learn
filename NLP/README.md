# 自然语言处理（NLP）作业

## 0. 相关

### 0.1 相关环境和库
1. 生成exe执行程序：pyinstaller
2. 程序运行环境：Windows 10系统，Python 3.5

### 0.2 使用pyinstaller对python程序打包
1. 如果是只需要GUI，不需要命令行界面弹出，在保存文件的时候应该是.pyw
2. 对python文件打包
```
$ pyinstaller -F path\\file.py/pyw # -F表示打包成单个exe文件
$ pyinstaller -F -w path\\file.py/pyw # -w表示不调用命令行窗口
$ pyinstaller -F path\\file.py/pyw --noconsole # 与-w一个效果
```

> references
> 1. [Python程序打包成exe可执行文件](http://blog.csdn.net/zengxiantao1994/article/details/76578421)
> 2. [pyinstaller打包后的exe运行怎么去掉弹出的dos窗口？](https://www.zhihu.com/question/22977098)


## 1. MED(Minimum Edit Distance)

### 1.1 作业要求
完成一个计算单词距离的系统（报告 + 源代码 + 执行程序）

### 1.2 动态规划求解MED

### 1.3 参考资料

> references
> 1. [stanford NLP学习笔记3：最小编辑距离（Minimum Edit Distance）](http://www.cnblogs.com/arkenstone/p/6196111.html)
> 2.[Tkinter GUI 教程系列](https://morvanzhou.github.io/tutorials/python-basic/tkinter/)