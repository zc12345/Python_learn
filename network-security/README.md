##  计算机网络安全
#### 1. RC4

> references

1. [RC4加密算法的原理及实现](http://blog.csdn.net/lc_910927/article/details/37599161)
2. [流加密RC4的C语言实现](http://gttiankai.github.io/2015/01/18/Rc4.html)
3. [RC4算法的Python实现详注](http://www.cnblogs.com/darkpig/p/5849161.html)
4. [【维基百科】RC4](https://zh.wikipedia.org/wiki/RC4)

#### 2. AES

> references

1. [【维基百科】AES](https://zh.wikipedia.org/zh-hans/%E9%AB%98%E7%BA%A7%E5%8A%A0%E5%AF%86%E6%A0%87%E5%87%86)
2. [AES加密算法的详细介绍与实现](http://blog.csdn.net/qq_28205153/article/details/55798628)
3. [AES加密算法的C++实现](http://blog.csdn.net/lisonglisonglisong/article/details/41909813)
4. [JAVA实现AES加密](http://blog.csdn.net/hbcui1984/article/details/5201247)
5. [Understanding AES & Rijndael](https://github.com/matt-wu/AES)

#### 3. PGP

> references

1. [使用GnuPG(PGP)加密信息及数字签名教程](www.williamlong.info/archives/3439.html)
2. [GnuPG使用介绍](http://blog.csdn.net/xingzouagain/article/details/52511129)

#### 4. OpenSSL

> references

1. [Download OpenSSL](https://www.openssl.org/source/)
2. [Source Code OpenSSL](https://github.com/openssl/openssl)
3. [使用 openssl 生成证书](https://www.cnblogs.com/littleatp/p/5878763.html)

#### 5. Secure Communication（安全通信）

> references

1. [Safe-Communication](https://github.com/spdv123/Safe-Communicate)
2. [python加密算法](http://blog.hszofficial.site/TutorialForPython/%E4%BF%A1%E6%81%AF%E5%AE%89%E5%85%A8/%E5%8A%A0%E5%AF%86%E7%AE%97%E6%B3%95.html)

#### 6. debug history

1. twisted 

bug report
```
0: UserWarning: You do not have a working installation of the service_identity module: 'cannot import name DNSName'. Please install it from <https://pypi.python.org/pypi/service_identity> and make sure all of its dependencies are satisfied. Without the service_identity module and a recent enough pyOpenSSL to support it, Twisted can perform only rudimentary TLS client hostname verification. Many valid certificate/hostname mappings may be rejected.
```
fixed
```shell
$ pip install service_identity --force --upgrade
```

2. twisted

bug report
```
AttributeError: 'module' object has no attribute 'OP_NO_TLSv1_1'
```
fixed
```shell
$ pip install Twisted==16.6.0
```
3. Listen port

bug report
```
twisted.internet.error.CannotListenError: Couldn't listen on any:23333: [Errno 98] Address already in use.
```
fixed
```shell
$ lsof -i TCP:23333 | grep LISTEN 
$ kill -s 9 <PID>
```
